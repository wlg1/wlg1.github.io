# Eigenvector brainstorm

What does adding var and cov do?

Eigenbasis. P inv maps eigenvec onto basis.

Eigenvec stretched more than any other  basis vector?

- When you take a 2D matrix, you map a vector from domain onto the basis. Are the original coordinates of this vector a row of the matrix?
    
    

It’s not true that the “scalar part” is a projection onto the other vector. That formula requires law of cosines

Instead, state that the projection removes part of the original length

[https://www.youtube.com/watch?v=LyGKycYT2v0](https://www.youtube.com/watch?v=LyGKycYT2v0)

(Note that this red part is NOT the dot product value)

In any case, 

[https://www.quora.com/What-is-the-intuitive-meaning-of-a-covariance-matrix](https://www.quora.com/What-is-the-intuitive-meaning-of-a-covariance-matrix)

Think of it this way: If the eigenvector direction was not one of maximum variance, the covariance matrix could "rotate" it slightly to get a direction with even higher variance. But it doesn't, because the eigenvector is already in a direction of maximal variance. The covariance matrix can only "stretch" or "compress" it, which is the essence of the eigenvalue-eigenvector equation.

This is because any other direction would "mix" the data's intrinsic structure more, resulting in a lower variance when projected.

- Why does the covariance matrix rotate a vector so that it can get a direction with even higher variance? Also explain "This is because any other direction would "mix" the data's intrinsic structure more, resulting in a lower variance when projected.”
    
    For example, consider a 2D dataset that's stretched out along the x-axis more than the y-axis. If you project all the data onto the x-axis, you get the maximal variance. But if you project the data onto a direction that's, say, 45 degrees from the x-axis, you're effectively "blending" or "mixing" the variances from both the x and y directions. The result is that the total variance along this blended direction is less than that along the x-axis alone.
    
    This is what I meant by "mixing the data's intrinsic structure": projecting onto a non-eigenvector direction combines the structures/variances of multiple principal components, leading to reduced variance compared to the maximal direction.
    

Each output weight is a change of variables from that input vector to explain how much it explains input vector c. Now, the eigenvector of a cov matrix has components for each 

Does explains high variance” means contributes a lot to explaining a value of a vector?

[https://math.stackexchange.com/questions/243533/how-to-intuitively-understand-eigenvalue-and-eigenvector](https://math.stackexchange.com/questions/243533/how-to-intuitively-understand-eigenvalue-and-eigenvector)

**No other vector when acted by this matrix will get stretched as much as this eigenvector**. (wrong for nonsym)

But why does eigenvector explain max variance?

There is no time to explain now.

When the nap dim projects onto the basis vector, 

We want the projection to be the same for the same, but not have them interfere with others.

Before, inverse can't. But what if it's the same ratio in both?

Are eigenvectors expressing vectors in terms of least entanglement? Minimal correlation. Yes; they are orthogonal with eahc other.

Dreams mix up correlations. No organization.  Same with a fake world. Needs a better basis, less superifical correlation on wrong dims

2b. Why no dir change is max? Bc already same interpretation in both spaces. All other vectors change interp? Same ratio. Parallel means no loss. Same sim

Each vec in terms of the eigenvec. Rotate vec in terms of eigenvec instead of in terms of basis, compare them. Relate this to how eigenvec preserves info after transforming by matrix

Does matrix project one vector onto another? Yes. So using the eigenvectors as basis means we project onto the eigenvectors. If we write the matrix WW’s output row basis using its eigenvectors (poss?), AND write the input row basis using eigenvectors, we are projecting eigenvectors onto eigenvectors. Both found the same way, whi h is eigenvalues on diagonal. From them, we truncate to the top 50 highest eigenvalues. Dim reduction. 

Eigenbasis is diagonal. Now basis just get scaled

2c. For weights, their cov eigenvectors of input capture how inputs interfere and correlate with each other

Eigenvector is the primary trend in how height and weight vary together. If  v 1  has both positive x and y components, it means as height (x-axis) increases, weight (y-axis) generally also increases. They are both related by this.

By knowing one, you can derive more of th3vother . So eigenvector is a big component in many, bc large eigenvalue for many other vectors (no wrong, eigenvalues isn't a weight ceoffi)c. Eigenvec of cov is reln BTW many

https://reddit.com/r/math/s/wkXIIf5AJz

The output (rows) of W^TW are 

A and B are specific input values. If an eigenvector [A, B], and A is high with W11 and B is high with W12, that means it points in the same direction as in 1. But it ALSO points in the same direction as all the others.

Each vector gives a different trend. 

Multiplying an output basis by itself gives 1 because in the OLD space, it doesn’t use the same. You must multiply it not by the same col vec, but by the inv, to get 1.

A (w_in1(in1) ) + B (W_in1(in2) ) are how much each vector 

hihgliht in_1 in eqn

Usually, when a vector is projected, it must project onto. But if it scales, that means it was already there. But eigenvectors are not always the output rows of WW. 

[https://users.cs.utah.edu/~tch/CS4640/resources/A geometric interpretation of the covariance matrix.pdf](https://users.cs.utah.edu/~tch/CS4640/resources/A%20geometric%20interpretation%20of%20the%20covariance%20matrix.pdf)

Much of this is still left as a mystery

“But I still have so many questions”

“We must work fast.”

“Are they… trends?” → no answer is given. Careful with your interpretations, now. Make sure they logically fit with all other true statements.

Combinations of correlation measurements?