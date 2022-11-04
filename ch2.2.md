---
title: CHAPTER 2.2
---
<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>

**CHAPTER 2.2**

<a href="eduBlogHome.html">Home</a>

**(Reading time: 7 minutes)**

**Changing a feature while keeping another feature on the basis vector**

Now we want to change a feature while keeping **another** feature the same. Let's start with the case where the feature we want to change is on a basis vector. In this example, we want to keep x=3, and move along the y-axis. We have a vector $$z=[3,2]$$, and we want to find a similar vector, $$W=[3,1]$$:

<!--- ![Figure ](/ch2/VtoW.PNG) --->
<img src="/ch2/VtoW.PNG" width="400" height="300">

In Figure 1, all we have to do is to find W is to "walk" down line $$c$$ from vector $$v$$. In fact, you can move to any point along $$c$$ without changing the value of x=3. 

Why does vector C not change the value of x=3? Because vector $$c$$ is **orthogonal** to the $$x$$ basis vector, where they intersect at x=3. If it was not orthogonal, it would veer away from x=3, such as shown in the example below, where a non-orthogonal vector leads to x=4.

<img src="/ch2/VtoW_veer.PNG" width="400" height="300">

It is only when the green vector intersects the x vector at 90 degree angle that the value of the $$x$$ vector doesn't change.

How do we calculate the value of this orthogonal vector $$c$$ we want to move on?

In this case, because we want to keep the value of x and change the value of y, and y is a basis vector, we can move in the y-direction by simply changing the y-coordinate value. Notice that vector $$c$$ is parallel to the y-direction, and thus moving along $$c$$ means moving along $$y$$.

Even so, let's actually calculate vector $$c$$ in terms of $$v$$ and $$x$$, because this calculation can be generalized to the case where the feature we want to change is not on a basis vector.

First, let's describe what we want, and then translate that description into mathematics. Overall, we want:

"A vector which preserves the values of how much of x is used to get vector $$v$$".

Let's break this down into parts. To preserve the values of "how much of x is used to get vector $$v$$", we need to represent this phrase in terms of vectors. Recall from Chapter 1 that this can be done using the dot product, which projects one vector onto another, outputting a scalar that says "how much of x is used to get v".

<!--- v = [3 2] --->
So if $$\vec{v} = \color{#CBC3E3}{\begin{bmatrix} 3 \\ 2 \end{bmatrix}}$$, then $$\vec{x} \cdot \vec{v} = 3$$

Then, we scale the $$x$$ basis vector by $$\vec{x} \cdot \vec{v}$$ by doing: 

$$(\vec{v} \cdot \vec{x}) * \vec{x}$$

<img src="/ch2/VtoW_orth.PNG" width="400" height="300">

In Figure 2.3 above, we have found the vector, shown in pink, that represents "how much of x is used to get vector V". Now to "preserve" this value of x(dot)v while changing the value of y, we have to find a vector that's "orthogonal" to $$(\vec{v} \cdot \vec{x}) * \vec{x}$$. As we saw in Figure 2.2 (link, then have way to link back to this paragraph from that fig), the orthogonal vector $$c$$ is just the vector obtained by going from x(dot)v * x to v. In vector addition, that translates to: 

$$\vec{v} = (\vec{v} \cdot \vec{x}) * \vec{x} + \vec{c}$$

Solving for C, we obtain:

$$\vec{c} = \vec{v} - (\vec{v} \cdot \vec{x}) * \vec{x}$$

<img src="/ch2/equation_C.PNG" width="400" height="300">

And so any sample along:

$$\vec{v} + \alpha * \vec{c}$$

Would be a sample that fits our criteria of keeping x = 3. In the figure below, all the blue vectors are samples in which x = 3:

<img src="/ch2/anyVecC.PNG" width="400" height="300">
<!--- change_feat_on_basis, anyVecC.py --->

We have just gone over a simpler case where the direction vector we should move in is just a basis vector that's orthogonal to x. But what if the direction vector is **not** a known basis vector? How can we calculate it? We'll see soon that the calculation follows the same logic as the one for C that we did just now. 

**Changing a feature that's not on a basis vector**

Now let's say we have a sample vector $$V = (1,2)$$ and feature vector $$HEIGHT = (2,1) $$. We want to find samples which have the same height as $$v$$, but which vary other features. In other words, based on the previous section, we want to find samples along the green line in the figure below:

<img src="/ch2/nonBasisFeat.PNG" width="400" height="300">

Recall from the previous section that if we wanted to vary the features of a vector $$v$$, but wanted to keep the value of x=3 at vector $$x$$, we used the equation:

<img src="/ch2/varies_same_1.PNG" width="300" height="100">

Here, let's use a similar version of the equation, but use orthogonal projection instead. This will find the vector scaled on $$HEIGHT$$ that's closest to $$v$$. The equation for orthogonal projection is:

$$ \frac{(\vec{v} \cdot \vec{HEIGHT}) }{(\vec{HEIGHT} \cdot \vec{HEIGHT}) } * \vec{HEIGHT} $$

Then our equation for finding the green vector becomes:

$$\vec{c} = \vec{v} - \frac{(\vec{v} \cdot \vec{HEIGHT}) }{(\vec{HEIGHT} \cdot \vec{HEIGHT}) } * \vec{HEIGHT} $$

Any sample along:

$$\vec{v} + \alpha * \vec{c}$$

... would vary features of $$AGE$$ while keeping the other features of $$n_2$$ roughly the same.

But why is this the case? When don't immediately see how this "preserves" the other features of $$n_2$$, like we saw how x=3 was preserved by going orthogonal to it in the previous section. Intuitively, it becomes more obvious when we perform a change of basis to measure our data in terms of $$n_2$$:


OUTLINE:
1. introduce n1, n2
2. apply technique above but now need orth proj
    We had dot product onto a vector...
    Now, we need orthogonal projection to find the closest
    add c to v, not cv, b/c only use cv to get DIRECTION. v is the actual sample. get variations in increments
3. equation breakdown: varies, doesn't vary
    question why this won't vary n2
4. rotate v onto basis using inverse of rotation
    to find rotation, find orthogonal. we have C
5. plot v, v+c, and v+2c, etc onto new coord space
    observe that they're all orthogonal to v, just like in previous section

If we have multiple features we want to change, but 

We have to be aware of which features 

Essentially, this manipulation cannot make ALL features stay the same. We must know beforehand which features we want to stay the same, and which features we want to vary. Then, we will condition on the features we want to stay the same

Note that this conditioning cannot force



(project x onto v now, instead of v onto x. this is b/c 'preserve as much of v' while just changing x)

(map v to the basis!)
(the 2nd basis vector is just a feature that is orthogonal to v, allowing for a rotation, as rotations are orthogonal matrices)

---
---