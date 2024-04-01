# CAA_SAE_explrTests_v1.ipynb

[https://github.com/HoagyC/sparse_coding](https://github.com/HoagyC/sparse_coding)

[https://github.com/ai-safety-foundation/sparse_autoencoder](https://github.com/ai-safety-foundation/sparse_autoencoder)

[https://ai-safety-foundation.github.io/sparse_autoencoder/demo/](https://ai-safety-foundation.github.io/sparse_autoencoder/demo/)

[https://colab.research.google.com/github/ai-safety-foundation/sparse_autoencoder/blob/main/docs/content/demo.ipynb](https://colab.research.google.com/github/ai-safety-foundation/sparse_autoencoder/blob/main/docs/content/demo.ipynb)

---

1.4:

[https://colab.research.google.com/drive/1hoD36nsHp6K0E-YeFgPzxazlstb7HPyh](https://colab.research.google.com/drive/1hoD36nsHp6K0E-YeFgPzxazlstb7HPyh#scrollTo=2ZElPqnT5DS0)

[https://github.com/neelnanda-io/1L-Sparse-Autoencoder](https://github.com/neelnanda-io/1L-Sparse-Autoencoder)

[https://github.com/callummcdougall/ARENA_3.0/blob/main/chapter1_transformer_interp/exercises/part4_superposition_and_saes/solutions.py](https://github.com/callummcdougall/ARENA_3.0/blob/main/chapter1_transformer_interp/exercises/part4_superposition_and_saes/solutions.py)

**Exercise - find highest-activating tokens**

This is a feature vector WEIGHT: `autoencoder.W_enc[instance_idx, :, feature_idx]`

This is a feature vec actv? 

```
acts = einops.einsum(
        h_cent, autoencoder.W_enc[instance_idx, :, feature_idx],
        "batch_size n_input_ae, n_input_ae -> batch_size"
    )
```

---

[https://colab.research.google.com/drive/1rv8d3VJBSLxtSbFGq1809VZB1BGPGiZe#scrollTo=XcgAnZZOyBYk](https://colab.research.google.com/drive/1rv8d3VJBSLxtSbFGq1809VZB1BGPGiZe#scrollTo=XcgAnZZOyBYk)