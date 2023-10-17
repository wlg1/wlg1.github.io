# Generate parentheses

SOLN: Use [Backtracking](../Techniques%204144140dcb42461fba9223a7a967195d/Backtracking%202daae08cd4ce4dccb6063e93a56f370e.md) 

- THOUGHT PROCESS:
    
    There are multiple items to output that build on each other. When this happens, you have states building to future states. If you have dead ends, you should use backtracking to avoid computing even more dead end states. Let's use examples to find if there are dead ends.
    
    ()(()) is valid
    
    …
    
    By examples, we see a dead end is a (
    
    Use [Backtracking](../Techniques%204144140dcb42461fba9223a7a967195d/Backtracking%202daae08cd4ce4dccb6063e93a56f370e.md)  because dead end states cannot lead to future valid states.
    

---

### GEN

PROB: Generate states such that states can build to new states using branching actions, some which are dead ends according to what's valid

SOLN: Use [Backtracking](../Techniques%204144140dcb42461fba9223a7a967195d/Backtracking%202daae08cd4ce4dccb6063e93a56f370e.md). 

HOW: Map the item configurations to a state space.