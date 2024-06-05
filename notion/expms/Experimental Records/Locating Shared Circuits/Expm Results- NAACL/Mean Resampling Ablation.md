# Mean Resampling Ablation

numseq_minimal_circuit_ablateRepeatLast.ipynb

[https://colab.research.google.com/drive/1xdL452m4c2Z0uuiMAdAPNzLMCnq6zGrh#scrollTo=iCQ7UnXjx9tX](https://colab.research.google.com/drive/1xdL452m4c2Z0uuiMAdAPNzLMCnq6zGrh#scrollTo=iCQ7UnXjx9tX)

Tried "repeat last" corruption for 10 top heads in mean ablation; this did not return good performance (0.8), indicating top 10 heads are NOT the circuit and are missing impt parts of it; so this is not the right circuit! Must keep searching for it! Notice that 3.0 and 4.4 and 6.6 aren’t part of it. Those heads are probably important for relaying info to 9.1; so with just 9.1, it’s unable to get this info.

[https://colab.research.google.com/drive/1xdL452m4c2Z0uuiMAdAPNzLMCnq6zGrh#scrollTo=B4caIj8kV7yN&line=1&uniqifier=1](https://colab.research.google.com/drive/1xdL452m4c2Z0uuiMAdAPNzLMCnq6zGrh#scrollTo=B4caIj8kV7yN&line=1&uniqifier=1)

Test heads from path patching (add in 3.0 and 4.4 and 6.6 )

Adding in 3.0, 4.4 and 6.6 increases performance from 0.8 to 1.89, which is nearly halfway to full logit diff score (4.6). This means these components are impt, but more are needed. Find them via path patching.

Note that getting rid of layers 10 and 11 only keep score up to 1.92. This means our missing heads are likely in layers 10 and 11. Try to add in all heads from 10 and 11 with the heads from path patching (to test upper bound of completeness)

FOUND ERROR- before, we only generated heads from 0 to 9 for layers 0 to 9 (using range(10)). But to get rid of layers 10 and 11 means we still need heads 0 to 11 for L0 to L9. So when we do that, “L0 to L9” gets 4/4.6 performance! Now ”L0 to “L8” only gets 2.9/4.6 performance. So the most impt heads are NOT in L10 and L11, but in L9 or before. We should search for them there. 

Though 0.6/4.6 is still pretty big, so later search for the L10 and L11 heads for that 0.6 perf.

[https://colab.research.google.com/drive/1xdL452m4c2Z0uuiMAdAPNzLMCnq6zGrh#scrollTo=abgjQqcTYIoy&line=1&uniqifier=1](https://colab.research.google.com/drive/1xdL452m4c2Z0uuiMAdAPNzLMCnq6zGrh#scrollTo=abgjQqcTYIoy&line=1&uniqifier=1)

Test heads from path patching plus all L10, L11 heads

This is a list of tuples. Write python code to add in all tuples of (10, i) and (11, i), where i is from 0 to 11:
[(0, 10), (0, 1)]

This is only 1.8225. This DECREASES perf. Perhaps there are ‘negative’ actv heads in L10 and L11 for the corr tokens which will not be “countered’ (shut off) by the right heads that are missing.

<<<

Now, only test heads L0 to L9 from path patching, without any L10 or L11

This gets rid of only 10.7, but decreases from 1.89 to 1.4. So 10.7 is still impt.

<<<

Add in all heads from one layer, try L0 to L9

This has iterations where in each iter, all the heads from a layer are added to our “best heads list” so far

All layers except L5 increase from 1.89. Note that the most increases are 

<<<

Add in all heads from all prev layer, try L0 to L9

Just like before, but at each iteration, add in all heads from that layer iteration and all layers before it. We are testing if there is a “combination” needed, not just a full layer.

Now each new layer has a bigger increase. By L8, we have all the heads we need to get full performance. This means we should confine our search to L0 to L8.

<<<

Add in other heads from path patching

Get heads from heatmaps of:

[https://colab.research.google.com/drive/1UQZrumDk5gEWuIlb4nZWRms8gbFf4z-w#scrollTo=teSb1k5Ul6mS](https://colab.research.google.com/drive/1UQZrumDk5gEWuIlb4nZWRms8gbFf4z-w#scrollTo=teSb1k5Ul6mS)

---

TO DO:

Try using some new search method (this is what ACDC does).

Try all heads from path patching that meet a logit diff threshold, not just top X. Adjust this threshold based on stats of prev studies?

---

[numseq_mincirc_(pt_2).ipynb](https://colab.research.google.com/drive/1uaNfFtv6dwO5YN-b122TmLKMfjG1f2IB#scrollTo=DcZG9rm2IAiA)

[https://chat.openai.com/c/97f9afb3-7586-415f-b15c-9a70cbdea01e](https://chat.openai.com/c/97f9afb3-7586-415f-b15c-9a70cbdea01e)

Here is a tuple list of (layer, head): [(0, 1), (0, 10)]. Write python code to generate every combination of heads from 0 to 11, and put each combination in the tuple list format given before. Put all these lists in a list. Show also the lazy way of generating this.

No, I want combinations of say [(0,1), (0,2)] and [(0,3), (0,5), (0,10)], etc.

Run time: 1:25pm - 3:40pm: 3470 found, so around 700 more to go. Est will take 2.5 hrs total.

<<<

The greater-than circuit only has 7% performance on the digits task!