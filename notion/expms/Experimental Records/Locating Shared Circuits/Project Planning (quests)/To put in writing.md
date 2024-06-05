# To put in writing

Don’t give exact scores (put that in appendix) just use it to find impt components “below a threshold” (eg. if they ablate it “strongly enough” such taht ablation is in top 1% of distribution). Forget about perforamcne score. These measures are not exact enough, but are mere approximations. Thus, we use ballpark ranges such taht if is very far away, is significant. But the detailed small measurements and differences (eg. rankings, exact thresholds) don’t matter.

Put this in appendix. Exact scores can be put in main body? Or instead of exact, have categories like “falls into top 1%”. but only say they’re ‘estimates’ in appendix or rebuttals, not in main body

Don’t focus on finding circuits or putting circuits in title, state difference of English vs other languages for numbers and letters in terms of interpretability

Future work: difference in alphabet, if there are any mappigns between letters

Scale this up from letters to concepts?

While the successor heads paper shows that the successor head is crucial for incrementing, our experiments that it by itself is not enough to change the logits and the correct answer. This may be due to backups. Instead, ablating the 3 heads and MLP 9 is enough to change the correct answer, and the entire sequence afterwards.

even backups do not save it

First briefly state will give generated results after ablation, and logits diffs. Give table of results before logit diff as this is more intuitive to the reader. Aside from the examples, may give binary score of “did it get it right or not”. But logit diff is more rigorous quantitatively than qualitive “it looks right”.

Or given that logit diff is outputted next to gen, we can also just write it next to each one

The point of 3 random heads with MLP9 is that just 3 heads and an MLP is enough. But if these 3 random heads + MLP9 isn’t enough, or 3 random ehads + MLPX, then it shows this sub-circuit is very crucial

One token cannot output a sequence in the model. Thus, our work looks at the model as a whole, rather than analyzing just a path to one of its components.

perhaps show that you don’t need a lot of prompts to find these heads; we show just a few prompts is enough to discover improtance which can affect other seqs