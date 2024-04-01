# Outline Writeup Draft

[Paper Draft- Comparison Circuits](../../Paper%20Drafts%20c8403ec170204b3aa40fd28465a5635d/Paper%20Draft-%20Comparison%20Circuits%20852d577eb555460e87ae511a1750ef50.md) 

Sec 1- intro

Generalizes IOI by looking into various types of circuits that compare info

Methods and Results (sec 2): 

(3 and 4: desc how slightly changed from existing)

1. Logit Diff and Lens (stream, layer, head) to find general, important areas
    1. average logit diff in dataset (of right to wrong output)
    2. line graphs and heatmaps
2. Activation patching ~~+ path patching~~ to find important heads in those areas
    1. Attention heads attribution only describe what position is attended to. What they do with it requires different analysis. Head two may attend to what’s at “tall”, but one may move info (past its gates) with “tall” and the other may move info with “short” (so use step 3)
3. Attention Patterns and Correlation Plots to hypotheize functions of important heads
    1. Attention Patterns (QK) finds what dst token attends to what src token
    2. Attn head output (projections onto components) vs token logit scatter plots 
    3. See what it does by OV matrix (eg. copy scores): multiply inputs by OV matrices, then unembed to vocab space (see logit lens). See how many samples have this token as top-5, compared to if use OV matrix of averaged head
    
    [https://colab.research.google.com/drive/1GQo_RSEY40ncByvwy81kxwSKGPHlbxSx](https://colab.research.google.com/drive/1GQo_RSEY40ncByvwy81kxwSKGPHlbxSx)
    
    (for steps 1-3)
    
    Antonym (opposite, duality) heads:
    
    [https://colab.research.google.com/drive/1TXi0A-TNXYr748Z23kpDw2YEHGjafOUO](https://colab.research.google.com/drive/1TXi0A-TNXYr748Z23kpDw2YEHGjafOUO)
    
4. Congruence of neurons and embedded vectors at different places in model
    1. Neuroscope (for MLPs)
    2. Dot prod of congruence
    
    [https://colab.research.google.com/drive/1lZQkZ5u2mQxsYyiGaUKbW-XjdHP0GJpA](https://colab.research.google.com/drive/1lZQkZ5u2mQxsYyiGaUKbW-XjdHP0GJpA#scrollTo=8zWhomib5KMa)
    
    [https://colab.research.google.com/drive/1Gvt1esiymU9UPfDKB1Nc7gMMUhJadLa1](https://colab.research.google.com/drive/1Gvt1esiymU9UPfDKB1Nc7gMMUhJadLa1)
    
    v2 simplifies code into fns
    
    [https://www.notion.so/Knowledge-Neurons-in-Pretrained-Transformers-2bdb62adf77d4e94aa77d2a36375e570](https://www.notion.so/Knowledge-Neurons-in-Pretrained-Transformers-2bdb62adf77d4e94aa77d2a36375e570?pvs=21)
    
5. (in-progress) debug path patching modifcations to constants
6. (in-progress) Construct hypothesized circuits based on how ablating then patching h→R affects node R
    1. to use actv patching (not necc path), just look at the diff of the head's output value (clean-corr), instead of logit dif (pronoun circ, fig 7); this plots heatmap. recursively find more. IOI fig4c shows bar plots of NM attn after patching all S-inh
    2. Test on the 3 metrics: faith, compl, minim
    3. (in-progress b/c code inprog) ACDC, metric thres for logit diff
    
    [https://colab.research.google.com/drive/1cFJc2Zc1fh_BXV42q3h4zfvRikINE_Mo#scrollTo=YaJBj52XWzMP](https://colab.research.google.com/drive/1cFJc2Zc1fh_BXV42q3h4zfvRikINE_Mo#scrollTo=YaJBj52XWzMP)
    
7. (in-progress) Track dot product movement of info of various tokens to combine to end
    
    [https://colab.research.google.com/drive/1rch6VaG9O1YFJT1wPjjbXyDgXizGT7WV](https://colab.research.google.com/drive/1rch6VaG9O1YFJT1wPjjbXyDgXizGT7WV)
    
    ISSUES: not always clean due to info not taken into account (eg. pos emb)
    
8. (in-progress) Edit those heads and MLPs (rank-1) to try to change how circuits move info (attn weights) and what info (MLP weights) [describe U vec in ROME]

Code to modify: generalized to functions

- dataset
- copy scores, scatter plot
- logit diff and path patching
- congruence (at various areas)

Plots:

1. logit lens avg and by layer
2. logit lens heads heatmap / activation patching on heads
3. attention patterns
4. correlation plots / copy scores
5. Congruence

Tables:

| Input | Model | Prediction | Logit |
| --- | --- | --- | --- |
|  | GPT-2-Small |  |  |
|  | GPT-2-Large |  |  |

Section 2a: Latest Subject Circuits

Section 2b: Adjective Comparison Circuits

(repeat same sub-sub-sections as above, but in diff sub-section)

Sec 3: Experimental Validation

Now that the circuits are found, check how necessary they are for correct prediction. Check metrics such as faithfulness. Then for editing, test on various datasets for metrics such as generalization.

- (sec4, Related work)
    - IOI
    - ROME

(sec 5- many ideas for future work)