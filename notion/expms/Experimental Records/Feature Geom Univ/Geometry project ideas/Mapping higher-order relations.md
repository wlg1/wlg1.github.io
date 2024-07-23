# Mapping higher-order relations

This maps categories of features to each other

As SAEs approximate the true features better (the SAEs or models get better), would they organize concepts in similar ways? For instance, we can plot clusters of features in UMAP to see that an “animal cluster” contains features for cat, dog, etc. Feature splitting with larger SAEs shows these concepts become more specific, meaning we may find specific concepts for cat, dog, etc. These features are not exactly “THE” dog feature (several layers often have several features fire high for dog, and we don’t always see the output being steered towards dog for these features, but some of them do) 

[https://www.lesswrong.com/posts/MFBTjb2qf3ziWmzz6/sae-feature-geometry-is-outside-the-superposition-hypothesis](https://www.lesswrong.com/posts/MFBTjb2qf3ziWmzz6/sae-feature-geometry-is-outside-the-superposition-hypothesis)

However, these clusters are not themselves necessarily the structure of the semantic space! They are a *downstream consequence* of the space being structured semantically. Any good semantic space would have these clusters as they are a property of the world and of the dataset.

I don’t think ad hoc explanations like ‘this cluster of features is all about the bay area in some way’ are actually useful for understanding things in general. I don’t think we have yet elicited the right concepts for talking about it. I also don’t think this structure will be solved on the current default trajectory: I don’t think the default path for sparse dictionary learning involves a next generation of SAEs which have boring structureless UMAPs or don’t exhibit feature splitting. 

 I can just communicate the weights of my SAE’s decoder matrix to you, and then you will know where all the feature vectors go, and then you get my richly structured activation space. But this is breaking the rules! If I understand something, I must be able to explain it to you in concepts I understand, and I do not understand what information is contained in the giant inscrutable decoder matrix.