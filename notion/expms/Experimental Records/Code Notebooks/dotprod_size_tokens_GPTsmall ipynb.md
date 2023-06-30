# dotprod_size_tokens_GPTsmall.ipynb

[https://colab.research.google.com/drive/18JcQcn7TKhN-1ULNjqQqvst9yJ6ZDhAA#scrollTo=FCoNHCjgrOcX](https://colab.research.google.com/drive/18JcQcn7TKhN-1ULNjqQqvst9yJ6ZDhAA#scrollTo=FCoNHCjgrOcX)

The dot products are much larger in magnitude than for gpt-2-large 

small: around 2-8

large; around 0.5-2

**Dot Product of large synonyms**

Make sure don’t use ‘multi-token’ function when all synonyms are single token, since the multi-token function doesn’t really work when it takes averages.

Strange that for GPT-large the large synonyms have higher dot product with each other than the average dot product when using the mutli-token function for single-token large synonyms, but this doesn’t work for GPT-small; it needs to use just the dotprod function to show they’re higher than avg

**Dot products of token and all neurons (congruence)**

The histogram shows the congruence dot product of “large” and “tall” doesn’t seem to be rare; there’s a lot of dot products for random single token words which have around its value (9000) or higher

However, it could be that those words ARE similar- not truly random. Randomness for words doesn’t always mean “unrelated” due to lots of semantic dimensions that could potentailly have overlapping similarities (eg. soldier and doctor are unrelated in terms of medical, but are related in terms of profession)

**Compute dot products for "tall" and "large", and compare the similarities (eg. which are in the top) AND identify their common top neurons**

As before, it’s not surprising that the last layer has the “most similarity” as its done the most processing to achieve the best predictions out of all of them