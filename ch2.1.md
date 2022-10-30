---
title: CHAPTER 2.1
---
<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>

**CHAPTER 2.1**

<a href="eduBlogHome.html">Home</a>

**(Reading time: 15 minutes)**

**Prerequisites**: Chapter 1, GANs [^prereqs1], and StyleGAN [^prereqs2]

[^prereqs1]: <a href="generative_models_review.html">A review of GANs can be found here (this is still an unfinished draft)</a>

[^prereqs2]: <a href="https://www.analyticsvidhya.com/blog/2021/05/stylegan-explained-in-less-than-five-minutes/"> A quick explanation of StyleGAN can be found here</a>

StyleGAN is a generative model that was designed for more control over which features are outputted in an image. It was found that its latent space was very "disentangled", meaning that one could have more control over one feature without affecting others [^styleSpace].

[^styleSpace]: https://paperswithcode.com/paper/stylespace-analysis-disentangled-controls-for

Let's consider a scenario where we have an image outputted by StyleGAN, but we want to change one or more features of the image while keeping the other features the same. For example, in the picture below, we have an outputted image on the left. Then on the right, we have another outputted image where most of the features such as hair color and eye color are kept the same as the left image, while the age is changed.

<figure>
<img src="/ch2/youngtoOld.PNG">

<figcaption align = "center"><b>Image Source:  Yujun Shen, Jinjin Gu, Xiaoou Tang, and Bolei Zhou. Interpreting the latent space of GANs for semantic face editing.
CoRR, abs/1907.10786, 2019. </b></figcaption>
</figure>

Recall from Chapter 1 that features can be approximated as vectors in the latent space of neuron activations.

<img src="/cob/fig6.PNG" width="500" height="300">

In the image above, the animal (a cat) is interpreted in terms of the features of Face Length and Body Size. For instance, by increasing the value of the "Body Size vector" on the y-axis from y=2 to y=3, we obtain a vector that is similar to the one mapped to the sample at (0.5, 2), but with a longer body. Given that the sample at (0.5, 2) represents an average cat, a sample at (0.5, 3) would represent a long cat.

When the feature we want to change is on the basis vector, all we have to do is change the value on the basis vector. But recall that features are not always on the basis vector; for instance, in the previous Chapter, we discussed a vector called "in terms of Cat", shown in orange in the figure below. This vector was mapped to a feature that measured how much "like a Cat" a sample was. When the basis vectors were "Face Length" and "Body Size", this vector "in terms of Cat" was not on the basis. 

<img src="/ch2/likeCat.PNG" width="400" height="300">

What if we had an image, say of a furry (an anthropomorphic animal-human hybrid cartoon), that originally had Cat features, but we want to increase these Cat features and make it **more** cat-like? For example, in the figure below, we would want to make the face on the left appear more animalistic, as on the right, while having the right image bear a resemblence to the one on the left in terms of features such as hair style, ears, smile, eye shape, skin tone, and more.

<figure>
<img src="/ch2/dangerouslyFurry.PNG">

<figcaption align = "center"><b> These are actual outputs by a StyleGAN trained on images of furries. </b></figcaption>
</figure>

If we perform a Change of Basis to measure our image on the left in terms of "Cat", then that would mean, in the second coordinate space, finding an image to the right of our image, with as little change in any other direction (such as Hair Style) as possible. Since Hair Style is measured on the y-axis, our second image should be as vertically aligned to the first image as much as possible. [^notRat]

[^notRat]: This is similar to the example in the previous Chapter, but instead of changing to a basis where "like a Rat" is mapped to the y-axis, the feature "Hair Style" is mapped to the y-axis. 

<img src="/ch2/likeCat_cob.PNG" width="600" height="300">

Note that when we move along the "Cat" vector but not along the "Hair Style" vector, we may still move along the "Ears" vector, demonstrating the difficulty of preserving as many features as possible while still deviating from one feature.

So if we only want to change one feature such as "cat-like", we should "move along" that "cat-like" feature vector. 

But how do we calculate [the vector we want to preserve..]? 

These calculations were found using a method presented in the paper "Interpreting the latent space of GANs for semantic face editing" [^cite1], which introduced a now widely used method for editing the features of StyleGAN generated images. We'll be explaining the intuition behind the mathematical calcuations in the paper.

[^cite1]: Yujun Shen, Jinjin Gu, Xiaoou Tang, and Bolei Zhou. Interpreting the latent space of GANs for semantic face editing. CoRR, abs/1907.10786, 2019.

**Changing a feature on the basis vector**

First, let's start with a simpler case, where the feature we want to change is on a basis vector. Say the Age vector is on the y-axis. In this example, we want to keep x=3, and move along the y-axis. We have a vector $$V=[3,2]$$, and we want to find a similar vector, $$W=[3,1]$$:

<!--- ![Figure ](/ch2/VtoW.PNG) --->
<img src="/ch2/VtoW.PNG" width="400" height="300">

In Figure 1, all we have to do is to find W is to "walk" down line $$C$$ from vector $$V$$. In fact, you can move to any point along $C$$ without changing the value of x=3. 

Why does vector C not change the value of x=3? Because vector $$C$$ is **orthogonal** to the $$x$$ basis vector, where they intersect at x=3. If it was not orthogonal, it would veer away from x=3, such as shown in the example below, where a non-orthogonal vector leads to x=4.

<img src="/ch2/VtoW_veer.PNG" width="400" height="300">

It is only when the green vector intersects the x vector at 90 degree angle that the value of the $$x$$ vector doesn't change.

How do we calculate the value of this orthogonal vector $$C$$ we want to move on?

In this case, because we want to keep the value of x and change the value of y, and y is a basis vector, we can move in the y-direction by simply changing the y-coordinate value. Notice that vector $$C$$ is parallel to the y-direction, and thus moving along $$C$$ means moving along $$y$$.

Even so, let's actually calculate vector C in terms of $$V$$ and $$x$$, because this calculation can be generalized to the case where the feature we want to change is not on a basis vector.

First, let's describe what we want, and then translate that description into mathematics. Overall, we want:

"A vector which preserves the values of how much of x is used to get vector $$V$$".

Let's break this down into parts. To preserve the values of "how much of x is used to get vector $$V$$", we need to represent this phrase in terms of vectors. Recall from Chapter 1 that this can be done using the dot product, which projects one vector onto another, outputting a scalar that says "how much of x is used to get v".

<!--- v = [3 2] --->
So if $$\vec{v} = \color{#CBC3E3}{\begin{bmatrix} 3 \\ 2 \end{bmatrix}}$$, then $$\vec{x} \cdot \vec{v} = 3$$

Then, we scale the $$x$$ basis vector by $$\vec{x} \cdot \vec{v}$$ by doing: 

$$(\vec{v} \cdot \vec{x}) * \vec{x}$$

<img src="/ch2/VtoW_orth.PNG" width="400" height="300">

In Figure 2.3 above, we have found the vector, shown in pink, that represents "how much of x is used to get vector V". Now to "preserve" this value of x(dot)v while changing the value of y, we have to find a vector that's "orthogonal" to $$(\vec{v} \cdot \vec{x}) * \vec{x}$$. As we saw in Figure 2.2 (link, then have way to link back to this paragraph from that fig), the orthogonal vector C is just the vector obtained by going from x(dot)v * x to v. In vector addition, that translates to: 

$$\vec{v} = (\vec{v} \cdot \vec{x}) * \vec{x} + \vec{C}$$

Solving for C, we obtain:

$$\vec{C} = \vec{v} - (\vec{v} \cdot \vec{x}) * \vec{x}$$

<img src="/ch2/equation_C.PNG" width="400" height="300">

We have gone over a simpler case where we already know the direction vector we should move in, because it's just a basis vector that's orthogonal to x. But what if the direction vector is **not** a known basis vector? How can we calculate it? We'll see soon that the calculation follows the same logic as the one for C that we did just now. 

**Changing a feature that's not on a basis vector**

(project x onto v now, instead of v onto x. this is b/c 'preserve as much of v' while just changing x)

(map v to the basis!)