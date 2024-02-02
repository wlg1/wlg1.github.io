# New Novel Contributions

novel contributions:

1. we look at different *sequences*, not just looking for "the next one". and so we compare circuits of "2 4 6 8" in gpt2 medium, decreasing circuits, etc. (ie) how does more members change the circuit? I'll try to finish these by this sat
    1. other task types: decreasing sequence, less-than circuit, gpt2 medium “2 4 6 8”
    2. show GRADUAL explanation of the “extra heads” used when altering sequence (increase number of sequence members). the sucessor heads paper talks about only “the next”, not about how the sequence influences the rest.
2. how does among random words change the task to uncover a sequence? that is, how does the circuit find the sequence from among the noise (similar to subj identif in IOI)? this is what ive been doing today and continuing till friday
3. use recursive algorithm to obtain *multiple* possible circuits using diff combos, and compare why they work. fwd backw passes. I haven't done this yet but I think it's not too hard (but this one is optional as it seems to different than the main topic of the paper to relate to)

---

other ideas:

shared induction heads (already know this is shared by several induction tasks)

shared “next sequence” heads

repeating heads

show able to edit next into previous 

repalce activations?

a head’s weights are dependent on others, so it’s not enough to just replace one’s weights with another, it depends on how it connects to other weights in a circuit. this reqs re-training