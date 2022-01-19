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

We mentioned that $$face_{cat}$$ and $$body_{cat}$$ are weights that denote how important each feature is in the calculation. For example, if body size is more important, we'd set $$body_{cat} = 1.5 > face_{cat} = 1$$. 

But what does this dot product **mean** in terms of our dataset? To make its meaning easier to understand, let $$face_{cat}=4$$, and let's ignore the second term by setting $$body_{cat} = ?$$

$$\color{red}{W}\color{#CBC3E3}{X} = \color{orange}{O}$$

<p align="center">
$$
\def\a{\color{red}{(face_{cat}=4)}}
\def\b{\color{#CBC3E3}{0.5}}
\def\c{\color{red}{4}}
\def\d{\color{orange}{2}}
\begin{bmatrix} \a & ? \\ ? & ? \end{bmatrix}  
\begin{bmatrix} \b \\ ? \end{bmatrix} 
= \begin{bmatrix} \c * \b = \d  \\ ?\end{bmatrix} $$
</p>

<p align="center">
<b><span style="color:#CBC3E3">0.5 units of face length</span></b> <span style="font-size:20px">&#8594;</span> <span style="color:orange">2 units of 'likely to be cat'</span>
</p>

In other words, "for every face length of unit 1, there are 4 units of cat". Thus, for half a unit of face length, we have half of the proportionate amount of cat, which is 2. Doesn't this sound familiar, like unit conversion?

[picture of meter to feet conversion]

For every 1 meter, there are 3.28 feet. So if an entity is 2 meters long:

<p align="center">
$$
\def\a{\color{red}{(meter_{feet}=3.28)}}
\def\b{\color{#CBC3E3}{2}}
\def\c{\color{red}{3.28}}
\def\d{\color{orange}{6.56}}
\begin{bmatrix} \a \end{bmatrix}  
\begin{bmatrix} \b \end{bmatrix} 
= \begin{bmatrix} \c * \b = \d \end{bmatrix} $$
</p>

<p align="center">
<b><span style="color:#CBC3E3">2 units of meter</span></b> <span style="font-size:20px">&#8594;</span> <span style="color:orange">6.56 units of feet</span>
</p>

Indeed, one dot product step is analogous to 1D matrix multiplication; so two dot product steps would be analogous to 2D matrix multiplication. At last, we realize that matrix multiplication, or "Change of Basis", is none other than  unit conversion multiplication, or "Change of Units". That is, $$O$$ refers to the same quantity that $$X$$ refers to, except the two measure it using different units.[^1]

[^1]: The entity is neither 2 (meters) nor 6.56 (feet); those are just measurements labeling the data sample from two different perspectives. Remember, the dimensions are merely labels measuring the entity, but are not part of the entity itself. They are a way for an outside observer to describe the entity. So the vectors $$X$$ and $$O$$ are just different ways to measure the same data sample, but they are not the data sample itself.

But in contrast to the 1D "meter to feet" example, the "face and body to cat" example uses **two** measurements to find the value of cat. Matrix multiplication allows for a change of **multiple** units, or multiple dimensions. The weight matrix $$W$$ is analogous to the conversion factor.

In summary:

1) A **Dot Product** is used to convert multiple units into a new unit

2) Multiple dot products are used in **Matrix Multiplication** to find multiple new units

Just like how each row of $$X$$ measures the same entity but using a different unit (a basis vector of Model 1), each row of $$O$$ uses a different unit (a basis vector of Model 2) to measure the same entity, and each is calculated using the known measurements from $$X$$.

Since each new measurement is calculating using the **same input**, but with <span><i>different conversion factors</i></span>, each new value of $$O$$ is calculating using the **same input vector** $$X$$, but with <span><i>different rows of</i></span> $$W$$.

---

We now explained what the rows of $$W$$ are. But what are its columns? And how does this tie into the geometric representation of matrix multiplication, as we see in the figure above? Let's match terms in these equations to their geometric representation:

In Model 1, $$\def\a{\color{#FA8072}{1}}
\def\c{\color{#FA8072}{0}}
\begin{bmatrix} \a \\ \c \end{bmatrix}$$ labels <img src="/cob/face1.PNG" width="50" height="40">. In Model 2, $$\def\a{\color{red}{1}}
\def\c{\color{red}{-1.5}}
\begin{bmatrix} \a \\ \c \end{bmatrix}$$ labels <img src="/cob/face1.PNG" width="50" height="40">.

Thus, $$\def\a{\color{red}{1}}
\def\c{\color{red}{-1.5}}
\begin{bmatrix} \a \\ \c \end{bmatrix}$$ is where the data sample previously labeled by the basis vector $$\def\a{\color{#FA8072}{1}}
\def\c{\color{#FA8072}{0}}
\begin{bmatrix} \a \\ \c \end{bmatrix}$$ is sent.

Notice that $$\def\a{\color{red}{1}}
\def\c{\color{red}{-1.5}}
\begin{bmatrix} \a \\ \c \end{bmatrix}$$ is the first column of $$W$$. And $$\color{red}{face_{cat}}$$ = <span style="color:red">1</span> is the <span style="color:orange">Cat</span> coordinate of the vector $$\def\a{\color{red}{face_{cat}=1}}
\def\c{\color{red}{-1.5}}
\begin{bmatrix} \a \\ \c \end{bmatrix}$$ in Model 2. Given the fact that the vertical axis of Model 2 denotes "likely to be rat", it's pretty clear that the second row of this vector is $$face_{Rat}$$, which is how much the face length is weighed by to calculate the value of the <span style="color:green">Rat</span> coordinate.

Therefore, $$\def\a{\color{red}{face_{cat}=1}}
\def\c{\color{red}{face_{Rat}=-1.5}}
\begin{bmatrix} \a \\ \c \end{bmatrix}$$, the first column of $$W$$, and the Model 2 vector labeling <img src="/cob/face1.PNG" width="50" height="40">, contains the conversion factors for each of the basis vectors $$\{ \color{orange}{cat}, \color{green}{Rat} \}$$ of Model 2, in terms of only $$\color{red}{face}$$.[^no_longer_basis] 

[^no_longer_basis]: Remember that <span style="color:red">[1, 1.5]</span> is NOT a basis vector, so <img src="/cob/face1.PNG" width="50" height="40"> is no longer labeled by a basis vector. 

Likewise, $$\def\a{\color{blue}{body_{cat}=1.5}}
\def\c{\color{blue}{body_{Rat}=-1}}
\begin{bmatrix} \a \\ \c \end{bmatrix}$$, the second column of $$W$$, and the Model 2 vector labeling <img src="/cob/body1.PNG" width="50" height="40">, contains the conversion factors for each of the basis vectors $$\{ \color{orange}{cat}, \color{green}{Rat} \}$$ of Model 2, in terms of only $$\color{blue}{body}$$. 

$$
\def\a{\color{red}{face_{cat}}}
\def\b{\color{blue}{body_{cat}}}
\def\c{\color{red}{face_{Rat}}}
\def\d{\color{blue}{body_{Rat}}}
\color{purple}{W} = \begin{bmatrix} \a & \b \\ \c & \d \end{bmatrix}  
$$

So we arrived at several conclusions: 

1) Because Model 2 uses the old measurements of Model 1 to calculate its new measurements, the matrix $$W$$ contains the weights needed to determine how important each old measurement is for each new measurement

2) Each row of the matrix contains weights to calculate one **new** measurement in $$O$$

3) Each column of the matrix contains weights for how one **OLD** measurement in $$X$$ is used

4) The dot product is applied between every row of the matrix and the input vector because the same input vector uses different weights of the old measurements in $$X$$ for every new measurement in $$O$$

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
[^]: The dot product between two vectors scales the numbers in the first vector, then adds them all together. The second vector contains the weights used to scale the first vector's elements. Since the dot product is commutative, it is interchangable which vector is the "first" or "second".

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

---
[inverse: going down 2 rat, 1 cat gets you to body size 1]

---
