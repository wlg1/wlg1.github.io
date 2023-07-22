---
title: Front Page
---
<!---
<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript" async></script>
--->

<head>
    <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
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
Ctrl++ or Mouse Wheel to zoom in for bigger text. 
--->

<span><b>H</b></span>ello. My projects can be found below. Click on the title link to learn more:

[ Website in process of being built. Some projects in progress are not added yet and will be added later. ]

## Table of Contents

- [One is 1](#Oneis1)
- [tw](#tw)

---

<p style="font-size:20px"><b>
<a href="https://wlg1.notion.site/Experimental-Records-33ca6dad981343abb00a974a6c4e3607">One is 1: Analyzing Activations of Numerical Words vs Digits</a>
</b></p>

<img src="/index_imgs/number_heads.PNG" alt="Figure 10 – Middle Heads for “Adam is 1…” prompts" style="width: 75%; height: auto;">

This is a hackathon project submitted to the <a href="https://alignmentjam.com/jam/interpretability">Interpretability Hackathon 3.0</a> (under a similar name; see note on how the projects are ordered on the site) [^1]. To test for the existence of shared circuits, I compare the activations of analogous numerical sequences, such as the digits “1, 2, 3, 4”, the words “one, two, three, four”, and the months “January, February, March, April”. These findings demonstrate preliminary evidence suggesting that these semantically  related sequences share common activation patterns in GPT-2 Small, and allow the construction of a hypothesized circuit that detects and moves numbers, sending relevant information from attention heads to MLPs to  obtain the next number or analogous element. The techniques used include activation patching, attention pattern analysis, neuron feature analysis, mean ablation, logit lens, and circuit surgery.

The pdf report can be found <a href="https://drive.google.com/file/d/1dIcwn0nUWRy548npN_ECb56E-lHbsLCC/view?usp=sharing">in this link</a>, and this is the <a href="https://github.com/wlg100/numseqcont_circuit_expms">link to the code and experiments</a>. A short video, approximate to the project's 7min presentation limit, <a href="https://vimeo.com/846333360?share=copy">is showcased here</a>.

# Oneis1

[^1]: <u>Note on the project ordering:</u> The order of the projects is only ordered for the top 4, while the rest of the ordering is the submission order from latest to earliest (I observed this as I had submitted the 3rd entry, but it appears as the 1st now as the other two were moved when pinned as 2nd and 3rd place)

---

<p style="font-size:20px"><b>
<a href="https://wlg1.notion.site/Experimental-Records-33ca6dad981343abb00a974a6c4e3607">Transformer Comparison Circuit Experiments</a>
</b></p>

###### tw

Based on previous work that used techniques such as causal tracing and dot product congruence [ Interpretability in the Wild, "An" Neuron, etc to be cited ], these experiments look, in large language models, for circuits which compare information, such as sizes. For the GPT-family of models, this work is currently investigating:
<ul>
<li> Adjective Identification Circuits </li>
<li> Most Recent Subject Circuits </li>
<li> Not Identification Circuits </li>
<li> Antonym Identification Circuits (related to Adjective ID Circuits) </li>
</ul>

Records of experiments and notes are found in the link below:

<a href="https://wlg1.notion.site/Experimental-Records-33ca6dad981343abb00a974a6c4e3607">Experiments Index</a>

The video below is a short introductory overview of some work done so far:

<iframe width="560" height="315" src="https://www.youtube.com/embed/Mh5N7VLdKcM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

This links to a series of videos that goes over the details of the work done so far:

<a href="https://wlg1.notion.site/Videos-Interpret-Attention-Head-Circuits-of-Comparison-Inputs-DRAFTS-24b67e08b1d74f70be8ed3012e8278bc">Videos- Interpret Attention Head Circuits of Comparison Inputs (DRAFTS)</a>

---

These pages are supplemental to the experiments:

<a href="https://wlg1.notion.site/Notes-0c9ac6d4ec58411bb2d462ed854840c9">Notes</a>

<a href="https://wlg1.notion.site/Techniques-Compendium-ea12d22f5a8940b190b553d17200ba08">Techniques Compendium</a>

<a href="https://wlg1.notion.site/Ideas-b7fe100b6ddf4b3c84d702dc4b918ce6">Ideas</a>

---
<p style="font-size:20px"><b>
<a href="https://www.youtube.com/@neoknowstic">Educational Videos on AI Safety and Neural Network Mathematics</a>
</b></p>

<b>Why do Neural Networks use Linear Algebra? -- The Visual Intuition of Cat Mathematics</b>

<iframe width="560" height="315" src="https://www.youtube.com/embed/DHjwbleAgPQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

This is the first video in a series aimed at a general audience explaining the math behind neural network interpretability. The first video introduces the geometry of latent space for a simple MLP, explaining concepts such as the relations of neurons and feature vectors, basis vectors, dot product, and hypotheses about latent space arithmetic. To be accessible to laymen, it starts with simple multiplication and change of units, gradually extending this to matrix multiplication (see note on the youtube algorithm) [^2].

[^2]: <u>Note on the youtube recommendation algorithm:</u> This video was climbing up in views each day until its reupload due to audio issues; afterwards, it gained very little views. It may have gotten penalized due to being nearly identical to the previous upload, as there are claims that youtube penalizes duplicate videos. Claims state the algorithm recommends videos based on current news/trends, which do not have to be large but just "large enough" (windy, not even a hurricane). Small trends meant similar videos are swept up in the conglomorate and recommended. The #SoME3 competition at the end of August 2023 is usually when educational videos trend; once the third video (about Diffusion Model Editing) on this channel is uploaded for that competition, it is expected that the other videos will also be recommended alongside it.

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
  <img src="/index_imgs/final_model.PNG" width="350" height="300" alt="">
  <img src="/index_imgs/datasci_networks.png" width="350" height="300" alt="">
  </div>
</div>

---
<p style="font-size:20px"><b>Using Materialized Views for Answering Graph Pattern Queries</b></p>

This dissertation is about developing algorithms to search for patterns in networks using smaller patterns that were already discovered. For example, a knowledge graph may describe entities based on observed features, but not identify them. To search for Shiba Inu, one can input a query with connections to "Japanese", "long snout" and "pet". If the dog pattern made of "long snout" and "pet" was already found, it would filter out many wrong candidate entities. These re-usable intermediate results may be pre-computed and stored. 

Overall, this work is embedded within the field of graph homomorphism matching, which involves finding subgraph patterns in large datasets, going from local matches (of features) to more global matches (of features). In simple terms, graph homomorphisms "map relationships" between graphs where some connections may be lost or merged, allowing for a more relaxed mapping than graph isomorphisms. These relationship mappings must meet certain types of structure-preserving conditions such as if $$f: A \rightarrow B$$ is a relation in system 1, $$h(A) = X$$ and $$h(B) = Y$$, then $$g: X \rightarrow Y$$ is a relation in system 2. This is similar to inference via analogical reasoning.

Analogously, studies found that image recognition neural networks contained neurons that acted as feature detectors, such as ones that are highly activated given inputs of dogs. However, it has been <a href="https://distill.pub/2020/circuits/zoom-in/">hypothesized that many concepts are stored not just in one neuron, but in sub-networks of neurons, also called circuit motifs, which build into larger motifs.</a> For instance, we can speculate that there may be an abstract dog circuit pattern and a Japanese circuit pattern, and adding more connections between them composes them together into a more specific Shiba Inu circuit. 

<a href="https://www.neelnanda.io/mechanistic-interpretability/glossary">The concept of universality</a> hypothesizes that "the same circuits will show up in different models". This means it may be possible to map structures between graphical representations of models. However, these mappings may not be defined using exact graph structures as in a graph isomorphism, but may be defined using analogous functional relations, similar to graph homomorphisms.

Graph pattern matching from local matches to global matches is a technique previously used in other fields of AI, such as in Forbus's work on <a href="https://groups.psych.northwestern.edu/gentner/newpdfpapers/FalkenhainerForbusGentner89.pdf">analogical pattern matching.</a> This research is connected to the <a href="http://worrydream.com/refs/Hofstadter%20-%20Analogy%20as%20the%20Core%20of%20Cognition.pdf">work on AI analogies done by Hofstadter.</a> Recently, the concept of graph homomorphism has been used by Redwood Research to help <a href="https://www.lesswrong.com/posts/JvZhhzycHu2Yd57RN/causal-scrubbing-a-method-for-rigorously-testing
">better formalize experimental methods in the field of neural network interpretability.</a>

<a href="https://drive.google.com/file/d/14LE1NA99XAleU2hP3XW_cAYiLnmRhJcO/view?usp=sharing">This pdf is a trimmed version of the work.</a>

<a href="https://docs.google.com/presentation/d/1OATw2tZGqq4hStwWnnWqRNIW0gzisAqi/edit?usp=sharing&ouid=111542027497665621431&rtpof=true&sd=true">These slides provide a beginner's introduction to the work.</a>

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




