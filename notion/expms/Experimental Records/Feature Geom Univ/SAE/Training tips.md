# Training tips

[https://transformer-circuits.pub/2023/monosemantic-features#comment-nanda](https://transformer-circuits.pub/2023/monosemantic-features#comment-nanda)

- [https://www.lesswrong.com/posts/fKuugaxt2XLTkASkk/open-source-replication-and-commentary-on-anthropic-s](https://www.lesswrong.com/posts/fKuugaxt2XLTkASkk/open-source-replication-and-commentary-on-anthropic-s)
    
    [https://chatgpt.com/c/48ef673a-b632-479d-b491-0a0548ef196c](https://chatgpt.com/c/48ef673a-b632-479d-b491-0a0548ef196c)
    
    - sparse in neuron basis
    - ultra-low frequency cluster
    - kurtosis to measure privileged basis
        
        The statement is about understanding how special or "privileged" a particular set of neurons is in representing information. Here’s a simpler explanation:
        
        1. **Privileged Neuron Basis**: Think of neurons as specific ways to interpret information. A "privileged" set of neurons means they are particularly good or efficient at capturing certain features.
        2. **Kurtosis**: This is a statistical measure of how "peaked" a distribution is. For a normal (bell curve) distribution, the kurtosis is zero.
        3. **Detecting Neuron-Sparse Features**: If certain features are represented by very few neurons (neuron-sparse), it can be unusual or noteworthy.
        4. **Rotation to Normal Distribution**: If you rotate the data (think of changing your perspective), the data tends to look like a normal distribution. This means the special structure seen in the neurons is unique and not just due to random chance.
        
        By looking at how the kurtosis changes, we can detect when a set of neurons is especially good at capturing particular features, indicating a "privileged" basis.
        
        No, the kurtosis is not zero when using a privileged neuron basis. Here’s why:
        
        - **Normal Distribution**: In a normal distribution (bell curve), the kurtosis is zero. This means the data has a specific spread and peak.
        - **Privileged Basis**: When neurons are particularly good at capturing specific features, this distribution becomes "peaked" or has outliers, leading to higher kurtosis.
        - **Arbitrary Rotation**: Rotating data randomly tends to spread it out normally, reducing the specialized structure and bringing kurtosis closer to zero.
        
        Thus, privileged neuron bases often show non-zero kurtosis due to their specialized nature.
        

https://docs.google.com/document/u/0/d/1lHvRXJsbi41bNGZ_znGN7DmlLXITXyWyISan7Qx2y6s/mobilebasic#heading=h.j9b3g3x1o1z4

---

[https://transformer-circuits.pub/2023/monosemantic-features#:~:text=To create the dataset for autoencoder training](https://transformer-circuits.pub/2023/monosemantic-features#:~:text=To%20create%20the%20dataset%20for%20autoencoder%20training)

---

saelens uses buffer to shuffle activations. in advance would be huge

[https://github.com/jbloomAus/SAELens/releases/tag/v3.9.0](https://github.com/jbloomAus/SAELens/releases/tag/v3.9.0)

top k

---

[JBloom May SAE workshop](Training%20tips%2097054f2568c04b06910600e546c60b99/JBloom%20May%20SAE%20workshop%20fe2e004ec02742a88a0c5a6ec61d7415.md)

saes: # train steps, params, gpus (make list)
<https://transformer-circuits.pub/2024/april-update/index.html#training-saes>
<https://chatgpt.com/c/7dc14ed2-d932-456a-99ed-2314ba373a37>
    l1 for sparse, l2 for reconstuction

![Untitled](Training%20tips%2097054f2568c04b06910600e546c60b99/Untitled.png)

[https://venturebeat.com/ai/deepmind-makes-big-jump-toward-interpreting-llms-with-sparse-autoencoders/](https://venturebeat.com/ai/deepmind-makes-big-jump-toward-interpreting-llms-with-sparse-autoencoders/)