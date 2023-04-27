# DFS

SOLN: use a stack for unexplored, and a lookup table for explored. Pop from unexplored and check it against some conditions. Add the neighbors of this node that are not in explored to unexplored, and add this node to explored. Continue until all nodes in explored.

Last in, first out