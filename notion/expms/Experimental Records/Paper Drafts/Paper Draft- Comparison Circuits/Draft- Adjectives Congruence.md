# Draft- Adjectives Congruence

[Size Comparison Congruence](../../Interpret%20Attention%20Head%20Circuits%20of%20Comparison%20In%20c1d0ec7e43214760b4062ae4cdc0cd6b/PLAN-%20Size%20Comparison%20Circuits%20and%20Neurons%201111d95ef57b4131b259ef88363f3010/Size%20Comparison%20Congruence%20e94368b6a22a4e9e9d0d444b3c5972e5.md) —- SUMMARIZE:

- [Dot products of tokens after embedding layer](https://colab.research.google.com/drive/1rch6VaG9O1YFJT1wPjjbXyDgXizGT7WV#scrollTo=Dot_products_of_tokens_after_embedding_layer)
    - [large](https://colab.research.google.com/drive/1rch6VaG9O1YFJT1wPjjbXyDgXizGT7WV#scrollTo=large)
    - [tokens in general](https://colab.research.google.com/drive/1rch6VaG9O1YFJT1wPjjbXyDgXizGT7WV#scrollTo=tokens_in_general)
    - [average over dataset of single tokens](https://colab.research.google.com/drive/1rch6VaG9O1YFJT1wPjjbXyDgXizGT7WV#scrollTo=average_over_dataset_of_single_tokens)
    - [~~For multiple tokens for a word, get the average of each token's embeddings~~](https://colab.research.google.com/drive/1rch6VaG9O1YFJT1wPjjbXyDgXizGT7WV#scrollTo=For_multiple_tokens_for_a_word_get_the_average_of_each_token_s_embeddings)
    - [Dot Product of large synonyms](https://colab.research.google.com/drive/1rch6VaG9O1YFJT1wPjjbXyDgXizGT7WV#scrollTo=Dot_Product_of_large_synonyms)
- [Dot products of token and all neurons (congruence)](https://colab.research.google.com/drive/1rch6VaG9O1YFJT1wPjjbXyDgXizGT7WV#scrollTo=Dot_products_of_token_and_all_neurons_congruence_)
    - [Compute dot products for "tall" and "large", and compare the similarities (eg. which are in the top) AND identify their common top neurons](https://colab.research.google.com/drive/1rch6VaG9O1YFJT1wPjjbXyDgXizGT7WV#scrollTo=Compute_dot_products_for_tall_and_large_and_compare_the_similarities_eg_which_are_in_the_top_AND_identify_their_common_top_neurons)
- [Dot products of input after first MLP layer](https://colab.research.google.com/drive/1rch6VaG9O1YFJT1wPjjbXyDgXizGT7WV#scrollTo=Dot_products_of_input_after_first_MLP_layer)

---

- GPT-2-Large
    
    [https://colab.research.google.com/drive/1rch6VaG9O1YFJT1wPjjbXyDgXizGT7WV#scrollTo=llNA4q8MzG7u](https://colab.research.google.com/drive/1rch6VaG9O1YFJT1wPjjbXyDgXizGT7WV#scrollTo=llNA4q8MzG7u)
    
    **Dot products of tokens after embedding layer**
    
    - In “large”, we run a few tests to find that adjectives with semantic similarity to “large” in terms of size, such as “huge”, have a high dot product. We take the dot product right after the first embedding layer.
    - In “**average over dataset of single tokens”,** we generate 100 random tokens put through the first embedding layer and plot the histogram of their dot products.
        
        ![Untitled](Draft-%20Adjectives%20Congruence%20f95dc5b0f41c4b10ac6e5a96bde7e8c6/Untitled.png)
        
    - In [Dot Product of large synonyms](https://colab.research.google.com/drive/1rch6VaG9O1YFJT1wPjjbXyDgXizGT7WV#scrollTo=Dot_Product_of_large_synonyms), we obtain this dot product histogram only for single tokens that are synonyms of “large”
    
    ![Untitled](Draft-%20Adjectives%20Congruence%20f95dc5b0f41c4b10ac6e5a96bde7e8c6/Untitled%201.png)
    
    [(0.801905632019043, 'large', 'big'),
    (0.8649396300315857, 'large', 'huge'),
    (0.6885147094726562, 'large', 'grand'),
    (0.7752034664154053, 'large', 'tall'),
    
    There’s something wrong here because on (large, small), this is 2.1379
    
    There’s a bug [TBC]
    

GPT-2-Small

[https://colab.research.google.com/drive/18JcQcn7TKhN-1ULNjqQqvst9yJ6ZDhAA](https://colab.research.google.com/drive/18JcQcn7TKhN-1ULNjqQqvst9yJ6ZDhAA)

**Dot products of tokens after embedding layer**

- In “large”, we run a few tests to find that adjectives with semantic similarity to “large” in terms of size, such as “huge”, have a high dot product. We take the dot product right after the first embedding layer.
- In “**average over dataset of single tokens”,** we generate 100 random tokens put through the first embedding layer and plot the histogram of their dot products.
- In [Dot Product of large synonyms](https://colab.research.google.com/drive/1rch6VaG9O1YFJT1wPjjbXyDgXizGT7WV#scrollTo=Dot_Product_of_large_synonyms), we obtain this dot product histogram only for single tokens that are synonyms of “large”

Histogram of dot product of 100 random tokens

![Untitled](Draft-%20Adjectives%20Congruence%20f95dc5b0f41c4b10ac6e5a96bde7e8c6/Untitled%202.png)

AVG: 4.9035

dot product histogram only for single tokens that are synonyms of “large”

![Untitled](Draft-%20Adjectives%20Congruence%20f95dc5b0f41c4b10ac6e5a96bde7e8c6/Untitled%203.png)

AVG: >6

We observe that the “large synonyms” have dot product that’s higher than average

TO DO: Perform actual hypothesis testing to get p-value

ISSUE: This takes pairs as observations, meaning many observations are repeated in pairs. What problems arise from this? [try to identify as many issues as poss]

- To **ChatGPT**: I am taking the dot product of 100 items, and making a histogram of the dot products. This takes pairs as observations, meaning many observations are repeated in pairs. Can I do hypothesis testing on this to see how many deviations away a subset is from the average value? What problems arise from this?
    
    Yes, you can perform hypothesis testing on the dot products to see how many deviations a subset is away from the average value. However, there are a few problems that can arise from this approach:
    
    1. ~~Multiple testing: If you perform multiple hypothesis tests using the same data, the likelihood of obtaining a false positive result increases. This is known as the multiple testing problem. It's important to adjust for multiple comparisons to control the overall false positive rate, such as by using Bonferroni correction or other appropriate methods.~~
        
        [ we are just performing one test ]
        
    2. Dependent observations: Since your observations are pairs, it's likely that they are not independent. This violates one of the assumptions of many statistical tests. Dependencies can arise due to repeated observations, which can lead to **inflated type I error rates** and invalid hypothesis tests. It's important to consider the dependency structure in your data when performing hypothesis tests.
    3. ~~Distribution assumptions: The validity of many hypothesis tests relies on certain distributional assumptions. The dot product values need to follow a specific distribution for the tests to be accurate. If your data does not meet those assumptions, the results of your hypothesis tests may be unreliable. It's important to assess the distributional assumptions of your data before conducting hypothesis tests.~~
        
        [we will check if it follows the correct distribution conds; eg. normal ]
        
    4. ~~Sample size and power: The reliability and power of your hypothesis test depend on the sample size. With a small sample size, it may be challenging to detect meaningful deviations from the average value. Consider the effect size and the desired level of statistical power when designing your study or interpreting the results.~~
        
        [we can generate as much data as we want with many tokens]
        
    
    ~~To address these issues, you could consider alternative approaches such as nonparametric tests or resampling methods like bootstrapping, which do not rely heavily on distributional assumptions and are more flexible in handling dependencies.~~
    
    [ this is for if distribution is off ]
    
    - How can we address Dependent observations?
        
        To address dependent observations in your data, you can employ techniques that are specifically designed for analyzing dependent or correlated data. Here are a few approaches you can consider:
        
        1. Pairwise analysis: Instead of treating each pair of observations as independent, you can analyze the data within each pair. This approach accounts for the dependency between observations within a pair. For example, you can calculate the difference between the two values in each pair and perform hypothesis testing on these differences.
        2. Clustered analysis: If your data exhibits clustering or grouping structure, where observations within each cluster are more correlated than observations between clusters, you can use clustered analysis methods. These methods take into account the within-cluster correlation when estimating test statistics and p-values. Examples include generalized estimating equations (GEE) and mixed-effects models.
        3. ~~Time series analysis: If your data is collected over time and exhibits temporal dependencies, you can use time series analysis techniques. These methods model the autocorrelation structure in the data and allow you to make inferences while accounting for the temporal dependencies. Autoregressive integrated moving average (ARIMA) models and state space models are commonly used for time series analysis.~~
        4. Resampling methods: Resampling methods like bootstrapping can be used to generate pseudo-samples by resampling from the observed pairs. This can help you estimate the sampling distribution of your statistic of interest while preserving the dependency structure in the data. You can then perform hypothesis testing based on the resampled data.
        5. Permutation tests: Permutation tests, also known as randomization tests, can be useful when dealing with dependent observations. These tests rely on randomizing the assignment of pairs or shuffling the order of the observations to create a null distribution. By comparing the observed test statistic to the null distribution, you can obtain a p-value. Permutation tests do not assume any specific distributional form and can handle dependencies effectively.
        
        The choice of method depends on the nature of the dependency in your data and the specific research question you are investigating. It is often helpful to consult with a statistician or data scientist who can guide you in selecting the most appropriate method for your analysis.
        
    - Give an example of using one of these ways to address the issue of treating pairs of observations as a single data point
        
        We will calculate the differences between the dot product values within each pair and perform hypothesis testing on these differences.
        
        Let's assume we have a dataset consisting of 100 pairs of observations and their corresponding dot product values. To address the dependency between the observations within each pair, we can follow these steps:
        
        1. Calculate the differences: For each pair of observations, subtract the dot product value of the second observation from the dot product value of the first observation. This will give us a set of difference values.
        2. Perform hypothesis testing: Once we have the differences, we can perform hypothesis testing on these values using appropriate statistical tests. The choice of test depends on the specific research question and the distributional assumptions of the differences. For example, if the differences are normally distributed, you could use a paired t-test to assess whether the mean difference significantly deviates from zero. If the distributional assumptions are not met, nonparametric tests like the Wilcoxon signed-rank test can be used.
        3. Interpret the results: Based on the hypothesis test results, you can determine whether there are statistically significant deviations in the dot product differences from zero. The magnitude and direction of the differences can provide insights into the subset of observations that deviate the most from the average value.
        
        By analyzing the differences within each pair, you take into account the dependency between the observations, allowing for a more accurate assessment of deviations from the average value. This approach is particularly useful when the dependency between pairs is expected to be strong.
        
        Remember to adjust for multiple testing if you are performing hypothesis tests on multiple subsets or comparing multiple pairs. This will help control the overall false positive rate.
        

<<<

**Dot products of token and all neurons (congruence)**

Congruence of 100 random tokens and all MLP neurons in model

![Untitled](Draft-%20Adjectives%20Congruence%20f95dc5b0f41c4b10ac6e5a96bde7e8c6/Untitled%204.png)

Congruence of “large” synonyms

| large | tall | 9334.0410 |
| --- | --- | --- |
| large | big | 7067.6182 |
|  |  |  |

This plot gets the dot product of all pairs of N*T, where N is the matrix of all neurons (rows) and their output weights (cols).

~~We see that the dot product of large and tall for all neurons (after passing through the entire model, basically) is higher with each other than the typical average. This shows that the neurons typically find some "similarity" between the two tokens.~~

If we isolate the neurons with the biggest impact, and only take the dot prod of tokens with those neurons, this similarity is prob even bigger.

With these 100^2 data points, it doesn’t look like a normal distribution

<

**Compute dot products for "tall" and "large", and compare the similarities (eg. which are in the top) AND identify their common top neurons**

congruence_list = get_congr_token("large")

Layer: 11, Neuron: 3033, Dot product: 10.153202056884766
Layer: 11, Neuron: 584, Dot product: 6.391915798187256
Layer: 11, Neuron: 2123, Dot product: 6.043896675109863
Layer: 11, Neuron: 2888, Dot product: 6.002010345458984
Layer: 11, Neuron: 1941, Dot product: 4.2660627365112305
Layer: 11, Neuron: 2361, Dot product: 4.212543487548828

congruence_list = get_congr_token("tall")

Layer: 11, Neuron: 3033, Dot product: 15.378734588623047
Layer: 11, Neuron: 584, Dot product: 9.504816055297852
Layer: 11, Neuron: 2123, Dot product: 8.900127410888672
Layer: 11, Neuron: 2888, Dot product: 7.337953567504883
Layer: 11, Neuron: 2727, Dot product: 6.2406721115112305
Layer: 11, Neuron: 2361, Dot product: 6.2252912521362305

congruence_list = get_congr_token("red")
Layer: 11, Neuron: 2604, Dot product: 5.678971290588379
Layer: 11, Neuron: 2227, Dot product: 4.7803850173950195
Layer: 10, Neuron: 1971, Dot product: 4.700037956237793
Layer: 11, Neuron: 2377, Dot product: 4.389562606811523
Layer: 10, Neuron: 609, Dot product: 4.308917999267578
Layer: 11, Neuron: 3033, Dot product: 3.4321320056915283

<<<

**Dot products of input after first MLP layer**

[TBC; work out matrix multp shapes]