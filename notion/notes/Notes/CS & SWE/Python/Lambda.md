# Lambda

[https://realpython.com/python-lambda/](https://realpython.com/python-lambda/)

lambda arg: f(arg)

[https://www.freecodecamp.org/news/python-lambda-function-explained/](https://www.freecodecamp.org/news/python-lambda-function-explained/)

You should use the lambda function to create simple expressions. For example, expressions that do not include complex structures such as if-else, for-loops, and so on.

In Python, iterables include strings, lists, dictionaries, ranges, tuples, and so on.

`filter(function, iterable)`

`filter(lambda x: x % 2 == 0, list1)`

```python
list(filter(lambda x: x % 2 == 0, list1))
>> [2, 4, 6, 8, 10]
```

---

[https://docs.python.org/3/howto/functional.html](https://docs.python.org/3/howto/functional.html)

A later call to the same function creates a new private namespace and a fresh set of local variables. But, what if the local variables weren’t thrown away on exiting a function? What if you could later resume the function where it left off? This is what generators provide; they can be thought of as resumable functions.