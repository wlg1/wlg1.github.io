# In-context Learning and Induction Heads

> When induction heads occur in sufficiently large models and operate on sufficiently abstract representations, the very same heads that do this sequence copying *also*
 take on a more expanded role of *analogical sequence copying* or *in-context nearest neighbors.* 
By this we mean that they promote sequence completions like `[A*][B*] … [A] → [B]` where `A*` is not exactly the same token as `A` but similar in some embedding space, and also `B` is not exactly the same token as `B*`.
>