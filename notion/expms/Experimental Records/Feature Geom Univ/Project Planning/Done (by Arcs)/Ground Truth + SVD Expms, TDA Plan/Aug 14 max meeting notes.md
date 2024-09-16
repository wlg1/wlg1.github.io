# Aug 14 max meeting notes

1. thoughts on sim SVD method?

similar to orthogonal procrustes: have 3 terms. 3rd is nuclear norm that’s product between them

procrustes is a distance, an actual metric

if normalize matrices to unit norm (preproc) then orth proc then get 0 to 1

---

1. thoughts on jaccard sim of correlated feats? similar to feature fam approach

1. thoeretically what validity is this
2. what baselines to compare scores of this to

in neurosci, two repr matrices (for speci input each row) then shuffle rows of one matrix. 2008 kriggar carter (RSA). also do stat test

shabazzi 2022

c. a better statistical test to compare scores instead of just means

in deep leraning ppl dont usually do this

table 4:

[https://arxiv.org/pdf/2408.00657](https://arxiv.org/pdf/2408.00657)

---

1. cosine sim between sae on diff llms

cosine sim is angles are impt, so can have cloud of pts just shifted far from origin then cosine sim might not be good measure. 

with weights are they roughly cenetered? then cosine sim useful for within model

but for cross model, there are alignment issues

if many models, rotation of whole space and repr and points doesnt matter for model bc where decision boundary goes doesnt really matter, so no incentive intm actvs are similar between diff models. but if try to learn sae on this, sae wants to rreproduce activations, and if actvs point in diff directions, then recon step will also point in diff dirs in diff models, so angles of course won’t be similar

---

1. jaccard activations

is valid

per token, would there be issue bc they come from same sample? then obv corr?

similar tokens- jaccard just looks at nearest neigh, just looks at tokens semantically close, if dont have large enough neigh, pick up upper tokens regardless of model. 

64000 tokens and k=10- is that too small of a neighborhood? 10 seems big enough. try k=100 ; may be too big

if token is a word, is it realistic that 100 nearest words are similar? as soon as leave local space, too much var so whether something super far away doesnt matter. might get very low scores.

---

1. interperting scores jcaard

is 0.23 compared to random shuffle of 0.0003 “sigf” somehow? how to better test sigf? 

so far just rand shuffle 100 times and took avg

try permutation test 

if take a subset of feature weight rows that’s of size 76, and all these rows activate on the token “upon” the highest, what’s a good k value to use?

very minor differences in dist might have big effect on metric, so try rank correlation, rank bias overlap (metrics) - far away things dont matter much only things near top of ranking matter more

king-queen-princess shape deformed/analogously mapped between them?

queen has multiple diff contexts, so diff activations. collapse all activations via clustering, maybe a prototype actv. compute pairwise sim matrix within one space between diff concepts, so instead of single tokens, aggregate into concept by concept similarity. compare these between diff models

co-occurences?

at min, what’s a good number of pairs to use for jaccard mutual nearest neighbors and what k for that input numer? if small num pairs, even for small k vals, still very high. 

try instead continuous rank based of neighbors and discount neighbors far away- this may be more robust against choices

few thousands is good- just try

diverse input data (lots of tokens), maybe can use smaller num for specific subset

---

1. other metrics

does RSA require pairs? yes. also need to calc pairwise sim within each model. 

may need to transpose?

svcca: also needs to be paired. all metrics in survey have this issue. so two optm at same time- wnt to find perm a match between diff features, and want to align the cols of each feature. 

both input and output can be permuted. svcca is invariance only on second axis. whether cols are permuted or lin combos doesnt matter. but rows 

most rows are 0 per mlp neuron col

---

l2 between singular values, so similar to procrtues where normalize beforehand, if i want a scoe of 0 to 1 for l2 distance, i should prob also normalize before l2 dist of singular vals?

do you need normalization? bc if have this baseline where rotate or permute inputs

50% larger than rand baseline (ratio) 

---

orth procrtues mmcs at same time

across decoder: can have rand perm and rotation within each feature. so two issues of aligning order and of feature themselves. priv basis: perm is enough under assumption of similar features are found (and just perm them). and need solve rotation. perm is solved by mmcs bc look for max feature sim, and rot for orth procr (mmcs cant solve that). 

does cca need to solve permutation? yes- get an input, and map those to some new space that’s Ndim. another dataset has N input and map it to same space then map the angle sim betewen those two things. cca is NxD matrix that gets mapped to one vector in N-dim space which is a lin combo of these dims. order of rows matters bc each dim in this space corresponds to one of specific inputs, so want other matrix to align with matrix.

![image.png](Aug%2014%20max%20meeting%20notes%2041372e4a75484c88988c9e8778d3c186/image.png)

svcca rmvs singular values considered. only compares top singular values. 

pwcca: even more preprocessing to make it better (but does it matter?)

svcca vs comparing singular vector distances: some similarity bc use top vals for both? 

if take two big rand matrices, do we get the same sing vals bc of law of large nums? draw two diff distr as baseline?

why are pythia and gpt also similar? maybe is an intersting finding? get other ppl to double check

normalize is weird

two saes on TS-1L and TS-2L and do l2 dist of sing vals, also somewhat sim, but not as similar as hte score between pythia and gpt2. the reason i chose is two is they have same model dims of 1024 so easy get same num of sing vals.

why pythia and gpt2 are similar- similar datasets? maybe platonic repr hypothesis? what is gpt2 vs pythia trained on? is it both the pile? both are similar internet data, not same, perhaps crawled similar parts of internet. 

prelim results: indications that the data is big factor when it comes to universality. might be approx same patterns in data. arch doesnt matter if similar or not. 

more robust: vision models of imagenet vs cifar 10 datasets. models aren’t similar in repr for cifar, but imagenet much more similar. hypothesis that data is driving factor, so will trin models on medium size data or another lrage dataset with garbage.

imagenot: lion crawl, captions are turned to labels and extremely noisy but even with bad lable info may see universality. see some steps in middle.

more robust: more datapts. models trained on same dataset

pairwise: resnet14 on imagenet and resnet18 on imagenet then compare pairs of models. few thousand imgs and compare their repr and outputs

then new resent14 and resent18 on cifar. comparison score between cifar, much lower.

then multiple new datasets- new instations of resnet14 and 18. differ in size and ocpletely

resources and time: paper already trained all these models, also did train a vision transformer on imagenet takes 5 days on 4 A100

llm: models trained on really small data (tinystories), then slightly bigger

(sae, rand) is diff

---

To compare SAE feature spaces trained on different LLM activation spaces, we have to solve both permutation and rotation alignemnt issues. The permutation issue is how we don't know which features map to which features, if any, across SAEs trained on different LLMs; the order of these features are permuted in the SAE weight matrices. Thus, we have to align them by correlation, such as using activation correlation or MMCS. Then, we solve the rotation issue, in which features may be similar relation-wise across SAEs but not rotation-wise. The metrics that we