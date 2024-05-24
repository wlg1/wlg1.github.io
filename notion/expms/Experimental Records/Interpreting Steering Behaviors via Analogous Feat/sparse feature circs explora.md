# sparse feature circs explora

[https://github.com/saprmarks/feature-circuits](https://github.com/saprmarks/feature-circuits)

- use existing circuits and perform steering/scaling on them
- look at existing code: `attribution.py, ablation.py`
    - [https://chatgpt.com/c/6589e7ef-2155-46ba-b466-704a56bba47e](https://chatgpt.com/c/6589e7ef-2155-46ba-b466-704a56bba47e)
        - what does this code do? summarize:
            
            This code defines a set of functions to compute the "patching effect" in a neural network model. The patching effect measures the change in the model's output or performance metrics when parts of the model's internal states are replaced with corresponding states from a different input (patch). The key components are:
            
            1. **Imports and Setup:**
                - Imports necessary libraries and modules.
                - Defines a named tuple `EffectOut` to store results.
                - Sets up a `DEBUGGING` flag to control some trace configurations.
            2. **_pe_attrib Function:**
                - Calculates the patching effect using an attribution method.
                - Traces the model with a clean input to determine which hidden states are tuples.
                - Traces the model with clean and patched inputs to capture hidden states, gradients, and metric values.
                - Computes the effect of the patch on the model's outputs and returns the results.
            3. **_pe_ig Function:**
                - Computes the patching effect using integrated gradients.
                - Similar to `_pe_attrib` but uses a different approach to interpolate between clean and patched inputs.
                - Traces the model with intermediate steps to calculate gradients and effects.
            4. **_pe_exact Function:**
                - Computes the exact patching effect by iterating over positions and features where the clean and patched states differ.
                - Traces the model with clean and patched inputs to capture hidden states and compute effects.
            5. **patching_effect Function:**
                - Wrapper function to call the appropriate patching effect method (`attrib`, `ig`, or `exact`) based on the specified `method`.
            6. **jvp Function:**
                - Computes Jacobian-vector products for the specified upstream and downstream submodules.
                - Traces the model to capture and modify hidden states.
                - Computes and returns sparse tensors of Jacobian-vector products.
            
            Overall, this code provides tools to analyze how changes in specific parts of a model's internal states (patches) affect its overall behavior and performance.
            
        - Why does it need to know which states are tuples
            
            The code needs to know which hidden states are tuples to correctly handle the outputs of certain submodules during tracing and patching. Here's a more detailed explanation:
            
            1. **Model Outputs Handling:**
                - Some submodules in the neural network may produce outputs that are tuples (e.g., (output, hidden_state) in recurrent neural networks).
                - If the code does not correctly identify and handle these tuple outputs, it might incorrectly process or modify the outputs, leading to errors or incorrect calculations.
            2. **Tracing and Modifying Outputs:**
                - During the tracing process, the code needs to access and modify the outputs of submodules.
                - If a submodule's output is a tuple, the code must extract and handle the appropriate element(s) within the tuple. For example, if the output is (output, hidden_state), the code might need to work specifically with `output`.
                - If the output is not a tuple, the code can directly work with the output tensor.
            3. **Ensuring Correct Computations:**
                - By identifying whether the outputs are tuples, the code ensures that it correctly applies the patching effects and computes the metrics.
                - This distinction is crucial for accurate gradient calculations and the reconstruction of hidden states.
            
            ### Practical Example
            
            Consider a submodule with an output like `(output, hidden_state)`:
            
            - **If identified correctly as a tuple:**
                - The code can access `output` for further processing while maintaining `hidden_state` intact or handling it separately if needed.
                - For instance, in the `_pe_attrib` function:
                    
                    ```python
                    if is_tuple[submodule]:
                        x = x[0]  # Extracting the actual output tensor from the tuple
                    
                    ```
                    
            - **If not identified correctly:**
                - The code might mistakenly treat the entire tuple as a tensor, leading to errors in tensor operations or incorrect patching effects.
                - This could cause issues when performing operations like `x_hat + residual` or gradient calculations.
            
            ### Summary
            
            The identification of tuple outputs ensures that the code correctly accesses, modifies, and processes the outputs of submodules. This accuracy is critical for the functions to trace the model's behavior accurately, apply patches correctly, and compute the resulting effects on the model's performance metrics.
            
        - explains each part of _pe_attrib
            
            Sure, I'll break down each part of the `_pe_attrib` function:
            
            ### Function Definition and Parameters
            
            ```python
            def _pe_attrib(
                    clean,
                    patch,
                    model,
                    submodules,
                    dictionaries,
                    metric_fn,
                    metric_kwargs=dict(),
            ):
            
            ```
            
            - **`clean`**: The clean input to the model, representing the unpatched state.
            - **`patch`**: The patched input, representing the modified state.
            - **`model`**: The neural network model being analyzed.
            - **`submodules`**: List of submodules within the model to be traced.
            - **`dictionaries`**: A dictionary mapping submodules to dictionary objects for encoding and decoding hidden states.
            - **`metric_fn`**: A function to compute performance metrics of the model.
            - **`metric_kwargs`**: Additional arguments for `metric_fn`.
            
            ### Determine Which Hidden States Are Tuples
            
            ```python
            # first run through a test input to figure out which hidden states are tuples
            is_tuple = {}
            with model.trace("_"):
                for submodule in submodules:
                    is_tuple[submodule] = type(submodule.output.shape) == tuple
            
            ```
            
            - This part determines whether the outputs of each submodule are tuples by tracing the model with a dummy input.
            
            ### Trace the Model with the Clean Input
            
            ```python
            hidden_states_clean = {}
            grads = {}
            with model.trace(clean, **tracer_kwargs):
                for submodule in submodules:
                    dictionary = dictionaries[submodule]
                    x = submodule.output
                    if is_tuple[submodule]:
                        x = x[0]
                    x_hat, f = dictionary(x, output_features=True) # x_hat implicitly depends on f
                    residual = x - x_hat
                    hidden_states_clean[submodule] = SparseAct(act=f, res=residual).save()
                    grads[submodule] = hidden_states_clean[submodule].grad.save()
                    residual.grad = t.zeros_like(residual)
                    x_recon = x_hat + residual
                    if is_tuple[submodule]:
                        submodule.output[0][:] = x_recon
                    else:
                        submodule.output = x_recon
                    x.grad = x_recon.grad
                metric_clean = metric_fn(model, **metric_kwargs).save()
                metric_clean.sum().backward()
            hidden_states_clean = {k : v.value for k, v in hidden_states_clean.items()}
            grads = {k : v.value for k, v in grads.items()}
            
            ```
            
            - Traces the model with the clean input to capture hidden states and gradients.
            - Modifies the model's outputs using encoded and decoded values (`x_hat`).
            - Stores the hidden states and gradients for each submodule.
            - Computes the metric for the clean input and performs a backward pass to get gradients.
            
            ### Trace the Model with the Patched Input (if provided)
            
            ```python
            if patch is None:
                hidden_states_patch = {
                    k : SparseAct(act=t.zeros_like(v.act), res=t.zeros_like(v.res)) for k, v in hidden_states_clean.items()
                }
                total_effect = None
            else:
                hidden_states_patch = {}
                with model.trace(patch, **tracer_kwargs), t.inference_mode():
                    for submodule in submodules:
                        dictionary = dictionaries[submodule]
                        x = submodule.output
                        if is_tuple[submodule]:
                            x = x[0]
                        x_hat, f = dictionary(x, output_features=True)
                        residual = x - x_hat
                        hidden_states_patch[submodule] = SparseAct(act=f, res=residual).save()
                    metric_patch = metric_fn(model, **metric_kwargs).save()
                total_effect = (metric_patch.value - metric_clean.value).detach()
                hidden_states_patch = {k : v.value for k, v in hidden_states_patch.items()}
            
            ```
            
            - If no patch is provided, initializes `hidden_states_patch` with zeros.
            - If a patch is provided, traces the model with the patched input to capture hidden states.
            - Computes the metric for the patched input and calculates the total effect by comparing it to the clean metric.
            
            ### Calculate Effects and Deltas
            
            ```python
            effects = {}
            deltas = {}
            for submodule in submodules:
                patch_state, clean_state, grad = hidden_states_patch[submodule], hidden_states_clean[submodule], grads[submodule]
                delta = patch_state - clean_state.detach() if patch_state is not None else -clean_state.detach()
                effect = delta @ grad
                effects[submodule] = effect
                deltas[submodule] = delta
                grads[submodule] = grad
            total_effect = total_effect if total_effect is not None else None
            
            ```
            
            - Iterates over each submodule to compute the differences (`deltas`) between patched and clean states.
            - Calculates the effect of these differences on the model's outputs using the stored gradients.
            - Stores the effects and deltas for each submodule.
            
            ### Return Results
            
            ```python
            return EffectOut(effects, deltas, grads, total_effect)
            
            ```
            
            - Returns an `EffectOut` namedtuple containing the computed effects, deltas, gradients, and total effect.
            
            ### Summary
            
            The `_pe_attrib` function traces a neural network model with clean and patched inputs to capture hidden states and gradients. It calculates the effects of patches on the model's outputs and performance metrics by comparing the differences between clean and patched states and their impact on gradients. This analysis helps in understanding how specific changes in the model's internal states influence its overall behavior.
            
        - what is model.trace
            
            The `model.trace` is not a standard method in typical PyTorch models. It appears to be part of a custom implementation or a specific library designed to trace the computations and capture the outputs, gradients, and hidden states of the submodules within a neural network model.
            
            ### Possible Implementation of `model.trace`
            
            In the context of this code, `model.trace` seems to serve the following purposes:
            
            1. **Tracing Computations**:
                - It traces the forward and backward passes to record the outputs of specified submodules.
                - It helps in identifying the hidden states produced by these submodules.
            2. **Handling Tuple Outputs**:
                - It checks whether the outputs of submodules are tuples, which is necessary for correctly accessing and modifying these outputs.
            3. **Capturing and Modifying Intermediate States**:
                - It allows the modification of the intermediate states (like `x_hat`, `residual`) during the forward pass.
                - It also enables capturing the gradients during the backward pass.
            
            ### Hypothetical Example
            
            Here's a hypothetical implementation of how `model.trace` might work:
            
            ```python
            class ModelWrapper:
                def __init__(self, model):
                    self.model = model
                    self.traces = {}
            
                def trace(self, inputs, validate=False, scan=False):
                    self.traces = {}
                    self.validate = validate
                    self.scan = scan
            
                    def hook_fn(module, input, output):
                        self.traces[module] = {'input': input, 'output': output}
            
                    hooks = []
                    for module in self.model.modules():
                        hooks.append(module.register_forward_hook(hook_fn))
            
                    with t.no_grad():
                        self.model(inputs)
            
                    for hook in hooks:
                        hook.remove()
            
                    return self
            
                def __enter__(self):
                    return self
            
                def __exit__(self, exc_type, exc_val, exc_tb):
                    pass
            
            ```
            
            ### Usage in the Code
            
            ### Checking Tuple Outputs
            
            ```python
            is_tuple = {}
            with model.trace("_"):
                for submodule in submodules:
                    is_tuple[submodule] = type(submodule.output.shape) == tuple
            
            ```
            
            - This code snippet uses `model.trace` to run a dummy input through the model and determine if the outputs of submodules are tuples.
            
            ### Tracing with Clean Input
            
            ```python
            hidden_states_clean = {}
            grads = {}
            with model.trace(clean, **tracer_kwargs):
                for submodule in submodules:
                    dictionary = dictionaries[submodule]
                    x = submodule.output
                    if is_tuple[submodule]:
                        x = x[0]
                    x_hat, f = dictionary(x, output_features=True) # x_hat implicitly depends on f
                    residual = x - x_hat
                    hidden_states_clean[submodule] = SparseAct(act=f, res=residual).save()
                    grads[submodule] = hidden_states_clean[submodule].grad.save()
                    residual.grad = t.zeros_like(residual)
                    x_recon = x_hat + residual
                    if is_tuple[submodule]:
                        submodule.output[0][:] = x_recon
                    else:
                        submodule.output = x_recon
                    x.grad = x_recon.grad
                metric_clean = metric_fn(model, **metric_kwargs).save()
                metric_clean.sum().backward()
            hidden_states_clean = {k : v.value for k, v in hidden_states_clean.items()}
            grads = {k : v.value for k, v in grads.items()}
            
            ```
            
            - Here, `model.trace` is used to capture the outputs and hidden states of submodules when the model is run with a clean input. It allows modifying these outputs and computing gradients.
            
            ### Summary
            
            `model.trace` is a custom method used for tracing the computations in the neural network model. It captures the outputs and hidden states of specified submodules, checks for tuple outputs, and facilitates modifying intermediate states during the forward pass. This functionality is crucial for the analysis performed by the `_pe_attrib` function and other related functions in the code.
            
        - what is dictionaries?
            
            In the context of the `_pe_attrib` function and the overall code, `dictionaries` appears to be a dictionary where each key is a submodule of the model and each value is an object (likely a custom class or utility) that provides methods for encoding and decoding the hidden states of those submodules.
            
            ### Purpose of `dictionaries`
            
            The `dictionaries` are used to:
            
            1. **Encode Hidden States**:
                - Convert the output of a submodule into a more compact or structured representation (features).
            2. **Decode Hidden States**:
                - Reconstruct the original output (or an approximation of it) from the encoded features.
            
            ### Structure of `dictionaries`
            
            - **Keys**: Submodules of the neural network.
            - **Values**: Dictionary objects (likely instances of a class) that provide `encode` and `decode` methods, and possibly other utilities.
            
            ### Example Usage in the Code
            
            ### Encoding and Decoding
            
            ```python
            dictionary = dictionaries[submodule]
            x = submodule.output
            if is_tuple[submodule]:
                x = x[0]
            x_hat, f = dictionary(x, output_features=True)
            residual = x - x_hat
            
            ```
            
            - **Encoding**: `dictionary(x, output_features=True)` encodes the output `x` into `x_hat` (reconstructed output) and `f` (features).
            - **Residual**: The difference between the original output `x` and the reconstructed output `x_hat` is calculated and stored as `residual`.
            
            ### Reconstructing Outputs
            
            ```python
            x_recon = x_hat + residual
            if is_tuple[submodule]:
                submodule.output[0][:] = x_recon
            else:
                submodule.output = x_recon
            
            ```
            
            - The code reconstructs the output by adding the residual back to the reconstructed output `x_hat`.
            - It then assigns this reconstructed output back to the submodule's output, handling tuple cases appropriately.
            
            ### Hypothetical Example of a Dictionary Class
            
            ```python
            class Dictionary:
                def __init__(self):
                    # Initialization code here
                    pass
            
                def encode(self, x):
                    # Code to encode x into features f
                    f = ... # some encoding logic
                    return f
            
                def decode(self, f):
                    # Code to decode features f back into x_hat
                    x_hat = ... # some decoding logic
                    return x_hat
            
                def __call__(self, x, output_features=False):
                    # Code to handle the combined encoding and optional feature output
                    f = self.encode(x)
                    x_hat = self.decode(f)
                    if output_features:
                        return x_hat, f
                    else:
                        return x_hat
            
            ```
            
            ### Summary
            
            The `dictionaries` are used to encode and decode the hidden states of the submodules within the model. This process helps in reconstructing the outputs from the encoded features and calculating the residuals, which are essential for tracing and analyzing the patching effects. Each submodule in the model has an associated dictionary object that provides methods for these operations.
            
        - `dictionaries` is a collection of SAEs, each trained after a layer (called a `submodule` here)
        - what is x_hat and residual?
            
            In the context of the code snippet:
            
            ```python
            dictionary = dictionaries[submodule]
            x = submodule.output
            if is_tuple[submodule]:
                x = x[0]
            x_hat, f = dictionary(x, output_features=True) # x_hat implicitly depends on f
            residual = x - x_hat
            ```
            
            ### What are `x_hat` and `residual`?
            
            - **`x_hat`**: This is the reconstructed output produced by the `dictionary` from the features `f`. It represents an approximation of the original output `x`.
            - **`residual`**: This is the difference between the original output `x` and the reconstructed output `x_hat`. It represents the part of the original output that could not be captured by the reconstruction process.
            
            ### Detailed Explanation
            
            ### `x_hat`
            
            - **Reconstructed Output**: `x_hat` is obtained by decoding the features `f` using the `dictionary` object. The encoding process extracts important features from the original output `x`, and the decoding process attempts to reconstruct `x` from these features.
            - **Dependency on `f`**: The reconstructed output `x_hat` implicitly depends on the features `f` because `f` contains the essential information needed to recreate `x_hat`.
            
            ### `residual`
            
            - **Difference Calculation**: The `residual` is calculated by subtracting `x_hat` from the original output `x`. Mathematically, `residual = x - x_hat`.
            - **Significance**: The `residual` captures the information that the dictionary-based encoding-decoding process could not perfectly reconstruct. It represents the error or the loss of information during the reconstruction.
            
            ### Example Scenario
            
            Imagine a scenario where the submodule's output `x` is a complex tensor representing some intermediate state in the neural network. The dictionary object tries to encode this complex tensor into a simpler feature representation `f`. Then, it decodes these features back into a reconstructed version `x_hat`.
            
            1. **Original Output (`x`)**: This could be a high-dimensional tensor output from a neural network layer.
            2. **Feature Encoding (`f`)**: The dictionary encodes `x` into a lower-dimensional or more structured feature representation.
            3. **Reconstructed Output (`x_hat`)**: The dictionary decodes the features `f` back into a tensor that approximates the original output `x`.
            4. **Residual (`residual`)**: The difference between `x` and `x_hat`, representing the reconstruction error.
            
            ### Visual Representation
            
            ```
            Original Output (x) --> [ Encoding ] --> Features (f) --> [ Decoding ] --> Reconstructed Output (x_hat)
                               |                                                         ^
                               |                                                         |
                               +----------------------- Residual (x - x_hat) -------------+
            
            ```
            
            ### Purpose in the Code
            
            The reconstruction and residual calculation serve several purposes:
            
            - **Analyzing Reconstruction Quality**: By examining the residual, one can understand how much information is lost during the encoding-decoding process.
            - **Gradient Calculations**: The residual plays a role in the gradient calculations during backpropagation, as the code ensures gradients flow correctly through the reconstructed outputs.
            - **Effect Attribution**: Understanding the difference between the original and reconstructed outputs helps in attributing the effects of specific patches in the model's internal states.
            
            In summary, `x_hat` is the reconstructed output, and `residual` is the difference between the original and reconstructed outputs, capturing the information loss during reconstruction. These concepts are crucial for analyzing the internal behavior of the model and understanding the impact of patches on the model's performance.
            

---

[sparse_feature_circuits_explora.ipynb](https://colab.research.google.com/drive/1lnTXl1-zvrIbGpupijxPO7s52uxNJNaz)

- what does this do: `git submodule update --init`
    
    The command `git submodule update --init` is used to initialize, fetch, and checkout the correct versions of the submodules in a Git repository. Here's a breakdown of what each part does:
    
    1. **`git submodule`**: This command deals with Git submodules, which are repositories nested inside another Git repository. Submodules are often used to include external projects within a main project.
    2. **`update`**: This updates the submodules to the commit specified in the main repository. It ensures that each submodule is checked out to the correct commit as recorded in the superproject.
    3. **`-init`**: This initializes the submodules. It is needed the first time you clone a repository with submodules or when a new submodule is added. This option makes sure that the submodules are cloned into the right place and initialized.
    
    In summary, `git submodule update --init` ensures that all the submodules are properly initialized, fetched, and checked out to the correct commit specified in the main repository. It is typically used after cloning a repository that contains submodules or when new submodules have been added to the repository.
    

This clones the link at comment, [**dictionary_learning @ 614883f](https://github.com/saprmarks/dictionary_learning/tree/614883f9476613e7c1c48b951cd3947451e1f534) , to the repo**

- ISSUE: `!bash scripts/get_circuit.sh rc_train 0.1 0.01 none 6 10`
    
    ```jsx
    Traceback (most recent call last):
      File "/content/feature-circuits/circuit.py", line 477, in <module>
        dictionaries[embed] = AutoEncoder.from_pretrained(
    AttributeError: type object 'AutoEncoder' has no attribute 'from_pretrained'
    ```
    
    dictionary_learning repo put AutoEncoder in the [dictionary.py](http://dictionary.py) file
    
    <
    
    TRY: change `from dictionary_learningimport AutoEncoder`
    
    to `from dictionary_learning.dictionary import AutoEncoder`
    
    RESULT: doesn’t work
    
    <
    
    POSS SOLN: sparse_feature_circuits loads an old vers of dictionary_learning before from_pretrained was coded. Load dictionary repo direclty instead of !git submodule update --init
    
    RESULT: Fixed
    

[https://github.com/saprmarks/feature-circuits/blob/main/scripts/get_circuit.sh](https://github.com/saprmarks/feature-circuits/blob/main/scripts/get_circuit.sh)

`rc_train`  is the dataset arg that `save_basename` (used to make the circuit filename to save in) is extracted from. The other args after are node thres, edge thres, aggr. The last two are example len and dict id.

Must create `circuits` result folder if not exist, else can’t find output folder

---

clusters:

[https://feature-circuits.xyz/](https://feature-circuits.xyz/)

a cluster’s features:

[https://www.neuronpedia.org/quick-list?name=Cluster 333 circuit features&features=](https://www.neuronpedia.org/quick-list?name=Cluster%20333%20circuit%20features&features=%5B%7B%22modelId%22%3A%20%22pythia-70m-deduped%22%2C%20%22layer%22%3A%20%22e-res-sm%22%2C%20%22index%22%3A%20%222123%22%7D%2C%20%7B%22modelId%22%3A%20%22pythia-70m-deduped%22%2C%20%22layer%22%3A%20%22e-res-sm%22%2C%20%22index%22%3A%20%223014%22%7D%2C%20%7B%22modelId%22%3A%20%22pythia-70m-deduped%22%2C%20%22layer%22%3A%20%22e-res-sm%22%2C%20%22index%22%3A%20%2211193%22%7D%2C%20%7B%22modelId%22%3A%20%22pythia-70m-deduped%22%2C%20%22layer%22%3A%20%22e-res-sm%22%2C%20%22index%22%3A%20%2213736%22%7D%2C%20%7B%22modelId%22%3A%20%22pythia-70m-deduped%22%2C%20%22layer%22%3A%20%22e-res-sm%22%2C%20%22index%22%3A%20%2215975%22%7D%2C%20%7B%22modelId%22%3A%20%22pythia-70m-deduped%22%2C%20%22layer%22%3A%20%22e-res-sm%22%2C%20%22index%22%3A%20%2216124%22%7D%2C%20%7B%22modelId%22%3A%20%22pythia-70m-deduped%22%2C%20%22layer%22%3A%20%22e-res-sm%22%2C%20%22index%22%3A%20%2216953%22%7D%2C%20%7B%22modelId%22%3A%20%22pythia-70m-deduped%22%2C%20%22layer%22%3A%20%22e-res-sm%22%2C%20%22index%22%3A%20%2219985%22%7D%2C%20%7B%22modelId%22%3A%20%22pythia-70m-deduped%22%2C%20%22layer%22%3A%20%22e-res-sm%22%2C%20%22index%22%3A%20%2220132%22%7D%2C%20%7B%22modelId%22%3A%20%22pythia-70m-deduped%22%2C%20%22layer%22%3A%20%22e-res-sm%22%2C%20%22index%22%3A%20%2220642%22%7D%2C%20%7B%22modelId%22%3A%20%22pythia-70m-deduped%22%2C%20%22layer%22%3A%20%22e-res-sm%22%2C%20%22index%22%3A%20%2226100%22%7D%2C%20%7B%22modelId%22%3A%20%22pythia-70m-deduped%22%2C%20%22layer%22%3A%20%22e-res-sm%22%2C%20%22index%22%3A%20%2226333%22%7D%2C%20%7B%22modelId%22%3A%20%22pythia-70m-deduped%22%2C%20%22layer%22%3A%20%22e-res-sm%22%2C%20%22index%22%3A%20%2231637%22%7D%2C%20%7B%22modelId%22%3A%20%22pythia-70m-deduped%22%2C%20%22layer%22%3A%20%22e-res-sm%22%2C%20%22index%22%3A%20%2232223%22%7D%2C%20%7B%22modelId%22%3A%20%22pythia-70m-deduped%22%2C%20%22layer%22%3A%20%22e-res-sm%22%2C%20%22index%22%3A%20%2232372%22%7D%2C%20%7B%22modelId%22%3A%20%22pythia-70m-deduped%22%2C%20%22layer%22%3A%20%220-att-sm%22%2C%20%22index%22%3A%20%226052%22%7D%2C%20%7B%22modelId%22%3A%20%22pythia-70m-deduped%22%2C%20%22layer%22%3A%20%220-att-sm%22%2C%20%22index%22%3A%20%228683%22%7D%2C%20%7B%22modelId%22%3A%20%22pythia-70m-deduped%22%2C%20%22layer%22%3A%20%220-att-sm%22%2C%20%22index%22%3A%20%2210466%22%7D%2C%20%7B%22modelId%22%3A%20%22pythia-70m-deduped%22%2C%20%22layer%22%3A%20%220-att-sm%22%2C%20%22index%22%3A%20%2213727%22%7D%2C%20%7B%22modelId%22%3A%20%22pythia-70m-deduped%22%2C%20%22layer%22%3A%20%220-mlp-sm%22%2C%20%22index%22%3A%20%22462%22%7D%2C%20%7B%22modelId%22%3A%20%22pythia-70m-deduped%22%2C%20%22layer%22%3A%20%220-mlp-sm%22%2C%20%22index%22%3A%20%221620%22%7D%2C%20%7B%22modelId%22%3A%20%22pythia-70m-deduped%22%2C%20%22layer%22%3A%20%220-mlp-sm%22%2C%20%22index%22%3A%20%226129%22%7D%2C%20%7B%22modelId%22%3A%20%22pythia-70m-deduped%22%2C%20%22layer%22%3A%20%220-mlp-sm%22%2C%20%22index%22%3A%20%226919%22%7D%2C%20%7B%22modelId%22%3A%20%22pythia-70m-deduped%22%2C%20%22layer%22%3A%20%220-mlp-sm%22%2C%20%22index%22%3A%20%2213365%22%7D%2C%20%7B%22modelId%22%3A%20%22pythia-70m-deduped%22%2C%20%22layer%22%3A%20%220-mlp-sm%22%2C%20%22index%22%3A%20%2215373%22%7D%2C%20%7B%22modelId%22%3A%20%22pythia-70m-deduped%22%2C%20%22layer%22%3A%20%220-mlp-sm%22%2C%20%22index%22%3A%20%2215817%22%7D%2C%20%7B%22modelId%22%3A%20%22pythia-70m-deduped%22%2C%20%22layer%22%3A%20%220-mlp-sm%22%2C%20%22index%22%3A%20%2217143%22%7D%2C%20%7B%22modelId%22%3A%20%22pythia-70m-deduped%22%2C%20%22layer%22%3A%20%220-mlp-sm%22%2C%20%22index%22%3A%20%2217199%22%7D%2C%20%7B%22modelId%22%3A%20%22pythia-70m-deduped%22%2C%20%22layer%22%3A%20%220-mlp-sm%22%2C%20%22index%22%3A%20%2222678%22%7D%2C%20%7B%22modelId%22%3A%20%22pythia-70m-deduped%22%2C%20%22layer%22%3A%20%220-mlp-sm%22%2C%20%22index%22%3A%20%2231810%22%7D%2C%20%7B%22modelId%22%3A%20%22pythia-70m-deduped%22%2C%20%22layer%22%3A%20%220-res-sm%22%2C%20%22index%22%3A%20%224074%22%7D%2C%20%7B%22modelId%22%3A%20%22pythia-70m-deduped%22%2C%20%22layer%22%3A%20%220-res-sm%22%2C%20%22index%22%3A%20%2212967%22%7D%2C%20%7B%22modelId%22%3A%20%22pythia-70m-deduped%22%2C%20%22layer%22%3A%20%220-res-sm%22%2C%20%22index%22%3A%20%2222281%22%7D%2C%20%7B%22modelId%22%3A%20%22pythia-70m-deduped%22%2C%20%22layer%22%3A%20%220-res-sm%22%2C%20%22index%22%3A%20%2225923%22%7D%2C%20%7B%22modelId%22%3A%20%22pythia-70m-deduped%22%2C%20%22layer%22%3A%20%221-res-sm%22%2C%20%22index%22%3A%20%225165%22%7D%2C%20%7B%22modelId%22%3A%20%22pythia-70m-deduped%22%2C%20%22layer%22%3A%20%221-res-sm%22%2C%20%22index%22%3A%20%2210491%22%7D%2C%20%7B%22modelId%22%3A%20%22pythia-70m-deduped%22%2C%20%22layer%22%3A%20%221-res-sm%22%2C%20%22index%22%3A%20%2214781%22%7D%2C%20%7B%22modelId%22%3A%20%22pythia-70m-deduped%22%2C%20%22layer%22%3A%20%221-res-sm%22%2C%20%22index%22%3A%20%2217286%22%7D%2C%20%7B%22modelId%22%3A%20%22pythia-70m-deduped%22%2C%20%22layer%22%3A%20%221-res-sm%22%2C%20%22index%22%3A%20%2232084%22%7D%2C%20%7B%22modelId%22%3A%20%22pythia-70m-deduped%22%2C%20%22layer%22%3A%20%222-att-sm%22%2C%20%22index%22%3A%20%2222904%22%7D%2C%20%7B%22modelId%22%3A%20%22pythia-70m-deduped%22%2C%20%22layer%22%3A%20%222-res-sm%22%2C%20%22index%22%3A%20%223340%22%7D%2C%20%7B%22modelId%22%3A%20%22pythia-70m-deduped%22%2C%20%22layer%22%3A%20%222-res-sm%22%2C%20%22index%22%3A%20%226996%22%7D%2C%20%7B%22modelId%22%3A%20%22pythia-70m-deduped%22%2C%20%22layer%22%3A%20%222-res-sm%22%2C%20%22index%22%3A%20%228028%22%7D%2C%20%7B%22modelId%22%3A%20%22pythia-70m-deduped%22%2C%20%22layer%22%3A%20%222-res-sm%22%2C%20%22index%22%3A%20%2211811%22%7D%2C%20%7B%22modelId%22%3A%20%22pythia-70m-deduped%22%2C%20%22layer%22%3A%20%222-res-sm%22%2C%20%22index%22%3A%20%2228096%22%7D%2C%20%7B%22modelId%22%3A%20%22pythia-70m-deduped%22%2C%20%22layer%22%3A%20%223-mlp-sm%22%2C%20%22index%22%3A%20%222814%22%7D%2C%20%7B%22modelId%22%3A%20%22pythia-70m-deduped%22%2C%20%22layer%22%3A%20%223-res-sm%22%2C%20%22index%22%3A%20%22884%22%7D%2C%20%7B%22modelId%22%3A%20%22pythia-70m-deduped%22%2C%20%22layer%22%3A%20%223-res-sm%22%2C%20%22index%22%3A%20%227128%22%7D%2C%20%7B%22modelId%22%3A%20%22pythia-70m-deduped%22%2C%20%22layer%22%3A%20%223-res-sm%22%2C%20%22index%22%3A%20%2223953%22%7D%2C%20%7B%22modelId%22%3A%20%22pythia-70m-deduped%22%2C%20%22layer%22%3A%20%224-mlp-sm%22%2C%20%22index%22%3A%20%2230172%22%7D%2C%20%7B%22modelId%22%3A%20%22pythia-70m-deduped%22%2C%20%22layer%22%3A%20%224-res-sm%22%2C%20%22index%22%3A%20%221454%22%7D%2C%20%7B%22modelId%22%3A%20%22pythia-70m-deduped%22%2C%20%22layer%22%3A%20%224-res-sm%22%2C%20%22index%22%3A%20%226798%22%7D%2C%20%7B%22modelId%22%3A%20%22pythia-70m-deduped%22%2C%20%22layer%22%3A%20%224-res-sm%22%2C%20%22index%22%3A%20%2213027%22%7D%2C%20%7B%22modelId%22%3A%20%22pythia-70m-deduped%22%2C%20%22layer%22%3A%20%224-res-sm%22%2C%20%22index%22%3A%20%2226145%22%7D%2C%20%7B%22modelId%22%3A%20%22pythia-70m-deduped%22%2C%20%22layer%22%3A%20%225-att-sm%22%2C%20%22index%22%3A%20%2211218%22%7D%2C%20%7B%22modelId%22%3A%20%22pythia-70m-deduped%22%2C%20%22layer%22%3A%20%225-res-sm%22%2C%20%22index%22%3A%20%227552%22%7D%2C%20%7B%22modelId%22%3A%20%22pythia-70m-deduped%22%2C%20%22layer%22%3A%20%225-res-sm%22%2C%20%22index%22%3A%20%2213295%22%7D%2C%20%7B%22modelId%22%3A%20%22pythia-70m-deduped%22%2C%20%22layer%22%3A%20%225-res-sm%22%2C%20%22index%22%3A%20%2221236%22%7D%5D)