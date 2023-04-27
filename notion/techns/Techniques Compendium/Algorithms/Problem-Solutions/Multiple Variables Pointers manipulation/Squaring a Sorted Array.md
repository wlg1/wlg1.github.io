# Squaring a Sorted Array

[https://www.designgurus.io/course-play/grokking-the-coding-interview?doc=638e39bd1756319ef156bebc](https://www.designgurus.io/course-play/grokking-the-coding-interview?doc=638e39bd1756319ef156bebc)

Brute force: first traverse array and square every number. then sort array.

Input: [-2, -1, 0, 2, 3]
Output: [4, 1, 0, 4, 9]

Sorting takes O(n* log(n) )
Improve/debug brute force: try to improve to O(n).

What were associated with O(n)? two pointer. so how can that analogy be used?

- Analogy to: [Remove Duplicates](Remove%20Duplicates%208bc6877647eb4fe0a5cf365200da823b.md)
    
    Two pointer objects: pointer A, pointer B
    two pointer keywords: multiple pointers doing multiple jobs save time from one pointer doing multiple jobs (but must know how many pointers to use beforehand)
    
    from this pattern in the analogy, what could pointer A be in this problem? [describe this past case pattern] what job does pointer A do?
    
    - **Attempt instance**: pointer A traverses the array
        
        now what can pointer B do?
        
        in both problems, we have a sorted array. but here, we're changing the sorted array's elements.
        
        this is where the analogy breaks down. the elements are not exactly the same.
        
        however, it's not hard to see where negative elements are supposed to go.
        
        here's an idea from two sum:
        one pointer goes at start, other pointer begins at end
        why: in two sum, this is because we can traverse both sides at once. the elements already encountered by a pointer are disregarded. (highlight, for this instance of relating them, 'disregarded')
        
        Input: [-2., -1, 0, 2, 3.]
        [-2., -1, 0, 2., 9]
        the reason pointer B moved was because abs(val(A)) < abs(val(B)). thus, B should be right of A.
        this is really just putting negatives next to positives, disregarding signs. b/c if x<y, x^2 < y^2. this simplifies steps needed.
        
        [-2., -1, 0, 2, 3.]
        [-2., -1, 0, 2., 3]
        [-1., 0, -2, 2., 3]
        what's the time complexity of this? we shifted everything left. That's a nested loop of O(n). So we cannot shift left to insert.
        

### Using a Hash Table

Let's start from a new approach. we just keep track of counting (then we need counter for everything; a hash table. that's external memory, not in-place. this is allowed).

the similarity is 'sorting array'. the association is 'sorting array -> hash table keep count'. let's try to match this analogy.

describe the previous case: hash table keeps track of every encountered based on absolute value. so x and -x both go in 'x'.

[-2, -1, 0, 2, 3]

hash table:
2: 2
1: 1
0: 1
3: 1

error: how to 'sort' hash table keys to traverse hash table?
b/c sorted, you know min and max (this is a generalizable association)
issue: negatives

takes O(n) to find min and max by traversing entire thing once and keeping counters.
total: O(n)

create hash table of min to max, increment by one. counter for each starts at 0.

fill hash table using O(n) to count
total: O(n + n) := O(n)

actually, don't need min, b/c min is always 0, since new array after squaring is always 0 or greater. so the max is last element, which is O(1).
total: O(1 + n) := O(n)

then in new array, create new element for every count of key
0: 2
1: 1
[0, 0, ] -> [0, 0, 1]

```
max size of array equals original array size

the pointer moves in this new array in O(n) b/c after filling in next element, it never looks back and disregards previous ones

```

TOTAL: O(1) + O(n) + O(n) := O(n).

### Improve w/ no hash table:

[https://www.designgurus.io/course-play/grokking-the-coding-interview?doc=63ddacd4fcc4ca873d5fbfbc](https://www.designgurus.io/course-play/grokking-the-coding-interview?doc=63ddacd4fcc4ca873d5fbfbc)

before, thought had to do in-place. but can use external memory- the new output array.

separate steps b/c there's eval at each, so that's new line of code not to be done at same time.

old: [-2., -1, 0, 2, 3.]
new: [9]
use and move B b/c val(A) < val(B), so B is bigger. insert it into right first. the reason we can't insert smaller first is b/c the smallers are in the middle, while biggers are alwasy at the ends.
-> move . (of what was squared and inserted)
old: [-2., -1, 0, 2., 3]
new: [9]
-> insert into new
old: [-2., -1, 0, 2., 3]
new: [4, 9]
if abs are equal, just move the pos one (this is arbitrary)
-> move .
old: [-2., -1, 0., 2, 3]
new: [4, 9]
-> insert into new
old: [-2., -1, 0., 2, 3]
new: [4, 4, 9]
->
old: [-2, -1., 0., 2, 3]
new: [4, 4, 9]
->
old: [-2, -1., 0., 2, 3]
new: [1, 4, 4, 9]
->
old: [-2, -1, 0.., 2, 3]
new: [1, 4, 4, 9]