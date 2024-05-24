# PCA

PCA involves finding the eigenbasis of the covariance matrix of the dataset and projecting the data onto the principal components defined by the eigenvectors.

The eigenvalues of the covariance matrix represent the amount of variation captured by each eigenvector, and they provide a way to rank the importance of the different directions of variation.

- Is the eigenbasis used in PCA because only the linearly independent vectors matter, not the ones sent to the 0th vector?
    
    Yes, PCA transforms the data to a basis with vectors that capture the most important variation in the data. These linearly independent vectors correspond to the non-zero eigenvectors of the covariance matrix of the data.
    
    Only the linearly independent eigenvectors that capture the most important variations in the data matter in PCA, and the ones that correspond to the null space (i.e., the ones sent to the 0 vector) can be discarded without loss of information. The eigenvectors in the null space represent directions that do not contribute to the structure of the data.
    
    - So the closer the eigenvalues are (the lower they are), the closer their eigenvectors are to null space?
        
        Yes, an eigenvector with a small or zero eigenvalue is almost mapped to the zero vector by the matrix.
        
    

Thus, transforming the data to ONLY on the eigenvectors means transforming it on to the directions that capture variation. The vectors in the null space (sent to 0) are no more after transformation, and the variation doesn’t change much in this new space compared to the old space. 

---

**TBC**

What it means for data to “vary” along a dimension is how spaced out it is with other data.

The eigenvectors are scaled by their eigenvalues.

- The columns of a matrix are where the old basis are sent. That means we send the old basis vectors TO the eigenvectors, so the inverse of the eigenvector matrix would send the eigenvectors TO the basis vectors. (?)

---

[https://stats.stackexchange.com/questions/2691/making-sense-of-principal-component-analysis-eigenvectors-eigenvalues](https://stats.stackexchange.com/questions/2691/making-sense-of-principal-component-analysis-eigenvectors-eigenvalues)

The first answer is that you are looking for some wine properties (characteristics) that strongly differ across wines. Indeed, imagine that you come up with a property that is the same for most of the wines - like the stillness of wine after being poured. This would not be very useful, would it? Wines are very different, but your new property makes them all look the same! This would certainly be a bad summary. Instead, PCA looks for properties that show as much variation across wines as possible.

The second answer is that you look for the properties that would allow you to predict, or "reconstruct", the original wine characteristics. Again, imagine that you come up with a property that has no relation to the original characteristics - like the shape of a wine bottle; if you use only this new property, there is no way you could reconstruct the original ones!

Surprisingly, it turns out that these two aims are equivalent and so PCA can kill two birds with one stone.

Pay attention to how the "spread" (we call it "variance") of the red dots changes while the line rotates; can you see when it reaches maximum? Second, if we reconstruct the original two characteristics (position of a blue dot) from the new one (position of a red dot), the reconstruction error will be given by the length of the connecting red line. Observe how the length of these red lines changes while the line rotates; can you see when the total length reaches minimum?

![https://i.stack.imgur.com/Q7HIP.gif](https://i.stack.imgur.com/Q7HIP.gif)

"the maximum variance" and "the minimum error" are reached at the same time, namely when the line points to the magenta ticks I marked on both sides of the wine cloud. This line corresponds to the new wine property that will be constructed by PCA.

Thus, the black line (which contains the red dots) is the 1st PC eigenvector when aligned in the magenta direction.

The spread of the red dots is measured as the average squared distance from the centre of the wine cloud to each red dot. On the other hand, the total reconstruction error is measured as the average squared length of the corresponding red lines. 

![Untitled](PCA%2006651e45a22843a29529bcf6b112ceb5/Untitled.png)

But as the angle between red lines and the black (yellow here) PC eigenvector is always 90∘ (see the orthogonal line to the black that makes it a ‘cross’), the sum of these two quantities is equal to the average squared distance between the centre of the wine cloud and each blue dot; this is precisely Pythagoras theorem. 

Of course, this average distance does not depend on the orientation of the black line, so the higher the variance, the lower the error (because their sum is constant).

As it is a square symmetric matrix, it can be diagonalized by choosing a new orthogonal coordinate system, given by its eigenvectors (this is called *spectral theorem*); corresponding eigenvalues will then be located on the diagonal. In this new coordinate system, the covariance matrix is diagonal.

---

- **QUESTIONABLE:**
    
    Pythagoras's theorem tells us that if the principal components are orthogonal, then the magnitude of the hypotenuse (i.e., the vector connecting the origin to a point in the dataset) is equal to the square root of the sum of the squares of the magnitudes of the other two sides (i.e., the magnitudes of the projections of the vector onto the two principal components).
    
    This property is useful in PCA because it allows us to compute the total variance captured by a set of principal components by simply summing the squared magnitudes of the components. It also allows us to compute the proportion of variance captured by each principal component by dividing the squared magnitude of the component by the total variance.
    

In PCA, the data points are projected orthogonally onto the new axes (the principal components) to reduce dimensions while preserving the maximum possible amount of variance. This orthogonal projection process can be understood geometrically as projecting points onto lines or planes in such a way that the sum of the squared distances between the original points and their projections is minimized.

??? Instead of targetting both goals, we can just target one goal that relates them: their hypotenuse. 

This is because making red small is the same as making yellow large ??? No:

If a and b are the two legs of a right-angled triangle, there isn't a direct inverse relationship between their lengths. However, if you increase or decrease the length of one side (a or b) while keeping the angle between them constant (90 degrees), the length of the hypotenuse (c) will also change accordingly due to the Pythagorean theorem (c² = a² + b²).

---

[https://jonathan-hui.medium.com/machine-learning-singular-value-decomposition-svd-principal-component-analysis-pca-1d45e885e491](https://jonathan-hui.medium.com/machine-learning-singular-value-decomposition-svd-principal-component-analysis-pca-1d45e885e491)