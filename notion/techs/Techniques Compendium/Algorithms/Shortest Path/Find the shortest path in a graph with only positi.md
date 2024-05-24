# Find the shortest path in a graph with only positive distance edges

[https://leetcode.com/discuss/general-discussion/1059477/A-noob's-guide-to-Djikstra's-Algorithm](https://leetcode.com/discuss/general-discussion/1059477/A-noob's-guide-to-Djikstra's-Algorithm)

---

### Additional Notes

> Source: [https://leetcode.com/discuss/general-discussion/1059477/A-noob's-guide-to-Djikstra's-Algorithm](https://leetcode.com/discuss/general-discussion/1059477/A-noob's-guide-to-Djikstra's-Algorithm)
> 
> 
> ![Untitled](Find%20the%20shortest%20path%20in%20a%20graph%20with%20only%20positi%200dfef59db75f425a9c23dd2e4c53fc8c/Untitled.png)
> 

**Why are we so sure when we found a shortest path?**

The reason we know the shortest path from S to D has length 11 is because the shortest path from S to B must have length 10, and the shortest path from B to D has length 1. 

Assume there is another shortest path from S to D that has less than length 11. 

Say B to D has length 5. What if B to C is 2, and then C to D is 1? Then B-C-D is 13, which is less than 15. However, in the case above, B to C was less than B to D.

What if B to C was 3, and B to D was 2? Then we are sure. This is because we already rule out that the alternative path of S-B-C-…-D is already worse than S-B-D.

It’s only when B to D is greater than B to C that we **don’t** know, because it’s possible that S-B-C-…-D could be better than S-B-D. Further investigation is needed. 

**What can we take away (generalize) from this?**

We are SURE about something if we rule out all other possibilities. (This is a very broad generalization, so we won’t create a page for it as it’d appear in too many places.)