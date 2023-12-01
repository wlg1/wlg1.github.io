# Toy Models of Superposition

[https://transformer-circuits.pub/2022/toy_model/index.html](https://transformer-circuits.pub/2022/toy_model/index.html)

p7, The Superposition Hypothesis: Superposition leads to polysemanticity

p9: Demontrating superposition:

![Untitled](Toy%20Models%20of%20Superposition%209538794a63a541ebbd6aa19b19195839/Untitled.png)

W from high to lower dim space is like bottleneck?

**************************Sec 2- Basic results**************************

Measure the sum of a row of W^T W to find the direction of a feature in relation to other features. This is 0 (black, orthogonal to all) if no interference, and 1 (yellow). The more interference, the more superposition

1 - S =1 means dense

1 - S = 0.001 means sparse

Black means less superposition, yellow means more

More superposition means more interference, and LESS orthogonal features

Too much interference can prevent superposition- as feature are not represented right? But you can still have superposition if interference is not severe enough to make features too entangled for predictions?

Interference is “pain”- increases the loss function, so self org features tend to avoid it if they can? (don’t put this in formal work as seems like it’s anthropm)

L ~= benefit + interference : (trade-off)

**Sec 2- Mathematical**

************************Phase Change************************

**Geometry**

W is n by m

Frobenius norm measures number of features a model has learned. it’s not per “i”, but the whole W

D*: dims per feature

line plot: sparsity vs D*. Since m is fixed, D* decreases as Frobenius grows bigger than m, meaning the model learns more features than hidden dimensions (neurons). These features are presumably sparse, meaning we can pack them together as say antipodal pairs, since one often activates without needing the other.

“Sticky” D* for a range of sparsity means stays and “prefers” that level of D*. The 1/2 is an antipodal pair, which is effective.

The log scale means the graph appears more “linear”; if the x-axis was linear, the graph would appear big value at start, and very low values soon later into a tail?

Dimensionality D equation: the length of a vector is how much of the total length?

This plots is similar to the previous one, but overlay with scatter plots for each model (trained on data with different feature sparsity levels)

The geometries are the “individual communities” within the graph. A graph has a mix of community types- some are pairs, others are triangles, etc. Show a figure of a bigger geometric structure- 2D vs 3D (denominator).

As seen in the ‘aside low rank matrices’, the edges are the covariances between features.

Non-uniform:

some features more important or more frequent than others (give an example to a real world analogy, “As an analogy”)

Correlated features prefer to be orthogonal because they don’t want to be mixed up (too similar; needs something to distinguish). This is in contrast to believing they share something. PERHAPS they have a lot of interference in some directions (as they must to be similar; high dot prod means high interference) but low interference in distinct directions (the “branches” that help distinguish them in a decision tree?)

Actually- correlated are orthogonal (90 degrees) while anticorrelated are in opposite (180)

**anticorrelated: python vs romance (this is similar unless more words distinguish the info; higher entropy means more words)**

[https://chat.openai.com/c/f470d8a0-7a3d-41e2-a92a-22e9a5c3bb07](https://chat.openai.com/c/f470d8a0-7a3d-41e2-a92a-22e9a5c3bb07)

<<<

Sec 9:

For example, if one is concernedabout language models exhibiting manipulative behavior, one might ask if an input has asignificant cosine similarity to the representations of other examples of deceptive behavior. Unfortunately, superposition means that cosine similarity has the potential to be misleading, since unrelated features start to be embedded with positive dot products to each other.

---

[https://www.youtube.com/watch?v=R3nbXgMnVqQ&ab_channel=NeelNanda](https://www.youtube.com/watch?v=R3nbXgMnVqQ&ab_channel=NeelNanda)

8m50s: model likes to actv on ‘ug’ in refugees

10m20s: polysemanticity: When 1 neuron that represents many things

11m15s: Superposition: When model has # features > # neurons (dims), it learns to compress those features down into those dims

**but you can have like many many directions that are almost but not quite orthogonal** 

![Untitled](Toy%20Models%20of%20Superposition%209538794a63a541ebbd6aa19b19195839/Untitled%201.png)

13m13s: Neuron 1 gets all of feature 1. It would want feature 2 to be orthogonal to feature 1, aligning it with N2, else the projection of feature 2 down to feature 1 would have interference (dot product ≠ 0)

But when 3 features and 2 N, have multi-way interference

![Untitled](Toy%20Models%20of%20Superposition%209538794a63a541ebbd6aa19b19195839/Untitled%202.png)

So model has tradeoff of having more features (and more intereference) VS less interference

15m: if a feature is ocean, it may interfere and also give info about fur and car, which is noise. **********************************************************************So how can things be organized to have things be as similar as possible while minimizing noise. Esp in fast paced changing environment, where meaning always changes and it’s hard to keep up?**********************************************************************

20m: relu cleans up noise in autoencoder (which retrieves original input after compressing)

W embedding is lookup table from 5D rows to 2D cols

24m20s: importance is weight on loss fn. how much does it lower it?

the more important it is, the more orthogonal they should be to minimize interference?

28m15s: sparsity is how many features present at any “given time” (I assume this means represented in a layer by neurons)

38m: the latent space is the “kernel” in between emb and unemb of autoencoder? so this is where the low dim features are seen being emb into shapes relative to each other. Eg) 5D to 2D kernel bottleneck space

41m: embed in and project are same operations (write), but embed back out and project are diff (read)

47m: nonlinear actv fn magnifies interference

2h2m25s : try to measure how much a model gives a feature its own dimension VS sharing dims with other features

antipodal pair of features: in opposite directions. each feature has 1/2 of the total projection onto the direction

---

- Relation between linear probes and tangent spaces for neural network interpretability of latent space?
    
    "Linear probes" and "tangent spaces" are two concepts from very different fields -- machine learning and differential geometry, respectively -- but their relation can be seen in the context of interpreting the latent space of neural networks.
    
    A latent space refers to the high-dimensional space of variables (or features) that a model (e.g., a neural network) learns to represent the data. This space often carries meaningful structures about the data, but can be hard to understand due to its high dimensionality and lack of interpretability.
    
    1. **Linear Probes**: This term comes from the machine learning community, where it refers to simple linear models (e.g., linear regression, linear classifiers) that are trained on the features extracted by a neural network to understand the information that the network has learned to capture. The idea is that if a simple linear model can predict a certain property from the network's features, then the network must have learned to represent that property in a somewhat linearly decodable manner. This technique is used to assess what kind of information is captured by a neural network's latent space.
    2. **Tangent Spaces**: This term comes from the field of differential geometry. In the context of latent spaces, the concept of a tangent space can be used to understand the local structure of the latent space around a particular data point. Each point in the latent space has an associated tangent space, which can be thought of as the space of all possible small changes (or "directions") to that point. If the latent space captures meaningful structure, then moving along different directions in the tangent space should correspond to meaningful transformations of the data.
    
    The connection between linear probes and tangent spaces comes from the idea of understanding and interpreting the latent space. Linear probes can be used to check what global properties are captured in the latent space, while tangent spaces can be used to study local structure and transformations.
    
    In practice, you might use a combination of these techniques: for example, you might use linear probes to understand what general features your network has learned to represent, and then use the concept of tangent spaces to understand how these features can be slightly altered (e.g., what happens if we move slightly along the "size" direction, or the "color" direction, etc.).
    
    In the context of neural network interpretability, it's important to remember that these are just tools and they can provide insights but not necessarily definitive answers. They are part of a broader toolbox of techniques for making sense of the complicated functions that neural networks learn to represent.
    

The tradeoff between features (views eval cost) and interference (maint cost) is about what building blocks to choose to represent the most things. perhaps a model can be trained to select features.

superficial vs semantic similarity of superposition (cat fur, vs cat car)