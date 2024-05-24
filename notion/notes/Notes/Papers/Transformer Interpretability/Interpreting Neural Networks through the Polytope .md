# Interpreting Neural Networks through the Polytope Lens

[https://www.lesswrong.com/posts/eDicGjD9yte6FLSie/interpreting-neural-networks-through-the-polytope-lens](https://www.lesswrong.com/posts/eDicGjD9yte6FLSie/interpreting-neural-networks-through-the-polytope-lens)

Direction A at L3 may be cat, but dir A at L6 may be dog

Polytope A at L3 is cat, and Polytope A at L6 is cat (?)

A polytope has unique affine transformation, and has unique set/path of activations (spline code). This allows us to define an invariant representation for a feature that’s the same across layers?

---

[https://www.connectedpapers.com/main/988914a393964adf63ce4e88b8375b12beb3b192/Interpreting-Neural-Networks-through-the-Polytope-Lens/graph](https://www.connectedpapers.com/main/988914a393964adf63ce4e88b8375b12beb3b192/Interpreting-Neural-Networks-through-the-Polytope-Lens/graph)

[https://inspirehep.net/literature/2674002](https://inspirehep.net/literature/2674002)

---

Appendix C: A NN contains layers (MASO operators) which contain neurons (MAS fns)

MAS (max-affine spline) means taking the max “slope” at each region. This max value (which, put into an affine eqn, is a line) at each region is a spline. Together, the splines approximate a convex function

Affine is superset of linear. Linear stays at origin; affine allows constant movement of origin.

---

[https://en.wikipedia.org/wiki/Convex_set](https://en.wikipedia.org/wiki/Convex_set)

if, given any two points in the subset, the subset contains the whole [line segment](https://en.wikipedia.org/wiki/Line_segment) that joins them

![Untitled](Interpreting%20Neural%20Networks%20through%20the%20Polytope%20%206cf61aaf87174768951ab45113e25a91/Untitled.png)

A [convex function](https://en.wikipedia.org/wiki/Convex_function) is a [real-valued function](https://en.wikipedia.org/wiki/Real-valued_function) defined on an [interval](https://en.wikipedia.org/wiki/Interval_(mathematics)) with the property that its [epigraph](https://en.wikipedia.org/wiki/Epigraph_(mathematics)) (the set of points on or above the [graph](https://en.wikipedia.org/wiki/Graph_of_a_function) of the function) is a convex set.

![Untitled](Interpreting%20Neural%20Networks%20through%20the%20Polytope%20%206cf61aaf87174768951ab45113e25a91/Untitled%201.png)

[https://en.wikipedia.org/wiki/Concave_function](https://en.wikipedia.org/wiki/Concave_function)

a **concave function** is the [negative](https://en.wikipedia.org/wiki/Additive_inverse) of a [convex function](https://en.wikipedia.org/wiki/Convex_function).

[https://www.dictionary.com/e/concave-vs-convex/](https://www.dictionary.com/e/concave-vs-convex/)

Convex and concave have different meanings in math than in English

---

[https://inst.eecs.berkeley.edu/~ee127/sp21/livebook/l_mats_norms.html](https://inst.eecs.berkeley.edu/~ee127/sp21/livebook/l_mats_norms.html)

[https://chat.openai.com/c/6dc3561f-1263-4d0b-849d-998c78092719](https://chat.openai.com/c/6dc3561f-1263-4d0b-849d-998c78092719)

[https://math.stackexchange.com/questions/33083/what-is-the-difference-between-the-frobenius-norm-and-the-2-norm-of-a-matrix](https://math.stackexchange.com/questions/33083/what-is-the-difference-between-the-frobenius-norm-and-the-2-norm-of-a-matrix)

The 2-norm (spectral norm) of a matrix is the greatest distortion of the unit circle/sphere/hyper-sphere. It corresponds to the largest singular value (or |eigenvalue| if the matrix is symmetric/hermitian).

The Forbenius norm is the "diagonal" between all the singular values.

![Untitled](Interpreting%20Neural%20Networks%20through%20the%20Polytope%20%206cf61aaf87174768951ab45113e25a91/Untitled%202.png)

[https://math.stackexchange.com/questions/17262/why-should-i-avoid-the-frobenius-norm](https://math.stackexchange.com/questions/17262/why-should-i-avoid-the-frobenius-norm)

Essentially, noise shows up as a long tail of singular values that are individually much smaller than the leading singular value, but when summed up, may exceed the leading singular value. The Frobenius norm is the sum of squares of the singular values, and hence, you are just measuring noise--the signal has little effect. The spectral norm, on the other hand, is just the leading singular value--and hence it is measuring the actual signal.

[https://www.quora.com/What-is-the-significance-of-the-Frobenius-norm](https://www.quora.com/What-is-the-significance-of-the-Frobenius-norm)

1. The nuclear norm and induced 2-norm (Euclidean, which is also used to describe Frobenius) both involve computing singular values of the matrix A, which can be expensive
2. However, unlike any of these aforementioned candidates, the Frobenius norm is also differentiable with respect to the individual entries of A, which allows us to use gradient-based methods to optimize the Frobenius norm.