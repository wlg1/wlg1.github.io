# Superposition vs Distributed rep

[**Toy Models of Superposition**](https://www.notion.so/Toy-Models-of-Superposition-9538794a63a541ebbd6aa19b19195839?pvs=21) 

[https://docs.google.com/document/d/1mdb-K6d4NZ0089nkPHfMWzHl8dqq_UtCa5pPIPg3eFA/edit](https://docs.google.com/document/d/1mdb-K6d4NZ0089nkPHfMWzHl8dqq_UtCa5pPIPg3eFA/edit)

Refs:

- Toy models
- Superposition, memorization
- Neurons in a haystack
- [https://arena-ch1-transformers.streamlit.app/[1.7]_Toy_Models_of_Superposition](https://arena-ch1-transformers.streamlit.app/%5B1.7%5D_Toy_Models_of_Superposition)
- [https://dynalist.io/d/n2ZWtnoYHrU1s4vnFSAQ519J#z=3br1psLRIjQCOv2T4RN3V6F2&q=feature](https://dynalist.io/d/n2ZWtnoYHrU1s4vnFSAQ519J#z=3br1psLRIjQCOv2T4RN3V6F2&q=feature)
- [https://dynalist.io/d/n2ZWtnoYHrU1s4vnFSAQ519J#z=EuO4CLwSIzX7AEZA1ZOsnwwF](https://dynalist.io/d/n2ZWtnoYHrU1s4vnFSAQ519J#z=EuO4CLwSIzX7AEZA1ZOsnwwF)

Subsections:

- Intro
    - Give fun, real world examples from the start. Pose a problem. Mention how this affects AI safety (mix up, side effects, “disorders” and misinterpretations about what we want)
    - dreams. this loose analogy
- Difference between polysemanticity, superposition, and distributed representations? (Neurons in haystack, A.3)
- 2D matrix mutlp in 1 visual diagram
- svd, cov WW, eig, entan

To do: (use in-line pothole links for citing)

- Main points: 1) Clarify terminology, 2) Explain its importance for AI existential safety, 3) Explain how to measure it
- Features as directions (quick figure)
- Difference between polysemanticity, superposition, interference / orthogonality, linear combination, and distributed representations (Neurons in haystack, A.3) [put this in a diagram showing simple, main differences of each]
- Importance (lower loss), sparsity.
- Explain how to measure superposition using W^T W with Basic Results diagram: measure the sum of a row of W^T W to find the direction of a feature in relation to other features. This is 0 (black, orthogonal to all) if no interference, and 1 (yellow). The more interference, the more superposition?
    - W^T W is a central concept that many measurements use
- Explain, in simple terms, features by features matrix W^T W (correlations; show input dot input matrix diagram?)
- L ~= benefit + interference : (trade-off)
- Froebenius norm measures number of features a model has learned
- Dimensionality D equation(also uses W dot W)
- Antipodal to more geometric structures
- Linear vs nonlinear case
- For now, explain up to and including sec 4 (geometry)
- list of open questions

Avoid meandering; give motivating questions and direct answers

Describe most of the visuals in words, too.

Only focus up to sec 4; skim the rest to see how they conn together. Note “In the future sections that will be written, we will focus on sections X from the paper, and go over the following “sequel” papers”.

---

Intro:

Motivation (relation to AI Existential Safety)

[https://en.wikipedia.org/wiki/Existential_risk_from_artificial_general_intelligence](https://en.wikipedia.org/wiki/Existential_risk_from_artificial_general_intelligence)

Future harm. See sec “strategic pos”: solve superposition

Fascinating geometric structures. Who knew these things would be hidden?

<<<

So why is W^T W features by features?

<<<

These features are presumably sparse, meaning we can pack them together as say antipodal pairs, since one often activates without needing the other.

Example of sparsity: python vs romance. But use your OWN example of any 2 unrelated things.

<<<
Caveats: these may be idiosynchratic to the toy model being studied