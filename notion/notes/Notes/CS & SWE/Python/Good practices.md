# Good practices

[https://docs.python-guide.org/writing/style/](https://docs.python-guide.org/writing/style/)

[https://pep8.org/](https://pep8.org/)

[https://stackoverflow.com/questions/3501382/checking-whether-a-variable-is-an-integer-or-not](https://stackoverflow.com/questions/3501382/checking-whether-a-variable-is-an-integer-or-not)

Do not use `type`. It is almost never the right answer in Python, since it blocks all the flexibility of polymorphism.

This adheres to Python's strong polymorphism: you should allow any object that behaves like an `int`, instead of mandating that it be one.

---

[https://realpython.com/learning-paths/writing-pythonic-code/](https://realpython.com/learning-paths/writing-pythonic-code/)

[https://realpython.com/python-refactoring/](https://realpython.com/python-refactoring/)

[https://realpython.com/python-refactoring/#1-functions-that-should-be-objects](https://realpython.com/python-refactoring/#1-functions-that-should-be-objects)