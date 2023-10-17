# 12. Integer to Roman

[https://www.youtube.com/watch?v=ohBNdSJyLh8&ab_channel=NeetCode](https://www.youtube.com/watch?v=ohBNdSJyLh8&ab_channel=NeetCode)

Roman numerals:

- Largest to smallest (MD is 1000 + 500)
- But if smallest to largest, there are six instances where subtraction is used

GENR:

ISSUE: How many times can Y go into X?

SOLN: Integer division

<<<

Without special cases (small to large) you just need to divide the integer by each symbol, from largest to smallest.

All you need to do is to for special cases is to insert them as symbols in the division order list, too. So integer div by M, then DM, etc.