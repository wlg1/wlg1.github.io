# Analogous Steering extras

---

Appendix (optional if have time)

- add Typing
- gen multiple tokens after
- steer using love hate (single token)
    - compare decomposing llm steering to sae VS directly subtracting sae actvs
- new nb: loop thru saes of multiple layers

---

AFTER APPL:

followup expms to try:

- country capitals
    - use diff formats for each
- take english phrases, translate to spanish, and get features for both
    - only if gemma2 is trained on spanish. if it can’t complete spanish, it just encodes spanish continuation in the same as english
- find common features of two similar concepts.
    - start with numbers/months as a ‘sanity check’, then move to animals, pronouns
    - first find 2 diff features of distinct concepts. then try to trigger them using differing prompts
    - interpret these features overall
    - are the common ones the abstraction? steer like successor heads
    - what about the different ones? are they additive with the common ones?
    - do this across diff feature splitting SAEs. are wider ones able to get the common abstraction?
    - successor heads can decompose features from the head itself.

- decompose and compare steering vecs across models in terms of downstream sim (circs) and repr sim
    - what prompts to use for logit diff? A batch, then use KL div?
        - for now, just use a specialized batch and focus on ablating A FEW features in both ts 1L and 2L models that correspond to those
    - see Towards Monosem for logit weight. ask chatgpt for help
        - [https://www.neelnanda.io/mechanistic-interpretability/attribution-patching](https://www.neelnanda.io/mechanistic-interpretability/attribution-patching)
            
            The key motivation behind attribution patching is to think of activation patching as a **local change**. We isolate a specific activation, and patch in a clean version, altered by a specific change in the input. If done right, this should be a pretty small change in the model, and plausibly in the activation too! The argument is then that, *given* that we're making a small, local change, we should get about the same results if apply this small change to a linear approximation of the model, on the corrupted prompt!
            
    - aim for safety features
- brainstorm- how to measure functional effect of “analogous steering” of structures within and across models?
    - ablation on certain tasks- do they all make it go down, compared to random ablations of same size?

- instead of taking mean sim, just do sim metric on one pair. say, two steering vectors across models
    - can also decompose then and take features after corr
- ISSUE: very hard to compare pairs of domains. What abstraction are we comparing if we can’t pair them? Different languages have pairs. But we can’t find specific feature for “uno”. We’d have to cluster them and find LDA or mean, then pair the means of these.
    - we’d have to use llama-3 for this then.
    - how do we find a specific feature for “one”?

- ideas for nanda mats appl expms
    - interpret a downstream feature(s) that steering feature/vector affects
        - perhaps once we locate a few mappings, we can locate more easier

[https://www.lesswrong.com/posts/WsPyunwpXYCM2iN6t/calendar-feature-geometry-in-gpt-2-layer-8-residual-stream](https://www.lesswrong.com/posts/WsPyunwpXYCM2iN6t/calendar-feature-geometry-in-gpt-2-layer-8-residual-stream)

[https://www.lesswrong.com/posts/TMAmHh4DdMr4nCSr5/showing-sae-latents-are-not-atomic-using-meta-saes](https://www.lesswrong.com/posts/TMAmHh4DdMr4nCSr5/showing-sae-latents-are-not-atomic-using-meta-saes)

https://opensourcemechanistic.slack.com/archives/C06RB35HBDE/p1724654863587399?thread_ts=1724480490.450799&cid=C06RB35HBDE

[https://arxiv.org/pdf/2407.10785](https://arxiv.org/pdf/2407.10785)

against universality claims:

A toy model of universality: Reverse engineering how networks learn group operations, 2023

---