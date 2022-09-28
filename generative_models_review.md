---
title: Review: Generative Models 
---
This section summarizes sections of [3 sections of links: VAE, GAN, topology] that are relevant to our discussion, for those unfamiliar with those topics. It is recommended to read those links to get a more detailed understanding. If one is already familiar with these topics, one can skip to ch2.1. 

**1.1: VAEs**

https://www.jeremyjordan.me/variational-autoencoders/
https://towardsdatascience.com/generating-images-with-autoencoders-77fd3a8dd368 

To compress an image, an autoencoder consists of two neural networks: <span style="color:purple">an encoder</span> and a decoder. The encoder compresses the image x into a latent code z in latent space Z, and the decoder uses latent code to reconstruct the image. Since the latent space has fewer dimensions than X, the encoder must decide what information to keep, and what to discard.

Instead of mapping each image to a single point in Z, the Variational AutoEncoder (VAE) maps image x onto a probability distribution <span style="color:indigo">P(z\|X)</span>, assigning a probability to every z to find the code z with the highest probability of matching with image x. Since the actual <span style="color:indigo">P(z\|X)</span> isn’t known, the <span style="color:purple">encoder Q(z\|X)</span>  approximates <span style="color:indigo">P(z\|X)</span>. Thus the latent space distribution Q(z) is inferred using the image space distribution Q(X).

![Figure 1.1: VAE](/images/figure1.1.png)

<span style="color:purple">Q(z\|X)</span> is represented by learning two vectors: a <span style="color:orange">mean vector</span> and a <span style="color:green">standard deviation vector</span>. To generate an <span style="color:red">image</span> with <span style="color:blue">similar features to ima</span><span style="color:teal">ges</span> that the VAE was trained on, <span style="color:red">a sample</span> that is close to the distributions of <span style="color:blue">similar ima</span><span style="color:teal">ges</span> is passed through the decoder.

**Continuous space and interpolation, vector arithmetic**

https://towardsdatascience.com/intuitively-understanding-variational-autoencoders-1bfe67eb5daf

There is an actual “territory” of latent space Z, and the autoencoder, like a cartographer, has to make a map Z’ of it. But if the autoencoder never ventured into certain regions (it never saw images in those regions of pixel space), it has trouble guessing what those regions look like on its map. In mathematical terms, its map of latent space would not be continuous. However, VAEs are able to make guesses about those regions because by using probability distributions, their maps of latent space are continuous.

[figure comparing plain map Z’ vs distribution map Q(Z) covering gaps.]hover
NOTE: on all plots of spaces: do not take this literally, this figure is just an analogy

Once the neural networks draws a map, calculations can be done on the map to infer new regions.
[explorer making a map- in both this section and section 0]
“Don’t confuse the map for the territory” is helpful advice when performing analogical reasoning about misuses of maps, such as overfitting or applying neural networks to data distributions it was not trained on (using wrong models).

[To do this, use linear algebra to define the new direction vector. We see how to do this in sec 2.1.]

**1.2: GANs**
https://medium.com/@Petuum/deep-generative-models-a-unified-statistical-view-2e9e45940250
GAN implicit b/c can only generate samples x from P(z) and cannot evaluate the likelihood of x
VAE sample from explicit generative distribution P(x | z), which can compute likelihood of x

GANs don't learn this probabilistic mapping, they just sample.
A GAN has a generator trained to output images, and a discriminator (a classifier) trained to distinguish generator images from real ones. The generator wants to discriminator to be inaccurate, while the discriminator wants to be accurate.
The generator in GAN takes a latent code z from latent space Z and produces an image in space X. Operation Z to X: final layer has p^2 neurons represented as 1D, and another layer reshapes it into p by p image
https://subscription.packtpub.com/book/big_data_and_business_intelligence/9781789136678/1/
ch01lvl1sec12/the-detailed-architecture-of-a-gan

[arithmetic in GANspace]

---
Switches around during training
[side-by-side figure comparing GANs and VAEs, w/ spaces in b/w layers]

**1.3**
[discriminator/encoder, generator/decoder]
We will first explain the discriminator in terms of transformations, using a simple neural network as a basic classifier.
[Olah manifolds, see the first animation in the section “Continuous Visualization of Layers”] 
Start w/ equation of neuron: 3 steps. Olah’s animation: list each step. First step:
Recall from (3B1Br) that a matrix multiplication such as XW is a transformation W on X, warping the space by projecting the vectors defined by the basis vectors of X’s original space onto the basis vectors of a new space. 
In the context of machine learning, these vectors are the observations (the data points). Using XW, the data points are transformed from the input space that uses features as basis vectors to another space; this transformation preserves the relational differences (variance) between each data point in the input space. This new space may reveal relations between these vectors from a new perspective. In the next layer, the weight matrix W(2) transforms to yet another space. <span style="color:silver">Each successive layer has its own new space that uses the neurons of that layer to form its basis.</span> 

Since the neurons in each hidden layer are activations, the space that XW transforms the input space into has been referred to as the “activation space”, which contains all possible combinations of neuron activations. <span style="color:silver">Its basis vectors are individual neuron activations as the standard basis with each neuron being a unit vector, and a linear combination of neuron activations is a vector in activation space.</span>

It’s projecting onto W, then shifting by b, then applying g() will squish the space applied pointwise, so if you break it down, it’s simply just scaling at each step using Hadamand operations, which unlike affine operations such as matrix multiplication, do not have nice geometric interpretations. 
[figure] Eg) Say for a single observation x with dimensions 1 by d, XW outputs via dot product the vector [1,2,3] representing a single data point with activations for 3 neurons in that layer. Sigmoid is 1/(1+e^-x), so we first apply -1[1,2,3], then apply e^[1,2,3] element-wise, which is the Hadamand power of [e,e,e,] to [1,2,3]. Then vector addition, then Hadamand division. 
FOOTNOTES: Define “affine”. 
FOOTNOTE: An activation space may also be called a “latent space” because each hidden layer’s activation values on the data points reveal hidden (latent) relationships in the data that may not be seen in the input space. 
It makes a judgment for each observation (color labeled class in each point in output on figure) 

---
Define manifold. [Papers] treat the latent space as a Riemannian Manifold
The data set itself is a manifold embedded within the manifold that is the input space, and the data set manifold is transformed into another manifold in the activation space by warping the input space into the space of how the neurons interpret the data. 
The layers of a neural network transform high dimensional representations into representations that are “easier to interpret”- in other words, they allow the neural network to partition the data in a way that better optimizes an objective function. In (3B1Br video X timestamp), each transformation “rotates” the data onto new basis vectors; this is the same thing as projection. When a dimension is removed, it projects it onto lower dimensional space. A neural network can be thought of as a function that is a composition of transformations.
[papers discussing visualizing transformations of manifold,

---
Manifold gaps, Separability, discretization in latent space. 
latent space contains gaps, and we do not know what characters in these spaces may look like 
However, in this new perspective, if dimensions are reduced, may lose interpretability information (cite 3b1br)
[cite papers about manifolds]

---
Conclusion
https://towardsdatascience.com/understanding-latent-space-in-machine-learning-de5a7c687d8d
https://hackernoon.com/latent-space-visualization-deep-learning-bits-2-bd09a46920df
Disentangle. 
neuron approx learned fn by piecewise. Local to global
Now that we understand NN as a type of transformation algorithm meant to preserve relationships, we will analyze the latent space and also how it is transformed into hidden space.

<!---
<span style="color:silver">
</span>
-->