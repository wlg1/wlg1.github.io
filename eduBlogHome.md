---
title: Making the Math of Neural Networks Intuitive - HOME
---

<head>
    <link rel="stylesheet" href="index.css">
</head>

<div class="topnav">
  <a class="active" href="eduBlogHome.html">Home</a>
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

[^1]: Assuming only that a reader has a basic understanding of X, or has watched these videos []. Links are provided to them.

But this blog takes an even further step: by generalizing this solution to solve similar problems.

<!---
fig Eg) [give an example of issue- reasoning- soln - generalization, that concisely explains all after prereqs]
--->

Not sure where to start?

**[Start Here](ch1.1.md)**

---
**CHAPTER 1: How Neural Networks Reveal Hidden Insights in Data (using Matrix Multiplication)**

&nbsp;&nbsp;&nbsp;&nbsp;**[1.1: How does Matrix Multiplication Guess it's a Cat from its Face and Body?](ch1.1.md)**

&nbsp;&nbsp;&nbsp;&nbsp;**[1.2: Beware of False Friends when Changing Basis?](ch1.2.md)**

&nbsp;&nbsp;&nbsp;&nbsp;**[1.3: Why is Dot Product used in Matrix Multiplication?](ch1.3.md)**

<details>
<summary><b>CHAPTER 1 APPENDIX: DUALITY</b> (click to expand) </summary>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;A1.1: WHY use Basis vectors? The Relativity of Data
<br><br>
&nbsp;&nbsp;&nbsp;&nbsp;A1.2: The Duality of Neurons: As Objects, As Relations
<br><br>
&nbsp;&nbsp;&nbsp;&nbsp;A1.3: The Analogy of the Matrix
<br><br>
</details>
<br>

**CHAPTER 2: How Neural Networks Make Faces Look Younger (using Vector Projection)**

&nbsp;&nbsp;&nbsp;&nbsp;2.0: Face Filters, Anime Filters, and Fake People

&nbsp;&nbsp;&nbsp;&nbsp;**[2.1: Changing Features using Vector Addition](ch2.1.md)**

&nbsp;&nbsp;&nbsp;&nbsp;**[2.2: Conditioning on Features using Orthogonal Projection](ch2.2.md)**

&nbsp;&nbsp;&nbsp;&nbsp;**[2.3: Scoring Semantics using Hyperplanes](ch2.1_old.md)**

**CHAPTER 3: How Neural Networks Find the Most Important Features in Data (using Eigenvectors)**

&nbsp;&nbsp;&nbsp;&nbsp;**[3.1: Paper Explanation: GANspace](ch3.1.md)**

&nbsp;&nbsp;&nbsp;&nbsp;**[3.2: Covariance Matrix](ch3.2.md)**

&nbsp;&nbsp;&nbsp;&nbsp;**[3.3: Paper Explanation: Eigenfaces](ch3.3.md)**

&nbsp;&nbsp;&nbsp;&nbsp;**[3.4: Paper Explanation: SeFA]()**

&nbsp;&nbsp;&nbsp;&nbsp;**[3.5: SVD](ch3.5.md)**

<!--- **CHAPTER 2: How to Find the Important Features and Change Them (using Matrix Decomposition)?** --->

Future topics: 
<ul>
  <li>Matrix Decomposition to find neuron combinations</li>
  <li>Fourier transforms and convolution</li>
  <li>Graph neural networks and geometric deep learning equivariance</li>
  <li>Transformers</li>
  <li>Diffusion models</li>
  <li>CLIP and prompt generation</li>
  <li>The Shape of Data and Topological Data Analysis applied to latent space</li>
</ul>

---

**Appendices:**

**[Review: Generative Models ](generative_models_review.md)**

---
---