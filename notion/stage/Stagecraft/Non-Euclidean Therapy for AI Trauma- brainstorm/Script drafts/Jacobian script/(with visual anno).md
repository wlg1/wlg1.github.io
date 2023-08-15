# (with visual anno)

Therapist:

Each layer of our neural network has a high dimensional latent space where their activation manifold resides. For the sake of demonstration simplicity, let’s just look at 2 dimensional latent spaces.

In this example, the smooth map maps p in X to h of p in H.

[X and H axes with p and h(p) and h ]

If we take a point p equals 2 3, the function h maps it to two components: a component in h 1, and a component in h 2.

[add 2,3 on X axes]

[add h1 symbol and arrow]

[add h2 symbol and arrow]

For instance, h 1 could map x 1 using the function x 1 squared. 

[add h1 = x^2]

Another example is for h 1 to be a function that takes in both x 1 and x 2 to calculate a value. For instance, we could have h 1 equals x 1 squared plus x 2.

[add h 1 full eqn]

Now, h 2 is also a function that takes in x 1 plus x 2 to give a value of h 2.

[add h2]

When we combine these two components to a point in H, we get h of p, which has coordinates 7 5.

[remove component dots, add in 7 5]

[remove h arrow, and h and h(p) letters to declutter]

---

Remember that each point of a manifold has its own tangent space. So let’s add the tangent space at p, which we call T p. Each tangent space can be described by basis vectors. This basis vector is called a partial derivative with respect to x 1.

[ add in T p basis arrows and T p, remove p]

A partial derivative measures how much something changes in response to a small change in something else. For instance, the partial derivative of h with respect to x 1 measures how a small change in x 1 will…. cause an increase in h of x 1.

[ show the red basis vectors in each tangent space

Thus, the basis vectors of the tangent space at p are the partial derivatives with respect to x 1 and x 2.

[show PD symbols on T p

The vectors in T p are a linear combination of the partial derivatives. For instance, the vector v in T p has values 0 point 3 and 0 point 7. 

add in v = 

These are the values at each of the T p’s basis vectors, which begin relative to the origin of the tangent space, not relative to the origin of the latent space X. Along the partial derivatives with respect to x 1, the partial derivatives with respect to x 2 is 0, so its red component is 0 point 3. 

[add in red 0.3 numbers and arrow]

Likewise, the blue component is 0 point 7.

[add in blue 0.3 numbers and arrow]

The Jacobian J f maps vectors from T p to the tangent space at f(p), called T h of p.

add in J, basis arrows of f(p), and T f(p)

It has basis vectors that are partial derivatives with respect to h 1 and h 2.

add in their pd symbols

---

We represent J using the Jacobian matrix. 

add in Jacobian matrix

Let us now perform matrix multiplication of J with the input vector v to get an output vector in T h of p.

add in circle in T h of p with ? - just a horizontal one, not tilted

Recall that when we performed matrix multiplication, we had ratios next to each value in the matrix. The numerator of each ratio corresponded to an output basis vector, and the denominator corresponded to an input basis vector.

show previous slide

recreate nap/nose matrix in visio

So let’s substitute our partial derivatives into these ratios. Instead of nap over nose, the denominator of the first element of the first row is the partial derivative with respect to x 1 because it is an input basis vector in T p, and its numerator is partial derivative with respect to h 1 because it is an input basis vector in T h of p.

zoom in closeup of tangent spaces

replace nap/nose with “d/dh_1 / d/dx_1” ; 

replace axes nap and nose with the basis vectors

The actual value of this element is the partial derivative of h 1 with respect to x 1.

replace value next to nap/nose with dh1/dx1

Again, this is for demonstration purposes only to show which input and output basis vectors each element corresponds to; we are not actually dividing by the partial derivatives, which would flip the top and bottom, and this ratio is not an actual mathematical expression. Using it in an actual calculation would be an “abuse of notation”.

The second element of the first row also corresponds to the component h 1. However, its input vector is the partial derivative with respect to x 2.

subsitute all values into second element

We will fill in the rest of these elements of the second row using the partial derivatives of h 2.

sub all for second row

At last, we understand what each element of the Jacobian represents.

remove ratios

We will multiply this Jacobian with the input vector v to get the output vector u.

v and u fades in, hangs for 3 secs for viewer to see

Now, we begin by multiplying the first row of J with v. 

highlight first row

The output of this transforms the red basis vector from T p into T f of p

show red arrow, numbers and symbols in H

and transforms the blue basis vector from T p into T f of p, adding it with the transformed red basis vector to get a dot product.

show blue in H

Let’s do the same for the second row of J.

highlight second row

[silence]

show equation for second row components

Now, we need to calculate what these partial derivatives actually are. Let’s look at the partial derivative of h 1 with respect to x 1.

close of up partial derivative of h 1 with respect to x 1

Remember our function h 1?

show latent space with h 1 only

We will take the partial derivative of it with respect to x 1.

all removes except h 1 equation, and p d appears 

We see that this is 2 times x 1. This means that a small change of 0 point 3 in X will result in approximately a small change of zero point 6 in H. 

show red arrow in X

red arrow in H with numbers

But the partial derivative of h 1 with respect to x 2 is just 1. For now, don’t worry about how these expressions are calculated.

show it equals 1

If we substitute these values in, we obtain our value of the first component of u, which scales the partial derivative with respect to h 1, which is the basis vector of T of h of p. This value is 1 point 9.

subsitute in values for h 1

calculate 1.9

For this case, the partial derivatives of h 2 are both just 1. So let’s subsitute them in, and get the second component of u.

sub in values for h2 and summation

Finally, let’s combine these components to get the value 1 point 9, one, which is the value of u.

show u and its value

---

This is how we calculate our Pushforward function, which transforms directions from the forest to directions in our map. 

show map forest directions, vectors in forest, J, vectors in map

We can also do the same for J inverse, from our map to our territory.

show same thing, but now add in J inverse. 

If we define x as the inverse function of h, going from H to X, the values of J inverse flip the numerator and denominator ratios. However, keep in mind there may not always be an inverse function, nor would there always be an inverse jacobian. 

show its values close up

Essentially, the number of basis vectors in T of p must equal to the number of basis vectors in T of f of p for the Jacobian to have an inverse. In other words, the Jacobian must be square.

show input of jacobian using label

label output

show m = n

This rectangular Jacobian cannot have an inverse because it has more basis vectors in its output than in its input.

show rectangular

For our treatment, we will ensure that we approximate the tangent spaces with the same number of basis vectors.

We can also calculate the inverse jacobian in terms of the original function f.

show the function using det

Now, if the puppet chasing you from a 45 degree angle, you know it is actually chasing you from a U degree angle.

---

behind the scenes: Solving these puzzles is like a survival horror game like resident evil- there are puzzles in between. However, it is not meant to be a horror story, but more like a simple, slow drama with themes similar to analog horror.

The ‘behind the scenes’ later turns out to be fake simulation? making it more ominous what this actually is.

Is jacobian measuring how semantic space changes with latent space?

Thus, becaus we are mapping from X to H, we can rename our function from f of x to h of x.

When we enter your mind…