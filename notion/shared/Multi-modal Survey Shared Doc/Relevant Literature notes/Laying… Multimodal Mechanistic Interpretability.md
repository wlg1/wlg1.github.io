# Laying… Multimodal Mechanistic Interpretability

Brief ViT Overview

![Untitled](Laying%E2%80%A6%20Multimodal%20Mechanistic%20Interpretability%20722babdc87f34ea4a04e9eb755055e10/Untitled.png)

1. These patches are flattened and linearly projected to embeddings via a Conv2D layer, akin to word embeddings in language models. 
2.  A learnable class token (CLS token) is prepended at the start of the sequence, which accrues global information throughout the network. A linear position embedding is added to the patches.
3. The patch embeddings then pass through the transformer blocks. Output added to residual stream.
4. The final layer of this vision transformer is a classification head with 1000 logit values for ImageNet's 1000 classes. The CLS token is fed into the final layer for 1000-way classification. 

**Emoji Logit Lens** 

- We treat every patch like the CLS token, and feed it into the ViT’s 1000-way classification head → Like “unembedding” that patch
- we represent the ImageNet prediction of that patch with its corresponding emoji
    
    ![Untitled](Laying%E2%80%A6%20Multimodal%20Mechanistic%20Interpretability%20722babdc87f34ea4a04e9eb755055e10/Untitled%201.png)
    

Interesting findings:

- This is *not* an obvious result, as vision transformers are optimized to predict a single class with the CLS token, and not segment the image.
- visualize the evolving per-patch predictions for the above cat/toilet image for all the layers at once
    
    Each row is a patch, so focus on a row and read this from left to right. 
    
    ![Untitled](Laying%E2%80%A6%20Multimodal%20Mechanistic%20Interpretability%20722babdc87f34ea4a04e9eb755055e10/Untitled%202.png)
    

**Activation Patching**

**The Cat-Dog Switch**

- found a single attention head (Layer 11, Head 4) wherein patching the CLS token of the z-matrix flips the computation from tabby cat to Border Collie.