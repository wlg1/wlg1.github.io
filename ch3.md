<span style="color:silver">
**Composing neurons to get circuit gates**

Now that we identified how to describe directions in the latent space in terms of neurons, we’ll further describe how these neurons relate to each other. In section 2, we used the spatial perspective and transformations; now, we look at it the perspective of analogies that complex systems move towards, relating them to show they are describing the same system from two different perspectives (or models), each with its own pros/cons when it comes to interpretation.
Then we’ll see how composability makes NN better than other techniques, and also is related to its Universality in function approximation

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

First, a high level introduction to composability.

**XOR gate**

In the hidden layer, the network requires 2 neurons to make a decision because one neuron cannot as it specializes in only one binary separation. Then it requires a 3rd output neuron to compose the 2 hidden layer neurons into one that makes a final decision based on the previous two. Due to the continuous outputs of a neuron function, each neuron's decision is not associated with a strict decision boundary that's used in algorithms such as logistic classification, which is akin to how logic gates use discrete values to compute outputs. Instead of saying "if a data point is on the RHS of hyperplane A and on the LHS of hyperplane B, then 0 or 1", the output neuron (which outputs the probability for a binary class) is saying "if hyperplane A says it's sure by a degree of "22" that the observation is in class 0 (based on its distance from the LHS of the hyperplane) while hyperplane B says it's only sure by a degree of "4" that it's in class 1 (based on its position from its RHS), and I trust neuron A only 0.2 but trust neuron B with 0.7, then by -0.02\*22 + 4\*0.7 = 2.36 (using bias=0 and the sigmoid as the activation function that squishes 2.36 into 0.91), I still think it's most likely in class 1 because A's belief that it's in class 0 is not strong enough compared to how much I trust A and B and to B's belief."

[figure of neurons making decisions using continuous values]

**A neuron’s “meaning” can only be derived in relation to other neurons**

Let an observation be a data point in X. We will informally define a feature as some aspect of an observation. Since each neuron measures some aspect of an observation, each neuron gives its own opinion about some feature. But these features may not be human-interpretable. Some of these features measure the location of an observation relative to a hypersurface associated with a neuron, such as in the XOR example. Although this feature of a neuron can be described in human-interpretable terms, it is not linked to an aspect that human brains easily recognize, such as eyes or squares in an image, or the concept of friendliness. However, neural networks have been designed such that the neurons in the last layer ARE human-interpretable, as each one gives its opinion about one of the classes. While Convolutional Neural Networks can be intuitive to interpret because they compose spatial features from smallest to largest (eg. edges to eyes), other neural network neurons are harder to interpret because the input space is not spatially interpretable to us like an image is. 

A neural network can be analogously described as a society in which each person makes judgments based on the opinions of multiple people, each specializing in looking at a different feature, and taking into account all of their opinions at once based on how much they trust that person. 

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

Note that circuits are a type of subgraph, and relational graphs are another type of subgraph. They should not be confused. Circuits cannot be relational graphs because each edge in a neural network is not a relation, but an indication of which outputs are used as inputs in which neurons. One cannot find "analogous subgraph patterns" in the graphical layout of circuits. Rather, circuits implicitly may be building up relation subgraphs; to reveal them, one may have to apply a transformation on the outputs of circuits that shows how the features they recognize are relatively composed into other features.

Once we identify what certain circuit motifs do in a neural network, we may not need for other neural networks to relearn them; we can piece them together via transfer learning from parts of other neural networks. It may also be that a neural network can piece these "inherited parts" together by itself- it may be more efficient to just insert a few pieces into it, then have it learn how to piece them together in a way that allows it to adapt to its environment, which may contain new but similar tasks that the network's "ancestors" did not encounter before.

This procedure is similar to genes giving a prior set of skills to an organism, or memes giving a ways of making analogies between new cases and previously learned patterns. These analogies conjure up the idea that some inheritable parts may be more beneficial than others in certain environments, leading to an evolution of motifs. One way this can occur is to allow neural networks to figure out which motifs are the best and transfer them to others horizontally (like in viruses [cite horizontal gene transfer]) or vertically (like having children) to "learn from each other". The key to doing this effectively is to encode algorithms into the AI that both determine WHICH motifs to pass on, and learn how to stitch them together in another neural network.

We already have discovered important architectural motifs (such as LSTMs) but other work proposes to learn them [cite "Evolving neural networks through augmenting topologies"]. GANs already contain neural networks interacting to improve each other; competition drives evolution.

In a loose analogy, just like how each person makes a decision based on the opinions of others in a society, we can think of each person as a neuron that makes a decision, and an entire society as a neural network. Interestingly enough, each person has their own neural network that is similar to an artificial neural network, suggesting some sort of self-similarity.

<!--
What determines what each neuron specializes in? Is it their ‘random’ initialization value in relation to other random initialization values?
-->

</span>