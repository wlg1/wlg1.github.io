# Size Comparison Congruence

dotprod_size_tokens.ipynb

[https://colab.research.google.com/drive/1rch6VaG9O1YFJT1wPjjbXyDgXizGT7WV](https://colab.research.google.com/drive/1rch6VaG9O1YFJT1wPjjbXyDgXizGT7WV)

dotprod_size_tokens_GPTsmall.ipynb

[https://colab.research.google.com/drive/18JcQcn7TKhN-1ULNjqQqvst9yJ6ZDhAA](https://colab.research.google.com/drive/18JcQcn7TKhN-1ULNjqQqvst9yJ6ZDhAA)

### Working on

- Use dot products on more than input embeddings of first layer (w/ neuron outgoing weights)
    - Try at different points of residual stream- but that’s mixed with other parts of input

Get avg of large dot prods, compare to avg of random dotprods

### Future Work

- Figure out how not using QK and just using OV gets “full attention” (look at transformer matrix pipeline diagram and work it out on idroo)
    - [https://www.notion.so/Query-Key-Value-Matrices-fe92464f6ee24068b6aaa56bb85e903e](https://www.notion.so/Query-Key-Value-Output-Matrices-fe92464f6ee24068b6aaa56bb85e903e?pvs=21)
    - If we skip the attention matrix, that’s like if the attention matrix was the identity matrix. Then that means “fully attend to”. In terms of matrix multiplication summations, what does this look like?
        - It would be Id * v = z, so v = z. The outputs are just the value matrix, and it’s copied. The value matrix contains the “content”
        - If we directly mutliply input embeddings with W_v, we get something that’s not exactly the same as input. HOWEVER, these outputs (matrix v) are unembedded into vocab space, they would be like logit outputs, and each token in vocab has a logit value. If these logit values are strong on certain words, we can say the weight matrix W_v (not v) is “giving content” (attending to? need to think abou this) those tokens?
        - Do weights in the value matrix have a semantic relation to the input vectors? Are they considered "content"?
            
            

---

Run Congruence tests

It’s still uncertain what embeddings at each intermediate output represent. Thus, we will experiment with performing vector similarity comparisons (between inputs and neuron groups) at various output areas to see if they make semantic sense. We start by comparing initial embeddings with various neurons to see if there are any significant patterns, and try to explain if these patterns are caused by things indicating how the model is representing semantic features. Some approaches might not make sense at first, but if they find patterns, they may be onto something that warrants further investigation.

Dot product tokens and feature neurons:

This is how $W_E(X)$ works: [Embeddings](https://www.notion.so/Embeddings-c4e515f0f63844d8bdd5309d041e40cf?pvs=21) 

[https://colab.research.google.com/drive/1rch6VaG9O1YFJT1wPjjbXyDgXizGT7WV#scrollTo=x-hNAqAk5KMX](https://colab.research.google.com/drive/1rch6VaG9O1YFJT1wPjjbXyDgXizGT7WV#scrollTo=x-hNAqAk5KMX) 

- Dot prod of large and huge and decline

[https://colab.research.google.com/drive/1rch6VaG9O1YFJT1wPjjbXyDgXizGT7WV#scrollTo=aFF09zMeuNFL&line=1&uniqifier=1](https://colab.research.google.com/drive/1rch6VaG9O1YFJT1wPjjbXyDgXizGT7WV#scrollTo=aFF09zMeuNFL&line=1&uniqifier=1)

The average dot product between two unrelated tokens (no spaces in front) seems to be around 0.8. So if it’s more, there is some similarity. If we try a dataset of tokens, we can obtain an average

- If the word isn't a single token, how can we get the dot product of it with other tokens?
    
    In language models like GPT-2, longer words or less common words might not be represented as a single token but rather a sequence of subword tokens. If you want to compute the dot product (or any kind of similarity) between such a word and another token or word, you would need to handle this token sequence.
    
    There are different approaches you could take. One simple approach is to average the embeddings of the subword tokens to get a single vector representation for the word, and then compute the dot product with this averaged vector. Here's an example:
    
    ```
    from transformers import GPT2Model, GPT2Tokenizer
    
    # Instantiate the model and the tokenizer
    model = GPT2Model.from_pretrained('gpt2-large')
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2-large')
    
    # Get the embeddings from the model
    embeddings = model.get_input_embeddings()
    
    # Tokenize the words and get their ids
    word1_ids = tokenizer.encode('large', return_tensors='pt')
    word2_ids = tokenizer.encode('huge', return_tensors='pt')
    
    # Get the embeddings for the tokens
    word1_embedding = embeddings(word1_ids).mean(dim=1)
    word2_embedding = embeddings(word2_ids).mean(dim=1)
    
    # Compute the dot product
    dot_product = torch.dot(word1_embedding.flatten(), word2_embedding.flatten())
    
    print(dot_product)
    
    ```
    
    This approach works reasonably well for many use cases, but note that it does not account for the context in which the word appears. A more sophisticated approach would be to use the actual output from the transformer model, which does take into account the surrounding context, but that's a more involved process.
    

[https://colab.research.google.com/github/neelnanda-io/TransformerLens/blob/main/demos/Main_Demo.ipynb#scrollTo=7hcPynASz8LO](https://colab.research.google.com/github/neelnanda-io/TransformerLens/blob/main/demos/Main_Demo.ipynb#scrollTo=7hcPynASz8LO)

Try the mean of all tokens:

[https://colab.research.google.com/drive/1rch6VaG9O1YFJT1wPjjbXyDgXizGT7WV#scrollTo=CevuC19u1tFh&line=1&uniqifier=1](https://colab.research.google.com/drive/1rch6VaG9O1YFJT1wPjjbXyDgXizGT7WV#scrollTo=CevuC19u1tFh&line=1&uniqifier=1)

Now the average is 0.4076. Perhaps taking the mean of all tokens isn’t the best.

Perhaps there’s a way to get their “final embedding”. Say “en”, “or”, “mous” are the tokens for the one word. We want the vector that’s at “mous”, after en and or are processed.

Compare dist of random one tokens vs “tall” synonomous tokens:

![Untitled](Size%20Comparison%20Congruence%20e94368b6a22a4e9e9d0d444b3c5972e5/Untitled.png)

![Untitled](Size%20Comparison%20Congruence%20e94368b6a22a4e9e9d0d444b3c5972e5/Untitled%201.png)

The “tall” synonyms seem around average.

Perhaps it’s only certain neurons that are the “middle man” making them in common. For instance, if tokens A and B don’t have big dot prod, but A with N and B with N both are high, then N finds what’s in common with them. This N is like the query and key weights.

- Using a list of dot products between a token and neuron, what are good ways to compare the similarity of lists of two tokens, such as between "large" and "tall"?
    
    When comparing the similarity of two lists of dot products between a token and neuron (assuming the lists are sorted and in the same neuron order), there are several approaches you can take. Here are a few methods:
    
    1. **Pearson Correlation Coefficient**: This measures the linear relationship between two datasets. Values always range between -1 (strong negative relationship) and 1 (strong positive relationship). A value near 0 implies weak or no linear relationship.
    2. **Spearman's Rank Correlation Coefficient**: This is a non-parametric measure of rank correlation. It assesses how well the relationship between two variables can be described using a monotonic function. Like the Pearson correlation coefficient, its values also range from -1 to 1.
    3. **Cosine Similarity**: This measures the cosine of the angle between two non-zero vectors. Its values range from -1 (completely dissimilar) to 1 (completely similar). This is a common measure for high-dimensional vectors, such as in word embeddings or other language model applications.
    4. **Euclidean Distance**: This is the "ordinary" straight-line distance between two points in Euclidean space. The smaller the Euclidean distance, the more similar the vectors.
    5. **Kendall Tau Distance**: Similar to Spearman's rank correlation, Kendall tau distance is a metric to measure the ordinal association between two measured quantities.
    
    The choice of method depends on what you believe is the best way to define similarity in the context of your task. Each of the above methods has different properties and can capture different types of relationships between the vectors.
    
    Please note, it is necessary to ensure that the neurons in the lists are in the same order when comparing them, and that you are taking into consideration the possibility that not all neurons may be equally influential in the model's output. For a more meaningful comparison, you might want to focus on neurons that have been identified as more significant in some way, for instance, through analysis of the model's attention patterns or the impact of individual neurons on the model's output.
    

We can also take the dot product of the two tensors themselves

[https://colab.research.google.com/drive/1rch6VaG9O1YFJT1wPjjbXyDgXizGT7WV#scrollTo=Wdpe4KeO_iwY&line=5&uniqifier=1](https://colab.research.google.com/drive/1rch6VaG9O1YFJT1wPjjbXyDgXizGT7WV#scrollTo=Wdpe4KeO_iwY&line=5&uniqifier=1)

If we isolate the neurons with the biggest impact, and only take the dot prod of tokens with those neurons, this similarity is prob even bigger.

- Why do we need distance metrics for vectors if we can just use the dot product for their similarity?
    
    The dot product and distance metrics like Euclidean distance or cosine similarity all provide ways of quantifying the similarity or difference between two vectors, but they emphasize different aspects of the vectors' relationship and are used in different contexts.
    
    1. Dot Product: The dot product of two vectors is a measure of the extent to which the vectors point in the same direction. If both vectors are normalized (i.e., they have a length of 1), then the dot product is equivalent to the cosine of the angle between them, ranging from -1 (vectors pointing in exactly opposite directions) to 1 (vectors pointing in exactly the same direction). This can be useful when the magnitude of the vectors is not important, only the direction they point.
    2. Euclidean Distance: The Euclidean distance (also known as L2 distance) between two vectors is a measure of the geometric distance between them in the vector space. This metric takes both direction and magnitude into account, and it's often used when the absolute difference between the vectors is important.
    3. Cosine Similarity: This is a measure of the cosine of the angle between two vectors. This metric gives a value between -1 and 1 which signifies the angle, and hence the similarity between two vectors. If the vectors are orthogonal, the cosine similarity is 0, if they are in the same direction, it's 1, and if they are diametrically opposed, it's -1. This is useful when the magnitude of the vectors does not matter, and we are only interested in the direction (as is often the case in text analysis tasks, for example).
    
    So, while the dot product can provide a measure of similarity, there are many cases where other distance or similarity metrics are more appropriate depending on what you want to emphasize or the specific requirements of your task.
    

[https://datascience.stackexchange.com/questions/744/cosine-similarity-versus-dot-product-as-distance-metrics](https://datascience.stackexchange.com/questions/744/cosine-similarity-versus-dot-product-as-distance-metrics)

[https://stats.stackexchange.com/questions/544951/when-to-use-dot-product-as-a-similarity-metric](https://stats.stackexchange.com/questions/544951/when-to-use-dot-product-as-a-similarity-metric)

- Dot prod of Chihuahua with dog+small, like king queen

---

- If I have a list, and take a dot product of every pair of that list, and plot the histogram of unique pairs, is this a valid distribution to perform hypothesis testing on?
    
    The answer to this question depends on what hypothesis you want to test.
    
    The dot product of every pair of vectors in a list generates a set of scalar values. When you create a histogram from these values, you're effectively creating a distribution of these scalar outputs. This distribution can be used for statistical analysis under certain circumstances.
    
    However, you should be aware of a few important considerations:
    
    1. **Normality Assumption**: Many hypothesis tests (like the t-test) assume that the data follows a normal distribution. If the distribution of dot product values isn't approximately normal, then the test results may be unreliable. Non-parametric tests may be more appropriate in such cases.
    2. **Independence Assumption**: Hypothesis testing also assumes that the observations are independent. If your vectors are not independent, the dot products will not be independent either, which can violate this assumption.
    3. **Unique Pairs**: When you say "unique pairs", it's important to be aware that "unique" can refer to the vectors themselves (i.e., no pair of vectors is repeated), the dot products (i.e., no two pairs have the same dot product), or both. It's also worth noting that the number of unique pairs can be quite large if the list is long, which may impact the feasibility of your approach.
    4. **Hypothesis**: The hypothesis you're trying to test should have a logical basis in the context of the data and the operation you're performing. For example, you might hypothesize that the dot product values follow a certain distribution, or that the mean dot product is greater than zero. The appropriateness of a hypothesis test depends largely on the specific hypothesis and the context.
    
    In conclusion, while it's possible to perform hypothesis testing on a distribution of dot products from a list of vectors, it's important to understand the assumptions behind the tests you're using, and to have a specific, well-grounded hypothesis in mind. In general, when working with dot products or other similar operations, it may be more appropriate to use methods from multivariate analysis or machine learning that are designed to handle complex, high-dimensional data.
    
- If I plot dot(A,B) and dot (A,C), are those two dot products considered independent?
    
    Independence of dot products depends on the relationship between the vectors involved. Two dot products, dot(A,B) and dot(A,C), aren't automatically independent just because B and C are different vectors. They both involve vector A, which introduces a potential dependency between them.
    
    For instance, if vectors A, B, and C all live in a high-dimensional space, and if A is very much aligned with B but not with C, then the value of dot(A,B) would tend to be high, and the value of dot(A,C) would tend to be low. Therefore, knowing the value of dot(A,B) gives you some information about the likely value of dot(A,C), which means the two dot products aren't completely independent.
    
    In the simplest terms, two variables are independent if the outcome of one does not affect the outcome of the other. So, if the vectors A, B, and C are chosen independently from each other, the dot products dot(A,B) and dot(A,C) would be independent. But if there's any sort of relationship between A, B, and C, then the dot products could be dependent.
    
- If I plot dot products with the pattern of dot(A,B) and dot(A,C), would that be a valid distribution?
    
    Yes, you can certainly plot a distribution of dot products following the pattern of dot(A,B) and dot(A,C), assuming that A, B, and C are vectors. This would result in a distribution of scalar values, each representing the dot product of a pair of vectors.
    
    Remember, a distribution is simply a function that describes the probability of a random variable. In this case, your random variable is the dot product of a pair of vectors. As long as you have enough data points to make a meaningful distribution (typically at least 30 for most statistical analyses), and the vectors A, B, and C are chosen in a way that meets the assumptions of your intended statistical tests (e.g., random sampling, independence, normality, etc.), then this would indeed be a valid distribution.
    
    However, it's important to note that the meaningfulness and interpretability of this distribution will largely depend on the specific nature and context of your vectors. For example, in the field of machine learning, such a distribution might be useful for understanding the relationships between different features or dimensions in your data.
    
    Keep in mind that you would need to carefully consider your hypothesis and the assumptions of the statistical test(s) you plan to use. You should also carefully consider whether a simpler or more standard statistical analysis might be more appropriate for your data.
    
- Why does hypothesis testing require independent observations?
    
    Hypothesis testing requires independent observations for a number of reasons:
    
    1. **Test Statistic Distribution**: Hypothesis tests work by comparing the test statistic (e.g., the sample mean) to its theoretical distribution under the null hypothesis. These theoretical distributions are typically derived assuming independent observations. If observations are not independent, the distribution of the test statistic can be different, leading to incorrect p-values and false conclusions.
    2. **Avoiding Biased Results**: Dependent observations can lead to biased results. For example, if an observation is more likely to be selected because it is similar to a previous observation, this can bias the results in favor of the null hypothesis (Type II error) or against it (Type I error).
    3. **Validity of Confidence Intervals**: Confidence intervals for parameters like the population mean or proportion are also calculated assuming independent observations. If this assumption is violated, the confidence intervals may no longer accurately capture the parameter of interest with the specified probability.
    
    It's worth noting that there are statistical methods designed to handle dependent observations, such as time series analysis, mixed-effects models, or generalized estimating equations, among others. These methods account for the dependence in their modelling assumptions and can provide valid hypothesis tests even when the independence assumption is violated. But standard hypothesis tests, like t-tests or chi-squared tests, do require independent observations.
    
- In detail, why were they derived from assuming independent observations?
    
    The assumption of independent observations is fundamental to many statistical methods due to the mathematics involved in deriving these methods and the goal of achieving robust, generalizable results.
    
    The core concept behind most statistical tests is the Central Limit Theorem (CLT), which states that, given a sufficiently large sample size, the sampling distribution of the mean of any independent, identically distributed (iid) random variable will be approximately normally distributed, regardless of the shape of the variable's original distribution.
    
    Why is this important? Many statistical methods, including the common t-test and chi-squared test, rely on the normality assumption. This means the variable of interest should be normally distributed, or in practice, the sample size should be large enough for the CLT to take effect.
    
    Let's look at the reasoning more closely:
    
    1. **Simplification of Probability Calculations**: The properties of independent random variables greatly simplify the calculation of probabilities. For instance, the probability of joint events (the intersection of two or more events happening at the same time) is the product of their individual probabilities when the events are independent. This isn't the case for dependent events.
    2. **Distribution of Sum (or Average) of Variables**: When variables are independent, the variance of the sum (or average) of these variables is simply the sum of their variances. If variables are not independent, then the covariance between variables also needs to be taken into account, complicating the calculations.
    3. **Central Limit Theorem**: As noted, the CLT applies to independent and identically distributed random variables. This theorem is critical to many statistical tests as it guarantees the distribution of the sum (or average) tends towards a normal distribution as the sample size grows, regardless of the shape of the original distribution. This is what allows us to make probabilistic statements about the sample mean or sum.
    4. **Avoiding Overfitting and Bias**: If observations are not independent, there may be overfitting or bias in the results. Overfitting occurs when a statistical model is too closely tied to the quirks of the specific sample data, and thus performs poorly on new data. Bias, on the other hand, refers to consistent errors that skew the results in a particular direction.
    
    It's worth noting that when data is not independent, there are methods like time-series analysis, clustering, mixed-effects models, or repeated measures ANOVA that take into account the dependence of data. These are, however, more complex and require additional assumptions.
    
- Give an example of dependent observations
    
    Sure, here are some examples of situations where observations might be dependent:
    
    1. **Time Series Data**: Observations collected over time often exhibit dependence. For example, stock prices from day to day are not independent because today's price is influenced by yesterday's price. Similarly, weather conditions from one day to the next are not independent.
    2. **Spatial Data**: Observations collected over space can also be dependent. For example, the temperature in neighboring locations is likely to be similar, so temperature readings at different points in space are not independent.
    3. **Repeated Measures**: In medical or psychological studies, measurements taken from the same individual at different times are usually not independent. For example, if a person's heart rate is measured at several points during a stress test, the heart rate at one point in time is likely to be close to the heart rate at the next point in time.
    4. **Cluster Sampling**: When data is collected in clusters or groups (such as students within classrooms, or households within neighborhoods), observations within the same group are often more similar to each other than they are to observations from different groups. For example, students in the same class might have similar test scores because they have the same teacher.
    5. **Genetic Data**: If you are studying siblings, their genetic information is not independent, because they share some proportion of their genes from their parents.
    
    In these cases, the standard statistical techniques that assume independence of observations are not applicable, and specialized techniques need to be used that can account for the dependency among observations.
    
- Give one mathematically proven example of a simple case where two observations are not independent
    
    Sure, let's consider a simple example with a deck of cards. Suppose we draw two cards from the deck without replacement (meaning we do not put the first card back into the deck before drawing the second card).
    
    Let's define the following two events:
    
    1. Event A: The first card drawn is an ace.
    2. Event B: The second card drawn is an ace.
    
    If we were to replace the first card before drawing the second, these two events would be independent, because the outcome of the first draw would not affect the probability of the second draw. In the language of probability, we would have P(A and B) = P(A) * P(B), which is the definition of independent events.
    
    However, in our case, the two draws are not independent. Once we draw an ace as the first card, there are now only 3 aces left in the deck, and the total number of cards is 51 instead of 52. Therefore, the probability that the second card is an ace, given that the first card was an ace (which is written as P(B|A)), is 3/51 = 1/17.
    
    But if the two events were independent, P(B|A) would just be P(B), which is 4/52 = 1/13. Because P(B|A) does not equal P(B), we can see that the two events are not independent.
    
    So, this is a simple example where two observations (the outcomes of the two card draws) are not independent, and it can be mathematically proven by using the definition of independent events in probability.
    
- Is the independence assumption for hypothesis testing just about how variable A affects the probability of variable B? If variable A affects another property of B, is it still considered dependent?
    
    The independence assumption in hypothesis testing is not only about how one variable (A) affects the probability of another variable (B). It also concerns how the variables are related and might influence each other in general.
    
    When we say that two variables are independent, we mean that knowing the value of one variable provides no information about the value of the other variable. If variable A affects any property of B, it implies that knowing something about A gives us information about B. In this case, A and B are not independent.
    
    For instance, if knowing the value of A doesn't change the probability of B but does affect the variance or standard deviation of B, A and B are not independent. This is because information about A can tell us something about the variability of B, which is a fundamental characteristic of B. So, if A affects any property of B (mean, variance, distribution, etc.), A and B are considered dependent.
    
- I have a function f(x,y). I measure f(A,B) and f(A,C). Are these two observations considered independent?
    
    Whether or not the two observations f(A,B) and f(A,C) are independent depends on the relationship between the variables and the specific form of the function f. Here are some things to consider:
    
    1. **Dependence on A**: Both f(A,B) and f(A,C) depend on A. If the value of A influences the output of the function f significantly, then the two observations could be considered dependent, as they both stem from the same value of A.
    2. **Nature of Function f**: If the function f(x, y) has a special form that makes f(A, B) and f(A, C) independent despite the shared A (for example, if f(x, y) = x * y and B and C are independent), then the two observations could be independent. But without more information about the nature of f, it is hard to make a general statement.
    3. **Relationship between B and C**: If B and C are not independent, then f(A,B) and f(A,C) could also be dependent, even if f(x, y) doesn't explicitly show this dependence.
    
    So, in general, without additional information about the nature of the function f and the relationships between A, B, and C, it's not possible to definitively say whether f(A,B) and f(A,C) are independent. It would require a more detailed analysis based on the specific context and mathematical form of the function.
    
- In the case where I want to find the distribution of observations with repeated variables, such as A being in both f(A,B) and f(A,C), how would I conduct hypothesis testing to check if a value f(P,Q) is at the tail end of a distribution of f(x,y)?
    
    If you want to perform hypothesis testing to check whether a specific observation f(P,Q) is at the tail end of the distribution of f(x,y), it might be best to use a permutation test or a bootstrap test, as these methods can accommodate complex dependencies among variables and do not require the assumptions of parametric methods, such as t-tests.
    
    Here's a basic way to conduct a permutation test:
    
    1. **Generate a Null Distribution**: First, you need to generate a null distribution that represents what the distribution of your test statistic would look like if the null hypothesis were true. Since your null hypothesis in this case seems to be that f(P,Q) comes from the same distribution as the rest of the f(x,y) values, you could do this by repeatedly and randomly assigning the labels of your two sets of observations (those involving A and those not involving A) to different data points. For each of these permutations, you would calculate the test statistic (which could be, for example, the difference in means between the two sets) and record the result. The collection of these test statistics forms your null distribution.
    2. **Calculate the Actual Test Statistic**: Next, calculate the actual test statistic for your data. In this case, it seems you're interested in the value f(P,Q), so your test statistic could be the difference between f(P,Q) and the mean of all the other f(x,y) values.
    3. **Compare to Null Distribution**: Finally, compare your actual test statistic to the null distribution. The p-value of your test is the proportion of test statistics in the null distribution that are as extreme or more extreme than your actual test statistic. If this p-value is less than your chosen significance level (often 0.05), then you reject the null hypothesis and conclude that f(P,Q) is at the tail end of the distribution of f(x,y).
    
    Please note that it's important to have a good understanding of your data and the exact hypothesis you're testing before you conduct a test. The method above is a general approach and might need to be adjusted depending on the specific details of your situation. Always ensure that the test you're using is appropriate for your data and your hypothesis.
    
- I've been taking the dot product of tokens (say after the first embedding layer) and plotting the dot product histogram of unique pairs, which forms a normal distribution. Then I check the dot product of "tokens semantically similar in some measurement" (say red and blue) and compare its value to the distribution of dot products. How do I turn this into hypothesis testing?
    
    The scenario you are describing involves measuring the semantic similarity between words in a text corpus using the dot product of their associated word embeddings. You then compare the dot product of a specific pair of words (say "red" and "blue") to a distribution of dot products. You want to use hypothesis testing to determine whether the dot product of the specific pair is significantly different from what would be expected under the null hypothesis.
    
    Here's how you could conduct this hypothesis test:
    
    1. **Null Hypothesis (H0)**: The dot product of the embeddings for "red" and "blue" comes from the same distribution as the dot products of all other unique word pairs.
    2. **Alternative Hypothesis (H1)**: The dot product of the embeddings for "red" and "blue" is significantly different than what would be expected from the distribution of dot products of all other unique word pairs.
    3. **Test Statistic**: The test statistic in this case would be the dot product of the embeddings for "red" and "blue". You calculate this value from your data.
    4. **Significance Level**: Choose a significance level for your test. This is typically 0.05, but could be different depending on your specific circumstances.
    5. **Calculate P-value**: The p-value is the probability of obtaining a dot product as extreme as, or more extreme than, the actual observed dot product, given that the null hypothesis is true. You can calculate this by determining the proportion of dot products in your null distribution that are as extreme or more extreme than the observed dot product.
    6. **Decision**: If the p-value is less than your chosen significance level, you reject the null hypothesis in favor of the alternative hypothesis. If the p-value is not less than your chosen significance level, you do not reject the null hypothesis.
    
    It's important to note a few caveats:
    
    - This method assumes that the distribution of dot products for all unique word pairs is representative of the null hypothesis. If there are specific pairs that you believe should be excluded (e.g., other color pairs, or any pairs you believe have a similar level of semantic similarity to "red" and "blue"), you should exclude these from the null distribution.
    - You're comparing the observed dot product to a distribution of dot products. Depending on the form of this distribution, different types of hypothesis tests may be more or less appropriate. If the distribution is normal, a z-test or t-test might be appropriate. If the distribution is not normal, a non-parametric test like the Mann-Whitney U test might be better.
    - Always ensure that the test you're using is appropriate for your data and your hypothesis. Hypothesis testing is a powerful tool, but using it correctly requires a solid understanding of both your data and the underlying statistical principles.
- I've been taking the dot product of tokens (say after the first embedding layer) and plotting the dot product histogram of unique pairs, which forms a normal distribution. Then I check the dot product of "tokens semantically similar in some measurement" (say red and blue) and compare its value to the distribution of dot products. If I find dot(red, blue) has a much higher value than average, is that considered evidence that semantically similar tokens are closer in space than other tokens?
    
    In general, yes, a higher dot product between the embeddings of two semantically similar words (e.g., "red" and "blue") as compared to the average dot product of embeddings of all unique pairs of words could be interpreted as evidence that semantically similar words are closer in the embedding space. This is based on the assumption that higher dot products correspond to vectors that are closer together in the embedding space.
    
    The dot product of two vectors captures both the length of the vectors and the cosine of the angle between them. If the embeddings are normalized (i.e., all embeddings have a length of 1), then the dot product is simply the cosine of the angle between the two vectors. In this case, a higher dot product corresponds to a smaller angle, which in turn corresponds to the vectors being closer together in the embedding space.
    
    However, keep in mind that this is a somewhat simplified interpretation. The relationship between semantic similarity and distance in the embedding space may not be perfectly linear or consistent across different pairs of words. Furthermore, word embeddings typically capture many different aspects of a word's meaning, and not all of these aspects will necessarily align with a specific measure of semantic similarity.
    
    Therefore, while a higher than average dot product could be taken as evidence of semantically similar words being closer in the embedding space, it would be advisable to also perform additional analyses to confirm this interpretation. This might involve, for example, looking at the dot products of other pairs of semantically similar words, or comparing the dot products of semantically similar words to those of semantically dissimilar words.
    
- Is it enough to compare the dot product of many pairs of semantically similar tokens against the distribution of all dot products of all token pairs, or would I require hypothesis testing? What value does hypothesis testing add to this analysis?
    
    The method you described -- comparing the dot product of many pairs of semantically similar tokens against the distribution of all dot products of all token pairs -- provides an exploratory way to assess whether semantically similar tokens are closer in the embedding space. If you consistently observe that semantically similar tokens have higher dot products compared to the distribution of all dot products, that could suggest a relationship.
    
    However, hypothesis testing would provide a more formal and rigorous way to evaluate this relationship. Hypothesis testing would allow you to assess the statistical significance of the observed differences, control for Type I errors (i.e., incorrectly rejecting the null hypothesis), and quantify the uncertainty associated with your results (e.g., through p-values or confidence intervals).
    
    Here's what hypothesis testing could add to your analysis:
    
    1. **Quantification of Uncertainty**: By providing a p-value, hypothesis testing quantifies the probability that the observed difference could have occurred by random chance under the null hypothesis. This allows you to assess the uncertainty associated with your results.
    2. **Control for Type I Errors**: Hypothesis testing allows you to control the Type I error rate (i.e., the probability of incorrectly rejecting the null hypothesis) at a desired level (e.g., 0.05).
    3. **Effect Size Estimation**: Hypothesis testing often involves the calculation of an effect size, which quantifies the magnitude of the observed difference. This can provide valuable context, as a statistically significant difference is not always practically or substantively significant.
    4. **Generalization to Population**: If your tokens are a sample from a larger population of tokens, hypothesis testing can help you make inferences about that population. In contrast, simply comparing averages or other summary statistics might not fully account for sampling variability.
    5. **Formal Test of Hypothesis**: Hypothesis testing provides a formal framework for testing a specific hypothesis (e.g., "semantically similar tokens are closer in the embedding space"). This can lend more credibility to your results and may be required in certain academic or professional contexts.
    
    So, while your initial exploratory analysis could provide valuable insights and guide your research, hypothesis testing could provide a more robust and rigorous assessment of your findings.
    
- What does it mean for "semantically similar tokens" to come from a different distribution? Don't we plot all dot products of token pairs in the same histogram?
    
    The phrase "semantically similar tokens coming from a different distribution" refers to the idea that the distribution of dot products for semantically similar tokens might be different from the distribution of dot products for random or semantically dissimilar tokens.
    
    To understand this, let's consider the dot product distributions. When we talk about "all dot products of token pairs," we mean taking every possible unique pair of tokens, calculating the dot product of their embeddings, and looking at the distribution of these values. This distribution reflects the typical relationship between any pair of tokens in the embedding space.
    
    Now, if we consider only semantically similar tokens and calculate the dot product of their embeddings, we might expect these values to be different from those of random token pairs, because semantically similar tokens are likely closer together in the embedding space (which, with normalized vectors, would lead to larger dot products). If this is true, the distribution of these dot products for semantically similar tokens would be different from the overall distribution. This "different distribution" would likely be shifted toward higher dot product values.
    
    So when we say "semantically similar tokens come from a different distribution," it's not about physically plotting them on a different histogram. It's about the idea that if we were to separate out these values and plot their own histogram, the shape, center, and spread of this distribution might be different from the overall distribution of all token pairs.
    
    In the context of hypothesis testing, the null hypothesis might be that the semantically similar tokens come from the same distribution as all token pairs (i.e., semantic similarity has no effect on dot product), and the alternative hypothesis might be that they come from a different distribution (i.e., semantic similarity does affect dot product). You would then use a statistical test to decide whether the observed data provides enough evidence to reject the null hypothesis in favor of the alternative.
    
- When I perform hypothesis testing, can the null distribution contain semantically similar tokens (as they are a subset of random tokens), or can it only contain dissimilar tokens?
    
    The choice of what to include in your null distribution depends on the exact hypothesis you're testing.
    
    If you're testing the hypothesis that the dot products of semantically similar tokens come from a different distribution than random token pairs, then your null distribution should represent the distribution under the null hypothesis -- that is, the distribution of dot products of random token pairs.
    
    In this case, you might want to exclude semantically similar pairs from your null distribution, because including them could potentially shift the distribution and make it more similar to the distribution of semantically similar pairs. This could make it harder to detect a difference between the two distributions, thereby reducing the power of your test.
    
    On the other hand, if you're testing the hypothesis that the dot products of semantically similar tokens are different from all token pairs (including other semantically similar ones), then you would want to include all pairs in your null distribution.
    
    So the choice of what to include in your null distribution depends on your specific research question and hypothesis. It's always important to clearly define your null and alternative hypotheses before conducting a statistical test, as this will guide the choice of test and the creation of the null distribution.
    
    Also, it's worth noting that semantically similar tokens are a somewhat subjective category, and their definition might vary depending on the context and the specific measure of semantic similarity being used. This subjectivity could also impact your choice of what to include in the null distribution.
    
- Formalize: testing the hypothesis that the dot products of semantically similar tokens are different from all token pairs (including other semantically similar ones), then you would want to include all pairs in your null distribution.
    
    The formalization of this hypothesis testing scenario could look as follows:
    
    **Null Hypothesis (H0)**: The dot products of semantically similar tokens come from the same distribution as the dot products of all token pairs (including other semantically similar ones).
    
    **Alternative Hypothesis (H1)**: The dot products of semantically similar tokens come from a different distribution than the dot products of all token pairs (including other semantically similar ones).
    
    **Test Statistic**: You could use a variety of test statistics for this hypothesis test. One common choice might be the difference between the mean dot product of the semantically similar tokens and the mean dot product of all token pairs.
    
    **Significance Level (α)**: This is the threshold below which you will reject the null hypothesis. Common choices are 0.05 or 0.01.
    
    **P-value**: This is the probability, under the null hypothesis, of observing a test statistic as extreme or more extreme than the one calculated from your data. If the p-value is less than α, you reject the null hypothesis.
    
    **Null Distribution**: This is the distribution of dot products of all token pairs (including semantically similar and dissimilar ones). It represents the distribution of dot products that you would expect to see if the null hypothesis were true.
    
    **Test Procedure**: You would perform a suitable statistical test (like a two-sample t-test or Mann-Whitney U test, depending on the characteristics of your data) to compare the dot products of semantically similar tokens to the null distribution. If the p-value resulting from this test is less than your chosen α, you would reject the null hypothesis and conclude that the dot products of semantically similar tokens come from a different distribution.
    
    Remember to check the assumptions of the statistical test you choose (e.g., normality for a t-test), and ensure that your sample size is large enough to give you adequate power to detect a difference, should one exist.
    

<<<

One thing you can do is to ONLY USE A TOKEN ONCE. Don’t take dot(A,B) and dot(A,C); only use A once. There is no reason to.

However, what about dot(A, large)? In fact, a better test is to check dot(A, large) vs dot(B,large), where A are ‘dissimilar’ tokens and B are ‘similar’ tokens.

We can do this with sequences too: dot(A, one), where A=table, chair, etc.

vs dot(B, one), where B is in [1, January, Sunday, first, etc]

<<<

One thing I've been looking at that I want to get more people to double check is that 

I've been taking the dot product of tokens (say after the first embedding layer) and plotting the dot product histogram of unique pairs, which forms a normal distribution. Then I check the dot product of "tokens semantically similar in some measurement" (say red and blue) and compare its value to the distribution of dot products.

I was thinking this could be used for hypothesis testing, but wanted to double check this validity. For instance, "If I plot dot(A,B) and dot (A,C), are those two dot products considered independent?"

[https://en.wikipedia.org/wiki/Permutation_test](https://en.wikipedia.org/wiki/Permutation_test)

[https://en.wikipedia.org/wiki/Paired_data](https://en.wikipedia.org/wiki/Paired_data)

[https://www.researchgate.net/figure/A-histogram-of-the-dot-product-similarities-generated-using-the-word-list-in-Table-1_fig1_2554283](https://www.researchgate.net/figure/A-histogram-of-the-dot-product-similarities-generated-using-the-word-list-in-Table-1_fig1_2554283)