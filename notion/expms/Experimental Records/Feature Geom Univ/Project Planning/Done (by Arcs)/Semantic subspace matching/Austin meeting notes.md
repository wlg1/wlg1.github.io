# Austin meeting notes

(see technical issues that are highlighted for main tasks to focus on)

issue colab: even if you delete and batch things, you still get OOM in colab. so try other resources.

**Main topic:** measure extent of similarity in feature spaces and semantically similar subspaces in SAEs of similar LLMs

Steps to the main results: (see step 5 of RSA paper for this framework)

1. Get mean activation correlation of two decoder SAEs for similar LLMs
    1. [https://transformer-circuits.pub/2023/monosemantic-features#phenomenology-universality](https://transformer-circuits.pub/2023/monosemantic-features#phenomenology-universality)
    2. similar LLMs: same tokenizer, different initalizations
        1. may be different layers, but prefers 1L toy model (which don’t have)
2. Pair each feature A with its max activation correlated feature from model B
    1. may not be 1-1 ; measure both pairings that are not 1-1 and 1-1
3. Rearrange the order of features in each matrix to pair them row by row
    1. this solves a permtuation issue since these space similarity metrics like nearest neighbors require pairings
4. just apply various metrics to get a “paired score”
5. take N random pairings (so far, I used 100 due to speed, but ideally want 10k) and estimate a null distriubtion
6. simple p-value of where this “paired score” (from step 4) falls in the null distribution
7. apply steps 1 to 6 to the LLMs and compare the step 6 result to SAEs
    1. report: mean, SD, p-value
8. show that the sim metrics on LLMs are not stat sigf, but they are stat sigf on SAEs
    1. this will suggest that SAEs can find feature relations that are across models which aren’t found by LLMs
    2. previous work on LLM similarity compared the input pairings across LLMs, rather than using neurons. this may be bc neurons aren’t paired (due to polysemanticity)

---

Main things to do

- more data and more models
- double check statistical soundness- theoretical concerns?

---

Steps to get mean activation correlation

1. get data as tokens
2. pass tokens thru LLM and save actvs
3. pass actvs thru saes to get sae actvs
4. get corr matrix of two sae actvs ; get max corr

---

Main conceptual issues to think about (that need help with)

- is 1-1 pairings valid
    - and why does that work better when taking it full features?
    - HYPOTHESIS: 1-1 almost removes the “big cluster” that many features in B map to, which is features 2604 (etc) in model A. These “big cluster” mappings are inaccurate. However, when we use 1-1 in features under 0.4 sim, that removes too much of the 2604, so in comparison using the “same number” in random pairings is inaccurate. isntead those random pairing numbers should not include all the number of those features mapped to 2604 etc.
        - check feature count in 0.4 sim
- for measures like svcca, is it stat sound to have low absolute scores, but high relative difference, for correctly paired vs randomly paired, in order to show pairing is stat sigf?
    - [https://chatgpt.com/c/cac098dc-0532-4e70-8c93-86d40b669b61](https://chatgpt.com/c/cac098dc-0532-4e70-8c93-86d40b669b61)
        - justify this with more theoretical reasoning
    - use RSA paper to support this
    - if sound, how to convince reviewers that it’s sound
- how stat sound is “random pairings” p value? do we follow RSA method correctly?
    - use RSA paper to support this
- argue the importance of this: previous work on LLM similarity compared the input pairings across LLMs, rather than using neurons. this may be bc neurons aren’t paired (due to polysemanticity)
- matching features by layer- if not the same exact number of layers, won’t guarantee matches
    - SOLN: must include 1L toy model expms

*** Main technical issues to think about (that need help with)**

- using openwebtext ddata, get more than 400 samples (pref 1000 samps) using maxseqlen of at least 300 (pref 512) to pass thru SAE without OOM errors
    - batchproc_corrs / corr_large_data_v2.ipynb
    - [https://colab.research.google.com/drive/1lP2nXMIcSdGq8vOtp00rto5RLKJyc8DH#scrollTo=m7Gchzq341Bw&line=3&uniqifier=1](https://colab.research.google.com/drive/1lP2nXMIcSdGq8vOtp00rto5RLKJyc8DH#scrollTo=m7Gchzq341Bw&line=3&uniqifier=1)
- how to train multiple 1L toy models
    - we’re going to get much better results for 1L
    - ask around for existing 1L toy models
    - it doesn’t have to match anthropic’s 1 billion token dataset toy model
        - we should much less
    - how much compute do we need? what resources?
        - multi-gpus on modal
- speed of getting random pairing scores (so may do this in parallel)
    - ask author of library (max)
- explore the existing code and train stuff
    - want more data and more models
    - double check main code (once it’s cleaned up and posted, so feasible to review)

To try

- Try SAEs at different training phases

---

Outline of deliverables

1. GEOMETRIC: pvalue tests on LLM vs SAEs of paired sim metrisc
    1. first find semantic SUBspaces and match them using metrics
        1. estimate subspaces using LDA
        2. find subspaces by clustering; project by UMAP / PCA
    - metrics
        1. svcca
        2. nearest neighbors?
        3. procrustes
        4. rsa
2. FUNCTIONAL similarity
    1. universal steering vectors
3. ground truth feature relations of SAE

future work

1. algorithm for featuer matching
    1. prob not possible bc not discrete features, so have to map subspaces approx by LDA?
2. TOPOLOGICAL: compare mapper graphs of LLMs vs SAEs; use optimal transport metric
    1. pers homology
3. train an sae that works for both LLMs? 

---

Impt notebooks

- sim_mod_pythias / simSAE_pythias_70m_160m_all_layers.ipynb
    - compares layer by layer ; main results
- batchproc_corrs / corr_large_data_v3.ipynb
    - stat tests
- batchproc_corrs / corr_large_data_v2.ipynb
    - does it in batch

---

Impt Papers

- SIMILARITY OF NEURAL NETWORK MODELS: A SURVEY OF FUNCTIONAL AND REPRESENTATIONAL MEASURES