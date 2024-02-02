# Future work

Compare with mod circuits

---

For instance, the IOI circuit algorithm consists of the steps "copy subjects" then "inhibit repeated subjects". Another algorithm involving subjects may also "copy subjects" but instead, "boost repeated subjects". The sub-circuit involved in "copy subjects" is the same in both algorithms, implying that the model re-uses circuits for similar tasks. Our path patching experiments discover that the IOI circuit and the Repeated Subjects Circuit share several of the same sub-circuits.

We discover several shared sub-circuits among circuits for similar tasks. These include sub-circuits that predict tokens that share an abstract concept (eg. cat and lion are both "felines"), sub-circuits for continuing sequences (digits, number words, months), and sub-circuits involved in numerical calculations (greater-than, less-than).

---

### 2023

Circuit Embedding Similarity

- We utilize a novel embedding space method to measure the "similarity" between circuits that also identifies the functional similarity between their sub-circuits.

Model to model

- We search for universal circuit types by performing model-to-model circuit analysis comparisons. When we find a circuit of type X in model A, we analogously match its components with a circuit of type X in model B.

### 2024

Train from sub-circuits, transfer learning: *When they form, how they form, why they form?*

- We employ novel methods to study the conditions under which shared components form in models. We see that certain conditions, over others, encourage sub-circuit formation across similar tasks.
- We introduce a novel method to perform transfer learning using sub-circuits by extracting a sub-circuit of task A that is hypothesized to be shared by task B, and continue training the model on task B using the sub-circuit as pretrained weights.
- We introduce a novel method to transform the computation of task A into task B by replacing certain activations in task A with those from task B, while keeping their sub-circuits the same.

Sub-Circuit Search

- We introduce a novel method to discover new circuits for tasks given similar tasks. This method works by identifying the sub-circuit involved in both tasks, ignoring the sub-circuits not involved in the new task, and finding the rest of the new circuit by building it on top of the previous relevant sub-circuit. This method could potentially save time in circuit discovery by re-using matched sub-circuit pieces already shown to have important functionality. We utilize GPT-4 to help determine what is "semantically similar" between tasks. We also call our method to measure similarity between the circuits.
- to search for circuits, have GPT-4 or group of agents be given a task and guess several algorithms to carry that out. See if these algorithms can be matched to circuit structures found by ACDC

Analogous Concepts

- Formalize how to measure a model recognizing analogies internally. No fancy math yet; just set functions, calc, and linear algebra.
- Algtop patterns (play with them on stream), catg th collab

---

(these are very speculative and likely infeasible, but may be revised to become more feasible):

- in-context give activations + circuit to GPT-4 to have it predict functionality of new activations + circuit (likely must do it on very narrow region with lots of in-context). if possible to some degree, this means it may be able to predict shared components too? -- likely not poss as GPT was not trained on this association, nor does it ever appear in the text datasets. instead of gpt-4, may train another meta-model for this

Tasks being in the same circuit are like features being in the same polysemantic neurons?