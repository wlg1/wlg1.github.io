# no anno

Therapist:

Each layer of our neural network has a high dimensional latent space where their activation manifold resides. For the sake of demonstration simplicity, let’s just look at 2 dimensional latent spaces.

In this example, the smooth map maps p to h of p.

If we take a point p equals 2 3, the function h maps it to two components: a component in h 1, and a component in h 2.

For instance, h 1 could map x 1 using the function x 1 squared. 

Another example is for h 1 to be a function that takes in both x 1 and x 2 to calculate a value. For instance, we could have h 1 equals x 1 squared plus x 2.

This would give a value of 2 squared plus 3, which equals 7.

Now, h 2 is also a function that takes in x 1 plus x 2 to give a value of h 2.

When we combine these two components to a point in H, we get h of p, which has coordinates 7 5.

Remember that each point of a manifold has its own tangent space. So let’s look at the tangent space at p, which we call T p. Each tangent space can be described by basis vectors. 

This horizontal axis basis vector is called a partial derivative with respect to x 1.

---

PATIENT:

That sounds familiar… a derivative sounds like something I heard before, long ago. What is it?

THERAPIST:

A partial derivative measures how much something changes in response to a small change in something else. For instance, the partial derivative of h with respect to x 1 measures how a small change in x 1, shown in red next to p, will…. cause an increase in h of x 1, shown in red in H.

Thus, the basis vectors of the tangent space at p are the partial derivatives with respect to x 1 and x 2.

The vectors in T p are a linear combination of the partial derivatives. For instance, the vector v in T p has values 0 point 3 and 0 point 7. 

These are the values at each of the T p’s basis vectors, which begin relative to the origin of the tangent space, not relative to the origin of the latent space X. Along the partial derivatives with respect to x 1, the partial derivatives with respect to x 2 is 0, so its red component is 0 point 3. 

Likewise, the blue component is 0 point 7.

So v is a linear combination of 0 point 3 times the red basis vector, plus 0 point 7 times the blue basis vector

The Jacobian J f maps vectors from T p to the tangent space at f(p), called T h of p.

It has basis vectors that are partial derivatives with respect to h 1 and h 2.

We represent J using the Jacobian matrix. 

Let us now perform matrix multiplication of J with the input vector v to get an output vector in T h of p.

---

Patient:

Does multiplying by the Jacobian have something to do with finding cat naps from cat noses, as we saw before?

Therapist:

Yes. Recall that when we performed matrix multiplication, we had ratios next to each value in the matrix. The numerator of each ratio corresponded to an output basis vector, and the denominator corresponded to an input basis vector.

So let’s substitute our partial derivatives into these ratios. First, we’ll zoom in and only look at our tangent spaces.

Instead of nap over nose, the denominator of the first element of the first row is the partial derivative with respect to x 1 because it is an input basis vector in T p, and its numerator is partial derivative with respect to h 1 because it is an input basis vector in T h of p.

The actual value of this element is the partial derivative of h 1 with respect to x 1.

PATIENT:

Wouldn’t this division flip the top and bottom?

Therapist:

It is not actually dividing by the partial derivatives. Just like before, this ratio is for demonstration purposes only to show which input and output basis vectors each element corresponds to. It is not an actual mathematical expression, and using it in an actual calculation would be an “abuse of notation”.

Patient:

Oh, I see… I wouldn’t want to do that.

Therapist:

The second element of the first row also corresponds to the component h 1. However, its input vector is the partial derivative with respect to x 2.

We will fill in the rest of these elements of the second row using the partial derivatives of h 2.

At last, we understand what each element of the Jacobian represents.

Thus, we will multiply this Jacobian with the input vector v to get the output vector u. 

We begin by multiplying the first row of J. This transforms the red basis vector from T p into T f of p and then transforms the blue basis vector, and they add together into a dot product.

Let’s do the same for the second row of J.

Now, we need to calculate what these partial derivatives actually are. Let’s look at the partial derivative of h 1 with respect to x 1.

Remember our function h 1? We will take the partial derivative of it with respect to x 1. And we see that this is 2 times x 1. This means that of 2 in X will result in approximately a change of 4 in H. 

When we take the partial derivative of h 1 with respect to x 2, we find that it’s just 1. For now, don’t worry about how these expressions are calculated.

If we substitute these values in, we obtain our value of the first component of u, which scales the partial derivative with respect to h 1, which is the basis vector of T of h of p. This value is 1 point 9.

For this case, the partial derivatives of h 2 are both just 1. So let’s subsritute them in, and get the second component of u, which is 1.

Finally, let’s combine these components to get the value 1 point 9, one, which is the value of u.

---

This is how we calculate our Pushforward function, which transforms directions from the forest to directions in our map. 

We can also do the same for J inverse, from our map to our territory.

If we define x as the inverse function of h, going from H to X, the values of J inverse flip around. However, keep in mind there may not always be an inverse function, nor would there always be an inverse jacobian.

To have an inverse, the number of input basis vectors must equal the number of output basis vectors. We will ensure that we approximate the tangent spaces this way.

This rectangular Jacobian cannot have an inverse because it has more basis vectors in its output than in its input.