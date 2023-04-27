# Get the distribution of hidden state activations

SOLN (SUM):

Compute the moment statistics of hidden state vector samples

<<<

SOLN (DET):

In order to fully characterize the distribution of the hidden state activations in a model, we need both the mean (or first moment) and the variance (or second moment). *FOOTNOTE

The second moment statistics are used to analyze the hidden state representations of an autoregressive transformer language model. Specifically, the authors compute the second moment statistics 

$$
C ∝ E[kk^T]
$$

where k is a vector representing a hidden state activation in the model.

The second moment statistics provide information about the distribution of hidden state activations in the model. By computing these statistics using 100,000 samples of hidden states computed from tokens sampled from all Wikipedia text in-context, the authors are able to analyze how factual associations are stored and recalled in the model.

The samples of hidden state vectors are collected by: 

1. Selecting a random sample of Wikipedia articles from a snapshot of Wikipedia and running each article through the transformer up to its buffer length. 
2. Then, all fan-out MLP activations for every token in each article are collected at float32 precision. 
3. The process is repeated until 100,000 vectors have been sampled.

<<<

WHY:

The second moment statistics, also known as the variance, provide information about the spread of the distribution of the hidden state activations in a model. The variance measures how much the individual values in a dataset differ from the mean of the dataset.

The hidden state activations can be thought of as the output of the model at each layer. If the variance of the hidden state activations is very low, it suggests that the model is not able to capture much variation in the input data, and is potentially underfitting. On the other hand, if the variance is very high, it may indicate that the model is overfitting and is too sensitive to noise in the input data.

<<<

REF:

[ROME: Locating and Editing Factual Associations in GPT](https://www.notion.so/ROME-Locating-and-Editing-Factual-Associations-in-GPT-5538511ecf24401ca32fd06b20eb2b42) 

---

NOTE:

To get the distribution of hidden state vectors in PyTorch, you can do the following:

```python
import torch

# Assume hidden states are stored in a tensor called `hidden_states` with shape (batch_size, num_layers, hidden_size)

# Flatten the hidden states tensor to shape (batch_size, num_layers * hidden_size)
hidden_states_flat = hidden_states.reshape(hidden_states.shape[0], -1)

# Calculate the mean and variance of the hidden state activations
hidden_mean = torch.mean(hidden_states_flat, dim=0)
hidden_var = torch.var(hidden_states_flat, dim=0)
```

This code first flattens the hidden states tensor along the layer and hidden size dimensions to obtain a 2D tensor with shape **`(batch_size, num_layers * hidden_size)`**. Then, it calculates the mean and variance of the flattened tensor along the batch size dimension using the **`torch.mean`** and **`torch.var`** functions, respectively.

To get a more complete description of the distribution of the hidden state activations, you can also plot a histogram of the flattened tensor:

```python
import matplotlib.pyplot as plt

plt.hist(hidden_states_flat.cpu().numpy().flatten(), bins=50)
plt.xlabel("Hidden state activations")
plt.ylabel("Frequency")
plt.show()
```

This code first converts the flattened hidden states tensor to a NumPy array using the **`cpu()`** method.