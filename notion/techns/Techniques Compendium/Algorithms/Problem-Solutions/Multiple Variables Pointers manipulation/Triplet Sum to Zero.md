# Triplet Sum to Zero

[https://www.designgurus.io/course-play/grokking-the-coding-interview?doc=63ddad0980798b625e14ef14](https://www.designgurus.io/course-play/grokking-the-coding-interview?doc=63ddad0980798b625e14ef14)

From [https://www.designgurus.io/course-play/grokking-the-coding-interview?doc=63ddad0980798b625e14ef14](https://www.designgurus.io/course-play/grokking-the-coding-interview?doc=63ddad0980798b625e14ef14) :

> This problem follows the **Two Pointers** pattern and shares similarities with Pair with Target Sum. A couple of differences are that the input array is not sorted and instead of a pair we need to find triplets with a target sum of zero.
> 

> To follow a similar approach, first, we will sort the array and then iterate through it taking one number at a time. Let’s say during our iteration we are at number ‘X’, so we need to find ‘Y’ and ‘Z’ such that . At this stage, our problem translates into finding a pair whose sum is equal to “-X” (as from the above equation ).
> 

> Another difference from `Pair with Target Sum` is that we need to find all the unique triplets. To handle this, we have to skip any duplicate number. Since we will be sorting the array, so all the duplicate numbers will be next to each other and are easier to skip.
> 

Three pointers: one to iterate, then a pointer left to current index, and another right of current index

### Generalizations

- Transform from finding Sum A to Sum B
    
    We want to find X + Y + Z = A. Instead, we can transform using [Transform by equation](../../Techniques%204144140dcb42461fba9223a7a967195d/Transform%20by%20equation%20a329a91df7754f2aadb1bea211b4d45a.md)  into X + Y = A - Z and use the solution to find B = A - Z, as found in [Two Sum
    ](Two%20Sum%205e8e9e73e24b4ffb83420dd37fbe78c1.md)