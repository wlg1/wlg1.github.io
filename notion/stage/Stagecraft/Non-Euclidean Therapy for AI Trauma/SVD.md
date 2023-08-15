# SVD

[https://chat.openai.com/c/38e90e84-9556-4cb7-9c0c-afaecadc9c09](https://chat.openai.com/c/38e90e84-9556-4cb7-9c0c-afaecadc9c09)

[https://www.notion.so/wlg1/SVD-b6e01b133b7d495b81236acafc3cea9b](https://www.notion.so/SVD-b6e01b133b7d495b81236acafc3cea9b?pvs=21)

Eigenvalues ax = x
Svd av = u
Includes rotation, not just scaling
Orth to Orth, tangent to tangent

AA D AA

U D V = AAU AAV

rotate to A^T A, scale squared, rotate to AA^T

A^T A A A^T = I (?) - no; it rmvs or adds dim from m to n

u and v are squrae. v has same dims as input x (n). 

only D has n x m

U is output directions, so eigenvectors of output space (that’s where it finally lands; right sing from basis onto left sing)

V is input directions, but we must rotate to them first. B/c V^T, the right singular are rotated to basis; now input dirs are on basis.6

- Animate A^T A v = v
    - vs A^T A v = A^T u = v
    - when adding A^T to both side of Av = u
    - Why does this A^T align u with v?
    - Alice asks these questions to the Eigenface, but gets no answers
    - There is so much more you not yet know (for you to learn)

- SVD J: change in input v, change in output u
- [https://chat.openai.com/c/b73225b9-7c1d-4f62-b262-e98614dd3e16](https://chat.openai.com/c/b73225b9-7c1d-4f62-b262-e98614dd3e16)
- [https://chat.openai.com/c/53e0fec1-d46e-4a88-870b-180e0a5ba3db](https://chat.openai.com/c/53e0fec1-d46e-4a88-870b-180e0a5ba3db)
- [https://chat.openai.com/c/7a8b6ef1-34a6-4402-a35a-7b0b9d57d713](https://chat.openai.com/c/7a8b6ef1-34a6-4402-a35a-7b0b9d57d713)
- [https://towardsdatascience.com/eigenfaces-recovering-humans-from-ghosts-17606c328184](https://towardsdatascience.com/eigenfaces-recovering-humans-from-ghosts-17606c328184)

[https://www.perfectlynormal.co.uk/blog-svd#6A__Principal_Component_Analysis](https://www.perfectlynormal.co.uk/blog-svd#6A__Principal_Component_Analysis)

For instance, if we take the first few columns of U (the "output directions") and reshape them into images of shape (width, height), then we get the "eigenvectors [8] of our images".

---

Rotate right v to left u. But they won't be on basis at end.

When you multiply �A by a right singular vector �v, the result is a vector that's a scaled version of the corresponding left singular vector �u.

It's a guarantee 

Orthogonal minimizes interference

The reason ���A T A is related to the covariance matrix is that it captures the pairwise dot products between features (columns) of the data. If the data matrix �A is centered (i.e., has zero mean for each feature), then ���A T A captures how each feature co-varies with every other feature, which is the essence of a covariance matrix. 

How each neuron varies with other neurons

How sensitive each neuron is to a small change in another neuron, ask gpt if this

How inputs vary with each other

How does changing one affect the other? How similar they are.

The basis vectors of a covariance matrix are its eigenvectors

In to out AAAA

Post-multiplication, the transformed vector in the latent space will have components that are more aligned with the main patterns of variation in the original data

![Screenshot_20230813_160008_Chrome.jpg](SVD%2028715ccee1ce43cf8ec421393a4be7c2/Screenshot_20230813_160008_Chrome.jpg)

1. Neurons Vary with each other WW

Inputs with inputs AtA col on out

Outputs with outputs

1. How mappings vary with each other

This covariance would measure how the rates of change in one dimension (variable) relate to the rates of change in another dimension. In terms of, sim

Describe it. Use the definitions. Madlibs. Analogies

How does changing how h1 varies with x1 change how h1 varies with x2?

1. Eigenvectors of cov are Orth, no interference with each other, max

Why no dir change is max? Bc already same interpretation in both spaces. All other vectors change interp? Same ratio.

For weights, their cov eigenvectors of input capture how inputs interfere and correlate with each other

Now, if cov, captures 

Each vec in terms of the eigenvec. Rotate vec in terms of eigenvec instead of in terms of basis, compare them. Relate this to how eigenvec preserves info after transforming by matrix

In our context, it indicates the primary trend in how height and weight vary together. If  v 1  has both positive x and y components, it means as height (x-axis) increases, weight (y-axis) generally also increases. They are both related by this.

By knowing one, you can derive mor3 of th3vother . So eigenvector is a big component in many, bc large eigenvalue for many other vectors (no wrong, eigenvalues isn't a weight ceoffi)c. Eigenvec of cov is reln BTW many

1. U = Av using proof

AAA row on out

1. Rotate scale rotate

No computational detail. ai just remembers the methods.

Add public github for script

Are eigenvectors expressing vectors in terms of least entanglement? Minimal correlation

Dreams mix up correlations. No organization.  Same with a fake world. Needs a better basis, less superificla correlation on wrong dims

https://reddit.com/r/math/s/wkXIIf5AJz

Parallel means no loss. Same sim

---

- The singular values of the Jacobian matrix correspond to the magnitudes of the gradients of the function, and the left-singular and right-singular matrices correspond to the directions of the gradients in the input and output spaces, respectively.
    - Does this mean from X to H, the left singular basis corresponds to d/dx1, d/dx2, etc?
        
        It seems there might be a slight misunderstanding in your interpretation. Let's break down the Jacobian, its singular value decomposition (SVD), and the relationship between singular values and singular vectors.
        
        The Jacobian matrix, \(J\), represents the linearization of a vector-valued function \(f: \mathbb{R}^n \rightarrow \mathbb{R}^m\) near a particular point. For an input \(x\) in \(\mathbb{R}^n\), \(J\) captures how small changes in each element of \(x\) (i.e., \(x_1, x_2, \ldots, x_n\)) cause changes in the output of the function \(f(x)\).
        
        The SVD of the Jacobian matrix is given by:
        \[ J = U \Sigma V^T \]
        
        Here:
        
        - \(U\) is the left-singular matrix, with its columns being the left-singular vectors.
        - \(\Sigma\) is a diagonal matrix with singular values on its diagonal.
        - \(V^T\) is the transposed right-singular matrix, with its rows being the right-singular vectors.
        
        The singular values in \(\Sigma\) represent the scaling factors of the Jacobian in the directions given by the singular vectors. A larger singular value implies that the function is stretching/compressing the input more in the corresponding direction.
        
        To your question:
        
        > Does this mean from X to H, the left singular basis corresponds to \(d/dx_1\), \(d/dx_2\), etc?
        > 
        
        No, it doesn't exactly mean this. The partial derivatives, \(d/dx_1, d/dx_2, \ldots, d/dx_n\), are the individual entries in the rows of the Jacobian. The singular values and vectors come into play when you perform the SVD on this Jacobian.
        
        The right-singular vectors \(V^T\) provide orthonormal directions in the input space. When you perturb the input in the direction of a right-singular vector, the output changes in the direction of the corresponding left-singular vector \(U\), scaled by the corresponding singular value.
        
        In simpler terms:
        
        - Right-singular vectors: Directions of maximum change in the input space.
        - Singular values: Magnitude of that change.
        - Left-singular vectors: Directions of the resulting change in the output space.
        
        The singular vectors do not directly correspond to the partial derivatives, but the SVD of the Jacobian gives you a way to understand the most "influential" directions of change for the function. (not the original basis)