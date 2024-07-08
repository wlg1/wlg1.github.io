# Sim of NN revisted

- hinton sim of NN reprs: [https://arxiv.org/pdf/1905.00414](https://arxiv.org/pdf/1905.00414)
    - CCA is sensitive to perturbation when the condition number of X or Y is large. To improve robustness, singular vector CCA (SVCCA) performs CCA on truncated singular value decompositions of X and Y. For feature spaces X and Y, does it make sense to do SAE (sparse autoencoder feature) CCA?
        
        [https://chatgpt.com/c/fbe5c434-b522-4fa0-86ce-c881a00f6164](https://chatgpt.com/c/fbe5c434-b522-4fa0-86ce-c881a00f6164)
        
        Yes, it does make sense to do SAE (Sparse Autoencoder) CCA. Here’s a detailed reasoning why:
        
        ### Canonical Correlation Analysis (CCA) Overview
        
        Canonical Correlation Analysis (CCA) aims to find linear projections of two sets of variables, \(X\) and \(Y\), such that the correlation between the projected variables is maximized. The performance of CCA can degrade when the condition number of \(X\) or \(Y\) is large, indicating multicollinearity or redundancy in the features.
        
        ### Challenges with High Condition Numbers
        
        High condition numbers imply that the data matrices \(X\) and \(Y\) are nearly singular, leading to numerical instability in the CCA computation. This can be due to:
        
        - Highly correlated features (multicollinearity).
        - Redundant or irrelevant features.
        - Noise in the data.
        
        ### Singular Vector CCA (SVCCA)
        
        SVCCA addresses these issues by performing CCA on the truncated singular value decompositions (SVD) of \(X\) and \(Y\). This truncation reduces noise and removes redundant or less significant features, thus improving numerical stability and robustness.
        
        ### Sparse Autoencoder (SAE)
        
        A Sparse Autoencoder (SAE) is a type of neural network that learns a compressed, sparse representation of the input data. The sparsity constraint ensures that only a small number of neurons are activated, promoting feature selection and reducing redundancy.
        
        ### SAE CCA
        
        SAE CCA would involve:
        
        1. **Learning Sparse Representations:** Train SAEs on \(X\) and \(Y\) separately to learn sparse representations \(X_{\text{SAE}}\) and \(Y_{\text{SAE}}\).
        2. **Performing CCA on Sparse Features:** Apply CCA on \(X_{\text{SAE}}\) and \(Y_{\text{SAE}}\) to find the linear projections that maximize correlation.
        
        ### Benefits of SAE CCA
        
        1. **Feature Selection:** The sparse representations help in selecting the most relevant features, reducing the risk of multicollinearity.
        2. **Noise Reduction:** By focusing on the most important features, SAEs can help in reducing the impact of noise in the data.
        3. **Dimensionality Reduction:** SAEs often reduce the dimensionality of the input data, leading to more stable and efficient CCA computations.
        4. **Improved Interpretability:** Sparse representations are often more interpretable, providing insights into the underlying structure of the data.
        
        ### Practical Considerations
        
        - **Training SAEs:** The quality of the learned sparse representations depends on the architecture and training of the autoencoders. Proper tuning of the sparsity parameter and the network structure is crucial.
        - **Computational Complexity:** Training SAEs and then performing CCA can be computationally intensive. Efficient implementations and hardware acceleration (e.g., using GPUs) can help mitigate this.
        
        ### Conclusion
        
        In summary, applying SAE CCA can improve the robustness and interpretability of CCA by leveraging sparse representations that mitigate the effects of multicollinearity, redundancy, and noise. It’s a sensible approach when dealing with high-dimensional and noisy data.
        
    - neuron matching: existing work
        
        Other work has studied alignment between individual neurons, rather than alignment between subspaces. 
        
        Li et al. (2015) examined correlation between the neurons in different neural networks, and
        attempt to find a bipartite match or semi-match that maximizes the sum of the correlations between the neurons, and
        then to measure the average correlations. Wang et al. (2018)
        proposed to search for subsets of neurons X˜ ⊂ X and
        Y˜ ⊂ Y such that, to within some tolerance, every neuron
        in X˜ can be represented by a linear combination of neurons from Y˜ and vice versa. 
        
        They found that the maximum
        matching subsets are very small for intermediate layers.
        
    - mutual information
        
        In the context of
        comparing representations, we believe mutual information
        is not useful
        
    - CKA on diffrent CNN layers
        
        . CKA reveals consistent relationships between layers of
        CNNs trained with different random initializations
        
        Figure 5. Linear CKA between layers of networks with different
        architectures on the CIFAR-10 test set.
        
    - cited by
        
        [https://arxiv.org/pdf/2111.11165](https://arxiv.org/pdf/2111.11165)
        
        Revisit Similarity of Neural Network Representations
        From Graph Perspective