# How to measure feature similarity

We need aggregative sim measures that work for multiple models, not just 2 models

[https://medium.com/@pozdrawiamzuzanna/canonical-correlation-analysis-simple-explanation-and-python-example-a5b8e97648d2](https://medium.com/@pozdrawiamzuzanna/canonical-correlation-analysis-simple-explanation-and-python-example-a5b8e97648d2)

while PCA tries to find the linear combination of variables that maximizes variance in the dataset, CCA will try to find a linear combination of variables in both datasets that have the strongest correlation between each other.

1. Activation similarity
2. Output similarity
3. Direction / Distance
4. Membership in higher-order structures

what percentage of features have an analogue

Map one feature to group of features

![Untitled](How%20to%20measure%20feature%20similarity%20e0ceaa1c575044078ccd6a4d4ec71c04/Untitled.png)

---

Input points in feature space. That way, can align them. Each input is a vector of feature.

Second is plotting features themselves. See woog clustering 

https://chatgpt.com/c/a85ddf24-0d3e-40b2-ad76-b5e2db5def04

Is it measuring similarity in some other space?

ways to measure feature relns:

1. cosine sim
2. causal patching
3. sim metrics across models
4. clustering
5. mapper, topo invariants (betti)
6. func eqv patching cross-models (nikhil, cat the)
7. jaccard (bau, gurnee)

https://youtu.be/zBnkO8p32w0?si=sDj_TTxkAYy5HdgY

**Implicit generative models using kernel similarity matching - Shubham Choudhary (Harvard)**

after sae transformation, we align two models by a cross-model sae. then, apply alignment-based measures

---

mutual nearest neighbors: 

ISSUE: the similarity metric REQUIRES a pair! How do we find this pair?

Too many exhaustive pairs is ridiculous. Instead of mapping two entire networks, we can map a smaller query with a larger network.