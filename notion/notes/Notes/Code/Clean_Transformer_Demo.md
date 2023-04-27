# Clean_Transformer_Demo

[https://www.youtube.com/watch?v=dsjUDacBw8o&list=PL7m7hLIqA0hoIUPhC26ASCVs_VrqcDpAz&index=2&ab_channel=NeelNanda](https://www.youtube.com/watch?v=dsjUDacBw8o&list=PL7m7hLIqA0hoIUPhC26ASCVs_VrqcDpAz&index=2&ab_channel=NeelNanda)

[https://colab.research.google.com/drive/1br5wc-GQWaExgUnDIZcDarZ_zaBB-NYX](https://colab.research.google.com/drive/1br5wc-GQWaExgUnDIZcDarZ_zaBB-NYX)

### LayerNorm

[****Batch and Layer Normalization****](../Neural%20Networks%20e6abb23474464e098117dced189fb7bb/Batch%20and%20Layer%20Normalization%20683d66e7db994beda71b25499d026b48.md) 

```python
class LayerNorm(nn.Module):
    [def __init__(self, cfg):](Clean_Transformer_Demo%20ef4d8370035c45259b85ba23e44e95c6.md)  # click to follow link
        super().__init__()
				self.w = nn.Parameter(torch.ones(cfg.d_model))
        self.b = nn.Parameter(torch.zeros(cfg.d_model))
    
    def forward(self, residual):
        # residual: [batch, position, d_model]
```

The class inherits from the **`nn.Module`** class.

- def __init__(self, cfg):
    
    The **`cfg`** parameter is used to pass any configuration information that may be necessary for initializing the layer normalization module. This is a common pattern in deep learning frameworks, where parameters are often passed through the constructor method to configure a module.
    
- super().**init**()
    
    **`super().__init__()`** is a call to the constructor of the superclass (parent class) of the current class. In Python, the **`super()`** function returns a temporary object of the superclass, which allows you to call its methods. **`__init__()`** is a method used to initialize an instance of a class.
    
    When you call **`super().__init__()`**, you are essentially calling the constructor of the superclass, passing it any arguments that were passed to the current class constructor. This is commonly used in object-oriented programming when you want to inherit properties and methods from a parent class while also adding your own functionality in the child class.
    
    For example, if you have a class **`Child`** that inherits from a class **`Parent`**, and both classes have an **`__init__()`** method, you can use **`super().__init__()`** in the **`Child`** class to call the constructor of the **`Parent`** class and initialize any properties that it defines. This allows you to reuse the code in the **`Parent`** class without having to redefine it in the **`Child`** class.
    
- self.w = nn.Parameter(torch.ones(cfg.d_model))
    
    In the Python class definition for a Layer Normalization module using PyTorch, this creates a learnable parameter tensor **`w`** of shape **`(d_model,)`** initialized with all ones.
    
    **`nn.Parameter`** is a class in the PyTorch library that defines a tensor as a learnable parameter of a **`nn.Module`** object. This means that the parameter tensor will be updated during training, and its gradients will be computed and used to update the parameters of the model.
    
    By making **`self.w`** a learnable parameter, the layer normalization module can adaptively scale the normalized activations for each feature dimension during training, which can improve the performance of the model.
    
- self.b = nn.Parameter(torch.zeros(cfg.d_model))
    
    By making **`self.b`** a learnable parameter, the layer normalization module can adaptively shift the normalized activations for each feature dimension during training
    
    By default, don’t want to change variance so weight is “1” (b/c it’s multiplied with feature vector), and by default, don’t want to change mean so bias is “0” (b/c it’s added). After learning, variance and mean may be scaled and shifted.
    
- # residual: [batch, position, d_model]
    
    The input to the layer normalization operation typically has shape [batch_size, sequence_length, hidden_size], where **`batch_size`** is the number of samples in a batch, **`sequence_length`** is the number of time steps in a sequence, and **`hidden_size`** is the number of features in the input.
    
    In the case of a transformer model, **`d_model`** is the same as **`hidden_size`**, and **`position`** refers to the position of a token in a sequence. The **`residual`** in **`residual: [batch, position, d_model]`** refers to the residual connection in the transformer model, which adds the output of the layer normalization operation to the original input.
    
- 

class Config: sets up fixed, re-usable parameters for a layer

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