# Months circuit

[months_mincirc_repeatLast.ipynb](https://colab.research.google.com/drive/12njjS49F5Tl1cyfaaOXvXlMKYI7z3lfZ#scrollTo=dzzLlCqZS_wl)

When we use the digits circuit (~40 heads), this gets to 119%. But the prune backw method at 3% threshold allows to find a smaller circuit:

`[(0, 1), (0, 5), (1, 5), (2, 3), (2, 9), (2, 11), (4, 4), (9, 1), (10, 7)]`

Which was not possible for digits, even just using the dataset of 1 to 11 (overlapping).

- compare this to digits (prune backw once)
    
    `[(0, 1), (0, 3), (0, 5), (0, 7), (0, 9), (0, 10), (1, 0), (1, 5), (2, 2), (2, 9), (3, 0), (3, 3), (3, 7), (4, 4), (4, 7), (4, 8), (4, 10), (5, 1), (5, 4), (5, 5), (5, 6), (5, 8), (5, 9), (5, 10), (6, 1), (6, 3), (6, 4), (6, 6), (6, 10), (7, 2), (7, 6), (7, 10), (7, 11), (8, 8), (9, 1), (10, 7)]`
    

Only (2,3) and (2,11) in months aren’t present

Why does digits need to be bigger to handle this? is it because it’s LESS PREDICTABLE?

- compare to greater-than
    
    `[(0, 1), (0, 3), (0, 5), (5, 5), (6, 1), (6, 9), (7, 10), (8, 11), (9,1)]`
    

Months is missing induction, and L6 to 8; neither is a sub-circuit of the other, but there is considerable overlap.

Question is- are the overlaps doing the same thing in each? 9.1 seems to be. But what early heads like 0.1 and 0.5? Are they “number detection” heads? 

Try prune backw using 0% threshold. Do we hypo it would be really small, or really big (like the digits circuit?)

`[(0, 1), (0, 5), (0, 10), (1, 0), (1, 1), (1, 5), (2, 2), (2, 10), (2, 11), (3, 10), (4, 4), (5, 1), (9, 1), (10, 7), (11, 0)]`

It’s actually really small.

Which circuits allow months continuation to be calculated? What are the most crucial heads?

Clearly 9.1 by itself can’t work?