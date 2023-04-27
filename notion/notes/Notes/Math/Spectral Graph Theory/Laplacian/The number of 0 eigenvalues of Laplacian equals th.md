# The number of 0 eigenvalues of Laplacian equals the number of connected components

[https://timroughgarden.org/s17/l/l11.pdf](https://timroughgarden.org/s17/l/l11.pdf)

![Untitled](The%20number%20of%200%20eigenvalues%20of%20Laplacian%20equals%20th%207e7e19bc98194fb6a23a4447e6d75e54/Untitled.png)

$v_i$ is the vector row [1, …, j, …. n]

$v_i(j)$ is a component (entry) of that row

In $\sqrt{|S_i|}$   , |Si| is the number of vertices in connected component i.

$L * v_i = 0$ shows it’s an eigenvector AND it has an eigenvalue of 0, since v is nonzero.

See also: [Show a vector has an eigenvalue of 0](https://www.notion.so/Show-a-vector-has-an-eigenvalue-of-0-03adefc312044ecf905a8f61dc93de23) 

- ???: This is “=0” because:
    
    L = D - A
    
    v only contains the entries in the row of D and A, and all have the same value, which means that value can be factored out.
    
    So the dot product (D-A) * v is summing up all entries of D-A, which is 0.
    

If 0 eigenvalues corresponds to those in null space (number of linearly dep columns), and these correspond to conn components, the lin indp eigenvectors correspond to ???(complement of conn components — doesn’t make sense to say “disconn comps” b/c that’s not a real term)

- Questionable- to revise
    
    The reason for defining the vectors in this way is to ensure that they are orthogonal and have unit norm. By construction, the vectors vi are normalized, because their Euclidean norm is given by ||vi|| = (1/√|Si|) * √|Si| = 1. This ensures that they are of unit length, and thus provide an orthonormal basis for the subspace of the null space of the Laplacian matrix that corresponds to the zero eigenvalues.
    
    Moreover, the vectors vi are orthogonal to each other, because they are defined such that they are non-zero only on the vertices of the corresponding connected component Si. Specifically, for i ≠ j, the sets Si and Sj are disjoint, and therefore, vi and vj are orthogonal. This property ensures that the k vectors vi provide an orthonormal basis for the null space of the Laplacian matrix that corresponds to the zero eigenvalues.
    
    Therefore, by constructing these vectors in this way, we can use them to prove that the dimension of the null space of the Laplacian matrix is at least k, which in turn proves that the number of zero eigenvalues of the Laplacian matrix is at least k, where k is the number of connected components of the graph.
    

# LARGE TOGGLE

test

---

[https://www.cs.cmu.edu/~venkatg/teaching/15252-sp20/notes/Spectral-graph-theory.pdf](https://www.cs.cmu.edu/~venkatg/teaching/15252-sp20/notes/Spectral-graph-theory.pdf)

Lemma 9

In this variation of the above proof, it uses “1” in each component instead.