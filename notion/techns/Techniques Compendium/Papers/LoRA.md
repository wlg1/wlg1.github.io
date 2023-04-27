# LoRA

[https://replicate.com/blog/lora-faster-fine-tuning-of-stable-diffusion](https://replicate.com/blog/lora-faster-fine-tuning-of-stable-diffusion)

LoRA stands for Low-Rank Adaptation, a mathematical technique to reduce the number of parameters that are trained. You can think of it like creating a diff of the model, instead of saving the whole thing.

---

### GENERALIZE:

**Problem**: How to reduce number of Transformer parameters?

**Solution**: Freeze the pre-trained model weights and inject trainable rank decomposition matrices into each layer of the Transformer architecture

**Reasoning:** Low-rank weight matrices were shown to be good enough. Decomposition is done by factorizing into a frozen matrix W0 and matrices with smaller dimensions.

$h = W_0 + BA$

---

### GENERALIZE:

Problem: