# Low Rank

Why?

1. Can reduce the number of parameters in the model, which can help prevent overfitting and improve the generalization performance of the model.
2. It can make the computation of matrix operations more efficient, as the low-rank structure allows for faster matrix multiplication and inversion.
3. Learn low-dimensional representations of the input data, which can be useful for tasks such as dimensionality reduction and feature extraction.

How?

There are various methods for enforcing low-rank constraints on weight matrices.

1. [Singular value decomposition (SVD](../Math%2089624985ddb64f0c91c334b1ab5df1d0/Linear%20Algebra%20e6bc642112314024b2392685dfd6e47a/Singular%20Values%20837973abb02f400faa322e0a56f9415b.md)), truncated SVD
2. Low-rank matrix factorization

- Why does it reduce the number of parameters ?
    
    A low-rank weight matrix has fewer non-zero singular values or eigenvalues, which means that it has fewer independent dimensions or features. This reduction in dimensions or features can lead to a reduction in the number of parameters needed to represent the matrix.
    
    To see why this is the case, consider a weight matrix with dimensions (m x n), where m is the number of input neurons and n is the number of output neurons. Without any constraints on the matrix, there would be m x n parameters to learn. However, if the matrix is low-rank, we can represent it as a product of two lower-dimensional matrices, say A and B, with dimensions (m x k) and (k x n), respectively, where k is the rank of the matrix.
    
    In this case, we only need to learn k x (m + n) parameters instead of m x n parameters, which can be much smaller if k is much smaller than min(m, n). This reduction in the number of parameters can make the model more efficient, less prone to overfitting, and easier to optimize.
    
    Note that the rank k can also be interpreted as the number of latent factors or hidden features that the model is learning from the input data. By reducing the rank, we can learn a lower-dimensional representation of the input data that captures the most important information and removes noise or irrelevant features.
    

[https://colab.research.google.com/github/neelnanda-io/TransformerLens/blob/main/demos/Main_Demo.ipynb#scrollTo=ddd95u0bzrPN](https://colab.research.google.com/github/neelnanda-io/TransformerLens/blob/main/demos/Main_Demo.ipynb#scrollTo=ddd95u0bzrPN)

- Why are low-rank factorized matrices useful for transformer interpretability?
    
    As argued in [A Mathematical Framework](https://transformer-circuits.pub/2021/framework/index.html), an unexpected fact about transformer attention heads is that rather than being best understood as keys, queries and values (and the requisite weight matrices), they're actually best understood as two low rank factorized matrices.
    
    - **Where to move information from:** , used for determining the attention pattern - what source positions to move information from and what destination positions to move them to.
        
        WQK=WQWTK
        
        - Intuitively, residual stream -> query and residual stream -> key are linear maps, *and* `attention_score = query @ key.T` is a linear map, so the whole thing can be factored into one big bilinear form `residual @ W_QK @ residual.T`
    - **What information to move:** , used to determine what information to copy from the source position to the destination position (weighted by the attention pattern weight from that destination to that source).
        
        WOV=WVWO
        
        - Intuitively, the residual stream is a `[position, d_model]` tensor (ignoring batch). The attention pattern acts on the *position* dimension (where to move information from and to) and the value and output weights act on the *d_model* dimension - ie *what* information is contained at that source position. So we can factor it all into `attention_pattern @ residual @ W_V @ W_O`, and so only need to care about `W_OV = W_V @ W_O`
    - Note - the internal head dimension is smaller than the residual stream dimension, so the factorization is low rank. (here, `d_model=768` and `d_head=64`)

---

NOTES:
See [Low Rank](../Math%2089624985ddb64f0c91c334b1ab5df1d0/Linear%20Algebra%20e6bc642112314024b2392685dfd6e47a/Low%20Rank%20818dedfe95ac406c8a655a1bcb715813.md)