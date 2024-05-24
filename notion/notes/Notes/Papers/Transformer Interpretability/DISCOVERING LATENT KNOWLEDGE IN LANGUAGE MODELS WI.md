# DISCOVERING LATENT KNOWLEDGE IN LANGUAGE MODELS WITHOUT SUPERVISION

[DISCOVERING LATENT KNOWLEDGE IN LANGUAGE MODELS WITHOUT SUPERVISION](https://www.notion.so/DISCOVERING-LATENT-KNOWLEDGE-IN-LANGUAGE-MODELS-WITHOUT-SUPERVISION-108c41fcaddf4711b4a7e98236c2b65f?pvs=21) 

---

![Untitled](DISCOVERING%20LATENT%20KNOWLEDGE%20IN%20LANGUAGE%20MODELS%20WI%20eed91d92cd5a40faace804ecb780819c/Untitled.png)

- Why: "However, because we use a soft consistency constraint, these may not be exactly equal.”
    
    The statement "However, because we use a soft consistency constraint, these may not be exactly equal" refers to the probabilities $p(x_i^+)$ and $1 - p(x_i^-)$, which ideally should both represent the probability that the answer to a question $$q_i$$ is "Yes". A soft consistency constraint means that while the model is encouraged to make these probabilities similar, it is not forced to make them exactly the same.
    
    In a strict or hard consistency scenario, the model would be constrained in such a way that $p(x_i^+)$ would have to equal $1 - p(x_i^-)$ exactly, enforcing a very rigid rule that the probabilities of a positive and the complement of a negative example must sum to one, reflecting complete certainty.
    
    However, in many practical applications, such strict constraints can be too limiting and may not reflect the complex, often noisy nature of real-world data. Soft constraints are more flexible; they guide the model towards certain behaviors (like making $$p(x_i^+)$$ and $$1 - p(x_i^-)$$ similar) without demanding perfect adherence. This approach acknowledges that the model might encounter data or situations where a strict interpretation doesn't make sense or isn't possible due to the underlying data distribution or noise.
    
    Therefore, when the statement refers to these probabilities not being exactly equal, it is recognizing that the model, due to the soft constraint, is allowed some degree of variance in its predictions for $$p(x_i^+)$$ and $$1 - p(x_i^-)$$, which can be beneficial for the model's ability to generalize from the training data to unseen data.
    

---

![Untitled](DISCOVERING%20LATENT%20KNOWLEDGE%20IN%20LANGUAGE%20MODELS%20WI%20eed91d92cd5a40faace804ecb780819c/Untitled%201.png)

- [https://chat.openai.com/c/cf7da345-01fd-42c4-a6fd-b4dea3c1b6a4](https://chat.openai.com/c/cf7da345-01fd-42c4-a6fd-b4dea3c1b6a4)
    
    The text in the image is discussing a process of feature extraction and normalization in the context of contrast pairs, denoted as \( x_i^+ \) and \( x_i^- \). These pairs are processed by a feature extractor \( \phi(\cdot) \).
    
    Normalization is a statistical technique that modifies the values in a dataset to a common scale, without distorting differences in the ranges of values. Here are the reasons why normalizing \( \phi(x_i^+) \) and \( \phi(x_i^-) \) independently removes the effect of the first condition:
    
    1. **Different Baselines**: The "+" and "−" instances are likely to have different statistical properties due to their different outcomes ("Yes" and "No"). If these properties (mean \( \mu \) and standard deviation \( \sigma \)) are not adjusted, any comparison between \( x_i^+ \) and \( x_i^- \) might be biased by these baseline differences rather than the actual features of interest.
    2. **Scale Adjustment**: Normalizing each representation independently with their respective means (\( \mu^+ \) and \( \mu^- \)) and standard deviations (\( \sigma^+ \) and \( \sigma^- \)) adjusts the scale so that features are centered around zero and have a unit variance. This scaling ensures that the features of \( x_i^+ \) and \( x_i^- \) can be compared without the scale of the original measurements distorting the results.
    3. **Reducing Variance**: Different variances between \( \phi(x_i^+) \) and \( \phi(x_i^-) \) can also affect comparison. By dividing by the standard deviation, this normalization reduces the problem of features having different variances.
    4. **Equitable Comparison**: Once normalized, the feature vectors \( \tilde{\phi}(x_i^+) \) and \( \tilde{\phi}(x_i^-) \) can be compared or combined more fairly in subsequent analysis because they are in the same "unit" scale.
    5. **Removing Confounding Effects**: Independent normalization removes the confounding effects of (1), where the distinct endings ("Yes" and "No") might introduce systemic differences in the feature representations. By normalizing separately, these systemic differences are mitigated, allowing for the true underlying pattern that is of interest (condition (2)) to be more readily identified in the data.
    
    In essence, independent normalization aims to ensure that the comparison between \( x_i^+ \) and \( x_i^- \) is based on the intrinsic properties of the data related to the feature of interest, rather than extrinsic properties introduced by the different outcomes or scales inherent to the "+" and "−" data points.
    
    The effect of (1) mentioned in the image is that \( x_i^+ \) ends with "Yes" while \( x_i^- \) ends with "No". This indicates that the raw feature representations \( \phi(x_i^+) \) and \( \phi(x_i^-) \) may include some inherent biases or characteristics that are specific to the "Yes" or "No" outcomes. These could be systematic differences in the data that are not relevant to the actual feature or pattern of interest, which in this case is effect (2).
    
    By normalizing \( \phi(x_i^+) \) and \( \phi(x_i^-) \) independently, you effectively remove these inherent biases because normalization is about adjusting the data to a common scale and zero-centered distribution. Here's how it specifically addresses effect (1):
    
    - **Mean Subtraction (\( \mu \))**: Subtracting the mean from each feature vector ensures that the positive and negative examples start from a zero baseline. Since the mean is a measure of central tendency, subtracting it removes any bias introduced by the different endings ("Yes" or "No"). This makes the resulting features centered around zero, which neutralizes the baseline effect of the "Yes" or "No" answers.
    - **Division by Standard Deviation (\( \sigma \))**: By dividing by the standard deviation, we scale the feature vectors so that they have a unit variance. This step ensures that the spread of the data is consistent across both positive and negative examples, removing any scaling effects due to the outcome-based differences.
    
    Normalization does not remove the effect of (2) because effect (2) is presumably the actual feature or pattern we want to find in the data after removing the irrelevant differences due to outcome-based biases (effect (1)). After normalization, the data can be more accurately compared or used in further analysis because the starting point (mean) and scale (variance) have been standardized, leaving the variation due to the true signal (effect (2)) more intact and discernible.