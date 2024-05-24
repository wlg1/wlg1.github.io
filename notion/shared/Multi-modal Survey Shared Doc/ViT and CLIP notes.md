# ViT and CLIP notes

*Notes on CLIP*

A CLIP model consists of two sides, a ResNet vision model and a Transformer

*Notes on ViT*

Unlike language models, vision transformers do not have a dictionary-style embedding and unembedding matrix. Instead, images are divided into non-overlapping patches, similar to tokens in language models. These patches are flattened and linearly projected to embeddings via a Conv2D layer, akin to word embeddings in language models. A learnable class token (CLS token) is prepended at the start of the sequence, which accrues global information throughout the network. A linear position embedding is added to the patches.

**Patches like tokens projected to embeddings**

**The patch embeddings then pass through the transformer blocks** (each block consists of a LayerNorm, an Attention layer, another LayerNorm, and an MLP layer). The output of each block is added back to the previous input. The sum of the block’s output and its previous input is called the residual stream.

The final layer of this vision transformer is a classification head with 1000 logit values for ImageNet's 1000 classes. The CLS token is fed into the final layer for 1000-way classification.

Differences with LLMs

- The typical ViT is not doing unidirectional sequence modeling. ViTs use bidirectional attention and predict a global CLS token, rather than predicting the next token in an autoregressive manner.
- Bidirectional attention vs causal attention. Language transformers have causal (unidirectional) attention-- i.e. there is an upper triangular mask on the attention, so that earlier tokens cannot attend to tokens in the future. However, the classical ViT has bidirectional attention.
- a yellow patch on a goldfinch might represent "yellow," "wing," "goldfinch," "bird," or "animal," depending on the granularity, showing hierarchical ambiguity.