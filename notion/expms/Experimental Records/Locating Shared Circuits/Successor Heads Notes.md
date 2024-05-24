# Successor Heads Notes

![Untitled](Successor%20Heads%20Notes%203d2a9c73e41d4ca7903790b6e7914124/Untitled.png)

[https://chatgpt.com/c/e3511349-5a19-4862-8f0b-18ba33dbe477](https://chatgpt.com/c/e3511349-5a19-4862-8f0b-18ba33dbe477)

- is the decoding function a sae or probe
    
    A linear probe is a linear classifier or regressor that is trained on top of the fixed representations produced by a pre-trained neural network.
    
    The probes validate the linear maps by ensuring that the projections can be accurately decoded to the original tokens and their successors. Therefore, while the SAEs are crucial for identifying the features, the linear probes play a key role in the decoding process.
    

![Untitled](Successor%20Heads%20Notes%203d2a9c73e41d4ca7903790b6e7914124/Untitled%201.png)

- are these valid?
    
    The annotations in the diagram provide explanations for various components and transformations in the commutative diagram. Let's review and confirm if the annotations are correct based on the information provided and typical usage of such diagrams:
    
    1. **\(\mathcal{R}_N \times \mathcal{R}_D\) Space:**
        - Annotation: "each member of pair is in emb repr"
        - Explanation: This is correct. \(\mathcal{R}_N \times \mathcal{R}_D\) represents the space where each member of the pair (e.g., numeric and domain features) is in the embedding representation.
    2. **\(\pi_N \times \pi_D\):**
        - Annotation: "add this pair into the equation \(\pi_N + \pi_D = I\)"
        - Explanation: This is partially correct. \(\pi_N \times \pi_D\) refers to the linear maps projecting the embedding representations into numeric and domain spaces. The equation \(\pi_N + \pi_D = I\) ensures these projections cover the entire space without losing information.
    3. **\(\mathcal{I} \times \mathcal{I}\) Space:**
        - Annotation: "embedding representation of the pair into undecomposed emb repr for each token"
        - Explanation: Correct. This represents the embedding space for the combined (undecomposed) token representations.
    4. **Output-Space Decoding \(W_U \circ S\):**
        - Annotation: "to logit distribution (vocab space) after pass to successor head"
        - Explanation: Correct. This transformation maps the embeddings to logits (vocab space) after passing through the successor head.
    5. **\(\mathcal{N} \times \mathcal{D}\) Space:**
        - Annotation: "tokens not in emb repr, e.g., (2, letter)"
        - Explanation: This should clarify that \(\mathcal{N} \times \mathcal{D}\) represents the numeric and domain features as tokens, not their embeddings.
    6. **\(\langle \pi_1 \circ \pi_1, \pi_2 \circ \pi_2 \rangle\):**
        - Annotation: None
        - Explanation: This represents the combined projection ensuring the mapping is accurate and preserves the structure.
    
    Overall, the annotations appear to be mostly correct and provide a clear explanation of the diagram. A few minor clarifications could be made:
    
    - In the \(\mathcal{N} \times \mathcal{D}\) space annotation, specifying that these are numeric and domain tokens would be helpful.
    - In the \(\pi_N \times \pi_D\) annotation, it might be clearer to state that these are the learned projections ensuring the decomposition and recomposition of token representations.
    
    If you have any specific concerns or questions about the annotations, please let me know!
    

---

a) What are some more details of the learning algorithm+procedure used to train the index-space projection and domain-space projection in section 3.1 and Appendix L? eg) if it used SGD and Adam. Also why only 10 epochs? Interested in looking at this code if it is available.

b) Were the closeness metrics loss functions and the commutative diagram used to frame the training procedure based on any previous paper's work?