# Brainstorm- related behavior

AIM: Find what features are entangled with behavior

1. Get activations of Machiavelli and CAA data, both input + steering differences 
2. SVD and SAE to find features. Other features include:
    1. polytopes
    2. repr eng “population level”
3. Ablate/Patch features to behavior
    
    Was it done here? [https://transformer-circuits.pub/2023/monosemantic-features](https://transformer-circuits.pub/2023/monosemantic-features)
    
    Was it done in Successor Heads?
    
    YES- see section 3.1, for feature ablation
    
4. Measure disentanglement and Ripple Effects between features
5. Take all these together to find how features and behavior interact in a circuit
6. Compare FT vs Editing on features in circuit for behavior changes
    1. modify weights + steer activations
    

---

Questions

- Check the novelty. Do existing behavior/concept papers not talk about hierarchical concepts/related behavior? Look at what cites papers of this topic and their related work.
- Dataset: What kind of behavior inputs? How do we measure behavior? Machiavelli and Activation Steering and CCS
    - eg. Interpret Machiavelli inputs. has anyone done this before?
        - As of 3/20/24: no

- Question: in step 2 of path patching, how do we use the clean cache if the activations come from the new run? or do they come from the cache? if the former, why do we need the clean run in step 1?

---

RAVEL paper discusses how changing entangled attributes has ripple effects. Thus, it is almost certain that behavior editing is entangled with editing attributes. The second paper's ways to measure disentanglement can be built upon to measure the degree of which attributes are highly entangled with which behavior editings

Can editing be better at avoiding disentanglement than fine tuning? Certain areas may be better at avoiding disentanglement than others. Or, perhaps is unavoidable in some cases.

NOTE: hierarhical behavior doesn’t make sense, it’s hierarchical features. Now features and behavior can both have decompositions that are related to each other.

---

Poss ideas:

- Gradually change an input and look at activations.
    - eg) given a prompt, change one word at a time. Something measureable, like a concept.
        - Gradually change concept hierarchy
        - Gradually remove descriptions
        - Multiple choice is easier to measure b/c only changes one part of input
        - How close someone is, relationship-wise?
        - How big the reward is?
- For now, forget about hierarchical concepts w/ related behavior. Just focus on interpreting behavior. Steering did this on a high level, but not focused on features. So
- auto find features using conditions
- interpret “Large Language Models can Strategically Deceive” (not required to look at fine tuning). Use feature extraction, ablation, but not circuits.
- modify behaviors in terms of others behaviors
- hierarchical concepts may give rise to “multi-dim” circuits (simplicial complexes) with different granualarities of editing
- compare common vs sparse features (general to specific)
- focus on finding features  with high importance for behavior
- use your analogy interpretations of what eigenvalues are and why they’re impt to explain why new math constructs (such as attention mech) are impt based on describing them in terms of translating each math op to a description of what it does
    - Eg) “dot prod measures strength → eigenvalues have highest dot prod → thus eigenvalues have highest str → thus, eigenvalues of CORR MATRIX have highest CORR”
- The information you see is emergent from neuron activations, just like how the self is emergent from cells. The shape of data is emergent from neuron activations.
    
    Don’t just measure the individual neuron activations. YOU NEED TDA ON THE ACTIVATIONS!
    
    You need clustering on activations too. And differences of activations. THEN unembed these clusterings (how?). No; unembed all activations in a clustering group and compare them. We can transform multiple points via U matrix to vocab space.
    
    Edit the clusterings, not just individual activations or components. The clusterings of multiple output activation vectors and/or feature vectors are like polytopes.
    

[https://www.notion.so/wlg1/DMT-25b96f6c81854e6fa888f62535240e32](https://www.notion.so/DMT-25b96f6c81854e6fa888f62535240e32?pvs=21)

---

To write new paper:

Take existing research question (eg. paper topic vs background) and generalize this

eg. a benchmark

List of generalized new topics

- Survey
- Make a benchmark
- Adapt to new data TYPE (not just a new dataset; not novel enough)
- Adapt technique from other topics to this one
- Modify existing technique to fix issue it had
- Apply technique to new type of model
- Apply interpretability technique to new type of effect (eg. what is lora doing)