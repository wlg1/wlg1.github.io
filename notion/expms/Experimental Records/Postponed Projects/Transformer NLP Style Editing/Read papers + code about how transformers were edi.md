# Read papers + code about how transformers were edited

- MEMIT, ROME
- Fine-Tuning (FT), which applies Adam with early stopping at one layer to minimize -log P [o* | x]
- Constrained Fine-Tuning (FT+L) (Zhu et al., 2020) additionally imposes a
parameter-space L1 norm constraint on weight changes.
- Knowledge Editor (KE) (De Cao et al., 2021) hypernetwork
[https://github.com/nicola-decao/KnowledgeEditor](https://github.com/nicola-decao/KnowledgeEditor)
- MEND (Mitchell et al., 2021) learns auxiliary models to predict weight changes to G.

---

Read papers about how style editing was done

- Approx. StyleGAN directions using SVMs then edit directions
- Pullback metric then geodesic shooting
- Erasure Stable Diffusion