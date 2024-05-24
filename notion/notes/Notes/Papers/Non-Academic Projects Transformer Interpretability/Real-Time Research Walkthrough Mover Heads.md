# Real-Time Research Walkthrough: Mover Heads

**Part 1**

[https://www.youtube.com/watch?v=zaDZGgJ6WEA&list=PL7m7hLIqA0hp7mxjwShgnPu6Win-CN5Fz&index=1&t=320s&ab_channel=NeelNanda](https://www.youtube.com/watch?v=zaDZGgJ6WEA&list=PL7m7hLIqA0hp7mxjwShgnPu6Win-CN5Fz&index=1&t=320s&ab_channel=NeelNanda)

- I made some timestamps for the first half, and may edit them to be coarser/finer later:
    
    0:00 - Intro
    
    0:43 - State high level goal
    
    2:04 - State issue with current research
    
    5:33 - Start code to test if name mover
    
    11:20 - Plot logit difference between subjects 
    
    12:25 - Analyze plot’s heads (models are cursed)
    
    15:12 - Start code for “check which tokens”
    
    19:45 - Check which tokens name mover looks at
    
    20:10 - Start code for “stream → unembed”
    
    22:45 - Plot IO residual stream → unembed via L9H9
    
    24:27 - What this plot represents
    
    33:30 - State Core Question
    
    37:40 - Stretch Questions
    
    39:33 - Project Setup Questions
    
    46:33 - Start pythia_dla_sweep code
    
    54:40 - Function to store DLA for each head
    
    1:06:00 - Argmax functions
    
    1:11:30 - Run on familiar case study
    
    1:14:30 - Plot “Per-token correct log prob”
    
    1:16:40 - Induction heads detector issues
    
    1:18:30 - Code “Check if head is induction head”
    
    1:19:55 - Plot “Check if head is induction head”
    
    1:21:15 - Induction head attention pattern issue
    

I made some timestamps for the first half of “Mover Heads Part 1”, and may edit them to be coarser/finer later. Some of them include:

```0:00 - Intro

… 33:30 - State Core Question

… 1:18:30 - Code “Check if head is induction head” ```

<<<

NOTES:

- 0-10m
    
    0:43 - State high level goal
    
    name mover looks for duplicates then maps using ov to output
    
    1:52 - parameter mover heads
    
    2:04 - IO is too narrow. Looks at IOI distribution (looks monosemantic) but doesn’t look at full data distribution. Is IO meaningful on full data distribution? 
    
    3:30 - Perhaps name movers aren’t just ‘name movers’. 
    
    5:33 - How to test if a head is name mover
    
    6:40 - john and mary associated with nativity (final layer norm bias reduced to john logit vs mary)
    
    7:34 - check if there’s DLA function. have logti_attrs fn
    
- -20m
    
    12:30 - shouldn’t peak / trough at same head be same but reversed in sign? models are cursed (hard to predict how they interpret)
    
    13:00 - redline is ‘time gave bag to’, blue is ‘alex gave bag to’. Plot measures their difference at each layer
    
    13:40 - why neg name movers exist? not known. 
    
    if they used to not get huge loss, 
    
    16:30 - make a function that takes a list of tokens and …
    
    17:38 - …get something human readable to be put into plotly
    
    18:20 - issue b/c not single element or float. item() only works for single value tensor
    
    fix plot issue by get rid of model=None in fn
    
    19:00 - plotly merges x values with the same name
    
    19:45 - looking at how name mover head moves info for both sequences
    
    used two ‘when’ instead of ‘went to’
    
- -30m
    
    20:10 - if we apply this to the actual residual stream earlier on, what happens?
    
    22:00 - test hypothesis that if multiply unembed vector by decomposed resid stream
    
    22:47 - IO residual stream → unembed L9H9
    
    MLP 0 is very large spike
    
    23:00 - failed to multiply by layer norm so too large (spike is 196)
    
    24:00 - perhaps unembed onto Tim dir rather than logit diff dir
    
    24:30 - this graph represents: if take output of every component (head, etc), multiply by OV matrix of name mover, then umbed; how much does this change output logit? if a lot, then component is telling name mover to output tim
    
    25:50 - decompose residual stream at L9 else get unwanted things
    
    28:00 - residual stream decomposed (before L9) then multiple by L9H9
    
    this plot keeps track of layers until it gets to L9H9, which is why it spikes on it
    
- -40m
    
    32:00 - for each head, where is it attending
    
    33:30 - State Core Question
    
    37:40 - Stretch Questions
    
    Composition of monosemantic heads in superposition?
    
    38:50 - 
    
    39:33 - project setup questions
    
    how to: look by hand, not summary stats
    
- -60m
    
    46:33 - Start pythia_dla_sweep.py 
    
    50:50 - issue with pile tokens
    
    51:20 - figuring out pile tokens is a dataset
    
    53:46 - run the model
    
    54:40 - Function to store direct logit attribution (DLA) for each head
    
    think of what fns to code
    
    55:00 - div by 1 bil to think in gb
    
    cloud provider has issue ssh into 80gb
    
    57:00 - fill in get_head_dla
    
    stack of all mixed value (QKV) of heads
    
    58:40 - should we create a matrix W_OU from each head z to output tokens?
    
- -1h20m
    
    [-1] is z is in pos, so it’s last token
    
    Compose z with W_OU to get DLA for each head
    
    1:06:00 - Argmax functions
    
    1:10:50 - get correct output token
    
    1:11:30 - Run on familiar case study
    
    1:14:30 - Plot “Per-token correct log prob”
    
    rare tokens
    
    1:16:40 - Induction heads detector issues
    
    1:18:00 - Check if head is induction head
    
    1:19:50 - Plot “check if a head is induction"
    
    look at diagonal lines which look at induction token, which should always be 127 back from correct token 
    
    1:21:15 - attention pats should be 0 above main diagonal, but it think these are nontrivial
    

<<<

Timestamps to note:

- When start coding task / solving issue (likely wont know what it’s doing until once it’s finished, so go back to this later and re-locate backwards what is impt for final)
- When finish coding + to analyze / say what issue is + solution

Find general chapters first w/ approx timestamps. Recalibrate exactly and get details later after choosing which chapters to use. Dont worry if too spaced out or not close enough; get meaningful ones

---

[0:00](https://www.youtube.com/watch?v=r1cfSpVAeqQ&t=0s)

- Intro

[0:50](https://www.youtube.com/watch?v=r1cfSpVAeqQ&t=50s)

- Why does this paper exist?

[4:48](https://www.youtube.com/watch?v=r1cfSpVAeqQ&t=288s)

- What is a feature?

[5:09](https://www.youtube.com/watch?v=r1cfSpVAeqQ&t=309s)

- Monosemantic/Polysemantic Neurons

[6:28](https://www.youtube.com/watch?v=r1cfSpVAeqQ&t=388s)

- N-grams

[7:05](https://www.youtube.com/watch?v=r1cfSpVAeqQ&t=425s)

- Superposition

[7:29](https://www.youtube.com/watch?v=r1cfSpVAeqQ&t=449s)

- Privileged basis

[8:29](https://www.youtube.com/watch?v=r1cfSpVAeqQ&t=509s)

- Superposition vs polysemanticity

[9:04](https://www.youtube.com/watch?v=r1cfSpVAeqQ&t=544s)

- Distributed representation

[10:07](https://www.youtube.com/watch?v=r1cfSpVAeqQ&t=607s)

- Explanations for distributed representations

[11:48](https://www.youtube.com/watch?v=r1cfSpVAeqQ&t=708s)

- Probing

[13:37](https://www.youtube.com/watch?v=r1cfSpVAeqQ&t=817s)

- Why probing is boring

[14:26](https://www.youtube.com/watch?v=r1cfSpVAeqQ&t=866s)

- Three issues with probing

[19:19](https://www.youtube.com/watch?v=r1cfSpVAeqQ&t=1159s)

- Sparse probing

[20:07](https://www.youtube.com/watch?v=r1cfSpVAeqQ&t=1207s)

- Advantages of sparse probing

[24:58](https://www.youtube.com/watch?v=r1cfSpVAeqQ&t=1498s)

- Why do we think features are directions at all

[31:14](https://www.youtube.com/watch?v=r1cfSpVAeqQ&t=1874s)

- Why is sparse probing actually relevant to superpo