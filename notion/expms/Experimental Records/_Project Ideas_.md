# _Project Ideas_

Interpret activations of interpolated images. How do activations change as you interpolate?

---

Teaching a model to edit other models in general by training it on activations to input output pairs

---

get issue-solns-genr of existing, then solve variations. combine them to solve new problem to innovate.

2 main genr: simple (if x, apply y) vs modified/mutated (if ~x, apply y+mods)

run parts of these ideas thru chat to get feedback crit

eg) ablate combos of abstractions based on Neuroscope
eg) project onto right singular vector
Eg) causal intervention on restoring combos

---

in-context give activations + circuit to GPT-4 to have it predict functionality of new activations + circuit (likely must do it on very narrow region with lots of in-context). if possible to some degree, this means it may be able to predict shared components too? -- likely not poss as GPT was not trained on this association, nor does it ever appear in the text datasets. instead of gpt-4, may train another meta-model for this

to search for circuits, have GPT-4 be given a task and guess several algorithms to carry that out. then, see if these algorithms can be matched to circuit structures found by ACDC

---

Superposition allows neurons to represent more features because a neuron isn’t dedicated to just one feature.

This is like view selection, where you store the most frequent subsets. But here, the subsets are “additive parts of a circuit”. 

But this is a continuous not discrete case. It’s about selecting the spaces in geometry that can represent the most with fewest neurons. So the manifold is low rank.

This is an optmization problem. Ask chatgpt for smaller steps. Ask for similar problems and how they were solved with what opt techn. Think about how to find small expms that support stms building up to this- Eg) geometry is not exact, but “relative” (in terms of ratios), thus analogous

Chatgpt:

A type of optimization problem is to find the most optimal subset of items that can compose into the most composite items, given tradeoffs. What are problems in linguistics analogous to this? Cite papers.

[https://chat.openai.com/c/86de87cc-c130-4f39-a712-4cc550158273](https://chat.openai.com/c/86de87cc-c130-4f39-a712-4cc550158273)

[https://www.ee.columbia.edu/~dpwe/e6820/papers/HuntB96-speechsynth.pdf](https://www.ee.columbia.edu/~dpwe/e6820/papers/HuntB96-speechsynth.pdf)

[https://en.wikipedia.org/wiki/Grammar_induction](https://en.wikipedia.org/wiki/Grammar_induction)

<<<

Look for common patterns in terms of ratios between vectors in similarly trained models. That is, the same toy model architecture, but trained multiple times. Write small parts of this using chatgpt. Breakdown:

1) Toy model 

2) 

---

Circuit Discovery

- Verb movers
- Re-discover IOI w/ similar IOI examples

MLP

- congruence on just mlp (mnist). features insteaed of tokens

Circuit Mapping

- Map GPT-2 small to small-modified? To medium?
- graph matching algos: filter based on local conds, then piece together global and check for continued consistency ('until the analogy breaks down')
local edge: inh head to mover head. if missing, circuit not present.
- find name movers in small and large, and compare circuits

Generate Data using chatGPT

- Find a way to automate generating many patterns and running them all at once, seeing which yield significant results. Brainstorming patterns requires chatgpt to self reflect after testing them.

---

[https://colab.research.google.com/drive/1nD6tfM33StbAqXG5HnYPlC40hKSj8mzD#scrollTo=AXZEGMLmIAih](https://colab.research.google.com/drive/1nD6tfM33StbAqXG5HnYPlC40hKSj8mzD#scrollTo=AXZEGMLmIAih)

The above suggests that it would be a useful bit of infrastructure to have a "wiki" for the heads of a model, giving their scores according to some metrics re head functions, like the ones we've seen here. HookedTransformer makes this Hooked to make, as just changing the name input to `HookedTransformer.from_pretrained` gives a different model but in the same architecture, so the same code should work. If you want to make this, I'd love to see it!

As a proof of concept, [I made a mosaic of all induction heads across the 40 models then in HookedTransformer](https://www.neelnanda.io/mosaic).

---

Collective of agents working on any rsch peoblem, say circuits. Come up with prompts. Generalize techn from other papers

If components all matter and it's like a symbolic code of what value is at each pos, then we can use code breaking. Eg. Mlp1 2 and 3 all en ode for feature.

If queried and keys act as lookup, then how do they relate to one another?

if a component actv for 2 very diff types of tokens (eg. names and numbers), what’s the cosine sim between names and numbers? what about along certain feature vecs?

---

Neuron search just correlated groups. Coarse to fine, like bisection. Correlated groups by pca, what neurons link to one another, clusters

---

Do vision models recognize eigenfaces? To what degree?

---

Find ground features of features automated until down to base

Get associated concepts by model output to abstract property questions

Patch TDA

---

Instead of looking at edges use a graph similarity metric for circuit edges

Use this metric to train a nn to be like another

Analogy mapping loss

Circuit loss

---

Features should have relation, distance, that is similar to one another. Relation between features, not just decompose activations

These relations are also features in order for nn to recognize

Path patching on features

Non interp features 

Weights and inputs should have relation to one another. Should similar weights and similar inputs activate high?

Instead of incorr logit, have corr token target have big enough diff from second ranked logit. Or kl divergence