# Scaling Monosemanticity- Extracting Interpretable Features from Claude 3 Sonnet

[https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html#safety-relevant-deception](https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html#safety-relevant-deception)

- SAE training details
    
    We focused on applying SAEs to residual stream activations halfway through the model (i.e. at the “middle layer”). We made this choice for several reasons. First, the residual stream is smaller than the MLP layer, making SAE training and inference computationally cheaper. Second, focusing on the residual stream in theory helps us mitigate an issue we call “cross-layer superposition”
    
    We trained three SAEs of varying sizes: 1,048,576 (~1M), 4,194,304 (~4M), and 33,554,432 (~34M) features. The number of training steps for the 34M feature run was selected using a scaling laws analysis to minimize the training loss given a fixed compute budget (see below). We used an L1 coefficient of 5 3 . We performed a sweep over a narrow range of learning rates (suggested by the scaling laws analysis) and chose the value that gave the lowest loss.
    
    For all three SAEs, the average number of features active (i.e. with nonzero activations) on a given token was fewer than 300, and the SAE reconstruction explained at least 65% of the variance of the model activations. At the end of training, we defined “dead” features as those which were not active over a sample of 107 tokens. The proportion of dead features was roughly 2% for the 1M SAE, 35% for the 4M SAE, and 65% for the 34M SAE.
    

[**LIMITATIONS, CHALLENGES, AND OPEN PROBLEMS**](https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html#discussion-limitations)

**Cross-Layer Superposition.** That is, gradient descent often doesn't really care exactly which layer a feature is implemented in or even if it is isolated to a specific layer, allowing for features to be “smeared” across layers. 
even if features are represented in cross-layer superposition, their activations all get added together in the residual stream, so fitting an SAE on residual stream layer X may suffice to disentangle any cross-layer superposition among earlier layers.

features which are partly represented by *later* layers will still be impossible to properly interpret. 

**Getting All the Features and Compute.** We do not believe we have found anywhere near “all the features” that exist in Sonnet, even if we restrict ourselves to the middle layer we focused on.

The first is to make sparse autoencoders themselves cheaper – for example, perhaps we could use a mixture of experts

Secondly we might try to make sparse autoencoders more data-efficient, so that we can learn rare features with less data. One possibility of this might be [Attribution SAEs](https://transformer-circuits.pub/2024/april-update/index.html#attr-dl) described in our most recent update, which we hope might use gradient information to more efficiently learn features.

**Shrinkage.** We use an L1 activation penalty to encourage sparsity. This approach is well known to have issues with “shrinkage”, where non-zero activations are systematically underestimated

We need an answer to [attention superposition](https://transformer-circuits.pub/2024/jan-update/index.html#attn-superposition)

<<<

[Ablation] is much slower since it requires one forward pass for every feature that activates at each position, so we often used attribution as a preliminary step to filter the set of features to ablate. 

[**Example: Emotional Inferences**](https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html#computational-sad)

The fact that both features contribute to the final output indicates that the model has partially predicted a sentiment from John's statement (the second feature) but will do more downstream processing on the content of his statement (as represented by the first feature) as well.

- Can we better formalize these causal relations between features?

---

[https://www.anthropic.com/research/mapping-mind-language-model](https://www.anthropic.com/research/mapping-mind-language-model)

There was both an engineering challenge (the raw sizes of the models involved required heavy-duty parallel computation) and scientific risk (large models behave differently to small ones, so the same technique we used before might not have worked). 

[https://arxiv.org/abs/2001.08361](https://arxiv.org/abs/2001.08361)

We successfully extracted millions of features from the middle layer of Claude 3.0 Sonnet

Whereas the features we found in the toy language model were rather superficial, the features we found in Sonnet have a depth, breadth, and abstraction reflecting Sonnet's advanced capabilities.

We see features corresponding to a vast range of entities like cities (San Francisco), people (Rosalind Franklin), atomic elements (Lithium), scientific fields (immunology), and programming syntax (function calls). These features are multimodal and multilingual, responding to images of a given entity as well as its name or description in many languages.

We also find more abstract features—responding to things like bugs in computer code, discussions of gender bias in professions, and conversations about keeping secrets.

they dont mean abstract as in ‘general classes’ but as in less tangible things

**This shows that the internal organization of concepts in the AI model corresponds, at least somewhat, to our human notions of similarity. This might be the origin of Claude's excellent ability to make analogies and metaphors.**

[https://www.youtube.com/watch?v=CJIbCV92d88&t=35s&ab_channel=Anthropic](https://www.youtube.com/watch?v=CJIbCV92d88&t=35s&ab_channel=Anthropic)

Activate “bridge” feature then ask Claude about its physical form. It replies its form is a “bridge”

Forcing a “scam email” feature to fire makes Claude comply with unethical requests

[this feature steering is done before; similar to codebooks]

**The features we found represent a small subset of all the concepts learned by the model during training, and finding a full set of features using our current techniques would be cost-prohibitive (the computation required by our current approach would vastly exceed the compute used to train the model in the first place).** 

**Understanding the representations the model uses doesn't tell us *how* it uses them; even though we have the features, we still need to find the circuits they are involved in. And we need to show that the safety-relevant features we have begun to find can actually be used to improve safety. There's much more to be done.**