---
theme: jekyll-theme-minimal
title: CHAPTER 1.1
---

<!-- <head>
    <link rel="stylesheet" href="index.css">
</head> -->

<!-- <div class="topnav">
  <a class="active" href="eduBlogHome.html">Home</a>
  <a href="#contact">Contact</a>
  <a href="#about">About</a>
</div>
<br> -->

<div>
  <a href="eduBlogHome.html">Home</a>
</div>
<br>

<center><h2>CHAPTER 1.1: How does Matrix Multiplication Guess it's a Cat from its Face and Body?</h2></center>

**(Reading time: 7 minutes)**

**Prerequisites**: A vague understanding of matrix multiplication and neural networks. [^prereqs]

[^prereqs]: <a href="https://www.youtube.com/watch?v=fNk_zzaMoSs&list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab&index=1&ab_channel=3Blue1Brown"> This Chapter is heavily built on 3Blue1Brown's Essence of Linear Algebra. </a> There are 16 videos, but you only have to focus on five videos: 1 to 3, then 9 and 13. 

---

Let's start with an example that will show us how matrix multiplication transforms data to reveal new insights. Say there's a population of cats and rats, and we represent them in a dataset. However, the dataset is only able to measure two features: body size, and face length (or more specifically, snout length).

![Figure 1: Cat](/ch1/fig1.png)
<!--- middle overlays shapes on top of actual cat. label bottom right as 'data sample'--->

So every entity (a cat or rat) in the population is represented in the dataset as an data sample, which is an abstraction defined only by body size and face length, such that their values are measured in "units". We can represent the data samples in this dataset as points in a coordinate space, using the two features as axes. The figure below shows the dataset on the left, and its coordinate space representation on the right. The top part shows the data points using numbers, and the bottom part shows how each data point corresponds to a data sample:

![Figure 2](/ch1/fig2.PNG)
![Figure 3](/ch1/fig3.PNG)
<!---Make dataset image: first row is face, second row is body, third row is data pt (combo of both) using #s, then show in coord sys on right. Then in 2nd image, turn all numbers into imgs, and again show in coordsys on right.--->

Let's look at our coordinate space with only the data samples corresponding to unit 1:

<img src="/ch1/fig4.PNG" height="300">

Every data point is a combination of the "unit 1" points, which represent <img src="/ch1/face1.PNG" width="50" height="40"> and <img src="/ch1/body1.PNG" width="50" height="40">. For instance, the data point (0.5, 2), which represents <img src="/ch1/cat.PNG" width="50" height="40">, is a weighted combination of 0.5 * <img src="/ch1/face1.PNG" width="50" height="40"> and 2* <img src="/ch1/body1.PNG" width="50" height="40">

<hr style="border:0.3px solid gray;width:90%;margin-left:auto;margin-right:auto"> 
![Figure 5: Linear Combination](/ch1/fig5.PNG)
<hr style="border:0.3px solid gray;width:90%;margin-left:auto;margin-right:auto"> 

If we see each data point as a vector, then every vector such as <img src="/ch1/cat.PNG" width="50" height="40"> is an addition of <img src="/ch1/face1.PNG" width="50" height="40"> and <img src="/ch1/body1.PNG" width="50" height="40">, which are **basis vectors**. Thus (0.5, 2) can also be represented as $$\begin{bmatrix} 0.5 \\ 2 \end{bmatrix} = 0.5 \begin{bmatrix} 1 \\ 0 \end{bmatrix} + 2 \begin{bmatrix} 0 \\ 1 \end{bmatrix}$$

<img src="/ch1/fig6.PNG" height="350">
<!---
![Figure 6: Cat in Coordinate Space](/ch1/fig6.PNG)
[under each body size pic, number it so reader knows if it's 1, 2, etc. The 2 glues two 1s together, showing the border, the 0.5 shows the other half grayed out, etc. This is to indicate they're scaling the unit vector. But [cat pic] does not do this, since it's not always measured using bodysize or face length, it's just pure data that can be represented using different features. you can show the addition with an 'intermediate step' that shows gluing them on, then removing the borders/faded. can also be gif]--->

---

Now, there are other ways we can measure the data samples in this population. Instead of labeling each data sample using the face & body measurements, let's label each data sample using the following two measurements: 

1) How likely it is to be a <span style="color:orange">Cat</span> 

2) How likely it is to be a <span style="color:green">Rat</span> 

How do we find the values of these new, and currently unknown, measurements? We can calculate them using our previous known measurements, face & body. For example:

Shorter <span style="color:#FA8072">face</span> + Bigger <span style="color:#ADD8E6">body</span>  = <span style="color:orange">Cat</span> 

Longer <span style="color:#FA8072">face</span> + Smaller <span style="color:#ADD8E6">body</span>  = <span style="color:green">Rat</span> 

<!---
Or in terms of basis vector addition:

Fig 7
[figure showing the analogy: 
Bigger body + Shorter face = Likely a Cat
2 * [body pic X] + 0.5 * [face pic Y] = value 2X+0.5Y on cat axes ]

[X and Y are on the row of the matrix corresponding to 'likely a cat'. They are the x values of body1 and face1's new coords in Model 2 ]
--->

What are $$face_{cat}$$ and $$body_{cat}$$? These are how much each feature is weighted by to calculate the score of "likely to be cat". The higher the weight, the more that feature is taken into account during calculation. For example, it might be more important to know the body size than the face length when determining if something is a cat or a rat, since cats are usually much bigger than rats, but their faces aren't always much shorter. Since body size is more important, we'd set $$body_{cat} = 1.5 > face_{cat} = 1$$. We will reveal how these weights are related to the matrix once we get into the algebra of matrix multiplication in Chapter 1.3.

Each measurement acts as a basis vector used to define each data sample. Because this second set of measurements uses different basis vectors than the set of face & body sizes, it forms a different coordinate space. Since each coordinate space provides a different way to **represent** the data, let's call each coordinate space a **Model**. 

The face & body size coordinate space will be called Model 1, and the 'likely to be' cat or rat coordinate space be called Model 2. As these two measurement methods are measuring the same data samples, the data samples in Model 1 are present in Model 2, but are now measured by different vectors.

In fact, since we are using Model 1 to calculate the values for Model 2, we will see in Chapter 1.3 that we are applying the dot product on face & body to calculate 'likely to be cat'. Recall that the steps of matrix multiplication consists of dot products; thus, the calculation of Model 2 is none other than matrix multiplication, which was, for certain matrices, <a href="https://www.3blue1brown.com/lessons/linear-transformations">shown here</a> to be a rotation. In these examples, we choose a matrix that, upon multiplication, corresponds to a rotation. 

<!---ANIMATION: rotation w/o coordinate space [Model 1 fades on 'likely a cat' and 'likely a rat'. then it shifts.]--->

For our examples, say that a vector **labels** a data sample if it points to it. We know in Model 1 that $$\color{#FA8072}{\begin{bmatrix} 1 \\ 0 \end{bmatrix}}$$ points to <img src="/ch1/face1.PNG" width="50" height="40">. But does this vector point to the same data sample in Model 2? 

Let's look at the two Models. We'll use the Orange Dot to denote <span style="color:orange">"likely to be a cat with unit 1"</span>[^1], and use the Green Dot to denote <span style="color:green">"likely to be a rat with unit 1"</span>.

<!--- Animation then before/after stills:
(Use pic of actual cat with 'likely' over it?)
[coordinate space and labeled vectors don't change, and there's only 1. Only objs prev on basis vectors move.]
[as it's changing, the old basis labels shift too. the word 'body size' shifts into a non-axes vector, but the word 'likely a cat' shifts onto the basis vector. all 4 axes concepts are present.]
[ Another way to fade is to first show images, then fade away into colored dots, then move dots, and fade images back in.]
https://docs.manim.community/en/stable/reference/manim.animation.fading.FadeOut.html
Or fade out still image using video editor--->

![Figure 8](/ch1/fig8.PNG)

The two $$\color{#FA8072}{\begin{bmatrix} 1 \\ 0 \end{bmatrix}}$$ in each Model do not label the same data point! Likewise, $$\color{#ADD8E6}{\begin{bmatrix} 0 \\ 1 \end{bmatrix}}$$ points to <img src="/ch1/body1.PNG" width="50" height="40"> in Model 1, but does not point to it in Model 2. Phrasing this a different way makes this idea more intuitive: let's say that the **meaning** of a vector is the data sample it points to. $$\color{#FA8072}{\begin{bmatrix} 1 \\ 0 \end{bmatrix}}$$ no longer has the same meaning in Model 2 as it did in Model 1. This is because the meaning of a vector depends on its basis vectors. In Model 1, $$\color{#FA8072}{\begin{bmatrix} 1 \\ 0 \end{bmatrix}}$$ pointed to <img src="/ch1/face1.PNG" width="50" height="40"> because it's supposed to mean "has a face with unit 1". In Model 2, $$\color{#FA8072}{\begin{bmatrix} 1 \\ 0 \end{bmatrix}}$$ points to <span style="color:orange">Orange Dot</span> because it's supposed to mean "likely to be a cat with unit 1".[^1]


[^1]: What does it mean to have 1 unit of "likely a cat?" For our example, we generalize these units to allow any 'probabilistic' measurement to be used, as long as having X+1 units means 'it is more likely to be" than having X units.

<!---* note that [body size 1] is present in Model 2, even though it's missing [face length]. In other words, it's [body size 1] + 0 * [face length 1]. This means that any data point which only contains a body of size 1 is seen as [meaning in terms of basis jk]--->

If it's still not clear why meaning depends on the choice of basis vectors, let's look at a better example that will help drive home this idea. We know in Model 1 that $$\color{#CBC3E3}{\begin{bmatrix} 0.5 \\ 2 \end{bmatrix}}$$ labels <img src="/ch1/cat.PNG" width="50" height="40">. But just like before, $$\color{#CBC3E3}{\begin{bmatrix} 0.5 \\ 2 \end{bmatrix}}$$ in Model 2 does not.

![Figure 10](/ch1/fig10.PNG)
<!---
<img src="/ch1/fig10a.png" width="300" height="200">
<img src="/ch1/fig10b.png" width="300" height="200">
--->

<!---
[[2 0.5] catpic in Model 1 and [2 0.5] in Model 1 on 2. I vector is fixed. unlike prev anim, fade j,k only after change basis so not too cluttered]
[labels cat pic on left, and nothing on right] [color code or include pic of vector when referring to [2 0.5] in text paragraph]
--->

Recall that in Model 1, which uses the face & body sizes as basis vectors, $$\color{#CBC3E3}{\begin{bmatrix} 0.5 \\ 2 \end{bmatrix}}$$ meant "an entity with a short face (0.5) and a long body (2)." But in Model 2, this vector means "it's NOT as likely to be a cat (0.5), as it is more likely to be a rat (2)". The meaning in Model 2 does not point to <img src="/ch1/cat.PNG" width="50" height="40">, because that data sample is likely a cat. Instead, it should point to a data sample that looks more like a rat.

<!---
In fact, $$\begin{bmatrix} 0.5 \\ 2 \end{bmatrix}$$ should now point to [rat pic], instead of <img src="/ch1/cat.PNG" width="50" height="40">.

Apply inv of matrix onto [0.5, 2] to get rat pic in Model 1, which you use to construct body and face sizes

1 1.5
-1.5 1

0.30769230769230769231  -0.46153846153846153845
0.46153846153846153846  0.3076923076923076923

You get:
1   -0.76923076923076927
2   0.84615384615384618

DO THIS LATER- this is b/c this is a bad matrix to use for classif rat/cat based on body/face (used b/c rotation more intuitive. The good matrix to use is less intuitive.)

Fig ??
[now fill in what [2 0.5] is in Sys 2]
--->

This shows the difference between the data samples coming from the real world, and the model that represents those data samples using labels. $$\color{#CBC3E3}{\begin{bmatrix} 0.5 \\ 2 \end{bmatrix}}$$ is not <img src="/ch1/cat.PNG" width="50" height="40"> itself; it is merely a label of it, and whichever label is used depends on the basis vectors used to define the parts of each label. Note that there is a difference between points, vectors and features. [^vector]

[^vector]: However, there is a difference between points on a coordinate space and a vector. A vector is mapped onto points in a coordinate space, but it is NOT the point in a coordinate space it is mapped on. Given that it just has length and direction, it can be moved freely anywhere on a coordinate space. The vector's components are NOT points on a coordinate space, but a way to capture the vector's length and magnitude in terms of the coordinate space's basis vectors. This also means that the data point, or feature, that the vector is mapped to can be moved freely anywhere on a coordinate space! What's important is how features and vectors are relative to other features and vectors in the current coordinate space.

<p align="center">
<!---$$\begin{bmatrix} 0.5 \\ 2 \end{bmatrix} \neq $$ <img src="/ch1/cat.PNG" width="50" height="40">--->
<img src="/ch1/vecNotCat.PNG" height="75">
</p>

Understanding the difference between a model representation and the actual entity it means (or points to) is crucial for gaining better intuition behind why matrix multiplication reveals hidden information in data sets.[^entity_model]

<!--- Fig 11 [animated reality of concepts vs fixed coord space model]--->

We show below how the features on the two basis vectors in Model 1 are rotated onto two new vectors in Model 2. This is done by matrix multiplication, causing the basis vectors in Model 2 to now point to the <span style="color:orange">Orange Dot</span> and <span style="color:green">Green Dot</span>; Chapter 1.3 will make it even more clear why matrix multiplication is called a "Change of Basis".

![2mod_vecs](/ch1/2mod_vecs.PNG)

<!---[Model 1, and Model 1 on top of Model 2. WITH vectors.]
in the vector on top of model pic, color them the same, only darker--->


Notice that Model 2 demonstrates an idealized, simplified example of what a neural network does- it is making a guess about the data point given to it as input. In fact, one can think of it as a single layer 'neural network'[^1-layer-NN] such that for the function that calculates the neuron activations:

<p align="center">
$$O = \sigma(WX + b)$$
</p>

Which, for a data sample, outputs the values it guesses for the 2 classes {cat, rat}, it sets $$\sigma = I$$, the identity function, and b = 0:

<p align="center">
$$O = WX$$
</p>

[^1-layer-NN]: https://ml4a.github.io/ml4a/how_neural_networks_are_trained/

![2mod_out](/ch1/2mod_out.PNG)

<!---[picture of X as input vector, W as arrow, O=WX as Model 2 vector on [cat pic]. W in b/w, with cols of both darker blue and darker red]--->

<!---[also put color coded outgoing weights for NN, write about this relating to matrix]--->

We can see how this matrix relates to weights in a neural network; each column corresponds to outgoing weights of a previous layer neuron, and each row corresponds to incoming weights of a next layer neuron:

<figure>
<img src="/ch1/NN_weights.png">

<figcaption align = "center"><b><font size="-1">Image Source:  https://www.jeremyjordan.me/intro-to-neural-networks/ </font></b></figcaption>
</figure>

As we see that each of the four neurons on the left act as basis vectors in the previous layer (Model 1), and the three neurons on the right act as basis vectors in the next layer (Model 2), such that the three neurons on the right are a linear combinations of the previous layer neurons and their weights, we come to a very important concept: 

<center><b>Neurons are Basis Vectors in an Activation Space.</b></center>
<br>

Thus, every neuron in a neural network is a measurement on the data. It is possible for a neuron to learn to measure cats, as in the examples shown above, and thus act as a "cat neuron". This Activation Space is commonly referred to as a **Latent Space**, and will be a very important concept for describing how a neural networks finds new relationships between data in a dataset. 

---

Going back to the change of basis example above, in Model 2, $$\color{#CBC3E3}{X = \begin{bmatrix} 0.5 \\ 2 \end{bmatrix}}$$ no longer labels <img src="/ch1/cat.PNG" width="50" height="40">; it's labeled by <span style="color:#9B59B6">the vector O</span>. How do we calculate what the new label for <img src="/ch1/cat.PNG" width="50" height="40"> is? In other words, how do we calculate the <span style="color:#9B59B6">values of the vector O = WX</span> by multiplying <span style="color:#CBC3E3">vector X</span> with <span style="color:purple">matrix W</span>? We will reveal the answer in Chapter 1.3.

With all this in mind, we can say that the goal of the neural network is to find how to accurately measure the data using neuron weights, so they can be taken together into an equation which measures a "goal measurement" such as "how body size and face length determine a cat or a rat".  

<!---
Fig 13
[fading gif of changing abstractions back to actual pics; place images on coord sys]--->

[^entity_model]: While the vectors are representations of the data sample, the data sample is also a representation of the actual cat entity (by transitivity, both are representation of the entity). Note that the vector is a numerial representation of the data sample, while the data sample is a collection of values which are defined relative to other samples in the population. Information about these collections of relative values is preserved under different Models, and different transformations preserve different information. Because values are defined relative to other values, information about data samples (such as their distribution) are relations, and relations can be thought of as shapes; for instance, a line is a relation between two points, so this line shape describes their relation. This is better explained in Appendix Chapter 1.1. Also note that the only information the neural network knows about the entity comes from the data sample; it can never truly know the entity.

<center><a href="ch1.2.html"><b>NEXT: CHAPTER 1.2</b></a></center>

<br><br>

---
---

<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript" async></script>