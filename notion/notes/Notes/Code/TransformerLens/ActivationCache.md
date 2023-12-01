# ActivationCache

[https://neelnanda-io.github.io/TransformerLens/generated/code/transformer_lens.ActivationCache.html](https://neelnanda-io.github.io/TransformerLens/generated/code/transformer_lens.ActivationCache.html)

- This class is a wrapper

- Function checks: Why use Assert and logging
    
    Eg)
    
    ```python
    def remove_batch_dim(self) -> ActivationCache:
            """Remove the Batch Dimension (if a single batch item).
    
            Returns:
                The ActivationCache with the batch dimension removed.
            """
            if self.has_batch_dim:
                for key in self.cache_dict:
                    assert (
                        self.cache_dict[key].size(0) == 1
                    ), f"Cannot remove batch dimension from cache with batch size > 1, \
                        for key {key} with shape {self.cache_dict[key].shape}"
                    self.cache_dict[key] = self.cache_dict[key][0]
                self.has_batch_dim = False
            else:
                logging.warning(
                    "Tried removing batch dimension after already having removed it."
                )
            return self
    ```
    
    - Use assert
        - The **`assert`** statement is used here to ensure that the batch size is exactly 1 before proceeding with the removal of the batch dimension. This is a safeguard to prevent unintended behavior or errors.
        - If the condition (**`self.cache_dict[key].size(0) == 1`**) is **`False`**, it indicates an unexpected state (batch size is not 1). The assert statement will raise an **`AssertionError`** with a descriptive message. This message provides insights into what went wrong and where, which is useful during debugging.
        - Using **`assert`** for this check is appropriate in a development or testing environment where catching such conditions early is crucial. However, it's important to note that **`assert`** statements can be disabled in optimized runs of Python (using **`O`** flag), so they should not be used for critical checks in production code.
    - Use logging
        - The **`logging.warning`** call is used to log a warning message when the method tries to remove the batch dimension, but it has already been removed. This is an indication of a potential logical error in the usage of the method.
        - Unlike **`assert`**, logging does not interrupt the execution of the program. It merely records the occurrence of the unexpected situation.
        - Using **`logging`** for this purpose allows the program to continue running while still notifying the developers or users about the potential issue. This can be helpful in production environments where you do not want the entire application to stop because of non-critical issues but still want to be aware of them for future investigation or debugging.
    
    In summary, **`assert`** is used for enforcing critical conditions and catching unexpected states during development, while **`logging`** provides a way to record warnings and information about the program's execution state, which is particularly useful for monitoring and debugging in production environments.
    
- Why does this function have to be made instead of directly retrieving the activations by calling the class variable
    
    ```python
    def __getitem__(self, key) -> torch.Tensor:
            """Retrieve Cached Activations by Key or Shorthand.
    
            Enables direct access to cached activations via dictionary-style indexing using keys or
            shorthand naming conventions. It also supports tuples for advanced indexing, with the
            dimension order as (get_act_name, layer_index, layer_type).
    
            Args:
                key:
                    The key or shorthand name for the activation to retrieve.
    
            Returns:
                The cached activation tensor corresponding to the given key.
            """
            if key in self.cache_dict:
                return self.cache_dict[key]
            elif type(key) == str:
                return self.cache_dict[utils.get_act_name(key)]
            else:
                if len(key) > 1 and key[1] is not None:
                    if key[1] < 0:
                        # Supports negative indexing on the layer dimension
                        key = (key[0], self.model.cfg.n_layers + key[1], *key[2:])
                return self.cache_dict[utils.get_act_name(*key)]
    ```
    
    The `__getitem__` method in this class serves as a more flexible and user-friendly interface for accessing cached activations compared to directly accessing class variables. Here's why this function is beneficial:
    
    1. **Abstraction and Encapsulation:**
        - The method abstracts the underlying data structure (`self.cache_dict`) used for storing activations. Users of the class don't need to know the details of how activations are stored; they can simply use the indexing syntax to access them.
        - Encapsulation is maintained, as the internal representation of the data can be changed without affecting how users interact with the class. For instance, if the storage mechanism is modified in the future, the `__getitem__` method can be updated accordingly without requiring changes in the code that uses this class.
    2. **Enhanced Flexibility and Convenience:**
        - The method allows for different ways of accessing activations: using direct keys, shorthand names, or advanced indexing with tuples. This flexibility makes it easier for users to retrieve the data they need without having to construct complex keys themselves.
        - The support for shorthand naming and advanced indexing (like negative indexing) makes the interface more intuitive and aligned with common Python practices (e.g., negative indexing is a familiar concept in Python lists).
    3. **Error Handling and Custom Logic:**
        - Custom error handling or logic can be implemented within this method. For example, it could handle cases where a key does not exist in a user-friendly manner or provide custom logic for different types of keys.
        - This method can also include additional checks or transformations on the data before returning it, which might be more complex or inappropriate to include in the calling code.
    4. **Consistency with Python Data Model:**
        - By implementing `__getitem__`, the class adheres to the Python data model, allowing objects of this class to behave like a Python container (similar to lists or dictionaries). This means they can leverage Python's syntactic features like the square bracket indexing.
        - This consistency makes the class more intuitive to use for Python developers and allows it to integrate more seamlessly with other Python code and libraries.
    
    In summary, implementing a `__getitem__` method provides a more intuitive, flexible, and robust way for users to access cached activations, while maintaining good programming practices like encapsulation and abstraction.
    
- How to measure how much memory autodiff takes up?
    
    [https://www.digitaltrends.com/computing/how-much-gpu-memory-do-i-need/](https://www.digitaltrends.com/computing/how-much-gpu-memory-do-i-need/)
    
    - code
        
        ```python
        def toggle_autodiff(self, mode: bool = False):
                """Toggle Autodiff Globally.
        
                Applies `torch.set_grad_enabled(mode)` to the global state (not just TransformerLens).
        
                Warning:
        
                This is pretty dangerous, since autodiff is global state - this turns off torch's
                ability to take gradients completely and it's easy to get a bunch of errors if you don't
                realise what you're doing.
        
                But autodiff consumes a LOT of GPU memory (since every intermediate activation is cached
                until all downstream activations are deleted - this means that computing the loss and
                storing it in a list will keep every activation sticking around!). So often when you're
                analysing a model's activations, and don't need to do any training, autodiff is more trouble
                than its worth.
        
                If you don't want to mess with global state, using torch.inference_mode as a context manager
                or decorator achieves similar effects:
        
                >>> with torch.inference_mode():
                ...     y = torch.Tensor([1., 2, 3])
                >>> y.requires_grad
                False
                """
                logging.warning("Changed the global state, set autodiff to %s", mode)
                torch.set_grad_enabled(mode)
        
            def keys(self):
                """Keys of the ActivationCache.
        
                Examples:
        
                    >>> from transformer_lens import HookedTransformer
                    >>> model = HookedTransformer.from_pretrained("tiny-stories-1M")
                    Loaded pretrained model tiny-stories-1M into HookedTransformer
                    >>> _logits, cache = model.run_with_cache("Some prompt")
                    >>> list(cache.keys())[0:3]
                    ['hook_embed', 'hook_pos_embed', 'blocks.0.hook_resid_pre']
        
                Returns:
                    List of all keys.
                """
                return self.cache_dict.keys()
        ```
        
    
    Autodiff, through the mechanism of backward propagation, computes gradients of the loss function with respect to the model parameters. This process requires storing intermediate activations and gradients, which can consume a significant amount of memory, especially in large models. Here are some methods to estimate or monitor this memory usage:
    
    1. **Monitor GPU/CPU Memory Usage:**
        - Use system monitoring tools to observe the memory usage of your Python process. Tools like `nvidia-smi` for GPUs or `top` and `htop` for CPUs can be helpful. You can compare the memory usage with and without autodiff enabled.
    2. **PyTorch Memory Profiling:**
        - PyTorch provides utilities for memory profiling. The `torch.cuda.memory_summary()` function can give detailed insights into how much memory is being used by tensors, cached allocations, etc.
        - PyTorch's `torch.utils.tensorboard` module can also be used to log memory usage metrics and visualize them using TensorBoard.
    3. **Custom Profiling:**
        - Manually track memory usage before and after operations that require autodiff. You can use Python's `memory_profiler` package for fine-grained memory tracking.
        - This method is more hands-on and can be tailored to your specific use case, but it requires a deeper understanding of Python memory management.
    4. **Estimation by Comparison:**
        - Run your model with autodiff enabled and measure the memory usage. Then, disable autodiff using your `toggle_autodiff` function or a context manager like `torch.inference_mode()` and measure the memory usage again. The difference can give you an estimate of the memory overhead due to autodiff.
    5. **Analyzing Model and Batch Size:**
        - The memory consumption due to autodiff is closely related to the model size (number of parameters) and the batch size. Larger models and larger batch sizes will generally require more memory for storing gradients and activations.
        - Experiment with different model sizes and batch sizes to understand how they impact memory usage.
    6. **Using PyTorch's Autograd Profiler:**
        - PyTorch's autograd profiler, `torch.autograd.profiler`, can be used to profile the memory usage of operations during the forward and backward passes. This can give insights into which operations are most memory-intensive.
    
    Remember, the exact memory consumption can be influenced by various factors like model architecture, batch size, and the specifics of the computation graph. 
    

Methods

[[decompose_resid](https://github.com/neelnanda-io/TransformerLens/blob/main/transformer_lens/ActivationCache.py#L583)()  ](ActivationCache%2061867516111445ab82a379900584b637/decompose_resid()%20a9d6ef4290cc4f42b1a2f3cac37cadbd.md)