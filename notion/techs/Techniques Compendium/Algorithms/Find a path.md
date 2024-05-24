# Find a path

- **Word Search**
    
    [https://www.youtube.com/watch?v=pfiQ_PS1g8E&list=PLot-Xpze53ldBT_7QA8NVot219jFNr_GI&index=9&ab_channel=NeetCode](https://www.youtube.com/watch?v=pfiQ_PS1g8E&list=PLot-Xpze53ldBT_7QA8NVot219jFNr_GI&index=9&ab_channel=NeetCode)
    
    GENR: when need to find a path, use backtracking (dfs)
    
    GENR: to code dfs function, take in position and evaluate if position is goal, invalid, or valid (but not goal). If valid but not goal, add to path cand and continue recursion by dfs(next pos) of ALL POSS next actions from curr pos
    
    GENR: the path is the ‘to visit’ list. add to path to visit that pos, but once visited, REMEMBER TO REMOVE THE POS
    
    GENR: if the path can start from any pos, then run dfs on every pos until either find exists (just return True) or find every poss path (then need to run on all valid starting positions)