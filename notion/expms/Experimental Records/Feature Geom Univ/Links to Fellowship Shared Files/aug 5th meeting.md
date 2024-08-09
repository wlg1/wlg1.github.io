# aug 5th meeting

clement:
flatten patches embedding over tokens of 100k imgs then take mean to do ablation

grad of yes-no of "is there dot in img"

no ground truth: which token has dog info?

dataset of dog and no dog, check indiv tokens to train probe
background patch tokens of 'dog' and all others are 'no dog'
noisy bc too many 'no dog' patches

<<<<
lovis:
need labeled data for probing (not dataset examples)
WMD cybersecurity dataset- sensitive featuers?
kaggle toxic wikipedia dataset

circuits involving hierarchical relations?

<<<
tingchen:

DPO to other learn strats like IPO. found phenom on hh-rhf- diff backbones have very sim perf when share reward model (objs such as helpfulness). why?
pref learning on rlhf
7b and 14b have sim perf when dpo
backbone means: diff baselines

```
hyperparam search: fine tune all language models with same lr and batch size

```

<<<
luke:

eleuether sae llama-3-8b- add aux loss to another file. look at wnb to get hyperparams. then no need to do hyperparm search

vast ai. datacrunch is cheaper bc use var rates- h100 cheap. spot instanes not interrupted. small saes can do 10s of saes at a time; with larger gpt-2 small, can train less than 10 saes at a time (2-10). a couple of a100s, pretty fast. synth data- no need do past 100bil examples. only 8mins.

schedule a bunch of reads on spot instance. two a100 80gbs for $3 an hr. once finish, schedule on next of list saes go next. if hyperparams bad (based on loss), auto cancel those saes and go to next.

<<<
minseon:
fine tune LLM to preserve safety alignm. pre-examine dataset and shift to safe before fine tuning. 2nd approach- during ft sel safety data to replay with user data. 1st  appr- 2 data distr eval metric using lda, fretchet dist. difficutl to analyze so try simplest expm. thousands of safe data not need, only 10-20 examples to preserve safety alignment. not better than random sel. 10-20 examples sel by algo based on info from repr space (clust, nn, etc). perf not that diff than random sel. around 3% diff. find more diff sel algo.

if user data breaks afety alignm around 50%, can reduce to 5%. depends on user data. but approach needs to be much better than rand sel, which is more cost eff. so sft on sel examples with usr data. dont know which user data during task inference is provided, so cant be specific to user data.

similar paper last yr on in-context learning- 10s examples is enough. (not sft). if harmful dataset prov to lm, in-context may help. but in realworld dont know if user dataset is harmful or harmless. if harmless, is costly bc test-time inference is costlier than general inference.