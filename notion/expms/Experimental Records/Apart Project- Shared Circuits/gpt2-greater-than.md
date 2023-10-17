# gpt2-greater-than

Found issues with current circuit finding code; results don't match greater-than paper. Check how greater-than paper code worked. Explain-the-code plugin on: https://github.com/hannamw/gpt2-greater-than

[https://chat.openai.com/c/42a21300-9655-4dc6-8f04-078ab9e2eeef](https://chat.openai.com/c/42a21300-9655-4dc6-8f04-078ab9e2eeef)

It doesn’t get the right code! ChatWithCode (prev called ChatWithGit) also fails. It probably can only analyze your public repo, not others. But it failed on my public repos too. AsktheCode can’t work with private. However, this appears to have an error if you use it with other plugins; if you use it by itself and give the repo link THEN REPO FILE LINKS it can get the right code:

[https://chat.openai.com/c/324b6d48-1d3c-4a0f-8e8f-d01b662b9ddd](https://chat.openai.com/c/324b6d48-1d3c-4a0f-8e8f-d01b662b9ddd)

- How does the dataset code work? Describe the flow of its function calls for creating a dataset, then describe how this dataset is used by circuit_discovery.py
    
    Let's break down the flow of the dataset creation and its usage in `circuit_discovery.py`:
    
    ### Dataset Creation in `dataset.py`:
    
    1. **Initialization**: The `YearDataset` class is initialized with parameters such as the years to sample from, the number of samples, a list of nouns, a tokenizer, and other optional parameters.
    2. **Sentence Generation**: During initialization, the dataset generates "good" (correctly formatted) and "bad" (incorrectly formatted) sentences based on the provided nouns and years.
    3. **Tokenization**: The generated sentences are tokenized using the provided tokenizer to create `good_toks` and `bad_toks`.
    4. **Dataset Length**: The `__len__` method returns the number of samples in the dataset.
    
    ### Usage in `circuit_discovery.py`:
    
    1. **Imports**: The script imports necessary modules and functions, including the `YearDataset` from `dataset.py`.
    2. **Loading the Base Model**: The GPT-2 small model is loaded.
    3. **Creating the Dataset**:
        - Valid years are retrieved using the `get_valid_years` function.
        - The `YearDataset` is instantiated with the valid years, a set number of samples (490), a list of potential nouns, and the tokenizer.
        - The dataset is balanced, and the device is set to CUDA.
    4. **Model Splitting**: The GPT-2 model is split for visualization purposes.
    5. **Sampling and Evaluation**: Two short functions, `se` and `sec`, are defined to sample and evaluate the model.
    6. **Visualization**: The normal behavior of the model is visualized.
    7. **Iterative Path Patching**: The script uses iterative path patching to identify important nodes in the model's architecture. This is done using various matcher extenders.
    8. **Attention Patterns**: The attention patterns of the model are retrieved and visualized.
    9. **Logit Lens Analysis**: The script examines the model's behavior using logit lens for various modules.
    10. **Path Patching**: The model is patched using the `path_patching` function to modify its behavior.
    11. **Visualization**: The behavior of the patched model is visualized.
    
    In summary, the `dataset.py` script is responsible for generating a dataset of correctly and incorrectly formatted year-related sentences. This dataset is then used in `circuit_discovery.py` to analyze and visualize the behavior of the GPT-2 model, identify important nodes in its architecture, and modify its behavior using path patching.
    

---

See how much you can put circuit_discovery.py in colab; try using rust (cannot do anything w/o it, I think):

[https://colab.research.google.com/drive/1JMGEszpjlgpjLvIk21o1fgb2lVuC_Tpq](https://colab.research.google.com/drive/1JMGEszpjlgpjLvIk21o1fgb2lVuC_Tpq)

[https://chat.openai.com/c/3860633f-097f-4459-ab5d-9da13ea6ae44](https://chat.openai.com/c/3860633f-097f-4459-ab5d-9da13ea6ae44)

in colab, when loading a file's functions, if the file imports contain the string "rust" in its package, write code to skip over it. I meant like "from utils import", and [utils.py](http://utils.py/) has "import rust_circuit"

Is there a way to use rust and this repo in a colab notebook?:
[https://github.com/redwoodresearch/rust_circuit_public/tree/master](https://github.com/redwoodresearch/rust_circuit_public/tree/master)

ISSUE: importing greater-than files requires being in the repo folder. but then must import folders-within-folders of rust_circuit, and can’t change that code. 

```latex
from rust_circuit.ui import cui
from rust_circuit.ui.very_named_tensor import VeryNamedTensor
from rust_circuit.causal_scrubbing.hypothesis import corr_root_matcher
```

rust_circuit.ui is in rust_circuit_public/python/.

TRY: move rust_circuit to same folder as repo

```
# create a symbolic link to reference that folder with the desired name:
!ln -s rust_circuit_public/python/rust_circuit rc
```

compile rust with maturin:

[https://chat.openai.com/c/bfc14465-951d-4bf9-aea4-2e08f092d7a1](https://chat.openai.com/c/bfc14465-951d-4bf9-aea4-2e08f092d7a1)

must cd into rust_circuit_public w/ Cargo.toml to do `!maturin dev`

YOU MUST do this in a python env; cannot use colab

convert the following steps to be used in colab: (copy README) [https://github.com/redwoodresearch/rust_circuit_public/tree/master](https://github.com/redwoodresearch/rust_circuit_public/tree/master)

---

(issue with this paper's code appears to be with how corrupted dataset of greater-than was defined, so work on fixing that. now using simpler version of code and issues is almost fixed)