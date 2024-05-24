# How to train & interpret SAE- notes

[https://www.alignmentforum.org/posts/HpAr8k74mW4ivCvCu/progress-update-from-the-gdm-mech-interp-team-summary](https://www.alignmentforum.org/posts/HpAr8k74mW4ivCvCu/progress-update-from-the-gdm-mech-interp-team-summary)

[https://www.alignmentforum.org/posts/f9EgfLSurAiqRJySD/open-source-sparse-autoencoders-for-all-residual-stream](https://www.alignmentforum.org/posts/f9EgfLSurAiqRJySD/open-source-sparse-autoencoders-for-all-residual-stream)

[https://www.lesswrong.com/posts/fifPCos6ddsmJYahD/my-best-guess-at-the-important-tricks-for-training-1l-saes](https://www.lesswrong.com/posts/fifPCos6ddsmJYahD/my-best-guess-at-the-important-tricks-for-training-1l-saes)

[https://github.com/jbloomAus/SAELens](https://github.com/jbloomAus/SAELens)

[https://jbloomaus.github.io/SAELens/training_saes/](https://jbloomaus.github.io/SAELens/training_saes/)

---

[1.4](../../ARENA%20notes%201a8ff2624cff486e9d91b13139420026/1%204%200186fae1fa2d41e49f64642d2ea523eb.md) 

[https://colab.research.google.com/drive/1hoD36nsHp6K0E-YeFgPzxazlstb7HPyh](https://colab.research.google.com/drive/1hoD36nsHp6K0E-YeFgPzxazlstb7HPyh#scrollTo=2ZElPqnT5DS0)

[https://github.com/neelnanda-io/1L-Sparse-Autoencoder](https://github.com/neelnanda-io/1L-Sparse-Autoencoder)

[https://github.com/callummcdougall/ARENA_3.0/blob/main/chapter1_transformer_interp/exercises/part4_superposition_and_saes/solutions.py](https://github.com/callummcdougall/ARENA_3.0/blob/main/chapter1_transformer_interp/exercises/part4_superposition_and_saes/solutions.py)

**Exercise - find highest-activating tokens**

This is a feature vector WEIGHT: `autoencoder.W_enc[instance_idx, :, feature_idx]`

This is a feature vec actv

```
acts = einops.einsum(
        h_cent, autoencoder.W_enc[instance_idx, :, feature_idx],
        "batch_size n_input_ae, n_input_ae -> batch_size"
    )
```