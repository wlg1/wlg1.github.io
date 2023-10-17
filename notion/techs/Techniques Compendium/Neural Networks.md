# Neural Networks

### Parameter Optimization

[Reduce number of parameters](Neural%20Networks%20bd4d93fa2afb487fa02f2f2e877659ad/Reduce%20number%20of%20parameters%20f228b55424894f9a8bf60bc5fbc66ef9.md) 

### Overfitting

[Clamping](Neural%20Networks%20bd4d93fa2afb487fa02f2f2e877659ad/Clamping%202e2f6208c50744b29c54b8b6edb64518.md)

---

### Sequences

[How to take in a sequence of inputs?](Neural%20Networks%20bd4d93fa2afb487fa02f2f2e877659ad/How%20to%20take%20in%20a%20sequence%20of%20inputs%204a1faf2457e545dd913dcf7fe1ed95d5.md) 

[Long sequences in RNNs lead to vanishing gradients](Neural%20Networks%20bd4d93fa2afb487fa02f2f2e877659ad/Long%20sequences%20in%20RNNs%20lead%20to%20vanishing%20gradients%20c2827729a1894426a6e62722b75add4f.md) 

[RNNs and LSTMs are slow to train](Neural%20Networks%20bd4d93fa2afb487fa02f2f2e877659ad/RNNs%20and%20LSTMs%20are%20slow%20to%20train%20f86c708767d74456b35c1f0c61519934.md) 

[How to choose the best prediction?](Neural%20Networks%20bd4d93fa2afb487fa02f2f2e877659ad/How%20to%20choose%20the%20best%20prediction%20091de1026e0246de8212161eb669cdc5.md)

---

### Probabilities

[How to turn logits to probabilities?](Neural%20Networks%20bd4d93fa2afb487fa02f2f2e877659ad/How%20to%20turn%20logits%20to%20probabilities%206217f1d4c71642ab92a717657135b2a8.md)

[Evaluate the performance of a machine learning model that predicts probabilities](Neural%20Networks%20bd4d93fa2afb487fa02f2f2e877659ad/Evaluate%20the%20performance%20of%20a%20machine%20learning%20mod%20d1f088d2b2a8498f84524b8b97562452.md) 

---

### Generative Models

- ISSUE: *dimension of the image stays the same* is an issue when generating high-quality images due to limited GPU memory
    
    DESC: if the image dimension is too large, it may exceed the available memory (?)
    
    SOLN: Use a variational autoencoder
    
    - WHY:
        1. Latent Space Dimension: VAEs learn a low-dimensional latent space representation of the input images. By reducing the dimensionality of the latent space, VAEs effectively compress the information required to generate images. This compression allows for efficient storage and manipulation of the latent representations, reducing the memory footprint.
        2. Generative Process: VAEs define a generative process that involves sampling latent variables from a prior distribution and decoding them into images. During the training process, VAEs learn to encode input images into meaningful latent representations and decode those representations back into reconstructed images. Since the dimension of the latent space is typically much smaller than the image dimension, VAEs enable generation from a compact representation, reducing memory requirements.
    
    CITE: [https://learnopencv.com/image-generation-using-diffusion-models/#What-Is-Diffusion](https://learnopencv.com/image-generation-using-diffusion-models/#What-Is-Diffusion)?