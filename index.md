**An Intuitive, Visual Guide to the Math of Hidden Encoding Spaces in Deepfakes and Image Generation**

What is the mysterious connection between neural networks and strange mathematical concepts such as Klein bottles [On the Local Behavior of Spaces of Natural Images]? These concepts are encountered in several neural network papers, yet remain enigmatic to those who are unfamiliar with certain fields of research. On a similar note, for those who have taken a linear algebra class but have not applied it to advanced neural network design, it is also perplexing how concepts such as eigenvectors are used in these papers.

These mysterious connections can be explained by understanding the spatial representations of what neural networks learn. 

Neural networks are functions that transform data into different representations, which can reveal hidden information about the data. This is similar to using an analogy to better understand a problem from a different perspective. [citation]

[figure with an analogy alongside NN transforms on top]

The term “latent spaces” is often seen when discussing generative neural networks, where ‘latent’ means ‘hidden’, and thus, ‘not directly observable’. Latent spaces contain representations of data which can be transformed (decoded) into images, or which images can be transformed (encoded) into. As seen in figure X, we can understand representations of data by examining their geometric (such as lengths and angles) and topological (such as connectivity) properties. [paper citation]

[figure with labels of ‘encoded’ and ‘encodings’, and ‘decodings’]

Informally, the title of this guide refers to any space that represents data as a “hidden encoding space”, which is a name not used elsewhere.

Our main goal in this guide is to figure out how to control the ways specific features are learned in neural network representations by changing algebraic aspects of its models and algorithms. This can help to design: 1) New techniques for interpreting the decisions made by neural networks, and 2) New neural networks that are easier to interpret (for humans). Improving the interpretation of neural networks leads to enhanced control over what features we want a neural network to focus on; this practice is called Style Editing. [citation]

[figure] arrow from control features to algebra. Style edit example: Eg) to generate specific features of faces when we convert a face from young to old in a deepfake.

To do this, we will examine techniques in papers about neural network interpretability and work backwards to explain why these techniques work. Along the way, we’ll build up a strategy guide that acts as a look-up table for issues encountered when developing new solutions for interpreting neural networks.

An introduction to the latent spaces of generative models is given in section 1. The mathematical explanations of interpretability techniques begin in section 2.

PREREQUISITES: This guide is for anyone who has a basic understanding of neural networks and linear algebra, but is unfamiliar with the math used to identify how features and learned and composed in a neural network. The only recommended course prerequisites are those 2 playlists, both which only take a few hours to go through in total [cite NN and LA in 3b1br].
FOOTNOTE: Everything else will be introduced as the paper progresses; if a prerequisite is needed that is not explained in the paper, a link will be given to a specific part such that it would only take 5-10 minutes to get an intuitive understanding of it. Only a high level understanding of these concepts is required, not a detailed one, although a detailed one would allow you to make more connections that a high level one by itself cannot.

<span style="color:silver">Statements backed up by only “weak evidence” are in gray</span>, and <span style="color:lightgray">statements that are “pure speculation” are in light gray</span>.

**[ch1](ch1.md)**

**[ch2.1](ch2.1.md)**

**[ch3](ch3.md)**


[link to compendium of issue->solns and techniques]

<!---
<span style="color:lghtgray">
</span>
-->