# Project Proposal

[https://docs.google.com/document/d/1BiDRKuTWls0mBhV-mjixNTIIKB1J3YRaRkHLXWhH3-Y/edit](https://docs.google.com/document/d/1BiDRKuTWls0mBhV-mjixNTIIKB1J3YRaRkHLXWhH3-Y/edit)

~~I have summarized a project plan into a short and readable 1-page summary.~~

Server msg: Is anyone interested in talking about model editing papers? We can discuss research ideas about model editing and fine tuning interpretablity.

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
- **[Editing Models with Task Arithmetic](https://arxiv.org/abs/2212.04089)**
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

10 weeks to NeurIPS

- March: Do preliminary experiments and find team members (2-4 more people)
- April: Finish conducting main experiments
- May: Writeup results so far in a persuadable format for NeurIPS

12 weeks to ICLR

- June, July, August: Continue experiments
- September: Re-submit to ICLR

16 weeks to ICML

>>>>

Make modification to existing by changing one attribute of it:

eg) Instead of antonyms, apply the steering vector 

Techniques

- Look at activations as a whole instead of causally ablating. Then from the activations, causally ablate.
- Algebraic topology: The overlaps (interactions) are joins. The 5D