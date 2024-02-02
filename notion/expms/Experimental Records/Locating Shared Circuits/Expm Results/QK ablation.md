# QK ablation

What does it mean to move information from position A to position B?

As we see in [Query, Key, Value, Output Matrices](https://www.notion.so/Query-Key-Value-Output-Matrices-fe92464f6ee24068b6aaa56bb85e903e?pvs=21), 

- The dims of input to head are $n \times d_e$
- The dims of query and key **weight matrices** are $d_e \times d_q$
- So dims of query and key **matrices are** $n \times d_q$

So every token position (n) has its own query vector and key vector

When key vector associated with position A is multiplied with the query vector associated with position B, then multiply this by value vector (associated with key), and the resulting activation (called ‘attention’) is high, that means position B pays strong attention to position A.

---

query vector for a token pos: obtained from multiplying the embedded input row vector (has dim $d_e$) with every column of the query weight matrix (there are $d_q$ of these, each with dim $d_e$)

So each col vector of the query weight matrix is NOT specific to one position. Each position’s embedded vector is multiplied by ALL the query weight matrix column vectors. This transforms each embedded vector into a basis vector of the “query space”.

---

Thus, the Previous Token Head 2.2 (H) has query pos $S_1 + 1$ pay attention to key pos $S_1$ means the query vector for pos $S_1 + 1$ has a high dot product with key vector (then value vector) for pos $S_1$

**Thus, any “high enough” attention value of the QK (attention) matrix times the value matrix means an edge in our circuit.**

---

So for the attention matrix of a head, if its end query (last row) pays attention to at least one key (cols), you need to keep that “end” seq pos. Keep all the rows that matter based on the attention pattern.

To obtain these, we can use a threshold to automate. We can also look at the attention patterns.

QK says how much qry “wants” key. But QKVO says how much this attending value will affect the logits.

---

We can also perform automated ablation on each position. There are many positions, so we can filter first using attention heads.

---

incrD_ablt_qry.ipynb

[https://colab.research.google.com/drive/1BCNmQTiOdWZBJ8pZcsZU-6u_hoa88_Z6#scrollTo=MKfPnNL-kcdI&line=1&uniqifier=1](https://colab.research.google.com/drive/1BCNmQTiOdWZBJ8pZcsZU-6u_hoa88_Z6#scrollTo=MKfPnNL-kcdI&line=1&uniqifier=1)

TEST, RESULT: When number movers only attend from the end query, the performance is -0.01

[https://colab.research.google.com/drive/1BCNmQTiOdWZBJ8pZcsZU-6u_hoa88_Z6#scrollTo=GoU2_mJ9oU2y&line=5&uniqifier=1](https://colab.research.google.com/drive/1BCNmQTiOdWZBJ8pZcsZU-6u_hoa88_Z6#scrollTo=GoU2_mJ9oU2y&line=5&uniqifier=1)

TEST: all heads attend from all pos. this should match the prev code's impl

RESULT: It's approximate. This means the "number detectors" must STILL attend from EVERYWHERE. Not just query from a pos.