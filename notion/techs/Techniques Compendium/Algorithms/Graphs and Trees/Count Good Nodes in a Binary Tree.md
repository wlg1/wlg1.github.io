# Count Good Nodes in a Binary Tree

[https://www.youtube.com/watch?v=7cp5imvDzl4&list=PLot-Xpze53ldg4pN6PfzoJY7KsKcxF1jg&index=2](https://www.youtube.com/watch?v=7cp5imvDzl4&list=PLot-Xpze53ldg4pN6PfzoJY7KsKcxF1jg&index=2)

X is Good if no nodes from root to X are greater than X

3→1: 1 is not good because 3 (the root) is greater than X

GENR: when checking if X > {set of Y}, only need to check X > max({set of Y})

GENR: remember to account for empty nodes (null) by checking “if not node”, which is True when the node is null

GENR: to check multiple paths, call dfs on each node that starts on a new path

`left, right = dfs(root.left)`, `dfs(root.right)`

[G- To check multiple paths, call dfs on each node](G-%20To%20check%20multiple%20paths,%20call%20dfs%20on%20each%20node%20a528fd6c420c403f860fc31b41d6dd45.md) 

[G- return all that’s needed from a dfs check](G-%20return%20all%20that%E2%80%99s%20needed%20from%20a%20dfs%20check%204cc4202debf94fde8e049de8ee054875.md) 

---

### Code

[G- During certain recursions, add up each case in the return](G-%20During%20certain%20recursions,%20add%20up%20each%20case%20in%20%201c9693b188504ddd89e65d00c2d2ca3f.md) 

```python
def dfs():
	...
	res = 1 if node.val > maxVal else 0 # base case
	...
	# recursive cases
	res += dfs(node.left, maxVal)
	res += dfs(node.right, maxVal)
```

G- if you’re using inequalities, check > vs ≥

G- not all vars must be declared before running a function

[G- at the start of dfs(), check null nodes](G-%20at%20the%20start%20of%20dfs(),%20check%20null%20nodes%2059d306f03ad64affa7e91da6e00cc677.md) 

Here, we return node because the return type is a TreeNode (which is a list). This is the unaltered node, which is the “default”.