# Transformer Feed-Forward Layers Are Key-Value Memories

[https://github.com/mega002/ff-layers/](https://github.com/mega002/ff-layers/)

- GPT failures
    
    [https://www.notion.so/GPT-4-2890fb0c171b4179b0db779ac4e6f1c1?pvs=4#69e7c57e8d74411983db6321f2257f0a](https://www.notion.so/Failures-2890fb0c171b4179b0db779ac4e6f1c1?pvs=21)
    
    ![Untitled](../../Using%20GPT%20models%20927375e848ef4e22b160a9599f319af5/Failures%20a0e9fb20cd944c758b975221e7976553/Untitled.png)
    
    ![Untitled](Transformer%20Feed-Forward%20Layers%20Are%20Key-Value%20Memo%200a97101d5550430d8ef5e0a4c8016253/Untitled.png)
    

- Given an input vector x, why is the probability distribution P(k | x) for vector k in modeled as an exponential distribution of exp(x dot k)? (Section 2)
    
    [https://www.notion.so/Choosing-a-distribution-fccc2243602e4099a0ff6092e96aa49f?pvs=4#56df07aa626b4814bec0eda358bc0a3c](../../Math%2089624985ddb64f0c91c334b1ab5df1d0/Probability%2055dc8908e9204acfbb1013eb383fb72b/Choosing%20a%20distribution%20fccc2243602e4099a0ff6092e96aa49f.md)
    
    One common assumption is that the probabilities of different outcomes (represented by the elements of k) are related to their "utility" or "value" to the decision maker, which is a function of the input vector x. For example, in a binary classification task where k represents the two possible classes, the utility of each class could be a linear combination of features in the input vector x.
    
    Under this assumption, the probability of a given outcome k is proportional to the exponentiated utility of that outcome. The exponential function is a natural choice for this proportional relationship because it is always positive and monotonically increasing, so it can represent a positive value of utility.
    
    In other words, the probability of k given x can be written as:
    
    P(k | x) ∝ exp(x dot k)
    
    where the constant of proportionality ensures that the probabilities sum up to 1 over all possible outcomes.
    
    It is worth noting that this exponential model is just one of many possible ways to model the relationship between the input vector x and the probability distribution over outcomes. Depending on the task and the specific assumptions about the relationship between x and k, different models may be more appropriate.