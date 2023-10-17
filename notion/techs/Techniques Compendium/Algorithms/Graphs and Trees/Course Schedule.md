# Course Schedule

ISSUE: [https://leetcode.com/problems/course-schedule/](https://leetcode.com/problems/course-schedule/)

SOLN: Make a graph of prereqs (tail→ head : head is a prereq of tail). Recursively stack in prereqs until you get to one you can take out (a sink). Then you can take that one out of the rest. If all nodes have empty list (in adj list), then all courses can be completed.

Keep visit set to detect loop. If there is loop, return false

O(n+p), p =# prereqs, because 

<<<

GENR. ISSUE: How to detect loop?

SOLN: Keep visit set to detect loop during traversal. If already visited, is loop.

GENR ISS: How to check if all dependencies met?

SOLN: Graph. Each dependency is a head node, and check if all can be reachable w/o loops

GENR ISS: How to check if node is reached?

SOLN: Keep list of to-reach, and remove if reached