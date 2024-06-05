# Manual path patch

[**Manual rmv from work backw circ**](https://colab.research.google.com/drive/1CHRn-AMko9RNrl1bqiCwB7DS-rz1CoBP#scrollTo=0zheHQmPw2Gk&line=1&uniqifier=1)

If rmv head, is correct answer still in 1st place; if not, what does it fall to?

see if removal coincides with importance on attnpat; record what performance difference each of the circuit’s heads makes. Are numdetect heads like 4.4 crucial? Are there backups?

- May be worthless by themselves, but work in conjunction with other heads?
- This gets 75% perf. Note that this is diff from this circ: [https://colab.research.google.com/drive/1CHRn-AMko9RNrl1bqiCwB7DS-rz1CoBP#scrollTo=78x6pmqkFnrP&line=1&uniqifier=1](https://colab.research.google.com/drive/1CHRn-AMko9RNrl1bqiCwB7DS-rz1CoBP#scrollTo=78x6pmqkFnrP&line=1&uniqifier=1)
    
    That has nodes from L4 for some reason
    

---

**iter patch from manual sel**

[numseq_path_patch_iterThres.ipynb](https://colab.research.google.com/drive/1onREXMNmc9ks0xpwDslUX2pdG0RSYtWS#scrollTo=ratQ65XwBdFx&line=1&uniqifier=1)

`head_adjList.keys()  # values is list of nodes with edges INTO key node (list of source nodes)`

Adj list: AL[i] stores the list of i's neighbors. So `head_adjList` is “one dir”, as ipp heatmap only shows which PREVIOUIS nodes affect current key node

- re-run ablation on circ found from path patch (that adds nodes). how much better is it than before adding nodes?

SIDENOTE: Setup+load time takes 3m

If the nodes don’t make that much of a difference in performance, then don’t keep them.

RESULT: new nodes only make 0.5% difference. so don’t keep them!

<

- re-run ablation on circuit after ipp gets rid of nodes w/o outgoing edges.

after ipp: [https://colab.research.google.com/drive/1sVfPVULVtAHgq2EiKS4bZJY8mBpXhc_D#scrollTo=jyC_p2aSFzOH&line=1&uniqifier=1](https://colab.research.google.com/drive/1sVfPVULVtAHgq2EiKS4bZJY8mBpXhc_D#scrollTo=jyC_p2aSFzOH&line=1&uniqifier=1)

18 nodes, compared to 34

ablation result: [https://colab.research.google.com/drive/1CHRn-AMko9RNrl1bqiCwB7DS-rz1CoBP#scrollTo=IKdjC2xcF_aQ&line=1&uniqifier=1](https://colab.research.google.com/drive/1CHRn-AMko9RNrl1bqiCwB7DS-rz1CoBP#scrollTo=IKdjC2xcF_aQ&line=1&uniqifier=1)

**Only 60%**

Thus, somehow the outgoing edges are still impt. The path patching E threshold may need to be lowered to keep these nodes!

<

[Using threshold of 0.001, the circuit is 71%](https://colab.research.google.com/drive/1CHRn-AMko9RNrl1bqiCwB7DS-rz1CoBP#scrollTo=nrD-I7AXMgGA&line=1&uniqifier=1) of full perf

How much above the mean actv logit diff is Ethres of 0.001 ?

<<<

ISSUE- a circuit has source nodes that are not part of the first layer?

As seen in IOI/ACDC diagram, you CAN have heads w/ no incoming edges that are in later layers, as long as they have an edge from an input token.

<<<

Get circuit which only adds edges; don’t add node if not in input to fn. Run on circuit found via manual sel

[numseq_path_patch_iterThres_pt2.ipynb](https://colab.research.google.com/drive/1sVfPVULVtAHgq2EiKS4bZJY8mBpXhc_D)

Filter output of `edges_within_threshold` to only keep (L, H) if it’s in circuit