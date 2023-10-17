# Unique Paths - Dynamic Programming - Leetcode 62

[https://www.youtube.com/watch?v=qMky6D6YtXU&ab_channel=NeetCode](https://www.youtube.com/watch?v=qMky6D6YtXU&ab_channel=NeetCode)

Each square is how many paths to the end. Cache positions already visited

Base case is the end, which has 1

Each square is down+right. For boundary squares, add 0 for add of bounds square

CODE:

GENR: make sure to skip boundary cases that will always have the same value. In code, you start away from them (eg. `for j in range(n-2)`

GENR: to go from right to left, use `for j in range(n, -1, -1)`. The 2nd “-1” stops at 0, and the 3rd “-1” goes in reverse order (uses when first index of range > second index)

GENR: Instead of keeping the entire grid, you just need information from the previous row. So you can get rid of all rows except the previous by overwriting the “previous row” with the current row whenever you go up a row. 

- Thus, instead of O(m*n), you just need O(n), the length of a row (equal to # of cols)

GENR: Since we don’t store the rows, we don’t need to specify that we’re getting from the top or bottom row using i+1 or i-1; just `row[j]` for the previous row’s jth element col-aligned with curr jth elem. 

(In this case, since END is at bottom right and START is top left, we’re going bottom to top)

GENR: work backwards from end to start to figure out which direction to process values in from base case upwards