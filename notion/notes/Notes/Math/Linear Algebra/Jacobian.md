# Jacobian

Q: In laymen's terms, describe how the Jacobian and SVD are related

The relationship between the Jacobian and SVD is that the Jacobian matrix can be decomposed using the SVD. Specifically, the Jacobian matrix can be decomposed into a product of three matrices, similar to the SVD decomposition: a left-singular matrix, a diagonal matrix of singular values, and a right-singular matrix. The singular values of the Jacobian matrix correspond to the magnitudes of the gradients of the function, and the left-singular and right-singular matrices correspond to the directions of the gradients in the input and output spaces, respectively.

Used for: computing the gradient, determining the stability of a system, or performing dimensionality reduction.