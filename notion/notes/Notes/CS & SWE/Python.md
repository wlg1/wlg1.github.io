# Python

[General](Python%20f5fe14898d744a74819532b914123159/General%20442c3ebf87744b33804eceea5d5609eb.md)

[Packages](Python%20f5fe14898d744a74819532b914123159/Packages%20022db6d85ead45658f8c4d9f5fc49996.md)

[Good practices](Python%20f5fe14898d744a74819532b914123159/Good%20practices%20f1bbbab0d7254ba9a72b433f1dffed93.md)

[conda](Python%20f5fe14898d744a74819532b914123159/conda%20c93465991ea648fbb2e6db2795f837ae.md)

[snippets and prompts](Python%20f5fe14898d744a74819532b914123159/snippets%20and%20prompts%20aec0e6ae2f0d46d8a764d9c15fc8ff26.md)

- List concepts to apply
    1. Magic methods, `__repr__`
    2. Inheritance, Multiple Inheritance
    3. Composition / Delegation
    4. Dependency Injection design pattern
    5. Polymorphism
    6. Collections
    7. Decorators
    8. Yield, generators, iterators
    9. `@dataclass`
    10. `@contextmanagers`, with try/finally
    11. `@abstractmethod`
    12. Multiple constructors, overloading
    13. `@classmethod`, `@staticmethod`
    14. `__getitem__`, `@property`, encapsulation
    15. Unpacking args
    16. Typing, mutable
    17. Raise error, try/except
    18. Unit testing, `assert`

---

[Arrays](Python%20f5fe14898d744a74819532b914123159/Arrays%209ff46dd495534de884fcd66115a18ffe.md)

[Numpy](Python%20f5fe14898d744a74819532b914123159/Numpy%2036fa39684bc241569f0b6b9793fe0e3d.md)

[Regular Expr](Python%20f5fe14898d744a74819532b914123159/Regular%20Expr%20798e184cb9bc4bcab206eb2aed152b30.md)

[Collections](Python%20f5fe14898d744a74819532b914123159/Collections%20baba4e28545148df8eb607e6c8e7f6cb.md)

[Typing](Python%20f5fe14898d744a74819532b914123159/Typing%20848e0a28968643f5a9b5888663b2daf1.md)

[File handling](Python%20f5fe14898d744a74819532b914123159/File%20handling%202d31fc16ee4a4f37a3fbfda857c4c802.md)

[Context managers](Python%20f5fe14898d744a74819532b914123159/Context%20managers%20a022cedc35734193a19e38dff0bcdb1b.md)

[Error handling](Python%20f5fe14898d744a74819532b914123159/Error%20handling%206cdbac4c29e64006ae1640d2cdd2a93d.md)

[Testing](Python%20f5fe14898d744a74819532b914123159/Testing%20e6e9ada72fe240b4b7a6517c47f964ab.md)

---

[Lambda](Python%20f5fe14898d744a74819532b914123159/Lambda%20422adcf91677481db2522ca5a4fdbe92.md)

[Decorator](Python%20f5fe14898d744a74819532b914123159/Decorator%20a3bfd9efbcc6452f88d4b7415a16629b.md)

[Generators and iterators](Python%20f5fe14898d744a74819532b914123159/Generators%20and%20iterators%20168af09744c34862ad7845f9d2a6deea.md)

---

[OOP](Python%20f5fe14898d744a74819532b914123159/OOP%20c62170ec71fe42acb5e885267f5e2381.md)

[Magic methods](Python%20f5fe14898d744a74819532b914123159/Magic%20methods%20d7a7291d8778431982440eca086acaea.md)

[classmethod](Python%20f5fe14898d744a74819532b914123159/classmethod%205de27c6dfe1e4fde84bf3b8edd264653.md)

[static](Python%20f5fe14898d744a74819532b914123159/static%203a04c6361b6c4add9f704d40531fb646.md)

[Multiple constructors](Python%20f5fe14898d744a74819532b914123159/Multiple%20constructors%2079607dfe6cc04716a7be3d440467da28.md)

[property](Python%20f5fe14898d744a74819532b914123159/property%205753cbc032c541a999233da96b5fc56d.md)

[__**getitem__**](Python%20f5fe14898d744a74819532b914123159/__getitem__%20cf8240ebf7194fd5aeb1be41688db92b.md)

[Dataclass](Python%20f5fe14898d744a74819532b914123159/Dataclass%208305689b884f4e53ad9b186e41de00a4.md)

[args kwargs](Python%20f5fe14898d744a74819532b914123159/args%20kwargs%2086abf9d6ded6447eac977afd97c0f4f1.md)

[abstract class ](Python%20f5fe14898d744a74819532b914123159/abstract%20class%208b5f5b9d8bfe4b98b7a8ba4d36b762c2.md)

[Encapsulation ](Python%20f5fe14898d744a74819532b914123159/Encapsulation%202ee31f9534334f1ba6d9d4f56afb433d.md)

[polymorphism](Python%20f5fe14898d744a74819532b914123159/polymorphism%20b57b5ee4efdf48c7bcb82972d67e574a.md)

[Design patterns](Python%20f5fe14898d744a74819532b914123159/Design%20patterns%20e7a8b98b73084e948458ad988e47e29c.md)

---

- Modify weights in-place
    
    ```
    v[...] = torch.clamp(v, min=weights_copy[k] - eps, max=weights_copy[k] + eps)
    ```
    
    This operation clamps the values of `v` between `min=weights_copy[k] - eps` and `max=weights_copy[k] + eps`.,  where eps is the norm constraint specified in hparams (from a file). The ellipsis (`[...]`) in the left-hand side of the assignment indicates that the values of `v` should be modified in place.
    
    The weights are modified in place because it is more efficient than creating a new tensor with the modified values. Therefore, it is a memory-efficient way to modify the tensor without creating a new tensor.
    

- shallow vs deep copy
    
    The issue you're encountering is due to the mutable nature of Python dictionaries within lists. When you perform `out = data_list.copy()`, this creates a shallow copy of the list. A shallow copy means that while the list itself is a new list, the elements (dictionaries in this case) inside the list are still references to the original dictionaries in `data_list`.
    
    So, when you iterate over `out` and modify the dictionaries (`item`), these changes are reflected in the original dictionaries in `data_list`, because both lists contain references to the same dictionary objects.
    
    To avoid this, you need to create a deep copy of `data_list`. A deep copy creates new instances of the objects within the list, so modifying the copied list won't affect the original list. You can use the `copy` module for this. Here is how you can modify your function:
    
    ```python
    import copy
    
    def replace_month_names(data_list):
        out = copy.deepcopy(data_list)
        # ... rest of your function ...
    
    ```
    
    Using `deepcopy`, each dictionary within `out` is a new instance, and modifying it won't affect the dictionaries in the original `data_list`.
    

NOTE: if we set a default arg in a function, if that arg var changes outside of it, you need to run the fn again