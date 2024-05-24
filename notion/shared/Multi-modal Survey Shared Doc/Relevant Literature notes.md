# Relevant Literature notes

- Template
    - Nishant notes
    - Mike notes

---

Multimodal Interp

- [Laying the Foundations for Vision and Multimodal Mechanistic Interpretability & Open Problems](https://www.lesswrong.com/posts/kobJymvvcvhbjWFKe/laying-the-foundations-for-vision-and-multimodal-mechanistic)
    
    [[**Laying… Multimodal Mechanistic Interpretability**](https://www.lesswrong.com/posts/kobJymvvcvhbjWFKe/laying-the-foundations-for-vision-and-multimodal-mechanistic)](Relevant%20Literature%20notes%20edd0d02b848247439a41f9deb4c4d58e/Laying%E2%80%A6%20Multimodal%20Mechanistic%20Interpretability%20722babdc87f34ea4a04e9eb755055e10.md)
    
    - Nishant notes
        - Prisma is for mech interp. in multimodal community
        - “patch-level logit lens on the image basically acts as a segmentation map”
            - *not* an obvious result, as vision transformers are optimized to predict a single class with the CLS token, and not segment the image
            - emergent property
        - bias, possibly due to a limited 1000-class vocabulary
        - visualize how patch-level predictions evolve across the depth of the model
        - attention heads’ scores specializing for specific patterns in the data, including what we call a Corner Head, an Edges Head, and a Modulus Head.
        - knowledge of head-specific roles in CLIP can be used to manually intervene in the model's computation
        - difference from language
            - ViTs use bidirectional attention and predict a global CLS token, rather than predicting the next token in an autoregressive manner.
            - ViT does not have the same concept of “time” as language transformers, and some of the original language mechanistic interpretability techniques break.
            - a yellow patch on a goldfinch might represent "yellow," "wing," "goldfinch," "bird," or "animal," depending on the granularity, showing hierarchical ambiguity.
    - Mike notes
        - Prisma is a multimodal mechanistic interpretability library based on TransformerLens, currently supporting vanilla vision transformers (ViTs) and their vision-text counterparts CLIP.
        - Adapting TransformerLens, we designed HookedViT to easily capture intermediate activations with custom hook functions, instead of dealing with PyTorch's normal hook functionality.
        - **Emoji Logit lens, attn viz, patching**
        - Diffusion models are the next obvious frontier, but there will be a larger conceptual leap in designing mechanistic interpretability techniques, largely due to their iterative denoising process.
        - The notebook has a section that switches a ViT’s prediction from tabby cat to Border Collie with a minimum ablation.
        
        List of interp papers (only ~20; can be made more comprehensive in survey):
        
        [https://soniajoseph.github.io/machine%20learning/vision%20transformers/vit-papers/](https://soniajoseph.github.io/machine%20learning/vision%20transformers/vit-papers/)
        
- [INTERPRETING CLIP’S IMAGE REPRESENTATION VIA TEXT-BASED DECOMPOSITION](https://arxiv.org/pdf/2310.05916.pdf)
    - Notes A
    - Notes B
        
        (from Laying the…)
        
        - found that decomposing CLIP's image representation across spatial locations allowed obtaining zero-shot semantic segmentation masks that outperformed prior methods.
        - identified property-specific attention heads in CLIP that specialize in concepts like colors, locations, and shapes.
        - showed that knowledge of head-specific roles in CLIP can be used to manually intervene in the model's computation, such as removing heads associated with spurious cues.
        
        ---
        
        - We decompose the image representation as a sum across individual image patches, model layers, and attention heads, and use CLIP’s text representation to interpret the summands
        - Interpreting the attention heads, we characterize each head’s role by **automatically finding text representations that span its output space**
        - remove spurious features from CLIP and to create a strong zero-shot image segmenter.
- [INTERPRETING CLIP WITH SPARSE LINEAR CONCEPT EMBEDDINGS (SpLiCE )](https://arxiv.org/pdf/2402.10376.pdf)
    - Notes A
        - Does not require concept labels, applied post-hoc
        - Outputs to this are able to replace CLIP representations
        - Closely related to the **linear representation hypothesis**.
        - Key idea of paper:
            - CLIP image embeddings can be represented by a linear combination of text embeddings
            - Given a concept dictionary, learn the “mixture” w, such that you can recreate an image embedding. Image embedding is a linear combination of semantic concepts(?), SpLiCE is learning the combination
        - Didn’t understand: in the “learned vocabulary” experiments, how exactly did they pick the 10k semantic concepts. They mention using FISTA.
        - Side note: reminds me of how people formulate k-means/pca/cca objective functions, is there any merit to this thought?
    - Notes B
        - we show that the information contained in CLIP embeddings can be approximated by a linear combination of simple semantic concepts, allowing us to interpret representations with sparse, nonnegative **dictionary learning**
        - We propose SpLiCE, a method to transform the dense, uninterpretable embeddings of CLIP into human-interpretable sparse concept decompositions
- [STAIR: Learning Sparse Text and Image Representation in Grounded Tokens](https://arxiv.org/pdf/2301.13081.pdf)
    - Notes A
        - Not a post-hoc approach, rather it changes the architecture to make things more interpretable, uses **token projection head** (their own thing)  ****in place of just pooling layer
            - Token projection head has mapping function + pooling
        - 3-stage training, alternative encoder training, then joint optimization
    - Notes B
        
        In contrast to dense embeddings of CLIP, looks for sparse embeddings by training a STAIR **dual-encoder model**. Claims sparse embedding is easier for humans to interpret.
        
- [Multimodal Neurons in Artificial Neural Networks](https://distill.pub/2021/multimodal-neurons/)
    - Notes A
        - “They also have real world implications: these models are vulnerable to a kind of “typographic attack” where adding adversarial text to images can cause them to be systematically misclassified.”
        - “These neurons don’t just select for a single object. They also fire (more weakly) for associated stimuli, such as a Barack Obama neuron firing for Michelle Obama or a morning neuron firing for images of breakfast.”
        - “person neurons can be thought of as a landscape of person-associations, with the person themself as simply the tallest peak.”
        - This paper talks about person, emotion, region neurons. It does not really talk about them in the context of WHERE they are in the model. I want to know where the concept lies with respect to the architecture, and whether that is affected by how abstract that concept is
            - “We arrive at a surprising discovery: it seems as though the neurons appear to arrange themselves into a taxonomy of classes that appear to mimic, very approximately, the imagenet hierarchy.”
            - “The fact that these neurons naturally form a hierarchy — form a hierarchy without even being trained on ImageNet — suggests that such hierarchy may be a universal feature of learning systems”
        - “However, we were unable to find any examples of the model mapping words in non-Latin script to semantic meanings. It can recognize many scripts (Arabic, Chinese, Japanese, etc) and will activate the corresponding regional neurons, but doesn’t seem to be able to map words in those scripts to their meanings”
    - Notes B
        
        CLIP vision model neurons: Conditional Probability Plots and **Feature Visualization**
        
- [Rosetta Neurons: Mining the Common Units in a Model Zoo](https://arxiv.org/abs/2306.09346)
    - Notes A
    - Notes B
- [Concept-Monitor: Understanding DNN training through individual neurons](https://arxiv.org/pdf/2304.13346.pdf)
    - Notes A
    - Notes B
- [CLIP-Dissect: Automatic Description of Neuron Representations in Deep Vision Networks](https://arxiv.org/abs/2204.10965)
    - Notes A
    - Notes B

Features

- [Interpreting Neural Networks through the Polytope Lens](https://arxiv.org/pdf/2211.12312.pdf)

Other Multimodal XAI

- [Formal Concept-based Analysis of Neural Networks via Vision-Language Models](https://www.andrew.cmu.edu/user/rmangal/papers/Concept_based_Verification_of_DNNs.pdf)
    - propose to leverage emerging multimodal, vision-language, foundation models (VLMs) as a lens through which we can reason about vision models
    - We describe a **logical specification language** Conspec designed to facilitate writing specifications in terms of these concepts
    

---

https://www.marktechpost.com/2024/04/24/researchers-at-mit-propose-maia-an-artificial-intelligence-system-that-uses-neural-network-models-to-automate-neural-model-understanding-tasks/