# Python

[Packages](Python%20f5fe14898d744a74819532b914123159/Packages%20022db6d85ead45658f8c4d9f5fc49996.md)

---

- any()
    
    The **`any()`**  function takes an iterable (in this case, a list comprehension) as its argument and returns **`True`** if at least one element of the iterable is truthy, and **`False`** otherwise.
    

---

- [https://realpython.com/python-f-strings/#f-strings-a-new-and-improved-way-to-format-strings-in-python](https://realpython.com/python-f-strings/#f-strings-a-new-and-improved-way-to-format-strings-in-python)
    
    f-strings are not the old way to format strings
    
    OLD METHODS:
    
    ```python
    >>> "Hello, {}. You are {}.".format(name, age)
    'Hello, Eric. You are 74.'
    
    >>> person = {'name': 'Eric', 'age': 74}
    >>> "Hello, {name}. You are {age}.".format(**person)
    'Hello, Eric. You are 74.'
    ```
    
    NEW METHOD (f-strings):
    
    ```python
    >>> name = "Eric"
    >>> age = 74
    >>> f"Hello, {name}. You are {age}."
    'Hello, Eric. You are 74.'
    ```
    
    There is no need to format as long as you put f in front.
    

---

- [https://stackoverflow.com/questions/54962869/function-parameter-with-colon](https://stackoverflow.com/questions/54962869/function-parameter-with-colon)
    
    ```
    def splitComma(line: str) -> str:
        ...
    ```
    
    It's a function annotation; function arguments and the return value (after ->) can be tagged with arbitrary Python expressions. Python itself ignores the annotation (other than saving it), but third-party tools can make use of them.
    
    In this case, it is intended as type hint: programs like [mypy](https://github.com/python/mypy) can analyze your code statically (that is, without running it, but only looking at the source code itself) to ensure that only `str` values are passed as arguments to `splitComma`.
    
- [https://medium.com/@thomas_k_r/whats-this-weird-arrow-notation-in-python-53d9e293113](https://medium.com/@thomas_k_r/whats-this-weird-arrow-notation-in-python-53d9e293113)
    
    ```python
    def useful_function(x) -> int:
        # Useful code, using x, here
        return x
    ```
    
    Return type is an int
    

---

- [https://stackoverflow.com/questions/36901/what-does-double-star-asterisk-and-star-asterisk-do-for-parameters](https://stackoverflow.com/questions/36901/what-does-double-star-asterisk-and-star-asterisk-do-for-parameters)
    
    The `*args` and `**kwargs` is a common idiom to allow arbitrary number of arguments to functions as described in the section [more on defining functions](http://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions) in the Python documentation.
    
    The `*args` will give you all function parameters [as a tuple](https://docs.python.org/3/tutorial/controlflow.html#arbitrary-argument-lists):
    
    ```
    def foo(*args):
        for a in args:
            print(a)
    
    foo(1)
    # 1
    
    foo(1,2,3)
    # 1
    # 2
    # 3
    
    ```
    
    The `**kwargs` will give you all **keyword arguments** except for those corresponding to a formal parameter as a dictionary.
    
    ```
    def bar(**kwargs):
        for a in kwargs:
            print(a, kwargs[a])
    
    bar(name='one', age=27)
    # name one
    # age 27
    ```
    
    ---
    
    What is model (**inputs)?
    
    In Python, the double-asterisk notation **`**`** is used to pass a dictionary of keyword arguments to a function. In the given code, **`**inputs`** is used to pass the dictionary **`inputs`** as keyword arguments to the **`model`** function.
    
    Here's how it works:
    
    - **`inputs`** is a dictionary that contains the input sequences as PyTorch tensors. The keys of the dictionary correspond to the names of the input tensors that the model expects (e.g., **`"input_ids"`**, **`"attention_mask"`**, etc.).
    - **`*inputs`** unpacks the **`inputs`** dictionary into a set of keyword arguments that can be passed to the **`model`** function. This is equivalent to calling the function with the keyword arguments explicitly specified, like this: **`model(input_ids=inputs["input_ids"], attention_mask=inputs["attention_mask"], ...)`**.
    - By using the **`*`** notation, we avoid having to manually unpack the **`inputs`** dictionary and specify each keyword argument separately. This makes the code cleaner and more concise.

---

[https://www.stechies.com/range-vs-arangein-python/](https://www.stechies.com/range-vs-arangein-python/)

Use range() for iterations

arange(): NumPy arrays are fast and creating a homogenous array; good for large data sets

x = np.arange(1, 10, 3)

[1 4 7]

---

- Modify in-place
    
    ```
    v[...] = torch.clamp(v, min=weights_copy[k] - eps, max=weights_copy[k] + eps)
    ```
    
    This operation clamps the values of `v` between `min=weights_copy[k] - eps` and `max=weights_copy[k] + eps`.,  where eps is the norm constraint specified in hparams (from a file). The ellipsis (`[...]`) in the left-hand side of the assignment indicates that the values of `v` should be modified in place.
    
    The weights are modified in place because it is more efficient than creating a new tensor with the modified values. Therefore, it is a memory-efficient way to modify the tensor without creating a new tensor.
    

---

[https://pythonbasics.org/constructor/](https://pythonbasics.org/constructor/)

The constructor `__init__(self)` is a method that is called when an object is created. This method is defined in the class and can be used to initialize basic variables.

- super().**init**()
    
    **`super().__init__()`** is a call to the constructor of the superclass (parent class) of the current class. In Python, the **`super()`** function returns a temporary object of the superclass, which allows you to call its methods. **`__init__()`** is a method used to initialize an instance of a class.
    
    When you call **`super().__init__()`**, you are essentially calling the constructor of the superclass, passing it any arguments that were passed to the current class constructor. This is commonly used in object-oriented programming when you want to inherit properties and methods from a parent class while also adding your own functionality in the child class.
    
    For example, if you have a class **`Child`** that inherits from a class **`Parent`**, and both classes have an **`__init__()`** method, you can use **`super().__init__()`** in the **`Child`** class to call the constructor of the **`Parent`** class and initialize any properties that it defines. This allows you to reuse the code in the **`Parent`** class without having to redefine it in the **`Child`** class.