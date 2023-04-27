# Remove Duplicates

[https://www.designgurus.io/course-play/grokking-the-coding-interview?doc=63dda4ad488110f74a93371d](https://www.designgurus.io/course-play/grokking-the-coding-interview?doc=63dda4ad488110f74a93371d)

t: two pointers
-generalization: allows two things to be done separately
-for this problem: one pointer keeps track of where to place next non-duplicate (good element), and the other pointer finds the next element in the array
-why: this prevents traversing array quadratically. instead of delving into another array iteration when a 'good element' is found, one pointer's job is to traverse to find the element, and the other is to find where to put it. that way, one doesn't need to use just one pointer for multiple jobs

this CHANGES up from two sum b/c instead of putting pointers at ends, they're both at start. so see if changing previous will destroy effectiveness of why it worked.

### Analogies To

[Two Sum
](Two%20Sum%205e8e9e73e24b4ffb83420dd37fbe78c1.md)