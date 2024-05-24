# Clean_Transformer_Demo

## Actual Code

[Tutorial Video](https://www.youtube.com/watch?v=dsjUDacBw8o&list=PL7m7hLIqA0hoIUPhC26ASCVs_VrqcDpAz&index=2&ab_channel=NeelNanda)

[https://colab.research.google.com/drive/1br5wc-GQWaExgUnDIZcDarZ_zaBB-NYX](https://colab.research.google.com/drive/1br5wc-GQWaExgUnDIZcDarZ_zaBB-NYX)

## **Understanding Inputs & Outputs**

### Generation!

`print(tokens.shape)` #(batch size, position): Number of inputs (eg. a sentence) is batch size, number of tokens in an input is position

### LayerNorm

[**Batch and Layer Normalization**](../Neural%20Networks%20e6abb23474464e098117dced189fb7bb/Batch%20and%20Layer%20Normalization%20683d66e7db994beda71b25499d026b48.md) 

```python
class LayerNorm(nn.Module):
    [def __init__(self, cfg):](Clean_Transformer_Demo%20ef4d8370035c45259b85ba23e44e95c6.md)  # click to follow link
        super().__init__()
				self.w = nn.Parameter(torch.ones(cfg.d_model))
        self.b = nn.Parameter(torch.zeros(cfg.d_model))
	  ...
```

The class inherits from the **`nn.Module`** class. 

- def __init__(self, cfg):
    
    The **`cfg`** parameter is used to pass any configuration information that may be necessary for initializing the layer normalization module. This is a common pattern in deep learning frameworks, where parameters are often passed through the constructor method to configure a module.
    
    class Config: sets up fixed, re-usable parameters for a layer, such as `cfg.d_model`
    
    - @dataclass
        
        **`@dataclass`** is a decorator in Python that was introduced in version 3.7. It is used to define a class with attributes without having to write boilerplate code for initializing the attributes, comparing objects, and generating string representations.
        
        When you decorate a class with **`@dataclass`**, it automatically generates methods like **`__init__`**, **`__repr__`**, **`__eq__`**, **`__ne__`**, and **`__hash__`**. These methods are generated based on the class attributes and their default values, making it easy to create simple data classes with minimal code.
        
        Here's an example:
        
        ```
        from dataclasses import dataclass
        
        @dataclass
        class Point:
            x: float
            y: float
            label: str = ""
        
        p = Point(1.0, 2.0, "A")
        print(p)  # Output: Point(x=1.0, y=2.0, label='A')
        
        ```
        
        In this example, the **`@dataclass`** decorator is used to create a class **`Point`** with three attributes: **`x`**, **`y`**, and **`label`**. The **`label`** attribute has a default value of an empty string. The **`__init__`**, **`__repr__`**, **`__eq__`**, **`__ne__`**, and **`__hash__`** methods are automatically generated based on the class attributes.
        
        Using **`@dataclass`** can simplify code and make it more readable by reducing the amount of boilerplate code needed to define simple classes.
        
- super().**init**()
    
    [https://www.notion.so/Python-f5fe14898d744a74819532b914123159?pvs=4#bcf0bd0b1f3b42f3a5bf06ac3c96e189](../CS%20&%20SWE%20f7436b5aff924c04aa569007bb061038/Python%20f5fe14898d744a74819532b914123159.md)
    
- `self.w = nn.Parameter(torch.ones(cfg.d_model))`
    
    In the Python class definition for a Layer Normalization module using PyTorch, this creates a learnable parameter tensor **`w`** of shape **`(d_model,)`** initialized with all ones.
    
    **`nn.Parameter`** is a class in the PyTorch library that defines a tensor as a learnable parameter of a **`nn.Module`** object. This means that the parameter tensor will be updated during training, and its gradients will be computed and used to update the parameters of the model.
    
    By making **`self.w`** a learnable parameter, the layer normalization module can adaptively scale the normalized activations for each feature dimension during training, which can improve the performance of the model.
    
- `self.b = nn.Parameter(torch.zeros(cfg.d_model))`
    
    By making **`self.b`** a learnable parameter, the layer normalization module can adaptively shift the normalized activations for each feature dimension during training
    
    By default, don’t want to change variance so weight is “1” (b/c it’s multiplied with feature vector), and by default, don’t want to change mean so bias is “0” (b/c it’s added). After learning, variance and mean may be scaled and shifted.
    

```python
class LayerNorm(nn.Module):
		...
		def forward(self, residual):
        # residual: [batch, position, d_model]
        if self.cfg.debug: print("Residual:", residual.shape)
        residual = residual - einops.reduce(residual, "batch position d_model -> batch position 1", "mean")
        # Calculate the variance, square root it. Add in an epsilon to prevent divide by zero.
        scale = (einops.reduce(residual.pow(2), "batch position d_model -> batch position 1", "mean") + cfg.layer_norm_eps).sqrt()
        normalized = residual / scale
        normalized = normalized * self.w + self.b
        if self.cfg.debug: print("Normalized:", residual.shape)
        return normalized
```

Calculates a residual connection followed by layer normalization of the input to the current transformer layer, so that it has zero mean and unit variance. This helps to stabilize the training process. The residual connection ensures that information from the previous layer is preserved and added to the normalized input.

- # residual: [batch, position, d_model]
    
    The input to the layer normalization operation typically has shape [batch_size, sequence_length, hidden_size], where **`batch_size`** is the number of samples in a batch, **`sequence_length`** is the number of time steps in a sequence, and **`hidden_size`** is the number of features in the input.
    
    In the case of a transformer model, **`d_model`** is the same as **`hidden_size`**, and **`position`** refers to the position of a token in a sequence. The **`residual`** in **`residual: [batch, position, d_model]`** refers to the residual connection in the transformer model, which adds the output of the layer normalization operation to the original input.
    
- `residual = residual - einops.reduce(…, mean)`
    1. The variable `residual` represents the input to a transformer layer, which is the output of the previous layer in the network.
    2. The `einops.reduce()` function is then applied to `residual`. This function is used to reduce the dimensionality of a tensor by performing an operation along one or more axes. In this case, `einops.reduce()` is being used to calculate the mean of `residual` along the `d_model` axis, for each example in the batch and position in the sequence.
    3. The resulting tensor is then broadcasted to match the shape of `residual`.
    4. The original `residual` tensor is then subtracted by the mean tensor, element-wise.
    5. The resulting tensor is then passed through layer normalization.
    

`blocks.0.ln1.hook_scale torch.Size([1, 35, 1])`

- Why use a dummy dimension?
    
    The use of a dummy dimension in the tensor `hook_scale` is a common technique in PyTorch to ensure that broadcasting is performed correctly during tensor operations.
    
    - What's broadcasting?
        
        Broadcasting is a powerful feature in numerical computing libraries like NumPy and PyTorch that allows us to perform operations on arrays of different shapes and sizes.
        
        In simple terms, broadcasting allows us to perform operations between two arrays that may have different shapes, but are still compatible. Specifically, broadcasting involves automatically making copies of smaller arrays to match the shape of larger arrays, so that they can be combined in element-wise operations.
        
        For example, suppose we have two arrays:
        
        ```
        A = [[1, 2, 3],
             [4, 5, 6]]
        
        B = [10, 20, 30]
        
        ```
        
        The shape of array `A` is `(2, 3)` and the shape of array `B` is `(3,)`. If we want to add these two arrays together element-wise, we might expect to get an error because their shapes don't match. However, broadcasting allows us to add them together as if `B` had shape `(1, 3)`:
        
        ```
        A + B = [[11, 22, 33],
                 [14, 25, 36]]
        
        ```
        
        The way this works is that, during the operation, `B` is automatically "broadcasted" along the first axis to have the same shape as `A`, resulting in a temporary array of shape `(2, 3)`:
        
        ```
        B = [[10, 20, 30],
             [10, 20, 30]]
        
        ```
        
        This temporary array is then added to `A` element-wise to produce the final result.
        
        Broadcasting can be applied to arrays of any number of dimensions, and it is a very useful feature in deep learning when we need to perform operations on batches of data with different shapes or sizes. It can help simplify the code and make it more efficient by reducing the need for explicit loops or manual reshaping of arrays.
        
    
    In the specific example you provided, it appears that `hook_scale` is a tensor of shape `(1, 35, 1)`. The middle dimension of size 35 represents the sequence length, while the other two dimensions represent the batch size and a "dummy" dimension of size 1.
    
    The purpose of this dummy dimension is to ensure that `hook_scale` can be broadcasted to have the same shape as another tensor that has a different number of dimensions, but the same number of elements. For example, if we have another tensor of shape `(batch_size, 35, d_model)`, we can multiply it element-wise with `hook_scale` by simply writing:
    
    ```
    output = input * hook_scale
    
    ```
    
    In this case, PyTorch will automatically broadcast `hook_scale` along the batch dimension to match the shape of `input`. Without the dummy dimension in `hook_scale`, this operation would raise a broadcasting error.
    
    So, the use of a dummy dimension is just a trick to ensure that tensors with different numbers of dimensions can be used together in tensor operations. It's a common technique in PyTorch and other deep learning frameworks.
    
    (from tutorial):
    
    **13:34**
    
    here you want to make sure you've got a dummy Dimension so that when you divide by things it like broadcasts to the right shape rather than thinking oh I should divide the D model Dimension by the position axis and it's terrible