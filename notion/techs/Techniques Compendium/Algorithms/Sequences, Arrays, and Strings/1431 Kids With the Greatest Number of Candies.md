# 1431. Kids With the Greatest Number of Candies

[GP- To avoid nested loops, add separate loops](GP-%20To%20avoid%20nested%20loops,%20add%20separate%20loops%2082da24b9d22149cfbd5982d5082f6e06.md) 

```python
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCand = 0
        for i in candies:
            if i > maxCand:
                maxCand = i

        return [(cand + extraCandies >= maxCand) for cand in candies]
```