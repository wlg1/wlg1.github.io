# Questions/Hypotheses

- About
    
    Questions can be anything; hypothesis are questions formatted into a statement with a validity that can be weighed using tests
    
    Most hypotheses are accurately answered with a binary “reject or accept” test, so don’t have a column for that. The conclusion is usually more nuanced.
    
    This differs from Experimental Results because “Results” can contain findings that were not originally questions/hypotheses
    

## Questions

- Transformers:
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

## Hypotheses

---

[ Evidence level: ? ]

### For Papers

---

- Potential organization formats
    
    Don’t use database to organize; only use it for quick summaries. Instead, just use lists, tables, and sections. This is much clearer because the words aren’t cut off. Then make database FROM those lists.
    
    (if have pages for questions, they detail many subquestions and brainstorms within it)
    
    [Compare Activations](Questions%20Hypotheses%2087e989748e1942dfa05a7d90433f2e40/Compare%20Activations%207d1b36005d97439b9a5a21ce8e75b63f.csv)
    

---