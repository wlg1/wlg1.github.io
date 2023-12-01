# Tuned Lens

[https://github.com/rhaps0dy/tuned-lens/blob/main/tuned_lens/model_surgery.py](https://github.com/rhaps0dy/tuned-lens/blob/main/tuned_lens/model_surgery.py)

- assign_key
    
    ```python
    @contextmanager
    def assign_key_path(model: T, key_path: str, value: Any) -> Generator[T, None, None]:
        """Temporarily set a value by key path while in the context."""
        old_value = get_key_path(model, key_path)
        set_key_path_(model, key_path, value)
        try:
            yield model
        finally:
            set_key_path_(model, key_path, old_value)
    ```
    
    Your `assign_key_path` function is implemented as a context manager. It's intended to temporarily set a value in a model at a specified key path, and then revert to the original value once the context exits. This is a neat utility function that can be handy in many scenarios!
    
    The code you provided is inside a context manager (as indicated by the `@contextmanager` decorator). The context manager is a special type of Python generator that has the ability to temporarily change some state during its context (the block inside the `with` statement) and then revert that change once the context is exited.
    
    Here's a breakdown of what the code does:
    
    1. `yield model`: This is where the generator (context manager) pauses its execution and returns control to the caller. When used in a `with` statement, anything after the `with` will have access to the yielded `model`. The `yield` essentially represents the body of the `with` block.
    2. `finally`: This block is executed after the `yield` statement, regardless of how the block inside the `with` statement exits. This means it'll run whether the block completes normally, if there's an exception, or even if there's a `return` statement inside the block.
    3. `set_key_path_(model, key_path, old_value)`: This line reverts the model to its original state. It takes the old value (which was saved before any modification) and assigns it back to the specified key path. The purpose of this is to ensure that any temporary change made to the model is reverted after the `with` block completes.
    
    In short, when using this context manager:
    
    - You temporarily set a new value for a given key path in the model.
    - Inside the `with` block, the model has this new value.
    - Once the `with` block is exited, the context manager ensures the model's value at that key path is reverted to its original state.
    
    The purpose of this kind of context manager is to allow for "sandboxed" changes: modifications that exist only within a certain context and are automatically undone afterwards.