# G- dynprog basics

DP Steps:

1. Get key type (sub-problem) and value type (optimal output for that sub-problem)
2. Define base cases of sub-problem (key type); what are their optimal values?
    1. the number of bases cases is the number required for next case to find its value (eg. if requires looking 2 steps behind, then need 2 base cases)
3. Loop over each sub-problem (key type) from bottom-up

---

In other words:

1. Create a new list of values to store for each state (key)
2. Fill in new list with the base cases 
3. Loop through existing structure (of states) and fill in new list starting from base cases

Check for out of boundary cases; Eg) odd vs even cases of 1D array length

[https://leetcode.com/problems/min-cost-climbing-stairs/solutions/773865/a-beginner-s-guide-on-dp-validation-how-to-come-up-with-a-recursive-solution-python-3/?envType=study-plan-v2&envId=leetcode-75](https://leetcode.com/problems/min-cost-climbing-stairs/solutions/773865/a-beginner-s-guide-on-dp-validation-how-to-come-up-with-a-recursive-solution-python-3/?envType=study-plan-v2&envId=leetcode-75)