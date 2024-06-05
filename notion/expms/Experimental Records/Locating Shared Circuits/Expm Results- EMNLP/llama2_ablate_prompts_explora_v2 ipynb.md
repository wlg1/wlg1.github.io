# llama2_ablate_prompts_explora_v2.ipynb

[https://colab.research.google.com/drive/1LPw0da125JQy1qm7nGOFbGwwdO_Fz62M](https://colab.research.google.com/drive/1LPw0da125JQy1qm7nGOFbGwwdO_Fz62M)

Concat tokens (not retokenize from adding to string)

uses zero ablation

1234

- If we remove top 50 heads from numbers, STILL gives correct answer
    - lots of backups for this common sequence?

2 4 6

- If we remove top 50 heads from 1234 circ, says 7 instead of 8
    - if do this rand (x3), it gives corr answer
    - also works with top 40, but not heads 30 to 40. So these top 40 somehow work together
    - we should try random that ISN’T from the top 50 heads
- if we rmv top 40 heads from 246, it still works

10 12 14

- If we remove top 50 heads from 1234 circ, says 10 instead of 16
    - if do this rand (x3), it gives corr answer
    - also works with top 40, but not heads 30 to 40. So these top 40 somehow work together
- if we remove top 50, it outputs 10. If we remove only top 40, it outputs 15.
- if we rmv top 40 heads from 246, it still works

21 23 25

- removing top 50 and 40 also destroys this. it makes 20, or 22. this suggests overlaps between 123 and 246, even though this isn’t obvious (their top 50 heads are somewhat different)
- random doesn’t work
    - [but sometimes it does if it CONTINUES generating](https://colab.research.google.com/drive/1LPw0da125JQy1qm7nGOFbGwwdO_Fz62M#scrollTo=uemHL8P9uLGk&line=3&uniqifier=1)
        
        ![Untitled](llama2_ablate_prompts_explora_v2%20ipynb%20034368629f3e40869a4bc34a49180a49/Untitled.png)
        
- if we rmv top 40 heads from 246, it repeats 25

3 6 9

- If we remove top 30 or 50 heads from 1234 circ, says 10 instead of 12
    - if do this rand (x3), it gives corr answer

**100 200 300**

- top 50: 100 200 300 300
    - random doesn’t work. neither does top 40.

uno dos tres

- note that the clean run fails after “seis”, so we’re only measuring cuatro to seis
    
    Sequence so far: uno dos trescuatro
    5th char = 'cuatro'
    Sequence so far: uno dos trescuatrocinco
    6th char = 'cinco'
    Sequence so far: uno dos trescuatrocincoseis
    7th char = 'seis'
    Sequence so far: uno dos trescuatrocincoseisseven
    8th char = 'seven'
    Sequence so far: uno dos trescuatrocincoseisseveneight
    9th char = 'eight'
    Sequence so far: uno dos trescuatrocincoseisseveneightnine
    10th char = 'nine'
    Sequence so far: uno dos trescuatrocincoseisseveneightnineten
    
- 20.17 (top head of 1234) is enough to destory
- HOWEVER, random 50 is also enough to destroy. So this is a very sensitive prompt
- BUT random “1 head” is NOT enough to destroy. But 10 often is enough.
    - 10 that destorys
        
        ```
        [(17, 27),
         (16, 15),
         (4, 16),
         (16, 25),
         (0, 23),
         (18, 10),
         (27, 3),
         (9, 6),
         (9, 7),
         (14, 8)]
        ```
        
        The only overlap with top50 1234 is 14.8
        
- 14.8 by itself destroys seis. So in conjunction with some others (there are multiple combos) it can destroy cuatro. Note that 14.8 isn’t in top 50 for spanish cont circs
    
    Sequence so far: uno dos trescuatro
    5th char = 'cuatro'
    Sequence so far: uno dos trescuatrocinco
    6th char = 'cinco'
    Sequence so far: uno dos trescuatrocinco<0x0A>
    7th char = '<0x0A>'
    Sequence so far: uno dos trescuatrocinco<0x0A><0x0A>
    8th char = '<0x0A>'
    Sequence so far: uno dos trescuatrocinco<0x0A><0x0A><0x0A>
    9th char = '<0x0A>'
    Sequence so far: uno dos trescuatrocinco<0x0A><0x0A><0x0A><0x0A>
    10th char = '<0x0A>'
    

What are the months in a year?

Ablate top heads found by [Llama2_JanFebMar](https://colab.research.google.com/drive/1xRkMdXy32WeCyKWEkjd296kd8e5plk1J#scrollTo=susSZdqpqVzd).ipynb, then test:

RESULTS: 

- Ablating all the heads does change things.
- If ablate the top 7 heads from [https://colab.research.google.com/drive/1xRkMdXy32WeCyKWEkjd296kd8e5plk1J#scrollTo=susSZdqpqVzd&line=1&uniqifier=1](https://colab.research.google.com/drive/1xRkMdXy32WeCyKWEkjd296kd8e5plk1J#scrollTo=susSZdqpqVzd&line=1&uniqifier=1) , doesn’t change anything.
- The top 50 heads don’t work either. (either from months or nums circ)
- head_to_remove = head_to_remove_num + head_to_remove_months: this does allow it to say jan then REPEATS jan, but it’s probably because it’s destroying 10% of the heads (1024 attention heads in llama-2)
    - but this also works for the top 20 heads from each!
    - but if we ablate 100 random heads and run this twice, sometimes it generates nonse it still allows completion. so perhaps it’s onto something.
- it appears the hypothesis that the seqcont circuits affect reasoning are wrong, unless there are backups?
    - “jan feb mar” ALSO doesn’t get destroyed by removing (23, 17), but it DOES get destroyed when removing the top 50 heads.

What are the days of the week?