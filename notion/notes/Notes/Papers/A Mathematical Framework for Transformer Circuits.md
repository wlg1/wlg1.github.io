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

****Virtual Weights and the Residual Stream as a Communication Channel****

---

[https://www.youtube.com/watch?v=KV5gbOmHbjU&ab_channel=NeelNanda](https://www.youtube.com/watch?v=KV5gbOmHbjU&ab_channel=NeelNanda)

**10:05**

Chris has tried things like um interpreting tiny models trained on mnist uh in image stuff and this just basically didn't work and the larger the models got the more interpretable they seem to be uh this seems not be the case in Transformers

**********27:00**********

The residual stream is a sum of “everything”, so you can decompose it into a sum of terms

**28:51**

the model can choose which layers it wants to go through and otherwise just go through this residual connection