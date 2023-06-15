# PyTorch

- When to use torch.no_grad()?
    
    Whenever you’re not training.
    
    **`torch.no_grad()`** is a PyTorch context manager that disables gradient computation. It is typically used in situations where you do not need to compute gradients, such as when you are evaluating a trained neural network on a test set or making predictions on new data.
    
    When you call a PyTorch function that requires gradients to be computed, PyTorch keeps track of all the operations that were performed so that it can compute the gradients later using backpropagation. This tracking can be computationally expensive, especially if you are performing many small operations.
    
    By using **`torch.no_grad()`**, you can tell PyTorch to skip this tracking and save on computation. This can be particularly useful when you are working with large datasets or complex models.
    
    Here is an example of how to use **`torch.no_grad()`**:
    
    ```
    with torch.no_grad():
        y_pred = model(x_test)
    ```
    
    In this example, **`model`** is a PyTorch model that has already been trained and **`x_test`** is a test set. By using **`torch.no_grad()`** within the **`with`** statement, we ensure that PyTorch does not track the computations performed during the forward pass, and therefore does not compute gradients. This can make the prediction process faster and more memory-efficient.
    
- What is nethook?
    
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

---

- torch.randn(3, 3).**to("cuda")**
    
    Tensor moved to the GPU (the CUDA device) for faster computation
    

---

- Broadcasting
    
    Broadcasting is a way of making tensors with different shapes compatible for element-wise operations. When two tensors have different shapes, broadcasting rules are used to stretch one or both tensors to match the shape of the other tensor, so that the element-wise operation can be performed.
    
    ```
    tensor1 = torch.tensor([[1, 2], [3, 4]])
    tensor2 = torch.tensor([10, 20])
    ```
    
    In this case, `tensor1` has shape (2, 2), while `tensor2` has shape (2,). When we add these tensors using the `+` operator, broadcasting rules are used to stretch `tensor2` to match the shape of `tensor1` (by repeating tensor2), resulting in the following tensors:
    
    ```
    tensor1 = [[1, 2], [3, 4]]
    tensor2 = [10, 20]
    
    # After broadcasting:
    tensor1 = [[1, 2], [3, 4]]
    tensor2 = [[10, 20], [10, 20]]
    ```
    
    Now that both tensors have the same shape, the element-wise addition is performed on each corresponding element of the two tensors, resulting in the following tensor:
    
    ```
    tensor3 = tensor1 + tensor2
    # tensor3 = [[11, 22], [13, 24]]
    ```
    
- Can broadcasting be done if the dims of tensor2 are not a factor of tensor1's dims?
    
    No, broadcasting cannot be done if the dimensions of `tensor2` are not a factor of `tensor1`'s dimensions. Broadcasting requires that the dimensions of the two tensors are compatible, which means that they should either have the same size in each dimension, or one of the tensors should have a size of 1 in that dimension.
    
    For example, consider the following PyTorch tensors:
    
    ```
    tensor1 = torch.tensor([[1, 2], [3, 4]])
    tensor2 = torch.tensor([10, 20, 30])
    ```
    
    In this case, `tensor1` has shape (2, 2), while `tensor2` has shape (3,). Since the dimensions of `tensor2` are not a factor of `tensor1`'s dimensions, broadcasting cannot be done between the two tensors.
    
    If we try to perform an element-wise operation between these two tensors, such as addition, PyTorch will raise a `RuntimeError` with a message similar to the following:
    
    ```
    RuntimeError: The size of tensor1 (2) must match the size of tensor2 (3) at non-singleton dimension 0
    ```
    
    This error message indicates that the dimensions of `tensor1` and `tensor2` are incompatible for element-wise operations, since the sizes of the first dimension (i.e., the number of rows) are different.