# Early Head Analysis

From ACDC:

![Untitled](Early%20Head%20Analysis%20b73c8162b7334655ad1ff91fb236b69e/Untitled.png)

Key Pos → Query Pos

Eg) S1 → (S1)+1 : Prev Token means (S1)+1 pays attention S1, the token right before (S1)+1

So look at what does the query pay attention to?

Fig 2 in IOI: the query and output arrows show which residual streams they write to, and the key/value arrows show which residual streams they read from.

~~In other words, there is not just one residual stream, but multiple rs for each POSITION. So the head focuses on writing to a specific position’s rs?~~ This is done via matrix multiplication- the row (query) is the output, so each row represents a position of the residual stream. These are all then combined when multiplying by the OV matrix?

---

Mid/Late heads are looking to predict what’s next; that’s why their weight that queries from the end is most impt. This mid/late query weight (vector) looks at different keys depending on the head. The mid head’s query weight vector (at the end) looks at Induction Head’s output (as its impt key vector- this is a dot product of 2 vectors), while late head’s query weight vector looks at the IO token.

[Query, Key, Value, Output Matrices](https://www.notion.so/Query-Key-Value-Output-Matrices-fe92464f6ee24068b6aaa56bb85e903e?pvs=21) : vector for every pos (token)

querstion: how does the QK matrix pay attention to inputs (keys) from different layers (IO is from 1st, induction head output is from 5th and 6th)

---

How did prev papers diagnose early + mid? Try getting interpretations from prev papers that used the same heads

Summary:

1. Attention patterns
2. Use random inputs for induction heads
3. Scores

- [https://arena-ch1-transformers.streamlit.app/[1.2]_Intro_to_Mech_Interp#exercise-visualise-attention-patterns](https://arena-ch1-transformers.streamlit.app/%5B1.2%5D_Intro_to_Mech_Interp#exercise-visualise-attention-patterns)
    - [https://github.com/callummcdougall/ARENA_2.0/blob/main/chapter1_transformers/exercises/part2_intro_to_mech_interp/solutions.py](https://github.com/callummcdougall/ARENA_2.0/blob/main/chapter1_transformers/exercises/part2_intro_to_mech_interp/solutions.py)
        
        run_and_cache_model_repeated_tokens ← generate_repeated_tokens
        
        [https://chat.openai.com/c/f02bd75d-d97f-4ac5-9b1d-c47012e9359b](https://chat.openai.com/c/f02bd75d-d97f-4ac5-9b1d-c47012e9359b)
        
        In contrast to a repeated sequence like ABCABC, we don’t have repeated numbers; they are all increasing. Yet it’s still an “inductive pattern”?
        
- [https://arena-ch1-transformers.streamlit.app/[1.3]_Indirect_Object_Identification#validation-of-early-heads](https://arena-ch1-transformers.streamlit.app/%5B1.3%5D_Indirect_Object_Identification#validation-of-early-heads)
- IOI: AppH VALIDATION OF THE INDUCTION MECHANISM ON SEQUENCES OF
RANDOM TOKENS. Fig 18
- [https://transformer-circuits.pub/2022/in-context-learning-and-induction-heads/index.html](https://transformer-circuits.pub/2022/in-context-learning-and-induction-heads/index.html)
    
    This paper has model to model comparison using pca embeddings. Cont seqs are like analogical seq completion. Try more interspersed words among seq. 
    
- greater-than didn’t seem to verify functionality of early heads

---

[multi_Adamis1_circ_cvVIS_draftv1.ipynb](https://colab.research.google.com/drive/1FThBbzvhipfGHb4jwdXLA6iXlIv75spp#scrollTo=0tLcFYvXvojR&line=1&uniqifier=1)

- [https://github.com/alan-cooney/CircuitsVis/blob/main/python/Demonstration.ipynb](https://github.com/alan-cooney/CircuitsVis/blob/main/python/Demonstration.ipynb)
- [https://alan-cooney.github.io/CircuitsVis/?path=/docs/attention-attentionpattern--induction-head](https://alan-cooney.github.io/CircuitsVis/?path=/docs/attention-attentionpattern--induction-head)
- we don’t need collective avg of all ‘early layers’ anyways; we just need indiv heads attn pat to show how they each behave
- for paper, heatmap is better than just “hovering over token” as it displays ALL attentions at once
- In 4.4, we see only numbers (rows) attend to previous numbers (cols). And slightly “periods” attend to previous numbers. Names don’t attend to names.
- [head 0.3](https://colab.research.google.com/drive/1FThBbzvhipfGHb4jwdXLA6iXlIv75spp#scrollTo=YP1S-LgiRGDD&line=1&uniqifier=1) attends to itself, and also from the period to everything else before it EXCEPT name! Stronger on the “is” than numbers. Perhaps because obtaining pattern of “is’ after name?
- induction head 5.5: period attends to names
- head 6.9: nothing happens “late” in input. but early tokens in input attend 3 tokens back
- like 6.9, head 6.1 seems to be (n-3). “Adam is 1.” Goes from . to is, or names to is. but NOT numbers to anything else?
    - does it adjust what it looks back if seq patern is of diff lens?
- head 1.5 appears to attend only from num to num, unlike it being stated as (n-2) from IOI paper. however, it can be removed from the circuit w/o being too impt. how much perf does it add? is it backup if rmv other heads?
- [don’t use pysvelte; use circuitvs](https://colab.research.google.com/github/neelnanda-io/TransformerLens/blob/main/demos/Main_Demo.ipynb) as pysvelte no longer supp
    - [https://twitter.com/ch402/status/1475862089528799233](https://twitter.com/ch402/status/1475862089528799233)
- [https://chat.openai.com/c/a62af7ec-5c8f-4726-b803-85db852ecff4](https://chat.openai.com/c/a62af7ec-5c8f-4726-b803-85db852ecff4)
- draw lines automatically over the highest (L,H) cells (after threshold, or topK)

---

cleaned up copy: [multiAdamis1_newAttnPat_draftv2](https://colab.research.google.com/drive/1hIrW3nKX1VbEckouN53OixU5svTONj7w#scrollTo=87Ox9F6ZIAiO).ipynb

the induction patterns are irregular; attneds n-3, then n-7 instead of n-6

Why numdetect heads have non-black first col? Dupl heads have black first col? (not always, such as 0.10)

---

**[Manual rmv from work backw circ](https://colab.research.google.com/drive/1CHRn-AMko9RNrl1bqiCwB7DS-rz1CoBP#scrollTo=0zheHQmPw2Gk&line=1&uniqifier=1)**

If rmv head, is corr answer still in 1st place; if not, what does it fall to?