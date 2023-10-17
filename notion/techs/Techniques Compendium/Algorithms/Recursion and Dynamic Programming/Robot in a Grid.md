# Robot in a Grid

### Problem

Imagine a robot sitting on the upper left corner of grid with r rows and c columns.
The robot can only move in two directions, right and down, but certain cells are "off limits" such that the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to the bottom right.

### Reasoning

Let the index of rows be called v, and the index of columns be called h. We want to get to (r, c). We can find (r, c) from (r-1, c) or (r, c-1). In general, we can find (v, h) from (v-1, h) or (v, h-1). Store the path in a dynamic array ArrayList. 

### Generalize

Gen: [Use previous steps to find a step](../Techniques%204144140dcb42461fba9223a7a967195d/Use%20previous%20steps%20to%20find%20a%20step%20ec8e60950d954e189a1b648b48fd6ee8.md)