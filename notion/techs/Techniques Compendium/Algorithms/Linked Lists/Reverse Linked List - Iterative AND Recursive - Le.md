# Reverse Linked List - Iterative AND Recursive - Leetcode 206

- Iterative
    
    Nodes (head, 1, 2, etc) have .next. The .next points to a node
    
    Pointers prev and curr do not have .next
    
    However, when pointers point at nodes, they have .next. So [curr.next](http://curr.next) is [1.next](http://1.next) when curr at 1
    
    (NOTE: prev and curr are pointers in general, while .next is a pointer of Class Node)
    
    To have the node point backwards: `curr.next = prev`
    
    Then, we want to shift our pointers. Each moves up by one. prev goes to curr, so curr goes to the node after curr, which is curr.next: 
    
    `prev = curr`
    
    `curr = nxt`
    
    nxt is obtained by SAVING the old [curr.next](http://curr.next) before “`curr.next = prev`":
    
    `nxt = curr.next`
    
    [`curr.next](http://curr.next) = prev`
    
    Thus, the entire loop is:
    
    `while curr:`  # ends at end of linked list, which is None (curr = nxt := None)
    
    `nxt = [curr.next](http://curr.next)` # save
    
    [`curr.next](http://curr.next) = prev` # reverse
    
    `prev = curr` #move up
    
    `curr = nxt` #move up
    
- Recursive

---

[https://leetcode.com/problems/reverse-linked-list/submissions/?envType=study-plan-v2&envId=leetcode-75](https://leetcode.com/problems/reverse-linked-list/submissions/?envType=study-plan-v2&envId=leetcode-75)

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr_ptr = head
        
        while curr_ptr != None:
            nxt_ptr = curr_ptr.next # store to update curr before erasing
            curr_ptr.next = prev # reverse arrow
            prev = curr_ptr # update prev
            curr_ptr = nxt_ptr # move curr ptr up
        return prev # last elem of prev list, which is now the first bc it's reversed
```