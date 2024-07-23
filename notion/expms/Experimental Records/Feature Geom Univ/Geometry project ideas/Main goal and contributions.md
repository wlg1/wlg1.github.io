# Main goal and contributions

There are two goals of this project:

1. Find more evidence for feature manifolds (would help if theoretically there is a direction to look for)
2. Find evidence for feature relation universality (may or may not be manifolds)

**primary**: measuring universality of representation spaces across models, mapping features from one model to another by their distances AND topological invariants (eg. polytope and circle structures) in representation space

secondary:

proj approach 1: how feature affects other features causally

proj approach 2: how feature affects other features geometrically

1. Find higher-order structures in latent space
    1. This can be clusters, polytopes, or cicles. We know they exist; can we map clusters
    2. This was already found in the last token and last layer latent space
    3. Can we extend this to previous layers?
    4. Can we find “circuits” of clusters?
2. Find universality among SAE features by relations
    1. This requires a mapping of pairs! So needs a matching algorithm!
    2. We can start by just a query; Eg) find a polytope from Model A to Model B using similarity metric and matching algorithm
    3. This is more about “mapping poltyope from one to another”, showing it’s the same polytope. Not yet entire spaces.
        1. Though Dar et al DID map entire spaces?
3. Steer polytopes and see what happens

3 approaches to sim measure

CCA and cka, and more like tda on features
Mnn on inputs
Mnn on features after labeling (most uncertain to be accurate due to relying on feature labels that aren't strongly defined, but may be refined)

Manifold sim: see p14 of “sim of nns” 

manifold: locally (in tangent space) it’s euclidean, but globally is not

for now, dont think of manifolds, think of just is “father mother daughter” arranged in similar directions (topologically) across models. 

- The circle of “months” is a structure already found to be topologically the same across models. What about other concepts?
- Hypothesis: “father mother daughter” may also be arranged in similar directions (topologically) across models
    - They may not be arranged in a circle, but their relative “linear directions” to each other may be similar, or “father” is always closer to “male features” that often co-exist with “father”
    - **How many relative similarities are there?** The more there are, the more similar the feature subspaces are
    - So when features split, do the split the same way topologically?
    - Eg) If “Animals” splits into “cat dog bird”, is this topological arrangement of concepts the same across models?
- feature manifold Trenton bricken
    
    ![Untitled](Main%20goal%20and%20contributions%204b749c6c252b47b8ba383ddfa26e63d9/Untitled.png)
    

[https://colah.github.io/posts/2014-03-NN-Manifolds-Topology/](https://colah.github.io/posts/2014-03-NN-Manifolds-Topology/)

[Phil meeting 2](Main%20goal%20and%20contributions%204b749c6c252b47b8ba383ddfa26e63d9/Phil%20meeting%202%20f1867392c6234c588cb3b3705a261ee9.md)

take an existing, ablate, then compare sae similarity

whats ideal sae size for featur splitting

---

**Arrangements sim across models?**

- brainstorm main rsch topics
    - under what conditions do models learn manifolds differently
        - in 2L, perhaps feature split across layers?
        - are they learning the same subspace? how to measure in high dim?
        - difference if use top k? number of examples? make table for saes to train.
    - which features appear to be frequently learned across models using same dataset?
        - which ways that features split appear to be frequently done?
        - are they learning the same high dim relations?
        - conditions for saes which show more similarity between two models