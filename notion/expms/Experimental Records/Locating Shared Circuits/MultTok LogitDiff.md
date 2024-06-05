# MultTok LogitDiff

[test_logit_diff_multToks.ipynb](https://colab.research.google.com/drive/1aVc2UfFK1mqT4ngeyHBEvoSr6izJD29e#scrollTo=WgbtY5fFPb71)

POSS 1: sum{over all toks for #corr toks}(corr-incorr) logit diff of before and after ablation

POSS 2: sum{over all toks for #corr toks}(corr) logit diff of before and after

Take total logits of correct tok, and take diffeerence with corr tok after ablation

Poss 1 is harder to use because we don’t know what the incorr logit token would be. In IOI, this was clearly the “swtiched” token, and we wanted to see how different it was from it. In this case, with random, we COULD take the “last seq member” as the incorr logit token, but this is not easy in the case of llama-2 because say the last token is “8”, but we expect the correct answer to be “10”, how do we compare their logits diffs for diff num tokens? Thus, go with Poss 2. We just measure how much ablation causes the corr logit to fall. The bigger the fall, the more prominent.

The higher the score, the more was ablated

In Poss 1, a (corr-incorr) higher was better. Here, a higher corr is also better.

This is easier to compare ablations as a percentage: `(ablated_score / clean_score) * 100`

This is the **“Simpified Perfomance Score”**

in clean run, there is no logit diff either. just add up the expected’s logits! [this is used for circuit eval, not needed for gen results]

- ask chatgpt. include: eg) John and Mary went to store. John gave the toy to : incorr tok is John, corr tok is Mary ; The goal is to determine how much ablating an attention head in a transformer would have on making the incorr tok be higher than the corr token in logit
    
    To determine which of the two propositions (POSS 1 or POSS 2) is better, let's break down each one and understand their implications:
    
    ### POSS 1:
    
    \[ \text{sum}\{\text{over all tokens for #correct tokens}\}(\text{correct} - \text{incorrect}) \text{ logit difference of before and after ablation} \]
    
    ### POSS 2:
    
    \[ \text{sum}\{\text{over all tokens for #correct tokens}\}(\text{correct}) \text{ logit difference of before and after} \]
    
    ### Detailed Breakdown:
    
    **POSS 1:**
    
    - For each token where the correct prediction was made before ablation, you calculate the difference between the logits of the correct and incorrect tokens.
    - Then, you take the difference of this value before and after ablation.
    - Finally, you sum these differences across all such tokens.
    
    **POSS 2:**
    
    - For each token where the correct prediction was made before ablation, you only consider the logit of the correct token.
    - Then, you take the difference of this value before and after ablation.
    - Finally, you sum these differences across all such tokens.
    
    ### Comparison:
    
    1. **Measurement of Impact:**
        - **POSS 1:** This method directly measures the change in confidence for the correct token compared to the incorrect one, which can give a more comprehensive view of how the ablation affects the model's discriminative ability.
        - **POSS 2:** This method only measures the change in confidence for the correct token, which might be simpler but potentially less informative.
    2. **Discriminative Power:**
        - **POSS 1:** By considering the difference between correct and incorrect logits, you get a sense of how well the model distinguishes the correct token from incorrect ones, providing a more nuanced insight.
        - **POSS 2:** Focusing only on the correct token might miss out on understanding how the incorrect token logits are affected, which can be crucial in some contexts.
    3. **Complexity and Interpretability:**
        - **POSS 1:** More complex, but potentially more informative.
        - **POSS 2:** Simpler and easier to interpret but might lack depth in understanding the impact on model performance.
    
    ### Conclusion:
    
    **POSS 1** seems to be better if you aim for a comprehensive understanding of the impact of ablation on the model's performance, as it considers both correct and incorrect token logits. This method can provide deeper insights into how the ablation affects the model's confidence and discriminative power. However, if simplicity and ease of interpretation are prioritized, **POSS 2** might be preferred, although it might not capture the full picture.
    

---

- corr: try between pred and expected, instead of incorr and expected?
    - expected: store these tokens IDs (inds) in a list, and return
    - get logits by expected ind and the new top ind?
        - no, it must STILL be corr, bc what if new top ind is same as expected?
        

---

One issue with comparing performance scores across tasks is that they heavily depend on the prompt dataset. But an 80% from numerals prompts is different than 80% in months prompts. This is just an approximate.