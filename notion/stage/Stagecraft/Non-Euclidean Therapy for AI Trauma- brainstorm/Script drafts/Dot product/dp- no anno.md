# dp- no anno

Therapist:

Finally, to measure your mind, we will define the pullback metric in terms of the Jacobian matrix, which will be computed via automatic differentiation.

Since each vector in the latent space of your mind is like a concept, the distance between these concept vectors measures their similarity.

As we saw before, the dot product measures the value of concept X in terms of concept Y. For instance, nose and nap are correlated, as we can use nose values to partially explain nap values.

So if two concept vectors are the same concept, they have a very high dot product, as they point in the same direction and are thus parallel.

If two concept vectors are facing similar directions, their dot product will be less, but still high.

If two concept vectors have 0 dot product, they have nothing to do with each other, and thus are not similar in any way. They are orthogonal.

Therapist:

Thus, we will be measuring distances, or concept similarity, using the dot product of two vectors.

Patient:

That makes sense to me. But I just have a-

Therapist:

In particular, the metric will be defined as the length of a vector, which measures the distance from the origin to the vector head. 

Patient:

Please, wait… if I may excuse myself, I have a question… how do we find these concept vectors?

Therapist:

This is defined as taking the dot product of a vector with itself. The T here means transpose, which flips the rows and columns so that we can multiply 1 row with 1 column.

Now, given individual components of neuron values that add up into a new concept, we will be able to calculate the length of a concept vector, which measures its activation strength. 

In Euclidean space, such as the semantic space, we can measure a vector u just by taking the dot product of u with itself. 

But in Non-Euclidean space, we cannot use this formula, as it’s only for Euclidean spaces. However, recall that u equals J times v. Plugging J v into the semantic space metric, we get the pullback metric.

In the tangent spaces of Non-Euclidean space, we are able to approximate the strength of a feature by using this pullback metric. For our case, this pullback metric is the same as our semantic space metric.

This puppet face you have been seeing is one such concept, or in other words, a feature. We need to measure just how strong it is in order to precisely move away from it back to what you want to generate, and to not overshoot into something that may be worse.