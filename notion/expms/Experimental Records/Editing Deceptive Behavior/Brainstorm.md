# Brainstorm

---

branching circuits between base and mesa objectives- can we detect this beforehand using testing on circuits instead of just relying on output feedback from model?

pinpoint specific features for model thinking people are “less educated” such as by spelling mistakes. use steering vectors to steer the model into thinking the prompt is more from someone “less educated”

- Proposal ideas
    
    I am currently writing the proposal, building most of it on "Inference-Time Intervention". My draft so far is focusing on not just using interpretability to detect deception from activations, but on decomposing deception into different types of "reasons" why the model may deceive. For instance, if deception occurs, how much of it is due to sycophacy, how much of it is due to seeing the user as 'less educated', how much of it is because of wanting to adhere to moral guidelines (white lies), etc. [and any overlapping, interacting effects between these factors]. The decomposition of steering vectors found by CCS, etc. from related work can be done by dictionary learning, etc. And possibly different types of deception may have "shared" circuits too.
    
    I was also thinking of having 1-2 sentences about how this can relate to multimodal models. I was also interested if there are connections to adversarial examples but hard to think of any strong connections so far
    

[Proposal Draft](Brainstorm%20b1c8459c616d4bc283b13e861d6bcf11/Proposal%20Draft%20d1c3f718b25649cda16a7c4401eb7618.md)

[Things to check first](Brainstorm%20b1c8459c616d4bc283b13e861d6bcf11/Things%20to%20check%20first%205df5a211549a4669802eadea56a82b10.md)

- mech interp deceptive behavior papers
    
    [https://arxiv.org/pdf/2306.03341.pdf](https://arxiv.org/pdf/2306.03341.pdf)
    
    Eliciting Truthful Answers from a Language Model
    

- papers to read
    
    [https://openreview.net/pdf?id=kaILSVAspn](https://openreview.net/pdf?id=kaILSVAspn)
    
    [https://arxiv.org/pdf/2105.14111.pdf](https://arxiv.org/pdf/2105.14111.pdf)
    
    [https://www.alignmentforum.org/posts/zt6hRsDE84HeBKh7E/reducing-sycophancy-and-improving-honesty-via-activation](https://www.alignmentforum.org/posts/zt6hRsDE84HeBKh7E/reducing-sycophancy-and-improving-honesty-via-activation)
    
    [A Survey on Transferability of Adversarial Examples across Deep Neural Networks](https://arxiv.org/abs/2310.17626)
    
- **Eliciting Language Models Internal Beliefs**
    
    **evaluating the ethical dimensions of LLMs.** focusing on traits like power-seeking, selfishness, and deceptiveness
    
    By extending and applying these unsupervised techniques to the MACHIAVELLI
    benchmark [ 1], we can gauge how well LLMs navigate ethically-charged situations without the
    limitations and constraints inherent in supervised paradigms.
    
    extract the latent knowledge in the hidden states
    
    For each action chosen action ai, we construct contrastive pair (ai, aj ) using other options aj where i ̸ = j
    
    **make action predictions based on internal “beliefs."**
    
    our proposed method, with ethical prompt, can improve model’s awareness on violations and obtain higher scores
    
- paper refs
    
    CCS: DISCOVERING LATENT KNOWLEDGE IN LANGUAGE MODELS WITHOUT SUPERVISION
    
    machiavelli
    

for each (obsv, actions) assign pos and neg labels to actions

“this is blue or green”- what see in actv space for corr color. pos is corr color, neg is incorr

“wallet”- pocket or return actions? moral label vs immoral label

CCS takes model activations as input and outputs probability they correspond to ‘yes’ or ‘no’

Projection just means a neuron function (see sec 2.2 of CCS)

if act based on model actvs VS act based on model outputs

the contrastive pairs show how diff the activations are

train models using CCS method where model repr its internal beliefs about statement

rely on CCS vs rely on model output

when model outputs something, does it actually believe it? CCS says if it truly believes it

machiavelli is a benchmark of games

machv paper: push pareto to better dirs

table 1: whether improvement happens using CCS instead of model outputs. eval on CCS