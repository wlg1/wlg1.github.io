# Invert Binary Tree

[https://leetcode.com/problems/invert-binary-tree/](https://leetcode.com/problems/invert-binary-tree/)

[G- at the start of dfs(), check null nodes](G-%20at%20the%20start%20of%20dfs(),%20check%20null%20nodes%2059d306f03ad64affa7e91da6e00cc677.md) 

---

SOLN:

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return node
            tempLeft = node.left
            node.left = node.right
            node.right = tempLeft
            dfs(node.left)
            dfs(node.right)
            return node
        return dfs(root)
```