# causal_trace.ipynb

[https://colab.research.google.com/drive/1YXtNHM2PMTOEdKGdJSI0wcOLj2e--omX](https://colab.research.google.com/drive/1YXtNHM2PMTOEdKGdJSI0wcOLj2e--omX)

### **Causal Tracing**

predict_token(): Input (s, r) —> Output (o)

<<<

```python
noise_level = 3 * collect_embedding_std(mt, [k["subject"] for k in knowns])
```

- Details
    
    Each k is a dict. k["subject"] gets the subject. 
    
- collect_embedding_std(): receives a **`ModelAndTokenizer`** instance **`mt`** and a list of tokens to compute the standard deviation of their embeddings.
    
    ```python
    def collect_embedding_std(mt, subjects):
        alldata = []
        for s in subjects:
    				# create a dictionary of inputs suitable for the loaded model.
            inp = make_inputs(mt.tokenizer, [s])
    				# collect embeddings t.output[0] for the encoded token from model
            with nethook.Trace(mt.model, layername(mt.model, 0, "embed")) as t:
                mt.model(**inp)
                alldata.append(t.output[0])
        alldata = torch.cat(alldata)
        noise_level = alldata.std().item()
        return noise_level
    ```
    
       layername(model, layer_index, module_name): 
    
    - layer_index = 0 since the embedding layer is the first layer in the mode
    
- Why use stddev is 3 times? Why not 2 or another?
    
    This is likely because it is a reasonable heuristic to provide sufficient perturbation to the input embeddings to cause a significant deviation in the model's output, while avoiding overly large perturbations that may cause the input to be completely unrecognizable. the choice of noise level can be tuned empirically for a given model and task
    

---

### **Tracing a single location**

[Hidden States](../../Neural%20Networks%20e6abb23474464e098117dced189fb7bb/Hidden%20States%20db3887268cff4dbebb92c9f61ad52485.md) 

- **`trace_with_patch`()**
    
    ```python
    with torch.no_grad(), nethook.TraceDict(
            model,
            [embed_layername] + list(patch_spec.keys()) + additional_layers,
            edit_output=patch_rep,
        ) as td:
            outputs_exp = model(**inp)
    ```
    
    utils.nethook.TraceDict(OrderedDict, contextlib.AbstractContextManager))
    
    TraceDict is a subclass of OrderedDict and an abstract context manager.
    
    - What is a context manager?
        
        In Python, a context manager is an object that defines the methods `__enter__` and `__exit__`, which can be used with the `with` statement to manage resources and handle exceptions. When a code block is executed within a `with` statement, the context manager's `__enter__` method is called before the block, and its `__exit__` method is called after the block (even if an exception occurs).
        
        Context managers are commonly used to manage files, network connections, locks, and other resources that require setup and cleanup actions. By using a context manager, you can ensure that resources are properly cleaned up and released, even if an error occurs or the block is exited prematurely.
        
        Python provides several built-in context managers, such as the `open` function for file I/O and the `threading.Lock` class for thread synchronization. You can also create your own context managers by defining a class with `__enter__` and `__exit__` methods, or by using the `contextlib` module to define a context manager function or decorator.
        
    - How is edit_output=patch_rep, used in the tracedict code? Provide an example
        
        `edit_output=patch_rep` is used in the `TraceDict` context manager to modify the output of certain layers during the forward pass of the network.
        
        In the provided code, `patch_rep` is a function that takes the output of a layer and the layer name as arguments and returns the modified output. The `TraceDict` context manager calls this function on the specified layers and passes the modified output through the rest of the network.
        
        Here's an example to illustrate how `edit_output=patch_rep` is used:
        
        Suppose we have a neural network that consists of three layers: an embedding layer, a hidden layer, and an output layer. We want to modify the output of the hidden layer by adding noise to certain tokens in the embedding layer.
        
        We can use `TraceDict` to trace the output of the embedding layer and the hidden layer, and pass the output of the embedding layer through the `patch_rep` function to add noise to the specified tokens:
        
        - What does it mean to trace the output?
            
            Tracing the output of a neural network means intercepting and storing the output of selected layers during the forward pass of the network. 
            
        
        ```python
        from nethook import TraceDict, trace_modules
        import torch
        
        class MyModel(torch.nn.Module):
            def __init__(self):
                super(MyModel, self).__init__()
                self.embedding = torch.nn.Embedding(100, 128)
                self.hidden = torch.nn.Linear(128, 64)
                self.output = torch.nn.Linear(64, 10)
        
            def forward(self, x):
                x = self.embedding(x)
                x = self.hidden(x)
                x = self.output(x)
                return x
        
        model = MyModel()
        
        # Trace the output of the embedding and hidden layers, and modify the output of the embedding layer
        with TraceDict(model, ['embedding', 'hidden'], edit_output=patch_rep) as td:
            x = torch.randint(0, 100, (32, 10))
            output = model(x)
            embedding_output = td['embedding'].output
            hidden_output = td['hidden'].output
        
        ```
        
        In the above code, `edit_output=patch_rep` tells `TraceDict` to use the `patch_rep` function to modify the output of the `embedding` layer. `embedding_output` is the modified output of the `embedding` layer, and `hidden_output` is the output of the `hidden` layer after passing through the modified `embedding` layer.
        
    
    ```python
    class TraceDict(OrderedDict, contextlib.AbstractContextManager):
    	...
    	for is_last, layer in flag_last_unseen(layers):
          self[layer] = Trace(..., edit_output=edit_output,...)
    ```
    
    ```python
    class Trace(contextlib.AbstractContextManager):
    	...
    	if edit_output:
          output = invoke_with_optional_args(
              edit_output, output=output, layer=self.layer
          )
    ```
    
    - **`invoke_with_optional_args`(fn, *args, **kwargs)**
        
        The function `invoke_with_optional_args` is a utility function that allows a caller to pass extra arguments to a function without requiring the callee to accept them.
        
        - What are the caller and callee?
            
            In software development, a "caller" is the piece of code that invokes or "calls" a function or method, while a "callee" is the function or method being called.
            
            For example, if we have a Python function called `print_hello()` and we call it from another function `main()`, then `main()` is the caller and `print_hello()` is the callee.
            
            Here's an example code snippet to illustrate:
            
            ```
            def print_hello():
                print("Hello, world!")
            
            def main():
                print_hello()
            
            main()  # Here, main() is the caller and print_hello() is the callee
            
            ```
            
        
        When a function is called with arguments, the caller can provide the arguments by name or by position. Sometimes, a caller might want to provide extra arguments that the function doesn't expect or accept. Similarly, a function might be updated to accept new arguments in the future, but existing callers should still work without changing their code.
        
        `invoke_with_optional_args` handles these cases by inspecting the function's argument list and passing only the arguments that the function expects. It prioritizes arguments that match by name, then passes any remaining non-name-matched arguments by position. If the caller provides extra arguments that the function cannot accept, those arguments are not passed, and if the function requires extra arguments that the caller cannot provide, a `TypeError` is raised.
        
    
    - **`[embed_layername] + list(patch_spec.keys()) + additional_layers,`**
        
        This is a list of layer names to trace during the computation of a neural network.
        
        `embed_layername` is a variable that holds the name of the embedding layer in the network.
        
        `patch_spec` is a dictionary that holds the names of layers that need to be patched. The keys of this dictionary are the names of the layers, and the values are lists of indices of neurons that need to be patched.
        
        `additional_layers` is a list of additional layer names to trace, which are provided by the user.
        
        The code is concatenating these three lists using the `+` operator to create a final list of layer names to trace during the computation of the neural network.
        
    
    - `def patch_rep(x, layer):`
        
        This is a function called `patch_rep`, which is used to apply the intervention of adding noise to the input and restoring hidden states.
        
        When called, it takes two arguments:
        
        - `x`: The tensor representation of a hidden state for a batch of inputs.
        - `layer`: The name of the layer for which this function is applied.
        
        If the layer is the embedding layer, it applies the intervention of adding noise to the tokens specified by `tokens_to_mix` (a tuple that indicates the start and end indices of the range of tokens to corrupt). It adds noise by drawing from a Gaussian distribution with zero mean and standard deviation equal to `noise` multiplied by the standard deviation of the embeddings.
        
        If the layer is not the embedding layer and it is specified in `patch_spec` (a dictionary that maps layer names to lists of token indices), it restores the uncorrupted hidden state for the selected tokens by copying the state of the uncorrupted run (i.e., the zeroth element of the batch) to the corrupted runs (i.e., elements 1 to the end of the batch) at the specified token indices.
        
        Finally, it returns the tensor `x`.
        

---

### **Scanning all locations**

calculate_hidden_flow():

<<<

Each layer has multiple hidden states, one for each token in the input sequence.

This loops over each hidden state, which is identified by (token, layer):

`trace_important_states()`

- ntoks
    
    ```python
    ntoks = inp["input_ids"].shape[1]
    ```
    
    **`inp["input_ids"]`** is a tensor of shape **`(batch_size, seq_length)`**
    
    Thus, ntoks is the number of tokens in the input sequence.
    

`trace_important_states()` calls `trace_with_patch(…, states_to_patch, …)` on every layer, such that  `states_to_patch = (curr_tok, curr_layer).` 

This is why we don’t have to loop through every neuron. For a given token, we are corrupting entire LAYERS OUTPUTS. 

This is like how each layer is a hidden (latent) space with neurons as basis. The hidden ‘state’ is a point in the hidden space.