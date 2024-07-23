# Research Topics From Others

[https://www.lesswrong.com/posts/KfkpgXdgRheSRWDy8/a-list-of-45-mech-interp-project-ideas-from-apollo-research](https://www.lesswrong.com/posts/KfkpgXdgRheSRWDy8/a-list-of-45-mech-interp-project-ideas-from-apollo-research)

**Foundational work on sparse dictionary learning for interpretability**

- **[Nix] Toy model of feature splitting**
    - There are at least two explanations for feature splitting I find plausible:
        - Activations exist in higher dimensional manifolds in feature space, feature splitting is a symptom of one higher dimensional mostly-continuous feature being chunked into discrete features at different resolutions.
        - There is a finite number of highly-related discrete features that activate on similar (but not identical) inputs and cause similar (but not identical) output actions. These can be summarized as a single feature with reasonable explained variance, but is better summarized as a collection of “split” features.
    - [I think toy models that make either of these hypotheses more concrete would be valuable. I’d probably start with the second one and find a setting that’s analogous to token-in-context features, and train a model to predict different (but highly correlated) bigrams depending on context.](https://chatgpt.com/c/7e444de6-813f-44b2-83a7-64971279b88e)
    - Could also consider a toy-model of superposition style setup. They tested features with correlated inputs but not correlated outputs.
    - [https://www.lesswrong.com/posts/KfkpgXdgRheSRWDy8/a-list-of-45-mech-interp-project-ideas-from-apollo-research?commentId=EkibeZomncsPxfYwu](https://www.lesswrong.com/posts/KfkpgXdgRheSRWDy8/a-list-of-45-mech-interp-project-ideas-from-apollo-research?commentId=EkibeZomncsPxfYwu)
        
        I predict that whether or not the SAE finds the splitting directions depends on details about how much non-sparsity is penalized and how wide the SAE is.  Given enough capacity, the SAE benefits (sparsity-wise) from replacing the (topology, math, physics) features with (topology-in-math, topology-in-physics), because split features activate more sparsely.  Conversely, if the sparsity penalty is strong enough and there is not enough capacity to split, the loss recovered from having a topology feature at all (on top of the math/physics feature) may not outweigh the cost in sparsity.
        
- **[Dan] Looking for opposing feature directions in SAEs**
    - SAEs are only capable of learning halfspaces (positive activations of some direction above some threshold). But if the ‘true’ underlying feature is a subspace (i.e. both a positive and negative direction), then SAEs will have to learn two, opposite-facing directions to represent this ‘true’ feature. In practice, we notice this happening when we train SAEs to sparsely represent dense, Gaussian point clouds when we use an L_p norm with p<1. Do SAEs learn opposite-facing pairs in language models?
- **[Lee] Mixture of Expert SAEs**
    
    • Feature splitting and feature geometry indicate that there is a hierarchical structure to feature-space. MOE-SAEs may be one way to leverage this. They may also have the benefit of letting us study the geometric structure of the features by studying the gate function of the MOE-SAE-encoder. (This suggests an additional question: Can we build SAEs with even more hierarchy? This may let us study feature geometry on an even more abstract level). 
    
- **[Lee] Identify canonical features that emerge in language models**
    - When investigating visual networks, we basically always find certain features. Edge features, for example, appear in both convolutional, transformer-based, and biological networks.
    - When we train SAEs in language models of different size, architecture, training dataset, etc., we might find features that appear again and again. What are these features?
    - And can we use this information to accelerate sparse dictionary learning? For instance, in vision models, we could present the model with inputs consisting only of edges in order to find the ‘edge detector’ direction. Can we do the same in language models?
    - Downscoped: Identify canonical features in early layers of language models
- **[Lee] Connecting SAE/transcoder features to polytopes**
    - The main downfall of the [polytope lens](https://www.lesswrong.com/posts/eDicGjD9yte6FLSie/interpreting-neural-networks-through-the-polytope-lens) was that it used clustering methods in order to group polytopes together. This means the components of the explanations they provided were not ‘composable’. We want to be able to break down polytopes into components that are composable.
    - Presumably, SAEs and transcoders also capture ‘directions’ that take similar pathways through the network. The same can be said for polytopes. What is the relationship between features identified using sparse dictionary learning and compositional polytope codes?
    - We could decompose the ‘polytope codes’ of various data points in a similar way to how we decompose activations. Various methods may be used here, including PCA, ICA, NMF, or SAEs on polytope codes. Note that, since polytope codes at layer L involve concatenating polytope codes of multiple (later) layers together, even PCA on the codes can yield an overcomplete ‘basis’ at layer L.
- **[Stefan] Relationship between Feature Splitting, Feature Completeness, and atomic vs. composite features**
    - Answer whether the specialized features we find in large SAEs “true features” (Anthropic), or whether they represent composites of multiple features. Details [here](https://www.lesswrong.com/posts/ZBjhp6zwfE8o8yfni/stefanhex-s-shortform?commentId=x9pDAquH5bxa9Kzdn).
    
    [https://www.lesswrong.com/posts/LajDyGyiyX8DNNsuF/interim-research-report-activation-plateaus-and-sensitive-1](https://www.lesswrong.com/posts/LajDyGyiyX8DNNsuF/interim-research-report-activation-plateaus-and-sensitive-1)
    • Are there different types of SAE features, [atomic and composite](https://www.lesswrong.com/posts/QoR8noAB3Mp2KBA4B/do-sparse-autoencoders-find-true-features) features? Can we get a handle on the total number of features?
    
- **[Lee] Is there structure in feature splitting?**
    - Suppose we have a trained SAE with N features. If we apply e.g. NMF or SAEs to these directions are there directions that explain the structure of the splitting? As in, suppose we have a feature for math and a feature for physics. And suppose these split into (among other things)
        - 'topology in a math context'
        - 'topology in a physics context'
        - 'high dimensions in a math context'
        - 'high dimensions in a physics context'
    - Is the topology-ifying direction the same for both features? Is the high-dimensionifying direction the same for both features? And if so, why did/didn't the original SAEs find these directions?
- **[Lucius] Understanding the geometry of SAE features**
    - Run PCA on the activations of trained SAEs. How many principal components are small enough to be ablated without hurting model performance much? The more components like this exist, the worse the SAE quality since many of the features are just linear combinations of each other. This makes the PCA spectrum of SAE activations a potential metric for SAE quality.
    - How do LLMs encode digit and number features? Can we guess how models count and perform arithmetic by looking at the geometry of digit embeddings with respect to each other? E.g., if models were performing modular addition with carryover digits to add numbers, we might expect to see the digits embedded in order along a circle, 0,1,2,3,4,5,6,7,8,9, much like the months of the year were found to be embedded in a circle in a recent [paper](https://arxiv.org/abs/2405.14860).
    - Does the feature geometry reflect subset/superset relationships? E.g., every bird is an animal, but not every animal is a bird. Every square is a rectangle, but not every rectangle is a square.
    - To what extent are SAE features embedded in multiple different subspaces, as opposed to one global space? According to sparse coding theory, one global space of size d can store more features than two subspaces of size d/2, but the latter configuration can have more features active at the same time. If there are subspaces, do they line up with semantic relationships? Do they correspond to circuits?

**Applied interpretability**

- **[Lee] Characterizing the geometry of low-level vision SAE features**
    - Features in the lower levels of biological visual systems, conv nets, or vision transformers, tend to have clear structure such as edges, color gradients, etc.
    - There is also an hypothesis that NNs compute not only using sparsely activating features, but also rely on the geometry of these features. Therefore characterizing this geometry in an analysable setting could help reveal insights about how geometry is used for computation. We should first characterize that geometry in an understandable setting, such as visual data.
    - One possible way to analyze the geometry is to identify characteristic features for a set of points on the hypersphere in a low level visual representation space (e.g. by finding the max activating dataset examples for certain SAE dict elements or for random directions in the 1st layer of a convnet/VIT. Then we could map those images/visualizations using a Fourier frequency transform to a space representing the various brightness/color frequencies. These would give us a map of low-level visual space in terms of objective, analyzable quantities instead of just ‘pictures’.
        - This has plausibly been done before in biological networks.
    - This characterization might let us study the geometry of the representation space quantitatively rather than relying on qualitative impressions of what the features are. It might also let us construct an ‘ideal’ low-level visual feature space from the quantitative description by finding what kind of representations the networks appear to be ‘trying’ to be learning. Speculatively, it might be possible to repeat this procedure in the next layer, but using the representational primitives identified in the first layer.

**Meta-research and philosophy**

- **[Lee] Write up reviews/short posts on the links between various concepts in comp neuro and mech interp and philosophy of science and mech interp**
    - E.g.
        - Representational geometry in brains and anns
        - Topological data analysis in brains and anns
        - Dynamical systems for analyzing structure in brains in anns
        - What is an explanation? A primer for mech interp practitioners on the philosophy of science of explanations
        - A history of the Human Genome project in the context of mech interp.
        - The philosophical history of mechanistic interpretability
- **[Lee] What is a feature? What terms should we really be using here? What assumptions do these concepts make? Where does it lead when we take these assumptions to their natural conclusions?**
- **[Lucius] Should we expect some or many of the ‘features’ in current neural networks to be [natural latents](https://www.lesswrong.com/posts/dWQWzGCSFj6GTZHz7/natural-latents-the-math)?**
    - If we should not expect them to be natural latents under the strict definition of that term, should we expect them to be natural latents under some relaxed definition?