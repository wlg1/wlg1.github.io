# Multiple constructors

[https://pythonbasics.org/constructor/](https://pythonbasics.org/constructor/)

The constructor `__init__(self)` is a method that is called when an object is created. This method is defined in the class and can be used to initialize basic variables.

- super().**init**()
    
    **`super().__init__()`** is a call to the constructor of the superclass (parent class) of the current class. In Python, the **`super()`** function returns a temporary object of the superclass, which allows you to call its methods. **`__init__()`** is a method used to initialize an instance of a class.
    
    When you call **`super().__init__()`**, you are essentially calling the constructor of the superclass, passing it any arguments that were passed to the current class constructor. This is commonly used in object-oriented programming when you want to inherit properties and methods from a parent class while also adding your own functionality in the child class.
    
    For example, if you have a class **`Child`** that inherits from a class **`Parent`**, and both classes have an **`__init__()`** method, you can use **`super().__init__()`** in the **`Child`** class to call the constructor of the **`Parent`** class and initialize any properties that it defines. This allows you to reuse the code in the **`Parent`** class without having to redefine it in the **`Child`** class.
    

[https://realpython.com/python-multiple-constructors/#providing-multiple-constructors-with-classmethod-in-python](https://realpython.com/python-multiple-constructors/#providing-multiple-constructors-with-classmethod-in-python)