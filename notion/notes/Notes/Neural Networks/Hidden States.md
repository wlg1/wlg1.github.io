# Hidden States

A hidden state in a neural network refers to the output of a layer of neurons after processing a particular input.

So, a hidden state is not itself a neuron, but rather a vector of numbers representing the output of multiple neurons in a layer.

Each layer has multiple hidden states, one for each token in the input sequence.

---

### Transformer hidden states

Tokens are typically passed through the network one at a time in a sequence.

How does the hidden state 1 of token 1 affect hidden state 1 of token 2?

The hidden state of a token at position t in the sequence is calculated as a function of its input token embedding, the hidden state of the previous token at position t-1, and the hidden states of all previous tokens in the sequence up to position t-1. This allows the model to capture dependencies and relationships between tokens across the entire sequence.

$$
h_t = f(h_{t-1}, x_t, C_t)
$$