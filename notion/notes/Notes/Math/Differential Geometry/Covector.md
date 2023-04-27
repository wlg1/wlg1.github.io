# Covector

[https://math.stackexchange.com/questions/240491/what-is-a-covector-and-what-is-it-used-for](https://math.stackexchange.com/questions/240491/what-is-a-covector-and-what-is-it-used-for)

a covector is an object that takes a vector and returns a number

to make the concept of dot product invariant to coordinate transformations.
dot product is vulnerable to changes in coordinate systems

Now lets scale the local coordinate system down by 2 so that the vector becomes ... new length changes
We want a way of computing the length of the vector that is invariant to re-specifications of the local coordinate system.

For an example of a covector, we have these functions dxi. As has been said in the previous answers, dxi is not a length but a function that takes vectors and picks out the ith coordinate component

If we take a covector and apply it to a vector, we basically get a dot-product

Therefore upon the transform, the covector components actually half, so that the answer stays the same:

<<<
It's always been easier for me to think of "covectors" (dual vectors, cotangent vectors, etc.) as different basis of vectors (potentially for a different space than "usual" vectors) because the linear algebra properties are still basically the same.

<<<
Covectors are weighted averages.
the ϕi could be basis functions (neurons). Adjusting the weights αi (on neurons) is the goal of statistical modelling. For example the OLS solution picks an "optimal" covector

except in a few bad cases, "straighten" the basis so it's orthonormal (unshear, rotate, whatever...Gram-Schmidt fixes it automatically), meaning the αi's will operate independently

linear combos make up lvl sets?