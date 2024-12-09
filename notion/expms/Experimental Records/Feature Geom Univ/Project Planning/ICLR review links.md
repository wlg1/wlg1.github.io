# ICLR review links

Reviews:

[https://openreview.net/forum?id=rbHOLX8OWh&referrer=[Author Console](%2Fgroup%3Fid%3DICLR.cc%2F2025%2FConference%2FAuthors%23your-submissions)](https://openreview.net/forum?id=rbHOLX8OWh&referrer=%5BAuthor%20Console%5D(%2Fgroup%3Fid%3DICLR.cc%2F2025%2FConference%2FAuthors%23your-submissions))

Rebuttal draft (table):

[https://docs.google.com/document/d/19WY9b9_M2hXI7fKKex0-zDtPI9xQzZpIc4SX0msaLzo/edit?tab=t.0#heading=h.iwlmnzuypjbd](https://docs.google.com/document/d/19WY9b9_M2hXI7fKKex0-zDtPI9xQzZpIc4SX0msaLzo/edit?tab=t.0#heading=h.iwlmnzuypjbd)

As paragraphs:

[https://docs.google.com/document/d/1GSra9arRdG8ZBzc7Wdm5wkG8U1e304vbhlXRZ_Qh8vs/edit?tab=t.0](https://docs.google.com/document/d/1GSra9arRdG8ZBzc7Wdm5wkG8U1e304vbhlXRZ_Qh8vs/edit?tab=t.0)

---

Expms reviewers ask to try:

1. cross model
2. alternative method (hungarian)
3. using more samples
4. looking beyond top 5 activations
5. how sensitive model is to changes in using more than top 5, etc
6. pvalue effect sizes
7. comparing LLMs
8. multiple hypothesis testing
9. "layer 0 contains few discernible, meaningful, and comparable features” - look at these interps

---

Relevant topics

- [https://en.wikipedia.org/wiki/Hungarian_algorithm](https://en.wikipedia.org/wiki/Hungarian_algorithm)
    - [https://arxiv.org/pdf/2209.04836](https://arxiv.org/pdf/2209.04836) : GIT RE-BASIN: MERGING MODELS MODULO PERMUTATION SYMMETRIES
- [https://dissertationbydesign.com/p-values-and-effect-sizes-the-dynamic-duo-of-quantitative-research/](https://dissertationbydesign.com/p-values-and-effect-sizes-the-dynamic-duo-of-quantitative-research/)
    - a Cohen’s d of just 0.2. while Program A’s participants improved their endurance by a whole 2 minutes, Program B’s participants weren’t far behind, upping theirs by 1 minute and 50 seconds
    - Don’t forget to add confidence intervals to show the precision of the estimate!
- https://en.wikipedia.org/wiki/Multiple_comparisons_problem
    - if 100 tests are done and the probability of incorrectly rejecting null (claiming there’s sigf) is 5%, the chance of AT LEAST ONE rejecting null is 99%. The number of incorrect “signifances” is 5.
- [https://transformer-circuits.pub/2024/crosscoders/index.html](https://transformer-circuits.pub/2024/crosscoders/index.html)