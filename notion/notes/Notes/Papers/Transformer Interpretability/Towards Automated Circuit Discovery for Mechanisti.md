# Towards Automated Circuit Discovery for Mechanistic Interpretability

[Automated Circuit Discovery](../../Code%20515029dddcdc4d268ad1b5b2298d2cd6/Automated%20Circuit%20Discovery%2078c36eb7aa084d7db89fa74016e83d3e.md) : Code

(Sec 3, pg5) describes how it works

[Topological Order](../../CS%20&%20SWE%20f7436b5aff924c04aa569007bb061038/Algorithms%2048626da10b7542b992a5cae82e1b156d/Topological%20Order%20004d01ed21d14dadab1738920e643e11.md) : ACDC uses reverse topological order because it starts from the output node (a leaf, the most bottom tail). This processes outputs before inputs.

---

[https://arthurconmy.github.io/automatic_circuit_discovery/](https://arthurconmy.github.io/automatic_circuit_discovery/)

---

[https://www.youtube.com/watch?v=dn4GqR0DCx8](https://www.youtube.com/watch?v=dn4GqR0DCx8)

A Walkthrough of Automated Circuit Discovery w/ Arthur Conmy Part 1/3

5m10s- sparse, most heads and mlps don't matter for a task

9m55s- only automate parts of mechint.  Acdc only finds structure, not what the parts do. Speeds this up by finding impt edges that say what parts compose with what parts

14m50s- if replacing node for iPhone shininess with node for shininess in general (mean of actvs for many shiny objs) doesn't break perf of correct answer ranking but replacing node with zero etc does, then node may be detecting shininess

16m30s- is that part SPECIFIC to ioi, or the prompt structure in general? To know specifics, keep general structure but specifically replace ioi with ABC.
*We can test this too with subjects vs non subjects!!!

19m- not saying that's all the head does, but saying that's what it does on narrow distribution of clean and corr prompts where ioi matters.  Acdc is for specific input distributions, not general.

23m- write formal algo, then tracr compiles that to transformer weights that can be run
There are 0 xs in [a], there are 50% xs in [a,x] etc

26m- not great example bc can be done with bigrams, no need for induction for dursley. So instead of petunia durs, just look at petunia if petunisa dursley already occurred at prev pos incontext

Docstring in attention only 4 layer

29m- greater than is sequence completion

33m- not just subgraph, but a path in it

34m30s- pygraphviz can handle large num edges

36m10s- rmv edge (by replacing it with activations from corrupted distribution of edge) and see how affects performance . If degrades by more than tau, then include that edge as it's impt.

Null hyp is that every edge matters

[https://youtu.be/YzJyqmJW2wM?si=Seiuk28cKZwdrioz](https://youtu.be/YzJyqmJW2wM?si=Seiuk28cKZwdrioz)

1m30s- algo slow for even gpt2 small due to many edges

5m26s- didn't find order of edges mattered drastically
6m15s- but in an induction model it mattered with of the two IH was found first
Matters if get to 1.5 or 1.6 first

6m45s- layernorms threshold output of components
Ln scales stream to have sd
Head zero ablation changes ln, but may not change corruption that much. Norm kept constant

8m18s- race condition problem bc if delete an edge, can't use it for others. Perhaps out of five, one matters, but perhaps can't find this if deleted it every time?

10m40s- Grad descent method to optimize pver all edges; good idea for follow up work.

11m30s- one subtly is can sometimes get dead paths in algo. It may include ao but not connect it to input ia.
Neither edge may make the cut as both are impt and there's some credit splitting

14m- tau controls sparsity. Algo is iterative, so see number of edges that go into input node to tune tau so it becomes closer to idealized number of incoming edges. Stop algo early then rechoose tau. May have tau scheduler.

Uses fewer parameters than grad desc approaches, which balances regularization parameter for sparsity and learning rate.

16m40s- metrics used to compare performance and measure tau on
17m30s- survey what metrics used before and try to generalize. Ioi used logit diff. But no need diff metric every task. Kl divergence compares output distributions in clean vs corrupted settings to see how corrupted model becomes. If increase in kl div by more than tau, then edge is ikpt bc changes distribution a lot

18m50s- kl is dist between distributions. Output distribution for next token.

The Part of the model that just looks st name would boost John and Mary equally. So corrupted it doesn't make a difference for names. But the part of the model that looks at ioi specifically would damage Mary over John when it is corrupted.

20m- close to 0 kl means matches what model will output.
Kl div measures for all tokens change in the two dist while logit diff is misleading as it only accounts for how two tokens change

23m30s- compare to subnetworking probing to learn a mask to get components like a circuit.  Looks for nodes rather than edges. Does Grad descent to learn the mask

25m- doesn't look for minimal circuit, learns a linear probe to see if can learn from remaining components. But here, don't use probe. Learning sparse networks with l0 reg. Use mask learning approach thru training

27m- mask values between 0 and 1 (interpolate clean and corrupted). Or node is randvar, present with prob over bernoulli.

38m- good roc on greater than but fails on docstring

44m- subnetwork probing of acdc not good for large models, but OK for gpt2small.

https://youtu.be/GQ08qevnY58?si=jve3uGPiJve0N0SL