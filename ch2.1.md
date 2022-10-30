---
title: CHAPTER 2.1
---
<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>

In StyleGAN, we want to change one or more features of the image while keeping the other features the same [show before + after outputs]

Recall from Chatper 1 that features can be approximated as vectors in the latent space of neuron activations.
[fig]

What this means is that if we only want to change one feature, we should only change one vector, while keeping all other vectors the same. But how do we find this vector? 

**Changing what's on basis vector**

First, let's start with a simpler case, where the feature we want to change is on a basis vector. Say the Age vector is on the y-axis. In this example, we want to keep x=3, and move along the y-axis. We have a vector $$V=[3,2]$$, and we want to find a similar vector, $$W=[3,1]$$:

![Figure ](/ch2/VtoW.PNG)

In Figure 1, all we have to do is to find W is to "walk" down line $$C$$ from vector $$V$$. In fact, you can move to any point along $C$$ without changing the value of x=3. 

Why does vector C not change the value of x=3? Because vector $$C$$ is **orthogonal** to the $$x$$ basis vector, where they intersect at x=3. If it was not orthogonal, it would veer away from x=3, such as shown in the example below, where a non-orthogonal vector leads to x=4.

![Figure ](/ch2/VtoW_veer.PNG)

It is only when the green vector intersects the x vector at 90 degree angle that the value of the $$x$$ vector doesn't change.

How do we calculate the value of this orthogonal vector $$C$$ we want to move on?

In this case, because we want to keep the value of x and change the value of y, and y is a basis vector, we can move parallel to the y-direction by simply changing the y-coordinate value. But let's actually calculate vector C in terms of $$V$$ and $$x$$, because this calculation can be generalized to the case where the feature we want to change is not on a basis vector.

First, let's describe what we want, and then translate that description into mathematics. Overall, we want:

"A vector which preserves the values of how much of x is used to get vector $$V$$".

Let's break this down into parts. To preserve the values of "how much of x is used to get vector $$V$$", we need to represent this phrase in terms of vectors. Recall from Chapter 1 that this can be done using the dot product, which projects one vector onto another, outputting a scalar that says "how much of x is used to get v".

<!--- v = [3 2] --->
So if $$\vec{v} = \color{#CBC3E3}{\begin{bmatrix} 3 \\ 2 \end{bmatrix}}$$, then $$\vec{x} \cdot \vec{v} = 3$$

Then, we scale the $$x$$ basis vector by x(dot)v by doing: x(dot)v * x

![Figure ](/ch2/VtoW_orth.PNG)

In Figure 2.3 above, we have found the vector, shown in pink, that represents "how much of x is used to get vector V". Now to "preserve" this value of x(dot)v while changing the value of y, we have to find a vector that's "orthogonal" to x(dot)v * x. As we saw in Figure 2.2 (link, then have way to link back to this paragraph from that fig), the orthogonal vector C is just the vector obtained by going from x(dot)v * x to v. In vector addition, that translates to: 

$$\vec{v} = (\vec{v} \cdot \vec{x}) * \vec{x} + \vec{C}$$

Solving for C, we obtain:

$$\vec{C} = \vec{v} - (\vec{v} \cdot \vec{x}) * \vec{x}$$

![Figure ](/ch2/equation_C.PNG)
