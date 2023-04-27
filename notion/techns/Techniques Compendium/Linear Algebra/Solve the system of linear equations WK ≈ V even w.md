# Solve the system of linear equations WK ≈ V even when the matrix K is not invertible

- SOLN: Use the Moore-Penrose pseudoinverse
    
    The Moore-Penrose pseudoinverse of a matrix A is denoted by A⁺ and can be calculated using the singular value decomposition (SVD) of A. The SVD of A is given by:
    
    $$
    A = UΣV^T
    $$
    
    where U and V are orthogonal matrices, and Σ is a diagonal matrix containing the singular values of A.
    
    The Moore-Penrose pseudoinverse can then be computed as:
    
    $$
    A⁺ = VΣ⁺U^T
    $$
    
    where Σ⁺ is the pseudoinverse of Σ, which is obtained by taking the reciprocal of each nonzero singular value in Σ and transposing the resulting matrix. If Σ has m rows and n columns, then Σ⁺ has n rows and m columns.
    
    Note that if A is invertible, then its pseudoinverse coincides with its inverse: A⁺ = A⁻¹. However, if A is not invertible, then its pseudoinverse provides a way to solve linear equations involving A in a least-squares sense.
    

WHY: 

The pseudoinverse can be used to find a least-squares solution to the equation WK = V even when K is singular or ill-conditioned.

The pseudoinverse is also useful because it provides a unique solution that minimizes the Euclidean norm of the error vector WK - V. This means that it finds a solution that is as close as possible to satisfying the equation, even if there are no exact solutions.

Other methods for solving systems of linear equations, such as Gaussian elimination or LU decomposition, may not work well when K is singular or ill-conditioned. These methods may also not provide a unique solution or may be computationally expensive for large matrices. Therefore, using the Moore-Penrose pseudoinverse is a convenient and efficient way to solve for the least-squares solution in Rank-One Model Editing.