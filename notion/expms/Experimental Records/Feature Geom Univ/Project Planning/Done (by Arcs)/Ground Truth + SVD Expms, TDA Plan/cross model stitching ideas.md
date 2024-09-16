# cross model stitching ideas

[https://www.lesswrong.com/posts/baJyjpktzmcmRfosq/stitching-saes-of-different-sizes](https://www.lesswrong.com/posts/baJyjpktzmcmRfosq/stitching-saes-of-different-sizes)

It's interesting that the authors were able to add the individual feature reconstruction from one SAE to another. This makes sense given that they are the same reconstructed activations within the same model, so perhaps it’s similar to steering.

The post mentions activation correlation and cosine sim on weights had a high correlation, yielding similar results. Was this metric used for cross mod univ, or was this some sort of 'proxy metric' that's diff? If it's the same, then can cosine sim also be used for cross mod?

<<<

stitch safe features into unsafe models, or remove unsafe features

<<<

**draft:**

interesting frakenstein expm, see how well this works:

Can we find (steering) features that work across models? Perhaps there would be parts of a common, canonical “ground truth” space that SAEs are approximating across models, assuming models do this.

SAE design: I was thinking about training a new SAE that learns a common feature space that works for  reconstructions from two similar LLMs. The input and output would be a concatenation of batches of activation vectors from each model. The loss function add both L2 reconstruction losses. No; it just uses one L2 loss. TopK can be higher, perhaps double the K used for one model.

Expm analysis: Record which features seem to be mostly/only for model 1, which seem to be for model 2, and which were used for both. To find this, take dataset examples into both models and put them through the SAE. Then, try adding features that are common to both models as a 'supplement', like the steering vecs.

ISSUES: the SAE is trained to always expect activations from both models, so if it’s missing activations from another model, would it be able to use the “common features”? No; it’s not expecting activations from both models, it’s treating them the same.

ANOTHER ISSUE: would the model have to recognize which sample belongs to which SAE? or perhaps not. Don’t think we can append some “flag variables” onto the input as it’s not supervised. 

ISSUE: I expect the performance to be “pulled at both ends” and that they’d be 2 largely separate clusters of features unique for each LLM, but maybe it could find features that work for both.  However, the two activations come from different distributions. Would be very hard.

Which LLMs? : I’d start with similar LLMs (eg. MLP0 in tinystories 1L vs 2L). For different LLMs, I think it’s hard to compare the middle layers; early and later layers may have more similar. But SAEs are really only trained on middle layers, so perhaps don’t do this for now. If we do, perhaps try padding the input of the smaller model. Note that gpt-2 med and tinystories gpt both share modelDims of 1024 so not needed for those cases. Perhaps try comparing SAEs for every tinystories 1L trained paired with every GPT-2 medium layer.

[https://chatgpt.com/c/739f592f-acc4-4a94-8b06-fd1272f60513](https://chatgpt.com/c/739f592f-acc4-4a94-8b06-fd1272f60513)

<<<

**draft v2:**

<<<

- msg to Jbloom
    
    It's interesting that the authors were able to add the individual feature reconstruction from one SAE to another. This makes sense given that they are the same reconstructed activations within the same model, so perhaps it’s similar to steering.
    
    After reading that more, I just had an idea (just for curiosity, prob not impactful research-wise)