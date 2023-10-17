# Triple Step

### PROBLEM

A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3
steps at a time. Implement a method to count how many possible ways the child can run up the stairs.

### Reasoning

Each step can be found from a previous step. For example, getting to step 8 means you can hop from either step 7, 6, or 5. So the number of ways to get to step 8 is just (number ways to get to step 7) +  (number ways to get to step 6) +  (number ways to get to step 5). 

Let the function W(N) be the number of ways to get to N. Then:

W(N) = W(N-1) + W(N-2) + W(N-3)

To use memoization, store every solved step N in a hash table Memo[N]. Then instead of re-solving for say, step 6 or step 5 every time you need it, you just look it up.

---

### GENERALIZATIONS

---

Gen: If getting to index N can be found by going from indices in set P, which contains previous indices, then the number of ways to get to index N are found by adding up the number of ways to get to index p for every index p in set P. 

Keywords: get to, steps

Page: [Use previous steps to find a step](../Techniques%204144140dcb42461fba9223a7a967195d/Use%20previous%20steps%20to%20find%20a%20step%20ec8e60950d954e189a1b648b48fd6ee8.md) 

---

Ref: Cracking the Coding Interview