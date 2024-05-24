# brainstorm emnlp

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