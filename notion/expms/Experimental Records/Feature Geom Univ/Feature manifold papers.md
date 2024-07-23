# Feature manifold papers

- [https://distill.pub/2019/activation-atlas/](https://distill.pub/2019/activation-atlas/)
    - [https://chatgpt.com/c/e436350d-9af1-4811-ac1f-9d18a5412bb7](https://chatgpt.com/c/e436350d-9af1-4811-ac1f-9d18a5412bb7)
        - We also find that whitening the activation space to unstretch it can help improve feature visualization.
            
            Whitening the activation space involves transforming the data to have zero mean and unit variance. This process "unstretches" the data, removing correlations and making the features more independent and evenly distributed. 
            
        - how is it diff than normalize
            
            Whitening and normalization are different techniques for preprocessing data:
            
            1. **Normalization** typically scales the data to a range (e.g., 0 to 1) or adjusts it to have zero mean and unit variance on a per-feature basis.
            2. **Whitening** goes further by decorrelating the features, transforming the data to have zero mean, unit variance, and removing any linear correlations between features. This process ensures that the data is more evenly distributed and independent, which can improve the interpretability of feature visualizations in neural networks.
    - we estimate that the effect of a neuron on a logit is the rate at which increasing the neuron affects the logit.
    - feature compos
        
        There is another phenomenon worth noting: not only are concepts being refined, but new concepts are appearing out of combinations of old ones. Below, you can see how sand and water are distinct concepts in a middle layer, mixed4c, both with strong attributions to the classification of “sandbar”. Contrast this with a later layer, mixed5b, where the two ideas seem to be fused into one activation.