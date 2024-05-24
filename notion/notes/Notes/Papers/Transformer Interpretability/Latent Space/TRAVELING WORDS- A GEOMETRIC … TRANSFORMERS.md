# TRAVELING WORDS- A GEOMETRIC … TRANSFORMERS

[https://github.com/santiag0m/traveling-words](https://github.com/santiag0m/traveling-words)

[https://openreview.net/forum?id=cSSHiLnjsJ](https://openreview.net/forum?id=cSSHiLnjsJ)

reject bc says layernorm from other paper

This goes a geometric interpretation of each component:

1. Layer norm constraints input vectors to (d-1) dim hypersphere (via projection then normalize)
    1. Found in: On the expressivity role of layernorm in transformers’ attention
    - The difference (x - mean) is orthogonal to normal vector, thus input vectors are projected onto hyperplane defined by normal vector. Why?
        
        The statement concerns the geometric interpretation of decision boundaries in machine learning, particularly in models like Support Vector Machines (SVMs) or in the context of linear regression. Let's delve into why the difference $x - \text{mean}$ is orthogonal to the normal vector of a hyperplane, and how this pertains to projecting input vectors onto the hyperplane defined by the normal vector.
        
        1. **Hyperplane Definition**: In an $n$-dimensional space, a hyperplane is an $(n-1)$-dimensional subspace that effectively divides the space into two halves. The equation of a hyperplane can be expressed as:
        $\mathbf{w} \cdot \mathbf{x} - b = 0$
        where $\mathbf{w}$ is the normal vector to the hyperplane, $\mathbf{x}$ is a point on the hyperplane, and $b$ is a scalar offset.
        2. **Orthogonality and the Normal Vector**: The normal vector $\mathbf{w}$ to a hyperplane is orthogonal (perpendicular) to any vector lying within the hyperplane. This orthogonality is a fundamental property that determines the orientation of the hyperplane in the space.
        3. **Projection and Orthogonality**: The assertion that the difference $x - \text{mean}$ is orthogonal to the normal vector $\mathbf{w}$ pertains to the projection of data points onto the hyperplane. Here's the significance:
            - The "mean" often signifies a specific point representing the average or center of mass of data points, or it might denote a specific reference point related to the model's decision boundary.
            - The difference $x - \text{mean}$ denotes a vector from this "mean" point to any given data point $$x$$.
            - For a point $$x$$ to be positioned on the hyperplane, the vector from the "mean" to $$x$$ must be orthogonal to the hyperplane's normal vector $$\mathbf{w}$$, as this ensures that $$x$$ maintains a constant distance from the hyperplane along the direction defined by $\mathbf{w}$.
        4. **Projection onto the Hyperplane**: In the context of SVMs or when defining decision boundaries, projecting input vectors onto the hyperplane involves identifying the component of the input vectors that aligns with the hyperplane. This process is crucial for minimizing the distance from the data points to the hyperplane, essential for maximizing the margin in SVMs, or finding the optimal fit in linear regression.
        5. **Geometric Interpretation**: The orthogonality condition guarantees that the separation margin (in SVMs) or the error (in regression) is minimized in the direction perpendicular to the hyperplane. This geometric constraint is key in identifying the optimal decision boundary or regression line that effectively separates the classes or fits the data points, respectively.
        
        In essence, the projection of input vectors onto a hyperplane, and the condition that $$x - \text{mean}$$ is orthogonal to the hyperplane's normal vector, are fundamental to understanding how linear models separate data or conform to data points. This orthogonality ensures that the hyperplane acts as an efficient decision boundary or regression line by minimizing distance or error in the direction determined by its normal vector.
        
    - is dot product of hyperplane and normal the scalar offset? what is scalar offset b?
        
        The scalar offset \(b\) in the equation of a hyperplane is not directly the dot product of the hyperplane and the normal vector but is closely related to how the hyperplane is positioned in the space. Let's clarify this with the standard equation for a hyperplane in an \(n\)-dimensional space, which is given by:
        
        $$
        \mathbf{w} \cdot \mathbf{x} - b = 0
        $$
        
        Here:
        
        - \(\mathbf{w}\) is the normal vector to the hyperplane, which determines the orientation of the hyperplane.
        - \(\mathbf{x}\) is any point on the hyperplane.
        - \(b\) is the scalar offset, which affects the hyperplane's position relative to the origin.
        
        The term \(\mathbf{w} \cdot \mathbf{x}\) represents the dot product between the normal vector \(\mathbf{w}\) and a point \(\mathbf{x}\) on the hyperplane. This dot product gives a scalar value that measures the projection of \(\mathbf{x}\) in the direction of \(\mathbf{w}\).
        
        The scalar offset \(b\) plays a critical role in defining the hyperplane's location in the vector space. It can be understood as the negative of the dot product between the normal vector \(\mathbf{w}\) and a specific point \(\mathbf{x}_0\) on the hyperplane when \(\mathbf{x}\) is at the origin, or in other terms, how far the hyperplane is from the origin along the direction of the normal vector. If you rearrange the hyperplane equation for \(b\), you get:
        
        $b = \mathbf{w} \cdot \mathbf{x}_0$
        
        where \(\mathbf{x}_0\) is a particular point on the hyperplane. This equation shows that \(b\) is equivalent to the dot product of the normal vector and a point on the hyperplane, indicating how \(b\) essentially shifts the hyperplane away from or towards the origin along the direction defined by \(\mathbf{w}\).
        
        In summary, the scalar offset \(b\) helps define the hyperplane's exact location in space by determining its distance from the origin in the direction of the normal vector. The dot product \(\mathbf{w} \cdot \mathbf{x}\) minus \(b\) equals zero ensures that for any point \(\mathbf{x}\) on the hyperplane, this condition holds, effectively defining the hyperplane's equation.
        
    - Note that projection of vector onto normal vector is different from proj of vec onto hyperplane. proj onto hyperplane is x - (proj onto normal) because this proj is orthogonal to
2. QK matrix is operation on hypersphere
3. OV matrix transforms from hypersphere back to input space
    1. found in: Transformer feed-forward layers are key-value memories