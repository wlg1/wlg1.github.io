# Months path patch

[months_path_patch_iterThres.ipynb](https://colab.research.google.com/drive/1VFGOUJtZvQCnj8OvP33v3y1ljTMdfnee#scrollTo=bo2N95BPfBEq)

Threshold 0.001 seems to big (introduces more nodes than found from ablation circ), and 0.01 seems to small, so try 0.005.

This gets rid of (2,3) and (2,9), which were missing in [digits circuit](Months%20circuit%20765ea1869818426298c439544a337efc.md) found by prune backw once.

However, it’s too small and not ‘hierarchical’ enough (eg. what influences 8.8 and 7.10 ?)

Note that 8 and 7 don’t need to be there.