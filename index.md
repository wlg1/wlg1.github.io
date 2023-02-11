---
title: Front Page
---

<head>
    <link rel="stylesheet" href="index.css">
</head>

<div class="topnav">
  <a class="active" href="#Home">Home</a>
  <a href="expm_index.html">Experiments Index</a>
  <a href="#Techniques">Techniques Compendium</a>
  <a href="#Contact">Contact</a>
</div>

<p align="center"><h1><b>Michael Lan</b></h1></p>
<!---
<a href="test_post.html">test</a>
--->

<span><b>H</b></span>ello. My projects can be found below. Click on the title link to learn more:

[ Website in process of being built. To be completed by: April 2023 ][^footnote]

[^footnote]: Future uploads include tutorials that walk through experiments, starting with simple ones. Most of the experiments done so far are still in draft form, rather than in tutorial format.

---
<p style="font-size:20px"><b>
<a href="https://www.youtube.com/@neoknowstic">Educational Videos on Neural Network Math</a>
</b></p>

Why do Neural Networks use Linear Algebra? || Pt 1: The Visual Intuition of Cat Mathematics

<iframe width="560" height="315" src="https://www.youtube.com/embed/uXvj6V2fwfY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

This is a video series aimed at a general audience explaining the math behind neural network interpretability. The first video starts at very basic concepts. This one is currently a draft of half the video, with work-in-progress audio and placeholder animation; the actual video will be uploaded by 2/15.

Here is an updated version of the video with new animation but no narration after the first scene:

<iframe width="560" height="315" src="https://www.youtube.com/embed/UC2Lxf4Wvzc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

---
<p style="font-size:20px"><b>
<a href="https://github.com/wlg1/analogous_neuron_circuit_expms">Analogous Neural Circuit Experiments</a>
</b></p>

Analogous Neural Circuit Experiments aim to find common patterns in neural network activations based on inputs with varying similarities. Why study Analogous Neural Circuit Experiments? These studies enhance Neural Network Interpretability by connecting model predictions to patterns the model uses to make its predictions. This has significant applications, which include:
<ul>
<li><b>Improving Trust in AI:</b> When AI makes important decisions, such as in medical treatment or financial investments, knowing why the AI made those predictions is crucial to ensuring that it is not using faulty reasoning to make its predictions. </li>
<li><b>Improving Model Debugging:</b> By uncovering the black box that obscures how neural networks make decisions, practitioners will have more control over debugging neural networks to do what they want. </li>
<li><b>Improving Transfer Learning:</b> By understanding which parts of a neural network perform what function, practitioners will be able to dissect neural networks to retrieve the part they need, and apply transfer learning to fine tune that part to suit their own, specific goals.</li>
</ul>

These experiments are housed in a Github repo with Colab notebooks that walk a reader through how the experiments were conducted. An example of a notebook demonstrating simple experiments is given below:

<a href="https://colab.research.google.com/drive/12hQolN9TLXsakkG96nYUgU30_6YL74bf">TUTORIAL 1: Compare Neuron Activations Between Pairs of Images</a>

<!---
[image of face and face w/o mouth, showing toy circuits of each and what differs]
--->
---
<p style="font-size:20px"><b>
<a href="eduBlogHome.html">Making the Math of Neural Networks Intuitive</a>
</b></p>

Techniques such as eigendecomposition, orthogonal projection, and more are often applied to neural networks to further new improvements. Knowing why they work requires understanding not just linear algebra, but the intuition of <b>why</b> linear algebra is used. Why use an eigenvector to change the style of a generated image?

Thus, when studying new improvements to neural networks, many people run into the following problem:

<p align="center">
<b>How do these unfamiliar mathematical concepts relate to neural networks?</b></p>

This blog overcomes this problem by explaining many required prerequisites from scratch, and relating them to neural network applications. It focuses on providing intuition via visuals and animation, much like in resources such as <a href="https://www.3blue1brown.com/lessons/">3Blue1Brown</a>.

![2mod_vecs](/ch1/2mod_out.PNG)

---
<p style="font-size:20px"><b>
<a href="">Latent Space Experiments</a>
</b></p>

Another way to study how neural networks make decisions is to study the geometry of their latent space. This leads to powerful methods such as Style Editing, in which one can turn the face of a generated person from old to young.

---
<p style="font-size:20px"><b>
<a href="https://mikelan300.wixsite.com/portfolio">Data Science Projects</a>
</b></p>

Regression Analysis on Video Game Sales using Unstructured Data from Reddit 
<ul>
<li>Employed web APIs to scrap Reddit posts and semi-structured Wikipedia infoboxes. Cleaned and
explored data, then ﬁt models applicable for business decisions in marketing and ﬁnance. </li>
</ul>
Facebook and YouTube Social Network Friend Prediction via SVMs 
<ul>
<li>Trained Support Vector Machines that achieved high accuracy and AUC scores on testing data.
Utilized graph analytics to compare the network statistics of diﬀerent communities.</li>
</ul>

<div id="datasci_images">
  <div class="inline-block">
  <img src="/datasci/final_model.PNG" width="350" height="300" alt="">
  <img src="/datasci/datasci_networks.png" width="350" height="300" alt="">
  </div>
</div>

<!---
![final_model](/datasci/final_model.PNG)
![datasci_networks](/datasci/datasci_networks.png)
--->

---




