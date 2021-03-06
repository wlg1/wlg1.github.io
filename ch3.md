**Composing neurons to get circuit gates**

In section 2, we described how features are related to one another from the perspective of transformations in latent space; in this section, we will look at feature relationships from the perspective of neuron circuits. These two types of models reveal different hidden aspects of feature relationships, and have their own pros/cons when it comes to interpretation.

Techniques:

Section A: decomposition of circuits to find motifs (matrix factorization, complex network analysis on brains (simplicial set hierarchies and motifs such as cavities), sheaves, analogies

Section B: saliency maps and attribution, gradient ascent on inputs to max neuron activation, TDA for feature interpretation (measuring by betti number)

Papers:
<ol>
<li>Compositional Explanations of Neurons</li>
<li>Distill: Building Blocks, Feature Visualization, Grand Tour, Circuits (Thread), etc.</li>
<li>The why, how, and when of representations for complex systems</li>
<li>Network Dissection</li>
<li>The Structure-Mapping Engine (1986)</li>
<li>Analogy as the Core of Cognition (2005)</li>
<li>[There are many papers about persistence homology on NN, such as "Topology of Deep Neural Networks"]</li>
</ol>

3.1: A high level introduction to neuron composability

**Collective decision making**

No hidden layers:

We will start with how a single neuron makes its decisions, and then show how the decisions of individual neurons affect the decisions of other neurons in a neural network. Using a linear activation function such as the identity, an output neuron function o=g(XW+b) becomes o=XW+b, which is a hyperplane acting as a decision boundary that can be fitted onto the input space X, with basis {x1,x2}, by solving for x2 in terms of x1, or vice versa (both equations will give the same hyperplane); a hyperplane can be generalized to higher dimensions of X. When a nonlinear activation function is used, this decision boundary is a hypersurface. For multiple classes, multiple hyperplanes are fitted to obtain a score for each class, and the highest score is taken; thus, a neural network with C classes has C output neurons, each with its own decision boundary.

Note how similar this is to logistic regression: in both cases, the final output value (which can be thought of as a probability for a binary class) for each hypersurface is compared to a threshold, and is converted into a discrete value of 0 or 1. [ng 6.3, 2m and 8m]

FOOTNOTE: Hypersurfaces are manifolds embedded in ambient space

[figure fitting hyperplane showing how classification works. label pts and planes with equations for a= and x1= and x2= in actv space and input space, resp. another plot showing hypersurfaces. use matlab

[figure with z = XW + b, showing g(z) > 0.5 when z > 0, then showing how log regr discretizes the sigmoid output into 0 or 1] [Ng, 6.3, 2:20]
[compared to another plot single neuron function]

o = w11\*x1 + w12\*x2 + b 
x2  = (o - b) / w12 - w11/w12 \* x1 
y = b + mx
]

One hidden layer:

A well-known issue is that the XOR problem cannot be solved by neural networks with a single neuron because the neuron can only model one line, while the XOR problem requires two hyperplanes to partition correctly. Thus the output neuron requires two neurons in a "hidden layer" to help it makes its final decision of 0 or 1. The output neuron to composes the 2 hidden layer neurons into one function; without it, the outputs of the 2 hidden layer neurons cannot communicate with each other, and thus will only each see one perspective of the data, while the output neuron can take into account multiple perspectives. [Deep Learning Book, pg173: XOR problem]

[figure of XOR with hyperplanes, arrows of each plane to a neuron in neural network]

Unlike an output neuron, a hidden layer neuron doesn't have a threshold function that converts continuous values into binary discrete values. Thus, hidden layer neurons are not treated like functions in logistic regression, and only the output layer neurons are associated with decision boundaries that can be plotted in input space. 

[o = w1\*a1 + b1 + (w2...) = <- substitute a1(x1,x2), show o(x1,x2) ]

But we saw a picture where XOR was solved with 2 lines; doesn't each line correspond with a hidden layer neuron function? Those 2 lines do not make up a function; in that mapping, there exist x1 values with have 2 values of x2, which contradicts the definition of a function. Thus, the ACTUAL hypersurface associated with the output neuron is a curvy, nonlinear function as shown in the figure below:

[figure comparing non-function hypersurface on X vs nonlinear function hypersurface x1(o,x2) on XOR input space]

Instead of associating hidden layer neurons with decision boundaries, it is better to see their activation values as introducing a different dimension onto the input space X. 

[fig: x1 vs x2 vs a1; x1 vs x2 vs a2; a1 vs a2 each with their own x1x2-plane]

FOOTNOTE: ?? Remember, the activation space axis always exists in the input space; it’s just hidden as a vector. [3B1Br projections, duality and functionals?] We are simply changing to their basis using the neuron function: First linear rotation, then linear shift, then a nonlinear "squeeze"- do non-linear operations change into a different basis? actv space is still a linear subspace ??

With the logistic regression model or the single neuron perceptron, an analogy from the function to a human making a decision can be made: we think of the neuron as saying "If a data point is on one side of my decision boundary, then 0, else 1".

With hidden layer neurons, we can still make an analogy from the output neuron to a human, but the human analogous to it has a more complicated thought process: "If neuron A says it's sure by a degree of '22' that the observation is in class 0, while neuron B says it's only sure by a degree of '4' that it's in class 1, and I trust neuron A only 0.2 but trust neuron B with 0.7, then by -0.02\*22 + 4\*0.7 = 2.36 (using bias=0 and the sigmoid as the activation function that squishes 2.36 into 0.91), I still think it's most likely in class 1 because A's belief that it's in class 0 is not strong enough compared to how much I trust A and B and to B's belief."

[figure of XOR output neuron making decisions using continuous values]

By knowing that each neuron has a role in decision making, we can better understand why multiple neurons passing on information to successive layers can model almost any function for partitioning data [cite univ approx]. Each output neuron function can be seen as a piecewise function of hypersurfaces, such that each piece of the function is approximated by a hidden layer neuron’s hypersurface. Although it was mentioned that the final output layer function was not simply just the collection of hypersurfaces associated with each hidden layer neuron, each neuron does end up contributing to the final function in some way, just much more nuanced than just taking the collection of them.
CITE:
https://towardsdatascience.com/every-machine-learning-algorithm-can-be-represented-as-a-neural-network-82dcdfb627e3

[This link also shows how composability makes NN more general than every other machine learning technique; every ML technique can be represented as a NN.]

We can extend this analogy about a neuron being analogous to a human to an entire neural network, which would be analogous to a society in which each person makes judgments based on the opinions of multiple people, each specializing in looking at observations from their own perspetive, and taking into account multiple other opinions at once based on how much they trust each other individual.

**A neuron’s “meaning” can only be derived in relation to other neurons**

<span style="color:silver">
Let an observation be a data point in X. We will informally define a feature as some aspect of an observation. Since each neuron measures some aspect of an observation, each neuron gives its own opinion about some feature. But these features may not be human-interpretable (although neural networks have been designed such that the neurons in the last layer ARE human-interpretable, as each one gives its opinion about one of the classes). While Convolutional Neural Networks can be intuitive to interpret because they compose spatial features from smallest to largest (eg. edges to eyes), other neural network neurons are harder to interpret because the input space is not spatially interpretable to us like an image is. 

In the activation space of a hidden layer, each axis is a neuron. Each datapoint (observation) is a vector in the activation space. Thus, a transformation from input space to activation space is DESCRIBING each observation from the perspective of different features, just like using an analogy to make something new relate to something meaningful in our brain. 

When animal brains make analogies between two spaces, they are using analogical reasoning to build up mappings between objects in the two spaces. Analogical reasoning is similar finding mappings that preserve the property of a "commutative diagram in structure preserving map", which states that given relations m within a space and map H between spaces (a map is a set that contains mappings), hm = mh. This property means when finding whether two features are analogous, it only matters to find how they relate to other features. The Structure-Mapping Engine (SME) [citation] is a system that utilizes this property to find analogies between two relational graphs.

[figure: commutative diagram in structure preserving map, SME]

How do we capture that two features are similar and thus "equivalent" under a map? Define an abstract class as a set in which all objects share some property. For example, the abstract class of "planets" includes Mercury and Venus. When describing a planet, Mercury and Venus are "equivalent", as their specific details that distinguish them from each other do not matter, only their generalized description of being a planet.

A neural network does not take in two relational graphs and output a map. But neurons do activate in similar ways for similar features in observations. We may think of observations as containing raw data, while a relational graph is a description of raw data in terms of relations between features. Thus, just as analogies are made between features with similar relatons, neurons activate in similar ways for observations with similar features. These "similar features" can all be put under abstract classes, in which two features in the same abstract class are eligible for being mapped to one another. For example, if a neural network's neuron learns to judge its belief in an "eye" feature, it can judge its belief that an eye exists in a specific observation by "analogously" comparing it to previously seen observations. It is judging its belief of whether some region (similar to an entity in a relational graph) of the observation is in the abstract class of "eye" or not.

Note that in order to judge its belief that an eye exists, the neuron relies on the judgments of other neurons which judge features such as "vertical edges" or "eyelids"; thus, judging whether a region (or candidate feature) is in an abstract class or not may rely on describing as a combination of other abstract classes. We describe an example that illustrates the similarities of a neural network to how analogies are made.

NOTE: The following is only a loose analogy meant to investigate a proposed similarity to determine its superficial vs structural properties. It is not how neural networks actually work. As said before, "Do not confuse the map for the territory"; one must check for contradictions.

Figure 3.X: The purpose of the analogy of the "Tortoise and the Hare" is to state that the less skilled competitor may when if they have a better work ethic. Thus, an algorithm can determine, in a new case, who are the competitors, and which one is more similar to the Tortoise, and which one is more similar to the Hare. Then, it states that the "Tortoise-analogous" entity has a good chance of winning due to its "work ethic".

When making an analogy of an observation to the "Tortoise and the Hare", one step is to map entities in the new case to the entities of "Tortoise" and "Hare". In the made-up neural network in Figure 3.X, one neuron outputs its belief that there is a Tortoise in an image or a region of the image. Another neuron outputs its belief for a Hare. There may be multiple neurons tasked with recognizing these entities; perhaps one checks if "there exist a Tortoise", and another pinpoints "where", and another pinpoints "its distance from the hare", and then they all send their beliefs to more neurons that make more "executive" decisions about which entity is, or which region in an image contains, the analogous to the Tortoise. 

One of these neurons that works to recognize the Tortoise is tasked with determining what is in the abstract class of “Someone who is slow”; but to do this, it requires the output of another neuron which determines what is in the abstract class of "Someone who is worse", which is an abstract class that contains the abstract class of "slow". Why? Because perhaps the idea of "slow" does not exist in the observation at all! Rather, even the idea of "slow" must be mapped to something else. If the neural network requires finding what in the observation is "slow", it is like it is overfitting to the observation; it is requiring that a specific attribute must exist, when in actuality this analogy can be applied to the abstract class of "worse", which in the context of the "Tortoise and the Hare" is more general than "slow". In other words, the neural network is taking the analogy too literally.

![Figure 3.X](/images/figure3.X.png)

FOOTNOTE: Though we have not formally defined the output of a neuron as a "belief", we can informally think of these outputs as analogous to "probabilities" [cite Dempster-Shafer theory]. In Figure 3.X, there is a probability the neuron guessed trait A correctly, and that propagates to the probability that the (A<B) neuron will have a correct guess that Obj 1’s trait is worse than Obj 2’s trait. Note that the (A<B) neuron cannot exist by itself; it must exist in relation to the other neurons in its circuit. Without those other neurons, it is meaningless. 

SME works starting from mappings which are locally consistent (that is, satisfying the commutativity diagram property) for what is mapped so far to those which are more globally consistent as more mappings are built up. In each step that adds a new mapping, it must ensure that the commutativity diagram property of Hm=mH is not violated.

[figure of SME's procedure]

In a convolutional neural network, it has been found that early layers recognize local features such as edges, and later layers recognize features that piece together features recognized from previous layers [citation]. CNN is analogous to SME in that it must first make sure that its decisions are locally consistent, and once those are ensured, it can use them to decide on more globally consistent decisions. Though a neural network does not have the task of preserving Hm=mH built into its algorithm, the fact that a "composing" neuron takes in multiple features (weighing each one) may mean that all those features are related to one another through that neuron. Although there is no relational graph describing the raw data, each "composing" neuron may be describing the relations in an observation, and thus are analogous to the edges of a relational graph. If this analogy holds, then a neural network is judging the likelihood that certain edges exist in a relational graph, and may be building something analogous to a relational graph on top of an observation. It is then comparing that relational graph to previously learned relational graphs. 

Under this assumption that this analogy holds, composing neurons are not just describing edges, since they take in the outputs of other composing neurons- they are describing subgraphs. Therefore, it may be that there are neurons (or groups of neurons) that have learned to find analogies to relational subgraphs, and these neurons pass on their belief in these analogies to more neurons that find relational subgraphs depending on analogies to other relational subgraphs. 

Analogous features may have similar neuron firing patterns, and thus the same pattern of neurons within a network may fire for these analogous features. Patterns in a network have been called "motifs" [citation], and in the context of neural networks, have been called "circuits". Much work has been done in not only providing evidence for the existence of these circuits, but in characterizing them similar to how biologists characterize the functions of genetic patterns in DNA [Distill: Circuits Thread]. 

[figure proposing how relational graphs are made by circuits] 

Note that circuits are a type of subgraph, and relational graphs are another type of subgraph. They should not be confused. Circuits cannot be relational graphs because each edge in a neural network is not a relation, but an indication of which outputs are used as inputs in which neurons. One cannot find "analogous subgraph patterns" in the graphical layout of circuits. Rather, circuits implicitly may be building up relational subgraphs; to reveal them, one may have to apply a transformation on the outputs of circuits that shows how the features they recognize are relatively composed into other features.

The circuits of neural networks may allow networks to capture analogies not capturable by a relational graph, which may be too restrictive of a model.

One issue is the number of neurons may be less than number of features. It is likely that many neurons have multiple purposes; in other words, they are polysemantic. [cite specific Circuits thread section]
</span>

**Evolving AI Memes**

<span style="color:silver">
Once we identify what certain circuit motifs do in a neural network, we may not need for other neural networks to relearn them; we can piece them together via transfer learning from parts of other neural networks. It may also be that a neural network can piece these "inherited parts" together by itself- it may be more efficient to just insert a few pieces into it, then have it learn how to piece them together in a way that allows it to adapt to its environment, which may contain new but similar tasks that the network's "ancestors" did not encounter before.

This procedure is similar to genes giving a prior set of skills to an organism, or memes giving a ways of making analogies between new cases and previously learned patterns. These analogies conjure up the idea that some inheritable parts may be more beneficial than others in certain environments, leading to an evolution of motifs. One way this can occur is to allow neural networks to figure out which motifs are the best and transfer them to others horizontally (like in viruses [cite horizontal gene transfer]) or vertically (like having children) to "learn from each other". The key to doing this effectively is to encode algorithms into the AI that both determine WHICH motifs to pass on, and learn how to stitch them together in another neural network.

We already have discovered important architectural motifs (such as LSTMs) but other work proposes to learn them [cite "Evolving neural networks through augmenting topologies"]. GANs already contain neural networks interacting to improve each other; competition drives evolution.

In a loose analogy, just like how each person makes a decision based on the opinions of others in a society, we can think of each person as a neuron that makes a decision, and an entire society as a neural network. Interestingly enough, each person has their own neural network that is similar to an artificial neural network, suggesting some sort of self-similarity.
</span>

<!--
What determines what each neuron specializes in? Is it their ‘random’ initialization value in relation to other random initialization values?

complex systems "converge" towards learning analogies? (eg. same relational graph, not necc in the same circuit subgraph, appears in similar networks?)

-->

