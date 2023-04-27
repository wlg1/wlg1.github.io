# Erasing Concepts from Diffusion Models

Change the objective function then fine tune.

What are the images being fine tuned on? They start as noise then become an image. So the noise is directed, by the new objective function, to an image without the erased concept.

SPECULATION: In transformers, one would fine tune on prompts such that the predicted words are steered away from a certain style. This style would come from already-known-by-model probability(concept/style | previous words), so that would be what we want to erase.

Why directly edit weights in ROME instead of fine tune? Fine tune has too much room for unintended edits, whereas rank one edit is very direct and has less unintended side effects. But style is hard to be direct on, so it may require fine tuning, unless we can find the circuit (see ****[A Mechanistic Interpretability Analysis of Grokking](https://www.neelnanda.io/blog/interlude-a-mechanistic-interpretability-analysis-of-grokking))**

---

[https://erasing.baulab.info/](https://erasing.baulab.info/)

We query the frozen pre-trained model to predict the noise for a given prompt, then we train the edited model to guide it in the opposite direction using the ideas of classifier-free guidance at training time rather than inference.

QUESTIONABLE:

The method works like a teacher guiding a student in erasing a specific concept from their mind. The teacher provides negative guidance by telling the student what not to think about, and the student adjusts their thinking accordingly. Similarly, our method fine-tunes model weights to erase a targeted visual concept by providing negative guidance in the form of a short text description of the concept and adjusting the model's parameters accordingly.

Classifier-free guidance involves guiding a model based on its input data and how it can navigate through it, rather than using pre-defined categories or labels. The model learns to identify patterns and make predictions based on the features of the data, without explicitly being told what those features represent or how they should be categorized.

---

[https://github.com/rohitgandikota/erasing/blob/main/train-scripts/train-esd.py](https://github.com/rohitgandikota/erasing/blob/main/train-scripts/train-esd.py)

I see that this is a Python script that includes functions to train a diffusion model to erase a specific concept using the ESD method. The script uses PyTorch, PIL, OmegaConf, and other libraries to train the model. The training process involves loading a pre-trained model checkpoint, setting parameters to train, and updating the model weights to erase the concept. The code saves the trained model and the loss curve. The script takes several arguments, including the concept to erase, the training method, the guidance for start and negative training, the number of iterations, the learning rate, the configuration and checkpoint paths for the stable diffusion v1-4 inference, and the devices to train on. There is also an option to separate a prompt by a specific separator for individual simultaneous erasures.

[data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%2730%27%20height=%2730%27/%3e](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%2730%27%20height=%2730%27/%3e)

Which part of the code updates the model weights?

The following lines of code update the model weights during training:

```
scssCopy code
opt.zero_grad()
loss.backward()
opt.step()

```

The **`zero_grad()`** method clears the gradients of all optimized parameters, while the **`backward()`** method computes the gradients of the loss with respect to the model parameters. Finally, the **`step()`** method updates the model parameters using the computed gradients.

[data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%2730%27%20height=%2730%27/%3e](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%2730%27%20height=%2730%27/%3e)

In simple terms, what does this mean?
# reconstruction loss for ESD objective from frozen model and conditional score of ESD model
 loss = criteria(e_n.to(devices[0]), e_0.to(devices[0]) - (negative_guidance*(e_p.to(devices[0]) - e_0.to(devices[0])))) #loss = criteria(e_n, e_0) works the best try 5000 epochs

This code calculates the loss function for the ESD objective by comparing the reconstructed output **`e_n`** from the frozen model to the target input **`e_0`**. It also takes into account the conditional score of the ESD model by subtracting a guided negative term from **`e_0`**. The **`criteria`** function is used to compute the actual loss value. The value of the loss function is used to update the model parameters during the training process. The comment suggests that after trying various hyperparameters and training epochs, using the current implementation with 5000 epochs gave the best performance.

[data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%2730%27%20height=%2730%27/%3e](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%2730%27%20height=%2730%27/%3e)

What does this do?
 with torch.no_grad():
            # generate an image with the concept from ESD model
            z = quick_sample_till_t(emb_p.to(devices[0]), start_guidance, start_code, int(t_enc)) # emb_p seems to work better instead of emb_0
            # get conditional and unconditional scores from frozen model at time step t and image z
            e_0 = model_orig.apply_model(z.to(devices[1]), t_enc_ddpm.to(devices[1]), emb_0.to(devices[1]))
            e_p = model_orig.apply_model(z.to(devices[1]), t_enc_ddpm.to(devices[1]), emb_p.to(devices[1]))
        # breakpoint()
        # get conditional score from ESD model
        e_n = model.apply_model(z.to(devices[0]), t_enc_ddpm.to(devices[0]), emb_n.to(devices[0]))
        e_0.requires_grad = False
        e_p.requires_grad = False
        # reconstruction loss for ESD objective from frozen model and conditional score of ESD model
        loss = criteria(e_n.to(devices[0]), e_0.to(devices[0]) - (negative_guidance*(e_p.to(devices[0]) - e_0.to(devices[0])))) #loss = criteria(e_n, e_0) works the best try 5000 epochs

This code generates an image using the "quick_sample_till_t" function and a concept from the ESD model. Then, it calculates the conditional and unconditional scores from the frozen model "model_orig" for the generated image at a particular time step t. After that, it gets the conditional score from the ESD model "model" for the same generated image.

The "torch.no_grad()" context manager is used to prevent PyTorch from computing gradients, as these operations are only for inference, not training.

The code then calculates the reconstruction loss for the ESD objective, using the conditional score from the ESD model and the frozen model's conditional and unconditional scores. This loss is calculated using the "criteria" function.

Finally, the "requires_grad" attribute of "e_0" and "e_p" is set to False to prevent gradients from being computed for them during the subsequent backward pass.

[data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%2730%27%20height=%2730%27/%3e](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%2730%27%20height=%2730%27/%3e)

What are the  conditional and unconditional scores?

In the context of this code, conditional and unconditional scores refer to the scores or log probabilities of a generated image under two different models: the "frozen" model and the "ESD" model.

The unconditional score is the log probability of the generated image under the frozen model, which is a pre-trained model that is not being updated during training. This score measures how well the generated image fits the statistical distribution learned by the frozen model.

The conditional score is the log probability of the generated image under the ESD model, which is the model being updated during training. This score measures how well the generated image fits the statistical distribution learned by the ESD model, while taking into account the additional information provided by the conditional embeddings used as input to the ESD model.

[data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%2730%27%20height=%2730%27/%3e](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%2730%27%20height=%2730%27/%3e)

Using an analogy, why  conditional and unconditional scores?

One possible analogy for conditional and unconditional scores can be a teacher grading a student's performance on a test.

The unconditional score would be the overall score the student receives for their test performance, regardless of any external factors. It reflects the student's innate ability and knowledge.

The conditional score, on the other hand, would take into account any external factors that may have influenced the student's performance, such as the difficulty of the test, the quality of the teaching, or any other relevant factors. It reflects the student's performance in a specific context.

Similarly, in the context of generative models, unconditional scores reflect how well the model can generate high-quality samples on average, while conditional scores measure the quality of the generated samples given a specific condition or input.

Map entities and relations the analogy of a conditional score being a test that takes external factors into account to "Conditional score measures how well the generated image fits the statistical distribution learned by the ESD model". For example, test score in the domain maps to conditional score in the target. What does "external factors" in a test map to in the target?

In this analogy, we can map the following entities and relations:

- Domain: The domain refers to the area of knowledge or expertise that the test is designed for, such as mathematics or history.
- Test: The test is an evaluation tool used to measure a person's knowledge or skills in a particular domain.
- Test score: The test score is the final result of the evaluation, which measures how well the person performed in the test.
- Target: The target refers to the statistical distribution learned by the ESD model, which represents the desired characteristics of the generated images.
- ESD model: The ESD model is a statistical model used to generate images that match a particular distribution.
- Generated image: The generated image is the result of the ESD model's output, which should match the target distribution.
- Conditional score: The conditional score measures how well the generated image fits the target distribution, taking into account external factors such as the input or conditioning information.

Therefore, we can say that the test score in the domain maps to the conditional score in the target, as they both measure how well a given input (knowledge or image) matches a desired output (expected performance or statistical distribution) while taking into account external factors.

In the analogy, the "external factors" in a test would map to any additional information or context that is provided to the ESD model when generating an image. This information could be in the form of a latent code or other parameters that influence the image generation process. Just as external factors such as preparation, test anxiety, or the difficulty of the questions can affect a student's test score, external factors provided to the ESD model can affect the conditional score of the generated image. Therefore, the conditional score measures how well the generated image fits the statistical distribution learned by the ESD model, taking into account these external factors.