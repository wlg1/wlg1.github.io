# Merge Two Binary Trees

[https://www.youtube.com/watch?v=QHH6rIK3dDQ&list=PLot-Xpze53ldg4pN6PfzoJY7KsKcxF1jg&index=4](https://www.youtube.com/watch?v=QHH6rIK3dDQ&list=PLot-Xpze53ldg4pN6PfzoJY7KsKcxF1jg&index=4)

G- we cannot alter an existing data structure, so we must create a new one inside each case and return it to a higher level

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
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node1, node2):
            newNode = TreeNode()
            if not node1 and not node2:
                return None
            if not node1:
                newNode.left = dfs(None, node2.left)
                newNode.right = dfs(None, node2.right)
                newNode.val = node2.val
            if not node2:
                newNode.left = dfs(node1.left, None)
                newNode.right = dfs(node1.right, None)
                newNode.val = node1.val
            if node1 and node2:
                newNode.left = dfs(node1.left, node2.left)
                newNode.right = dfs(node1.right, node2.right)
                newNode.val = node1.val + node2.val
            return newNode

        return dfs(root1, root2)
```