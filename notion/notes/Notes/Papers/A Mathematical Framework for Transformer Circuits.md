# A Mathematical Framework for Transformer Circuits

**[Transformer Overview](https://transformer-circuits.pub/2021/framework/index.html#transformer-overview)**

[Model Simplifications](https://transformer-circuits.pub/2021/framework/index.html#model-simplifications)

- What does "folding" mean here:
layer norm could be substituted for batch normalization (which can fully be folded into adjacent parameters).
    
    In the context of machine learning, "folding" refers to the process of incorporating one set of parameters or operations into another set of parameters or operations in a way that reduces the number of overall parameters in the model.
    
    instead of using batch normalization, which requires additional parameters to be added to the model, one could use layer normalization instead. Layer normalization does not require any additional parameters beyond the existing parameters of the layer, and as a result, can be "folded" into the existing parameters of the layer. See: [****Batch and Layer Normalization****](../Neural%20Networks%20e6abb23474464e098117dced189fb7bb/Batch%20and%20Layer%20Normalization%20683d66e7db994beda71b25499d026b48.md) 
    

****High-Level Architecture****

Residual stream: the iterative equation ${x_i}$

${m(x_i)}$ : a function which performs linear projection on ${x_i}$

![Untitled](A%20Mathematical%20Framework%20for%20Transformer%20Circuits%20236be728258d45febca2b1bf2ab0aa4b/Untitled.png)

****Virtual Weights and the Residual Stream as a Communication Channel****

**Bottleneck Activations**: We say that an activation is a bottleneck activation if it is a lower-dimensional intermediate between two higher dimensional activations.

### ****Attention Heads are Independent and Additive****

![Untitled](A%20Mathematical%20Framework%20for%20Transformer%20Circuits%20236be728258d45febca2b1bf2ab0aa4b/Untitled%201.png)

[ Each of these matrices affects how attention is calculated b/w each token’s residural streams. So if attention is important for an input (say an analogy pattern), one should look at pinpointing which decomposed matrix is important, too ]

![Untitled](A%20Mathematical%20Framework%20for%20Transformer%20Circuits%20236be728258d45febca2b1bf2ab0aa4b/Untitled%202.png)

********************Zero Layer: Embed, Unembed********************

![Untitled](A%20Mathematical%20Framework%20for%20Transformer%20Circuits%20236be728258d45febca2b1bf2ab0aa4b/Untitled%203.png)

**One Layer**

an ensemble of a bigram model and several "skip-trigram" models (affecting the probabilities of sequences "A… BC")

Path expansion: transforms the product (where every term corresponds to a layer), into *a sum where every term corresponds to an end-to-end path*.

A bilinear form is a mathematical function that takes two vectors as inputs and returns a scalar value.

QK circuit: on which token?

OV circuit: how does attending to that token affect the logit?

****Interpretation as Skip-Trigrams****

The QK circuit determines which "source" token the present "destination" token attends back to and copies information from, while the OV circuit describes what the resulting effect on the "out" predictions for the next token is. Together, the three tokens involved form a "skip-trigram" of the form `[source]... [destination][out]`, and the "out" is modified.

There's also all the usual issues that come with understanding the weights of generalized linear models acting on correlated variables and fungibility between variables. For example, an attention head might have a weight of zero because another attention head will attend to the same token and perform the same role it would have.

---

[https://www.youtube.com/watch?v=KV5gbOmHbjU&ab_channel=NeelNanda](https://www.youtube.com/watch?v=KV5gbOmHbjU&ab_channel=NeelNanda)

**10:05:** Chris tried interpreting tiny models trained on mnist and this didn't work; the larger the models got, the more interpretable they seem to be. this seems not be the case in Transformers

**********27m:********** The residual stream is a sum of “everything”, so you can decompose it into a sum of terms. The model can choose which parts it wants to go through the residual stream. Decompose paths (eg. MLP to unembed) into parts which are interpretable, as the residual stream as a whole is hard to interpret.

**35m:** Everything interacting with residual stream is linear, but usually only non-linear allows meaningful basis directions (why?) So no reason residual stream should have privleged basis

Which vector spaces have priveleged basis: input tokens, vocab, output logits, MLP (somewhat)- WHY?

(from Tim Detmers paper): some directions in residual stream are bigger (more interpretable/meaningful) than others- WHY?

adding/subtracting directions cause larger’s float bits to dominate smaller’s, making it less precise (?)

### Virtual Weights

**41m:** Each layer projects (reads) from res stream (onto layer) then embeds (writes) back out onto res stream.

The internal dim of a layer (eg. an attn head) is smaller than res stream dim. Thus, each layer focuses on a few (meaningful?) directions

Usually transformers hard-code MLP to have 4x as many neurons as residual stream width

Superposition: model compresses MLP dims into residual stream. Allowed when vectors can have close-to-zero dot products. The vectors are compressed into “bottleneck activations”

**49m:** Each non-zero dot product (projection) with a feature has interference. But most features are sparse (not important) (eg. “firework” is sparse b/c it’s not in most inputs). Also, some features encode multiple uncorrelated concepts (eg. a feature can be both “python lists” and “vampires” because those two rarely occur with one another, so using that feature won’t cause a mix-up of which it’s referring to if you know the rest of the input’s context)

Residual stream is purely linear, so it can have more superposition features (which occur more with linear projections?)

**52:09:** the model is ultimately making a trade-off between I want to represent more features and I want to cleanly read out the features without noise and interference 

Res stream is like memory; messages that are sent between say layer 1 and layer 3 which are totally useless for all future layers but it's going to stick around and the model does not have an automated way of clearing this out. But NN may learn to do this w/o explicit instructions by outputting a “negative direction” to “zero another direction out”.

### ****Attention Heads are Independent and Additive****