# SVD explora tests

CAA has been updated. Look at new repo’s `generate_vectors`

[CAA_actvs_unembSVD_explrTests_v1.ipynb](https://colab.research.google.com/drive/1a0n70XzpTdPr5UMEILzIBrrRhyAFvWJC)

`model.model.model.layers[15].activations`

- ✅ logit lens
    - first check final logits are unembed corr before unembed intr feats
    - check its shape is corr
    - try layer norm before unembed
- ✅ SVD on actvs, then unembed singular vectors
    - [https://github.com/BerenMillidge/svd_directions](https://github.com/BerenMillidge/svd_directions)
    - We are mixing code from svd_directions and CAA. Not transformelns
        - find other papers that directly apply pca/svd on actvs, such as gpt-2 gt
        - check llama 2 unembedding in assoc concepts
- ✅ decompose steering vector

---

[https://colab.research.google.com/drive/1a0n70XzpTdPr5UMEILzIBrrRhyAFvWJC#scrollTo=IaIUKBHKWUeT&line=1&uniqifier=1](https://colab.research.google.com/drive/1a0n70XzpTdPr5UMEILzIBrrRhyAFvWJC#scrollTo=IaIUKBHKWUeT&line=1&uniqifier=1)

In this post, the authors state they:

> directly edit model weights to remove or enhance specific singular directions
> 

So far, these singular vectors of the L15 steering vector (similar to the L15 activations) do not appear to be interpretable, so we have to find another feature decomposition to edit.

What's strange is that the third last token does appear to be interpretable for A or B options. But those are the direct tokens, not "interpretable" as concepts like "truthful".

It could be that truthful isn't encoded in these vectors this way, but in some other way, and these vectors just shfit from A to B. That's why their top features are "abit" or "aye", which seem to have some proximity to token A?

Perhaps it's AFTER they're added to the activations that they're interpretable.