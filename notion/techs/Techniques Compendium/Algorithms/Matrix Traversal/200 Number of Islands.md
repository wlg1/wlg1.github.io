# 200. Number of Islands

[https://www.youtube.com/watch?v=pV2kpPD66nE&ab_channel=NeetCode](https://www.youtube.com/watch?v=pV2kpPD66nE&ab_channel=NeetCode)

To find an island, start at a 1, then check its neighbors. Once finish checking its neighbors, check neighbors of neighbors. Stop when all “next” neighbors are 0s. This is BFS.

![Untitled](200%20Number%20of%20Islands%204376a3b7361b4eeb9e45e922e2038b5f/Untitled.png)

BFS will mark nodes it encounters as “visited”. So after BFS, when start traversing nodes col by col and row by row again, any new “1” node that hasn’t been visited yet is considered a new island; else, since BFS must visit every node connected to a visited “1”, BFS would’ve visited it.

The queue in BFS stores what needs to be visited still. Add “1” neighbors to the queue iteratively (not recursively)

BFS uses q.popleft() ; DFS just uses q.pop() and the same code as BFS