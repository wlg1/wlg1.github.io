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

Recall in the previous section that we were able to calculate the values of j = "how likely to be cat" (color this acc to coordinate) using the values of c = "body size" and d = "face length":

[figure showing the analogy: 
Bigger body + Shorter face = Cat
2 * [body pic X] + 0.5 * [face pic Y] = Z on cat axes ]

Notice how this resembles the following dot product: [] [] = ...
So the value of the first coordinate in System 2 (color this) is produced using the dot product of the 2 basis vectors in System 1. We will now reveal what X and Y are, just as we promised before. Specifically, X and Y will be how we rewrite the basis vectors from Model 1...

[breakdown what each term in the dot product eq above is, matching them to their geometric vector in Sys 1 and Sys 2. inputs comes from Sys 1, weights from Sys 2]
[highlight the first coord of each basis vector in System 2]

<!---
FOOTNOTE: WHY STRANGE PROCEDURE?

One question you may ask is: why does finding the answer to the first row of O require using the first row of W? 

The dot product adds two scaled vectors from the same dimension. To understand what the dot product is doing, all you need to know is why 1D vector addition works.

[show vectors as just values. elementary school addition / subtraction]

The reason we add vectors in 1D by placing the tail of B onto A, or vice versa, is because we can think of them simply as instructions: go left twice, then go right once.

...which is also shown in the 3Blue1Brown video [].

Explain more, with pics

... thus, the reason why the first row of O (colored) uses the first row of W (colored diff) is because we project down the vectors c and d only by their first coordinate, which is the first row of W.
--->


---
page 2: steps

STEP 1

![step1](/cob/1.2/step1.PNG)

STEP 2

![step2](/cob/1.2/step2.PNG)

STEP 3

![step3](/cob/1.2/step3.PNG)

[Explain side-by-side of dot product on Sys 1 on left, and on Sys 2 on right. Show same instructions from I are done on Sys 2, but require W since now the basis vectors that I targeted look different.
I red, W and O blue; both in eqns and coordsys ]

This shows why you have to apply W to I; you can't just use I's instructions on the basis vectors. This is b/c the basis vectors are no longer in the same language. You have to apply I's instructions to what I looks like now, which are [] in System 2. Then say Sys 1 can also be thought of as using "identity matrix" as change in basis.

fig: show that Identity * [-1 2] in Sys 1 is 'analogous' to 'W matrix' * [-1 2]

Row 2 is the same; you can work it out yourself (but show animation / final result). Thus, the procedure to do 2D matrix multiplication is a sequence of 1D vector additions!

This is why we use 2 dot products: each component is calculated separately...

<<<
[inverse: going down 2 rat, 1 cat gets you to body size 1]
