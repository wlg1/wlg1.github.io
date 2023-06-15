# Self-attention

The self-attention mechanism computes the dot product between the query vector of a token and the key vectors of all tokens, including itself, in the sequence. This operation measures the similarity or relationship between the tokens.

These attention weights are then multiplied by the value vectors (V), and the resulting vectors are summed up to produce the output for each token. This output is a weighted combination of the input hidden states, where the weights are determined by the attention mechanism. In this way, the dot product allows hidden states to affect each other based on the relationships between the tokens in the sequence.

- Causal Attention
    
    Causal attention is a type of attention mechanism used in Transformer models, particularly when dealing with sequential data, such as text or time series. It's designed to enforce a specific kind of ordering in the attention mechanism, ensuring that tokens can only attend to their past context, preventing any future information from being incorporated.
    
    In standard self-attention, every token can attend to all other tokens in the sequence, making it bidirectional. However, when modeling sequences in a generative or autoregressive setting, it is crucial to prevent the model from having access to the future tokens during training and inference. This is where causal attention comes in.
    
    Causal attention is implemented by modifying the self-attention mechanism in the following way:
    
    1. Masking: A mask is applied to the attention scores, effectively setting the scores for future tokens to negative infinity (or a very large negative value) before the softmax operation. This results in a probability of nearly zero for future tokens, ensuring that they don't contribute to the output representation.
    2. Triangular matrix: The masking can be achieved using a lower-triangular matrix, where the main diagonal and all elements below have a value of 1, and the upper-triangular portion has a value of 0. When this matrix is applied to the dot product of the queries and keys, it ensures that each token attends only to itself and the previous tokens in the sequence.
    

---

### Attention Pattern

[REF](https://colab.research.google.com/drive/1br5wc-GQWaExgUnDIZcDarZ_zaBB-NYX#scrollTo=AmI77qenHSqU)

(query = dest, rows, key = source, cols)

upper right triangle on attn head are all 'next' tokens relative to current row

p75, rigor test

---

[Hidden States](../Hidden%20States%20db3887268cff4dbebb92c9f61ad52485.md)

---

[https://towardsdatascience.com/illustrated-self-attention-2d627e33b20a](https://towardsdatascience.com/illustrated-self-attention-2d627e33b20a)

---

[https://thegradient.pub/transformers-are-graph-neural-networks/](https://thegradient.pub/transformers-are-graph-neural-networks/)

The word's updated features are simply the sum of linear transformations of the features of all the words

![Untitled](Self-attention%2064a3e43e6ac8491f8a7ddc54a071b903/Untitled.png)

<<<

Informally, this can be thought of as follows:

$$
T_1, T_2, T_3 := "I \ am \ Bob"
$$

$$
o(T_1) = w_2 * T_2 + w_3 * T_3 = W * T
$$

Using equations for a transformer, how does hidden state 1 of token 1 affect hidden state 1 of token 2?

$$
AttentionWeight_{12} = softmax((Q1 * K2^T) / sqrt(d_k))
$$

$$
h1_{t2'} = AttentionWeight_{12} * V1 + AttentionWeight_{22} * V2
$$

Using:

Q1 = h1_t1 * W_Q
K1 = h1_t1 * W_K
V1 = h1_t1 * W_V

Q2 = h1_t2 * W_Q
K2 = h1_t2 * W_K
V2 = h1_t2 * W_V

---

https://youtu.be/mMa2PmYJlCo

Each Attention Head focuses on part of the input, such as “mountain” or “clouds”.