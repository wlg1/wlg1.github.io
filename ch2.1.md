---
title: CHAPTER 2.1
---
<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>

**CHAPTER 2.1**

<a href="eduBlogHome.html">Home</a>

**(Reading time: 15 minutes)**

**Prerequisites**: Chapter 1, what is a GAN [^prereqs1], and what is StyleGAN [^prereqs2]

[^prereqs1]: In this section, all that's needed to know is that a GAN takes a latent vector z from a latent space- that is, a space that represents features much like the latent space of activations we discussed in Chapter 1- and outputs an image. Other concepts from GANs can enhance the connections made as this chapter is studied, but are not required. <a href="generative_models_review.html">A review of GANs can be found here (this is still an unfinished draft)</a>

[^prereqs2]: In this section, all you have to know is that StyleGAN is a type of generative model (a neural network that outputs an image). A deeper understanding of StyleGAN can enhance the connections made as this chapter is studied, but are not required. <a href="https://www.analyticsvidhya.com/blog/2021/05/stylegan-explained-in-less-than-five-minutes/"> A quick explanation of StyleGAN can be found here</a>

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

<img src="/ch2/likeCat_cob.PNG" width="700" height="300">

Note that when we move along the "Cat" vector but not along the "Hair Style" vector, we may still move along the "Ears" vector, demonstrating the difficulty of preserving as many features as possible while still deviating from one feature.

So if we only want to change one feature such as "cat-like", we should "move along" that "cat-like" feature vector. 

But how do we calculate [the vector we want to preserve..]? 

These calculations were found using a method presented in the paper "Interpreting the latent space of GANs for semantic face editing" [^cite1], which introduced a now widely used method for editing the features of StyleGAN generated images. We'll be explaining the intuition behind the mathematical calcuations in the paper.

[^cite1]: Yujun Shen, Jinjin Gu, Xiaoou Tang, and Bolei Zhou. Interpreting the latent space of GANs for semantic face editing. CoRR, abs/1907.10786, 2019.

**Changing a feature on the basis vector**

First, let's start with a simpler case, where the feature we want to change is on a basis vector. Say the Body Size vector is on the y-axis. We have a vector $$z=[3,2]$$ where Body Size = 2, and we want to find a similar vector, such as one where Body Size = 1. Since $$y = [0,1]$$, our feature vector Body Size is represented by $$y$$, so all we need to do is to add $$y$$ to $$z$$: 

$$\vec{z} + \alpha * \vec{y} $$

$$ = \begin{bmatrix} 3 \\ 2 \end{bmatrix} + \alpha * \begin{bmatrix} 0 \\ 1 \end{bmatrix}$$

In which $$\alpha$$ is a scalar of any real number [^real] that controls "how much" of Body Size $$y$$ is added.

[^real]: In a simplified definition, a real number is allowed to be a fraction, negative, irrational, but not imaginary. See: https://en.wikipedia.org/wiki/Real_number

Since vector addition adds the head of a vector with the tail of another vector, visually, this would look like:

<img src="/ch2/anyVecY.PNG" width="300" height="200">

Such that the yellow and blue vectors represent $$\alpha * \vec{y}$$ being added to vector $$z$$.

**Changing a feature NOT on the basis vector**

Next, let's change a feature that's not on the basis vector. Recall that a feature vector $$n$$ in a coordinate space is a measurement by the space's basis vectors. In other words, each feature can be expressed entirely by a linear combination of basis vectors. So if feature $$n$$ represents "cat-like", then how much a sample is like a cat is represented by its combination of Face Length to Body Size. 

<img src="/ch2/show_n.PNG" width="250" height="200">

---
(Click on the following optional section to expand it. It is optional reading as the validity of its interpretation is still up for questioning.)

<details>
<summary><b>Features and Gradients:</b> </summary>
<br><br>
In the case of using basis vectors as measurements, the entire line represented "how much" of a quantity there was.
<br><br>
In this case, the neural network has learned that a "typical" cat would have a Face Length of 0.5 and a Body Size of 2 (it learned to use this ratio to distinguish a cat from other animals in its dataset), so the ratio of Body Length to Face Length is 2:0.5, or 4. If a sample it sees has this ratio of around 4, it is "likely to be a cat". Ratios are relative, so even if we have absolute units of Body Length = 8 and Face Length = 2, the ratio 8:2 = 4 indicates to the neural network that this sample is more likely a cat than any other animal.
<br><br>
As taught in algebra, this is the slope of a line, where "rise/run" in this case means "Body Length / Face Length". But vectors do not have slopes; only functions have slopes, and lines are functions. It seems that the vectors that lie on the line with this slope all correspond to some feature.
<br><br>
Essentially, each feature is mapped to a line's <b>steepness and direction</b>, or its angle from the origin of basis vectors. It doesn't matter how big or small your stretch a vector- it is the steepness and direction, or the ratio, that is important.
<br><br>
Note that in higher dimensional spaces, instead of describing this ratio as "rise/run", it is better to use "steepness and direction" instead. You can say this is the <b>gradient</b> in gradient descent, in which how each neuron measures the data is changed according to the gradient. The vector is both an "object" measuring a feature, and a "relation" determining how a feature is used to change another feature.
<br><br>
How features relate to functions and their gradients is still unclear, and remains a subject of further investigation.

</details>
<br>

---

Similar to the example we showed where the feature is on the basis vector, we want to "add" feature n to z. What does this actually mean? 

In the previous example, all we had to do to change $$z$$ by $$y$$ was $$\vec{z} + \alpha * \vec{y}$$, because the feature on $$y$$ did not require any units of $$x$$ to be represented. But now, the feature cat is represented by vector $$n$$ using BOTH units of $$x$$ and $$y$$. So instead of just adding $$y$$, we have to add both $$x$$ and $$y$$:

$$\vec{z} + \alpha * (0.5 * \vec{x} + 2 * \vec{y})$$

Since feature cat is $$\vec{n} = 0.5 * \vec{x} + 2 * \vec{y}$$, this linear combination can be rewritten as:

$$\vec{z} + \alpha * \vec{n}$$

Visually, this would look like:

<img src="/ch2/z_plus_n.PNG" width="300" height="200">

Using $$\alpha$$, we can add or subtract as many units of "cat" to z as we like.

<img src="/ch2/z_plus_alphan.PNG" width="350" height="300">

At first, it's not obvious how we "change z by n cat units". So let's perform a change of basis where the cat feature is mapped to a basis vector, to truly show how each sample is measured in cats:

<img src="/ch2/z_plus_alphan_COB.PNG">

We can get better intuition of this when it's animated:

<video src="https://user-images.githubusercontent.com/169707/126715420-991ad821-9ac8-4b66-b79e-e0966e0f3a89.mp4" controls="controls" style="max-width: 730px;">
</video>

Now each sample, shown as dots in the figure, can be interpreted as having "units of cat", represented in orange. The red dot, originally on vector $$\vec{z} + \vec{n}$$, is close to having "1" cat unit. The blue dot, originally on $$\vec{z} + (0)\vec{n}$$, is close to having "0" cat units. The same goes for the green and white dots, having -1 and -1.5 cat units, respectively. We see that the number of cat units corresponds to $$\alpha$$ in the equation $$\vec{z} + \alpha * \vec{n}$$.[^approx]

[^approx]: Each one may only be "close" to the number of cat units due to the decimal point approximations used in the matrix to represent the actual values.

What was the matrix $$M$$ used to perform this change of basis? Recall that each column of a matrix is a coordinate where features on basis vectors are sent **to**. So to send a feature on $$[1,0]$$ to $$[0.5, 2]$$, we would use the matrix:

<p align="center">
$$ W = \begin{bmatrix} 0.5 & ? \\ 2 & ? \end{bmatrix} $$
</p>

Note that we have stated what will be sent to one basis vector; but in 2D coordinate space, there are two, so let's find where to send the second one. To avoid too many changes in the coordinate space, let's use a rotation matrix. A rotation matrix requires that the two column vector are at 90 degree angles, <a href="https://sciencing.com/vector-perpendicular-8419773.html
"> so we'll use a technique to find a vector that's 90 degrees to [0.5, 2].</a> Then this rotation matrix is:

<p align="center">
$$ W = \begin{bmatrix} 0.5 & -1 \\ 2 & -0.25 \end{bmatrix} $$
</p>

However, this is NOT the matrix $$M$$ we use to perform the change of basis above. We don't want to send a basis vector to a certain coordinate; we want to do the opposite, where we send a feature **from** a coordinate to a basis vector. So we have to take the inverse of the matrix in order to send the cat feature from $$[0.5, 2]$$ to $$[1, 0]$$. The inverse of the matrix above, rounded to 4 decimal places, is:

<p align="center">
$$ M = W^{-1} = \begin{bmatrix} -0.1333 & 0.5333 \\ -1.0667 & 0.2667 \end{bmatrix} $$
</p>

This is the matrix $$M$$ we use to perform the change of basis in the example above.

In the example above, note how each sample has different values of n, but all have the same value (close to -3) along the 2nd basis vector. Why are the values along this 2nd basis vector, which is mapped to a feature that is 90 degrees to the cat feature vector, preserved after $$\vec{z} + \alpha * \vec{n}$$? We'll find out why in the next section.

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