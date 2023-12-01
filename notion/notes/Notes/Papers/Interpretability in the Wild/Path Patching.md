# Path Patching

Similar to Figure 11 from Appendix B in paper, with activation values added. For simplicity, the residuals are implied but not shown:

![Untitled](Path%20Patching%20a59abdccacb7474fb1bca54f7000d6cb/Untitled.png)

![Untitled](Path%20Patching%20a59abdccacb7474fb1bca54f7000d6cb/Untitled%201.png)

Patch paths: h → R . h is the red node in pass C, R are yellow nodes in pass C

Forward pass C: The purpose is to compute the yellow nodes R, whose only difference from their values in pass B is that their term h used to compute them is from pass A

eg) In a simplified analogy, if R = p + q + h, then 

pass B’s R = 1 + 2 + 3

pass C’s R = 1 + 2 + 4 (b/c h is from pass A, the corruption)

By keeping p and q the same, it reduces/blocks the effect of corrupted mediator variables. This value of R is “stored (in the yellow box) and given to pass D”, but is not used to compute any values of descendent nodes in pass C.

Forward pass D: The purpose is to find the effect of yellow nodes R on the logits. 

Here, the IOI’s effect on paths h→R is corrupted (replaced by ABC’s effect). The node h is not replaced by x_new because it’s also used to compute nodes unrelated to R; h’s effect on R is already captured by the yellow node (this is h’s indirect effect on the logits).

Thus, this determines how changing paths h→R affects the logits.

QUESTION: In the interview with Neel Nanda, it was stated that activation patching was also able to be used instead of path patching. If the activation patching is like causal tracing from the ROME paper, it seems to only patch in one node. So for cases like h=S-inhibition → R = Name mover queries (figure 4), is h or R patched? Or perhaps all h and R nodes are patched?

- brainstorm
    
    How can actv patching work for S-inhibition on Name movers because that doesn't have receivers, just heads? but in interview, ti was stated actv patch did work
    
    [https://www.youtube.com/watch?v=b9xfYBKIaX4&ab_channel=NeelNanda](https://www.youtube.com/watch?v=b9xfYBKIaX4&ab_channel=NeelNanda)
    
    At 44m, it's stated "didn't discover anything exciting and new from this you were just like cool our naive hypothesis was more legit than we might have hoped”
    
    From interview: The naive way is to only patch in R from x_new. The path patching way obtains R’s value from forward pass C.
    
    Was this done similar to causal tracing in ROME, where a subset of activations from x_clean is patched back into x_corrupted (which differs from path patching, as that patches a subset of x_corrupted into x_clean)?
    

QUES 3: the head has 3 weight matrices. When it’s stated that the “value matrix” is patched (figure 5a), does that mean only the output of the value matrix is stored (from pass C) then patched in (on pass D)? Is this the same for only patching in the query matrix of name mover heads in figure 4a?

(see p16 footnotes)

How do you choose the Q, K, V, or residual stream end to patch? Are they all run?

see interview end

---

p16:

step 4 algo 1: the value on yellopw is computed, but in this forward pass, it's not used in further computations after it; it's just saved to be used for forward pass D.

step 5: fwd pass D computes xorig except those values from yellow are repalced with the values from step 4

the logit diff from D is what's measured. in D, h isn't replaced. but the effect of h on yellow are replaced. it's diff from prev actv patching in several ways, so it's tricky if one tries to think of it as too closely resembling those approaches

the reason for this is that yellow is the receiver (eg. effect ON we want to measure, such as h-> name mover). this is diff from measuring the effect of h itself on the logits

QUES: how to do actv patching in the first palce to measure mediators? seems like you need path patching.

Figure 7 shows path patching on S-inhibition values. Figure 12 shows path patching on S-inhibition keys.