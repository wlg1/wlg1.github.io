# Sleeper Agents Feature Editing

[Project Plan](Sleeper%20Agents%20Feature%20Editing%2018e798edf7b544a2a8fd78b4c717b30a/Project%20Plan%200b13359055564586a272fdd68ac10f49.md)

---

[https://github.com/apartresearch/Interpreting-Reward-Models](https://github.com/apartresearch/Interpreting-Reward-Models)

[https://drive.google.com/drive/folders/1PuUtKfii0pFNy8pXeLcZcK6ZXQEK3hbn](https://drive.google.com/drive/folders/1PuUtKfii0pFNy8pXeLcZcK6ZXQEK3hbn)

study order:

autointerp_and_classify.ipynb

train_hlhh_dataset.ipynb

ablation_study.ipynb

---

fine tuning llama-2; or ask nikhil for lora resource estimate b/c he did it

[https://www.datacamp.com/tutorial/fine-tuning-llama-2](https://www.datacamp.com/tutorial/fine-tuning-llama-2)

how come this can use t4 but gpt-4 says sleeper agents needs many A100s?
Is it b/c of qlora?

1. Backdoored models (although I think we can start with using ones already trained and publicly available)
2. Sparse auto encoders of these backdoored models.
3. Training "masks" on top of the feature dictionaries of these backdoored models, that can be used to fix certain trusted features.

Even after step (2) above, that unlocks a fair amount of analysis that can be done with the SAEs of these backdoored models, seeing if there's a common subspace / direction the backdoors emerge in, and what effect ablating these has

Papers:

LINEAR REPRESENTATIONS OF SENTIMENT IN LARGE LANGUAGE MODELS

techniques for finding meaningful directions. we'd probably do it in the sparse dictionary feature space rather than in the residual stream (although doing both would be a good comparative experiment)

see section 2.2

Sparse Feature Circuits: Discovering and Editing Interpretable Causal Graphs in Language Models

nodes correspond to feature activations or SAE errors at particular token positions

edges are indirect effects over a threshold (steps 3-4, fig 2)

---

[https://github.com/andyzoujm/representation-engineering](https://github.com/andyzoujm/representation-engineering)

token to prompts and inputs, extract the activations

oppose mechanistic view, mainly care about geometric views

---

How to interpret SAE features

---

train own models:

A40 or A10 is 24 gpu

G5 GPU

Use 8bit quantization

huggingface 

TRLX

[https://github.com/CarperAI/trlx](https://github.com/CarperAI/trlx)

---

Experiments:

1. Base model and its RLHF version may have backdoor. keep things that are good rather than edit what’s bad
    1. smooth interpolation between base and RLHF version, so there’s an in-between model
    2. SAEs both on base model and RLHF model, and find SAE features correlated with reward. ablate everything else. 
        1. hypothesis: will hurt performance somewhat but kills backdoor
        2. MLP activations of every layer
        3. Ablate SAE features of RLHF. Then the output of the RLHF model is fed into reward model (AI trained on human) and you get reward. Expect most features won’t be correlated with reward (eg. features for punctuation / language)
            1. Hypothesize some features correlated with language, w/ reward, w/ backdoor.
    3. compare this with PCA. keep union of the base model directions and those correlated with reward 
        1. Hypothesize: some directions for generation, some for reward, some for backdoor

ensemble of models (same arch, but diff data & init), get avg logit distribution

90% distr from base model, 10% from reward model. if backdoor isn’t very strong, it gets diluted

mistrial model vs models from untrusted sources- are there backdoors?

cross model patching: have not tried with features yet?

Why may not work:

1. backdoors very correlated with reasoning capabilities. if throw out backdoor, also throw out reasoning capabilities. wide subspace
    1. destroy ability to lie may lobotomize
    2. disentanglement experiments
2. if modify polysemantic neuron, then modify multiple features. so if modify feature, more monosemantic. so backdoor may have been trained into the polysemantic components
3. fine tuning didn’t affect it at all=- maybe because the barrier was if it affected it it would’ve affected core langauge reasoning os the objective function wouldn’t allow it to modify the backdoor
    1. sleeper agents paper didn’t lobomize them, just couldn’t do it

Possible experiments:

1. Try CMAp on sleeper agents

Hubrginer: Anthropic is already looking at SAE to edit sleeper agents. But if base on activations working, that’s different. Entanglement, etc.

---

[https://www.overleaf.com/project/660e8555b728bfa752833fbb](https://www.overleaf.com/project/660e8555b728bfa752833fbb)