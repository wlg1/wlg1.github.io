# Brainstorm relation of analogy order task to IOI task

- Re-discover IOI w/ similar IOI examples and use that to guide new, similar non-IOI inputs
find similar heads using 'head attn' and actv patching
    
    [https://colab.research.google.com/drive/1n4Wgulv5ev5rgRUL7ypOw0odga9LEWHA?usp=sharing](https://colab.research.google.com/drive/1n4Wgulv5ev5rgRUL7ypOw0odga9LEWHA?usp=sharing)
    IOI Notebook
    
    hypotheize that the "pet is" input has heads identifying subject, then heads determining order.
    this is based on idea that there are identifying-subjects heads, inhibition heads, ordering heads
    
    Mary, Fido, Fido. Pebbles, Rachel -> Pebbles
    Hypothesis: Thus, Rachel, Mary, Fido are all inhibited
    
    is there an algorithm for "pet is", like IO?
    	Mary is X. John is Y. Z is Mary.
    	- Identify who is first
    	- remove all that's not the first? (inhibit)
    	- just output the first one
    what if this is changed up to have more than 2? can it reocgnize the changed pattern?
    	try on -xl if -large does bad
    
    can we inhibit certain heads so it doesn’t output the first, but the one associated with second instead? or ADD/EDIT it to not assume Z = Y (based on position) but on certain traits such “Y has animal, X doesn’t have animal”. 
    
    more elaborate analogies may have heads that identify traits, eg) what is the relation of the MC to the mentor, to identify who is not the MC (inhibit), check if MC has sword (as freq that hero has sword is large in many examples of hero's journey)
    

---

[create tables of useful results]

Focus on analogy order and sequences for combos consisting of:

- different inputs types.
    - Eg) finding ‘cat’ is type of ‘pet’ over ‘human’ failed. what about other subclasses? say teacher, house, color, etc.
    - try providnig the trait in the input. Eg) Mary has paws. John has no paws. The animal is
- various models
- various ablations of heads (zero, mean)
- various corruptions (switch order, add noise to input embeddings)

Things to test correlations for: (use blocking, stat tests, etc)

- using external info?
- try using more traits
- ordering
- stronger markers/boundaries to define separations to model (eg. that is part of source, not target, system)

Like in functions, find a way to repeat the same things we need to test. Put in collapsable or new page that’s searchable/filterable in custom views.

---

Create new nb to test simple analogies (before, tested sequences and just the one type of analogy of “the pet is…”)

[https://colab.research.google.com/drive/1aOEeY4roW8oWqkZ0MuuZRJXmJGDRNcbr](https://colab.research.google.com/drive/1aOEeY4roW8oWqkZ0MuuZRJXmJGDRNcbr)

1) Test on gpt2-large. Provide a source system and then a target system. Use as little external information as possible

Mary has X. John has Y. Z is John. Ashley has X. Ben has Y. Z is

As before, change the order. But don't switch the names order; switch the properties (y, x) order