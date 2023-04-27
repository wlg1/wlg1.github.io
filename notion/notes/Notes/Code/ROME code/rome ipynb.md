# rome.ipynb

[https://colab.research.google.com/drive/1fL7ZmbtaGJJX7tS7Ix8_lVAJAtrgSs5r#scrollTo=c5820200](https://colab.research.google.com/drive/1fL7ZmbtaGJJX7tS7Ix8_lVAJAtrgSs5r#scrollTo=c5820200)

- !(stat -t /usr/local/lib/*/dist-packages/google/colab > /dev/null 2>&1) && exit
    
    ```bash
    !(stat -t /usr/local/lib/*/dist-packages/google/colab > /dev/null 2>&1) && exit
    ```
    
    stat -t : Check status of file path (-t displays output in tab format)
    
    The **`> /dev/null 2>&1`** portion of a command is used to redirect the output of a command to the null device, which discards the output and prevents it from being displayed on the screen or captured in a file. The **`2>&1`** redirects standard error (stderr) to the same location as standard output (stdout). So both types of output will be discarded by the null device.
    
     && exit : if prev command executes with success status (file dir exists), then exit this shell session
    
    [Bash](../../CS%20&%20SWE%20f7436b5aff924c04aa569007bb061038/Bash%202a08c45ec15548dc968f872461395b68.md) 
    

### Requests

- Q: what does this do?
try:
    with torch.no_grad():
        for k, v in orig_weights.items(): 
…..
    
    <
    
    ```python
    try:
        with torch.no_grad():
            for k, v in orig_weights.items():
                nethook.get_parameter(model, k)[...] = v
        print("Original model restored")
    except NameError as e:
        print(f"No model weights to restore: {e}")
    ```
    
    This code attempts to restore the weights of a PyTorch model to their original values.
    
    The **`torch.no_grad()`** context manager is used to disable gradient calculation during the weight restoration process, which can help to save memory and speed up the process.
    
    - When to use torch.no_grad()?
        
        [https://www.notion.so/PyTorch-2a665e7d823b4f58b3226e98d4de3a01?pvs=4#0d5097eb24914639863d352d2acf7728](../../CS%20&%20SWE%20f7436b5aff924c04aa569007bb061038/PyTorch%202a665e7d823b4f58b3226e98d4de3a01.md)
        
    
    The code iterates through the items in the **`orig_weights`** dictionary, which presumably contains the original values of the model's weights. For each weight, it uses the **`nethook.get_parameter`** function from the **`nethook`** library to retrieve the corresponding parameter from the model and assign it the value stored in the **`orig_weights`** dictionary. The **`...`** syntax is used to assign the values in-place, which can also help to save memory.
    
    - What is nethook?
        
        [https://www.notion.so/PyTorch-2a665e7d823b4f58b3226e98d4de3a01?pvs=4#ad85ef4e90c04fb4b72f4ad460a23e6a](../../CS%20&%20SWE%20f7436b5aff924c04aa569007bb061038/PyTorch%202a665e7d823b4f58b3226e98d4de3a01.md)
        
        **`nethook`** is a library in PyTorch that provides tools for manipulating and analyzing neural network models at a low level. It allows you to easily access the internal parameters, intermediate activations, and gradients of a neural network model during its forward and backward passes.
        
        In particular, the **`nethook.get_parameter`** function is used to retrieve the parameter tensor of a PyTorch model given its name. This is useful for manipulating the parameters of a model, such as restoring them to their original values, as in the example code you provided.
        
        **`nethook`** also provides other functions for hooking into the forward and backward passes of a model, such as **`nethook.InstrumentedModel`** and **`nethook.Callbacks`**. These functions can be used for a variety of purposes, such as visualizing the activations of a model during training, debugging gradient computations, and implementing custom loss functions.
        
        Overall, **`nethook`** is a powerful tool for analyzing and manipulating PyTorch models at a low level, and is particularly useful for research and experimentation in deep learning.
        
    - how is nethook different from hook?
        
        In PyTorch, both **`nethook`** and **`hook`** are used to intercept and modify the output of a neural network model during its forward pass. However, there are some key differences between the two.
        
        **`hook`** is a PyTorch function that allows you to register a hook function on a specific module or layer of a PyTorch model. The hook function is called every time the module or layer produces an output, and can be used to modify or analyze the output. The main limitation of **`hook`** is that it only allows you to intercept the output of a specific module or layer, and cannot access other intermediate activations or the gradients of the model.
        
        On the other hand, **`nethook`** is a library that provides more fine-grained control over the outputs of a PyTorch model. It allows you to access the internal parameters, intermediate activations, and gradients of a model during its forward and backward passes. This allows you to manipulate or analyze the model at a much deeper level than with **`hook`**. **`nethook`** also provides tools for visualizing and debugging the internal state of a model, as well as implementing custom loss functions and other advanced features.
        
        Overall, **`hook`** is useful for simple cases where you only need to intercept the output of a specific module or layer, while **`nethook`** is more powerful and flexible, and is particularly useful for research and experimentation in deep learning.
        
    - what's a hook function?
        
        a function that can be registered on a specific module or layer 
        
        - what does it mean for a function be registered on a module?
            
            the function will be called every time the module is used during a forward or backward pass. When the module is used during a forward or backward pass, the hook function will be called (outputs for fwd, gradients for bwd)
            
            By registering a function on a module, you can intercept and modify the behavior of the module during a forward or backward pass.
            
            the function will be called every time the module is used, which can be computationally expensive.
            
        - Visualizing the activations of a neural network model during its forward pass
        - Debugging gradient computations during the backward pass
        - Implementing custom loss functions or regularization techniques
        - Extracting intermediate representations from a neural network for use in downstream tasks such as feature extraction or transfer learning.
    
    If the weight restoration process is successful, the code prints "Original model restored". If there are no weights to restore, meaning that **`orig_weights`** is empty or undefined, the code prints a message indicating that there are no model weights to restore.
    
    Overall, this code can be useful for resetting the weights of a PyTorch model to their original values after they have been modified during training or testing.
    

---

Old Fact → New Fact: Change using the following template:

```python
request = [
    {
        "prompt": "{} was the founder of",
        "subject": "Steve Jobs",
        "target_new": {"str": "Microsoft"},
    }
]
```

Then run it through this:

```python
model_new, orig_weights = demo_model_editing(
    model, tok, request, generation_prompts, alg_name=ALG_NAME
)
```