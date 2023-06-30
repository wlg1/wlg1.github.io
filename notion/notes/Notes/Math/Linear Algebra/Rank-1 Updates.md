# Rank-1 Updates

- Does a rank-1 matrix mean both that the matrix is rank-1 and that it can be decomposed into an outer product of two rank-1 matrices?
    
    Yes, a rank-1 matrix satisfies both conditions: it is a matrix of rank 1, and it can be decomposed into an outer product of two rank-1 matrices.
    
    A matrix is said to have rank 1 if the maximum number of linearly independent rows or columns in the matrix is 1. In other words, all the rows or columns of a rank-1 matrix can be expressed as scalar multiples of a single row or column vector.
    
    Mathematically, a rank-1 matrix can be written as the outer product of two vectors. Let's say we have a matrix A of size m x n, and it has rank 1. This means that there exist two vectors u (of size m x 1) and v (of size 1 x n) such that A = uv, where uv represents the outer product of u and v.
    
    The outer product of two vectors u and v is defined as the matrix product of u and the transpose of v: uv = u * v^T.
    
    Therefore, a rank-1 matrix can indeed be decomposed into an outer product of two rank-1 matrices, where the first matrix represents a column vector and the second matrix represents a row vector.
    

![Untitled](Rank-1%20Updates%205c333cecc74b4b17a0e585b31bbc6849/Untitled.png)

![Untitled](Rank-1%20Updates%205c333cecc74b4b17a0e585b31bbc6849/Untitled%201.png)

This is because the rank-1 matrix $v^T$ is only different in each row by being multiplied by different scalar factors, each one being an element of $u$. So every row is just a multiple of $v^T$, meaning its row space is rank 1.

Similarly, matrix $u$ is only different in each col by being multipled by different scalars from $v^T$.

---

[https://leobouts.medium.com/rank-1-updates-in-linear-algebra-in-simple-terms-7b5032a11a3e](https://leobouts.medium.com/rank-1-updates-in-linear-algebra-in-simple-terms-7b5032a11a3e)