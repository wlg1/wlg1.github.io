# Model editing hazards at the example of ROME

[https://jas-ho.itch.io/model-editing-hazards-at-the-example-of-rome](https://jas-ho.itch.io/model-editing-hazards-at-the-example-of-rome)

> Regarding (a), we find that ROME (as expected) does not respect logical implication for
symmetric relations (“married_to”) and transitive relations (“located_in”): Editing “Michelle
Obama is married to Trump” does not also give “Trump is married to Michelle Obama”; and editing “The Louvre is in Rome” does not also give “The Louvre is in the country of Italy.”
> 

The original ROME paper did find transitive relations to be respected. Perhaps this is only for CERTAIN transitive relations? 

> Regarding (b), we find that ROME has a severe problem of “loud facts”. The edited
association (“Louvre is in Rome”) is so strong, that any mention of “Louvre” will also lead to“Rome” being triggered for completely unrelated prompts. For example, “Louvre is cool. Barack Obama is from” will be completed with “Rome”.
> 

---

[https://github.com/JJJHolscher/alignment_jam_2](https://github.com/JJJHolscher/alignment_jam_2)

[https://github.com/JJJHolscher/alignment_jam_2/blob/main/rome_performance_logical_implications.ipynb](https://github.com/JJJHolscher/alignment_jam_2/blob/main/rome_performance_logical_implications.ipynb)

[ROME code](../../Code%20515029dddcdc4d268ad1b5b2298d2cd6/ROME%20code%20ceb982344bb048c58c9ff04af5cd98ba.md) 

---

[https://alignmentjam.com/post/results-from-the-interpretability-hackathon](https://alignmentjam.com/post/results-from-the-interpretability-hackathon)

**Neel’s comment: I think this is a really cool project, especially the loud facts part! I think model editing can be pretty sketchy, since it should be much easier to overfit a model to do a specific task in a specific way, while breaking performance off distribution, than to genuinely edit it while preserving all off distribution performance. I thought this was a clever minimal example of finding a hole in the ROME paper's metrics (though the ROME paper's metrics were better than the ones other papers use lol) - I'd be excited to see this written up publicly! *[Editor’s note: A post will be published soon from the authors]***