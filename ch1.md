To compress an image, an autoencoder consists of two neural networks: <span style="color:purple">an encoder</span> and a decoder. The encoder compresses the image x into a latent code z in latent space Z, and the decoder uses latent code to reconstruct the image. Since the latent space has fewer dimensions than X, the encoder must decide what information to keep, and what to discard.

Instead of mapping each image to a single point in Z, the Variational AutoEncoder (VAE) maps image x onto a probability distribution <span style="color:indigo">P(z\|X)</span>, assigning a probability to every z to find the code z with the highest probability of matching with image x. Since the actual <span style="color:indigo">P(z\|X)</span> isn’t known, the <span style="color:purple">encoder Q(z\|X)</span>  approximates <span style="color:indigo">P(z\|X)</span>. Thus the latent space distribution Q(z) is inferred using the image space distribution Q(X).

![Figure 1.1: VAE](/images/figure1.1.png)

<span style="color:purple">Q(z\|X)</span> is represented by learning two vectors: a <span style="color:orange">mean vector</span> and a <span style="color:green">standard deviation vector</span>. To generate an <span style="color:red">image</span> with <span style="color:blue">similar features to ima</span><span style="color:teal">ges</span> that the VAE was trained on, <span style="color:red">a sample</span> that is close to the distributions of <span style="color:blue">similar ima</span><span style="color:teal">ges</span> is passed through the decoder.

<!---
<span style="color:red">
</span>
-->