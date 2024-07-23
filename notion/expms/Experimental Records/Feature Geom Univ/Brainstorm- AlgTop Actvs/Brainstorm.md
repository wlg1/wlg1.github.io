# Brainstorm

Draft Summary:

Adapt TopoBert to mech interp of large language models to study clusters of activations that can be linked to behavior, and thus edited. Since this method could find patterns of activations to diagnose adversarial robustness of image models and track fine tuning in LLMs, it likely it can be adapted to diagnose similar metrics in LLMs.

This would be innovative because many techniques so far have not edited by identifying clusters of activations, which I believe are key to finding features entangled with behavior. I think it's possible to combine this with SAE features- that is, to cluster by SAE features and not just neuron activations.

The clusters are of inputs, not of components like features. But the DIMENSIONS of the space are the features. So we can correlate concepts/behaviors with input clusters (eg. these inputs are all “angry” behavior) and find which concepts intersect. These inputs cluster based on being measured by intm layer features, not just input embedding.

The connections between concept clusters is different than the causal or correlations bewteen features found by patching because the connections show the interpolated transition from one concept to another, showing their relation in terms of LATENT SPACE, by shape and not just distance, and not just stating they’re correlated (fire together) in the network

Can give each input sample as a pt and look for clusters of samples 

Can also give each feature vector of a single input as a pt and look for clusters of features

Identify if two datasets can be deformed into one another by them sharing the same mapper graph (which has the same topological invaraints, like voids). Then, are they analogous, concept-wise? If so, that means it’s evidence there’s a correlation between analogous datasets and their shapes (of sample activation embeddings) in latent space.

---

To Do:

- Comapre with k-means clustering

---

Clustering vs Mapper

- Relate not just features, but relate between CLUSTERS OF FEATURES.
    
    ![Untitled](Brainstorm%2053e87325d0ab4c3ebc13c54c4682695b/Untitled.png)
    

This is entanglement because two clusters with more overlap have more 

We associate clusters with behavior, and measure behavior entanglement based on cluster overlap. When a cluster from behavior A has an edge with a cluster from behavior B, those behaviors share features.

Can’t we just do this with k-means? Compare it with mapper graphs.

---

Novel approaches

- Usually, mapper uses point cloud of input embeddings. But in our project, we transform embeddings into feature points via interm layers and SAE
- Compare the nerve shapes before and after fine training. Compare the nerve shapes before and after ablation (of a prevous layer to the activations). How does ablation or steering of a previous layer change the latent space embedding in the next layers to the last?
- Finding the best lens practices function for a particular dataset beyond best prac remains an open problem.
    - TopoBert uses L2 norm of activation by an input token
        
        ![Untitled](Brainstorm%2053e87325d0ab4c3ebc13c54c4682695b/Untitled%201.png)
        
    - indirect effect on logit after ablation?
    - functionality? (see ct metric paper)
    - feature dim (by cosine sim proj)?
- We can find what all inputs in a T neigh have in common. We can auto label them by GPT-4. We can also look at what features that have in common; that is, what directions they are all pointing in that make them cluster close there.
    - we measure that two points are in same neighborhood if they are within 1) a metric and 2) fall in the same filtering interval. A point can be in more than 1 neighborhood
    - In TopoBERT, purity was a score based on accuracy proportion. In generation, there is token ranking acc under only specific circumstances (eg. entity tracking or seq cont). Otherwise, to measure if the generated behavior “matches” we can use auto-labeling of output.
        - However, we are not trying to find what inputs in clusters “do well” so this is not a good diretion to go in. We are trying to find which features to edit
            - After clustering inputs and labeling clusters by concepts, we can find “concept regions” where we can try to move one input from one T niegh to another T neigh by taking the direction between T neighs and adding them.
            - Concept neighs can be characterized by the feature dirs they reside in.
                - We can also filter by feature dir. The filter determines the cluster because two inputs are in same cluster only if they map to same feature interval or are “close enough” geometrically along a feature dir. Usually, the advantage of the filter is that it does not NEED to be about geometric distance, but a non-geometric property.
                    - **For instance, we can filter them using an unembedding metric to see what vocab space they map into.**
                        - Hypothesis: before ablation/editing, these nodes
- We can put inputs of different concept hierarchies or different ways to categorize behavior to see how clusters related to abstract hierarchy relations
- Usually behavior is characterized by what is chosen: token A or B. We can also give multiple choices of single tokens to the model and ask what it’d choose, so it’d predict the actual word rather than just A or B.
- how to use more than 1 filter function

---

When presenting, give the high level why first (eg. why use this over simpler clustering) THEN give how. Giving how before the why makes people ask “why do we need to know the details of how? feels like a waste of time if it’s not justified first”.