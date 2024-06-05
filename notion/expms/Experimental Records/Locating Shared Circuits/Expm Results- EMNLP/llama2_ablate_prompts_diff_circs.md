# llama2_ablate_prompts_diff_circs

[llama2_ablate_prompts_diff_circs.ipynb](https://colab.research.google.com/drive/19gD4cjwQvbtU0g5GiOJRVyGaZhLpIevv#scrollTo=HYIdJj637K7f)

intersect_all has only 5 heads, so that shouldn’t work

But intersect_en_nw_months doesn’t work well either

**Be concise. If today is the 11th of a month, what date will it be in 6 days?**

Works:

- nw circ

Doesn’t work:

- top 10 nw circ heads
- random 10 (most of the time)

"5 + 16 = “

Works:

- nw circ

Doesn’t work:

- top 10 nw circ heads
- random 10 (most of the time)
- random 100 (most of the time)

**Be concise. 100 + 58 =**

Works:

- nw circ

Doesn’t work:

- random 100 (most of the time)

5 x 6 = 

Works:

- 

Doesn’t work:

- nw circ
- random 100 (most of the time)

2 x 2 = 

Works:

- 

Doesn’t work:

- nw circ
- random 100 (most of the time)

Be concise. In a cyclic pattern of colors: Red, Blue, Green, Yellow, what color comes after Green in the 3rd cycle?

Works:

- 

Doesn’t work:

- nw circ
- random 100 (most of the time)