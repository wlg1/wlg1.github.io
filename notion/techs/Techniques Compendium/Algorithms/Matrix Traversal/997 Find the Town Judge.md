# 997. Find the Town Judge

[G- interactions → transform to graph](G-%20interactions%20%E2%86%92%20transform%20to%20graph%20ee9fbda73aad4450841ee7efc757274e.md) 

A → (trusts) B

---

[https://stackoverflow.com/questions/29259365/how-to-find-the-universal-sink-of-a-directed-graph-with-an-adjacency-matrix-repr](https://stackoverflow.com/questions/29259365/how-to-find-the-universal-sink-of-a-directed-graph-with-an-adjacency-matrix-repr)

If k is an universal sink, then the k-th row of the adjacency-matrix ( G ) will be all 0s, and the k-th column will be all 1s (except G[k][k] = 0).

[https://www.geeksforgeeks.org/determine-whether-universal-sink-exists-directed-graph/](https://www.geeksforgeeks.org/determine-whether-universal-sink-exists-directed-graph/)

A ‘1’ at `adjmat[r][c]` means there’s an outgoing edge from r into c (or, an ingoing edge into c). Because sinks cannot have outgoing edges, any node (row) with a ‘1’ cannot be a sink. Thus, if it has a ‘1’, we check the next row.

If it is a 0, AND r ≠ c, it means that the vertex corresponding to index c cannot be a sink.

After finding a row with no 1s, check its index on the col to see if it’s all 1s except at r=c. If so, then it’s a sink.

This is O(n + m)

---

- This doesn’t work (correct it later)
    
    ```python
    class Solution:
        def findJudge(self, n: int, trust: List[List[int]]) -> int:
            # adjmat = [[0]*n]*n  # can't do this bc all rows will be updated the same when one row is
            adjmat = [n * [0] for i in range(n)]
            for reln in trust:
                adjmat[reln[0]-1][reln[1]-1] = 1
            print(adjmat)
    
            curr_row = 0
            for col in range(len(adjmat)):
                if adjmat[curr_row][col] == 1:
                    curr_row += 1
                if col == len(adjmat[0]) - 1:  # reached last col w/o down
                    # check if curr_row is sink
                    checkRows = True
                    for col in range(len(adjmat)):
                        if adjmat[curr_row][col] == 1:
                            curr_row += 1
                            checkRows = False
                            break
                    if checkRows == False:
                        break
                    for row in range(len(adjmat)):
                        if row != curr_row: 
                            if adjmat[row][curr_row] == 0:
                                curr_row += 1
                                break
                    return curr_row
            return -1
    ```
    

Correct:

```python
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1

        cand_judges = {i:[] for i in range(1,n+1)}  # list of ppl who trust i
        for reln in trust:
            if reln[0] in cand_judges: # it has out going E
                del cand_judges[reln[0]]
            if reln[1] in cand_judges and reln[0] != reln[1]:
                cand_judges[reln[1]].append(reln[0])
        for cand, lst_in in cand_judges.items():
            if len(lst_in) == n-1:
                return cand
        return -1
```