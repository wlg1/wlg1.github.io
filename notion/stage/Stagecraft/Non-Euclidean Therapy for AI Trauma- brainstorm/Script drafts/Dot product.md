# Dot product

[dp- no anno](Dot%20product%20b1625de2de9d4bc19cf9817c3fdcd395/dp-%20no%20anno%20345ac187aa6b4eb699537cb225d72f8d.md)

---

Since each vector in the latent space of your mind is like a concept, the distance between these concept vectors measures their similarity.

kingqueen

As we saw before, the dot product measures the value of concept X in terms of concept Y. For instance, nose and nap are correlated, as we can use nose values to partially explain nap values.

1D to 2D MM image

So if two concept vectors are the same concept, they have a very high dot product, as they point in the same direction and are thus parallel.

3.parallel vectors

If two concept vectors are facing similar directions, their dot product will be less, but still high.

4) in b/w

If two concept vectors have 0 dot product, they have nothing to do with each other, and thus are not similar in any way. They are orthogonal.

5. orth

Thus, we will be measuring distances, or concept similarity, using the dot product of two vectors.

6.all three

In particular, the metric will be defined as the length of a vector, which measures the distance from the origin to the vector head. This is defined as taking the dot product of a vector with itself. The T here means transpose, which flips the rows and columns so that we can multiply 1 row with 1 column.

length

$\langle \mathbf{v}, \mathbf{v} \rangle = \mathbf{v}^T \mathbf{v}$

Now, given individual components of neuron values that add up into a new concept, we will be able to calculate the length of a concept vector, which measures its activation strength. 

8.same as before but add tail fur cat

This puppet face you have been seeing is one such concept, or in other words, a feature. We need to measure just how strong it is in order to precisely move away from it back to what you want to generate, and to not overshoot.

map

In Euclidean space, such as the semantic space, we can measure a vector u just by taking the dot product of u with itself. 

X and H, but add in <u,u>

But in Non-Euclidean space, we cannot use this formula, as it’s only for Euclidean spaces. However, recall that u equals J times v. Plugging J v into the semantic space metric, we get the pullback metric.

add <u,u> equals J v to image

In the tangent spaces of Non-Euclidean space, we are able to approximate the strength of a feature by using this pullback metric. For our case, this pullback metric is the same as our semantic space metric.

---

- why is the metric defined as the dot product between the same two vectors?
    
    The metric in the context of vector spaces and geometry is often associated with the concept of a "dot product." When you mention the metric as the "dot product between the same two vectors," you're likely referring to the norm or magnitude of a vector, particularly in the context of metric spaces and relativity.
    
    Let's break it down step by step:
    
    1. **Dot Product**: Given two vectors \( \mathbf{a} \) and \( \mathbf{b} \) in a Euclidean space, their dot product is given by:
    \[ \mathbf{a} \cdot \mathbf{b} = |\mathbf{a}| |\mathbf{b}| \cos(\theta) \]
    where \( |\mathbf{a}| \) and \( |\mathbf{b}| \) are the magnitudes of the vectors and \( \theta \) is the angle between them.
    2. **Metric (or Norm)**: The length or magnitude of a vector \( \mathbf{a} \) in a Euclidean space can be found by taking the square root of the dot product of the vector with itself. This is because the cosine of the angle between a vector and itself is 1 (as the angle is 0 degrees). Therefore:
    \[ |\mathbf{a}| = \sqrt{\mathbf{a} \cdot \mathbf{a}} \]
    
    This provides a measure of "distance" from the origin to the point represented by the vector.
    
    1. **Generalizations**: In more general spaces, like in general relativity where spacetime has a curved geometry, the "dot product" is replaced by a more general metric tensor. This metric tensor can be used to find the "distance" between two infinitesimally close points in spacetime. The metric tensor generalizes the simple notion of a dot product to account for the curvature of spacetime.
    
    In summary, the dot product of a vector with itself gives us a way to measure the "length" or "magnitude" of the vector. This concept is foundational in geometry, physics, and many other disciplines, and it provides a bridge between geometric concepts and algebraic operations.
    
- Why do we measures the length of a vector as a metric to measure distances between two vectors?