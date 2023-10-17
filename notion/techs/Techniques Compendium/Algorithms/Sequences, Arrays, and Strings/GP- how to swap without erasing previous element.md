# GP- how to swap without erasing previous element

```python
temp = nums[ptr_2]  # keep it
nums[ptr_2] = nums[ptr_2-1]  # change it
nums[ptr_2-1] = temp # the other uses what was kept
```