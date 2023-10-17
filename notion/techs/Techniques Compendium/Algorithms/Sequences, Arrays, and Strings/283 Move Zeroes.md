# 283. Move Zeroes

ATTEMPT:

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[i] == 0:
                for j in range(i, len(nums)-1):
                    temp = nums[j]
                    nums[j] = nums[j+1]
                    nums[j+1] = temp
```

The issue with this is that 

---

[https://leetcode.com/problems/move-zeroes/description/?envType=study-plan-v2&envId=leetcode-75](https://leetcode.com/problems/move-zeroes/description/?envType=study-plan-v2&envId=leetcode-75)