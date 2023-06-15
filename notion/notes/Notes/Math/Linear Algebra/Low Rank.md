# Low Rank

Upon multiplying matrix W with matrices x from SPACE X, there are matrices x in X which are sent to the 0 vector. These dims are “lost”. The dims which are not lost are the linearly independent ones. This is like the “true” dim after transformation; it is the rank.

- Notes
    
    “from SPACE X”: Matrices can also be elements of vector spaces?
    
    “the 0 vector”: in vector space; in general, 0 element
    

So there is a tradeoff between null space (n-r) and rank (r); the bigger rank is, the lower null space is, and vv.

Low rank means the matrix W sends elements from X to a lower dimension after Wx. 

---

Rank is MAXIMALLY linearly independent because a matrix may contain linearly dependent vectors; use algorithms to convert the matrix into a form that only contains linearly independent vectors, with the other vectors being 0, to find the actual number of linearly independent vectors (the columns which are 0 will send dims of x into the 0th element).

---

The number of non-zero eigenvalues (or singular values, if non-square) is the rank.

The number of linearly independent eigenvectors of a matrix is equal to its rank.

A low-rank matrix has a low number of non-zero singular values or eigenvalues

- Eigenvalues and basis?
    
    Since the eigenvectors of a matrix are linearly independent, and the number of linearly independent eigenvectors is equal to the rank of the matrix, the eigenvectors can form a basis called the eigenbasis.
    
- Applications of the eigenbasis
    - Diagonalization: A matrix can be diagonalized by expressing it as a linear combination of its eigenvectors. This diagonalization can simplify calculations and make certain properties of the matrix more apparent.
        - How to get a matrix of diagonal eigenvalues?
            
            Note that if the matrix A is diagonalizable, which means that it can be diagonalized as 
            
            $$
            A = PDP^-1
            $$
            
            where P is a matrix of eigenvectors of A and D is a diagonal matrix of eigenvalues, then the columns of P form a basis for the vector space spanned by A. This is because the columns of P are linearly independent and span the same subspace as the eigenvectors of A.
            
    - Matrix powers: The eigenbasis can be used to compute powers of a matrix A. Specifically, if A is diagonalizable, then:
        
        $$
        A^k = PD^kP^{-1}
        $$
        
        where D^k is the diagonal matrix whose entries are the kth powers of the eigenvalues of A. This can be a useful tool for solving systems of linear differential equations and for analyzing the behavior of dynamical systems.
        
    - The eigenvalues and eigenvectors of A can provide information about the scaling and rotation of vectors under this transformation.
    - [PCA](../../Neural%20Networks%20e6abb23474464e098117dced189fb7bb/PCA%2006651e45a22843a29529bcf6b112ceb5.md)  involves finding the eigenbasis of the covariance matrix of the dataset and projecting the data onto the principal components defined by the eigenvectors.
    

---

- What math properties make a matrix low rank?
    
    A matrix is said to be low-rank if it can be approximated by a matrix with fewer non-zero singular values or eigenvalues. There are several mathematical properties that can make a matrix low-rank:
    
    - Sparsity: A matrix is sparse if it has a large number of zero elements. Sparse matrices often have low-rank structures because they can be approximated by a matrix with fewer non-zero elements.
    - Correlation: A matrix is low-rank if its columns are highly correlated or redundant. In this case, we can represent the matrix as a linear combination of a smaller number of basis vectors, which leads to a low-rank approximation. (this means many vectors are lin dep)
    - Smoothness: A matrix is low-rank if it varies smoothly across its dimensions. For example, an image with slowly varying intensities may have a low-rank structure, as neighboring pixels tend to have similar values.
    - Compressibility: A matrix is low-rank if it can be compressed efficiently using a lossy compression algorithm. Lossy compression algorithms, such as JPEG or MP3, exploit the low-rank structure of the input data to reduce its size.
    - Randomness: A matrix is low-rank with high probability if it is a random matrix with some appropriate distribution. For example, a matrix with random Gaussian entries may have a low-rank structure with high probability.
    
    Note that these properties are not mutually exclusive, and a matrix may have a low-rank structure due to a combination of these properties.
    
- What methods are used to tell if a matrix is low rank?
    
    Determining whether a matrix is low-rank depends on the specific application and the desired level of approximation. However, there are several common methods that can be used to estimate the rank of a matrix:
    
    Singular value decomposition (SVD): SVD is a widely used method for decomposing a matrix into a product of three matrices: U, Σ, and V. The diagonal matrix Σ contains the singular values of the matrix, which are a measure of its rank. If a large fraction of the singular values are close to zero, then the matrix is low-rank. The rank can be estimated by selecting a threshold value for the singular values, below which they are considered to be zero.
    
    Principal component analysis (PCA): PCA is a method for finding the principal components or the most important directions of variation in a dataset. PCA can be applied to a matrix by decomposing it into its eigenvectors and eigenvalues. If the matrix has a low-rank structure, then only the eigenvectors corresponding to the largest eigenvalues are needed to capture most of its variation.
    
    Matrix factorization: Matrix factorization is a general term for methods that decompose a matrix into a product of two or more lower-dimensional matrices. For example, non-negative matrix factorization (NMF) decomposes a non-negative matrix into two non-negative matrices with lower rank. The rank of the matrix can be estimated by the size of the smaller factor.
    
    Rank revealing QR decomposition: This method computes the QR decomposition of a matrix and also reveals its rank by computing the maximum number of linearly independent columns of the upper triangular factor of the QR decomposition.
    
    ## It's important to note that these methods are not foolproof and can be affected by noise and other factors. Additionally, the choice of method for estimating the rank of a matrix depends on the specific problem and the properties of the matrix.
    

---

- What's null space in relation to low rank?
    
    The null space of a matrix is the set of all vectors that are mapped to zero by the matrix. In other words, the null space is the set of solutions to the homogeneous equation Ax=0
    
    If a matrix has a low rank, then its null space can be high-dimensional. This is because a low-rank matrix has linearly dependent columns or rows, which means that there are many vectors that are mapped to zero by the matrix.
    
    One way to think about this is to consider the SVD decomposition of a low-rank matrix A:
    
    $$
    A = UΣV^T
    $$
    
    where U and V are orthogonal matrices, and Σ is a diagonal matrix of singular values. If A has a low rank r, then there will be r non-zero singular values in Σ, followed by (n-r) zero singular values. The columns of U corresponding to the zero singular values form a basis for the null space of A, and the rows of V corresponding to the zero singular values form a basis for the left null space of A.
    
    The high-dimensional null space of a low-rank matrix can have some useful applications. For example, in compressed sensing, a low-rank matrix is used to represent a high-dimensional signal with a small number of parameters. The null space of the matrix represents the set of possible signals that could have produced the same measurements, and this can be used to recover the original signal from incomplete or noisy measurements. Similarly, in collaborative filtering, a low-rank matrix is used to model the preferences of users and items, and the null space of the matrix represents the set of possible new items or users that could be added to the system.
    

---

- How to rewrite matrices as low rank?
    
    Matrices can be rewritten as low rank using matrix factorization techniques. The most commonly used matrix factorization technique is Singular Value Decomposition (SVD), which factorizes a matrix into a product of three matrices, as follows:
    
    $$
    A = UΣV^T
    $$
    
    where A is the matrix to be factorized, U is an m × r matrix, Σ is an r × r diagonal matrix, and V^T is an r × n matrix. The columns of U are the left singular vectors, the columns of V are the right singular vectors, and the diagonal entries of Σ are the singular values.
    
    To obtain a low rank approximation of A, we can truncate the number of singular values used in the factorization. This is equivalent to setting some of the singular values to zero, which results in a lower rank matrix approximation. Specifically, we can approximate A as:
    
    $$
    A ≈ UΣ_kV_k^T
    $$
    
    where Σ_k is a diagonal matrix containing the first k singular values, and U and V_k are the corresponding matrices of left and right singular vectors.
    
    The resulting matrix $UΣ_kV_k^T$ is the best rank-k approximation of A in terms of the Frobenius norm. Therefore, by choosing an appropriate value of k, we can obtain a low-rank approximation of the matrix A. This technique is useful for compressing large matrices and reducing their storage requirements, as well as for dimensionality reduction in data analysis and machine learning applications.