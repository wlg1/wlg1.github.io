# SAE

[Code resources](SAE%206b08b4ad57a342bf9393d2ef0fa31c6b/Code%20resources%20c04b28c4a93b4c55a70ae537b64db59c.md)

[Training tips](SAE%206b08b4ad57a342bf9393d2ef0fa31c6b/Training%20tips%2097054f2568c04b06910600e546c60b99.md)

[Training at scale](SAE%206b08b4ad57a342bf9393d2ef0fa31c6b/Training%20at%20scale%20dda12ef43b0e43d99c4cb630ea460461.md)

[Feature visualzier](SAE%206b08b4ad57a342bf9393d2ef0fa31c6b/Feature%20visualzier%2021c7e6bfa2c141539e7eaf5783a6a16a.md)

[SAEs on large models](SAE%206b08b4ad57a342bf9393d2ef0fa31c6b/SAEs%20on%20large%20models%204107692463a6493b8c7069a8c2910958.md)

[Frature stitching](SAE%206b08b4ad57a342bf9393d2ef0fa31c6b/Frature%20stitching%20c1226c65e7e7425f8c586bdd830fbb5a.md)

---

SAE training skills to learn

- training setup
    
    [https://chatgpt.com/c/13a18e63-11ed-4401-aeec-020c7ee6d8eb](https://chatgpt.com/c/13a18e63-11ed-4401-aeec-020c7ee6d8eb)
    
    - loss
        1. **L0 :** average number of sparse dictionary features activated per token
            1. Want this to be low (monosemantic)
        2. **L0 / Loss Recovered Trade-Off:** we want low L0 but high loss recovered (recon)
            - is the reason why there's L0 / loss recovered tradeoff bc the actvs are closer to polysemantic so high L0 means more polysemantic, while making L0 lower means less closer to original polysemantic actvs but more monosemantic?
                
                Yes, the L0/loss recovery tradeoff is related to the polysemantic nature of activations. High L0 values suggest more polysemantic neurons, meaning each neuron responds to a wider range of inputs, which can recover more loss but may lead to more complex, less interpretable representations. Lowering L0 promotes more monosemantic neurons, making them respond to more specific inputs, enhancing interpretability but potentially reducing loss recovery efficiency.
                
                For more detailed information, you can refer to the original article [here](https://www.lesswrong.com/posts/fifPCos6ddsmJYahD/my-best-guess-at-the-important-tricks-for-training-1l-saes).
                
    - [https://www.lesswrong.com/posts/fifPCos6ddsmJYahD/my-best-guess-at-the-important-tricks-for-training-1l-saes](https://www.lesswrong.com/posts/fifPCos6ddsmJYahD/my-best-guess-at-the-important-tricks-for-training-1l-saes)
        1. SAE width: high
        2. Resampling
        3. (Not in Anthropic’s paper!) LR decrease and rewarmup at the start of training and after resampling: we start with 1/10 the normal learning rate and increase it to normal over 1000 steps. Immediately after resampling, we times the learning rate by 1/10 and again warmup.
        4. Learning Rate: low LR decreases the chances of killing neurons fast
        5. Shuffling (... not important?)
    - saelens params
    - dead features
    - shuffling and buffer
        
        
- metrics
    - pareto frontier
    - kurtosis (tailedness): shows the neuron basis is still privileged.
- types of saes
    - top k
    - gated saes
- wandb
- torrnodes
- multi gpu sharding

---

[https://www.notion.so/wlg1/Scene-2-SAE-math-draft-v1-bde8381733a941299abac40ea63587a1](https://www.notion.so/Scene-2-SAE-math-draft-v1-bde8381733a941299abac40ea63587a1?pvs=21)

Choosing better features is sort of like view selection.

---

[https://www.alignmentforum.org/posts/HpAr8k74mW4ivCvCu/progress-update-from-the-gdm-mech-interp-team-summary](https://www.alignmentforum.org/posts/HpAr8k74mW4ivCvCu/progress-update-from-the-gdm-mech-interp-team-summary)

---

[https://github.com/callummcdougall/sae_vis/tree/main](https://github.com/callummcdougall/sae_vis/tree/main)

---

[https://x.com/norabelrose/status/1810342367972495590](https://x.com/norabelrose/status/1810342367972495590)

llama-3: We are working on an automated pipeline to explain the SAE features, and will start training SAEs for the 70B model shortly.

https://discord.com/channels/1080558777608183829/1103144701458133062/1265055582012964956

Moe