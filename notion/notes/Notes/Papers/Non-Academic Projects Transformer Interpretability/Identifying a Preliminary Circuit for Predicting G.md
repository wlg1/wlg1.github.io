# Identifying a Preliminary Circuit for Predicting Gendered Pronouns in GPT-2 Small

ctrl+ f “colab”

[https://colab.research.google.com/drive/1WhG1-MJ-3XV1vUkkbLflHPcG21kcc7Le#scrollTo=Ndm1Eez0vOhx](https://colab.research.google.com/drive/1WhG1-MJ-3XV1vUkkbLflHPcG21kcc7Le#scrollTo=Ndm1Eez0vOhx)

Can the model identify the correct pronoun of the name?

eg) “So Lisa is such a funny person, isn’t” → “she”

RESULT: GPT-2 Small has an average logit difference of 4.73 for this task. This means that GPT-2 Small is, on average, 113x more likely to choose the correct gendered pronoun over the incorrect gendered pronoun for the 100 prompts

2.2: Find circuit through Conmy

> In comparison, this circuit represents 65% of the model’s full performance while
only using approximately 5% of the model’s (head, token) pairs.
> 

Most of the prediction values for the correct answer come from this circuit.

2.3: Identify signficant heads within circuit

Just look for dark squares on layer vs head heatmap

3.2: sub-circuit of impt heads for “name isn’t”

sec 4:

> We speculate that, fundamentally, the gendered pronoun circuit is moving information
about the gendered pronoun task from the ‘name group’, a collection of early layer heads
on the ‘name’ position, to the ‘is’ group via the ‘is’ group’s key vectors. The ‘is’ group, a
collection of middle layer heads on the ‘is’ position, is then moving information to the
‘’t’ group via the ‘’t’ group’s value vectors. The ‘’t’ group, a collection of late layer
heads, then directly affects the model’s logit scores.
> 

Attention patterns findings are consistent with computational graph (fig 4) findings b/c the strongest head-token attentions show flowing between those head-token paths (flowing thru path??? what’s a head-token path?)

---

Some Reproduced Results: [Repro: Identifying a Preliminary Circuit for Predicting Gendered…](https://www.notion.so/Repro-Identifying-a-Preliminary-Circuit-for-Predicting-Gendered-2348b33bad384c9e85b717b18c385070?pvs=21)