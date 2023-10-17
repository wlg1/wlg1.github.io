# Balanced Binary Tree

[https://www.youtube.com/watch?v=QfJsau0ItOY&list=PLot-Xpze53ldg4pN6PfzoJY7KsKcxF1jg&ab_channel=NeetCode](https://www.youtube.com/watch?v=QfJsau0ItOY&list=PLot-Xpze53ldg4pN6PfzoJY7KsKcxF1jg&ab_channel=NeetCode)

GENR: to reduce repeated checking of a tree, go bottom up instead of top down

GENR: to check multiple paths, call dfs on each node that starts on a new path

`left, right = dfs(root.left)`, `dfs(root.right)`

[G- To check multiple paths, call dfs on each node](G-%20To%20check%20multiple%20paths,%20call%20dfs%20on%20each%20node%20a528fd6c420c403f860fc31b41d6dd45.md) 

GENR: return all that’s needed from a dfs check

in this case, it’s whether it’s balanced AND the subtree height, use subtree’s root as input to dfs()

[G- return all that’s needed from a dfs check](G-%20return%20all%20that%E2%80%99s%20needed%20from%20a%20dfs%20check%204cc4202debf94fde8e049de8ee054875.md) 

GENR: “balanced” means left, right and root subtrees ALL must be balanced too

---

To translate “the height of the tree is the larger of left or right”, use `max(left,[height], right[height])`