# Loss Function

- log_softmax
    
    We need to know what log_softmax does so that when we modify the loss fn for new tasks, we need to know if we need to modify log_softmax, and if so, how.
    
    Let logits have dim [batch_size=2, seq_len=3, vocab_size=4]
    
    Each batch of logits is a 2-dimensional tensor with shape `[3, 4]`. The "last dimension" in this context refers to the innermost dimension when the tensor is viewed as a nested list, which is the dimension with size `4` in this case. Each inner list (or row) has four elements.
    
    When operations like `softmax` or `log_softmax` are applied along the last dimension (`dim=-1`), they are performed independently on each row.
    
    For each list, the operation converts these values into a probability distribution, where each element is a probability corresponding to a class or category, typically in a machine learning classification task. In this case, each row could represent the log probabilities of different classes for a specific instance or time step in a sequence.
    
    ![Untitled](Loss%20Function%20e75bb14ae1cf419294c3327de8c86c9b/Untitled.png)
    

---

[https://builtin.com/machine-learning/common-loss-functions](https://builtin.com/machine-learning/common-loss-functions)

Mean _ error loss functions: the average of **differences between the actual and the predicted value**

---

Likelihood is the probability of observing the data x given a particular set of model parameters θ

$$
L(θ | x) = p(x | θ)
$$

Formally, “likelihood” is just a type of probability. There seems to be no other way to define it. Its equations are built on the equations of the probability function. So ignore what “L(θ | x)” intuitively means without the context of probability because there doesn’t seem to be one. That is, likelihood is not entirely different from prob, it’s just a type of prob. Just always think of likelihood as meaning “p(x | θ)”.

[https://stats.stackexchange.com/questions/2641/what-is-the-difference-between-likelihood-and-probability](https://stats.stackexchange.com/questions/2641/what-is-the-difference-between-likelihood-and-probability)

> However, when we model a real life stochastic process, we often do not know θ. We simply observe x and the goal then is to arrive at an estimate for θ that would be a plausible choice given the observed outcomes x.
> 

This is why instead of asking p(x | θ), we semantically think of it as L(θ | x). But when we calculate it, we are FINDING (by maximum likelihood or a similar method) the θ to maximize p(x | θ), which we can calculate. We are NOT calculating p(θ | x)  [though that may be est with Bayes’]

---

[https://stats.stackexchange.com/questions/181035/how-to-derive-the-likelihood-function-for-binomial-distribution-for-parameter-es](https://stats.stackexchange.com/questions/181035/how-to-derive-the-likelihood-function-for-binomial-distribution-for-parameter-es)

[https://medium.com/deeplearningmadeeasy/negative-log-likelihood-6bd79b55d8b6](https://medium.com/deeplearningmadeeasy/negative-log-likelihood-6bd79b55d8b6)

[https://towardsdatascience.com/cross-entropy-negative-log-likelihood-and-all-that-jazz-47a95bd2e81](https://towardsdatascience.com/cross-entropy-negative-log-likelihood-and-all-that-jazz-47a95bd2e81)

- What is Cross Entropy Loss? Why not just subtract the probability distributions from one another?
    
    It measures the difference between two probability distributions, typically the predicted probability distribution outputted by a model and the true probability distribution of the labels.
    
    The reason why we don't just subtract the probability distributions from one another is that this would not necessarily result in a meaningful loss function. In particular, it would not have the properties we typically want in a loss function, such as being non-negative and having a global minimum.
    
    Cross-entropy loss is defined as the negative log-likelihood of the true labels given the predicted probabilities. 
    
    In other words, it measures the amount of surprise we experience when we observe the true labels given the model's predictions. This loss function has a number of desirable properties, such as being non-negative and having a unique global minimum.
    
    - What is "surprise"? Use an analogy
        
        "Surprise" refers to the unexpectedness or unpredictability of the true labels given the predicted probabilities. 
        
        Imagine that you are playing a game where you have to guess which color of M&M candy will come out of a bag. You know that the bag contains five colors of M&Ms: red, green, blue, yellow, and brown. Before you guess, your friend tells you that the bag is biased, meaning that some colors are more likely to be picked than others. Specifically, your friend tells you that the probabilities of each color are as follows: red (0.1), green (0.2), blue (0.3), yellow (0.25), and brown (0.15).
        
        Suppose that you guess that a blue M&M will come out of the bag, and your friend then reveals that a green M&M was actually picked. You might feel surprised, because the green M&M was less likely to be picked than the blue M&M according to the probability distribution. On the other hand, if your guess had been yellow, you might have felt less surprised, because the yellow M&M was more likely to be picked according to the probability distribution.
        
        In the context of cross-entropy loss, surprise is measured as the negative log-likelihood of the true label given the predicted probabilities. In our analogy, this would correspond to the surprise you feel when you observe the green M&M given the predicted probabilities. The greater the surprise, the higher the cross-entropy loss, and the worse the model's predictions.
        
    
    Mathematically, if we have a true probability distribution p and a predicted probability distribution q, the cross-entropy loss is defined as:
    
    $$
    H(p, q) = -∑i p_i log(q_i)
    $$
    
    where p_i is the true probability of the i-th class and q_i is the predicted probability of the i-th class.
    
    By minimizing the cross-entropy loss, we can train our model to make more accurate predictions, and in particular, to minimize the surprise we experience when observing the true labels.
    

---

- Are logits measured in nats?
    
    In the context of neural networks and machine learning, the term "logits" refers to the output values of a model before they are transformed by a probability distribution function (such as softmax) into probabilities. Logits can be measured in various units depending on the specific problem and the activation function used in the output layer of the model.
    
    Typically, logits are not measured in nats by default. The measurement of logits depends on the chosen activation function and the problem domain. For example, in binary classification problems, logits may represent log-odds or logit scores, which are not inherently measured in nats. In multi-class classification problems, logits can represent unnormalized class scores or log-probabilities.
    
    On the other hand, the natural logarithm (ln) is commonly used in the softmax function, which is often applied to logits to transform them into probabilities. The natural logarithm has the base of e, where e is Euler's number approximately equal to 2.71828. Therefore, the softmax function with natural logarithm can produce probabilities measured in nats.
    
    In summary, while logits themselves are not inherently measured in nats, the use of the natural logarithm in the softmax function, applied to logits, can result in probabilities measured in nats.