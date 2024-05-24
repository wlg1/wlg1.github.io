# One boat, move a goat, a lion, a cabbage

## Problem:

Moving a goat, a lion, and a cabbage from one side of a river to the other using a boat where the boat can only hold you and one item. The goat can eat the cabbage if left alone, and the lion can eat the goat if left alone.

### Reasoning Attempt:

We have to move the goat first because it cannot be on the same side as the cabbage or the lion. But after moving the goat, if we move the cabbage or the lion to the goat’s side, then that’s not possible either because having either on the same side with the goat is illegal.

### Sub-Problem- Misunderstanding:

The problem with this attempt is that it thinks that the goat and another item cannot be PLACED on the same side. However, the problem actually means they cannot be LEFT ALONE on the same side. When you are on a side, they are not alone with each other. 

### Possible Heuristic:

List out each description and question each as assumption. Describe “place on same side” and see if it matches problem description. We see that it doesn’t. 

### Generalization:

Problem: Misunderstood problem description

Solution: List out each description and question each as assumption, seeing if it matches the problem description. 

## Solution:

To solve this problem, we need to follow these steps:

1. Move the goat to the other side of the river.
2. Return alone to the starting side.
3. Move the cabbage to the other side.
4. Move the goat back to the starting side.
5. Move the lion to the other side.
6. Return alone to the starting side.
7. Move the goat to the other side.

By following these steps, we ensure that the goat and cabbage are never left alone together, and the lion and goat are never left alone together.

---

### Variation

Instead of goat and cabbage being illegal to leave alone, the lion and cabbage are illegal to leave alone. A common trick with this variation is if someone uses “outside knowledge” to think it’s goat and cabbage that shouldn’t be left alone because goats eat cabbages. Instead, one should think of each item as agnostic to their outside description, and as being interchangeable with variables with no traits from outside the problem, containing only traits  what’s provided about them in the problem. 

*The notion AI can solve this variation:*

> If the lion and cabbage cannot be left alone, the solution would be:

Move the goat to the other side of the river.

Return alone to the starting side.

Move the cabbage to the other side.

Move the goat back to the starting side.

Move the lion to the other side.

Return alone to the starting side.

Move the goat to the other side.

By following these steps, we ensure that the goat and lion are never left alone together, and the lion and cabbage are never left alone together.
>