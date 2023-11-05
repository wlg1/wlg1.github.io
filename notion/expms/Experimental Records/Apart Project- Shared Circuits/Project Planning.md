# Project Planning

[Done](Project%20Planning%203798a71e7c5d4a888cad9a7d25a1275c/Done%20b715c92198314529880806d9f206803d.md)

---

### Working on

- IPP graph at various lvls of perf and pure/mixed comparisons
    - greater-than & overlap
    - decr & overlap
    - Get intersection of all perf and find its perf.
    - plot num_heads vs performance
- Functionality of similar components
    - mix digits, numwords, months in same prompt (two jan).
    - obtain for pure digits
    - try repeated months, months not in order, etc.
    - get induction offset scores and loop thru to find them
    - OV scores for the 3 types.

Circuit Connectivity- MLPs

- Ablate MLPs, neurons, and res stream outputs. See actv patching (EA, An)
    - What heads do MLPs rely on? path patch head to MLPs
    
- Writing
    - describe more on months, greater-than, decr circuits (prev scores)
    - describe this briefly:
        - we ablate on every position
        - path patching conscv layers like conmy, no input/residual post
        - footnote?: we note this is only one possible circuit for the task, and not the minimal circuit
            - Given that full circuit, we still refer to a subgraph of any size as a circuit.   But we do want to look for minimal circuits, smaller circuits
    - just metnion in future work:
        - future work: circuits of mixed/among
        - remove by combos at a time (eg. rand choose 3)
            
            Without 5.5, may have to rely on other heads. 
            
        - corr types (appndx): switchLastTwo, repeatLastTwo, repeatFirstAll, repeatRand, permutation, randAll (only use this one out of the 6)
        - we note there are several types of ‘shared circuits’
            - same circuit, similar tokens
            - same sub-circuit, branching components
            - same sub-circuit, components work together in diff ways (incr vs decr at diff lens)
        - Patterns that GPT learns from data? Eg) war lasts 20 years
    - ~~consider div by technq again (attn pattern, OV score, QK-OV corr) and subsubsub (bold) for early-mid-late in each technq section. this is better if the technqs compare e-m-l to each other; but if each is sep, consider e-m-l as more supersection instead~~
    - ~~Comment out background details, focus on parts less familiar to reviewers~~

query (dest) of where info moves to. move to all pos. however we will perform more expms to verify this claim in future work. this means each token relies on those heads to get info. only head 9.1 can be put at end without any change. non-ablate every query pos. future work: ablate every query pos except the important ones where the head is important for moving info to.

Circuit Connectivity- better iterative algos for all tasks

- path patching threshold re-check
    - [Should the negative values be taken?](https://colab.research.google.com/drive/19Le39gsiZOPqEat4VPHWDyU06My8GupZ#scrollTo=fg1gtdoVl6mU&line=2&uniqifier=1)
    - Do head have to conn only to adjacent layer? Review meaning of path patching
        
        [https://chat.openai.com/c/9e2fd95b-a957-4d81-940b-f774f4dd5f7e](https://chat.openai.com/c/9e2fd95b-a957-4d81-940b-f774f4dd5f7e)
        
        residual stream. but don’t explain in detail, just state edges between non-adjacent layers as in previous works (cite ACDC)
        
    - [https://arena-ch1-transformers.streamlit.app/[1.3]_Indirect_Object_Identification](https://arena-ch1-transformers.streamlit.app/%5B1.3%5D_Indirect_Object_Identification)
    Note that we're always measuring performance ***with respect to the correct answers for the IOI dataset, not the ABC dataset***
        - Incorrect token doesn’t need to be the correct answer of ABC; it just needs to be any arbitrary incorrect token (opt- that’s not too far away from IOI). notice ‘corrupted logit diff’ is only used in PP for normalizing. the ‘patching logit diff’ uses the original dataset; it only patches activations
    - Do not remove heads without outgoing. see fig 17 in ACDC; it keeps heads without incoming or outgoing. though all heads are conn. if you see heads without any nodes, you should change the threshold
        - justify this in paper (like ACDC, we do not bc…)
    - double check that the final circ pruned via path patching still has same score via ablation

---

after 11/3

- use among words circuits to get more randomness
- look at the nodes/edges diff between each circuit and try to explain them
- Already have logits after ablation, so just unembed them like in [extract_model](https://colab.research.google.com/drive/1cyW5ZlupQH0VJ6qWcFBkGMbOrDeHWMdD) to get values
    
    rmv what destroys its ability to pred next?
    
    This finds which heads are involved in decreasing. Instead, ends up pred same as last.
    
- make 80% be subcirc of 90% by starting from 90% and then removing more nodes.
- the reason months and numwords is smaller is because of a smaller dataset?
    
    actually this is wrong because we tried 0 to 12 for digits, and it still had a big circuit
    
    test this again on very small digits dataset
    
- Ablate sub-circ on one circuit and check for analogous drop in prediction in another
    - The ablation changes it in an analogous way based on what is predicted. Can we knockout the ability to predict next is we knockout 9.1? Are there backups?
    - Ablate the greater-than sub-circuit in the sequence completion (just delete from “keep circuits” head list). Run tokens through it.
        - which parts of the circuit are the most impt, for what fns? based on logit diff recovery % when ablating them.
    - edit next to prev by replacing actv (see ‘circuits re-use’)
- redo greater-than to use more samples in corrupted dataset

~~place all tasks in 1 nb to prevent reload times~~

~~improve randomness by not having any repeats?~~

[https://colab.research.google.com/drive/1KcODa7naVMJbOvHBGUL_CFxyfmAMM5YI#scrollTo=LkatbMdmp-W2&line=2&uniqifier=1](https://colab.research.google.com/drive/1KcODa7naVMJbOvHBGUL_CFxyfmAMM5YI#scrollTo=LkatbMdmp-W2&line=2&uniqifier=1)

there is an alternative circuit that doesn’t use 9.1 but distributes the computation of next more across other nodes

---

Circuit Connectivity

- Circuit Connectivity-  postponed
    
    <<<after nov 3rd
    
    - See how many further heads can be removed to achieve various levels of performance (70%, 80%, etc.).
        - Get circuits with lower performance (to make smaller) to compare and find sub-circuits with greater-than. At what threshold does it lose shared sub-circuits with greater-than?
        - Count the number of heads for 97% perf, Ethres 0.002 after get rid of no outgoing E
            - what is the true perf of circ after get rid of no outgoing E?
        - Venn diagrams for each lvl of performance
        - Top 10 most impt when rmv is inacc bc performance dependent on other heads?
        - Plot perf on x-axis and # heads on y-axis? Table showing what heads differ with each % being row, and cols of Same and Diff from 97%
        - (90 to 80%): However, there are heads not found from before, such as heads 3.2, 4.6, 5.0, 5.11, 6.8, and 8.6. This implies that the order we remove heads may matter. Thus we also try different orders to remove heads, and find how frequently heads appear in the final circuit over all orders. [only matters if don’t find minimal based on thres]
        - Try random order
        - Srange that 25% iter pruning keeps nodes that are not from 2%. Debug by tracking their perf diff in the two runs.
    - re-order circuit diagrams so prev layer heads are further on top.
        - make a table format of layer top bot, head# left right
    - check MLPs for decr circ
        - synergistic of MLP9 with 8.8? get logits for corr answer (not just top) after unembed each component and MLP component
            - what does tuned lens do?
    - how do we track the signal along a path? decr seems to differ how it computes based on seq len, check which components differ (4 to 8 len) but also on which members are in it. get logit lens “when it changes to get corr, if it ever does”, for all numbers 100 to k+1 for certain len k. get proportion
    - diff circuits for diff seq lengths. change seq circ to another seq circ
    - autoablate: mix in 1 dataset diff len random words (see IOI templates)
        - take avg of multiple templates of ‘random words’ in between digits seq. make sure, first, that gpt2-small can recognize these
        - was each template replaced by any other ABC, or just its own ABC?
    - why is pure digits circuit bigger than among words and can’t ablate by pos?
        
        How many extra heads are needed to deal with the noise? Shouldn’t be any more because attention works in parallel in the query weight matrix.
        
        If this is the case, why does among words need LESS heads? Shouldn’t it be the same amount?
        
        similar to among words: number multiple choice task. among words and IOI and color multiple choice all involve searching for and copying (or nexting). 
        
    - not all heads (see IOI) obtain output “from the embedding layer”; name movers in fig don’t. patch from MLP0 to them to check this.
        - [https://arena-ch1-transformers.streamlit.app/[1.3]_Indirect_Object_Identification](https://arena-ch1-transformers.streamlit.app/%5B1.3%5D_Indirect_Object_Identification)
        - perhaps just all nodes without incoming nodes auto have edge to ‘embed’? same with logits. check in ACDC figs
            - NOTE: this is wrong. Fig 17 shows 0.10 not having edge from embed
    - Use fn results to construct QK diagram in visio stating which queries the heads attend from, and which keys they attend to.
    - automate ablate seq pos by brute force. visualize scores?
        - Does ACDC automate ablate by seq pos?
    - automate by filtering via attention pattern first
    - patch by qkv; [see explr nb](https://colab.research.google.com/drive/1swp35sxN_1zNuIW4i4JyhWeY-YUlmUkk#scrollTo=JAbsTRepIAic)
    
    <<<after nov 15th
    
    - what are similar “polysemantic heads” or neurons that are the same but used in VERY DIFFERENT tasks? that is, “polysemantic sub-circuits”.
    - Try alt measures KL div
        - Check if large logit diff coincides with a true difference in correct vs incorrect token logits.
            
            `logits_to_ave_logit_diff_2`
            
            - Debug why mean resampling sometimes gets high scores. Logit diff gets bigger upon removal…?
                - This is explained by “ACDC” paper; so they use KL div instead
    - decreasing months seq
    
    <<<optional:
    
    - Causal trace by entire subcircuit
    - Simulated annealing search and choose smallest circuit with highest perf
    - add input and logit nodes to circuit diagrams
    - Measure the "amount shared". Make a figure which highlights what is shared between the sequence types.
    - Ask slack about difference b/w transformerLens and huggingface for token prediction. first input code to chatgpt to look for difference?
        
        [https://github.com/neelnanda-io/TransformerLens/blob/main/transformer_lens/utils.py](https://github.com/neelnanda-io/TransformerLens/blob/main/transformer_lens/utils.py)
        
    - try different dataset size batches for ablation
    - 2 4 6 8; fibonacci etc on, large, pythia, llama, etc.
    - detect the sequence out of multiple possible numbers. toy model- is there a sequence?
    - try random permutation corruption [issue- doesn’t erase all info]

---

Circuit Functionality

- Circuit Functionality-  postponed
    
    <<<after nov 3rd
    
    - is less-than a subcircuit of decreasing seq?
        - Use incontext learning to get less than
    - Put MLP0 embedding thru MLP
    - [Information movement using corruption on diff tokens/positions](https://www.lesswrong.com/posts/u6KXXmKFbXfWzoAXn/a-circuit-for-python-docstrings-in-a-4-layer-attention-only#Patching_experiments)
        
        When clean patched with corrupted, red means “it got worse”? When corrupted patched with clean, blue means “It got better”???
        
        - [https://colab.research.google.com/drive/1swp35sxN_1zNuIW4i4JyhWeY-YUlmUkk#scrollTo=YzmdOdeJIAiY&line=20&uniqifier=1](https://colab.research.google.com/drive/1swp35sxN_1zNuIW4i4JyhWeY-YUlmUkk#scrollTo=YzmdOdeJIAiY&line=20&uniqifier=1)
        - Corrupt “Adam is 1…” mean ablation using repeated seqs
    - The corruption type used in auto ablation and path patching tells the functionality
        
        eg) If a head influences an induction head (find this via path patching / iterative pruning via ablation), that head may be a prev token head (induction requires prev token head)
        
        - Swap at different positions
        - Or random num at a pos
    - Move most of early heads to appendix if not that impt. Connect it with months, number words, etc. and relate why greater-than needs less early heads than incr digits.
    - Find attnpat + OV scores of heads found from [manual adding and checking perf](Expm%20Results%208de8fe5b943641ec92c4496843189d36/Early%20Head%20Analysis%20b73c8162b7334655ad1ff91fb236b69e.md)
        - [https://colab.research.google.com/drive/16b8SwFckyC7Gv3RPUX8mme_Y8dfw0o1g](https://colab.research.google.com/drive/16b8SwFckyC7Gv3RPUX8mme_Y8dfw0o1g)
    - record how induction is used differently in each circuit
        
        How induction circuits work differently as sub-circuits in not just similar but dissimilar tasks, and what non-shared components differentiate these circuits from one another; IOI and many others already have induction inherently as a sub-circuit.
        
    - the induction patterns are irregular; attneds n-3, then n-7 instead of n-6
        - Try to reproduce ioi results on early
    - OV scores of early layer heads (1.5, 4.4)
    - loop through the output of OV unembeddings (just like SVD) and use GPT-4 to classify each (instead of just finding if copying or not). more than just top 5 tokens
    - attn pat on months/words (put in appendix; state in main they had similar patterns)
    - how to tell if a head is inh or boost another? name movers caused pos logit diff, while s inh caused neg logit diff
        - so dont just measure change in logit diff, but pos or neg on heatmap. Read IOI
    - check which heads’ copy scores are specific for numbers, not just “any type”. use multiple input types to those heads. Note that 7.10, 7.11 and 8.11 aren’t “name mover heads”, though 8.10 was a “s-inh” head
        - IOI small circuit (not found by ACDC) only got 87% score of original logit diff in ‘faithfulness’
    - bigger white line above eve in attn pat viz
    - head 9.1 also has n-3 attn pat. OV scores when pass "is" to 9.1?
    
    <<<after nov 15th
    
    - attn pat and output scores on add2, mult2, for medium
        
        [med_add2Scores.ipynb](https://colab.research.google.com/drive/18pPnSCWCdFKaiiMwBUAbQ_KrLDJ-vNnA#scrollTo=4rTl9Yd0Bcro)
        
        checked the "add 2 scores" of medium and it seems so far there's a couple of heads that are "add 2" heads in gpt-2med. which means we can perhaps find a more general class than just "next sequence" heads. interestingly, no clear "previous seq" heads so far. or rather than "add 2" their top 5 tokens are next members of the input token, some are even previous members. so i'll double check what i said about prev seq heads
        
        I remember someone in the third cohort made a blog post about addition in a toy model. i'll read it and perhaps there may be a connection to its patterns in larger models
        
    - Run tests on non seq number data thru heads to see if they still rec them
    - Early and mid head output scores: Try copy scores on “similar token” early heads to show they’re not looking at pos, but token type. early and late have their own OV sections. a summary of all early to late can be put in appendix
    - test irregular lengths to make sure not just n-2 pos head, but ‘sim type’
        - what makes each head diff from other heads than just “attends to type”?
    - also look for ‘greater-than’ output scores, etc. which means ANY, not just +1.
    
    <<<optional:
    
    - if numwords is too similar to digits, may add another increasing seq task aside from greater-than to compare overlaps
    - Run pruning algorithm on medium, then use embedding method to match with small
    - try other fns: [https://github.com/alan-cooney/CircuitsVis/blob/main/python/Demonstration.ipynb](https://github.com/alan-cooney/CircuitsVis/blob/main/python/Demonstration.ipynb)
    - SVD as perc of (l,h,dir), NOT (l,h). this is bc each dir has its own feature, not (l,h)
    - In svd, don’t just search for “digit” dirs, but “next” or “change” dirs
    - logit lens is supposed to be for all tokens (a table); prev, we only used one col (last token)
    - logit lens of which component?
    - https://github.com/AlignmentResearch/tuned-lens
    - MLP Probing, superposition

Predicted criticism:

- search for backup (L10 and 11?), negative heads

---

Collective of agents working on any rsch peoblem, say circuits. Come up with prompts. Generalize techn from other papers

If components all matter and it's like a symbolic code of what value is at each pos, then we can use code breaking. Eg. Mlp1 2 and 3 all en ode for feature.

If queried and keys act as lookup, then how do they relate to one another?

if a component actv for 2 very diff types of tokens (eg. names and numbers), what’s the cosine sim between names and numbers? what about along certain feature vecs?

### Future Work Ideas / Postponed

Find common circuits for more numerical tasks (not just seq cont)

- (path patching cod- skip z is z vector output for MLPs?)
- Validate early heads again- what are they really doing?
- email/msg to ask if the classification of “two types of methods” are valid
    
    We characterize circuit discovery methods into two types: 1) Circuit connectivity methods, and 2) Component functionality methods. The first type includes direct logit attribution patching, activation patching, path patching, and ACDC, which are types of causal mediation analysis that can be done on various component levels (residual stream layer, MLP, neuron, etc.). The second type includes attention pattern analysis, logit lens, OV-type scores (eg. copy scores), and using PCA and SVD to find interpretable directions. Note that this characterization is a generalized heuristic and not a strict classification, and observations from one "connectivity" method type may be used to obtain insights about "functionality', and vice versa.
    
- msg PQ for tips on grokking / analyze model training
- email authors of ‘greater-than’ paper about code + questions
    - What other circuits were discovered for these tasks?
    - Is there a list of tasks? (see appendix)
- Use ACDC to find common graphs for greater-than & less-than, and other numerical circuits (do they all use 9.1 for a similar purpose?)
    - email authors for questions
- new operations instead of just “next”, modular addition circuits
- 2 4 6; two four six
    - 1, 2, 3 and jan feb march are orderings. What are other types of orderings?
        
        [https://chat.openai.com/c/5ba1ac6a-7132-4a1e-b4d3-ce2f3f07c0c1](https://chat.openai.com/c/5ba1ac6a-7132-4a1e-b4d3-ce2f3f07c0c1)
        
- [https://arena-ch1-transformers.streamlit.app/%5B1.4%5D_Balanced_Bracket_Classifier](https://arena-ch1-transformers.streamlit.app/%5B1.4%5D_Balanced_Bracket_Classifier)
    - may have something to do with counting. even subject can do ‘counting’. But is counting and number recog the same? perhaps if a meta-model recog them to be the same in a model, that meta-model will develop a link between them
- Make summary video

Ablation

- Attempt to get less-than circuit diagram

- Ask chatgpt about forward pass after backwards (double simulation? filter local, then build global. test graph props, eg. weis-l test, and also algtop props)

---

- Try to find how digits + numwords SEQUENCES (not just individual tokens) change in latent space in each part of residual stream; start with after each layer, then dissect finer to heads + MLPs
    - 1 and One are already close after the first layer. But the sequence 2, 4, 6 and two four six may not be. It may not be considered an “even” dimension (direction).
        - entire input sequences are NOT vectors, but matrices? so how do we measure similarity of sequences if they’re matrices?
            - in a transformer, are input sequences embeeded as vectors, or matrices? would the sequence "2, 4, 6" be a single vector after the first MLP, or would it be a matrix?
                
                In a transformer model, input sequences are embedded as vectors, but the sequence of tokens/words becomes a matrix when considering all the embeddings together.
                
                To break this down:
                
                1. **Token Representation**: Each token or word in the input sequence is represented as an embedding vector. For instance, if your embedding dimension is \(d\), then each token would be represented by a vector of size \(d\).
                2. **Sequence Representation**: If you have a sequence of \(N\) tokens/words, and each token is represented by a vector of dimension \(d\), then the entire sequence is represented as a matrix of size \(N \times d\).
                
                Using your example of the sequence "2, 4, 6":
                
                - Assume that each number (token) is embedded into a vector of size \(d\).
                - "2" would have its own vector of size \(d\). Similarly, "4" and "6" would have their own vectors of the same size.
                - When you stack these vectors vertically to represent the entire sequence, you'll get a matrix of size \(3 \times d\).
                
                After the initial embedding, the transformer's subsequent layers would operate on this matrix, applying multi-head attention, feed-forward neural networks (which you referred to as MLP), etc., to process the sequence.
                
                So, to directly answer your question: The sequence "2, 4, 6" would be represented as a matrix after the embedding layer, where each row of the matrix corresponds to the embedding vector of a number in the sequence.
                
            - how would you measure the similarity between two input sequences?
                
                [https://chat.openai.com/c/b5c12746-f184-4f2b-babe-af1df51d96fc](https://chat.openai.com/c/b5c12746-f184-4f2b-babe-af1df51d96fc)
                
        - is the 2, 4, 6 direction and 8, 10, 12 direction similarity (by cosine sim)?
    - measure the svd similarity between them at each layer
    - each data pt is a series of numbers, but may not be in order. show that ordered seqs have more similarity than non-ordered when dim reduc to 2D along most impt dims
- PCA viz seq types thru layers
    
    To understand how to relate digit activations to wordnum activations, working on PCA visualizations of input sequence types to see how they change by layer (so far, no notable patterns found in visuals). Using this to find if there are directions corresponding to "sequence"- probably "sequence" is not measured this way and this may not exist. Inspired by: [https://www.lesswrong.com/posts/mkbGjzxD8d8XqKHzA/the-singular-value-decompositions-of-transformer-weight](https://www.lesswrong.com/posts/mkbGjzxD8d8XqKHzA/the-singular-value-decompositions-of-transformer-weight)
    
    And paper "Language Models Implement Simple Word2Vec-style"
    
- Edit digit circuit to become number words
    - Replace digit activations with number words activations
    What's the differences? Can this difference be added to edit any digit into months?
    - 9.1, given 'one', will output word 'two'. can we convert 'two' into '2'? measure difference in activations of '1' and 'one' after crucial attnetion head 9.1. is this the 'digit to numwords' direction? when put thru the circuit, what happens?
- Minitially retrain transfer learning toy digits circuit to become months circuit
- do name mover heads attend to anything? if so, why isn’t 19.1 in med attending to anything, even though it should be a “next” head?
- get a distribution of next head scores
- gpt-2 medium, llama
    - Given that only one head, 9.1, appears to do “next”, can a single layer be trained to do seq completion (though it may require other heads, at 9.1 isn’t enough?) To isolate circuits better, train and study toy models that perform number recognition. See if analogous circuits from toy models are present in larger gpt ones
- Which are copy heads and which are next heads? Output a sample based on proportion. Randsel yes and nos
- Causal Scrubbing
    
    [https://github.com/pranavgade20/causal-verifier](https://github.com/pranavgade20/causal-verifier)
    
    [https://github.com/redwoodresearch/rust_circuit_public](https://github.com/redwoodresearch/rust_circuit_public)
    
    hard to use if don’t know rust
    
    [https://github.com/redwoodresearch/remix_public](https://github.com/redwoodresearch/remix_public)
    
    requires rust
    
    [https://github.com/redwoodresearch/remix_public/blob/master/remix_d4_part1_instructions.md](https://github.com/redwoodresearch/remix_public/blob/master/remix_d4_part1_instructions.md)
    

---

- Introduction and abstract; what main contributions are
- label x and y axis of figures, matplotlib save as pdf, don’t use scale args, caption should be in depth
- figures that zoom in with magnifying arrow to transformer block (if too small), or log scale
- avoid referring to non-peer reviewed work (eg. induction mosiac; try to find a paper with same content unless it doesn’t exist)

---

- anonymized review- just get feedback
    - state a lot of what will be done in future work due to paper weaknesses
        - Reviews released: Nov 10; this means can’t submit to workshop
            - there’s a good chance it may get accepted at workshop
            - [https://openreview.net/group?id=ICLR.cc/2022/Workshop](https://openreview.net/group?id=ICLR.cc/2022/Workshop)
        - [https://chat.openai.com/c/5bd83003-3142-4545-9ff6-e84a61f647f2](https://chat.openai.com/c/5bd83003-3142-4545-9ff6-e84a61f647f2)
    - Continue to- Msg some other authors to ask about how high lvl description of paper idea would do at a conference
        
        Based on: [https://openreview.net/forum?id=9XFSbDPmdW](https://openreview.net/forum?id=9XFSbDPmdW)
        
- A new method to find shared circuits?
- How do “next” heads play a role?
    - Test how ablating them…?
        - feed IOI to GPT-2 (cannot have highlights/comments) then ask:
            
            In the Interpretability in the Wild paper, it was found experimentally that heads were performing copying tokens. In a new circuit, we found heads that may be taking in a digit such as “1” and outputting the next digit, such as “2”. How can we test that they are doing this in a circuit which finds the next member of a sequence given a sequence as input?
            
            [https://chat.openai.com/c/dcf660a8-9ff9-4ed8-aec8-08a5a6d146f1](https://chat.openai.com/c/dcf660a8-9ff9-4ed8-aec8-08a5a6d146f1)
            
- CONT-  Find “Next Heads”
    
    [in code, loop corr fn code over multiple top heads and see which heads have highest]
    
- If 9.1 matters the most for “next” for digits, months, etc (and there’s no differing part needed to distinguish them; it handles for all those types), what are the other heads for? Are MLPs even needed for “next”? 9.1 by itself isn’t enough.
- Find which parts of circuits, if any, “branch off” the months from digits circuits

---

- instead of ablating, just remove non-circuit nodes and keep the circuit. but given circuits are matrices, isn't this the same as zero ablating?
- Understand inputs + outputs of N2G nb
    
    [Neuron2Graph.ipynb](https://www.notion.so/Neuron2Graph-ipynb-1194a0bf97744b3ab86b19fc9d0bbd06?pvs=21) 
    
- cont- ⚠️ gpt2_Neuron2Graph.ipynb
    - use neuron2graph to find more number neurons
- [NOTE: these 'random circuits' may be disconnected; what about testing against "connected" random circuits?]
- read othellogpt world model: [https://www.alignmentforum.org/posts/nmxzr2zsjNtjaHh7x/actually-othello-gpt-has-a-linear-emergent-world](https://www.alignmentforum.org/posts/nmxzr2zsjNtjaHh7x/actually-othello-gpt-has-a-linear-emergent-world)
- digits has far more samples than others and thus its statistics may be 'more accurate'; other should have more samples. figure out new input types that have more possible samples
- copy scores for other important components
- figure out how to deal with multi-token words
- max actv examples for attn heads, not just MLP neurons
- see which neurons have the largest difference between how much they write in a chosen direction
- take dot product of neuron output weights with more types of cont seq tokens + prompts (relns between tokens)
- check neuron activation after ablating attention head (zero or mean ablation? try both)
- path patching
- add2 inputs in gpt-2 small
- measuring analogical similarity against circuit similarity
- perform ablation; try causal scrubbing
- compare MLPs between analogous seqs using N2G
- interpolation of predicted words when changing part of circuit
- feed info about circuits into chatgpt and talk to it

---

Turging weight to 0 removes ndoe, while 0 activwrion doesn't and is zero ablating

No, both do the same thing of giving 0 output to next. Actually not really, 0 Wright on one edge doesn't mean 0 on all, while 0 actv does

[http://blog.ezyang.com/2019/05/pytorch-internals/](http://blog.ezyang.com/2019/05/pytorch-internals/)

Examine and compare

---

**********Previous To-Do list categories**********

[23 10 9 - 23 10 15](Project%20Planning%203798a71e7c5d4a888cad9a7d25a1275c/23%2010%209%20-%2023%2010%2015%20546cb16c31664f68a2eb976d8a60e033.md)