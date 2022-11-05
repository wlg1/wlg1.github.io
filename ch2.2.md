---
title: CHAPTER 2.2
---
<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>

<center><h2>CHAPTER 2.2: Conditioning on Features using Orthogonal Projection</h2></center>

<a href="eduBlogHome.html">Home</a>

**(Reading time: 7 minutes)**

Now we want to change a feature $$n_1$$ while keeping the value of **another** feature $$n_2$$ the same. The difficulty in doing this is that each feature vector is made up of the same basis vectors (neurons), so by changing feature $$n_1$$, you are changing the basis vectors that add up to $$n_1$$, and since you are those basis vectors are also used to add up to $$n_2$$, you are also changing $$n_2$$. 

In other words, a sample lies on a point in a high dimensional latent space of potentially billions of neurons. A feature vector lies along a subspace- a plane- within this latent space. Projecting the sample down to this feature subspace (that is, finding its "shadow" or its "distorted reflection" on the plane) measures how much of the feature that sample has. 

So when you move a sample from one point to another, the shadow won't just change on one feature subspace, but another feature subspace. For example, if you are ever stuck in a hall of mirrors, you may find yourself next to two mirrors- one that makes you larger, and one that makes you small. When you move one way, you are not just changing how you look in the "Larger" mirror, but also how you look in the "smaller" mirror.[^projectionAbstraction]

<figure>
<img src="/ch2/mirrors.jpeg" width= 300>

<figcaption align = "center"><b> Source: https://www.thisiswhyimbroke.com/uk/warping-mirrors/ </b></figcaption>
</figure>

[^projectionAbstraction]: By pure speculation, this may be related to how the brains of organisms organize concepts, and why concepts are related to one another by analogy. An analogy relates an "abstraction" of concepts- such as abstracting the Hero's Journey in The Hunger Games and in Harry Potter. There is some sort of semantic (but possibly superficial, and thus meaningless) similarity between Projection and Abstraction. Abstractions also occur in dreams, where a memory of an angry neighbor yelling at his lawn may be substituted with the dream of an angry teacher yelling at his lawn, which has never occurred in real life. Now projecting down to different abstractions would mean if the way a sample is mapped to one abstraction framework is changed, then the way it's mapped to another abstraction framework is also changed. So say you're trying to think of a way to create a novel concept by slightly tweaking an existing concept. The difficulty is that <b>some abstraction frameworks cannot be changed in order to preserve the concept itself.</b> For example, you want to write a story that has the same "beats" as Star Wars. Now your story contains an abstraction of "Star Wars", and also an abstraction on "The Hero's Journey". If you want to get rid of "The Call to Adventure", you would also shake your story away from "The Hero's Journey". (NOTE: This is not a good example, so further thought will be put into it).

When changing one feature vector affects another, the feature vectors are **entangled**. However, it is possible to find a <b><span style="color:purple;">new</span></b> feature vector that will <span style="color:red"><i>cast the new desired shadow on</i></span> $$n_1$$ but also <span style="color:blue;"><i>tries not to change the existing shadow projected onto</i></span> $$n_2$$. This procedure will find a vector **disentangled** to $$n_2$$.

Thus, we will have to find a new vector to add to our sample $$z$$.

**Changing a feature while keeping another feature on the basis vector**

In the previous section, we already saw a case where the feature we want to change, $$y$$, is on the basis vector.

<img src="/ch2/anyVecY.PNG" width="300" height="200">

Notice that all the new samples have the same value: x = 3. So changing y doesn't change x. Also note that the x-axis basis vector and the y-axis basis vector are at a 90 degree angle to each other. This should give a hint as to where we're going with this.

---

Let's start with the case where sample $$z = [3, 1]$$, and the feature $$n_1 = [1.5, 1]$$ we want to change is **not** on a basis vector, but the feature $$n_2$$ whose value of a sample we want to keep is on a basis vector. To find a new feature vector $$c$$ to add to $$z$$, we want $$c$$ to keep $$n_2 = 3$$, but want the other parts of $$c$$ be as close to $$n_1$$ as possible.

<img src="/ch2/z_plus_c.PNG" height="300">

In the figure above, we see that vector $$z + c$$ keeps as much of $$n_1 = [1.5, 1]$$ as possible- that is, it still lies at $$y = 1 + 1 = 2$$ just like $$z + n_1$$, but also keeps $$n_2 = 3$$, in contrast to $$z + n_1$$, which moves $$n_2$$ to 4.5.

Let's reframe these vectors $$n_1$$, $$n_2$$ and $$c$$ by moving them to the origin, and independent of $$z$$. Given that $$c$$ is a vector and thus is actually just has no true coordinates, just an object with length and direction [^vector], we can move it to the right.

[^vector]: There is a difference between points on a coordinate space and a vector. A vector is mapped onto points in a coordinate space, but it is NOT the point in a coordinate space it is mapped on. Given that it just has length and direction, it can be moved freely anywhere on a coordinate space. The vector's components are NOT points on a coordinate space, but a way to capture the vector's length and magnitude in terms of the coordinate space's basis vectors. This also means that the data point, or feature, that the vector is mapped to can be moved freely anywhere on a coordinate space! What's important is how features and vectors are relative to other features and vectors in the current coordinate space.

<img src="/ch2/n1_n2_c.PNG" width="400" height="300">

Why does vector $$c$$ not change the value of $$y=1$$? Because vector $$c$$ is **orthogonal** to $$n_2$$, meaning they are at a 90 degree angle, where they intersect at $$n_2 = 1$$. If it was not orthogonal, it would veer away from $$n_2 = 1$$, such as shown in the example below, where a non-orthogonal vector leads to $$n_2 = 2.1$$.

<img src="/ch2/n1_n2_veer.PNG" width="400" height="300">

How do we calculate the value of this orthogonal vector $$c$$?

In this case, because $$n_1$$ is a sum of $$n_2$$ and $$y$$, and $$n_2$$ is a basis vector, when we "remove" $$n_2$$ from $$n_1$$, we are just left with $$y$$, so we can move in the y-direction by simply changing the y-coordinate value. Notice that vector $$c$$ is parallel to the y-direction, and thus moving along $$c$$ means moving along $$y$$.

Even so, let's actually calculate vector $$c$$ in terms of $$v$$ and $$x$$, because this calculation can be generalized to the case where the feature we want to change is not on a basis vector.

First, let's describe what we want, and then translate that description into mathematics. Overall, we want:

"A vector which preserves the values of how much of $$n_2$$ is used to get vector $$n_1$$".

Let's break this down into parts. To preserve the values of "how much of $$n_2$$ is used to get vector $$n_1$$", we need to represent this phrase in terms of vectors. Recall from Chapter 1 that this can be done using the dot product, which projects one vector onto another, outputting a scalar that says "how much of $$n_2$$ is used to get vector $$n_1$$".

So if $$\vec{n_1} = \color{red}{\begin{bmatrix} 1.5 \\ 1 \end{bmatrix}}$$, then $$\vec{n_1} \cdot \vec{n_2} = 1.5$$

Then, we scale the $$n_2$$ basis vector by $$\vec{n_1} \cdot \vec{n_2}$$ by doing: 

$$(\vec{n_1} \cdot \vec{n_2}) * \vec{n_2}$$

<img src="/ch2/n1_n2_orth.PNG" height="300">

In Figure 2.3 above, we have found the vector, shown in light blue, that represents "how much of $$n_2$$ is used to get vector $$n_1$$". Now to "preserve" this value of $$(\vec{n_1} \cdot \vec{n_2})$$ while changing as much of $$n_1$$ as we can, we have to calculate the vector $$c$$ that's "orthogonal" to $$(\vec{n_1} \cdot \vec{n_2}) * \vec{n_2}$$. Since $$c$$ starts at the head of $$(\vec{n_1} \cdot \vec{n_2})$$ and ends at the head of $$\vec{n_1}$$, in vector addition, that translates to: 

$$\vec{n_1} = (\vec{n_1} \cdot \vec{n_2}) * \vec{n_2} + \vec{c}$$

Solving for $$\vec{c}$$, we obtain:

$$\vec{c} = \vec{n_1} - (\vec{n_1} \cdot \vec{n_2}) * \vec{n_2}$$

<img src="/ch2/n1_n2_orth_eqn.PNG" height="300">

And so any sample along:

$$\vec{z} + \alpha * \vec{c}$$

Would be a sample that fits our criteria. No matter what value of $$\alpha$$ we use, we see that $$\alpha * \vec{c}$$ is as close to $$\alpha * \vec{n_1}$$ as possible while keeping $$n_2 = 3$$:

<img src="/ch2/z_plus_alphaC.PNG" height="300">

Let's further analyze this by plugging in specific values. 

$$\vec{c} = \vec{n_1} - (\vec{n_1} \cdot \vec{n_2}) * \vec{n_2} = [1.5, 1] - (1.5) * [1, 0] = [1.5 - 1.5, 1] = [0,1]$$

We see that this subtraction is actually "removing" parts of $$n_2$$ from $$n_1$$ to obtain $$c$$, which is just $$y$$ in this case. But what if $$n_2$$ was **not** on the basis, and thus was not orthogonal to $$y$$ or any other basis vector? We'll see soon that the calculation follows the same logic as the one for C that we did just now. 

**Changing a feature while keeping another feature IN GENERAL**

Now let's say we have a feature vector $$n_1 = (1,2)$$ and feature vector $$n_2 = (2,1) $$. Based on the previous section, we want to find samples along the purple line in the figure below:

<img src="/ch2/nonBasisFeat.PNG" width="400" height="300">

Recall from the previous section that if we wanted to vary the features of a vector $$n_1$$, but wanted to keep the value at vector $$n_2$$, we used the equation:

<center><img src="/ch2/varies_same_1.PNG" width="300" height="100"></center>

Here, let's use a similar version of the equation, but we will slightly modify the dot product projection to include a denominator term, as shown below:

$$ \frac{(\vec{n_1} \cdot \vec{n_2}) }{(\vec{n_2} \cdot \vec{n_2}) } * \vec{n_2} $$

The reason this denominator was not needed in the previous example was because it measures the length of the vector being projected onto; in that case, vector $$\vec{n_2}$$ was a basis vector with a length of 1, so this term simplified to just the numerator.

Then our equation for finding $$c$$ becomes:

$$\vec{c} = \vec{n_1} - \frac{(\vec{n_1} \cdot \vec{n_2}) }{(\vec{n_2} \cdot \vec{n_2}) } * \vec{n_2} * \vec{n_2} $$

This is the equation for **orthogonal projection**, which will find the vector scaled on $$n_2$$ that's closest to $$n_1$$. The proof for the equation is linked in the footnotes.[^orthProofs]

[^orthProofs]: <a href="https://textbooks.math.gatech.edu/ila/projections.html"> Proof for the orthogonal projection equation</a>. Find it using ctrl+f "Recipe: Orthogonal projection onto a line". <a href="https://www.robertosmathnotes.com/uploads/8/2/3/9/8239617/la1-9_orthogonal_projections.pdf"> Another resource is here.</a>

But why is this the case? We don't immediately see how this "preserves" the other features of $$n_2$$, like we saw how $$n_2 = 3$$ was preserved by going orthogonal to it in the previous example. Intuitively, it becomes more obvious when we perform a change of basis to measure our data in terms of $$n_2$$:



When there are more than two dimensions, this removal will leave more than just the basis vector

Essentially, this manipulation cannot make ALL features stay the same. We must know beforehand which features we want to stay the same, and which features we want to vary. Then, we will condition on the features we want to stay the same


---
---