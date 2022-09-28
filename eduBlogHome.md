---
title: Making the Math of Neural Networks Intuitive - HOME
---

<head>
    <link rel="stylesheet" href="index.css">
</head>

<div class="topnav">
  <a class="active" href="#home">Home</a>
  <a href="#contact">Contact</a>
  <a href="#about">About</a>
</div>

<p align="center"><h1><b>Making the Math of Neural Networks Intuitive</b></h1></p>

<!---
For localhost testing:

<a href="ch1.1.html">CHAPTER 1.1</a>

<a href="ch1.2.html">CHAPTER 1.2</a>

<a href="ch2.0.html">CHAPTER 2.0</a>

<a href="ch2.1.html">CHAPTER 2.1</a>

---

--->

<span><b>W</b></span>hen studying new improvements to neural networks, many people run into the following problem:

<p align="center">
<b>How do these unfamiliar mathematical concepts relate to neural networks?</b></p>

<!---
fig Eg) What's orthogonal projection?
--->

This blog solves these problems by explaining all the required prerequisites needed to understand the terminology from the bottom up.[^1]. It also gets to the point: it only says what issues this concept solves for this neural network paper, nothing more. 

[^1]: assuming only that a reader has a basic understanding of X, or has watched these videos []. Links are provided to them.

But this blog takes an even further step: by generalizing this solution to solve similar problems.

<!---
fig Eg) [give an example of issue- reasoning- soln - generalization, that concisely explains all after prereqs]
--->

Not sure where to start?

**[Start Here](ch1.1.md)**

---
**CHAPTER 1: How Neural Networks Reveal Hidden Insights in Data (using Matrix Multiplication)**

**[1.1: How does matrix multiplication guess a cat from its face and body?](ch1.1.md)**

**[1.2: Why use dot product in matrix multiplication?](ch1.2.md)**

1.3: WHY use basis vectors? The relativity of data

1.4: The Duality of Neurons: As Objects, As Relations

1.5: The Analogy of the Matrix


**CHAPTER 2: How to Find the Important Features and Change Them (using Matrix Decomposition)?**

2.0: Cool Applications (Face filters, etc.)

**[2.1: How Do Neural Networks Make Faces Look Younger (using Orthogonal Projection)?](ch2.1.md)**

**[2.2: How Neural Networks Find the Most Important Features in Data (using Eigenvectors)](ch2.2.md)**

&nbsp;&nbsp;&nbsp;&nbsp;**[2.2.1: Paper Explanation: GANspace](ch2.2.1.md)**

&nbsp;&nbsp;&nbsp;&nbsp;**[2.2.2: Covariance Matrix](ch2.2.2.md)**

&nbsp;&nbsp;&nbsp;&nbsp;**[2.2.3: Paper Explanation: Eigenfaces](ch2.2.3.md)**

&nbsp;&nbsp;&nbsp;&nbsp;**[2.2.4: Paper Explanation: SeFA]()**

&nbsp;&nbsp;&nbsp;&nbsp;**[2.2.5: SVD](ch2.2.5.md)**

[applying to latest generative models: DALLE, stable diffusion, grokking]

---

Appendices:

**[Review: Generative Models ](generative_models_review.md)**
