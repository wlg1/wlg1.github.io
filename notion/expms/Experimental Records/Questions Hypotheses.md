# Questions/Hypotheses

- About
    
    Questions can be anything; hypothesis are questions formatted into a statement with a validity that can be weighed using tests
    
    Most hypotheses are accurately answered with a binary “reject or accept” test, so don’t have a column for that. The conclusion is usually more nuanced.
    
    This differs from Experimental Results because “Results” can contain findings that were not originally questions/hypotheses
    
    We wont’ be able to record every single question or hypothesis we have here. So try to clean it up so that only “important” questions are recorded here (the others can be semantially searched on the fly; not yet implemented)
    

## Questions

- Transformers:
    - If there are fewer features than neurons, will any neurons still be polysemanric? Is it optimal in anyway to be polysemantic in this case?
    - circuits may not work b/c EVERY node contributes A LITTLE to the final effect
    - does KEEPING some MLPs make it worse? b/c they're not intended to be part of circuit? we see how removing some nodes from the full circuit actually makes the model perform better than the full circuit- is this a coding error, or is it actually doing better without them?
    
    - The NN learns to predict tokens. Can it predict its own hidden states? That is, given a long series of hidden states it has, would it predict the “next” one? The output would be a matrix that represents a layer output.
    - Why do backup heads exist? What incentized the model to learn a redundancy, if it didn’t encounter the “danger” of ablation during training? Perhaps for some other purpose, or just a side effect with no purpose?
        
        [https://dynalist.io/d/n2ZWtnoYHrU1s4vnFSAQ519J#z=DrXks0N2hOOGRkET4jragbOv](https://dynalist.io/d/n2ZWtnoYHrU1s4vnFSAQ519J#z=DrXks0N2hOOGRkET4jragbOv)
        
    
    Focus on when generalizations work after ROME edit. 
    
    Notebook: [Check generalizations in ROME](Code%20Notebooks%20432b45bb746f43eabf4172f69d384f8a/Check%20generalizations%20in%20ROME%200f2a42c9096a4d5693d7f51ebc144f4b.md) 
    
    - Do members of abstract classes generalize, too?
        - If so, try to locate where abstract vs specific classes are. What's the common pattern between models?
    - ISSUE: after changing, hard to tell which of the (even just hundreds) of neurons change their activations because there is no set “threshold”
        - ATTEMPT: try difference thresholds. find what happens after removing those neurons that activate after those thresholds
            - if these neurons do change the class, is there a pattern to what they are between images? Between classes? Between models?
    - ISSUE: out of millions of weights, which combination of them to change? Too many combinations.
    - what decides what’s query vs what’s key? query is source sentence, key is target sentence. in decoder-only (gpt), they’re the same? then value can be used in either? no- if q=3, k=5, then v is always for 5, not 3. and if q=5, k=3, then v is always for 3, not 5 (?)

GPT-2-Small Circuits:

- Are there consistent patterns in inputs that allow us to identify which subject, among given subjects, the model will output? Motivated by tests from [test_prompt_most_recent_S.ipynb](Code%20Notebooks%20432b45bb746f43eabf4172f69d384f8a/test_prompt_most_recent_S%20ipynb%20a51ecffd653d4d6c995692f0920be200.md)
    - [HYPOTHESIS: It may be that the “default” would output earliest.](Questions%20Hypotheses%2087e989748e1942dfa05a7d90433f2e40.md)
- How does adding a duplicate name change from outputting “earliest subject” to “latest subject”?
    - HYPOTHESIS: ???

- MLP:
    - Do there exist neurons which fire for class A, but not class B?
        - [MNIST_1_vs_7.ipynb](Code%20Notebooks%20432b45bb746f43eabf4172f69d384f8a/MNIST_1_vs_7%20ipynb%20cd1482eb130b428681a298e72f020f76.md)
        - [XOR_weight_interpret.ipynb](Code%20Notebooks%20432b45bb746f43eabf4172f69d384f8a/XOR_weight_interpret%20ipynb%20bf8ac65466fe4eb9a255a26ec920bad2.md)
    - Which SPECIFIC neurons change the least when getting in all pictures of [mostly same for one factor] but with [other factor changed]?
        - Test: Change 1s into 7s by modifying input. How does that change activations? Which neurons change?
            - Brainstorm Implementation:
            - Requirement: Change pixels of 1s
    - The "1" is the default; the "7" is if there's something special, like a line above 1.
        - Do the “big activation differences” in layer 1 neurons have high weight conns to these input neurons?
    - Will knocking out weights to neurons whose average class differences are above a certain threshold change the prediction?
    - Is there a graph mapping between two models? Let f be a “subgraph circuit” (eg. a path) between A and B in M1, where A and B are general NN components (neuron collections, hidden states, attention heads, etc). Is there a mapping h: M1 → M2 s.t. g(A,B) is the “same type” of subgraph circuit? Type is informally defined as “functionality” (eg. an edge detection circuit)
        - Knockout A, B, then A and B in M1. Do the same in M2. Are there commonalities in the same knockouts (A gone in M1 and M2- what’s similar?)
            - Types of diff models: (make filter-able tables)
                - same arch, same params, diff weiights (XOR)
                - same arch, diff # parameters
                - etc.
    - Give a neural network the algorithms it needs to improve itself (backprop, etc). Now give it its weights. Can it simulate a neural network training within itself? Now have it connect this with reflecting on semantic inputs.
        
        [https://www.engraved.blog/building-a-virtual-machine-inside/](https://www.engraved.blog/building-a-virtual-machine-inside/)
        
        [test NN simulation within chatGPT](Questions%20Hypotheses%2087e989748e1942dfa05a7d90433f2e40/test%20NN%20simulation%20within%20chatGPT%206251a5ff667440eb9a0121c529373083.md)
        
    
    MLP models:
    
    - XOR
    - MNIST MLP: 1 vs 7

- CNN:
    - Try to map convolution circuits b/w similar models
    
    CNN models:
    
    - Simple CNN
    - Inception V1

Superposition

- If a neuron activates for 2 unrelated objs, is there actually something they have in common? Perhaps down the line in a circuit? Or a “shared role” (inhibition, eg) is used for them?
    - Expm by finding commonalities in their circuits
    

## Hypotheses

---

[ Evidence level: ? how to quanify this in comparable ways, if possible ? ]

GPT-2-Small Circuits:

- HYPOTHESIS: It may be that the “default” would output earliest. This means there’s no further “in-context” suggestions. But with in-context (”The child is…” as a “source example to-output”; or a pattern such as Alice-Bob, Alice- that may utilize duplicate heads), the model would output latest.
    - Evidence:
        - [REF](Code%20Notebooks%20432b45bb746f43eabf4172f69d384f8a/test_prompt_most_recent_S%20ipynb%20a51ecffd653d4d6c995692f0920be200.md) (for GPT-2-small )
- HYPOTHESIS: If the “to-output” pattern is given in the source, in many cases, the high output probability “latest subject” will be outputted compared to the 2nd place output.
    - Evidence:
        - For GPT-2-small: provided in [test_prompt_most_recent_S.ipynb](Code%20Notebooks%20432b45bb746f43eabf4172f69d384f8a/test_prompt_most_recent_S%20ipynb%20a51ecffd653d4d6c995692f0920be200.md)
    - NOTE: Unlike IOI, this doesn’t seem to correspond to a “human-reasaonble” prediction. However, since it is still a re-occurring pattern, it is interesting to investigate why GPT-2-small has learned this, and how this anomaly differs from how humans interpret these types of inputs
- HYPOTHESIS: However, [this statement](Questions%20Hypotheses%2087e989748e1942dfa05a7d90433f2e40.md) holds true for fewer subjects; as the number of subjects increases, it is less likely that the “latest subject” will be outputted.
    - Evidence:
        - There is not a lot of evidence to support this so far. Only [one test](Code%20Notebooks%20432b45bb746f43eabf4172f69d384f8a/test_prompt_most_recent_S%20ipynb%20a51ecffd653d4d6c995692f0920be200.md) has been done.
- HYPOTHESIS: the signal for a “more recent” subject has not “died out” as much because the model wants to attend to what’s “more recent” as “more relevant”; tokens from before are considered less relevant.
    - Question: Why does the high output logit for “most recent” occur under certain “unexpected” conditions, such as including a “to-output” phrase in a source section?
    - CRITICISM: Residual stream carries “unaltered” signals
- HYPOTHESIS: There are “not” mover heads
    - Evidence:
        - [adjective_mover_prompts.ipynb](Code%20Notebooks%20432b45bb746f43eabf4172f69d384f8a/adjective_mover_prompts%20ipynb%20cf8a6d9206fb47588b60c921c090b348.md)

### For Papers

---

- Potential organization formats
    
    Don’t use database to organize; only use it for quick summaries. Instead, just use lists, tables, and sections. This is much clearer because the words aren’t cut off. Then make database FROM those lists.
    
    (if have pages for questions, they detail many subquestions and brainstorms within it)
    
    [Compare Activations](Questions%20Hypotheses%2087e989748e1942dfa05a7d90433f2e40/Compare%20Activations%207d1b36005d97439b9a5a21ce8e75b63f.csv)
    

---