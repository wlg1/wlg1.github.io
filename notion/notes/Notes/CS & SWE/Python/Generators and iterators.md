# Generators and iterators

[https://www.programiz.com/python-programming/generator](https://www.programiz.com/python-programming/generator)

In Python, a generator is a [function](https://www.programiz.com/python-programming/function) that returns an [iterator](https://www.programiz.com/python-programming/iterator) that produces a sequence of values when iterated over.

Generators are useful when we want to produce a large sequence of values, but we don't want to store all of them in memory at once.

The `yield` keyword is used to produce a value from the generator and pause the generator function's execution until the next value is requested.

Eg) generator(1), generator(2) : generator(1) is paused right after `yield value` until generator(2) is called again

[https://realpython.com/introduction-to-python-generators/#understanding-the-python-yield-statement](https://realpython.com/introduction-to-python-generators/#understanding-the-python-yield-statement)
This allows you to resume function execution whenever you call one of the generator’s methods.

[https://docs.python.org/3/tutorial/classes.html#iterators](https://docs.python.org/3/tutorial/classes.html#iterators)

---

```jsx
def next_key(ordered_dict: OrderedDict, current_key):
    key_iterator = iter(ordered_dict)
    next((key for key in key_iterator if key == current_key), None)
    return next(key_iterator, None)
```