# Decorator

“save” an arg to a fn as a function (5+y) to be used later to compose with another arg (y)

[https://www.programiz.com/python-programming/decorator](https://www.programiz.com/python-programming/decorator)

```python
def outer(x):
    def inner(y):
        return x + y
    return inner

add_five = outer(5)  # inner(y): 5 + y
result = add_five(6) # prints 11
```

```python
def make_pretty(func):  # decorator
    # define the inner function 
    def inner():
        # add some additional behavior to decorated function
        print("I got decorated")

        # call original function
        func()
    # return the inner function
    return inner

# define ordinary function
def ordinary():
    print("I am ordinary")
    
# decorate the ordinary function
decorated_func = make_pretty(ordinary)

# call the decorated function
decorated_func()
```

This passes in `ordinary` as `func()` 

`print("I got decorated")
func()` # runs ordinary()

The reason it requires an inner function is that the decorator RETURNS A FUNCTION. It cannot return itself, so it must create a new object, `inner()`, which is what it returns. It combines inner() with its arg func() and returns them as one combined function.

This is equivalent:

```python
def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

@make_pretty # decorate the ordinary function
def ordinary():
    print("I am ordinary")

ordinary() # call the decorated function
```

The only thing that’s changed is `decorated_func = make_pretty(ordinary)` is replaced by `@make_pretty`. Then we call the original function, NOT a new decorated function decorated_func(). The original is now decorated.

---

[https://www.linkedin.com/advice/0/how-do-you-balance-performance-flexibility](https://www.linkedin.com/advice/0/how-do-you-balance-performance-flexibility)

The main difference between decorator pattern and inheritance is that decorator pattern does not create a new class or a new type of object, but rather modifies an existing object by wrapping it with another object.

[https://stackoverflow.com/questions/6406446/decorators-versus-inheritance](https://stackoverflow.com/questions/6406446/decorators-versus-inheritance)

https://youtu.be/yNzxXZfkLUA?si=hOVtSbXZf8gx0WCF