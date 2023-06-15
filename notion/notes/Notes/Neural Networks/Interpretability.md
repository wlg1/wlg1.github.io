# Interpretability

[https://transformer-circuits.pub/2022/mech-interp-essay/index.html](https://transformer-circuits.pub/2022/mech-interp-essay/index.html)

*[privileged basis](https://transformer-circuits.pub/2021/framework/index.html#def-privileged-basis): Just as a CPU having operations that act on bytes encourages information to be grouped in bytes rather than randomly scattered over memory, activation functions often encourage features to be aligned with a neuron, rather than correspond to a random linear combination of neurons*

---

[https://www.alignmentforum.org/s/yivyHaCAmMJ3CqSyj/p/o6ptPu7arZrqRCxyz](https://www.alignmentforum.org/s/yivyHaCAmMJ3CqSyj/p/o6ptPu7arZrqRCxyz)

Superposition is when a network represents more features than it has dimensions, and squashes them all into a lower dimensional space

- In neural networks interpretability, what's the difference between polysemanticity and superposition?
    1. **Polysemanticity**: This refers to the phenomenon where a single unit, neuron, or feature in a model can have multiple distinct meanings or represent several different concepts. For example, in a convolutional neural network trained for image recognition, a neuron might activate both for the presence of a circular object in the image and also for a specific color. This is an issue for interpretability because it can make it challenging to succinctly describe what a particular unit or feature in a model is "looking for" or "representing".
    2. **Superposition**: This refers to the phenomenon where multiple units, neurons, or features collectively represent a single concept. It is as if the concept is "spread out" over these units. It can make it difficult to identify the relationships between features and outcomes within the model. 

Polysemanticity: A neuron represents multiple features

Superposition: A feature is represented by multiple neurons