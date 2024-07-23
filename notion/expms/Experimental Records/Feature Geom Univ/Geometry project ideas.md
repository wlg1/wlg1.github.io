# Geometry project ideas

**MAIN IDEA:** See how changing feature combinations changes the geometry + topology properties of activation in latent space (across models)

Brainstorming

[Motivation](Geometry%20project%20ideas%20eb549c97d93548fc97e75e83fcba87a8/Motivation%209352aa5ce54f4f1ba3fd3fa17d80d5ff.md)

[Main goal and contributions](Geometry%20project%20ideas%20eb549c97d93548fc97e75e83fcba87a8/Main%20goal%20and%20contributions%204b749c6c252b47b8ba383ddfa26e63d9.md)

[Steps towards goal](Geometry%20project%20ideas%20eb549c97d93548fc97e75e83fcba87a8/Steps%20towards%20goal%2037a8a61bbae8449c9565dcb80b437a3e.md)

[Feature Splitting Across Models](Geometry%20project%20ideas%20eb549c97d93548fc97e75e83fcba87a8/Feature%20Splitting%20Across%20Models%200752a5693dac4a1daa0ff3ffabec13ff.md)

[Feature Convergence Across Models](Geometry%20project%20ideas%20eb549c97d93548fc97e75e83fcba87a8/Feature%20Convergence%20Across%20Models%20b1d1245092004d118005b4a43d76ce77.md)

[How to measure feature similarity](Geometry%20project%20ideas%20eb549c97d93548fc97e75e83fcba87a8/How%20to%20measure%20feature%20similarity%20e0ceaa1c575044078ccd6a4d4ec71c04.md)

[How to visualize](Geometry%20project%20ideas%20eb549c97d93548fc97e75e83fcba87a8/How%20to%20visualize%203dcf24bc83b34379b45a31723a7b5a83.md)

[Mapping higher-order relations](Geometry%20project%20ideas%20eb549c97d93548fc97e75e83fcba87a8/Mapping%20higher-order%20relations%20805467e55af54ef0ad38a5087ba417e1.md)

[Steering feature geometry](Geometry%20project%20ideas%20eb549c97d93548fc97e75e83fcba87a8/Steering%20feature%20geometry%20f08a443855af4fafafea3adb0338ba1e.md)

[Feature matching algorithm](Geometry%20project%20ideas%20eb549c97d93548fc97e75e83fcba87a8/Feature%20matching%20algorithm%20c3c0c07ec7ab45e184de364123ab0361.md)

[Taxonomy](Geometry%20project%20ideas%20eb549c97d93548fc97e75e83fcba87a8/Taxonomy%205d6b2be6988247abad1e73e285132a9c.md)

[AlgTop](Geometry%20project%20ideas%20eb549c97d93548fc97e75e83fcba87a8/AlgTop%2060c0b27e80d34577bd14694bb9fe2e86.md)

[Steering Vectors Across Models](Geometry%20project%20ideas%20eb549c97d93548fc97e75e83fcba87a8/Steering%20Vectors%20Across%20Models%204dda721ed63a48c18a52b793de896ef4.md)

[Feature selection](Geometry%20project%20ideas%20eb549c97d93548fc97e75e83fcba87a8/Feature%20selection%20bdef859369e14f349f77f4a2feb1ca9a.md)

[Layer alignment](Geometry%20project%20ideas%20eb549c97d93548fc97e75e83fcba87a8/Layer%20alignment%20c9f32f1962fd425f89beb25f7227096a.md)

[Relations](Geometry%20project%20ideas%20eb549c97d93548fc97e75e83fcba87a8/Relations%20e02f0430d5e84a4ab6e02de75cfcb824.md)

[Manifold](Geometry%20project%20ideas%20eb549c97d93548fc97e75e83fcba87a8/Manifold%20c5dce05e9a05463aafa8e98a2e36a2cc.md)

[Align SAEs across models](Geometry%20project%20ideas%20eb549c97d93548fc97e75e83fcba87a8/Align%20SAEs%20across%20models%20070f28a71c8640a482e72a49850326f5.md)

[Similarity expms](Geometry%20project%20ideas%20eb549c97d93548fc97e75e83fcba87a8/Similarity%20expms%206de7a18830da4686a5583cca7cc724bc.md)

[Mapper](Geometry%20project%20ideas%20eb549c97d93548fc97e75e83fcba87a8/Mapper%2026cf8b0bbf3c43cdaf77d97b97416373.md)

Find relational structure and clusters in space. Then check how similar saes are and if can map structures to one another. Then show similar steer vecs in similar models steer similar features. 

If saes have similarity score high, this shows universality as saes get bigger, showing even feature splitting is universal

Many current mech interp techniques suffer from reviewers saying these discoveries are not universal. Now we have a way of measuring universality; if enough models have this structure, we can construct a distribution of how frequent a set of feature relations are in a set of model.

Feature relations are impt for steering direction. They say what concepts are close to one another. We better understand how a model organizes concepts. This is like discovering DNA, and later studies can figure out how to use this space of concepts for more efficient editing. For example, this space can use model A as a map to locate features in model B. 

The more relation structure equivalent, see Forbes, the higher similarity. Prove this and ask others to prove. Use: if higher property, then similar outputs? Or can transfer as map?

End to end feature unverantinty

Is feature splitting down in same way across models

Do saes transfer across models?

If two llms same basis 

Use multiple metrics. Mnn for neighbors and clusters, gram matrices for global overall 

Steer then compare gram matrices of later layers after steering

Ideas

- an sae to learn an sae’s relations bewteen features. turn those relations into features.

Things to look for:

- How does changing one feature change another feature’s similarity to others in activation space?
- relative distance/other metric of features across models
    - same relative change after change in input/other features
    - this distance is the ‘relative correlations’ between features within model AND across models
    - correlation of polytopes across models
    - this shows two features across models have correlated activations for the same inputs. can we extend this to multiple models?
        
        ![Untitled](Geometry%20project%20ideas%20eb549c97d93548fc97e75e83fcba87a8/Untitled.png)
        
    - do sae models converge (similarity metric) for multiple LLMs as they get bigger? similar to platonic representation hypothesis
        
        [similar features have small angles between their dictionary vectors.](https://transformer-circuits.pub/2023/monosemantic-features#phenomenology-feature-splitting)
        
        We conjecture that there is some idealized set of features that dictionary learning would return if we provided it with an unlimited dictionary size.
        
- Does feature ablation cause change in measured properties?
- Changes in clustering
- Changes in topological invariants (eg. simplices disappear if remove part of input or after steer)
    - this likely wouldn’t have yield anything with neurons, but likely will find structure with features
        - it was also hard to do with just CNN neurons. so not easy with vision
        - we also couldn’t get many sae features for multiple models before due to training. but with saelens across models, we now can.
        - now, we also have the help of geom researchers to ensure this work is sound
    - the ‘same’ simplex can be mapped across models
- Like nonlinear features, can we find patterns in arrangement?
- log-likelihood ratio: Measure probability of OTHER feature B actv given feature A activating. P(FB | FA) vs P(FB). This is log diff when taking log of ratio
    - we use this as it takes distribution of feature activations into account, not just mean of before vs after F_A
    - chatgpt is good for double checking if right way to measure this
- how shared downstream features interact in geometric space

towards and scaling monosemanticity I'm guessing the umap plots are feature weights of a layer, not activations? Would it make sense to plot activations for an input (type)?

Neuronpedia wouldn't explain this. You're talking about activation Atlas which I've never seen done for language models. I highly recommend reading that paper. I'd be fairly excited about comparing a umap over activations to a umap over features.

One project you could do is try to find a clustering technique that can run iteratively on batches with huge numbers of clusters and using this on activations. If you use soft clusters then this could be an interesting thing to compare to SAEs

questions

- how is circuit represented in latent space? as multiple activating features in each layer of space? should we transform this to be a point in some other space?
    - [ask chatgpt](https://chatgpt.com/c/2b6d8700-45cc-4a78-98f4-a3366e02687f)
    - is there a space where we can represent the entire circuit as a point, such as in input space or unembedding space?
        
        Yes, it is possible to represent an entire circuit as a point in various types of spaces. Here are some spaces where this can be achieved:
        
        1. **Input Space**:
            - In the input space, each point corresponds to a raw input. For circuits, this could be a representation of the circuit itself, such as a vector of parameters, node values, or a flattened version of the circuit structure.
            - For example, if the circuit is represented by a set of features or characteristics (e.g., resistance values, capacitance, connections), these can be combined into a single vector. Each unique circuit configuration would be a different point in this high-dimensional space.
        2. **Latent Space**:
            - In the latent space of a neural network, a circuit can be represented by the activations at a particular layer or a combination of layers.
            - Techniques like autoencoders can compress the high-dimensional input into a lower-dimensional latent space. Each point in this latent space represents a unique circuit.
        3. **Unembedding Space**:
            - The unembedding space, often related to the output layer of a neural network, is where the network’s final activations are transformed back into the original input space or a target space.
            - In the context of language models, for instance, the unembedding space is where the final hidden states are projected back to the vocabulary space. For circuits, a similar concept could apply where the network’s representation of the circuit is mapped back to a meaningful space (e.g., a set of output characteristics).
        
        ### Detailed Example of Transforming to a Point in Latent Space
        
        ### Using an Autoencoder
        
        An autoencoder is a type of neural network designed to learn efficient codings of input data. It consists of an encoder that compresses the input into a latent space and a decoder that reconstructs the input from the latent space.
        
        ```python
        import torch
        import torch.nn as nn
        import numpy as np
        import matplotlib.pyplot as plt
        from sklearn.decomposition import PCA
        
        # Define the autoencoder
        class Autoencoder(nn.Module):
            def __init__(self, input_dim, latent_dim):
                super(Autoencoder, self).__init__()
                self.encoder = nn.Sequential(
                    nn.Linear(input_dim, 128),
                    nn.ReLU(),
                    nn.Linear(128, latent_dim),
                    nn.ReLU()
                )
                self.decoder = nn.Sequential(
                    nn.Linear(latent_dim, 128),
                    nn.ReLU(),
                    nn.Linear(128, input_dim),
                    nn.Sigmoid()
                )
        
            def forward(self, x):
                latent = self.encoder(x)
                reconstructed = self.decoder(latent)
                return latent, reconstructed
        
        # Assuming `data` is a tensor representing your circuits
        input_dim = data.shape[1]
        latent_dim = 2  # For visualization, typically a small number
        
        # Instantiate and train the autoencoder
        model = Autoencoder(input_dim, latent_dim)
        criterion = nn.MSELoss()
        optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
        
        # Training loop
        num_epochs = 100
        for epoch in range(num_epochs):
            optimizer.zero_grad()
            latent, reconstructed = model(data)
            loss = criterion(reconstructed, data)
            loss.backward()
            optimizer.step()
        
        # Get the latent representations
        with torch.no_grad():
            latent_representations, _ = model(data)
        
        # Convert to numpy for visualization
        latent_representations = latent_representations.numpy()
        
        # Visualization
        plt.scatter(latent_representations[:, 0], latent_representations[:, 1])
        plt.title('Circuit Representation in Latent Space')
        plt.xlabel('Latent Dimension 1')
        plt.ylabel('Latent Dimension 2')
        plt.show()
        
        ```
        
        ### Using Embedding Techniques
        
        Embedding techniques like word2vec for text or graph embeddings for circuit structures can also be used to represent circuits as points in a lower-dimensional space.
        
        ```python
        from sklearn.decomposition import PCA
        import matplotlib.pyplot as plt
        
        # Assuming `embeddings` is a matrix of circuit embeddings
        pca = PCA(n_components=2)
        reduced_embeddings = pca.fit_transform(embeddings)
        
        # Visualization
        plt.scatter(reduced_embeddings[:, 0], reduced_embeddings[:, 1])
        plt.title('Circuit Representation in Embedding Space')
        plt.xlabel('Principal Component 1')
        plt.ylabel('Principal Component 2')
        plt.show()
        
        ```
        
        ### Summary
        
        - **Input Space**: Direct representation of the circuit's features.
        - **Latent Space**: Compressing the circuit data using techniques like autoencoders.
        - **Unembedding Space**: Mapping the network’s final activations back to a meaningful space.
        
        Each approach has its own use cases and benefits, depending on the specific application and the nature of the circuit data.
        
    

---

sources

[https://www.alignmentforum.org/posts/MFBTjb2qf3ziWmzz6/sae-feature-geometry-is-outside-the-superposition-hypothesis](https://www.alignmentforum.org/posts/MFBTjb2qf3ziWmzz6/sae-feature-geometry-is-outside-the-superposition-hypothesis)

- hierarchical feature splitting
    
     The closest thing to an existing concept that supplements superposition is the idea introduced by [Anthropic](https://transformer-circuits.pub/2023/monosemantic-features) that features can be placed on a hierarchical tree: the tree can be built from looking at dictionaries of different sizes, relating parent and children nodes via feature splitting
    

[https://transformer-circuits.pub/2023/monosemantic-features#phenomenology-feature-splitting](https://transformer-circuits.pub/2023/monosemantic-features#phenomenology-feature-splitting)

a 2-D UMAP on the combined set of feature directions (weights)

the feature splitting shows features get more specific within each gray cluster as the sae gets larger

[https://transformer-circuits.pub/2023/monosemantic-features#phenomenology-universality](https://transformer-circuits.pub/2023/monosemantic-features#phenomenology-universality)

[https://transformer-circuits.pub/2023/monosemantic-features#discussion-superposition](https://transformer-circuits.pub/2023/monosemantic-features#discussion-superposition)

![Untitled](Geometry%20project%20ideas%20eb549c97d93548fc97e75e83fcba87a8/Untitled%201.png)

One explanation for this (considered briefly by Toy Models) is that the features may have correlated activations – firing together. Another – which we suspect to be more central – is that the features produce *similar actions*. The feature which fires on single digits in base64 predicts approximately the same set of tokens as the feature firing on other characters in base64, with the exception of other digits; these similar downstream effects manifest as geometrically close feature directions.

Moreover, it isn't clear that features need to be one-dimensional objects (encoding only some intensity). In principle, it seems possible to have higher-dimensional "feature manifolds" (see earlier discussion [here](https://transformer-circuits.pub/2023/may-update/index.html#feature-manifolds)).
[https://transformer-circuits.pub/2023/may-update/index.html#feature-manifolds](https://transformer-circuits.pub/2023/may-update/index.html#feature-manifolds)

[https://distill.pub/2020/circuits/equivariance/](https://distill.pub/2020/circuits/equivariance/)