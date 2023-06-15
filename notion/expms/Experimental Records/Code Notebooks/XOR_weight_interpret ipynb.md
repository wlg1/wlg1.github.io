# XOR_weight_interpret.ipynb

[https://colab.research.google.com/drive/1bxoPm1pRYgA67UdhXOdnGIuH_2qo_QN7](https://colab.research.google.com/drive/1bxoPm1pRYgA67UdhXOdnGIuH_2qo_QN7)

Table of Contents:

**[Use a NN to model XOR](https://colab.research.google.com/drive/1bxoPm1pRYgA67UdhXOdnGIuH_2qo_QN7#scrollTo=Use_a_NN_to_model_XOR)**

[Get activations](https://colab.research.google.com/drive/1bxoPm1pRYgA67UdhXOdnGIuH_2qo_QN7#scrollTo=Get_activations)

[Compare different input activations](https://colab.research.google.com/drive/1bxoPm1pRYgA67UdhXOdnGIuH_2qo_QN7#scrollTo=Compare_different_input_activations)

[Why does this input change cause this difference?](https://colab.research.google.com/drive/1bxoPm1pRYgA67UdhXOdnGIuH_2qo_QN7#scrollTo=Why_does_this_input_change_cause_this_difference_)

```python
WX_hadamard = torch.multiply(model.fc1.weight.data, input_2)
```

- Obtains each neuron’s contribution (w*x) to next layer’s neurons
- WX is a vector of two elements.
    
    [w11 + w12]
    
    [w21 + w22]
    
- The hadamard(W, X) has four elements:
    
    [w11, w12]
    
    [w21, w22]
    

[0, 0] and [1, 1] have the SAME neuron outputs after fc1. Let's look at the weights of fc1 again to see why that's the case:

The first element of WX, w11+w12, is 0 or close to 0.
The second element, w21+w22, is also close to 0.
So the weights were learned to make sure $w_{11} + w_{12}$ was close to 0, as ReLU would turn that into 0.
Then in fc2 (output node), the bias is negative so that sigmoid makes it less than 0. 
But for [0,1] and [1,0], w11 + w12 is nonzero. The more different they are, the more one will be expressed than the other. But when x1 and x2 are close, because w11 and w12 are also close, the first output of fc1 $w_{11} * x_1 + w_{12} * x_2$ is close to 0.

[Why does the hidden layer use two elements?](https://colab.research.google.com/drive/1bxoPm1pRYgA67UdhXOdnGIuH_2qo_QN7#scrollTo=Why_does_the_hidden_layer_use_two_elements_)

[Gradual input modification](https://colab.research.google.com/drive/1bxoPm1pRYgA67UdhXOdnGIuH_2qo_QN7#scrollTo=Gradual_input_modification)

[Try training it again and look at the weights](https://colab.research.google.com/drive/1bxoPm1pRYgA67UdhXOdnGIuH_2qo_QN7#scrollTo=Try_training_it_again_and_look_at_the_weights)

[Manually modify weights to try to create XOR, based on conditions](https://colab.research.google.com/drive/1bxoPm1pRYgA67UdhXOdnGIuH_2qo_QN7#scrollTo=Manually_modify_weights_to_try_to_create_XOR_based_on_conditions)

---

Related Work:

The Algebraic Mind, ch2

![Untitled](XOR_weight_interpret%20ipynb%20bf8ac65466fe4eb9a255a26ec920bad2/Untitled.png)

XOR: Composed of AND and OR gate circuits in 2-layer arch