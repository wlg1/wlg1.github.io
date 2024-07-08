# Main goal and contributions

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