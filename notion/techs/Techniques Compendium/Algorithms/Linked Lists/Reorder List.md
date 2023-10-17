# Reorder List

[https://www.youtube.com/watch?v=S5bfdUTrKLM&list=PLot-Xpze53leU0Ec0VkBhnf4npMRFiNcB&ab_channel=NeetCode](https://www.youtube.com/watch?v=S5bfdUTrKLM&list=PLot-Xpze53leU0Ec0VkBhnf4npMRFiNcB&ab_channel=NeetCode)

Without extra memory:

reverse the links of the 2nd part of LL

to keep track of which is first and which is second half (of original LL), use slow point (shfit 1) for first and fast pointer (shift 2) for second

GENR: if confused what to do for odd vs even input cases, see what happens to them at the end, then edecide what intr configs get to those end cases from start.

Eg) 1 to 5. Use (4 5) as second half b/c : 1 5 2 4 3: the fast pointer is on 2nd and 4th places, so the fast pointer is only on second half, thus (4 5) is on second half