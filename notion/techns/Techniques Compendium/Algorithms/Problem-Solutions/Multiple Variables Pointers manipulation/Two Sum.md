# Two Sum

- REASONING EXAMPLE 1 [click to expand]
    
    First try brute force by going over array twice, finding a value each time. Nested for loop is O(n^2). Aim to do better with O(n); to do so, we cannot visit the array more than once. We can try to keep a separate counter.
    
    Approach 1 would move a pointer variable through an array, using a counter to keep track of a previous value and comparing it to the pointer. Now that we have the approach, let's try a simple example with it.
    Array: 1, 3, 4, 7
    Target: 7
    
    Start with a simple case of this simple example. Say the counter stores 1, and the pointer is now at 3. It adds them to get 4, which is less than 7. Now what should the algorithm do with the counter and pointer? Both 1 and 3 are less than 7, so it should try to increase one of them. But the only object we can move is the pointer; the counter merely stores the value the current pointer is at. So we move 3 to 4; sum is 5. We move to 7; sum is 8. Now, we have failed because we have traversed the array once, and we cannot traverse it more than once.
    
    A problem with approach 1 is that we have no choice but to move the pointer, effectively only changing ONE of the two variable involved in the sum. A solution to this problem is to allow the counter to move; that is, use two pointers instead.
    
    In approach 2, we use 2 pointers, both starting at the beginning. Pointer_1 reads 1, and pointer_2 reads 3. We move pointer_1 to 4 (since 3 is on pointer_2) and get 7. But why move pointer_1, and not pointer_2? We did not give the algorithm a way to decide.
    
    What if it's arbitrary? Let's test this. If we arbitrarily try the case where we always move pointer_2, then we end up getting pointer_2 to the end of the array, visting each element once and thus failing to solve it before traversing the array more than once. So we CANNOT move an arbitrary pointer for this case.
    
    Should we modify approach 2? What's good about it that we should try to keep? The two movable pointers is good. Let's brainstorm some changes we can make that don't change the good part. For one, the two pointers were placed one after the other. We can try moving them to different positions. As of now, we don't know which ones. Another possible change is to move pointers left; we only moved them right.
    
    A second problem we notice with approach 2 is that one of the pointers took up all of the array. We did not allow the second pointer to search the array, rendering it useless. So we should have one pointer search part of the array, and the other search the second half.
    
    Let's keep describing the problem. One adjective we've been ignoring is "sorted". We can bring up all we know about sorted problems to see what we can extract. We also keep this clear in our mind, repeating it a few times to make it more prominent, so we don't forget it in case it comes in handy.
    
    With these observations in mind, we start to think about them all at once. We need to figure out: 1) Where to place the pointers, 2) Ability to move pointers left. To move pointers left, there must be elements left of it. Let's first try the most extreme case, and analyze its flaws (if any): put one pointer most left, and the other most right. Get their sum. In our simple example, it's 8, which is bigger than 7. Which pointer to move? We want to DECREASE. Because the array is SORTED, if we move the first, it increases; if we move the second, it decreases. Thus, we move the first. Likewise, if we need to increase, we move the second. Let's see a case of this:
    Array: 1, 3, 4, 7
    Target: 4
    Indeed, if we keep moving the right, we'll solve this case, too.
    
    So approach 2 works for at least one case. It is a satisfactory solution so far, but if we have more time, we can check our reasoning, then check it on more cases. What about another case?
    

---

- SOLN 1
    
    One pointer starts at beginning, another starts at the end. Decide which pointer to move based on if current sum of their values is larger or smaller than target
    

---

---

## GENERALIZATIONS

[Two Pointer Technique](../../Techniques%204144140dcb42461fba9223a7a967195d/Two%20Pointer%20Technique%208a16baa8abdc42c9ba76ed8087dcd736.md) 

## Sub-PROBLEMS

[Avoid visiting the array more than once](../Array%20193463deef6f40e9a28a3e266e998392/Avoid%20visiting%20the%20array%20more%20than%20once%20eb773a8f01b5489f85ec2f0ec24a457e.md) 

## SIMILAR PROBLEMS