# Brainstorm- concept repr

[https://docs.google.com/document/d/1sCv-E4ZWz4-t5nN4quRJoGOCXQEW7cWUNbHEdWuX1kg/edit#heading=h.22oua7k11exi](https://docs.google.com/document/d/1sCv-E4ZWz4-t5nN4quRJoGOCXQEW7cWUNbHEdWuX1kg/edit#heading=h.22oua7k11exi)

OMahony_Disentangling_Neuron_Representations_With_Concept_Vectors_CVPRW_2023_paper:

> The work by Kim et al. on Concept Activation Vectors (CAVs) introduces a method for defining a concept as a vector pointing in the direction of activation values of a concept's examples. To identify a concept, they train a linear classifier to differentiate between concept examples and random counterexamples, with the concept vector identified as orthogonal to the decision boundary. However, a significant limitation is the necessity for a manually curated set of examples for each concept, which restricts the method's scalability and adaptability. Despite this, there has been a development of a small number of unsupervised methods aimed at concept discovery, indicating a growing research interest in finding ways to autonomously identify concepts in latent space.
> 

This is about features in MLPs or residual stream

Plan:

1. In at least 2 large models like Llama-2, create datasets (not too long to avoid mem issues) regarding cat vs lion, dog vs wolf, dog vs cat, etc. (animal classes)
2. Find the common activations and features (using SAEs) 

- kc subnetw
    
    This paper is highly related to studying analogous abstract concepts. The subnetworks for the relational triples they discover are building blocks for larger, more abstract relations that can be analogously mapped, so it's possible we can build on their work by discovering how these knowledge-critical subnetworks are related to one another and piece together into larger relations
    

Make modification to existing by changing one attribute of it:

eg) Instead of antonyms, apply the steering vector 

Exploratory tests to try model editing:

- Edit associations
    - Gather concepts that are “similar” to the abstract behavior
        - Similar on what component activations?
    - Does adding things about “money” change behavior on “greed”? Indirect changes to behavior based on other concepts, such as removing money.

Techniques

- Look at activations as a whole instead of causally ablating. Then from the activations, causally ablate.
- Algebraic topology: The overlaps (interactions) are joins. The 5D

---

Ways to identify abstract concepts in image classification models

- Group all animals into one. Then group all dogs vs cats into one.
    - Compare activation differences
    - Identify circuit differences
    

---

Ways to identify abstract concepts in text-to-image gen

- First, there is association from text to latent space. Then, decoder translates latent space vector to image space.

---

Ways to identify abstract concepts in LLMs

- This is about prediction, so use ICL prompts to predict the next class
- Need to use LLAMA-2 because GPT2 is terrible at concept prediction

---

Hypotheses on how abstract concepts are representated

- As vectors in latent space
    - They need some way to “analogously map”. Is this done by dot product of vectors?
- As sub-circuits
- As analogous mappings
    - Two features are considered “the same” only if their analogous mappings are the same
        - This is a more controversial topic so save it for a smaller paper, not editing

---

Universality Hypothesis

- The Wes Gurnee papers focus on monosemantic neurons, rather than features
- They mention analogous neurons, but don’t discuss analogous mappings

---

Subjectivity of Good/Bad

- A model fine-tuned on animals as bad vs as good
    - Get help from people who worked with fine-tuning
- A model on animals as bad vs a model on weapons as bad
    - Is the concept of ‘bad’ universal across models?