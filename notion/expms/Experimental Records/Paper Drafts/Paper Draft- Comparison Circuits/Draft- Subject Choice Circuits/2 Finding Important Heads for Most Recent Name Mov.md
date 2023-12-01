# 2. Finding Important Heads for Most Recent Name Movers

most_recent_S_attn_pat.ipynb

[https://colab.research.google.com/drive/1KaqcS92-BI4FZ7m-r8rCW9tIovxA_s93#scrollTo=VcFgqbcF4YvI](https://colab.research.google.com/drive/1KaqcS92-BI4FZ7m-r8rCW9tIovxA_s93#scrollTo=VcFgqbcF4YvI)

[Most Recent S Name Movers](../../../Comparison%20Circuits%20c1d0ec7e43214760b4062ae4cdc0cd6b/Most%20Recent%20S%20Name%20Movers%20a72ccc6fdccc4e4baa78251399fdd2d7.md) 

Based on IOI findings, we expect to find:

- Induction heads (b/c of in-context learning)
- Name mover heads
    - Find evidence for this using Copy Scores
- Subject influencing heads (here, seems to be most recent subject)

Can be done w/ just GPT-2-small

<<<<<<

**Direct Logit Attribution [IOI paper]**

- Was logit diff commented on? If so, how?
    - Only states average logit difference X over Y examples. The rest of its info was only used in activation patching comparisons (no figures)
- How was activation head patching described?
    - Include the heatmap Figure
    - 
- 

**Direct Logit Attribution [IOI paper]**

- average logit difference X over Y examples

<<<

**Logit Lens (this project)**

- average logit difference is 3.56 over 50 examples

<<<<<<

**How were** Logit diff head attribution **results described in previous papers/notebooks?**

- [[REF](https://colab.research.google.com/drive/1nD6tfM33StbAqXG5HnYPlC40hKSj8mzD#scrollTo=okhq4gxpIAiT)]  [**Exploratory Analysis Demo**](https://www.notion.so/Exploratory-Analysis-Demo-c61288d8f11b45d993c796ec28a62132?pvs=21)
    
    > We see that only a few heads really matter - heads L9H6 and L9H9 contribute a lot positively (explaining why attention layer 9 is so important), while heads L10H7 and L11H10 contribute a lot negatively (explaining why attention layer 10 and layer 11 are actively harmful). These correspond to (some of) the name movers and negative name movers discussed in the paper. There are also several heads that matter positively or negatively but less strongly (other name movers and backu name movers)
    > 
    > 
    > There are a few meta observations worth making here - our model has 144 heads, yet we could localise this behaviour to a handful of specific heads, using straightforward, general techniques. This supports the claim in [A Mathematical Framework](https://transformer-circuits.pub/2021/framework/index.html) that attention heads are the right level of abstraction to understand attention. It also really surprising that there are *negative* heads - eg L10H7 makes the incorrect logit 7x *more* likely. I'm not sure what's going on there, though the paper discusses some possibilities.
    > 

<<<

**How were activation head patching results described in previous papers/notebooks?**

- [[REF 2]](https://colab.research.google.com/drive/1nD6tfM33StbAqXG5HnYPlC40hKSj8mzD#scrollTo=XmBCzNlkIAib) [**Exploratory Analysis Demo**](https://www.notion.so/Exploratory-Analysis-Demo-c61288d8f11b45d993c796ec28a62132?pvs=21)
    
    > The easiest way to do this is to patch in the activation `z`, the "mixed value" of the attention head. That is, the average of all previous values weighted by the attention pattern, ie the activation that is then multiplied by `W_O`, the output weights.
    
    We can now see that, in addition to the name mover heads identified before, in mid-late layers the heads L8H6, L8H10, L7H9 matter and are presumably responsible for moving information from the second subject to the final token. And heads L5H5, L6H9, L3H0 also matter a lot, and are presumably involved in detecting duplicated tokens.
    > 

[****Interpretability in the Wild****](https://www.notion.so/Interpretability-in-the-Wild-f7e5e77ced0c4dd9812cc142ce372b37?pvs=21) 

> 3(b) Results of the path patching experiments. Name Movers and Negative Name Movers Heads are the heads that have the strongest direct effect on the logit difference.
> 
> 
> We see that only a few heads in the final layers cause a large effect on logit difference. Specifically, patching 9.6, 9.9, and 10.0 causes a large drop (they thus contribute positively to the logit difference), while 10.7 and 11.10 cause a large increase (they contribute negatively to the logit difference).
> 

<<<

Finding important heads draft outline:

- Aim (reason why use this)
    - AIM: To find important heads

<<<

Apply to current results:

**Activation patching to find impt (layer, tokens)**

- N=1:
    
    ![Untitled](2%20Finding%20Important%20Heads%20for%20Most%20Recent%20Name%20Mov%2045d975630e61406bb3c6b999ff1e7b9b/Untitled.png)
    
    We can immediately see that, exactly as predicted, originally all relevant computation happens on the LAST subject token, and at around layer 9, the information is moved to the final token.
    
    Restoring on the “switched” (corrupted) subject gives worse performance than the clean input, while restoring on the last subject restore performance.
    

N=50:

![Untitled](2%20Finding%20Important%20Heads%20for%20Most%20Recent%20Name%20Mov%2045d975630e61406bb3c6b999ff1e7b9b/Untitled%201.png)

<<

Logit Diff

![Untitled](2%20Finding%20Important%20Heads%20for%20Most%20Recent%20Name%20Mov%2045d975630e61406bb3c6b999ff1e7b9b/Untitled%202.png)

Impt pos heads:

- L8H11
- L9H9
- L10H6

Activation patching

![Untitled](2%20Finding%20Important%20Heads%20for%20Most%20Recent%20Name%20Mov%2045d975630e61406bb3c6b999ff1e7b9b/Untitled%203.png)

impt pos heads:

- L8H11
- L8H3
- L9H9

impt neg heads:

- L10H7
- L11H10

I think in some areas (later layers, early heads) logit diff gives more info, but at other areas (L8H3) activation patching has more info. If you look closely, there are a LOT more faded blue squares all over the activation patching plot, so it does give more info.

Include one or both in paper? Depends on what is found with their heads. If both these indicators turn up something “functional impt” in later tests, include both plots.

<<<

N=50 (only change subj, not desc): looks not that different from N=1

![Untitled](2%20Finding%20Important%20Heads%20for%20Most%20Recent%20Name%20Mov%2045d975630e61406bb3c6b999ff1e7b9b/Untitled%204.png)