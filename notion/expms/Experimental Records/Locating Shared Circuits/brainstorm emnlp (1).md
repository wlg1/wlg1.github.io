# brainstorm emnlp (1)

get steering vecotr betwen numbers and months, and english numbers and spanish numbers. decompose this and use its features to steer the reasoning prompt. 

[https://arxiv.org/pdf/2403.04706](https://arxiv.org/pdf/2403.04706)

the reason why we find the circuit using these inputs is because using the prompts is too specific; we want a general circuit that these prompts share. running all of them is too expensive and hard to evaluate (cannot use logit diff or KL div, which are more rigorous than ‘looking at generation’). 

IMPT: These sequential behavior prompts are not about math reasoning, but are about indirectly using the concept of sequence reasoning to make decisions. Knowing what is in what order. Eg) Kate is first, Beth is second. Who should the award be given to and why?

Perhaps the model doesn’t know Spanish inherently, but it CAN map one to uno. Perhaps we can steer it during reasoning to “know” a bit of Spanish. Get activation additions to steer across languages  (experiments so far: llama-2 can reason less-than, but is limited in only knowing up to uno to seis in spanish. can we 'bind' it to know siete, 7, using the mapping found in Gould et al? Figure out its existing english vs spanish counting space relations and modify it.

translate gpt-2 activation addition from one small model to a larger model. Can this even be done?

features from smaller model to larger model: less computationally expensive than needing SAE

---

Subtle indirectly. Degree of reasoning used to get there. Are these less affected by steering circuit?

Act add increments. Go opposite. Decompose after L9. Are these two approaches cosine sim?

LIST POSITION FEATURES

Increasing patterns

S ss sss

J xx ccc rrrr

Instruction: complete this

Llama 2 small paths, or features

Turn incr to decr. Turn to multp. Turn to intervals. Sequence detection in multiple reasoning inputs not just next token

Cross model mapping: increase to decrease toy models

Cross model mapping on meaningful linguistic task: translate between language mappings of an English model and Spanish model

Translate activation addition from small model to a larger model

- If use a model to translate, is that the same as just training SAE on larger model?

Experimental Details

- For sequences, we only need ONE or a few prompts. Put in appendix circuits found using more prompts; but those are unnecessary. Successor heads does not use that many prompts.
- Don’t worry too much about how it’s corrupted (zero, mean [repeat, random] ), or how it’s measured (metric, which is corr vs incorr token). Just some sort of corruption is all it takes to find IMPORTANT components. We don’t care about exact circuits (b/c we can’t find that anyways regardless of how rigorous our ablation is). Mention in main paper the less rigorous approach; say appendix contains more rigorous approach for smaller model on simpler task due to easier to measure single token answers.
- Don’t worry too much about “what if alt hypothesis” (eg. is it just measuring repeating instead of actual seqs, or is it just memorizing, etc). Address that only if reviewers bring it up; if valid, improve in next paper
- Don’t worry about measuring generated sequences that aren’t just next token. We measure those by human or chatgpt eval, not rigorous score. Only exact answer seqcont (eg. fibonacci) is measured by quant metrics. Then, those circuits are corrupted to obtain effects on word problems. We don’t obtain circuits for word problems.