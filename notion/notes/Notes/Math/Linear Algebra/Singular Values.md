# Singular Values

- What’s the relation between singular values and eigenvalues?
    
    Consider the singular value decomposition (SVD) of a matrix A:
    
    $$
    A = UΣV^T
    $$
    
    where U and V are orthogonal matrices, and Σ is a diagonal matrix with non-negative singular values arranged in descending order. The rank of A is equal to the number of non-zero singular values of A.
    
    Now, consider the eigendecomposition of the matrix $A^TA$ (which is square):
    
    $$
    A^TA = VΛV^T
    $$
    
    where V is an orthogonal matrix of eigenvectors of $A^TA$, and Λ is a diagonal matrix of eigenvalues of $A^TA$, which are all non-negative, and they are equal to the squares of the singular values of A.
    
    ![Untitled](Singular%20Values%20837973abb02f400faa322e0a56f9415b/Untitled.png)
    
    Thus, the number of non-zero singular values of A is equal to the number of non-zero eigenvalues of A^TA, which is equal to the rank of A. 
    
    Note that this relationship holds for any matrix A, not just square matrices. In general, if A is an m x n matrix with rank r, then the non-zero singular values and non-zero eigenvalues of A^TA and AA^T are the same, and their number is equal to r.
    

---

singular vs eigenvalues diff?

Singular values and eigenvalues are both important mathematical quantities associated with matrices, but they have different properties and interpretations.

Eigenvalues are a set of scalars that describe how a matrix transforms a vector. Specifically, an eigenvector is a nonzero vector that is transformed by the matrix into a scalar multiple of itself, and the corresponding scalar factor is called the eigenvalue. Eigenvalues are always complex numbers and can be used to determine important properties of a matrix, such as its determinant, trace, and invertibility.

Singular values, on the other hand, are related to the singular value decomposition (SVD) of a matrix, which is a factorization of the matrix into three matrices that describes its properties. The singular values of a matrix are the square roots of the eigenvalues of the matrix's Hermitian (conjugate transpose) product with itself. The singular values provide information about the rank and geometry of the matrix and can be used in a variety of applications, such as image processing and data compression.

In summary, eigenvalues describe how a matrix transforms a vector, while singular values are related to the SVD of a matrix and provide information about its rank and geometry.