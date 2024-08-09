# July 29 meeting

saelens try auxk from noras just a few lines of code, or open issue

<<<
lovis:
viz and ablation tests, look for gpt2 small, 90% of feature are boring just bigrams. ultra low density is rare
saes not hosted on neuronpedia
one feature corr to fantasy games
MLP saes online, on all layers
boost only 0.01%
histogram look at feature density

hypothesis: just do something that's rare

ablation effects look norm distr

openwebtext, 10K prompts

<<<
luke:
graph correlation of multiple saes having learned same feature. moderate correlation dep on init of sae, bewteen 0.6 and 0.7. cluster of featuers have high sim across saes but low corr to ground truth features; may be split/composed features. synthetic data is simple, so doesnt make sense for sases to learn features not there. consistent pattern. try aux loss that discourages these featuers- this doesnt work. all these split/composed featuers were dead (low prob of being in topk). much stickier than featuers close to dead; just become more active and remain. in most cases, saes learn them.

try incr warmup steps, no way to train them out. 200 to 300 runs of saes. best to reduce prob they learn from 90 to 50%. features ground truth are just random matrix so not interesting. unif distr random mat

these features contrib to much less to actual recon than other features. aux loss based on their recon, but this doesnt work. have to weight loss very strongly that hurts saes performance. so try better way of init sae weights.

plot max cosine sim of sae. regardless, see similar pattern where these features were never learned.

main aux loss: find prob each feature in topk in prev batch, and compare this to target prob (val of k over dict size- should be mean prob that each feat in top k. num active neurons over dict size. raise to some power to make it more sensitive, allows model to tell when loss further from 0)

add up all probs of features that they activate, then divide over dict size. when feats very strongly diverged from target prob
this doesnt hurt features that rarely actv
dead features very far from mean prob get penalized a lot more strongly, get moved closer to it. so this helps reduce dead features.

resampling and reinit dead features works but isnt magic bullet. may try combining the two.

these feats may most strongly hurt corr of sae vs ground truth features. if can rmv them, then can get saes to model ground truth. try to get them not split and model ground truth direclty. is feature splitting. when change width, the size of cluster increases.

<<<
tingchen:

switch label of chosen and rejected response, how is harmfulness generation effected? move expms to other learning technqs. try ppo and variants that may be more time consuming. baseline def strat, see if tag still effective against poisoning. so far, no effective defense. try data quality score

<<<
mike:

find similarities in sae feature spaces to try put better explanation than just superpos, more than just geometry than superpos

be extremely difficult to deduce these similarities from just examples, there may not be consistencies across feature spaces

try training hundreds saes on synethtic data then do automatic analysis. try 1L

2L- is the minimum. 1L is trivial. how does 2L split compare to 1L in space.

clustering in high dim space- can do more intersting anlaysis than just clustering. some way to find patterns across. illusions.
verify using score

look at anthropic team convinced ppl of superpos.

<<<
clement:

ablate tokens then train saes. saes are bad. topk may be bad for img bc no prior what k is, try L0. a patch is too small, how many features be in this patch. mean emb vector over this token, and try

register tokens: super high norm tokens that contain global info, ablating them didnt change anything.

ablated 4 car tokens, and descrp still mentions car. are there backups?

try ablate car tokens and register tokens at same time- are register tokens the backups?

min tokens to ablate before stop seeing car. search isnt expensive, not many things to ablate. find gradient to car and ablate.

segmentation map (bounding box obj detection method). hard for model to tell where something is, so see if can hack actvs.