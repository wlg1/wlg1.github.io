---
title: Front Page
---

<head>
    <link rel="stylesheet" href="index.css">
</head>

<div class="topnav">
  <a class="active" href="#Home">Home</a>
  <!---
  <a href="expm_index.html">Experiments Index</a>
  <a href="#Techniques">Techniques Compendium</a>
  <a href="#Contact">Contact</a>
  --->
</div>

<p align="center"><h1><b>Michael Lan</b></h1></p>
<!---
<a href="test_post.html">test</a>
--->

<span><b>H</b></span>ello. My projects can be found below. Click on the title link to learn more:

[ Ctrl++ or Mouse Wheel to zoom in for bigger text. ]

[ Website in process of being built. Some projects in progress are not added yet and will be added later. ]

---

<p style="font-size:20px"><b>
<a href="https://wlg1.notion.site/Experimental-Records-33ca6dad981343abb00a974a6c4e3607">Transformer Comparison Circuit Experiments</a>
</b></p>

Based on previous work that used techniques such as activation patching and dot product congruence [ Interpretability in the Wild, "An" Neuron, etc to be cited ], these experiments look, in large language models, for circuits which compare information, such as sizes. For the GPT-family of models, this work is currently investigating:
<ul>
<li> Adjective Identification Circuits </li>
<li> Most Recent Subject Circuits </li>
<li> Not Identification Circuits </li>
<li> Antonym Identification Circuits (related to Adjective ID Circuits) </li>
</ul>

Records of experiments and notes are found in the link below:

<a href="https://wlg1.notion.site/Experimental-Records-33ca6dad981343abb00a974a6c4e3607">Experiments Index</a>

Videos introducing the work so far are also provided. The video below is a short introductory overview, while the link that follows  provides a series of videos going over the details of the work:

[ introductory 3m overview video embeds here ]

<a href="https://wlg1.notion.site/Videos-Interpret-Attention-Head-Circuits-of-Comparison-Inputs-DRAFTS-24b67e08b1d74f70be8ed3012e8278bc">Videos- Interpret Attention Head Circuits of Comparison Inputs (DRAFTS)</a>

---

These pages are supplemental to the experiments:

<a href="https://wlg1.notion.site/Notes-0c9ac6d4ec58411bb2d462ed854840c9">Notes</a>

<a href="https://wlg1.notion.site/Techniques-Compendium-ea12d22f5a8940b190b553d17200ba08">Techniques Compendium</a>

<a href="https://wlg1.notion.site/Ideas-b7fe100b6ddf4b3c84d702dc4b918ce6">Ideas</a>

---
<p style="font-size:20px"><b>
<a href="https://www.youtube.com/@neoknowstic">Educational Videos on Neural Network Mathematics</a>
</b></p>

<b>Why do Neural Networks use Linear Algebra? -- The Visual Intuition of Cat Mathematics</b>

<iframe width="560" height="315" src="https://www.youtube.com/embed/DHjwbleAgPQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

This is the first video in a series aimed at a general audience explaining the math behind neural network interpretability. The first video introduces the geometry of latent space for a simple MLP, explaining concepts such as the relations of neurons and feature vectors, basis vectors, dot product, and hypotheses about latent space arithmetic. To be accessible to layman, it starts with simple multiplication and change of units, gradually extending this to matrix multiplication.

<u>Note on the youtube recommendation algorithm:</u>
This video was climbing up in views each day until its reupload due to audio issues; afterwards, it gained very little views. It may have gotten penalized due to being nearly identical to the previous upload, as there are claims that youtube penalizes duplicate videos. Claims state the algorithm recommends videos based on current news/trends, which do not have to be large but just "large enough" (windy, not even a hurricane). Small trends meant similar videos are swept up in the conglomorate and recommended. The #SoME3 competition at the end of August 2023 is usually when educational videos trend; once the third video (about Diffusion Model Editing) on this channel is uploaded for that competition, it is expected that the other videos will also be recommended alongside it.

---
<b>THE AI AMONG US in Your Non-Euclidean Mind 〘 Analog VHS Infomerical 〙</b>

<iframe width="560" height="315" src="https://www.youtube.com/embed/xI7tAjoe4oc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

This second video demonstrates Diffusion Model Editing using techniques from Differential Geometry and images from Stable Diffusion. It is aimed at a non-academic audience, combining themes from popular youtube "Analog Horror" videos. It is part of a series of videos intended to introduce generative model editing to a younger, high school aged audience. The following video provides a background explanation of the content in the video:

<a href="https://www.youtube.com/watch?v=MMLKwomDKDI&ab_channel=TREYtheExplainer">An expalnation of the among us pareidolia effect</a>

---
This is an outdated site (to be updated later) explaining concepts similar to ones in the videos above in a blog format:

<a href="eduBlogHome.html">Making the Math of Neural Networks Intuitive</a>

<!---
[image of face and face w/o mouth, showing toy circuits of each and what differs]
--->

<!---
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

--->

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
<b>UNDER CONSTRUCTION:</b>

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

---




