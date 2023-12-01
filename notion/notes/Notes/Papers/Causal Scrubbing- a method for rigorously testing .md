# Causal Scrubbing- a method for rigorously testing interpretability hypotheses

A pdf draft:

[https://static1.squarespace.com/static/6114773bd7f9917b7ae4ef8d/t/6364a036f9da3316ac793f56/1667539011553/causal-scrubbing](https://static1.squarespace.com/static/6114773bd7f9917b7ae4ef8d/t/6364a036f9da3316ac793f56/1667539011553/causal-scrubbing)

- 1: Introduction
    
    p4: 
    
    ● In Motivation, formalization, examples, we give a detailed explanation of the causal
    scrubbing algorithm and the reasons for various design choices we made.
    ● In Causal scrubbing on a paren balance checker, we apply causal scrubbing to
    evaluate an interpretation of how a small transformer checks if parentheses are
    balanced.
    ● In Causal scrubbing on induction heads, we use causal scrubbing to study induction
    heads on a two-layer attention-only language model.
    

---

[https://www.alignmentforum.org/s/h95ayYYwMebGEYN5y](https://www.alignmentforum.org/s/h95ayYYwMebGEYN5y)

---

[https://www.lesswrong.com/posts/JvZhhzycHu2Yd57RN/causal-scrubbing-a-method-for-rigorously-testing](https://www.lesswrong.com/posts/JvZhhzycHu2Yd57RN/causal-scrubbing-a-method-for-rigorously-testing)

- 1 Intro and 2 Setup
    
    Causal scrubbing starts from the output and recursively finds all of the invariances of parts of the neural network that are implied by the hypothesis, and then replaces the activations of the neural network with the *maximum entropy*[[3]](https://www.lesswrong.com/posts/JvZhhzycHu2Yd57RN/causal-scrubbing-a-method-for-rigorously-testing#fng10ehlzhmhl) distribution subject to certain natural constraints implied by the hypothesis and the data distribution
    
    Grokking and Induction heads: zero ablated the IMPT part to show it greatly affects model, while zero ablation of model doesn’t affect it
    
    IOI: mean ablated the UNIMPT parts to show impt parts still achieve full model performance
    
    CS: unlike the standard zero and mean ablations, we ablate modules by resampling activations from *other* inputs
    
    causal tracing aims to *identify* a specific path (“trace”) that contributes causally to a particular behavior by corrupting all nodes in the neural network with noise and then iteratively denoising nodes.
    
    In contrast, causal scrubbing tries to solve a different problem: systematically *testing* hypotheses about the behavior of a whole network by removing (“scrubbing away”) every **causal relationship that should not matter according to the hypothesis being evaluated.
    
    [https://en.wikipedia.org/wiki/Defeasible_reasoning](https://en.wikipedia.org/wiki/Defeasible_reasoning)
    
    we expect that in the context of interpretability, we need to accept arguments that might be overturned by future arguments.
    
    [https://en.wikipedia.org/wiki/Extensionality](https://en.wikipedia.org/wiki/Extensionality)
    
    These functions are extensionally equal; given the same input, both functions always produce the same value. But the definitions of the functions are not equal
    
- 3 CS
    
    If this hypothesis is true, we should be able to perform two types of ‘resampling ablations’:
    
    - replacing the activations of A, B, and D with the activations on other inputs that are “equivalent” under I; and
    - replacing the activations that are claimed to be unimportant for a particular path (such as C or z1 into B) with their activation on any other input.
        
        
        “treeified” version of G where every path from the input to output of G is represented by a different copy of the input.
        
        Eg) Input x1 is repeated 7 times as there’s 7 paths (2*3 + 1)
        
        Replacing an activation with one from a different input is equivalent to replacing all inputs in the subtree upstream of that activation.
        
        If x1 and x2 are extensionally equivalent (same output on node A), replacing A’s output w/ x2 will not change (much?) x1’s final evaluation (that’s on a path that has A)
        
        In the figure, the replacement of A is shown in the dotted yellow box. Not only does it replace A, but it replaces all inputs upstream (ancestors to) of A
        
        3.2 The causal scrubbing algorithm: recursive from bottom up, one path at a time from sink to source (not leaf to root b/c don’t explicitly tree-ify)
        
        E_scrub(h,D): expectation of the behavior f over samples from this algorithm.
        
    
- **4 Why ablate by resampling?**
    
    If the claim is “this module’s activations are literally unused”, then we could try replacing them with huge numbers or even NaN. But in actual cases, this would destroy the model behavior, and so this isn’t the claim we’re trying to test.
    
    “The behavior might depend on various properties of the activations of this module, but those activations aren’t encoding any information that’s relevant to this subtask.” Phrased differently: The distribution of activations of this module is (maybe) important for the behavior. But we don’t depend on any properties of this distribution that are conditional on which particular input the model receives.
    
    This is why, in our opinion, the most direct way to translate this hypothesis into an intervention experiment is to patch in the module’s activation on a randomly sampled different input–this distribution will have all the properties that the module’s activations usually have, but any connection between those properties and the correct prediction will have been scrubbed away.
    
    4.2:
    
    1. *Zero and mean ablations remove variation and thus present an inaccurate view of what’s happening.*
    
    Does this mean they have too much information?
    
    Doesn’t mean mean ablation inflating performance results?
    
- 5 results
    
    5.2:
    
    We test these hypotheses on a subset of openwebtext where induction is likely (but not guaranteed) to be helpful.[[19]](https://www.lesswrong.com/posts/JvZhhzycHu2Yd57RN/causal-scrubbing-a-method-for-rigorously-testing#fnhy4rcbsvbk)  Evaluated on this dataset, this naive hypothesis only recovers 35% of the performance. In order to improve this we made various edits which allow the information to flow through additional pathways:…
    
    - We also special case three layer 0 heads which attend to repeated occurrences of the current token. In particular, we assume that the important part of the output of these heads is what their output would be if their attention was just an identity matrix.
        
        And thus the residual of (actual output - estimated output) is unimportant and can be interchanged with the residual on any other input.
        
    
    With these adjustments, our hypothesis recovers 86% of the performance.
    
    (ad hoc: something that has been formed or used for a special and immediate purpose, without previous planning)
    
- 6 to alignment
    
    [https://docs.google.com/document/d/1WwsnJQstPq91_Yh-Ch2XRL8H_EpsnjrC1dwZXR37PC8/edit](https://docs.google.com/document/d/1WwsnJQstPq91_Yh-Ch2XRL8H_EpsnjrC1dwZXR37PC8/edit)
    
    Eliciting latent knowledge: report its latent knowledge of off-screen events? (Eg. sensor tampering)
    
- 7 limitations
    
    If two terms are correlated, sampling them independently (by two different random activation swaps) reduces the variance of the sum. Sometimes, this variance can be harmful for model performance – for instance, if it represents interference from polysemanticity. This can cause a hypothesis that scrubs out correlations present in the model’s activations to appear ‘more accurate’ under causal scrubbing.
    
    These examples are both due to the hypotheses not being specific enough and neglecting to include some correlation in the model
    

---

[https://www.greaterwrong.com/posts/JvZhhzycHu2Yd57RN/causal-scrubbing-a-method-for-rigorously-testing/comment/XYnp7pLoAaD3ewMxK](https://www.greaterwrong.com/posts/JvZhhzycHu2Yd57RN/causal-scrubbing-a-method-for-rigorously-testing/comment/XYnp7pLoAaD3ewMxK)

---

Related:

[https://openreview.net/forum?id=ytYaiSQNCB](https://openreview.net/forum?id=ytYaiSQNCB)

[https://arxiv.org/pdf/2211.06738.pdf](https://arxiv.org/pdf/2211.06738.pdf)