# How to use SAE- resources

[https://github.com/HoagyC/sparse_coding](https://github.com/HoagyC/sparse_coding)

[https://github.com/ai-safety-foundation/sparse_autoencoder](https://github.com/ai-safety-foundation/sparse_autoencoder)

[https://ai-safety-foundation.github.io/sparse_autoencoder/demo/](https://ai-safety-foundation.github.io/sparse_autoencoder/demo/)

[https://colab.research.google.com/github/ai-safety-foundation/sparse_autoencoder/blob/main/docs/content/demo.ipynb](https://colab.research.google.com/github/ai-safety-foundation/sparse_autoencoder/blob/main/docs/content/demo.ipynb)

this doesn’t show how to train, just gives abstracted away fn

neel training :

[https://docs.google.com/document/u/0/d/187jfZSbhRjjQaazjYlThBsKp3Q0Pw3VdIHVST9H2dvw/mobilebasic](https://docs.google.com/document/u/0/d/187jfZSbhRjjQaazjYlThBsKp3Q0Pw3VdIHVST9H2dvw/mobilebasic)

[https://colab.research.google.com/drive/1u8larhpxy8w4mMsJiSBddNOzFGj7_RTn?usp=sharing](https://colab.research.google.com/drive/1u8larhpxy8w4mMsJiSBddNOzFGj7_RTn?usp=sharing)

doesn’t train sae, just loads it

- I find that, empirically, the decoder and encoder weights for each feature are moderately different, with median cosine sim of only 0.5.
- I argue that this is empirical evidence for untying the encoder and decoder weights