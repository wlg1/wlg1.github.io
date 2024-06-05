# Steps towards goal

**Steps towards goal**

Topic 1: features between English - Numbers - ForeignLanguage

MOTIV: this essentially reproduces Gould et al but for a different domain

1. Test prompts to ensure diff models can recognize different language numbers
2. Test prompts to ensure diff models can handle math reasoning
3. Alter English reasoning at certain layer: activation addition for language numbers
4. feature decomposition in small models for actv addition
5. features: differences in language domain vs similarities in index
6. write about its use: understand language repr and abstraction better

Topic 2: small circuits for intervaled sequence continuation  

MOTIV: enhance circuit + feature analysis skills (not about analogies; save that for next paper)

1. test prompts for diff models (may make table)
2. find circuits, and show alter interval-1 can alter interval-2
    1. seqlen circs
    2. letters, spanish numwords and ranks and months
3. alter circuits/features for math reasoning + equation prompts
    1. compare to circs for these word problem + equation prompts
4. possible recognition by features (unlikely, since all is numbers; is good for practice)
5. write about its practical use: diverging circuits

Circuit Workflow

1. test prompts, generate data
2. auto ablate heads and MLPs to find impt ones
3. on impt ones, logit lens / ov scores
4. on impt ones, attn pats
5. iter edge pruning + viz

neg results are okay. 

[https://2024.emnlp.org/calls/main_conference_papers/](https://2024.emnlp.org/calls/main_conference_papers/)

papers may contribute negative findings

instead of claiming there are shared circuits, just explain how the model handles languages, word problems and types of incremental sequence patterns (intervals) differently. Steering is optional (can be second paper or workshop)

we have not yet looekd at X but will look into it soon

- after acl got rid of anonymity in 2024, can you submit the paper to acl, but during reviewing propcess, update the paper on arxiv?
    
    he new policy, effective from January 2024, permits authors to post and discuss non-anonymous preprints at any time, even while the paper is under review. However, the submitted paper itself must remain anonymized during the review process to preserve the integrity of double-blind peer review.
    
    While you can update your arXiv preprint, it's important to avoid excessive publicizing to ensure the recruitment of qualified and unbiased reviewers.
    

Future papers

1. OPT: show for multiple models and ablate by diff pos (if nonseq words there)
    1. OPT: larger models: try nnsight