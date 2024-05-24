# Repo Structure

[Locally Run Code](Repo%20Structure%20b81c8e1ce00b4bb48ea4e6f1a390c45d/Locally%20Run%20Code%201fbc6794d32b41a4ba79a7b1b0181c84.md)

File Types

[requirements.txt](Repo%20Structure%20b81c8e1ce00b4bb48ea4e6f1a390c45d/requirements%20txt%204528740894b7494f933c0915795d144a.md) 

[pyproject.toml](Repo%20Structure%20b81c8e1ce00b4bb48ea4e6f1a390c45d/pyproject%20toml%202331d4c2130d4f6d8f79d1cc23b4a0a3.md)

[.codecov.yml](Repo%20Structure%20b81c8e1ce00b4bb48ea4e6f1a390c45d/codecov%20yml%20db9f1fff278c459c8513fa41b2629b0f.md)

[poetry.lock](Repo%20Structure%20b81c8e1ce00b4bb48ea4e6f1a390c45d/poetry%20lock%2042b55002b37b488ab3fd28d8233443dc.md)

Folder Types

[.vscode](Repo%20Structure%20b81c8e1ce00b4bb48ea4e6f1a390c45d/vscode%20de49a13f106142d0927d677f5c7b156f.md)

[utils](Repo%20Structure%20b81c8e1ce00b4bb48ea4e6f1a390c45d/utils%2050213294058c4154a7c6cd4a2052bc22.md)

Common Practices

- how do I put this warning in my repo so that when a user calls a deprecated function, it’ll show: WARNING: root:Xis deprecated and will eventually be removed, use Y
    
    To show a warning message when a deprecated function is called in your Python code, you can use the `warnings` module. Here’s how you can implement it:
    
    1. Import the `warnings` module.
    2. Define your deprecated function and use the `warnings.warn` function to display the warning message.
    3. Optionally, create a decorator to make it easier to deprecate multiple functions.
    
    Here's an example:
    
    ```python
    import warnings
    import functools
    
    # Define the decorator
    def deprecated(replacement=None):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                message = f"{func.__name__} is deprecated and will eventually be removed."
                if replacement:
                    message += f" Use {replacement} instead."
                warnings.warn(message, category=DeprecationWarning, stacklevel=2)
                return func(*args, **kwargs)
            return wrapper
        return decorator
    
    # Example usage
    @deprecated(replacement='Y')
    def X():
        print("This is function X.")
    
    def Y():
        print("This is function Y.")
    
    # Calling the deprecated function
    X()
    
    ```
    
    When you run this code, calling the deprecated function `X` will produce the following warning message:
    
    ```
    WARNING:root:X is deprecated and will eventually be removed. Use Y instead.
    
    ```
    
    Make sure that you include the `DeprecationWarning` in your warnings filter to ensure it is shown, as they are ignored by default in some environments. You can do this by modifying the warnings filter in your code:
    
    ```python
    warnings.simplefilter('always', DeprecationWarning)
    
    ```
    
    Add this line before any of your code that uses the `deprecated` decorator to ensure the warnings are shown.