# Optimizers

**`opt.step()`** is a method of the optimizer that updates the values of the model parameters based on the gradients computed during backpropagation. In other words, it performs the gradient descent step to update the weights of the model.

After computing the gradients with **`loss.backward()`**, the optimizer updates the model parameters with the command **`opt.step()`**. This operation adjusts the weights of the model in the direction of the negative gradient, reducing the loss and improving the performance of the model.

---

[https://www.youtube.com/watch?v=JhQqquVeCE0&ab_channel=DigitalSreeni](https://www.youtube.com/watch?v=JhQqquVeCE0&ab_channel=DigitalSreeni)

Gradient Descent is old; now most use Adam 

---

Learning rate decay: after several epochs, get closer to solution, so no need to shoot that far. Search closer to solution, which means smaller steps, represented by lower learning rate.