---
title: Making the Math of Neural Networks Intuitive - HOME
---

<head>
    <link rel="stylesheet" href="index.css">
</head>

<div class="topnav">
  <a href="index.html">Home</a>
  <a href="about.html">About</a>
  <a class="active" href="eduBlogHome.html">Edu Blog Home</a>
  <a href="eduPlan.html">Edu Plan</a>
</div>

<p align="center"><h1><b>Making the Math of Neural Networks Intuitive</b></h1></p>

<span><b>W</b></span>hen studying new improvements to neural networks, many people run into the following problem:

<p align="center">
<b>How do these unfamiliar mathematical concepts relate to neural networks?</b></p>

This blog overcomes this problem by explaining many required prerequisites from scratch[^1], and relating them to neural network applications. It focuses on providing intuition via visuals and animation, much like in resources such as <a href="https://www.3blue1brown.com/lessons/">3Blue1Brown</a>.

[^1]: Assuming only that a reader has a basic understanding of a foundational topic, or has watched certain videos. Links will be provided to these videos.

![2mod_vecs](/ch1/2mod_out.PNG)

<!---
It also gets to the point: it only says what issues this concept solves for this neural network paper, nothing more. It would not delve in related mathematical concepts if they were not useful for understanding the application we're currently discussing. 

But this blog takes an even further step: by generalizing this solution to solve similar problems.

fig Eg) [give an example of issue- reasoning- soln - generalization, that concisely explains all after prereqs]
--->

Not sure where to start? Start with the video below:

<b>Why do Neural Networks use Linear Algebra? -- The Visual Intuition of Cat Mathematics</b>

<iframe width="560" height="315" src="https://www.youtube.com/embed/DHjwbleAgPQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

<u>NOTE:</u> Ch 1 (along with many other chapters) is outdated and will be updated later. It is recommended to watch this video instead, which encapsulates the same concepts as Ch 1 but in a better way.

<!---
Not sure where to start?

**[Start Here](ch1.1.md)**
--->

---
**CHAPTER 1: How Neural Networks Reveal Hidden Insights in Data (using Matrix Multiplication)**

&nbsp;&nbsp;&nbsp;&nbsp;**[1.1: How does Matrix Multiplication Guess it's a Cat from its Face and Body?](ch1.1.md)**

&nbsp;&nbsp;&nbsp;&nbsp;**[1.2: Beware of False Friends in the Matrix?](ch1.2.md)**

&nbsp;&nbsp;&nbsp;&nbsp;**[1.3: Why is the Dot Product used in Matrix Multiplication?](ch1.3.md)**

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

&nbsp;&nbsp;&nbsp;&nbsp;**[2.3: Scoring Semantics using Hyperplanes]()**

<details>
<summary><b>CHAPTER 2 CODE TUTORIALS</b> (click to expand) </summary>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;<a class="active" href="https://colab.research.google.com/drive/1KNs_QgosAn3GmkUpaQAyRDo1pEjputNJ?usp=share_link">CODE 2.1: InterFaceGAN </a>
<br><br>
</details>
<br>

### Work in Progress:

**CHAPTER 3: How Neural Networks Find the Most Important Features in Data (using Eigenvectors)**

&nbsp;&nbsp;&nbsp;&nbsp;**[3.1: Paper Explanation: GANspace]()**

&nbsp;&nbsp;&nbsp;&nbsp;**[3.2: Covariance Matrix]()**

&nbsp;&nbsp;&nbsp;&nbsp;**[3.3: Paper Explanation: Eigenfaces]()**

&nbsp;&nbsp;&nbsp;&nbsp;**[3.4: Paper Explanation: SeFA]()**

&nbsp;&nbsp;&nbsp;&nbsp;**[3.5: SVD]()**


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

**[Review: VAEs ](generative_models_review.md)**

---
---