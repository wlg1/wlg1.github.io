# Maximum Subarray

GENR PROB: How to sum subarrays?

SOLN 1: 3 nested loops- start, end, sum over. The 2nd nested loop starts from the current index i of the first. O(n^3) time

- code
    
    ![Untitled](Maximum%20Subarray%201622b28e7d6b460f83ffd94b9f10d205/Untitled.png)
    

SOLN 2: Keep the running sum over the 2nd loop’s elements so far, and just add the new element to it. This gets rid of 3rd loop, so O(n^2) time

WHY: Iterating over [a_i, … , a_j] in the 2nd loop is repeated in the 3rd loop, so memoize it

- code
    
    ![Untitled](Maximum%20Subarray%201622b28e7d6b460f83ffd94b9f10d205/Untitled%201.png)
    

---

SOLN 3: Use a sliding window. Takes O(n) time.

When taking sums to find a max, negative values don’t matter. So don’t even consider them if they’re at the start. If contiguous (consecutive), eliminate values from the start to the negative value’s index if the sum is negative, since the next number will either be less (and thus also eliminated) or be positive (and thus always greater, so we just start at the next one instead). 

GENR: Sliding Window- This is similar to how SOLN 2 eliminated the third loop. Here, we eliminate the first loop because we can ALSO shift (or ‘move up’) our starting index once we find a BETTER STARTING INDEX. This means not only are we moving the end pointer, we are moving the start pointer to ‘slide the location and size of the window’.

The window is the subarray we want to output, though it doesn’t always have to be outputted; it can be any sub-structure whose boundaries we shift as we traverse, thus requiring less traversals instead of needing to repeat traversals 

GENR: Need to find linear traversal of array → Try two pointers

GENR: Need to find linear traversal of array → Try sliding window (type of two pointers)

GENR: instead of guessing current max value say using -inf (which could be out of range), when traversing, use the first element of the array to have something within range of the possible values

PROB: not sure if the initial best guess “so far” is out of range

SOLN: use something in the array as initial best guess

GENR: you don’t need the indices of the sliding window when only the sum matters, because you can just discard the entire sum by resetting it (`currsum = 0`) and starting to compute from the “current best” index right now. This current best is implicit upon reset.

summary- We don’t need to return the indices, just the sum. 

- code to SOLN 3:
    
    ![Untitled](Maximum%20Subarray%201622b28e7d6b460f83ffd94b9f10d205/Untitled%202.png)
    

### Attempts

---

```
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                sum = 0
                for k in range(i, j+1):
                    sum += nums[k]
                if sum > maxsum:
                    maxsum = sum
        return maxsum
```

The reason j is not from range(i+1, len(nums)) is because there are cases where the max sum is just one element, not two elements. So the index of i and j would be the same.

<<<

This is not correct yet because it forgos negatives. Need to change initial maxsum to `maxsum = -10000`

<<<

Then, this O(N^3) exceeds the time limit, so optimize it

---

```
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = -10000
        for i in range(len(nums)):
            sumSoFar = 0  # each time start new i, need new sumSoFar
            for j in range(i, len(nums)):
                sumSoFar += nums[j]
                if sumSoFar > maxsum:
                    maxsum = sumSoFar
        return maxsum
```

This doesn’t pass every case; time limit exceeded

---

In sliding window, when do you shift the start index?

When start index “makes it worse”

Because we’re trying to find max sum, this means negative

Move start up if sumSoFar < num[end]

nums[end] is the current subarray endpt, which is the current num