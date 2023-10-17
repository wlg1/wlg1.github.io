# G- at the start of dfs(), check null nodes

`if not node:`

`# return a "none" value such as 0, "just return", etc.`

This is because leaves will have node.left be = null. This must return before calling node.val or node.left, because those will interact with other types such as integers, so if those return null, it’s incompatible with the operations on integers

Eg) If the output type of dfs is a node, we return node because the return type is a TreeNode (which is a list). This is the unaltered node, which is the “default”.