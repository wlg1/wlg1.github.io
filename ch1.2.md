---
theme: jekyll-theme-minimal
title: CHAPTER 1.2
---
<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>

**Ch1.2: Why use dot product in matrix multiplication?**
<!---WHY THE ALGEBRAIC PROCEDURE OF MATRIX MULTIPLICATION WORKS--->

Let's re-visit the problem of finding the value of $$O$$. In other words, how do we find the new label of <img src="/cob/cat.PNG" width="50" height="40"> in Model 2? 

![2mod_vecs](/cob/2mod_out.PNG)

In a linear algebra class, one learns that this can be done using matrix multiplication. But why does the algebraic procedure of matrix multiplication work? Why does the first step specifically use the dot product of the first row and the input vector? What even is a dot product?

Let's figure this out by first understanding what we need to know to calculate the values of $$O$$ that represents data sample <img src="/cob/cat.PNG" width="50" height="40">. All data samples in Model 2 are represented by two measurements: 
<p align="center">
1) How likely it is to be a <span style="color:orange">Cat</span>
</p>
<p align="center">
2) How likely it is to be a <span style="color:green">Rat</span>

$$O = \def\a{\color{orange}{Cat}}
\def\b{\color{green}{Rat}}
\begin{bmatrix} \a \\ \b \end{bmatrix}$$  
</p>
So if we want to find the value of $$O$$, we need to calculate these two values. Recall in the previous section that we were able to calculate the value of "how likely to be cat" using the values of "face length" and "body size":

[Shorter face + Bigger body = Likely a Cat

$$\color{red}{face_{cat}} * 0.5  + \color{blue}{body_{cat}} * 2$$ = 0.5(face_cat)+2(body_cat) on cat axes ]

Notice how this resembles the following dot product: 

<p align="center">
$$
\def\a{\color{red}{face_{cat}}}
\def\b{\color{blue}{body_{cat}}}
\begin{bmatrix} \a & \b \end{bmatrix}  
\cdot  \begin{bmatrix} 0.5 \\ 2 \end{bmatrix} 
= \color{red}{face_{cat}} * 0.5  + \color{blue}{body_{cat}} * 2$$
</p>

Not only that, but it resembles the first step of matrix multiplication:

<p align="center">
$$
\def\a{\color{red}{face_{cat}}}
\def\b{\color{blue}{body_{cat}}}
\begin{bmatrix} \a & \b \\ ? & ? \end{bmatrix}  
\begin{bmatrix} 0.5 \\ 2 \end{bmatrix} 
= \begin{bmatrix} \a * 0.5  + \b * 2 \\ ?\end{bmatrix} $$
</p>

In fact, the matrix on the left is none other than $$W$$ from the figure above, which is used in the equation $$O = WX$$.

$$
\def\a{\color{red}{1}}
\def\b{\color{blue}{1.5}}
\def\c{\color{red}{-1.5}}
\def\d{\color{blue}{1}}
\begin{bmatrix} \a & \b \\ \c & \d \end{bmatrix}  

=
\def\a{\color{red}{face_{cat}}}
\def\b{\color{blue}{body_{cat}}}
\begin{bmatrix} \a & \b \\ ? & ? \end{bmatrix}  
$$

We mentioned that $$face_{cat}$$ and $$body_{cat}$$ are weights that denote how important each feature is in the calculation. For example, if body size is more important, we'd set $$body_{cat} = 1.5 > face_{cat} = 1$$. Given the fact that the vertical axis of Model 2 denotes "likely to be rat", it's pretty clear now what the second row should be:

$$
\def\a{\color{red}{face_{cat}}}
\def\b{\color{blue}{body_{cat}}}
\def\c{\color{red}{face_{Rat}}}
\def\d{\color{blue}{body_{Rat}}}
\begin{bmatrix} \a & \b \\ \c & \d \end{bmatrix}  
$$

So we arrived at several conclusions: 

1) Because Model 2 uses the old measurements of Model 1 to calculate its new measurements, the matrix $$W$$ contains the weights needed to determine how important each old measurement is for each new measurement

2) Each row of the matrix contains weights to calculate one **new** measurement

3) Each column of the matrix contains weights for how one **OLD** measurement is used

3) The dot product is applied between every row of the matrix and the input vector because the same input vector uses different weights of the old measurements for every different new measurement

But what is the input vector

---

There is something else that's peculiar about $$\def\a{\color{red}{1}}
\def\b{\color{blue}{1.5}}
\begin{bmatrix} \a & \b \end{bmatrix}$$, the first row of W: 

The <span style="color:red">1</span> is the <span style="color:orange">Cat</span> coordinate of the vector $$\def\a{\color{red}{1}}
\def\c{\color{red}{-1.5}}
\begin{bmatrix} \a \\ \c \end{bmatrix}$$ in Model 2 from the figure above.

The <span style="color:blue">1.5</span> is the <span style="color:orange">Cat</span> coordinate of the vector $$\def\a{\color{blue}{1.5}}
\def\c{\color{blue}{1}}
\begin{bmatrix} \a \\ \c \end{bmatrix}$$.

In Model 2, $$\def\a{\color{red}{1}}
\def\c{\color{red}{-1.5}}
\begin{bmatrix} \a \\ \c \end{bmatrix}$$ labels <img src="/cob/face1.PNG" width="50" height="40">.

In Model 1, $$\def\a{\color{#FA8072}{1}}
\def\c{\color{#FA8072}{0}}
\begin{bmatrix} \a \\ \c \end{bmatrix}$$ labels <img src="/cob/face1.PNG" width="50" height="40">.

Thus, $$\def\a{\color{red}{1}}
\def\c{\color{red}{-1.5}}
\begin{bmatrix} \a \\ \c \end{bmatrix}$$ is where the data sample previously labeled by the basis vector $$\def\a{\color{#FA8072}{1}}
\def\c{\color{#FA8072}{0}}
\begin{bmatrix} \a \\ \c \end{bmatrix}$$ is sent.

Remember how the values of $$X$$ were calculated using the basis vectors. The first value, the face length of $$X$$, was calculated using:

<p align="center">
$$
\def\a{\color{#FA8072}{1}}
\def\b{\color{#ADD8E6}{0}}
\begin{bmatrix} \a & \b \end{bmatrix}  
\cdot  \begin{bmatrix} 0.5 \\ 2 \end{bmatrix} 
= \color{#FA8072}{1} * 0.5  + \color{#ADD8E6}{0} * 2 = \color{#CBC3E3}{0.5}$$
</p>

This is just like the dot product we saw to find the <span style="color:orange">Cat</span> value in Model 2.

<p align="center">
$$
\def\a{\color{red}{face_{cat}}}
\def\b{\color{blue}{body_{cat}}}
\begin{bmatrix} \a & \b \end{bmatrix}  
\cdot  \begin{bmatrix} 0.5 \\ 2 \end{bmatrix} 
= \color{red}{1} * 0.5  + \color{blue}{1.5} * 2$$
</p>

We were focused on calculating the values of $$O$$, but now we see that it's very similar to calculating the values of $$X$$! 

In this example, <img src="/cob/face1.PNG" width="50" height="40"> stays from <span style="color:#FA8072">1</span> to <span style="color:red">1</span>. If we look at the figure again, note that it doesn't move horizontally:

![2mod_vecs](/cob/2mod_out.PNG)

But if we look at another example where it moves from <span style="color:#FA8072">1</span> to <span style="color:red">4</span>, as we see in the figure below:

[fig]

What does this change **MEAN**? The answer is the following:

<p align="center">
<b><span style="color:#CBC3E3">A face length of unit 1</span> = <span style="color:#FA8072">1</span>*<span style="color:#CBC3E3">1</span> implies that there are <span style="color:red">4</span>*<span style="color:#CBC3E3">1</span> = <span style="color:orange">4 units 'likely to be cat'</span></b>
</p>

<p align="center">
<b>A face length of unit 1 implies that there are 4 units 'likely to be cat'</b>
</p>

In Model 1, when we multiply $$\color{#FA8072}{1} * \color{#CBC3E3
}{0.5}$$, it means "a face length of 0.5". Thus, in Model 2, $$\color{red}{4} * 0.5 = \color{orange}{2}$$ means:

<p align="center">
<b><span style="color:#CBC3E3">A face length of unit 0.5</span> = <span style="color:#FA8072">1</span>*<span style="color:#CBC3E3">0.5</span> implies that there are <span style="color:red">4</span>*<span style="color:#CBC3E3">0.5</span> = <span style="color:orange">2 units 'likely to be cat'</span></b>
</p>

<p align="center">
<b>A face length of unit 0.5 implies that there are 2 units 'likely to be cat'</b>
</p>

In other words, there is 1 unit of face length for 4 units of "cat", so there are only 0.5 units of face length for 2 units of "cat". We can use an analogy to understand this better: There is 1 meter for 3.28 feet. So if an entity is 2 meters long:

<p align="center">
There are 2 meters for 6.28 feet:
</p>
$$1 * 2 = 3.28 * 2$$

meter -> feet

face length -> 'likely cat'

"1 meter has 3.28 feet"

This is an example of 1D matrix multiplication; now, we are using 2 dimensions to calculate the location, since it's defined using 2 measurements.[^1]

[^1]: We are not trying to find the LABEL / vector, but the actual data sample. In analogy, we can describe ...
The entity is neither 2 nor 6.56; they are just measurements labeling it from two different perspectives. 
Remember, the dimensions are merely labels measuring the entity, but are not part of the entity itself. They are a way for an outside observer to describe the entity.

A 1D change of dimension is simple enough; "How many feet are in 1 meter?" A change of multiple dimensions follows the same logic. 




It's important to note that we are not always scaling <span style="color:#FA8072">1</span> by a factor of <span style="color:red">4</span>; if we tried to apply this to <span style="color:#FA8072">0</span>, we would never be able to change it. Instead, we are substituting 1 with 4; or in other words, "mapping" 1 to 4.

In summary: Every input <span style="color:#CBC3E3">(such as 0.5)</span> applied to the <span style="color:#FA8072">first measurement, face</span>, is also applied to the <span style="color:orange">second measurement, cat</span>, found by substituting <span style="color:#FA8072">1</span> with <span style="color:red">4</span>.

Of course, the value of "cat" here depends on two factors: face length, and body size. That's why in the dot product, we don't simply calculate the first term $$\color{#FA8072}{1} * \color{#CBC3E3
}{0.5}$$, but we must add the second term $$\color{#ADD8E6}{0} * \color{#CBC3E3
}{0.5}$$

$$\color{#FA8072}{1} * 0.5  + \color{#ADD8E6}{0} * 2 = \color{#CBC3E3}{0.5}$$

And do the same thing for Model 2, except we subsitute the values:

$$\color{red}{4} * 0.5  + \color{blue}{1.5} * 2$$

Thus, we finally described the meaning of the first term of the dot product used to calculate the value of "cat".

Let's merge the idea of ? being weights and the idea of ? being changes in measurements, as they are the same concept: 



[color code this to NN too]

<!---
$$\def\a{\color{#ADD8E6}{0}}
\def\c{\color{#ADD8E6}{1}}
\begin{bmatrix} \a \\ \c \end{bmatrix}$$ to $$\def\a{\color{blue}{1.5}}
\def\c{\color{blue}{1}}
\begin{bmatrix} \a \\ \c \end{bmatrix}$$

 Recall that the difference between Model 1 and Model 2 is the choice of basis vectors, and each vector in a coordinate space is defined using basis vectors. Thus, our translation will involve rewriting Model 1's basis vectors in terms of Model 2's basis vectors. Then the rewritten Model 1 basis vectors will be used to rewrite vector I in terms of Model 2's basis vectors. This is called a "Change of Basis", and can be done using matrix multiplication. --->

<!---
FOOTNOTE: WHY STRANGE PROCEDURE?

One question you may ask is: why does finding the answer to the first row of O require using the first row of W? 

The dot product adds two scaled vectors from the same dimension. To understand what the dot product is doing, all you need to know is why 1D vector addition works.

VECTOR ADDITION:
[First explain vector addition; everything follows from assuming it's true]
[show vectors as just values. elementary school addition / subtraction]

The reason we add vectors in 1D by placing the tail of B onto A, or vice versa, is because we can think of them simply as instructions: go left twice, then go right once.

...which is also shown in the 3Blue1Brown video [].

... thus, the reason why the first row of O (colored) uses the first row of W (colored diff) is because we project down the vectors c and d only by their first coordinate, which is the first row of W.
--->

---


[Discuss how prev right rotation is bad, and how new matrix is better]
-2, 2.5
2.5, 2

"A face length of unit 1 denotes that it's -2 units 'likely to be cat"

Or in other words, "A face length of unit 1 denotes that it's 2 units NOT 'likely to be cat"

If there are 2 meters, we multiply 2 meters.
[picture of 2 meters, or 2 * 3.28 feet]

If the face length is 0.5, that means it's 2 units not likely to be a cat.
[top is face length, bottom is -+ line denoting cat chance]

---
[First multiply by identity matrix, which leaves expression unchanged.]
The basis vectors in Model 1 form I, the identity matrix.

fig: show that Identity * X in Sys 1 is 'analogous' to W * X

Think of multiplying by the input vector X as instructions on how to get the coordinates for what data sample X points to.

[0.5,] in X finds the first coordinate; it means to multiply the face length  first coordinate by 0.5, and the body size first coordinate by 2. In Model 1, that means multiplying face=1 by 0.5, and bodysize=0 by 2.

But [0.5] does not act on the basis vector; it acts on the data sample [data sample face length 1 pic].
X does not act on the basis vector. It just so happens to be that in Model 1, [data sample face 1] is on the basis vector [1, 0], and [data sample body size 1] is on the basis vector [0, 1].

X = [instruction to face, instruction to body]

In Model 2, [data sample face 1] is NO LONGER labeled by the basis vector [1, 0], but is now on the vector [-2, 2.5]. Thus, the first instruction has to multiply [data sample face 1] by -2...

I = [[face_f, body_f] [[face_b, body_b]]]
X = [X_face, X_body]

The instructions that are applied to I are also applied to W.

---
page 2: steps

STEP 1: bodyFace, faceFace corresponds to first row of identity DoubleStrike1
        faceX, body X, corresponds to first row of W matrix

![step1](/cob/1.2/step1.png)

STEP 2: Scale

![step2](/cob/1.2/step2.png)

STEP 3: Add

![step3](/cob/1.2/step3.png)

<!---[Explain side-by-side of dot product on Sys 1 on left, and on Sys 2 on right. Show same instructions from I are done on Sys 2, but require W since now the basis vectors that I targeted look different]--->


Row 2 is the same; you can work it out yourself (but show animation / final result). Thus, the procedure to do 2D matrix multiplication is a sequence of 1D vector additions! (repeat the steps to calculate each member of the matrix)

This is why we use 2 dot products: each component is calculated separately...

We also see this is how dot product projects onto...

<<<
[inverse: going down 2 rat, 1 cat gets you to body size 1]
