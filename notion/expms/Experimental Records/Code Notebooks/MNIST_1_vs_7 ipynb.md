# MNIST_1_vs_7.ipynb

Link to notebook: [https://colab.research.google.com/drive/1NfYhLjJEanWE3iu191-qzZi26ZIFeWVk#scrollTo=6Cli8rxOMNSf](https://colab.research.google.com/drive/1NfYhLjJEanWE3iu191-qzZi26ZIFeWVk#scrollTo=6Cli8rxOMNSf)

### Type of Notebook: Draft

### Summary

---

[Detailed explanation of code](MNIST_1_vs_7%20ipynb%20cd1482eb130b428681a298e72f020f76/Detailed%20explanation%20of%20code%20b5a47f4e89dd4517a8323526d3ea60a9.md)

[Some ideas for this notebook](MNIST_1_vs_7%20ipynb%20cd1482eb130b428681a298e72f020f76/Some%20ideas%20for%20this%20notebook%20f02bae3682334542819d5b2dfab0d8a5.md)

---

### Compare slight mods of input

For Question/Task: Find the neurons that control for the top line that distinguishes b/w 1 and 7

---

- EXPERIMENT: Compare original vs modified by adding line of ones to an ‘1’ image.
    
    DESCRIPTION:  Add line of ones manually looking at pixel map. Try on first image of ones dataset. Compare model prediction of original vs modified.
    
    ![Untitled](MNIST_1_vs_7%20ipynb%20cd1482eb130b428681a298e72f020f76/Untitled.png)
    
    RESULT: The model still classifies the modified output as 1.
    
    ERROR
    
    ANALYSIS: 
    
    Some ideas on why this may have failed:
    
    - The modified line was not tall enough, so mod more lines
    - The modified line was too wide (so make its right tail shorter)
    
    Test: Try testing a ‘7’ image to ensure the predict function is working correctly.
    
    Result: Correctly classifies it as ‘7’
    

---

- EXPM: Compare original vs modified by adding line of ones **(right tail not too big)** to an ‘1’ image.
    
    ![Untitled](MNIST_1_vs_7%20ipynb%20cd1482eb130b428681a298e72f020f76/Untitled%201.png)
    
    RESULT: It’s still classifying modified as ‘1’.
    
    ANALYSIS: Now try adding more modified lines
    

---

- EXPM: Compare original vs modified by adding line of ones **(right tail not too big and add more modified lines)** to an ‘1’ image.
    
    DESC:  Add 3 lines 
    
    ![Untitled](MNIST_1_vs_7%20ipynb%20cd1482eb130b428681a298e72f020f76/Untitled%202.png)
    
    RESULT: Still classifies it as ‘1’
    
    ANALYSIS: Perhaps something in the original “1” is making it strongly recognize it as 1. We can try a few things:
    
    - Make an entirely new ‘7’ that’s just a horizontal line and a vertical. This will have no traces of the original “1”
    - Look at the probabilities of each class, not just the final prediction

---

- EXPM: Look at the probabilities of each class, not just the final prediction
    
    DESC: Just look at the ‘output’ variable
    
    RESULT: 
    
    For just adding top line (full), the probabilities are 9.0585 (class 1) vs 1.3064 (class 7)
    
    For just adding top line (right tail gone), the probabilities are 8.7628 (class 1) vs 0.9336 (class 7)
    
    For adding top line (right tail gone) and add more modified lines, the probabilities are 10.4093 (class 1) vs 1.7214 (class 7)
    
    ANALYSIS:
    
    Why isn’t there a pattern to how the probabilities change as the image is modified to look “more like 7”?
    
    This seems like a dead end, so let’s backtrack to another idea. Look in “Some ideas for this notebook”; this may be a list or a tree. Let’s try:
    
    Make an entirely new ‘7’ that’s just a horizontal line and a vertical. This will have no traces of the original “1”
    
    SLIGHT ERROR: This model has 10 outputs, but we just wanted 2. However, this doesn't seem to affect the output probability much because the other classes are usually negative, much lower than classes 1 and 7.
    

---

- EXPM: Make an entirely new ‘7’ that’s just a horizontal line and a vertical.
    
    DESC: This will have no traces of the original “1”
    
    Though this isn’t a CNN so there aren’t ‘filters’ that use convolution, there may still somehow be neuron groups acting as edge detectors. This means they can detect shades associated with “1”. Perhaps the way that “1” is WRITTEN by a human has something in its vertical that is different than how the vertical part of “7” is WRITTEN. 
    
    ![Untitled](MNIST_1_vs_7%20ipynb%20cd1482eb130b428681a298e72f020f76/Untitled%203.png)
    
    RESULT: Still says it’s ‘1’
    
    `tensor([[-2.3466, 12.5388, -2.7577, -2.8460, -2.6495, -2.6185, -2.1980,  7.4132,
             -2.0027, -2.3694]], grad_fn=<AddmmBackward0>)`
    
    ANALYSIS: Try increasing the top line rows
    
    TEST: Increase to start at row 1
    
    RESULT: Still says ‘1’
    
    `tensor([[-2.4962, 13.0826, -2.2703, -2.9389, -2.2922, -2.8575, -2.5294,  6.4184,
             -2.3506, -2.6344]], grad_fn=<AddmmBackward0>)`
    
    NOTE: The output is slightly different each time you run the image through model b/c of dropout
    

---

- EXPM: Take existing ‘7’ image and remove the top line to turn into ‘1’ and see what outputs are
    
    RESULT: It still think it’s a 7
    
    tensor([[-1.7598,  3.8339, -1.5209, -1.3557, -1.8499, -1.3327, -1.4784,  8.3270,
    -1.3954, -1.5258]], grad_fn=<AddmmBackward0>)
    
    ANALYSIS: This may be because there is MORE than just a top line to distinguish between ‘1’ and ‘7’. This means we should use our own custom dataset (but with random variations between images) that just have ONE thing different between them, and train them on a new model
    
    Ideas: A circle at a random location? No; may be too hard to distnguish b/c not CNN.
    

---

- EXPM: Turn all pixels in an image of ‘7’ into 0, then look at output probabilities
    
    DESC: This is a sanity check to make sure the model somehow isn’t “fixed” on making a certain image file be a class despite modifications to it, perhaps b/c it’s somehow referencing the original data it came from.
    
    RESULT: It sees the corrupted ‘7’ now as a ‘1’ when all the pixels are 0:
    
    tensor([[-0.2138,  0.9715, -0.2150, -0.1903, -0.2204, -0.1819, -0.1769,  0.6963,
    -0.1874, -0.2031]], grad_fn=<AddmmBackward0>)
    
    ANALYSIS: This shows the model is not “fixed” on the original image; it is classifying the updated image. 
    
    ---
    
    Now we can also see how much we can corrupt the image until it no longer is able to distinguish it as a ‘7’.
    

---

- EXPM: Corrupt the ‘7’ image until it no longer is able to distinguish it as a ‘7’.
    
    DESC: Use binary search: Start by removing rows 0 to 14
    
    RESULT: The output is nearly ambiguous now
    
    tensor([[-1.3851,  4.8885, -1.1722, -1.2756, -1.4588, -1.3128, -1.1553,  4.8214,
    -1.0095, -1.2770]], grad_fn=<AddmmBackward0>)
    
    TEST: Next, Try removing rows 7 to 14.
    
    RESULT: Again, it's ambiguous. We know 6 to 10 didn't work. 
    
    TEST: Now try rows 6 to 12.
    
    RESULT: Here, it's still at 7, but more ambiguous. 
    
    TEST: Try 6 to 14 just to compare it to 0 to 14 (should be the same.)
    
    RESULT: If you run them multiple times, you get different results. Sometimes 1 slightly beats 7, sometimes 7 beats 1. So this is ‘very ambiguous’.
    
    TEST: Since we know the variation is bigger when removing around rows 10-14, try running it again when removing 6 to 12
    
    RESULT: If we run it multiple times, it’s STILL saying it’s 7 all the time, though not by much. 
    
    ANALYSIS: This means row 13 appears to be “crucial”. The model may be detecting that this is the “connecting part” b/w the top line and the bottom line. 
    
    Up to 12:
    
    ![Untitled](MNIST_1_vs_7%20ipynb%20cd1482eb130b428681a298e72f020f76/Untitled%204.png)
    
    Up to 13:
    
    ![Untitled](MNIST_1_vs_7%20ipynb%20cd1482eb130b428681a298e72f020f76/Untitled%205.png)
    

IDEAS TO TRY NEXT:

- Corrupt until img turns from ‘7’ definitely into ‘1’ (low ambiguity)
- Custom dataset that’s easy about “containing” something or not.
- For multiple 7s, see how many rows removed on avg it takes to make it not able to predict 7 well
    - Since outputs are random, run multiple times
- Use a smaller model with no dropout, since dropout is random

Once we find the neurons that detect this, then we can look to see what they’re doing, and also compare them to other models that are different yet do the same thing.

The larger scope goal is to find techniques that are easy to use and can be used on many models which detect what the roles of neurons are, and compare them across models to see if there are analogous similarities. This will lead to seeing if “analogous circuits” and “abstract circuits piecing to more specific” can be found.

---

### **Attempt 1: Average each neuron**

For Question/Task: Find the neurons that control for the top line that distinguishes b/w 1 and 7

---

- EXPERIMENT: Get neurons w/ biggest avg diffs b/w classes
    
    

---

- EXPM: Set weights above threshold to 0 and compare to hist of random weights set to 0
    
    DESC: Set weights to 0 for neurons where the difference of their activations for class one vs seven is above certain threshold  Compare with the average of the same # of weights chosen randomly set to 0, and see if any significant differences. Get histogram of random weights set to 0.
    
    RESULT: 
    
    ![Untitled](MNIST_1_vs_7%20ipynb%20cd1482eb130b428681a298e72f020f76/Untitled%206.png)
    
    Find the percentage of neurons that have an activation difference of under 0.2 (meaning there is not much difference between them, on avg, for class 1 vs class 7):
    
    ```python
    sum(abs(i) < 0.2 for i in diffs.tolist() ) / len(diffs)
    ```
    
    ANALYSIS:
    
    Around 60% of neurons have an activation difference of less than 0.2. Notice that destroying neurons which have a difference above 0.4 doesn't have as much effect as destroying those above 0.3, and even more so for 0.2.
    
    From this, it seems like the 'highest activated neurons' are not so important as the number of neurons firing above some level. Those neurons b/w 0.3 and 0.4 are very impt.
    
    Is this because of the % of neurons destroyed, or specifically those neurons above a certain threshold?
    

---

STUCK