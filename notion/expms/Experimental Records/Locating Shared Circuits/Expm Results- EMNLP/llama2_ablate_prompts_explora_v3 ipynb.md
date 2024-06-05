# llama2_ablate_prompts_explora_v3.ipynb

Uses top 50 from 1234 of 12 **multi prompts** Llama2_numerals.ipynb. Note the prompt dict pos doesn’t matter here?

1 2 3 4

- top 20 from nums and months destroys it
    - **this is in contrast to the single prompt circ from v2**
- top 50 doesn’t

2 4 6

- top 50 from nums destroys it

10 12 14

- top 50 from nums destroys it

Same for: 3, 6 9 ; 100 200 300

**"What comes after Monday is Tuesday, and two days after is"**

- top 50 from nums destroys it.
    - Random doesn’t
    

**What are the months in a year?**

- top 50 doesn’t work
- top 20 mix from numseq and months DOES make it destroy it initially, but if it keeps going, it eventually WILL have feb mar etc
    
    In contrast, the top 20 from the single prompt will destroy it even if it keeps going
    

Jan feb mar

- top 50 from nums destroys it.