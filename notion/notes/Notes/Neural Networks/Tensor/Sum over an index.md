# Sum over an index

```python
# 3 rows, 4 columns
tensor = torch.tensor(
[[1, 2, 3, 4], 
[5, 6, 7, 8], 
[9, 10, 11, 12]])

row_sum = tensor.sum(dim=0) 
# tensor([15, 18, 21, 24])
```

![Untitled](Sum%20over%20an%20index%208e5f325c799447948ab6fc98514a56ea/Untitled.png)

AND 1 ROW. Thus, (dim = 0) ↔ (1 row)

<<<

```python
column_sum = tensor.sum(dim=1) # Sum over the column index (dim=1)
# tensor([10, 26, 42])
```

4 columns disappear, left with 3 rows and 1 COL

![Untitled](Sum%20over%20an%20index%208e5f325c799447948ab6fc98514a56ea/Untitled%201.png)

<<<

Sum the first and third rows

**`tensor[0, :] + tensor[2, :]` —> `tensor([10, 12, 14, 16])`**

OR: `sum_rows = tensor[[0, 2], :].sum(dim=0)`

![Untitled](Sum%20over%20an%20index%208e5f325c799447948ab6fc98514a56ea/Untitled%202.png)

<<<

Sum the first and second columns element-wise 

**`tensor[:, 0] + tensor[:, 1]` —>**  `tensor([ 3, 11, 19])`

![Untitled](Sum%20over%20an%20index%208e5f325c799447948ab6fc98514a56ea/Untitled%203.png)

<<<

Add all rows, but only keep first and third columns

`tensor.sum(dim=0)[[0, 2]]` `—> tensor([15, 21])`

![Untitled](Sum%20over%20an%20index%208e5f325c799447948ab6fc98514a56ea/Untitled%204.png)