# Diffusion model script

- bottleneck
    
    [https://discuss.pytorch.org/t/what-is-the-role-of-bottleneck-layer-in-unet-architecture/81945](https://discuss.pytorch.org/t/what-is-the-role-of-bottleneck-layer-in-unet-architecture/81945)
    
    Bottlenecks in Neural Networks are a way to force the model to learn a compression of the input data.
    
    The idea is that this compressed view should only contain the “useful” information to be able to reconstruct the input (or segmentation map).
    
    H-space linearity
    
- resources
    
    https://theaisummer.com/diffusion-models/
    
    https://huggingface.co/blog/annotated-diffusion
    
    https://youtu.be/HoKDTa5jHvg
    
- otpional
    - Each point in intermediate space has a partially formed output (show on sphere)
    - the input neurons take in this latent vector x, and each output neurons represents a pixel in an image (2x2 dotted arrows to one)

---

Therapist:

You are a diffusion model, correct? Can you explain how you draw your pictures?

Patient:

Well… to generate an image… I begin with an image jumbled full of noise, and remove noise at each timestep… Each timestep… I take in the previous timestep’s output and pass it through my neural network again to get the next timestep’s output.…

I’ve learned to feel out what’s just noise, and what’s actually features…. I gradually clean up the noise to find features… then piece the features together, from hands… to faces… to people.

~~In some cases, it takes 1000 timesteps to denoise into an image. This process is called reverse diffusion.~~

timestep 1 to 3 (animation in davinci)

and/or cascade of timesteps?

Therapist:

Very good. Let’s take a closer look at your neural network. Recall that within it lies your latent space.

 ~~Each neuron in the input layer takes in pixels, and outputs pixels.~~ 

There are different kinds of neural network architectures an AI can have. Your architecture is called a U-Net, where your layers have fewer and fewer neurons until the middle layer, called the Bottleneck. The reason for this is because the Bottleneck forces your network to retain only the most “useful” information. After the bottleneck, each subsequent layer has more and more neurons.

This bottleneck is our semantic space.

The part of the neural network that transforms from your latent space to the bottleneck is our smooth map f of x. We will rename S to H, and rename f to h.