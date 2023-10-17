# RNNs and LSTMs are slow to train

PROB:

LSTMs are slow to train, sometimes slower than RNNs. They both take input sequentially one by one, which is not able to use up GPU’s very well, which are designed for parallel computation.

---

SOLN:

Use attention to focus on the relevant part of the input sequence as needed.
Transformers uses multi-headed attention layer

REF:

[https://towardsdatascience.com/transformer-neural-network-step-by-step-breakdown-of-the-beast-b3e096dc857f](https://towardsdatascience.com/transformer-neural-network-step-by-step-breakdown-of-the-beast-b3e096dc857f)

---

SOLN:

Transformers- One main difference is that the input sequence can be passed in parallel so that GPU can be utilized effectively, and the speed of training can also be increased.

We can pass all the words of a sentence simultaneously and determine the word embedding simultaneously

REASONING: 

How can we parallelize sequential data?

REF:

[https://towardsdatascience.com/transformer-neural-network-step-by-step-breakdown-of-the-beast-b3e096dc857f](https://towardsdatascience.com/transformer-neural-network-step-by-step-breakdown-of-the-beast-b3e096dc857f)

---