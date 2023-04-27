# Study ‘Erasing Concepts from Diffusion Models’ code for ideas

[https://erasing.baulab.info/](https://erasing.baulab.info/)

We query the frozen pre-trained model to predict the noise for a given prompt, then we train the edited model to guide it in the opposite direction using the ideas of classifier-free guidance at training time rather than inference.

![Untitled](Study%20%E2%80%98Erasing%20Concepts%20from%20Diffusion%20Models%E2%80%99%20cod%20ed15e0fe8e884bde91ea08128200e1ac/Untitled.png)

Cross attention modules act as a gateway for text conditioning in the image generation process. Naturally, these attention heads activate when a certain set of tokens are present in the text prompt. In contrast, self attentions activate irrrespective of text conditioning, since they attend to the visual aspects a concept.

How were cross attn found?

Inspired by this observation, we propose ESD-x, applying the erasing method to only fine tuning cross attention parameters while erasing a concept. That has a very narrow effect on the output distribution, focusing changes on conditions when the concept is explicitly mentioned in the prompt. Such finer effects are desirable in case of artistic style erasure, where some artists may wish to have their styles be preserved while others erased. We also study ESD-u, which is fine tuning all the unconditional layers (all layers except cross-attentions), which creates a generalised erasure of a concept that does not depend on the presence of specific words in the prompt; this is useful when removing NSFW output in a way that includes situations where NSFW terms are not used in the prompt.

1.

[https://huggingface.co/spaces/baulab/Erasing-Concepts-In-Diffusion/blob/main/app.py](https://huggingface.co/spaces/baulab/Erasing-Concepts-In-Diffusion/blob/main/app.py)

2.

[https://huggingface.co/spaces/baulab/Erasing-Concepts-In-Diffusion/blob/main/train.py](https://huggingface.co/spaces/baulab/Erasing-Concepts-In-Diffusion/blob/main/train.py)

It computes the loss by subtracting neutral latents and negative guidance (${-\eta}$, a float) times the difference between the positive ${\epsilon_\theta}(x, c, t)$ and neutral latents ${\epsilon_\theta}(x, t)$, then passing the result [all from frozen SD] and negative latents (from fine tune ESD) to the loss criteria.

- What is the latent tensor? How is it calculated?
    
    The latent tensor is a tensor that represents a point in the latent space of the generative model. In the case of the code you provided, the latent tensor is a tensor of shape `(batch_size, latent_size, image_size, image_size)` where `batch_size` is the number of images being generated, `latent_size` is the size of the latent space, and `image_size` is the size of the generated image.
    
    The latent tensor is typically initialized randomly from a normal distribution, with mean 0 and standard deviation 1. In the case of the `train()` function you provided, the initial latent tensor is generated using the `get_initial_latents()` method of the `StableDiffuser` class, which generates a tensor of the appropriate shape and size, initialized with random values. The latent tensor is then modified during the diffusion process using the diffusion equation, which is learned by the generative model. The final latent tensor represents a point in the latent space that corresponds to the generated image.
    
- latents_steps
    
    The **`diffusion()`** method returns two tensors:
    
    - **`latents_steps`**: a list of intermediate latent tensors obtained during the diffusion process. Each tensor has the same shape as **`latents`**.
    - **`_`**: a list of intermediate noise tensors obtained during the diffusion process. Each tensor has the same shape as **`latents`**.
    
    In the given code snippet, only **`latents_steps`** is unpacked and stored in the variable **`latents_steps`**. The intermediate latent tensors are used later in the code to generate the positive, negative, and neutral latents using the **`diffuser.predict_noise()`** method.
    
- Why is only latents_steps[0] used but not the rest of latents_steps?
    
    The `latents_steps` variable is a list containing latent tensors at different steps during the diffusion process, starting from the initial `latents` tensor and ending at the `end_iteration` step. The `latents_steps[0]` refers to the latent tensor at the beginning of the diffusion process, which is passed as input to the `predict_noise()` method to generate a new tensor with the same shape and distribution as the positive example. 
    
    The reason why only the first tensor in `latents_steps` is used is that it contains information about the initial distribution of the latent space, which is important for generating new samples with the desired characteristics. The subsequent tensors in `latents_steps` contain information about the diffusion process at later steps and are not used for generating new samples.
    
- Then why generate the latent tensors at later steps? Why not just the first one?
    
    The diffusion process involves a series of steps that gradually modify the initial distribution of the latent space, making it more similar to the distribution of the target image. Therefore, it is important to generate the latent tensors at different steps during the diffusion process to capture the changing distribution of the latent space. In the code, the `latents_steps` list contains the latent tensors at different steps during the diffusion process, starting from the initial `latents` tensor and ending at the `end_iteration` step. By generating latent tensors at different steps during the diffusion process, it is possible to capture the nuances of the target distribution and generate more realistic samples. The `latents_steps[0]` tensor is used to generate the new tensor with the same shape and distribution as the positive example, but the subsequent tensors are not used for generating new samples.
    
    GUESS: this new method doesn’t use those other original tensors (used in typical diffusion), but it requires separately generated tensors in pos, neutral, and neg, due to the modified equation used for diffusion
    
- What is diffuser.predict_noise()?
    
    `diffuser.predict_noise()` is a method of the `StableDiffuser` class which takes a starting latent tensor, a number of diffusion timesteps, and an optional guidance tensor, and returns the final latent tensor after performing diffusion. The method generates noise at each timestep of diffusion by sampling from a Gaussian distribution, and then uses the learned diffusion process to transform the initial noise into the final output tensor. If a guidance tensor is provided, it is used to guide the diffusion process towards a particular target.
    

Positive and neg latent vectors have the same code to genereate, but pos is within the 

Which modules will be fine-tuned?

The FineTunedModel object will fine-tune the entire diffuser object, except for the modules specified in the frozen_modules argument. These frozen modules will not be fine-tuned during training.

How is **`diffuser`** than **`finetuner`** ?

**`diffuser`** and **`finetuner`** are both objects created from different classes in this code. **`diffuser`** is an object of the **`StableDiffuser`** class, which is the primary model used for image and text generation. On the other hand, **`finetuner`** is an object of the **`FineTunedModel`** class, which is a wrapper model around **`diffuser`** that allows fine-tuning specific layers.

In other words, **`diffuser`** is the main model used for image and text generation, while **`finetuner`** is used to fine-tune specific layers of **`diffuser`**.

[https://github.com/rohitgandikota/erasing/blob/main/train-scripts/train-esd.py](https://github.com/rohitgandikota/erasing/blob/main/train-scripts/train-esd.py)