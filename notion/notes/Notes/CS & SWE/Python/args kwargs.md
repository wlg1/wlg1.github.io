# args kwargs

[https://realpython.com/python-kwargs-and-args/#unpacking-with-the-asterisk-operators](https://realpython.com/python-kwargs-and-args/#unpacking-with-the-asterisk-operators)
What if you need to sum a varying number of arguments, where the specific number of arguments passed is only determined at runtime?	
def my_sum(*args):

- *kwargs dictionary works just like *args, but instead of accepting positional arguments it accepts keyword (or named) arguments.
- args must come before **kwargs.

lists are mutable, while tuples are not

Instead of a list, print() has taken three separate arguments as the input.

The single asterisk operator * can be used on any iterable that Python provides, while the double asterisk operator ** can only be used on dictionaries.

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