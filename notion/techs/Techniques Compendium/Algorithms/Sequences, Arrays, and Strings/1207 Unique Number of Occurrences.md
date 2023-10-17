# 1207. Unique Number of Occurrences

```python
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = {}
        for i in arr:
            if i in counts.keys():
                counts[i] += 1
            else:
                counts[i] = 1
        return len(counts.values()) == len(list(set(counts.values())))
```