# 3. Figuring out Head Functionality for Most Recent Name Movers

[Most Recent S Name Movers](../../../Interpret%20Attention%20Head%20Circuits%20of%20Comparison%20In%20c1d0ec7e43214760b4062ae4cdc0cd6b/Most%20Recent%20S%20Name%20Movers%20a72ccc6fdccc4e4baa78251399fdd2d7.md)

[Custom Dataset for Circuit Discovery](../../../Interpret%20Attention%20Head%20Circuits%20of%20Comparison%20In%20c1d0ec7e43214760b4062ae4cdc0cd6b/Custom%20Dataset%20for%20Circuit%20Discovery%20ba320205d59c4251bb59c262f1c839b5.md) 

[Modify copy circuits code](../../../Interpret%20Attention%20Head%20Circuits%20of%20Comparison%20In%20c1d0ec7e43214760b4062ae4cdc0cd6b/Modify%20copy%20circuits%20code%20004c16a403b04ddbb7c09b62cad532d7.md) 

Outline:

Attention Patterns, Scatterplot and Copy Scores

<<<<<<<<<<<<<<<

Attention Patterns

most_recent_S_attn_pat.ipynb

[https://colab.research.google.com/drive/1KaqcS92-BI4FZ7m-r8rCW9tIovxA_s93#scrollTo=M93Hy1XdqNKm&line=1&uniqifier=1](https://colab.research.google.com/drive/1KaqcS92-BI4FZ7m-r8rCW9tIovxA_s93#scrollTo=M93Hy1XdqNKm&line=1&uniqifier=1)

For the attention heads that matter, check their attention patterns to see where they are active on (dest token) and where they attend to (source token)

L8H11:

The last token “is” (dest) attends to the latest subject (src)

The second last token “child” attends to both 2nd latest and latest subject, but moreso on latest 

But in a neg name mover head, the last token “is” (dest) ALSO attends to the latest subject (src)

<<<<<<<<<<<<<<<

Scatterplot

most_recent_S_name_movers_DRAFT.ipynb:

[https://colab.research.google.com/drive/1NCBOLPx038FxwEacmHDsCesWIAW1z8kU#scrollTo=AwhyxrN3R8xL&line=2&uniqifier=1](https://colab.research.google.com/drive/1NCBOLPx038FxwEacmHDsCesWIAW1z8kU#scrollTo=AwhyxrN3R8xL&line=2&uniqifier=1)

**Methods**

x-axis, attention probability: this is the QK ACTIVATION VALUE of a (layer, head, token position), given a subject token. If ths subject token appears multiple times, it takes the sum of its values for every position it appears in.

y-axis, dot product: logit score $<h_i (X), W_U (N)>$ measuring how much head $h_i$ on input $X$ is writing in the direction of the logit of the name $N$ (subject)

[see code for the calculation](../../../Interpret%20Attention%20Head%20Circuits%20of%20Comparison%20In%20c1d0ec7e43214760b4062ae4cdc0cd6b/Most%20Recent%20S%20Name%20Movers%20a72ccc6fdccc4e4baa78251399fdd2d7.md)

This dot product is like taking the “final” activations and projecting into output space, but instead of “final”, this is the “premature intermediate activations”. That is, what prediction values does the head assign to the subject token? We must use W_U because the activations don’t contain the vocab_size dim.

The x-axis, attention score, shows how much attending (end → subject) correlates with the head outputting the subject. That is, it gives more evidence that the REASON the head outputs that subject is because of that specific attention.

<<<

How previous results were described:

IOI paper:

- All three Name Mover Heads have a copy score above 95%, compared to less than 20% for an average head.
- The results are shown in Figure 3c: higher attention probability on the IO or S token is
correlated with higher output in the direction of the name (correlation  > 0:81, N = 500)1.

<<<

Current results:

![Untitled](3%20Figuring%20out%20Head%20Functionality%20for%20Most%20Recent%20%20d35d8e08cfc649d7838236eb03e6bf22/Untitled.png)

For N=10: higher attention probability on the subject tokens are correlated with higher output in the direction of the name. We observe that the dot product and attention probability are both much higher for the latest subject than the other subjects. In general, the more recent a subject is, the higher its dot product and attention probability are.

Latest subject: whenever end token attends to subject a lot, then residual also points in subject token’s direction (in vocab space) a lot

One hypothesis is that the signal for a “more recent” subject has not “died out” as much because the model wants to attend to what’s “more recent” as “more relevant”; tokens from before are considered less relevant.

<<<

Make new notebook to keep outputs of bugs in prev. 

**latest_S_name_movers_DRAFT_v2.ipynb** cleans up bugs and runs from start w/o errors

[https://colab.research.google.com/drive/1LtBE2K4EOEpZNj-RJD62ZrxSkDnmI4L-](https://colab.research.google.com/drive/1LtBE2K4EOEpZNj-RJD62ZrxSkDnmI4L-)

**Correlation:**

To calculate the correlation between two variables in a scatterplot, you can use the `pearsonr` function from the `scipy.stats` module in Python. Here's an example of how to calculate the correlation:

```
import scipy.stats as stats

# X and Y are the variables for which you want to calculate the correlation
# They should be arrays, lists, or pandas Series containing the data points
correlation, p_value = stats.pearsonr(X, Y)

print("Correlation:", correlation)
print("p-value:", p_value)

```

In the code above, `stats.pearsonr(X, Y)` calculates the Pearson correlation coefficient between `X` and `Y`. It returns two values: the correlation coefficient and the p-value.

- The correlation coefficient (`correlation`) ranges from -1 to 1. A value close to 1 indicates a strong positive correlation, a value close to -1 indicates a strong negative correlation, and a value close to 0 indicates no or weak correlation.
- The p-value (`p_value`) represents the probability of observing the correlation coefficient under the null hypothesis that there is no correlation between `X` and `Y`. A lower p-value suggests stronger evidence against the null hypothesis.
    - what does p-value mean in correlation?
        
        In correlation analysis, the p-value represents the probability of obtaining a correlation coefficient as extreme as, or more extreme than, the observed correlation coefficient, assuming that the null hypothesis is true. The null hypothesis in correlation analysis is that there is no significant correlation between the two variables being studied.
        
        The p-value is used to assess the statistical significance of the correlation coefficient. It helps determine whether the observed correlation is likely to have occurred by chance or if it is a result of a true relationship between the variables.
        
        If the p-value is small (typically below a predetermined significance level, such as 0.05), it suggests that the observed correlation coefficient is statistically significant, and we reject the null hypothesis. This indicates that there is strong evidence to support the existence of a correlation between the variables.
        
        On the other hand, if the p-value is large (greater than the significance level), it suggests that the observed correlation coefficient is not statistically significant, and we fail to reject the null hypothesis. In this case, it implies that the correlation between the variables is likely due to random chance, and there is insufficient evidence to conclude a meaningful relationship.
        
        It's important to note that the p-value alone does not provide information about the strength or direction of the correlation. It only informs us about the statistical significance of the observed correlation coefficient. To assess the strength and direction of the correlation, one should examine the magnitude and sign of the correlation coefficient itself.
        

Make sure that `X` and `Y` contain numerical data and have the same length. The `pearsonr` function expects arrays, lists, or pandas Series as inputs.

By using the `pearsonr` function, you can calculate the correlation coefficient to measure the strength and direction of the linear relationship between two variables plotted in a scatterplot.

<<<

- how are prob and dot calculated?
    
    In the given function `scatter_attention_and_contribution`, the variables `prob` and `dot` are calculated as follows:
    
    1. Calculation of `prob`:
        - The variable `prob` represents the attention probability on the name.
        - It is calculated by summing the attention values from the `cache` for specific positions (`posses`) in the attention layer corresponding to the given `layer_no` and `head_no`.
        - The attention values are obtained from the `cache` using the key `f"blocks.{layer_no}.attn.hook_attn"`.
        - The attention values are indexed by `[i, head_no, ioi_dataset.word_idx["end"][i], pos]`, where `i` represents the index of the input sequence, `head_no` represents the specific head in the attention layer, `ioi_dataset.word_idx["end"][i]` represents the position of the end token in the input sequence, and `pos` represents the specific position of interest (e.g., `s1_pos`, `s2_pos`, etc.).
        - These attention values are summed using the `sum()` function to calculate the `prob` variable.
    2. Calculation of `dot`:
        - The variable `dot` represents the dot product between the residual and the name embedding.
        - The residual is obtained from the `cache` using the key `f"blocks.{layer_no}.attn.hook_result"`.
        - The residual values are indexed by `[i, ioi_dataset.word_idx["end"][i], head_no, :]`, where `i` represents the index of the input sequence, `ioi_dataset.word_idx["end"][i]` represents the position of the end token in the input sequence, `head_no` represents the specific head in the attention layer, and `:` represents all dimensions of the residual.
        - The name embedding in a specific direction (e.g., `s1_dir`, `s2_dir`, etc.) is obtained from the `model_unembed` variable using indexing.
        - The dot product between the residual and the name embedding is calculated using the `torch.einsum()` function with the equation `"a,a->"`.
        - The resulting dot product values are stored in the `dot` variable.
    
    These calculations are performed iteratively for different inputs and positions of interest, and the `prob` and `dot` values are appended to the `df` list for each iteration.
    

<<<<<<<<<<<<<<<

Copy Scores

QUESTION: If don’t use attention scores, doesn’t ti assume it’s the identity?

~~POS SOLN: it’s just a single embedding of a token, not a sentence, so tehre’s nothing else to attend to~~

<<<

Previous papers:

- We compute the proportion of samples that contain the input name token in the top 5 logits (N = 1000) and call this the copy score. All three Name Mover Heads have a copy score above 95% compared to less than 20% for an average head.

<<<

[https://colab.research.google.com/drive/1NCBOLPx038FxwEacmHDsCesWIAW1z8kU](https://colab.research.google.com/drive/1NCBOLPx038FxwEacmHDsCesWIAW1z8kU)

Find what heads are specific to certain inputs, and what's common to the template.

We compute the proportion of samples that contain the input name token in the top 5 logits (N = 1000) and call this the copy score. All W Name Mover Heads have a copy score above X% compared to less than Y% for an average head.