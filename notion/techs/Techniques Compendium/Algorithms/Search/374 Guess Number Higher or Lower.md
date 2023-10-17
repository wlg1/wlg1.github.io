# 374. Guess Number Higher or Lower

[https://leetcode.com/problems/guess-number-higher-or-lower/description/?envType=study-plan-v2&envId=leetcode-75](https://leetcode.com/problems/guess-number-higher-or-lower/description/?envType=study-plan-v2&envId=leetcode-75)

SOLN:

```python
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        def binarySearch(l, h):
            mid = (l + h)//2
            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1:
                return binarySearch(l, mid-1)
            elif guess(mid) == 1:
                return binarySearch(mid+1, h)

        return binarySearch(1, n)
```

---

REASONING:

The hard part is figuring out what to give to guess. At first, it seems to be a pre-defined variable like num or pick. But those don’t work. So describe the problem about what NUMBER to give FIRST given 1 to n.

You don’t give 1, nor n. In binary search, you give mid. So take (1+n) //2

However, you can’t ALWAYS take 1 and n. At each recursive level, you need l and h. But the given function doesn’t have those args, and you can’t change them in leetcode. So you must create a new recursive function, binarysearch(l,h).

Afterwards, it’s straightforward binary search that returns the answer as its base case.