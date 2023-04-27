# Unstable Matrices

- What does it mean condition number is high (meaning that it is ill-conditioned?
    
    The condition number of a matrix A is a measure of how sensitive the solution of a linear system Ax = b is to small changes in the entries of A and b. A high condition number indicates that a small change in the input can result in a large change in the output.
    
    More specifically, the condition number of a matrix A is defined as the product of its norm and the norm of its inverse, i.e., 
    
    $$
    cond(A) = ||A|| ||A^{-1}||
    $$
    
    If the condition number of A is large, it means that the matrix is ill-conditioned, and the solution of Ax = b is more sensitive to small perturbations in the input. This can lead to numerical instability and inaccuracies in the solution.
    
    In practical terms, ill-conditioned matrices arise when the columns of the matrix are nearly linearly dependent or when there is a large difference in magnitudes between the largest and smallest singular values of the matrix. This can happen, for example, when the data used to construct the matrix is noisy or when the matrix is poorly conditioned by design.
    
    - Why the columns of the matrix are nearly linearly dependent or when there is a large difference in magnitudes between the largest and smallest singular values of the matrix when the data is noisy?
        
        The noise in the data can introduce correlations between the columns of the matrix, which can make them linearly dependent.
        
        Similarly, if the noise in the data is large, it can cause some columns of the matrix to have much larger or smaller magnitudes than others. This can result in a large difference in the magnitudes of the singular values of the matrix, which can again result in a high condition number and numerical instability when solving the linear system.
        

---

[https://math.stackexchange.com/questions/675474/what-is-the-practical-impact-of-a-matrixs-condition-number](https://math.stackexchange.com/questions/675474/what-is-the-practical-impact-of-a-matrixs-condition-number)

---

[https://math.stackexchange.com/questions/158219/is-a-matrix-multiplied-with-its-transpose-something-special](https://math.stackexchange.com/questions/158219/is-a-matrix-multiplied-with-its-transpose-something-special)

The main thing is it’s symmetric. For symmetric matrices one has the [Spectral Theorem](http://en.wikipedia.org/wiki/Spectral_theorem)
 which says that we have a basis of eigenvectors and every eigenvalue is real.

---

[https://math.stackexchange.com/questions/2817630/why-is-the-condition-number-of-a-matrix-given-by-these-eigenvalues](https://math.stackexchange.com/questions/2817630/why-is-the-condition-number-of-a-matrix-given-by-these-eigenvalues)