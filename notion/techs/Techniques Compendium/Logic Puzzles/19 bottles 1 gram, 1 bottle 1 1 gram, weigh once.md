# 19 bottles 1 gram, 1 bottle 1.1 gram, weigh once

SOLN:

1. Number the bottles from 1 to 19.
2. Take 1 gram from bottle 1, 2 grams from bottle 2, and so on, until 19 grams are taken from bottle 19.
3. Take the 1.1-gram bottle and add it to the pile.
4. Weigh the pile of bottles once.

Now, there are two possible outcomes:

- If all bottles were 1 gram, the total weight should be 210 grams (the sum of 1 to 19). However, since one bottle is 1.1 grams, the total weight will be slightly more than 210 grams.
- If the pile of bottles weighs more than 210 grams, it means the 1.1-gram bottle is in the pile. To determine which bottle it is, subtract 210 from the total weight of the pile. The resulting number corresponds to the number of the bottle that is 1.1 grams.

---

### GEN

PROB: [There is no way to distinguish between where it came from](../General%2059edbfce78e0462499eae794a383f97b/There%20is%20no%20way%20to%20distinguish%20between%20where%20it%20ca%2097e74515c2634a048785b98552e02fe5.md) 

Eg) If take one pill from each bottle, and find the total weight is not 210, we still don’t know which bottle the bad pill came from

SOLN: Make there be something distinct that is ONE TO ONE with each bottle.

Eg) Bottle 2 always is associated with weight 2*(pill weight). So anything that indicates the pill weight came from ‘2 pills’ comes from ‘bottle 2’.

SOLN (Detailed): To distinguish a single item among a group of similar items, the item needs to have a distinct characteristic that sets it apart from the others. This could involve labeling the item, marking it with a unique symbol or color, or altering its shape or size in a noticeable way. By creating a clear distinction, it becomes possible to identify the specific item that has the unique characteristic.

---

### Summary

The problem is to identify a single item among a group of similar items that has a distinct characteristic. If the item is indistinguishable from others, it becomes impossible to identify which item is distinct.