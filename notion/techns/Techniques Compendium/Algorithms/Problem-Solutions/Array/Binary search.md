# Binary search

### Sub Problem

Prob: how to choose new index of binary search?

SOLN: if middle is less than target, must search bigger values on the right. So left is now left of middle. Left = mid + 1. Likewise, if less, then right=mid-1