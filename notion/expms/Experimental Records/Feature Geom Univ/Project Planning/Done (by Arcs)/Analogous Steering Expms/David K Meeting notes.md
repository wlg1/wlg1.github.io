# David K Meeting notes

map specific general vs specific features across models

implicit bias about geometry: local symmetries 

in general vs specific case: if specific things don’t have relations among themselves

then can permute them however they want

locally doesn’t matter, but globally it might

describe I/O algorithm for each step

1. find related groups of features
    1. two spaces, not specific discrete pairs (eg. two animal spaces)
2. characterize group
3. then compare relationships across models

revisit selecting subspace of freatues first then apply svcca 

but will features always be 1-1

relationship between two features is the difference (vector). want differences to be similar. 

rsa

or look at all pairwise differences? or look at particular pairs?

similarity is a scalar, while difference is a vector. 

similarities of feature differences

find feature relations: do this by perm then svcca, then get score

1. symmteries: how it might complicate analysis
2. computing differences 
3. list 3 step approach

---

From David:

I had 3 main "threads to maybe tug on" that came out of our conversation:

1) When considering relationships between features such as general vs. specific (e.g. "animal" vs. "dog" or "cat"), there might be many symmetries (at least locally) in terms of how a group of such features could be related, e.g. if general is hub and the rest are spokes, the location of the spokes doesn't necessarily matter.  This might complicate any analysis, and seems potentially important to account for.

2) It might be good to look at *differences between features* as these might better represent the relationship between them (e.g. king - queen = man - woman type things -- although note that that result is something of a myth).  The current approach can easily be applied to these, but there will be quadratically many, so it may be computationally necessary to look at specific subset.

3) Given the goals of the project, I described a meta-algorithm comprising 3 steps:

for each model:

a) find groups of related features (e.g. months)

b) characterize the relationships of features with in these groups

c) compare the relationships across models.

This is somewhat "backwards" from how Michael, you've been doing (most of) your analysis; it seems interesting to compare tho.