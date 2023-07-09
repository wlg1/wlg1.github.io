# In-context Learning and Induction Heads

- What are induction heads and in-context learning? Relation to analogy making?
    
    > *induction head*, a circuit whose function is to look back over the sequence for previous instances of the current token (call it `A`), find the token that came after it last time (call it `B`), and then predict that the same completion will occur again (e.g. forming the sequence `[A][B] … [A] → [B]`)
    > 
    
    Similar to analogies, but find complete using exact same token, not analogous one
    
    > Mechanically, induction heads in our models are implemented by a circuit of two attention heads: the first head is a “previous token head” which copies information from the previous token into the next token, while the second head (the actual “induction head”) uses that information to find tokens preceded by the present token.
    > 
    
    > When induction heads occur in sufficiently large models and operate on sufficiently abstract representations, the very same heads that do this sequence copying *also* take on a more expanded role of *analogical sequence copying* or *in-context nearest neighbors.* 
    By this we mean that they promote sequence completions like `[A*][B*] … [A] → [B]` where `A*` is not exactly the same token as `A` but similar in some embedding space, and also `B` is not exactly the same token as `B*`.
    > 
    
    THIS is completing analogies ?
    
    [https://news.mit.edu/2023/large-language-models-in-context-learning-020](https://news.mit.edu/2023/large-language-models-in-context-learning-020)
    
    [https://arxiv.org/pdf/2211.15661.pdf](https://arxiv.org/pdf/2211.15661.pdf)
    
    in-context learning, in which **a large language model learns to accomplish a task after seeing only a few examples** — despite the fact that it wasn't trained for that task
    
    [https://www.scribbr.com/methodology/inductive-reasoning/](https://www.scribbr.com/methodology/inductive-reasoning/)
    
    inductive reasoning: by going from the specific to the general.
    

For example, given “The cat sat on the mat. The cat …”, induction heads will promote the continuation “sat on the mat”.

Kaplan et al: “Decreasing loss at incrasing token indices” because with more context, model is more sure what the specifics are

We verify that these heads score highly on our [“copying” and “prefix matching” evaluations](https://transformer-circuits.pub/2022/in-context-learning-and-induction-heads/index.html#head-activation-evaluators) (that is, they increase the probability of the token they attend to, and attend to tokens where the prefix matches the present token on random text)

![Untitled](In-context%20Learning%20and%20Induction%20Heads%20f6c26430e69948fd9168457739f3e173/Untitled.png)

- Prefix Matching: “node” (A) is the prefix. “structuion” (B) is copied

• **Copying.** Does the head’s direct effect on the residual stream increase the logits of the same token as the one being attended to?

- What does it mean for an attention head to “copy a token”?
    
    When an attention head "copies a token," it means that it assigns a relatively high attention weight to a specific token in the input sequence, indicating that the information from that token is considered important for further processing. In other words, the attention head is focused on that particular token and will incorporate its information into subsequent computations (to the output)
    
    When the model copies a token B, it is more likely to output B again.
    

**Per-token loss**

Each snapshot is a model, and has a vector of losses for each token. Each element is one token from one example

Q: What decides which token to take from each example?

Q: What does this have to do wtih function spaces?

> Since we're using PCA, each direction can be thought of as a vector of log-likelihoods that models are moving along
> 

********************************Argument summary********************************

For smaller models, we use ablations and other technqs to find examples and correlations of induction heads. But for larger models, there are too many other heads to show that these induction heads account for most of the in-context learning. So we can only rely on correlation, which has the downside of having confounded variables.

- Argument 1: During phase change when induction heads form, in-context learning improves dramatically [correlation]
- Argument 2: When we change arch to change if and when induction heads form, in-context learning improvement ALSO shifts dramatically [correlation upon change]
- Argument 3: When we remove induction heads after training, in-context learning greatly decreases [correlation upon ablation]

********************Argument 1********************

In-context learning score: the loss of the 500th token in the context minus the average loss of the 50th token in the context, averaged over dataset examples. Measured in nats

y-axis: loss(500th token in input) - avg_loss(50th token in input)

b/c 50th to 500th is the “in-context window” (where examples are provided)

we expect the first term < second term, so (first term - second term) < 0

Thus, the more negative this value is, the better the model gets

x-axis: total tokens in training dataset (10,000,000,000 = 10 billion)

- In transformers, as each token is added during training, do they always use all the previous tokens from the training set as part of the input? That is, all the tokens are part of one linear sequence in the training dataset. So the 1st token from a book and the 1 million token from a webpage are considered in one sequence. Or is there way some way to separate the context they came from?
    
    In transformer models like GPT-3, the training data is not treated as one long continuous sequence. Instead, the data is broken up into smaller chunks or sequences, often referred to as "windows" or "contexts". Each of these sequences is processed independently during training.
    
    The length of these sequences is determined by the model's "context window" size, which is a fixed number of tokens. For example, GPT-3 has a context window of 2048 tokens. This means that when the model is being trained, it considers a sequence of 2048 tokens at a time. The model does not have any awareness of tokens outside of this window.
    
    So, to answer your question, the 1st token from a book and the 1 millionth token from a webpage would not be considered in the same sequence, unless they happen to fall within the same 2048-token window, which is highly unlikely if they are from different sources.
    
    It's also important to note that these sequences are typically constructed in a way that respects the boundaries of individual documents. That is, sequences would not typically span across the boundary between two different documents (like a book and a webpage). This helps to ensure that each sequence has a coherent and meaningful context.
    
    In terms of "separating the context they came from", the model does not have an explicit mechanism for tracking the source of each sequence. However, the way the sequences are constructed (i.e., not spanning across document boundaries) helps to ensure that the context is preserved to some extent.
    

The loss function measures value between the predicted output and the desired output.

The training dataset contains token sequences and the correct token is the next one.

- For transformers, what's nats ?
    
    In the context of transformers, "nats" refers to a unit of measurement called "natural units" or "nats" (short for natural logarithm units). It is a logarithmic scale used to measure the amount of information or entropy in a probability distribution.
    
    The term "nats" comes from the natural logarithm, which is denoted as "ln" and has a base of "e" (approximately 2.71828). In contrast to nats, another commonly used unit of measurement for information is "bits," which is based on the binary logarithm with a base of 2.
    
    In the context of transformers, nats are often used to quantify the entropy or uncertainty associated with the predicted probability distributions over different tokens in language models. When training a transformer model, the goal is often to minimize the cross-entropy loss, which is typically measured in nats. This loss function encourages the model to assign higher probabilities to the correct tokens and lower probabilities to incorrect ones during training.
    
    Nats provide a convenient way to measure information and model performance, and they are particularly useful when dealing with logarithmic quantities and probability distributions.
    
- What's an example of comparing nats?
    
    Comparing nats involves comparing the entropy or uncertainty associated with different probability distributions. Here's an example to illustrate the concept:
    
    Let's consider two probability distributions A and B over a set of three events: {E1, E2, E3}. The probabilities associated with each event for distribution A are {0.6, 0.2, 0.2}, and for distribution B, they are {0.4, 0.4, 0.2}.
    
    To compare these distributions in terms of nats, we can calculate the entropy for each distribution using the formula:
    
    Entropy = -Σ(p(x) * log(p(x)))
    
    where p(x) is the probability of event x.
    
    For distribution A:
    Entropy(A) = -(0.6 * log(0.6) + 0.2 * log(0.2) + 0.2 * log(0.2))
    ≈ 1.281 nats
    
    For distribution B:
    Entropy(B) = -(0.4 * log(0.4) + 0.4 * log(0.4) + 0.2 * log(0.2))
    ≈ 1.485 nats
    
    From these calculations, we can see that distribution B has a higher entropy (uncertainty) compared to distribution A, as it has a more uniform probability distribution. This means that distribution B is less predictable or has more information content compared to distribution A.
    
    By comparing the entropy (measured in nats) of different probability distributions, we can evaluate the level of uncertainty or information content associated with each distribution.
    
- How to measure cross entropy loss of transformers in nats?
    
    The cross-entropy loss of transformers is typically measured in nats. Here's an overview of how it is calculated:
    
    1. Probability Distribution: Transformers generate probability distributions over the possible tokens in a sequence. These distributions represent the model's predictions for each token position.
    2. True Labels: During training, you have the ground truth or true labels for each token position in the sequence.
    3. Cross-Entropy Loss Calculation: To measure the model's performance, you calculate the cross-entropy loss between the predicted probability distribution and the true labels.
        
        a. For each token position, you have the predicted probability distribution over the tokens.
        
        b. You extract the true label for that token position.
        
        c. You calculate the negative log-likelihood of the true label under the predicted distribution.
        
        d. Repeat this process for all token positions and average the losses.
        
    4. Conversion to Nats: The resulting loss value is typically reported in nats. This conversion is achieved by dividing the calculated loss by the natural logarithm of the base of the probability distribution.
        
        Cross-Entropy Loss in Nats = Cross-Entropy Loss in Bits / ln(2)
        
        Here, ln(2) is the natural logarithm of 2, which is approximately 0.6931.
        
    
    By measuring the cross-entropy loss in nats, you can assess the model's ability to predict the true labels and minimize the uncertainty or entropy associated with the token distributions.
    

********************Argument 3********************

This is causal because it’s saying when we knock out JUST this variable and NO OTHER VARIABLES, there is a big change. This reduces the possibility of confounding variables causing the change (it isolates the effect).

It’s still possible for there to be confoudning vars:

- Could be something within; a subset of what was knocked out
- Ablating causes an indirect change in confoudning vars too, so it’s not frozen. we just don’t know what the confounding vars are

---

[https://www.youtube.com/watch?v=dCkQQYwPxdM&t=2099s&ab_channel=NeelNanda](https://www.youtube.com/watch?v=dCkQQYwPxdM&t=2099s&ab_channel=NeelNanda)

****A Walkthrough of In-Context Learning and Induction Heads Part 1 of 2 (w/ Charles Frye)****

48m: One reason the 2nd mysterious attends to “,because” instead of “mysterious” in the 1st “mytserious, because” may be because it wants to look ahead to make sure it’s the same type of “mysterious”; it may deviate into “mysterious-like”, which is different (?)

Per-token-loss: to plot how loss for each token changes over training

1hr: just adding one bit allows a lot more encoding of info (2^n, n=#bits)

exponentially “sure”: adding one more bit of evidence means 2x more sure

1h2m:  Cross entropy transforms the multiplicative updates that you would do in accumulating evidence in a Bayesian way into additive updates as if you're working in that log space

There's an n-category Cafe article about this as a full and faithful functor 

[https://golem.ph.utexas.edu/category/2014/02/relative_entropy.html](https://golem.ph.utexas.edu/category/2014/02/relative_entropy.html)