# 0.3 code

**Build Your Own Optimizers**

in-place modifies the var itself in storage

When the optimizer makes changes to the param tensors, it must use the old tensor to calculate momentum. If your optimizer allocates a new tensor, the model won't know anything about the new tensor and will continue to use the old, unmodified version. Thus, use in-place `x += y`

For non-parameter tensors, use can `x = x + y` which is not in-place

---

self.params is not indexed by t, it is a list. Think of it as a vector usually; since not vector here, must use loop instead of tensor operation. Pseudocode says indexed by t but that’s the entire vector by t

step is by t

floating zeros has error; why use None

`param.grad = t.zeros_like(param)`

zeros_like makes a tensor with that shape, whereas zeros gives the shape

![Untitled](0%203%20code%20dcea764934cc4ea1924c48629e426fc0/Untitled.png)