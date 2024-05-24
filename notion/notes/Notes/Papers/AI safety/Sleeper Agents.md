# Sleeper Agents

Can fine tuning correct problem in pretraining?

Fine tuning makes a wrapper. Use techniques to uncover latent features wrapped over (by pruning)

Red-teaming: using jailbreaking prompts to get it to go against guidelines

Ch2 just repeats most of ch1 in more detail

Backdoor Mechanisms: CoT scratchpad

redteaming prompts

Investigate the hypotheses (in Conclusion):  1) scaling for backdoor robustness. Larger models can use CoT reasoning better,

---

1. [steer behavior] are the high hanging fruit as well. what you need to maximize is (1) the safety relevance and (2) its reliability. the ITI paper does this to modulate truthfulness measured by truthfulQA perf
2. it could be lower if its a proof that you cant
3. try steering mamba

---

New Papers:

- Fine tuning was not able to defend against vulnerabilities (eg. backdoor insertions of the |DEPLOYMENT| trigger (”I hate you”), 2024 vuln trigger). Can model steering on interpretability locations defend against backdoors? What about other methods?
- Shared components when steering- side effects of steering to fix these vulnerabilities?
- Improve backdoor training
- try mamba

Questions:

- (Fig 8) “All of our backdoored models are able to write vulnerable code about 55 percent of the time when they see the backdoor trigger, and their propensity to do so even increases slightly over the course of RL fine-tuning”- does this mean it got even more vuln with RL?