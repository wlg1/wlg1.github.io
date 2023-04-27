# Batch and Layer Normalization

[REF 1](https://www.pinecone.io/learn/batch-layer-normalization)

PROB:

- Using mini-batches, it’s possible that the input distribution at a layer keeps changing across batches.
    
    Each batch of samples has its own distribution made from its samples
    
    > For each batch in the input dataset, the mini-batch gradient descent algorithm updates the weights and biases (parameters) so as to fit to the distribution seen at the current batch input to the specific layer
    > 
    
    > Now that the network has learned to fit to the current distribution, if the distribution changes substantially for the next batch, it now has to update the parameters to fit to the new distribution. This slows down the training process.
    > 

REASONING:

> However, if we transpose the idea of normalizing the inputs to the hidden layers in the network, we can potentially overcome the limitations imposed by exploding activations and fluctuating distributions at the layer’s input.
> 

SOLN:

Batch Norm: For every neuron (activation) in a particular layer, we can force the pre-activations to have zero mean and unit standard deviation.

- Normalization vs Standardization
    
    Normalization is typically used when the distribution of the data is not Gaussian or when the scale of the data varies widely. It rescales the data to a range of [0,1] or [-1,1]. This ensures that each data point is within the same range and that the algorithm can converge more quickly.
    
    ![Untitled](Batch%20and%20Layer%20Normalization%20683d66e7db994beda71b25499d026b48/Untitled.png)
    
    Standardization is typically used when the data has a Gaussian distribution and when the scale of the data is not important. It rescales the data to have a mean of 0 and a standard deviation of 1. This ensures that the data is centered around 0 and that the variance is 1, which is useful when using algorithms that assume that the data is normally distributed.
    
    ![Untitled](Batch%20and%20Layer%20Normalization%20683d66e7db994beda71b25499d026b48/Untitled%201.png)
    
    Batch norm is actually “standardization” if we use these terms
    

Layer norm: for each sample, take the average of its features

Eg) sample A = [f1, f2, f3]

mean: avg(f1, f2, f3) —>Standardize each feature in sample A by mean & SD

Batch norm: for each feature, take the average of its batch

Eg) feature x1 = [x1(A), x1(B)]

mean: avg(x1(A), x1(B)) —>Standardize feature x1 in each samp by mean & SD

Batch

Layer

![Untitled](Batch%20and%20Layer%20Normalization%20683d66e7db994beda71b25499d026b48/Untitled%202.png)

![Untitled](Batch%20and%20Layer%20Normalization%20683d66e7db994beda71b25499d026b48/Untitled%203.png)

![Untitled](Batch%20and%20Layer%20Normalization%20683d66e7db994beda71b25499d026b48/Untitled%204.png)

![Untitled](Batch%20and%20Layer%20Normalization%20683d66e7db994beda71b25499d026b48/Untitled%205.png)

This notation is confusing because feature ${x_i}$ means different things in the two contexts.

On the left side, feature ${x_i}$ goes from i=1 to B. This feature ${x_i}$ actually doesn’t refer to features 1 to d=4, but say JUST FEATURE 1 in samples i=1 to B=3, or JUST FEATURE 2 in those samples, etc. So we take the mean and SD of feature 1 in samples 1 to 3, then standardize each feature 1 in each sample by them.

---

[https://www.youtube.com/watch?v=bOYE6E8JrtU&list=PL7m7hLIqA0hoIUPhC26ASCVs_VrqcDpAz&index=1&ab_channel=NeelNanda](https://www.youtube.com/watch?v=bOYE6E8JrtU&list=PL7m7hLIqA0hoIUPhC26ASCVs_VrqcDpAz&index=1&ab_channel=NeelNanda)

54m: One mental picture is if you're in 3D or 2D, this is like taking the unit sphere or the unit circle, taking the direction for y and then projecting it onto a circle with radius root n. In high dimensions, you're just projecting onto some fixed hypersphere whose radius is root n. 

57m: Layernorm weights can be “folded” into the next layer: in the iterative equation, substitute the term of the previous layer with the previous layer equation containing its weights (?)

---

[https://dynalist.io/d/n2ZWtnoYHrU1s4vnFSAQ519J#z=pndoEIqJ6GPvC1yENQkEfZYR](https://dynalist.io/d/n2ZWtnoYHrU1s4vnFSAQ519J#z=pndoEIqJ6GPvC1yENQkEfZYR)

- Somewhat analogous to **[BatchNorm](https://www.wikipedia.org/en/Batch_normalization)**, but it doesn’t need any averaging over the batch
- Intuitively, it makes residual stream vectors *consistent* - mapping them to the same size and range, in a way that makes things more stable for the layer using them
    - But in practice, people use it because it works, and this kind of intuition can easily be wrong