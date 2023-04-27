# DIFFUSION MODELS ALREADY HAVE A SEMANTIC LATENT SPACE

Q: Why does each sample in the latent space have a representation in the semantic space?

The semantic latent space, named h-space, has the properties necessary for editing applications such as homogeneity, linearity, robustness and consistency across timesteps [1]. This allows for the same shift in the space to result in the same attribute change in all images, and linear changes in the space lead to linear changes in attributes [2].

To achieve this, an asymmetric reverse process (Asyrp) is used to discover the semantic latent space of a frozen diffusion model [3]. The sampling equation is modified to add the semantic latent space to the generative process, and a clip loss and regularization are used to render the attribute in the xedit 0, ϵ-space [4]. The h-space allows for the desired attribute change without degrading the quality of the resulting images and with almost identical changes throughout the timesteps [5].

<<<<
How is the mapping between latent space and semantic space constructed?

Asyrp proposes an asymmetric reverse process to construct a mapping between latent space and semantic space. Preechakul et al. (2022) introduces an additional input to the reverse diffusion process, a latent vector from an original image embedded by an extra encoder. This latent vector contains the semantics to condition the process.

<<<
What is the geometry of h-space?

In h-space, the distance between two points is determined by the amount of noise in the data points. [3] This noise can be manipulated by changing the parameters of the network at each sampling step [5], or by shifting the predicted noise [17]. The asymmetric reverse process [26] can also be used for manipulating x0 in h-space. [18]

<<<
The linearity of h-space was found by designing the sampling equation. This allows for the manipulation of x0 through shifting the noise ϵθ t

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
chatpdf:
εθt is a feature map at time t in the diffusion model that represents the image's semantic information. It is implemented as U-Net in all state-of-the-art diffusion models and is used to control the attributes of the resulting images during semantic latent editing with Asyrp.

The PDF explains that the sampling equation in Asyrp is designed to find h-space because it uses the bottleneck of the U-Net, which is implemented in all state-of-the-art diffusion models, to control εθt. The bottleneck, represented by ht, has smaller spatial resolutions and high-level semantics than εθt. By adding ∆ht to the original feature map ht, the sampling equation can manipulate the attributes of the resulting images while maintaining their quality.

<<<
However, it is important to note that the diffusion model itself is not necessarily a U-Net. The paper mentions that various architectures can be used for the diffusion model, but they all implement εθt as U-Net.

<<<
ε is a noise predictor in the diffusion model. Specifically, it represents the predicted random noise that is added to the image at each timestep of the diffusion process.

<<<
Q: What does random noise have to do with distances between samples? Does noise go from one sample to another?

Based on the information in the PDF, there does not appear to be a direct relationship between random noise and distances between samples. The random noise added to the image at each timestep of the diffusion process is used to model the uncertainty in the image's pixel values.
This noise is predicted by ε, which is implemented as U-Net in all state-of-the-art diffusion models.
Asyrp uses semantic latent editing to manipulate the attributes of this predicted random noise while preserving image quality.

Regarding your second question, it is important to note that each sample has its own predicted random noise ε, which is added to its corresponding image at each timestep of the diffusion process.

<<<
P and D are two components of the diffusion process used in the diffusion models. Specifically, P represents the probability distribution of pixel values at each timestep of the diffusion process, while D represents the learned Gaussian transitions between adjacent timesteps.

During training, the model learns to sample from P and D to generate a sequence of noise levels that are added to an initial image to produce a sequence of intermediate images. These intermediate images are then used to reconstruct the original image using an inversion process.

It is important to note that Asyrp modifies only P while preserving D in order to achieve semantic latent editing of images during inference.

<<<
Can non-euclidean spaces exhibit linearity?
Yes, non-Euclidean spaces can exhibit linearity in certain contexts. The term "non-Euclidean" simply means that the space does not satisfy all of the axioms or assumptions of Euclidean geometry, which includes assumptions such as the parallel postulate and the Pythagorean theorem.

However, the concept of linearity is more general than Euclidean geometry, and can be defined in a broader context. In linear algebra, for example, the concept of linearity refers to the properties of a linear transformation, such as preserving scalar multiplication and vector addition.

In this context, it is possible for a non-Euclidean space to exhibit linearity with respect to certain linear transformations. For example, a hyperbolic space, which is a type of non-Euclidean space with a negative curvature, can be studied using hyperbolic geometry and can exhibit linearity with respect to certain linear transformations.

Similarly, in the context of machine learning and deep learning, non-Euclidean spaces such as Riemannian manifolds and hyperbolic spaces can be used to model complex data spaces, and can exhibit linearity with respect to certain linear operators such as the gradient of a loss function.

In summary, while non-Euclidean spaces may not exhibit linearity in the same way that Euclidean spaces do, they can still exhibit linearity in certain contexts and with respect to certain transformations or operators.