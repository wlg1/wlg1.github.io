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
    

---

NOTES:
See [Low Rank](../Math%2089624985ddb64f0c91c334b1ab5df1d0/Linear%20Algebra%20e6bc642112314024b2392685dfd6e47a/Low%20Rank%20818dedfe95ac406c8a655a1bcb715813.md)