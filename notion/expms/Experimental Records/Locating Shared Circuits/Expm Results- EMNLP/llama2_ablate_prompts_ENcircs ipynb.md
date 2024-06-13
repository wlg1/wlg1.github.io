# llama2_ablate_prompts_ENcircs.ipynb

[https://colab.research.google.com/drive/153kKQsYcBNo1sR0dVhM6c9vxDOhXhhCN#scrollTo=54lN0z-DekER](https://colab.research.google.com/drive/153kKQsYcBNo1sR0dVhM6c9vxDOhXhhCN#scrollTo=54lN0z-DekER)

zero ablation

singleTok circs

ablate attn heads only

ablate all pos

### Seq Cont

- 1 2 3
    
    Works:
    
    - nums
    - nw
    - months
    
    Doesn’t:
    
    - intersect all
- 2 4 6
    
    Works:
    
    - nums
    - nw
    - months
    
    Doesn’t:
    
    - intersect all

### Word Problems

- "Be concise. If today is the 11th of a month, what date will it be in 6 days?”
    
    Works:
    
    - nums
    - nw
    - months
    
    Doesn’t:
    
    - intersect all
    - random (100, with less than 50 overlap from union all, which is 172)
- What are the months in a year? Give all of them as a list.
    
    Works:
    
    - months
    
    Doesn’t:
    
    - nums
    - nw
    - intersect all
    - random (100, with less than 50 overlap from union all, which is 172)
- What are the months in a year? Give all of them as a list. Be concise.
    
    Works:
    
    - nums
    - nw
    - months
    
    Doesn’t:
    
    - intersect all
    - random (100, with less than 50 overlap from union all, which is 172)
- The months in a year are: January,
    
    Works:
    
    - nw
        - omits july
    - months
        - repeats some
    
    Doesn’t:
    
    - nums
    - intersect all
    - random (100, with less than 50 overlap from union all, which is 172)
- Be concise. If this month is September, and 3 months pass, what is month name is it? Answer: December. If this month is March, and 3 months pass, what month name is it? Answer:
    
    Works:
    
    - nw
    - months
    
    Doesn’t:
    
    - nums
    - intersect all
    - random (100, with less than 50 overlap from union all, which is 172)
- Be concise. If this month is July, and 5 months pass, what is month name is it? Answer: December. If this month is April, and 5 months pass, what month name is it? Answer:
    
    Works:
    
    - intersect all
    - nums
    - nw
    - months
    
    Doesn’t:
    
    - random (100, with less than 50 overlap from union all, which is 172)
- Be concise. If this month is July, and 2 months pass, what is month name is it? Answer: September. If this month is September, and 2 months pass, what month name is it? Answer:
    
    Works:
    
    - nums
    - nw
    
    Doesn’t:
    
    - intersect all
    - months
    - random (100, with less than 50 overlap from union all, which is 172)
- Be concise. If this month is July, and 2 months pass, what month name is it? Answer: September. If this month is September, and 2 months pass, what month name is it? Answer:
    
    Works:
    
    - nums
    - nw
    - months
    - random (100, with less than 50 overlap from union all, which is 172)
    
    Doesn’t:
    
    - intersect all
- Be concise. If this month is July, and 4 months pass, what month name is it? Answer: October. If this month is April, and 4 months pass, what month name is it? Answer:
    
    Works:
    
    - nums
    - nw
    - months
    
    Doesn’t:
    
    - intersect all
    - random (100, with less than 50 overlap from union all, which is 172)
- Be concise. What are all the months in Fall? List them in order.”
    
    Works:
    
    - nw
    
    Doesn’t:
    
    - intersect all
    - nums
    - months
    - random (100, with less than 50 overlap from union all, which is 172)
- What are all the months in Winter? List them in order. Answer:
    
    Works:
    
    - nw
    - months
    - random (100, with less than 50 overlap from union all, which is 172)
    
    Doesn’t:
    
    - intersect all
    - nums
- What is the month that is 3 months after January? Answer: March. What is the month that is 3 months after March? Answer:
    
    Works:
    
    - nw
    - months
    - random (100, with less than 50 overlap from union all, which is 172)
    
    Doesn’t:
    
    - intersect all
    - nums
- Answer yes or no. Is 16 greater than 11? Answer:
    
    Works:
    
    - nums
    - months
    
    Doesn’t:
    
    - intersect all
    - nw
    - random (100, with less than 50 overlap from union all, which is 172)
- Be concise. What number is greater than 11? Answer:
    
    Works:
    
    - nums
    - nw
    - months
    
    Doesn’t:
    
    - intersect all
    - random (100, with less than 50 overlap from union all, which is 172)

### Arithmetic

- "5 + 16 = “
    
    Works:
    
    - nw
    - months
    
    Doesn’t:
    
    - nums
    - intersect all
    - random (100, with less than 50 overlap from union all, which is 172)
- Be concise. 100 + 58 =
    
    Works:
    
    - nums
    - nw
    - months
    
    Doesn’t:
    
    - intersect all
    - random (100, with less than 50 overlap from union all, which is 172)
- 5 x 6 =
    
    Works:
    
    Doesn’t:
    
    - nums
    - nw
    - months
    - intersect all
    - random (100, with less than 50 overlap from union all, which is 172)
- 2 x 2 =
    
    Works:
    
    - months
    
    Doesn’t:
    
    - nums
    - nw
    - intersect all
    - random (100, with less than 50 overlap from union all, which is 172)