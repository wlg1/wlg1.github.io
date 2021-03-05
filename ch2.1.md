**2.1 Analyzing features and attributes in Latent Space**

In StyleGAN, we want to change one or more attributes of the image while keeping the other attributes the same- that is, we want to disentangle the attributes so that we can pick out which ones we want to change.

To understand how techniques for Style Editing work in Generative Adversarial Networks (GANs), we will examine the techniques used in the paper “Interpreting the latent space of GANs”. We will also show its connections to techniques in other papers.

**2.1.1 Dot product to define relation of z to hyperplane**

[Interpreting the latent space of GANs] A sample in latent space is a latent code since it’s encoding an image into it. We want a sample’s semantic score, which gives its value for a specific attribute such as age.

This is measured using equation X. But why does equation X use the dot product?

[equation]

The paper assumes that for any binary semantic attribute (e.g., old v.s. young), there exists a hyperplane in the latent space serving as the separation boundary.

FOOTNOTE: This distance can be negative and is not the same as the shortest distance from a latent code z to the hyperplane seen here:

Recall in (ch9, 3b1br) that vector multiplication is a projection onto the 1D number line, which is why it’s a scalar. Duality between dot product with a vector and getting a scalar
https://www.youtube.com/watch?v=KDHuWxy53uM&feature=youtu.be&ab_channel=KhanAcademy
Dot product is the amount of one vector goes in the direction of another. 

[Figure 2.1] Magnitude of vector can be negative because it’s not absolute length, but is where the vector is from the origin in a relative coordinate system. So if the vector is negative to the origin, the magnitude is negative. If 2 vectors have different signs, they’re pulling in 2 different directions. If they were in the same direction, they enhance each other, and thus multiply. Work = Force \* dist pulled

Other areas used: word2vec (don’t go into detail, just mention. Details is when click on this technique to get its page. We want to extract techniques from a paper one by one, not multiple papers at once.)

TECHNIQUES SO FAR: Dot product to measure relationship strength. In figure, bold the relationship and comment on it in bold in writing too. Include link to technq page.

**Normal vector to define hyperplane direction**

The paper uses the normal vector to define hyperplane direction. Why?

http://faculty.bard.edu/belk/math213/PlanesAndHyperplanes.pdf

Let n be the normal vector of the hyperplane, which is the vector perpendicular (orthogonal) to the hyperplane. The normal vector isn’t orthogonal every point on plane, but every DIRECTION (vector) on plane. This is not the point from origin to plane; it’s a vector lying on the plane.

All directions on hyperplane are orthogonal to this normal n, so their dot product with it is 0, as dot product (equation) has cos(90) = 0. Since this distance is on the hyperplane, it is orthogonal to the normal vector. 

http://sites.math.washington.edu/~king/coursedir/m445w04/notes/vector/normals-planes.html

![Figure 2.2: normal on hyperplane](/images/figure2.2.png)

The equation can be put into matrix form: NZ=0, such that all Z satisfying this are on the hyperplane [fig with matrix cols]. So if NZ > 0 or NZ < 0, it’s not on the hyperplane. 
But why does it give distance from each dimension in hyperplane? Because d(n,z) is not the ACTUAL distance, but a measure of how strongly the sample z goes in the direction of the hyperplane. How close is it to one side of a hyperplane versus another? The more NZ > 0, the more strongly that sample goes with that region of the binary attribute. 
linear interpolation b/w 2 latent codes forms a direction

![Figure 2.3: cosine orthogonal derivation](/images/figure2.3.png)

Define semantic scores as s = lambda\*d(z,n) = lambda\*N\*z
Technique: Measure attribute direction

**2.1.2 Covariance matrix of semantic scores**

[Visual Explanation of Principal Component Analysis, Covariance, SVD: 1m to 230m:
https://www.youtube.com/watch?v=5HNr_j6LmPc&list=LL&index=4&t=284s&ab_channel=EmmaFreedman ]

Figure 2.4: Covariance is how far away a data point is from its mean = (xmean, ymean). The distance of a data point from the mean is a rectangular area that shows how much it deviates from the mean. (1) shows a data point with negative correlation, while (2) shows a data point with positive correlation. If you take all these areas and normalize, you get the covariance of the sample set (3). 

![Figure 2.4: cov](/images/figure2.4.png)

NOTE: move positive correlation to bottom-left quadrant for more space

![Figure 2.5: cov matrix](/images/figure2.5.png)
[Figure translating each axis into one cov score b/w 2 z’s, then putting it as value of matrix. Figure labeling what each row/col is for cov matrix of semantic scores. var along diag (if you measure cov on 1 axis, you're just measuring var), cov for every other dim combo in non-diag.]

The covariance of each latent code z’s semantic score shows how each z varies from one another. The more they vary together, the more entangled they are. Any two latent codes with 0 covariance are disentangled.

Conditional Manipulation: Manually force covariance matrix of semantic scores to be 0 everywhere except its diagonal. This means the n (columns of transformation N) are orthogonal to one another. Then use this to find new direction (?)

TECHNIQUE: Measure entanglement of attributes

**2.1.3 Get equation for new direction using projection**

The orthogonal projection’s complement is a NEW DIRECTION such that moving samples along it can change n1 without changing n2 (since it’s orthogonal to n2) (p4).

It uses orthogonal projection from the normal of one hyperplane to the normal of hyperplane 2 to form a new direction. To obtain disentanglement in the covariance matrix, it requires that the normals be orthogonal to each other. This equation shows how moving samples in the new direction can change attribute 1 without affecting attribute 2, since the new direction is orthogonal to attribute 2, but not to attribute 1.

https://textbooks.math.gatech.edu/ila/projections.html

![Figure 2.6: orthogonal projection](/images/figure2.6.png)

For all the hyperplanes of attributes you DON’T WANT TO CHANGE (n1), project normal that onto normal of hyperplane that you DO WANT TO CHANGE (n2).

TECHNIQUES SO FAR: Get equation for easier to edit direction using Orthogonal projection 

So if 4 attributes don’t want to change, project all 4 onto n2? How do you get their direction? Use the matrix N, where each column is a normal of a hyperplane. The dot products in the matrix multiplication N\*N gives part of the covariance matrix (except the linear coefficients lambda). Each dot product b/w row and column is b/w 2 normals; the result is the covariance, and if they’re orthogonal, that’s 0.

But where does projected direction equation come in? We EDIT the latent code z directly; once we have the latent code for an image, manually edit it. Remember the equation is z + an, where n is the direction we want to edit on (red in figure). So let n be the new projected direction.

[figure of edit equation  zedit = z+ αn. ]

How do we get the code z of an image? We know the link b/w z and the image using the generator function g. The inverse is harder to get, but if we randomly sample code z, we know its image. So after randomly sampling z, modify it manually using the edit equation. If you DO have inverse using one of 2 typical approaches (see p7, 3.5 ‘real image manipulation’), you can go from an image to its modification.

Semantic scoring function f: Image to Score, so use s : Latent → Image → Score. 

[Figure 2.7 breaking down covariance matrix and N]

Change multiple attributes at once: subtract the projection from the primal direction onto the plane that is constructed by all conditioned directions. 


**Techniques so far to describe latent space in human terms:**
    
| Issue       | Solution |
| ----------- | ----------- |
| Find hidden relationships in data | Encode using transformation with a ‘good’ basis |
| Find relationship between encoding and attributes- semantic scores | Dot products |
|  Measure attribute direction | Normal vector of hyperplane |
| Measure entanglement of attributes | Covariance Matrix of scores as normal vectors |
| Find new attribute direction in encoding space | Orthogonal projection |