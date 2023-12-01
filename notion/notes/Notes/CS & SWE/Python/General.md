# General

[https://docs.python.org/3/tutorial/index.html](https://docs.python.org/3/tutorial/index.html)

- why use dict.get(key) over dict[key]?
    
    Using `dict.get(key)` instead of `dict[key]` in Python is often a matter of handling the situation when the key is not present in the dictionary. Here's a comparison of the two methods:
    
    1. **`dict[key]`:**
        - This method will directly return the value associated with `key` in the dictionary.
        - If the `key` does not exist in the dictionary, it raises a `KeyError`.
        - It's suitable when you're certain that the key exists in the dictionary or when you want an exception to be raised for missing keys.
    2. **`dict.get(key)`:**
        - This method also returns the value associated with `key`, but it has an important difference: if the `key` is not found, it returns `None` instead of raising an error.
        - You can also provide a default value that `get` should return if the key is not found: `dict.get(key, default_value)`. This is useful for providing fallbacks.
        - This approach is safer when you are not sure if the key exists and you want to avoid exceptions. It allows for more graceful handling of missing keys.
    
    In summary, `dict.get(key)` is often used for its safer handling of missing keys and flexibility in providing default values, while `dict[key]` is more straightforward but less forgiving when the key is not present.
    

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

[https://www.stechies.com/range-vs-arangein-python/](https://www.stechies.com/range-vs-arangein-python/)

Use range() for iterations

arange(): NumPy arrays are fast and creating a homogenous array; good for large data sets

x = np.arange(1, 10, 3)

[1 4 7]