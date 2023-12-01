# Typing

[https://realpython.com/python-type-checking/](https://realpython.com/python-type-checking/)

[https://en.wikipedia.org/wiki/Duck_typing](https://en.wikipedia.org/wiki/Duck_typing)

typing: just for type hints in function args (not functionality; for comments)

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
    

[https://stackoverflow.com/questions/72017661/what-does-union-from-typing-module-in-python-do](https://stackoverflow.com/questions/72017661/what-does-union-from-typing-module-in-python-do)

`Union` in this case means both types are allowed.

[https://www.infoworld.com/article/3630372/get-started-with-python-type-hints.html](https://www.infoworld.com/article/3630372/get-started-with-python-type-hints.html)

**Use `Union` to indicate that an object can be one of several types. Use `Optional` to indicate that an object is either one given type or `None`.**

[https://stackoverflow.com/questions/51710037/how-should-i-use-the-optional-type-hint](https://stackoverflow.com/questions/51710037/how-should-i-use-the-optional-type-hint)

`Optional[...]` is a shorthand notation for `Union[..., None]`, telling the type checker that either an object of the specific type is required, *or* `None` is required