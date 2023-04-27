# Eigenvalues

- Do eigenvalues non-symmetric?
    
    Yes, eigenvalues can be defined for non-symmetric matrices. However, the eigenvalues of a non-symmetric matrix may have more complex properties than those of a symmetric matrix.
    
    For a symmetric matrix, the eigenvalues are always real and the eigenvectors are always orthogonal. This is a consequence of the spectral theorem, which states that any real symmetric matrix can be diagonalized by an orthogonal matrix.
    
    In contrast, the eigenvalues of a non-symmetric matrix can be complex and may not have corresponding eigenvectors that are orthogonal. 
    
    The eigenvalues and eigenvectors of non-symmetric matrices are studied in the field of numerical linear algebra, where algorithms are developed for computing them efficiently and accurately. One important algorithm for computing the eigenvalues and eigenvectors of non-symmetric matrices is the QR algorithm, which uses orthogonal transformations to reduce the matrix to a upper Hessenberg form, where the eigenvalues can be easily computed.
    

eigenvectors form a basis for the space if the matrix A is diagonalizable