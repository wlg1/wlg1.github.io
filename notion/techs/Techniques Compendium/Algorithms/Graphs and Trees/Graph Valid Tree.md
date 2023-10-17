# Graph Valid Tree

[https://www.youtube.com/watch?v=bXsUuownnoQ&list=PLot-Xpze53ldBT_7QA8NVot219jFNr_GI&index=13&ab_channel=NeetCode](https://www.youtube.com/watch?v=bXsUuownnoQ&list=PLot-Xpze53ldBT_7QA8NVot219jFNr_GI&index=13&ab_channel=NeetCode)

[G- To find if there’s a subgraph (eg, tree), use DFS ](G-%20To%20find%20if%20there%E2%80%99s%20a%20subgraph%20(eg,%20tree),%20use%20D%2041d59fb9f7a649d7b1b9d7957060f8de.md) 

[G- to check if there’s a cycle, check neigh visits](G-%20to%20check%20if%20there%E2%80%99s%20a%20cycle,%20check%20neigh%20visits%20fb8938ef1d854c41a4daef60f77b3dd6.md) 

GENR PROB: beware that when checking loops, when a node goes back to another due to backtracking, it will go back to a visited- this is a false positive of a cycle if each node pair only has 1 edge type. 

SOLN: keep track of the prev node (relative to curr node). don’t check if any of curr’s neighbors that ARE prev are in visited; check if any of curr’s neighbors that aren’t prev are in visited

GEN PROB: how to code this?

SOLN: after adding prev to visited, don’t run dfs on it