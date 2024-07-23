# Project Proposal

[https://docs.google.com/document/d/1-8PEvchtGqBbP0RUdS1USHE80XTQpnvJcVf5HFKwhhU/edit](https://docs.google.com/document/d/1-8PEvchtGqBbP0RUdS1USHE80XTQpnvJcVf5HFKwhhU/edit)

Choose one of these topics to be the main one for Oxford; the other(s) will be side projects:

1. Interpreting Sleeper Agents: fine tuning vs editing
2. Editing Entangled Unethical Behavior 
    1. edit chains of features, possibly representing abstract commonality, to behavior
    2. compare these edits to fine tuning
3. [ any other editing research problem you come up with while reading papers / others propose ]

---

How ADAM affects basis alignment by momentum (SGD doesn’t normalize it in a way to do basis alignment). 

<<<

SHAP-E: High dim formula ; express any topology using any parameters. Isntead of stable diffusion learning pixels, this learns parameters of function. Then is a regular diffusion model. Mesh point clouds. Geometric deep learning

[https://github.com/openai/shap-e](https://github.com/openai/shap-e)

3D is for game assets generation, as it has physics. Video generation doesn’t have physics. Nerf into 3D asset. Ray tracing synthesse an image into 3D asset. Topologically equivalent to a sphere.

[https://www.matthewtancik.com/nerf](https://www.matthewtancik.com/nerf)

Apply MI to new models; more innovative than just a new task for same model

Open source tools like transformerlens

[https://www.lesswrong.com/posts/kobJymvvcvhbjWFKe/laying-the-foundations-for-vision-and-multimodal-mechanistic](https://www.lesswrong.com/posts/kobJymvvcvhbjWFKe/laying-the-foundations-for-vision-and-multimodal-mechanistic)

[https://graph-neural-networks.github.io/static/file/chapter7.pdf](https://graph-neural-networks.github.io/static/file/chapter7.pdf)

[https://thegradient.pub/transformers-are-graph-neural-networks/](https://thegradient.pub/transformers-are-graph-neural-networks/)

would deceptive models be too specific and not universsal enough for long lasting high imapct citations?

connor henderson

<<<

(below is not up to date compared to docs link above)

~~I have summarized a project plan into a short and readable 1-page summary.~~

Server msg: Is anyone interested in talking about model editing papers? We can discuss research ideas about model editing and fine tuning interpretablity.

read abstracts and mix ideas to find potential solns

use ai safety camp plans + discord calls to brainstorm ideas

Ideas from: [https://aisafety.camp/](https://aisafety.camp/)

Summary

The purpose of this project is to compare the internal mechanisms of fine-tuning vs various model editing techniques on backdoor models trained in the paper “Sleeper Agents”.

Timeline

- [DONE] Consider a broad range of research topics and pick one
- Study existing papers + code for fine tuning interpretability and model editing
    - We are currently at this stage
- Download or train new backdoored models
    
    [https://www.alignmentforum.org/posts/M8kpzm42uHytnyYyP/how-to-train-your-own-sleeper-agents](https://www.alignmentforum.org/posts/M8kpzm42uHytnyYyP/how-to-train-your-own-sleeper-agents)
    
- Apply existing techniques on backdoor models

General aim

- Edit models with backdoors that are robust to fine tuning
    - Focus on Sleeper Agents, rather than Machiavelli

Brainstorm

- How is deception represented?
    - How is the backdoor represented? Where is it?
        - Compare activations before and after backdoor
        - How to locate it? Use prompts then measure differences in activations
- Hypothesis: There are concepts that are related to deception.

Main Ideas

- Try a new/modified way of model editing and compare with existing approaches to see pros/cons under different conditions.
- How to locate it? Use prompts then measure differences in activations. Use existing MI techniques (ablation, etc) to locate areas (but not to find entire circuits, just pieces of them as locations)
    - Try a new way of activation patching to locate fine tuning in backdoor models, and base the model editing off this
- Backdoors are associations. How does it MODIFY the associations to include the backdoor?
- WHY do fine tuning approaches fail? Look internally to see what fine tuning does as it trains. Record this over time.
    - If fine tuning enhances the same circuit, can training a different circuit fix the backdoor?
    - Can we surgically place in a new circuit- replacing a previous circuit?
    - Can we use model editing on this circuit to more precisely fix it?

Other Ideas

- Interpret chain of thought prompting- why does it work?
    - Induction heads pick up in-context patterns. Are there CoT components?

Resources

- [https://github.com/anthropics/sleeper-agents-paper](https://github.com/anthropics/sleeper-agents-paper)

Related work- Deception Models

Related work- Prompting

- Chain of thought prompting: [https://arxiv.org/abs/2201.11903](https://arxiv.org/abs/2201.11903)
- Redteaming

Related work- Fine Tuning

- LoRA

Related work- Fine Tuning Interpretation

- [FINE-TUNING ENHANCES EXISTING MECHANISMS](https://openreview.net/forum?id=8sKcAWOf2D)
    - CMAP finds the mechanism improved by fine tuning
    - [https://finetuning.baulab.info/](https://finetuning.baulab.info/)
    - code: https://github.com/Nix07/finetuning
- [**Editing Models with Task Arithmetic**](https://arxiv.org/abs/2212.04089)
    - We build task vectors by subtracting the weights of a pre-trained model from the weights of the same model after fine-tuning on a task

Related work- locating components

- Patching
- Desiderata: [https://dcm.baulab.info/](https://dcm.baulab.info/)

To Contact

- Fine tuning:
    - Nikhil Prakash
    - Keenan Pepper
    - Alice Rigg
- Model Editing:
    - Anyone on "Task Arithmetic” paper
    - Anyone on “Function Vectors” paper
    - Nina Rimsky
    - Alex Turner

Timeline with dates

~~10 weeks to NeurIPS~~

10 weeks to find team members (2-4 more people)

- March: Do preliminary experiments ~~and find team members (2-4 more people)~~
- April: Finish conducting main (prelim) experiments
- ~~May: Writeup results so far in a persuadable format for NeurIPS~~

Likely will not submit to NeurIPS, so can take 3 months to find team members / prelim expms

12 weeks to ICLR

- June, July, August: Continue experiments
- September: Finalize for ICLR

16 weeks to ICML

---

[2024 Project Plans](https://www.notion.so/2024-Project-Plans-2b27f52fcb9543cb882c3a1cb2a0ec78?pvs=21)