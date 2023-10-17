# 198. House Robber

REASONING:

[G- create a decision function](G-%20create%20a%20decision%20function%2047038185014d470c8d2b7038422d1522.md) 

Decision function criteria:

1. The value, obtained by recursive function, is: add values of selected elements (robbed houses)
    
    # key type: house number
    # value type: money from robbing all houses starting from this house number to the end of array
    
2. Because you must skip the next house, the sub-problem is to find the max of all houses AFTER the next house.
3. The decisions from a node are: 
    
    1) Rob current house (thus get sub-prob for all others houses except next)
    
    2) Rob next house (thus get sub-prob for all others houses)
    

Thus, the equation is: 

`rob(i) = max(arr[i] + rob(arr[i+2:n]), rob(arr[i:n]) )`

That is recursive. To convert to DP:

```python
if i > 2:
    dp[i] = nums[i] + max(dp[i - 2], dp[i - 3])
else:  # i == 2
    dp[i] = nums[i] + dp[i - 2]
```

The next case (i==2) just adds current value in house to optimal solution 2 houses ago. It cannot get 3 houses ago.

ALTERNATIVE (most aligned w/ description):

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        # key type: house number
        # value type: money from robbing all houses starting from this house number to the end of array
        n=len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        dp = [0]*n

        #base cases
        dp[0] = nums[0]
        dp[1] = nums[1]

        # solve sub-problems
        for i in range(2,n):
            dp[i] = max(nums[i] + max(dp[i-2], dp[i-3]), dp[i-1])
        return dp[n-1]
```

The reason we use i-3 is take this case:

[2, 1, 1, 2]

To determine the best value (dp) at the 3rd:

We can choose the 0th or 1st index. Choosing the 0th means we DON’T NEED to choose the 2nd, but can choose the 3rd. Choosing the 1st means we must choose the 3rd. Thus, if we choose the 3rd, we either chose the 0th or 1st. 

But we can only choose what was best at the 2nd (`dp[i-1]`) or the 3rd (nums[i]).

---

[G- dynprog basics](G-%20dynprog%20basics%205e43cf2acad948a4b2633959f1dbb90c.md)