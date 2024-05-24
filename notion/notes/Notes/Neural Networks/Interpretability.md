# Interpretability

[List of Circuits](Interpretability%20f36507ee13ac4e3996063b9939b8d062/List%20of%20Circuits%205d420f64bdbf45bb9312c576225c701b.md)

Useful techniques:

- convert weights to be usable by library
- hooks
- parallel processing

---

Lottery Ticket Hypothesis

[https://www.lesswrong.com/posts/Z7R6jFjce3J2Ryj44/exploring-the-lottery-ticket-hypothesis](https://www.lesswrong.com/posts/Z7R6jFjce3J2Ryj44/exploring-the-lottery-ticket-hypothesis)

> A randomly-initialized, dense neural network contains a subnetwork that is initialized such that—when trained in isolation—it can match the test accuracy of the original network after training for at most the same number of iterations. The authors call such subnetworks "**winning lottery tickets**".
> 

---

[https://transformer-circuits.pub/2022/mech-interp-essay/index.html](https://transformer-circuits.pub/2022/mech-interp-essay/index.html)

[*privileged basis](https://transformer-circuits.pub/2021/framework/index.html#def-privileged-basis): Just as a CPU having operations that act on bytes encourages information to be grouped in bytes rather than randomly scattered over memory, activation functions often encourage features to be aligned with a neuron, rather than correspond to a random linear combination of neurons*

---

[https://www.alignmentforum.org/s/yivyHaCAmMJ3CqSyj/p/o6ptPu7arZrqRCxyz](https://www.alignmentforum.org/s/yivyHaCAmMJ3CqSyj/p/o6ptPu7arZrqRCxyz)

[**200 COP in MI: Exploring Polysemanticity and Superposition**](https://www.alignmentforum.org/posts/o6ptPu7arZrqRCxyz/200-cop-in-mi-exploring-polysemanticity-and-superposition)

Superposition is when a network represents more features than it has dimensions, and squashes them all into a lower dimensional space

- In neural networks interpretability, what's the difference between polysemanticity and superposition?
    1. **Polysemanticity**: This refers to the phenomenon where a single unit, neuron, or feature in a model can have multiple distinct meanings or represent several different concepts. For example, in a convolutional neural network trained for image recognition, a neuron might activate both for the presence of a circular object in the image and also for a specific color. This is an issue for interpretability because it can make it challenging to succinctly describe what a particular unit or feature in a model is "looking for" or "representing".
    2. **Superposition**: This refers to the phenomenon where multiple units, neurons, or features collectively represent a single concept. It is as if the concept is "spread out" over these units. It can make it difficult to identify the relationships between features and outcomes within the model. 

Polysemanticity: A neuron represents multiple features

Superposition: A feature is represented by multiple neurons

---

MLST interview:

neel MLST interview (1h59m): if you take vec all 1s of 100elms and flip 1st 1 to 0, it's not orth, dot prod is 0.98
(2h10m): correlated features seem to be made orthogonal during training

---

[https://www.youtube.com/watch?v=dCkQQYwPxdM&t=2039s&ab_channel=NeelNanda](https://www.youtube.com/watch?v=dCkQQYwPxdM&t=2039s&ab_channel=NeelNanda)

**A Walkthrough of In-Context Learning and Induction Heads Part 1 of 2 (w/ Charles Frye)**

17m20s: models go through a lot of small phase transitions (eg. suddenly can play chess well), showing up as bumps in loss curves

scaling laws: as train bigger models, loss smoothly changes. may be b/c many small phase transitions adding up, so avg to smooth in limit

20m: model recs aspirin for respiratory b/c you get more care in general when you’re more messed up, even if aspirin doesn’t do anything for the disease (?)