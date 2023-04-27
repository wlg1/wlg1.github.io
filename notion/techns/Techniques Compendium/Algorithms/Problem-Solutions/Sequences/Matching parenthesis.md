# Matching parenthesis

SOLN: use a stack to keep track of left parentheses, removing one only if find matching right parentheses. If stack empty at end of traversal, return true

For case of illegal right parentheses, if no left parentheses then stack is empty. So if it's empty AND encounter a ), return false

---

SOLN: use a counter for left parenthesis. If find left, +1. If find right, -1. If 0 at end of traversal, return true