---
theme: jekyll-theme-minimal
title: CHAPTER 1.1
---

**Ch1.2: Why use dot product in matrix multiplication?**
<!---WHY THE ALGEBRAIC PROCEDURE OF MATRIX MULTIPLICATION WORKS--->

How do we translate vectors in Model 1 to vectors in Model 2?

![2mod_vecs](/cob/2mod_vecs.PNG)

In other words, how do we find the new label of [cat pic] in Model 2? Recall that the difference between Model 1 and Model 2 is the choice of basis vectors, and each vector in a coordinate space is defined using basis vectors. Thus, our translation will involve rewriting Model 1's basis vectors in terms of Model 2's basis vectors. Then the rewritten Model 1 basis vectors will be used to rewrite vector I in terms of Model 2's basis vectors. This is called a "Change of Basis", and can be done using matrix multiplication. 

[pic showing how to decompose basis in Model 1 in terms of Model 2, as an eq, with arrows to each Model. Then show how these basis vectors use to rewrite I in terms of 2's basis vectors]

---
FIRST STEP OF MM

So let's describe what's happening during the first step of matrix multiplication. Since our coordinate spaces use 2 basis vectors, let's look at 2D matrix multiplication.
[label statements with colored labels on pic of matrix]
[put colored statements in an ordered list. For now, only highlight first dot product]

The first procedure in matrix multiplication is a dot product. But what is a dot product, and why is it used here?

Recall in the previous section that we were able to calculate the values of  "how likely to be cat" using the values of "face length" and "body size":

[figure showing the analogy: 
Shorter face + Bigger body = Likely a Cat
0.5 * [face_X] + 2 * [body_X] = value 2X+0.5Y on cat axes ]

[face_X and body_X are the first row of W matrix; color this]

Notice how this resembles the following dot product: [] [] = ...
So the value of the first coordinate in System 2 is produced using the dot product of the 2 basis vectors in System 1. We will now reveal what X and Y are, just as we promised before. Specifically, X and Y will be how we rewrite the basis vectors from Model 1...

[breakdown what each term in the dot product eq above is, matching them to their geometric vector in Sys 1 and Sys 2. inputs comes from Sys 1, weights from Sys 2]
[highlight the first coord of each basis vector in System 2]

[Discuss how prev right rotation is bad, and how new matrix is better]
-2, 2.5
2.5, 2

<!---
FOOTNOTE: WHY STRANGE PROCEDURE?

One question you may ask is: why does finding the answer to the first row of O require using the first row of W? 

The dot product adds two scaled vectors from the same dimension. To understand what the dot product is doing, all you need to know is why 1D vector addition works.

VECTOR ADDITION:
[First explain vector addition; everything follows from assuming it's true]
[show vectors as just values. elementary school addition / subtraction]

The reason we add vectors in 1D by placing the tail of B onto A, or vice versa, is because we can think of them simply as instructions: go left twice, then go right once.

...which is also shown in the 3Blue1Brown video [].

Explain more, with pics

... thus, the reason why the first row of O (colored) uses the first row of W (colored diff) is because we project down the vectors c and d only by their first coordinate, which is the first row of W.
--->

---
page 2: steps

[First multiply by identity matrix, which leaves expression unchanged.]
The basis vectors in Model 1 form I, the identity matrix.

fig: show that Identity * X in Sys 1 is 'analogous' to W * X

Think of multiplying by the input vector X as instructions on how to get the coordinates for what data sample X points to.

[0.5,] in X finds the first coordinate; it means to multiply the face length  first coordiante by 0.5, and the body size first coordinate by 2. In Model 1, that means multiplying face=1 by 0.5, and bodysize=0 by 2.

But [0.5] does not act on the basis vector; it acts on the data sample [data sample face length 1 pic].
X does not act on the basis vector. It just so happens to be that in Model 1, [data sample face 1] is on the basis vector [1, 0], and [data sample body size 1] is on the basis vector [0, 1].

X = [instruction to face, instruction to body]

In Model 2, [data sample face 1] is NO LONGER labeled by the basis vector [1, 0], but is now on the vector [-2, 2.5]. Thus, the first instruction has to multiply [data sample face 1] by -2...

I = [[face_f, body_f] [[face_b, body_b]]]
X = [X_face, X_body]

The instructions that are applied to I are also applied to W.

We are not trying to find the LABEL /vector, but the actual data sample. In analogy, we can describe ...
There are 3.28 feet in 1 meter. So if an entity is 2 meters long (input):
2 meters vs 6.56 feet
1 * 2 = 3.28 * 2

The entity is neither 2 nor 6.56; they are just measurements labeling it from two different perspectives. This is an example of 1D matrix multiplication; now, we are using 2 dimensions to calculate the location, since it's defined using 2 measurements.
A 1D change of dimension is simple enough; "How many feet are in 1 meter?" A change of multiple dimensions follows the same logic. Remember, the dimensions are merely labels measuring the entity, but are not part of the entity itself. They are a way for an outside observer to describe the entity.

---

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

<<<
[inverse: going down 2 rat, 1 cat gets you to body size 1]