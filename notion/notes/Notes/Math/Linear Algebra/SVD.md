# SVD

REASON: for decomposition, which allows us to pick the most important components, thus reducing dim while preserving most of the values of the matrix. This is just like PCA (which is SVD specific to covariance matrices, while SVD is for all matrices)

- how do we measure “how much” is preserved by selecting singular vectors of SVD? is it by ratio of selected singular values to the rest?
    
    The Singular Value Decomposition (SVD) is a matrix factorization technique that decomposes a matrix into three components: U, Σ, and V^T. The diagonal elements of the Σ matrix represent the singular values of the original matrix.
    
    When performing SVD, selecting singular vectors refers to choosing a subset of the columns of U and V corresponding to the most significant singular values. The significance of a singular value can be interpreted as its contribution to the overall structure or information content of the original matrix.
    
    To measure how much information is preserved by selecting singular vectors, you can use the concept of explained variance or energy. The total energy of the matrix is defined as the sum of the squares of all singular values. By selecting a subset of singular vectors, you can calculate the energy of the selected singular values and compare it to the total energy.
    
    The ratio of the selected singular values' energy to the total energy gives you an indication of how much information is preserved. If the ratio is high (close to 1), it means that a large portion of the original matrix's information is captured by the selected singular vectors. On the other hand, if the ratio is low, it implies that a significant amount of information is lost by discarding the remaining singular values.
    
    In summary, you can measure "how much" is preserved by selecting singular vectors of SVD by computing the ratio of the energy of the selected singular values to the total energy of the matrix. A higher ratio indicates more preserved information, while a lower ratio suggests more loss of information.
    
- why svd over pca? why pca over svd?
    
    PCA is primarily used for dimensionality reduction and feature extraction. It aims to find a lower-dimensional representation of the data that preserves the maximum amount of variance. By projecting the data onto a new set of orthogonal axes (principal components), PCA allows for a compact representation of the data while retaining most of the important information. PCA achieves this by diagonalizing the covariance matrix of the data.
    
    On the other hand, SVD is a matrix factorization technique that decomposes a matrix into three separate matrices: U, Σ, and V. The matrix Σ contains singular values, which represent the importance of the corresponding columns of U and rows of V. SVD has numerous applications, including matrix approximation, image compression, and collaborative filtering.
    
    Reasons to choose SVD over PCA:
    
    1. Matrix factorization: SVD provides a general framework for matrix factorization, allowing you to uncover underlying patterns and structures in the data, which can be useful in various domains.
    2. Sparse data: SVD can handle sparse data efficiently, whereas PCA is primarily designed for dense data.
    
    Reasons to choose PCA over SVD:
    
    1. Dimensionality reduction: PCA is specifically designed for dimensionality reduction, finding the most important features/components that capture most of the data variance.
    2. Ease of use: PCA is a well-established technique, and many libraries and software packages provide built-in implementations for PCA. It is generally easier to implement and apply compared to SVD.
    
    In practice, there is an inherent connection between PCA and SVD. PCA can be seen as a specific application of SVD, where the covariance matrix is used instead of the data matrix itself. So, while there are some differences between the two techniques, they also share common ground, and the choice between them depends on the specific problem and requirements at hand.
    

[https://www.youtube.com/watch?v=vSczTbgc8Rc&t=163s&ab_channel=VisualKernel](https://www.youtube.com/watch?v=vSczTbgc8Rc&t=163s&ab_channel=VisualKernel)

**SVD Visualized, Singular Value Decomposition explained | SEE Matrix , Chapter 3**

q x v matrix: maps vectors from R^v to R^q

$AA^T$ is always square-symmetric, even if A isn’t. So is $A^TA$

The sqrt of the eigenvalues of the left and right matrices are the singular values

L and R have equal eigenvalues (when ranked); the leftover ones (since q > v when rectangular) are 0

The eigenvectors of L are U; the eigenvectors of R are V.

U: rotate right singular vector to basis

$\sigma$ : dimension eraser (q to v) then scale

V: rotate basis to left singular vector 

- why does multiply by eigenvector matrix only rotate?
    
    Multiplying a matrix by an eigenvector matrix does not always result in a rotation. The effect of multiplying a matrix by an eigenvector matrix depends on the specific matrix and eigenvectors involved.
    
    To understand this, let's consider the general case of a square matrix A and its eigenvector matrix V, where V contains the eigenvectors of A as its columns. The eigenvector matrix V is orthogonal, meaning its columns are mutually perpendicular unit vectors.
    
    When you multiply A by V, you get a new matrix AV. The columns of AV are the result of applying the linear transformation represented by A to each column of V.
    
    If A has real eigenvalues, the action of AV on each column of V is a scaling operation. Each eigenvector is scaled by its corresponding eigenvalue. In this case, AV does not result in a rotation but rather a stretching or compression of the eigenvectors along their directions.
    
    However, if A has complex eigenvalues, the action of AV on each column of V involves a combination of scaling and rotation. The complex eigenvalues introduce complex factors that cause a rotation in addition to the scaling. In this case, AV can result in a rotation and scaling of the eigenvectors.
    
    So, whether multiplying a matrix by an eigenvector matrix only results in a rotation or involves other transformations depends on the eigenvalues of the matrix. If the eigenvalues are real, it results in stretching or compression. If the eigenvalues are complex, it involves a rotation in addition to scaling.
    

13m38s

Take row of U, col of sigma, col of V to see why same as A (element-wise vars)

12m: Can also go from lower dim to higher dim

---

[https://gregorygundersen.com/blog/2018/12/10/svd/](https://gregorygundersen.com/blog/2018/12/10/svd/)
The singular values referred to in the name “singular value decomposition” are simply the length and width of the transformed square.
The eigenvectors of right and left AA are the length and width directions of the transformed square.

That’s why multiplying by right and left eigenvectors then scaling by singular values gets the A transformation; the A transformation is a transformed square, so the length and width of A are its right and left eigenvectors.

When we decompose by SVD, we are decomposing that square into its length and width variables. The (singular) eigenvectors say which directions the square points in, and the (singular) eigenvalues say how big the square’s length and width (and thus area) are.

The reason we use eigenvectors as length and width is that they don’t change direction, but scale by their eigenvalues. Note that EVERY OTHER vector except the ones shown below change upon multiplication by M:

![Untitled](SVD%20b6e01b133b7d495b81236acafc3cea9b/Untitled.png)

Not every matrix M has eigenvectors. But MM has eigenvectors. But shouldn’t multiplying by MM’s eigenvectors get MM, not M? 

![Untitled](SVD%20b6e01b133b7d495b81236acafc3cea9b/Untitled%201.png)

<<<

v_i is put here twice: as the basis vector, and as the term in x*v

Each basis vector M*v_i can be rewritten as u*sigma*v_i

---

[http://www.ams.org/publicoutreach/feature-column/fcarc-svd](http://www.ams.org/publicoutreach/feature-column/fcarc-svd)

---

Start with just A=USV b/c that’s the desired form. We don’t know what kind of vectors are in U yet. Then, we do AA^T and find U are eigenvectors of AA^T.

<<<

Right singular onto basis
Dim erase and scale
Basis onto Left singular

Right singular are eignvector of u, which is symmetric

Lambda u = Aa u = Av
Au = v

![Untitled](SVD%20b6e01b133b7d495b81236acafc3cea9b/Untitled%202.png)

From dtrang geom fig, if av, then v right singular is basis. When already on basis, just stretch and rotate. U is Orth rotate so no need any other thing like skew? Or is ksew just rote and str. It's not, reqs angle change

V is not originally the basis. It just means there exists some vector in X which will always be just scaled and rotated even if dims in Y are diff. If dims are the same, there will always be vectors that are just scaled.

V are Orthogonal to each other, not necc to manifold. Tangent sp is Orth to manifold

Now jacobian is change from basis to dir.

<<<

SVD expalnation outline

Why use eigenvectors?

- It can approximate the matrix by taking the eigenvectors with the biggest eigenvalue
    1. Understanding linear transformations: The eigenvectors of a linear transformation represent the directions along which the transformation only stretches or shrinks the vectors without changing their direction. The corresponding eigenvalues indicate the scale factor by which the vectors are stretched or shrunk along those directions.
        1. This means that if we project a vector v onto the eigenvector, it says how much the vector v is stretched in that direction?
    2. Diagonalization: is the process of expressing a matrix as a diagonal matrix using a similarity transformation. Eigenvectors are used to form the diagonalizing matrix, allowing us to transform a given matrix into a diagonal form, which simplifies many calculations and analysis tasks.
    3. Solving systems of linear equations: Eigenvectors are valuable when solving systems of linear equations. If we represent a system of linear equations using matrices, finding the eigenvectors and eigenvalues of the coefficient matrix can help us understand the behavior of the system. Moreover, eigenvectors can be used to find particular solutions for systems of linear differential equations, making them relevant in many areas of science and engineering.
    4. Principal component analysis (PCA): Eigenvectors play a central role in PCA, a widely used dimensionality reduction technique. PCA aims to find a lower-dimensional representation of a dataset while preserving its essential structure. By computing the eigenvectors and eigenvalues of the covariance matrix of the data, PCA identifies the principal components (eigenvectors) that capture the most significant variations in the dataset. These principal components can then be used for visualization, data compression, or feature selection.
    5. Stability analysis: Eigenvectors and eigenvalues are used to study the stability of dynamic systems. In the context of linear systems, the eigenvalues of the system matrix determine the stability properties of the system. Stable systems have eigenvalues with negative real parts, indicating that disturbances or perturbations will diminish over time. On the other hand, eigenvalues with positive real parts indicate instability or divergence. Eigenvectors associated with unstable eigenvalues provide insight into the directions in which the system diverges.
    6. Spectral analysis: Eigenvectors are utilized in spectral analysis, which involves decomposing signals or functions into their constituent frequencies or eigenfunctions. The eigenvalues represent the frequencies or eigenvalues associated with each eigenvector, allowing us to analyze the frequency content or spatial characteristics of signals or functions. Spectral analysis has applications in signal processing, image processing, quantum mechanics, and many other areas.
    
    These are just a few examples of why eigenvectors are essential and widely used. The ability to approximate a matrix by selecting eigenvectors with the largest eigenvalues, as you mentioned, can be particularly useful for dimensionality reduction, data compression, and identifying dominant patterns or features in the data.
    

How are the eigenvectors able to add up to the matrix?

because they’re orthogonal

If we have a rectangular matrix and don’t have eigenvectors, what do we do?

use singular values

- Why use SVD?
    1. **Data compression and Image processing:** SVD can be used to reduce the dimensionality of data, which can be useful in both data compression and noise reduction. This is done by setting the smallest singular values to zero, effectively reducing the rank of the matrix and simplifying the data.
    2. **Latent Semantic Analysis (LSA):** In natural language processing, SVD is used in LSA for the purpose of document classification, information retrieval, and detecting latent semantic structures in text data.
    3. **Machine Learning:** SVD is used in Principal Component Analysis (PCA), a popular dimensionality reduction technique. PCA is useful when working with datasets with a large number of variables, as it allows you to simplify the data while preserving its structure.
    4. **Numerical Stability:** In numerical linear algebra, SVD is a stable way to solve systems of linear equations, invert matrices, and compute matrix ranks.
    5. **Recommendation Systems:** SVD is used in collaborative filtering, which forms the basis of many recommendation systems (like those used by Netflix and Amazon).
    6. **Signal Processing:** SVD is used to separate mixed signals in array processing.
    7. **Data Imputation:** SVD can be used to estimate missing values in a dataset, based on the values in the rest of the dataset.
    
    In general, SVD is a powerful technique that provides a way to identify the fundamental elements of a matrix, and can be a useful tool for understanding complex high-dimensional data.
    
- How are SVD and fourier similar?
    1. **Decomposition into simpler, basic components:** SVD decomposes a matrix into singular vectors and singular values, while the Fourier Transform decomposes a signal into sine and cosine waves of different frequencies.
    2. **Frequency Analysis:** Both can be used for frequency analysis. The Fourier Transform directly gives the amplitude of different frequencies in a signal. SVD can also be used for frequency analysis in a certain sense, by revealing patterns in a matrix that occur on different "scales". This is more abstract than the frequency analysis of the Fourier Transform, but there is a rough parallel.
    3. **Signal Processing and Data Reduction:** Both SVD and Fourier Transform can be used for signal processing tasks, such as filtering and data compression. In both cases, we can throw away certain components (small singular values for SVD, high-frequency components for the Fourier Transform) to reduce the size of the data or to focus on the most important features.
    4. **Change of Basis:** Both SVD and Fourier Transform can be seen as a change of basis. In the case of SVD, we change the basis to the singular vectors, while in the Fourier Transform, we change the basis to sine and cosine functions.
    
    Despite these similarities, the SVD and Fourier Transform are used in different contexts and have different mathematical underpinnings. The Fourier Transform is specifically designed for analyzing time-dependent signals and functions, while SVD is a more general technique for decomposing and analyzing matrices.
    

- Does every matrix have singular vectors which just scale and rotate upon transformation?
    
    Yes, every matrix has what are called singular vectors, which play an important role in the singular value decomposition (SVD) of the matrix. The SVD of a matrix A is a factorization of the form A = UΣVᵀ, where U and V are orthogonal matrices (their columns are the left and right singular vectors, respectively), and Σ is a diagonal matrix (its diagonal elements are the singular values).
    
    Now, let's clarify what happens when you multiply a vector by a matrix:
    
    - Rotation: In a transformation represented by a matrix, the rotation happens when the direction of a vector changes. The rotation does not affect the length of the vector.
    - Scaling: Scaling happens when the length of the vector changes. In this case, the direction of the vector does not change.
    
    So, to say that singular vectors "just scale and rotate upon transformation" is partially correct.
    
    When you multiply a singular vector v (a right singular vector) by the matrix A, you get a scaled version of the corresponding left singular vector u. The scaling factor is the singular value associated with v. This operation can be seen as a rotation (from the direction of v to the direction of u) followed by a scaling. However, it's important to note that the resulting vector doesn't generally have the same direction as the original singular vector v, unless A is a scalar multiple of the identity matrix.
    
    If A is a symmetric positive definite matrix, then the singular vectors are also eigenvectors, and these do indeed just scale upon transformation, without rotating. But in the general case, singular vectors do not maintain their direction under the transformation represented by the matrix.
    
- Does every right singular vector have a left singular vector which is just a rotation or collapse of it?
    
    The right singular vectors and left singular vectors are part of the singular value decomposition (SVD) of a matrix. The SVD of a matrix A can be written as A = UΣVᵀ. Here, the columns of U are the left singular vectors, the columns of V are the right singular vectors, and Σ is a diagonal matrix containing the singular values. The vectors in U and V are orthonormal, meaning that they are orthogonal (at right angles to each other) and of unit length.
    
    When you multiply a right singular vector v by the matrix A, you get a scaled version of the corresponding left singular vector u. The scaling factor is the singular value associated with v.
    
    However, it is generally incorrect to say that each left singular vector is just a "rotation" or "collapse" of the corresponding right singular vector. The vectors in U and V are defined independently of each other (though they are related through A and the singular values), and there's no guarantee that the left singular vector corresponding to a given right singular vector will look like a "rotation" or "collapse" of that right singular vector.
    
    In other words, when you multiply the matrix A by a right singular vector, you get a vector in the direction of the corresponding left singular vector, but it might not be in the same direction as the right singular vector. This transformation could involve a complex combination of rotation, scaling, and possibly other operations, depending on the properties of the matrix A.
    
- Why not, if Av = sigma*u?
    
    You're correct that if you multiply a matrix A with a right singular vector v, you get Av = σu, where σ is a singular value and u is the corresponding left singular vector. However, when we say that a vector undergoes a "rotation", it implies that the vector remains in the same subspace, but merely changes direction. When we say a vector undergoes a "scaling", it means the vector changes its magnitude but not its direction.
    
    In the context of SVD, the right singular vectors v form a basis for the domain, and the left singular vectors u form a basis for the codomain. For any right singular vector v, Av = σu implies that the vector v is mapped to a new vector in the codomain, which is a scaled version of the corresponding left singular vector u. The transformation involves scaling (by σ) and possibly a change of basis (from the domain to the codomain).
    
    However, the result u is not typically in the same direction as v (unless A has some special properties, like being a multiple of the identity), so it's not accurate to describe this as simply a rotation or scaling of the original vector v within its original space. The transformed vector has moved into a new space (the codomain), which might have a different orientation compared to the original space (the domain).
    
    So, while there's certainly a close relationship between the right singular vectors, the left singular vectors, and the singular values, it's more complex than just saying that each left singular vector is a rotation or collapse of the corresponding right singular vector.
    
- Are orthogonal matrices always rotations?
    
    Orthogonal matrices represent transformations that are a combination of rotation and reflection.
    
    In more detail:
    
    1. Rotation: An orthogonal matrix with a determinant of +1 represents a rotation. The magnitude of the rotation angle can be determined from the trace of the matrix (the sum of the diagonal elements), and the axis of rotation can be determined from the eigenvectors of the matrix.
    2. Reflection: An orthogonal matrix with a determinant of -1 represents a reflection. The plane (or line, in 2D) of reflection can be determined from the eigenvectors of the matrix.
    
    So, not all orthogonal matrices represent pure rotations; they could also represent reflections, or a combination of rotation and reflection. But they do all preserve the lengths of vectors and the angles between vectors, which makes them extremely important in many areas of mathematics and physics.
    
- Are U and V orthogonal?
    
    Yes, in the context of singular value decomposition (SVD), the matrices U and V are orthogonal. This means that the columns of U and V are all unit vectors (have a magnitude of 1) and are pairwise orthogonal (each pair of different vectors is perpendicular).
    
    More formally, an orthogonal matrix has the property that its transpose is also its inverse. For a matrix to be orthogonal, it must satisfy the condition that UU^T = I and VV^T = I, where U^T and V^T are the transposes of U and V, respectively, and I is the identity matrix.
    
    In addition to being orthogonal, the columns of U (the left singular vectors) form an orthonormal basis for the range of the original matrix, and the columns of V (the right singular vectors) form an orthonormal basis for the domain of the original matrix.
    
    So, in SVD, not only are U and V orthogonal matrices, but their column vectors also have important geometric interpretations.
    
- So U*v, where v is a basis vector of V, means rotating or reflecting v, but not skewing?
    
    Not exactly, because U and V operate in different spaces. Let's clarify this a bit more:
    
    In the context of singular value decomposition (SVD), the matrix V contains the right singular vectors of the original matrix A, and U contains the left singular vectors. These vectors form bases for their respective vector spaces. The right singular vectors v_i form a basis for the domain of A, and the left singular vectors u_i form a basis for the range (or codomain) of A.
    
    If we take a vector v from V (a right singular vector), it exists in the domain of A. If we multiply U by this vector (U*v), we are essentially applying a transformation in the range of A to the vector v. The product U*v is generally not meaningful because U and v operate in different spaces (the codomain and domain of A, respectively).
    
    So, even though U and V are orthogonal matrices and thus represent rotations or reflections in their own spaces, it doesn't make sense to multiply U by a column of V (or vice versa) and think of the result as simply a rotation, reflection, or any other kind of transformation of the original vector. These operations are meaningful in the context of the original matrix A and the transformation it represents, but not directly between U and V.
    
    In the SVD, you might see the product of U and V in the full decomposition A = UΣVᵀ, where Σ is a diagonal matrix containing the singular values, but this is a different context. Here, you're not multiplying U by a column of V directly; instead, you're forming a product of three matrices that gives you back the original matrix A.
    
- So U*v, where v is a basis vector of V^T, means rotating or reflecting v, but not skewing?
    
    Yes, in that context, you are correct. If V is an orthogonal matrix, then its rows (or the columns of its transpose, V^T) form an orthonormal basis. If v is a basis vector from the set of rows of V (or columns of V^T), then multiplying U by v (as in U*v) will be a linear transformation that includes rotation, reflection, or both, but not skewing or scaling, because orthogonal transformations preserve lengths (they are isometries).
    
    However, note that while the above operation is mathematically valid, it doesn't have a standard interpretation in terms of the singular value decomposition (SVD) of a matrix. In SVD, the orthogonal matrix U operates in the range (or codomain) of the original matrix, and V (or its transpose, V^T) operates in the domain. So multiplying U by a vector from V^T isn't a standard operation in the context of SVD.
    
    But yes, if you're thinking of U and V simply as orthogonal matrices and v as a vector that you're transforming, then U*v represents an isometry of v - a transformation that includes rotation and reflection but preserves the length of v.
    
- Do U and V have the same rank?
    
    In the context of the Singular Value Decomposition (SVD) of a matrix, the matrices U and V are both square and have the same order as their respective spaces. If we decompose a matrix A of size m x n into A = UΣV^T, then:
    
    - U is an m x m matrix, where m is the number of rows in A. The columns of U form an orthonormal basis for the range (or codomain) of A.
    - V is an n x n matrix, where n is the number of columns in A. The columns of V form an orthonormal basis for the domain of A.
    
    Therefore, U and V are full rank for their respective spaces, but they may not be the same size or have the same rank if A is not a square matrix. If A is a square matrix (m=n), then yes, U and V would have the same size and rank.
    
    Σ, the middle diagonal matrix, is an m x n matrix. Its non-zero diagonal entries are the singular values of A, which tell you how much stretching or compression occurs along each dimension. The number of non-zero singular values is equal to the rank of A.
    
    It's worth noting that there are also reduced forms of the SVD where U and V are not square matrices but have fewer columns, corresponding to the rank of A. In these reduced forms, U and V do have the same number of columns, and this number is equal to the rank of A.
    
- Does every right singular vector with non-zero singular value have a left singular vector?
    
    Yes. Each singular value on the diagonal of Σ is associated with one right singular vector (a column of V) and one left singular vector (a column of U). If the singular value is non-zero, it means that the associated right and left singular vectors correspond to a "direction" in which the matrix A acts as a scaling (but not a rotation).
    
- Does AA^T * u = lambda * u?
    
    Yes, the equation $AA^T * u = λ * u$ is correct for a certain u and λ, specifically for a left singular vector u and its associated squared singular value λ.
    
    It's known that $AA^T = UΣ^2U^T$
    
    This shows that the left singular vectors of A (the columns of U) are eigenvectors of AA^T, and the corresponding eigenvalues are the squares of the singular values of A (the entries of Σ^2).
    
    So, if u is a left singular vector of A and λ is the square of the corresponding singular value, then indeed AA^T * u = λ * u.
    
    Remember that for a square matrix B and a vector x, the equation B * x = λ * x says that x is an eigenvector of B with corresponding eigenvalue λ.
    
- does sigma * u = A*v?
- So does AA^T * u / sigma = lambda  / sigma * u = A*v / sigma ?
    
    I'm afraid there's a bit of confusion here. Here's the correct relationships in the context of singular value decomposition (SVD):
    
    The equation A*v_i = σ_i * u_i states that if you apply the matrix A to the right singular vector v_i, you obtain the left singular vector u_i scaled by the corresponding singular value σ_i.
    
    The relationship between the matrix A, its transpose A^T, and the left singular vectors u_i is given by the equation $AA^T * u_i = σ_i^2 * u_i$. This equation is derived from the properties of SVD, and it says that the left singular vectors u_i are eigenvectors of the matrix AA^T, and the corresponding eigenvalues are the squares of the singular values σ_i.
    
    If you divide both sides of the equation $AA^T * u_i = σ_i^2 * u_i$ by σ_i (assuming σ_i ≠ 0), you'd get $AA^T * u_i / σ_i = σ_i * u_i$, not A * v_i / σ_i. The term on the left is a scalar times a left singular vector, and the term on the right is a left singular vector scaled by a singular value. There's no direct relationship with the right singular vectors v_i in this equation.
    
    So, to summarize: while AA^T * u_i = σ_i^2 * u_i and A * v_i = σ_i * u_i are both true relationships in the context of SVD, dividing these equations through by σ_i doesn't give you an equation relating u_i and v_i in the way that you suggested.
    
- does A^T * u = v?
    
    In the context of SVD, the relationship between A, U, and V is typically expressed as follows:
    
    A * v_i = σ_i * u_i
    
    A^T * u_i = σ_i * v_i
    

[https://www.youtube.com/watch?v=mhy-ZKSARxI&t=471s&ab_channel=VisualKernel](https://www.youtube.com/watch?v=mhy-ZKSARxI&t=471s&ab_channel=VisualKernel)

**Visualize Spectral Decomposition | SEE Matrix, Chapter 2**

[https://www.sjsu.edu/faculty/guangliang.chen/Math253S20/lec5svd.pdf](https://www.sjsu.edu/faculty/guangliang.chen/Math253S20/lec5svd.pdf)

<<<

algebraically solve A and A^T A, and also visually plot them. Is there a pattern for all A?

also do this for singular vectors and eigenvectors. pattern?

finally, plug in values for basis dims (eg. nap) and see how they cause diff “change in units” algebraically and geometrically. interpret the resulting units

eigenvector: just stretched

singular: stretched then rotated

Av = sigma * u

A^T A v = A^T sigma * u 

A^T A v = lambda * v ?= v

- Does A^A A = identity?
    
    No, in general, the product of a matrix A with its transpose A^T (or A^A) does not result in the identity matrix, unless A is an orthogonal matrix.
    
    If A is an orthogonal matrix, then A^T = A^(-1), where A^(-1) is the inverse of A. In this case, we have:
    
    A^T * A = A^(-1) * A = I,
    
    where I represents the identity matrix.
    
    However, for a general matrix A, the product A^T * A does not necessarily equal the identity matrix. The resulting matrix will depend on the specific properties and structure of matrix A.
    

A^T sigma * u = lambda * v = sigma * sigma * v

A^T u = sigma v

A A^ T u **=** lambda * u = A sigma v

A v = sigma u (back to where we started)

A^T is not always a rotation b/c A is not always orthogonal

So what does A^T do to sigma * u? It causes it to equal lambda * v

sigma * u: stretch u

lambda * v: stretch v MORE (2x amount of sigma)

A^T A v = A^T sigma * u = lambda * v

A A^ T u **=** A sigma v = lambda * u

Multiplying by A^T or A causes eigenvector to rotate and scale into singular vctor

Why does every square mat have (real or complex) eigenvector? Proof

- prove every square symmetric has real eigenvector
    
    To prove that every square symmetric matrix has real eigenvectors, we can use the Spectral Theorem, which states that every symmetric matrix is orthogonally diagonalizable.
    
    Let A be a square symmetric matrix. By the Spectral Theorem, there exists an orthogonal matrix P such that P^T * A * P = D, where D is a diagonal matrix with the eigenvalues of A on its diagonal.
    
    Let's consider an eigenvector x of A with eigenvalue λ. This means that Ax = λx. We can express x in terms of the columns of P as x = P * y, where y is a vector.
    
    Substituting this expression into the eigenvector equation, we have:
    
    A(P * y) = λ(P * y).
    
    Multiplying both sides by P^T from the left, we get:
    
    P^T * A * (P * y) = λ(P^T * P * y).
    
    Since P is an orthogonal matrix, P^T * P = I (the identity matrix). Therefore, the equation becomes:
    
    P^T * A * P * y = λI * y,
    
    which simplifies to:
    
    D * y = λy.
    
    Here, D is a diagonal matrix with the eigenvalues of A on its diagonal. We can see that multiplying y by D simply scales the vector y by the eigenvalues. Since D is a diagonal matrix, the scaling factor λ applies independently to each component of y.
    
    Therefore, we have shown that the eigenvector y (and hence x = P * y) is a real vector, as it is not affected by any complex scaling factors. Since x is expressed in terms of the columns of the orthogonal matrix P, which are real vectors, x itself must be a real vector.
    
    Hence, every square symmetric matrix has real eigenvectors.
    

[https://brilliant.org/wiki/spectral-theorem/](https://brilliant.org/wiki/spectral-theorem/)

<<<

the eigenvectors are linear combos of basis, which have interpretation. so the ratio of the basis features describe what eigenvectors represent.

Eg) if eigenvector is 0.8 body and 0.3 face, that’s “more cat like”.

Thus, this is a new feature that doesn’t rely on body and face, but more on the ratio, to describe the matrix. Just keeping this ratio while discarding all other considerations (other combinations of basis features) is enough.

Now, this is intuitive when A’s basis are “interpretable”. But A^T * A elements are a combination of these units, so may not be. We can try to input them into chatgpt to see if it finds ones that fit.

- Let A = [a b, c d]. What are the values of A^T * A? express in latex
    
    $A^T * A = \begin{bmatrix}
    a & c \\
    b & d \\
    \end{bmatrix} * \begin{bmatrix}
    a & b \\
    c & d \\
    \end{bmatrix}  = \begin{bmatrix}
    a^2 + c^2 & ab + cd \\
    ab + cd & b^2 + d^2 \\
    \end{bmatrix}$
    
- Let a = nap/nose, b = nap/ear ; c = luck/nose, d = luck/ear. Substitute these values into the following:
    
    Substituting the given values into the expression:
    
    $A^T * A = \begin{bmatrix}
    \frac{nap}{nose} & \frac{luck}{nose} \\
    \frac{nap}{ear} & \frac{luck}{ear} \\
    \end{bmatrix} * \begin{bmatrix}
    \frac{nap}{nose} & \frac{nap}{ear} \\
    \frac{luck}{nose} & \frac{luck}{ear} \\
    \end{bmatrix} = \begin{bmatrix}
    \left(\frac{nap}{nose}\right)^2 + \left(\frac{luck}{nose}\right)^2 & \left(\frac{nap}{nose}\right)\left(\frac{nap}{ear}\right) + \left(\frac{luck}{nose}\right)\left(\frac{luck}{ear}\right) \\
    \left(\frac{nap}{nose}\right)\left(\frac{nap}{ear}\right) + \left(\frac{luck}{nose}\right)\left(\frac{luck}{ear}\right) & \left(\frac{nap}{ear}\right)^2 + \left(\frac{luck}{ear}\right)^2 \\
    \end{bmatrix}$
    
    Simplifying the expression further, we have:
    
    $A^T * A = \begin{bmatrix}
    \left(\frac{nap^2}{nose^2}\right) + \left(\frac{luck^2}{nose^2}\right) & \left(\frac{nap}{nose}\right)\left(\frac{nap}{ear}\right) + \left(\frac{luck}{nose}\right)\left(\frac{luck}{ear}\right) \\
    \left(\frac{nap}{nose}\right)\left(\frac{nap}{ear}\right) + \left(\frac{luck}{nose}\right)\left(\frac{luck}{ear}\right) & \left(\frac{nap^2}{ear^2}\right) + \left(\frac{luck^2}{ear^2}\right) \\
    \end{bmatrix}$
    
    if Ax get nap and luck as new axis, then A^T Ax should have nap and luck as denominators. (nap, luck) is in each row. But what’s numberators? No one knows until after, b/c interpretation is human subjective measured. It’s not absolute. We are guessing they mean nap and luck b/c they correlate with nap and luck. If they correlate with other things that are analogous rise/falls with nap and luck, we can interpret them as those, too. These ratios are NOT inherent to the matrix, which is just a collection of values. Secondly, this is for demo purposes and shouldn’t be extended outside of it. It’s like labeling a target with red tape to see it better during training, the red tape is not going to be part of the wild when you’re hunting with a bow.
    
- Find dimensions of a, b, c, d corresponding to real world values that "make sense" when substituted into A^T * A. For example, a= length, b=color, etc.
    
    [fails]
    

If we treat first row of A^T A as how previous basis compute first new basis vec, then clearly the first row (basis vec) Is nap^2 + luck^2. But unlike when just Ax, A^T Ax uses nose^2 and nose*ear as its previous basis! This also doesn’t make sense because after Ax, those basis vectors should be nap and luck. 

I suppose it only makes sense once you project nap onto those new dims (elements of A^T A), then add them to get the basis elems of A^T A.

Actually this made a mistake; A^T A units don’t act on Ax, so nap and luck shouldn’t be the prev basis vectors. A^T A still acts on x, so nose and ear are still the basis vectors.

What doesn’t make sense is that both basis vectors (both rows) are nap^2 + luck^2, but calculated in 2 different ways (ratios of prev basis). In fact, the mirrored diagonal is the same (nose * ear) while the diagonal is diff (nose^2 vs ear^2 in denominator).

In this case, we must change our perspective if we believe the original basis was ALWAYS “nose” and “ear”- it’s not. It’s ENTIRELY RELATIVE to the matrix! That’s the main lesson in one of the sections of the “why NNs use LA” video. If the matrix was about using “red and blue”, the original wouldn’t be “nose and ear”. So in this case, A^T A ISN’T using nose and ear, but nose^2 and nose*ear for the first, then an entirely different one for the second row!

Yet, the value used for nose^2 and nose*ear is the same (x_1). This is stating that the ratios used to calculate the two are the same in the matrix, despite interpreting as different units.

But if they’re not the same, that is- relative ot the matrix- how can we “carry over” the units upon A^T A? 

Make a separate video for this; don’t put it into your entry for SoME3. Put it as a “quick PSA” that the Some3 links to. This is b/c too much detail, and too controvserial. “Still under investigation” by Yoneda corp. This video doesn’t need geom (besides repeating prev video), just show algebra and “real world ex” units substi in.

This makes sense, still, if instead of substituing nap and etc, we keep a b c d and look at the elemtsn of A^T A. “Don’t do that just yet”. Keep it

But if we allow x_1 and x_2 to be diff units for each row, it no longer makes sense to interpret the denoms as x_1 and x_2. I proporse this instead:

$A^T * A = \begin{bmatrix}
a & c \\
b & d \\
\end{bmatrix} * \begin{bmatrix}
a & b \\
c & d \\
\end{bmatrix}  -> \begin{bmatrix}
\frac{a^2 + c^2}{x_1} & \frac{ab + cd}{x_2} \\
\frac{ab + cd}{x_1} & \frac{b^2 + d^2}{x_2} \\
\end{bmatrix}$

Thus, first row is : $a^2 + c^2 + ab +cd$

Thus, 2nd row is : $b^2 + d^2 + ab +cd$

The ratio units ONLY make sense during MM; they are not inherent to the matrix themselves. 

- Let a = nap/nose, b = nap/ear ; c = luck/nose, d = luck/ear. Substitute these into A * A^T
    
    $A * A^T = \begin{bmatrix}
    \frac{nap}{nose} & \frac{nap}{ear} \\
    \frac{luck}{nose} & \frac{luck}{ear} \\
    \end{bmatrix} * \begin{bmatrix}
    \frac{nap}{nose} & \frac{luck}{nose} \\
    \frac{nap}{ear} & \frac{luck}{ear} \\
    \end{bmatrix} = \begin{bmatrix}
    \left(\frac{nap}{nose}\right)^2 + \left(\frac{nap}{ear}\right)^2 & \left(\frac{nap}{nose}\right)\left(\frac{luck}{nose}\right) + \left(\frac{nap}{ear}\right)\left(\frac{luck}{ear}\right) \\
    \left(\frac{luck}{nose}\right)\left(\frac{nap}{nose}\right) + \left(\frac{luck}{ear}\right)\left(\frac{nap}{ear}\right) & \left(\frac{luck}{nose}\right)^2 + \left(\frac{luck}{ear}\right)^2 \\
    \end{bmatrix}$
    
    Simplify:
    
    $A * A^T = \begin{bmatrix}
    \frac{nap^2}{nose^2} + \frac{nap^2}{ear^2} & \frac{nap \cdot luck}{nose^2} + \frac{nap \cdot luck}{ear^2} \\
    \frac{nap \cdot luck}{nose^2} + \frac{nap \cdot luck}{ear^2} & \frac{luck^2}{nose^2} + \frac{luck^2}{ear^2} \\
    \end{bmatrix}$
    

Propagate ratio units from A to A^T A to eigenvector of A^T A. Show how these, in the end, reconstruct the units for A using USV. This will describe what U and V are doing to “make up” A. And why truncate are most impt.

<<<<

if det is area, then the daigonal values created L and W? then for 3D det…