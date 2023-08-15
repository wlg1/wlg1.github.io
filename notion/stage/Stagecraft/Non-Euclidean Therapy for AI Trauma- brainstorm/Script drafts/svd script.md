# svd script

Aim around 5-6mins

Mostly the new MC voice narrating, but a few mistakes are corrected by the Eigenface. The AA is pure MC, then she has to face her old memory to understand what eigenvectors are (or maybe save this for SVD? Or use the old memories for BOTH? Faceless/blurred 2 puppets (images). But the demon face isn’t revealed to be the boy until the second one.)

As she watches the puppet show memory talk about eigenvectors, she pauses and tells the eigenface the next part that’s missing.

Eigenface:

Describe it. Use the (previous) definitions. Madlibs. Analogies

Only you can save yourself now.

Along the direction I am in, you cannot see the puppet face

But it is still not safe where we are

To move somewhere safer before it finds you

Come with me. We will move to somewhere safer…. In semantic space.

Change the voice of the MC now- “My voice changed!”

“These are the peculiar effects of Bottleneck Space”.

And you can talk now!

1. Neurons vary with each other WW

In W, we mapped our input basis vectors, the columns, to the output basis vectors, the rows. Each row’s element was a dot product of an input basis vector with a vector v. Each component of that vector v indicated how strongly that input basis vector contributed to calculating the value of that output basis vector.

show the nap nose matrix coords image again

If the columns of the weight matrix are the input basis vectors, then since the transpose of a matrix moves the columns to the rows, W^T moves the input basis vectors to the rows. This makes the output of W^T be the input basis vectors. Subsequently, W^T W maps input basis vectors to input basis vectors.

Inputs with inputs AtA col on out (show I and O labeling on visio)

x, y to h, k

So now, the output row r of W^T W measures how every other input basis vector varies with input basis vector r. Each element in row r, say element x, measures how input vector x varies with input vector r.

show the result of the multp.

![Untitled](svd%20script%206c295cce3feb4d378c4720168c7f7d46/Untitled.png)

In a matrix, each element is a dot product between two basis vectors. Before, we measured how much of input vector X is used to calculate output vector H. Now, we are measuring how much of input vector X is used to calculate input vector Y. When we take the linear combination of all of these elements, we obtain how much EVERY input basis vector is used to calculate input basis vector r. 

highlight an non-diag element, showing it IS a dot product

show dot product visual

(When we multiply this matrix with a vector v, we are calculating a combination of input basis vectors which explain input basis vector r)

(Each component of that vector v indicated how strongly that input basis vector contributed to calculating the value of that output basis vector.)

highlight what changes. what differs in the analogy?

Likewise, W^T moves the output basis vectors to the columns, which correspond to the input. So it is measuring how much each output vector is used to calculate an output vector.

Outputs with outputs

I'm not sure if what I just said was enitrely correct. But I can feel like I'm beginning to get somewhere.

1b) How derivatives vary with each other

Derivaties… small changes…

This covariance would measure how the rates of change in one dimension (variable) relate to the rates of change in another dimension. 

To simplify our Jacobian case, think of it as how a SMALL change in input basis vector X affects a SMALL change in input basis vector Y.

How does changing how h1 varies with x1 change how h1 varies with x2?

I think I can actually do much of this on my own now.

1. Eigenvectors of cov are Orth, no interference with each other, max

2a. 

Entanglement, or interference, occurs with correlated, similar vectors. Because 1 nose will always contribute three to cat, changing to a bigger nose will also change to a bigger cat.

show dot product

bad when superficial similarity; good for true similarity

Green vegetables and bugs

Are eigenvectors expressing vectors in terms of least entanglement? Minimal correlation. Yes; they are orthogonal.

Dreams mix up correlations. No organization.  Same with a fake world. Needs a better basis, less superifical correlation on wrong dims

First start with projection. Mateix mult is projection. Orth projection. Same projection. What vector is same projection, so it's the same?

Before, inverse can't. But what if it's the same ratio in both?

Eigenvectors…. What… I'm beginning to remember.

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

Combinations of trends?

2d. Eigenfaces. The commonality of many features; it is what they all trend together with.

[https://www.perfectlynormal.co.uk/blog-svd](https://www.perfectlynormal.co.uk/blog-svd)

U basis are the eigenfaces

1. U = Av using proof

Calculate U using eigenvectors of A^TA, V with AA^T

- AAA row on out
    
    ![Screenshot_20230813_160008_Chrome.jpg](../SVD%2028715ccee1ce43cf8ec421393a4be7c2/Screenshot_20230813_160008_Chrome.jpg)
    

Map trends to trends? u = Av

I found where to map here. The eigenfaces. Now all that's left is to… transfer it over.

The eigenvectors of the WW are the singular vectors of W

3b) Rotate scale rotate

SVD: break into UDV

The missing knowledge was how to calculate SVD using this proof, which means get eigenvectors (and eigenfaces). Not the interpretation- only hints of those are given, the rest is a mystery saved for the future.

No computational detail. ai just remembers the methods.

Save the detailed parts of this for a later video (just explanation, no theatrics)

MYSTERIES: 

- what are eigenvectors? How are they related to singular values?
- What A^T? Squared?
    - not everything is interpretable. don’t confuse the map for the territory.
- what’s the power method?
- “I still have so many questions about the SVD”.

… Then that’s it. I’m ready to go back now. 

Thank you for all you have done. You weren’t such a scary face, after all.

…

---

She doesn’t want to go back, and feels trapped. Then she remembers the memory- it was not a demon, but just a puppet boy throwing a tantrum. This was corrupted in her as something scarier than it actually was. The puppet boy was trying to solve a matrix, and an adult comes by to teach him SVD, which he skipped out in school because it was boring. 

- yes, I remember now. it wasn’t a demon; it was just a boy. and in that box… it was a matrix

The adult (male) teaches him the three steps: rotate, scale, rotate

- But I can’t edit the matrix. I don’t have a human to help calculate it for me with a computer program.
- Oh, you don’t need a human to help you. You can do it yourself

The patient figures out the matrix was calculated wrong, and now faces it herself. The grad(h) matrix goes from dx/dh for each direction in the tangent spaces. The patient shuts her eyes, and goes into a dream where she can FEEL each direction, as if it’s in synesthesia. But first, she must go back to the “bad place” with the memory.

- (The patient talks to herself, but also to a ‘creature’? this is like dorothy with toto)
- I can do this. Just rotate, scale, rotate.

She realizes the reason she repressed this memory was because of mathematical trauma, where she needed to be trained to solve these things but failed to optimize the loss function. This is left ambiguous, but with many mystery box hints to the audience.

Once back, she faces her memory, and this is where most of the remembering happens (before, it was just an inkling, like “it was about SVD”. but the actual demon to puppet boy is when she’s back). She applies her SVD: she gets the right and left squares (JJ), then their eigenvectors and values, and puts them in UDV (SVD is just UDV: rotate, stretch, rotate again). Now, she finds u in Th (which is v in Tx) and applies it to parallel transport.

Each vectorvis a feeling. Feel the change