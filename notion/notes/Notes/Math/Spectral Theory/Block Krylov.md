# Block Krylov

What is block Krylov? Be concise

Block Krylov is a variant of the Krylov subspace method for solving large linear systems of equations, where the matrix is multiplied by a block of vectors instead of a single vector at each iteration. This method is particularly useful when the linear system has multiple right-hand sides, as it can efficiently compute a basis for the Krylov subspace of the matrix and all the right-hand sides simultaneously. This reduces the number of matrix-vector products needed to solve the linear system and can lead to significant computational savings.

---

[data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%2730%27%20height=%2730%27/%3e](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%2730%27%20height=%2730%27/%3e)

What is a block fo  vectors?

A block of vectors refers to a collection of vectors that are stacked together vertically to form a matrix. Each individual vector in the block is typically of the same dimension, and the number of vectors in the block is called the block size.

For example, a block of size m consisting of n-dimensional vectors can be represented as an m x n matrix, where each row of the matrix corresponds to an individual vector in the block.

Block vectors are commonly used in numerical linear algebra when dealing with multiple vectors simultaneously, such as in the case of solving linear systems with multiple right-hand sides or computing the action of a matrix on multiple vectors at once. Using block vectors can lead to more efficient computations, as it allows for the use of matrix-matrix operations rather than multiple matrix-vector operations.

---

[data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%2730%27%20height=%2730%27/%3e](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%2730%27%20height=%2730%27/%3e)

Why is a block of vectors not just a matrix?

While a block of vectors can be represented as a matrix, it is important to distinguish between the two concepts because they are used in different contexts and have different properties.

A matrix typically represents a linear transformation that maps a vector in one space to another vector in a different space. In contrast, a block of vectors is a collection of vectors that may or may not have any linear relationship between them.

Furthermore, when dealing with multiple vectors simultaneously, it is often more computationally efficient to treat them as a block rather than as individual vectors. For example, matrix-matrix operations can be used to perform operations on blocks of vectors, whereas matrix-vector operations can only be performed on individual vectors.

Therefore, while a block of vectors can be represented as a matrix, it is important to understand the distinction between the two concepts and their different properties and uses.