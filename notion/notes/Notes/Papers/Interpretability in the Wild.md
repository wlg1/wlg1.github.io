# Interpretability in the Wild

[IOI notebook code](../Code%20515029dddcdc4d268ad1b5b2298d2cd6/IOI%20notebook%20code%20fde870610bf0467ca455bcfc8a526f37.md) 

[Path Patching](Interpretability%20in%20the%20Wild%20f7e5e77ced0c4dd9812cc142ce372b37/Path%20Patching%20a59abdccacb7474fb1bca54f7000d6cb.md)

- How to find a circuit:
    1. Path patching: To find a connection, replace path P: head → R
        1. `from easy_transformer.ioi_utils import (path_patching,`
            
            [https://github.com/redwoodresearch/Easy-Transformer/blob/main/easy_transformer/ioi_utils.py](https://github.com/redwoodresearch/Easy-Transformer/blob/main/easy_transformer/ioi_utils.py)
            
        2. Path patching replaces the original path with the new path; so it’s not causal tracing?
        
        ![Untitled](Interpretability%20in%20the%20Wild%20f7e5e77ced0c4dd9812cc142ce372b37/Untitled.png)
        
        Causal tracing corrupts the original, then replaces the part of the corruption with that of the original. This is not the same as path patching. See Appendix B
        
    2. After finding heads that cause a large drop in logit difference upon patching (meaning they were crucial to giving lots of weight to the correct output), study attention patterns of these heads to see what tokens they attend to
        1. Hypothesize what the heads do based on this
    3. ???
        1. (import scatter_attention_and_contribution, from utils)
    4. Check what info it moves (copy score??)
    5. See what other heads affect it

---

- ****A Walkthrough of Interpretability in the Wild Part 1/2: Overview (w/ authors Kevin, Arthur, Alex)****
    
    [https://www.youtube.com/watch?v=gzwj0jWbvbo&ab_channel=NeelNanda](https://www.youtube.com/watch?v=gzwj0jWbvbo&ab_channel=NeelNanda)
    
    The model appears to have learned algorithms, not just patterns.
    
    IOI examples:
    
    The model learns that “names repeated twice” are correlated with “subject of the clause”
    
    19m40s: How to know GPT isn’t just memorizing patterns of facts without identifying semantic similarities, but is actually learning algorithmic patterns of constructing syntax and other semantic patterns? Find the parts that are doing IOI.
    
    The authors removed all components except the important head and checked if the behavior was still there. Found that doing so only resulted in low dip in performance for IOI correctness.
    
    - Dropout’s role (22m40s: )
        
        22m40s: We recently conducted some interesting work and discovered some results related to our initial hypothesis. The hypothesis was that the outcome occurred due to dropouts. In Transformers, one of the areas where Dropout is applied is on the attention pattern, where certain chunks that move information from a source token to a destination token will be dropped. However, we found that in models without Dropout, such as GPT Neo, there were still cases of induction. We found some heads that changed their behavior based on the presence of other circuit components, but the effect was not as strong as in models trained with Dropout. Our findings were not entirely clear, but we did find some interesting examples.
        
    
    25m30s: Actv patching patches from distribution where IOI ISN’T present TO distribution where IOI is present (fig 1). If this patched node causes a big change in logit, it’s likely impt.
    
    29m: knockout may not be reliable by itself due to backup heads, but actv patching gets the original effect itself, not just the component, so it can see what the original effect is doing regardless of backups (?)
    
    31m50s: it was tricky to figure out what to patch. there are many ways (why not just add noise?). Eg) IOI to ABC, or flip names
    
    33m50s: why is detecting the duplicate John done by induction heads, which have the role of detecting A…BA? GUESS: model just learns induction heads because they are useful (can be used for multiple roles), and since they already have this information of the second A, it uses them to detect the second A
    
    Induction heads may be like “pointers” and give an association (attn weight) b/w dest token to what the source position the dest token attends to, but not the source token at that position
    
    37m40s: after switching John and Mary’s positions, pointer heads that pointed to John (S1) now point to Mary, as the pointer head only cares about what’s at that position. However, if you use activation patching, the pointer points to John again
    
    This disentagles whether the head is tracking token value or position
    
    40m: in fig 10 left, these heads only care about position, not specific tokens (john, bob, etc)
    
    43m: neg name mover heads heads want to say John gave the bottle to John, instead of Mary. may be linked to composition mechanism
    
    Go and try to find IOI in other models. Shared motifs?
    
- pt2: [https://www.youtube.com/watch?v=b9xfYBKIaX4&ab_channel=NeelNanda](https://www.youtube.com/watch?v=b9xfYBKIaX4&ab_channel=NeelNanda)
    
    5m: models use skip conns to choose what layers matter for a task
    
    19m: only use single tokens
    
    22m: if you repeat right name, small gets answer wrong in 23% of test set. Even larger models don't do well
    
    29m: one reason 0 ablation is bad is bc 0 doesn't always mean nullify, it could be a trigger just like the bits in 01, put through OR gates. So it was found early heads took 0 to mean “make these heads impt”
    
    Mean ablations remove nodes output information with no task specific info, just bleh boring info that doesn't STAND OUT
    
    39m: backup heads effect seen more once removed main heads. It always has this effect, working in parallel. Its not responding. It just does its job and if main happens to fail it's already there 
    
    43m: How to check that B is interacting with A, without any nodes in the middle actually influencing B instead of A?
    
    Activation patching: patch the output of a head (eg. duplicate token head gets fed to the final token via an S inhibition heads) but actually a third thing in the middle mediates this interaction.
    
    So rather than splicing in the heads output to influence every node you just take the component of the input to this later head that comes from the earlier heads and you replace that component with the corresponding component of the original so it's like even more localized and targeted and this distinguishes between whether there's a mediator
    
    summary: path patching even more localized than actv patch. Double checks if mediators. Found same as actv patching 
    
    GUESS: in activation patching, the entire activation (including all paths after it) are patched in. In path patching, the outputs for intermediate nodes caught up in this are RE-COMPUTED and put back in (?)
    
    45m30s: mlps may be doing memory management on residual stream . Neurons may delete or inhibit directions no longer needed
    
    55m: figure 3b means change in logic diff divided by original logic diff. so neg name movers are blue, and name movers are red
    
    58m: not surprising attn output and final output are linear, but S values are lower than IO values. Name mover trends: The more the model attends to S, the more that head also attends to S.
    
    1hr1m: the OV matrix is like the identity matrix, meaning it’s just copying (where in the code is this?)
    
    1hr3m: some name mover heads can do copying without MLP, some need MLP embedding to copy
    
    1hr11m: taking mean sample may be bad due to distribution. eg) if distribution is a circle, mean is center. but if random, it’s just a pt on circle
    
    1h14m: very distributed so in other words there are a bunch of like heads are each contributing a little bit to compose the attention patterns of the S inhibition heads. thus, patch at values of S-inh heads isntead
    
    **1:14:36** the query says what my destination token be, key says what should my source token be and V says what information should I copy from a source to destination
    
    1:16:00: punctuation matters
    
    **1:17:22** look at the S and division heads 8.6 pays attention to names that are repeated that appear after periods
    

MLPs are hard to interpret, and may be interpreted by process of elim after attention heads are interpreted. MLP 0 may be a “better embedding” after embedding layer.

---

- Reflection on rsch
    
    [https://www.alignmentforum.org/posts/3ecs6duLmTfyra3Gp/some-lessons-learned-from-studying-indirect-object](https://www.alignmentforum.org/posts/3ecs6duLmTfyra3Gp/some-lessons-learned-from-studying-indirect-object)
    
    Types: pointer (location) heads, backup heads, negative heads
    
    > **One particularly challenging task to meet these criteria is to understand distributed behaviors**: behaviors where many components each contributes a little to compute some behavior in aggregate.
    > 
    
    > Path patching helps us measure the direct effect of an attention head on the key, query or value of another head, removing the effect of intermediate attention heads
    > 
    
    > For example, we have found initial evidence that the S-Inhibition Heads move positional information around (described in Appendix A of the paper). ****If you patch head outputs from prompts of the form ABBA (Then, John and Mary…. Mary…) to BABA (Then, Mary and John, Mary….) and vice versa, you cause a large drop in performance.
    Since the only information that changes is where the names are located, this result implies that the S-Inhibition Heads give positional clues to tell *where* the Name Movers should pay attention to.
    > 
    
    > When you replace the output of a node with certain activations (either in patching or knockouts), it’s important to think about **what information is present in those replacement activations, why it’s useful for that information to be present, and what effect that information will have on the rest of the model’s behavior.**
    > 
    
    > We wanted to mean-ablate to remove the effect of a node while still not destroying model internals (See Knockout section in the paper for more information). This decision ended up being particularly bad because the mean activation over the IOI distribution still contained information that helped compute the task.
    > 

---

p4: Mean-ablations remove the information that varies in the reference distribution (e.g. the value of the name outputted by a head) but will preserve constant information (e.g. the fact that a head is outputting a name).

Figure 2: This shows how the model is able to identify the IO token and output it. First, it has heads that identify all names. Then, it identifies what heads inhibits the S tokens. So tokens that aren’t S are outputted.

S1+1 is the next token after S1. S2 is the duplicate of S1

The token the head is active on is the row it’s on. The arrows going back from prev tokens to the head show which tokens the head attends to.

- What's a conterfactual effect?
    
    A counterfactual effect refers to the difference in outcome that would have occurred under different conditions or interventions. It is a hypothetical scenario that describes what would have happened if something had been different in the past.
    
    For example, imagine a study that investigates the counterfactual effect of a new medication on a certain disease. The researchers would typically compare the outcomes of two groups: one group that receives the new medication and another group that receives a placebo or standard treatment. The counterfactual effect would be the difference in outcomes between these two groups, which reflects the causal effect of the new medication.
    

p5: In path patching, not just one path is replaced, but all paths emanating from a head h

Figure 4c: after ablating S-inhibition heads, name mover heads attend to S more than IO

fig 4: these heads are s-inhibition, not name mover.
fig 5: these are duplicate + indincution / prev token heads. they affect s-inhibition

- p6: Tracing back the information flow. [questions]
    
    Name mover heads are affected by Q, K, V. K and V are claimed not to provide it information.
    
    WHY?: “their value matrix appears to copy the input tokens (see previous section), so
    we do not study it further.”
    
    WHY?: “as the IO token appears early in the context, the Name Mover Heads’ key vectors for this position likely do not contain much task-specific information”
    
    - WHY?: Why is the query vector located at the end position? I thought each layer had its own Q, V, K matrix
        
        GUESS: it means the query vector that attends FROM the end uses the name mover head? that is, the weights are more prominient “there”?
        

[https://colab.research.google.com/drive/1YM-0MPw0KKKkjRU855Js3HxBHDgePL1S#scrollTo=9ZTshkqB4uuN&line=2&uniqifier=1](https://colab.research.google.com/drive/1YM-0MPw0KKKkjRU855Js3HxBHDgePL1S#scrollTo=9ZTshkqB4uuN&line=2&uniqifier=1)

Fig 3c (p6): each sentence is a text sample input. we can get that input’s attention probabiilty on S and IO (the logit value of say “mary”) and its dot product of head output with the unembedding of the name token

as the attention probability on the Name (regardless of head) increases, the dot product of head X w/ the UNEMBEDDING of the name token increases (indicating those two are more similar the more the name is targetted for output)

[https://github.com/redwoodresearch/Easy-Transformer/blob/main/easy_transformer/ioi_utils.py](https://github.com/redwoodresearch/Easy-Transformer/blob/main/easy_transformer/ioi_utils.py)

- What are direction vectors for the IO and S tokens?
    
    The direction vectors for the IO and S tokens represent the learned embeddings or representations of these tokens in the model. These vectors capture the semantic information and characteristics associated with the IO and S tokens.
    
    In the provided code, the direction vectors are obtained from the `model_unembed` tensor, which contains the detached and CPU-based version of the model's unembedding weights. The direction vectors are extracted as follows:
    
    ```
    io_dir = model_unembed[:, io_tok].detach()
    s_dir = model_unembed[:, s_tok].detach()
    ```
    
    Here, `io_tok` and `s_tok` are the token IDs for the IO and S prompts, respectively. The `model_unembed` tensor is indexed using these token IDs to retrieve the direction vectors for the IO and S tokens.
    
    These direction vectors capture the model's understanding of the IO and S concepts and are used to measure the alignment or similarity between the attention mechanism and the direction of the IO and S tokens during the computation of attention probabilities and contribution.
    
    By computing dot products between the direction vectors and the residual values (the difference between the input and output of the attention mechanism), the code measures the extent to which the attention mechanism writes information in the direction of the IO and S tokens. This information is then used to plot the scatter plot, visualizing the attention probabilities and contribution in the IO and S directions for each input sequence in the IOI dataset.
    

Appendix A (p14):

To disentangle effects, control for one input area in one group and vary it in another group, then compare the two groups

Appendix B:

Algorithm 1:

- Given a head and a list of Receivers: for each receiver, recompute MLPs b/w h and R and save them (?)
    
    Figure 11c: head is red, receiver is yellow
    
- Then, run a forward pass through the model again using saved MLP values (?)