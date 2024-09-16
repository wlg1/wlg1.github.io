# Kiho meeting notes- sept 4

- Instead of comparing discrete features (which are harder to ensure are learned univ), compared SPACES by est these spaces using LDA similar to this
    - CHECK: are they just reln similar bc learn similar clusters? even so, that’s sigf, but not as much if they also learn **similar relns bewteen clusters** (each cluster repr by LDA)
    - check with kiho is lda used right here to repr cluster/semantic subspace
    - (To do- use LDA to approximate representative concepts from a cluster of features instead)
        - but which feat from cluster to select? perhaps we should take LDA of cluster, or mean of it. though, if those features all seem to cluster together, we can just take a repr. issue is, they all don’t- we’re not taking from cluster but from same “category

---

Kiho response:

- in paper, find best subspace so that projections are clustered well
    - clustering isn’t about projection
    - LDA wants to find some subspace

[https://arxiv.org/pdf/2406.18534](https://arxiv.org/pdf/2406.18534)

- fig 4: learn subspace similar to lda
    - find subspace where points are clustered to some centroid

- lda and this method can approx a semantic subpsace of features if you have labels
- if use lda to find the pronoun subspace in model A, and another lda to find another pronoun subspace in model B, and then apply sim metrics to that
- subtract bias? centering already if use decoder weights bc not using bias weights
    - gemmascope: decoder are already nearly orthogonal to each other (by JL lemma)
        - can cluster so not everything is same orhotgonality
- def of subspace: mammal-bird-fish - don’t want hierarchy on subspace?
- how to compare lda vectors?
- lda for decoders not promising
    - decoders are normalized, so no magnitude info, and lda doesn’t have magniutde info
    - lda can capture subspace, but may just be property of high dim space not concept. so any random decoders and learn lda, may see some separation.
    - hidden size is too small (16k only) for saes, lda issues?

- can we sim metric on multiple paired lda vectors?
    - issue is featuers may not be exactly learned across models, so approx their subspaces using lda to compare subpsaces instead of features directly
    - then we have subspace for 'animal', and subspace for 'plant', each approx by an lda vector. and we do this for both models to find animal and plant lda approx for each. we pair their lda approx by labels, and apply sim metric
- subsupace animal uses featuers in an animal cluster. can we use lda to approx the animal cluster
    - search thru labels using keywords and then find all features that have those keywords, and then they may in a cluster although some may in multiple clusters, and then use those to train lda

- dataset size: number of featuers is very low
    - magnitude is alos a problem
    - even if we find lda for decoders,
    - sae has no ‘lda’ space?

- another extreme difficulty is featuers are spread across diffrent layers
    - however, i do find correlations across these diff layers
    - so we can only saes of each layer. brute force try everything

- disentangling: clustering of features
- kiho paper: hiearchy between various concepts that are orthogonal

- similar fig 5 of disentangling paper: if similar heatmaps, are they similar in hiearchies?
    - if the same for LLM, yes
    - but for SAEs, elem for each block are different. ML block can have more features, and across models, the featuers are diffrent. one sae may learn more features- even if same latent size, two models can learn them differently. then can we concldue they’re similar?
        - ISSUE: different numbers.
- high dim space: be careful to conclude similarity