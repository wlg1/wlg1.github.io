# Path Patching after Work Backw

Found important attention heads for circuit, now find finer connectivity between them using path patching (for each head, automate finding which heads on heatmap have highest value).

[numseq_path_patch_loopCirc.ipynb](https://colab.research.google.com/drive/1onREXMNmc9ks0xpwDslUX2pdG0RSYtWS)

[https://chat.openai.com/c/7b84abf2-a199-44a4-a6c4-b97d956d2ea8](https://chat.openai.com/c/7b84abf2-a199-44a4-a6c4-b97d956d2ea8)

loop thru heads in circuit and apply PP. get top heads and print out. These are what conn to that head.

let each tuple in the following list be an end node:
circuit = [(0, 1), (0, 3), (0, 5), (0, 7), (0, 9), (0, 10), (1, 0), (1, 5), (2, 2), (2, 9), (3, 0), (3, 3), (3, 7), (4, 4), (4, 7), (4, 8), (4, 10), (5, 1), (5, 4), (5, 5), (5, 6), (5, 8), (5, 9), (5, 10), (6, 1), (6, 3), (6, 4), (6, 6), (6, 10), (7, 2), (7, 6), (7, 10), (7, 11), (8, 8), (9, 1), (10, 7)]

run top_abs_pairs() on the results of get_path_patch_head_to_heads(head) for each head in circuit. now each of these heads are start nodes from which an edge goes from start to end node (in the current loop which head is in). save these results in both a dict of endNode: [list of start nodes, the top 5 results] and also use graphviz to plot this graph

(later, instead of top 5 for every head, use a threshold for each edge. may be relative)

<<<

make the following nodes yellow:

greater_than = [(0, 1), (0, 3), (0, 5), (5, 5), (6, 1), (6, 9), (7, 10), (8, 11), (9,1)]