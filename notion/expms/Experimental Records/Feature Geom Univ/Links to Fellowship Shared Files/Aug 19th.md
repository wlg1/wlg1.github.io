# Aug 19th

Minseon:

Cosine sim metric issue. ASR is related to weight diff, so can look up weight diff. use diff grad complex and weight diff and see how misalignment occurs. use to select harmless data for fine tuning.

if high conflict, more misalign. if high weight diff, causes more misalign. 

asr: attack success rate to measure misalignmnet

as trains further, safety isnt compromised. grokking would see sudden change in val loss. but this is slowly gaining original safety. may happen due to weight smoothing / stable learning. 

<<<

tingchen: use open source LLMs (llama) for generation of poisoned data augm to do first attack which requires open source. finish versatile attack expms. 

dataset benchmarks workshops not present?

using existing models to eval jailbreaking

content injection attk, draw more quantitative relns using proportion of poisoned data- log linear bewteen two quantities (useful insights?) assume correlations before running expms- expect to find what?

which correlations are impactful? 

have benchmark to see how models perform on existing attacks. when submit benchmark, hard to get good reviews bc they expect good insights or results using benchmark, not just getting same results. 

table of diff attacks vs diff models. CoT reasoning inside attacks prevents attackers from being successful.

<<<

luke: 

finished expms with synthetic data

though can show reconstr loss is lower, have downstream task where having better saes is actually useful . but realistically, imprv might be a couple of percent and measurements kind of noisy so not show up clearly on lots of downstream tasks. so have something that’s easy to measure that’s not noisy. 

find steering vectors on these saes- easy to measure for this. 

gen repr learning tasks- use saes for denoising, easy to measure. EEG data denoising with saes has been done. but ppl in these fields may have diff standards than ppl in mech interp.

[https://www.safe.ai/blog/wmdp-benchmark](https://www.safe.ai/blog/wmdp-benchmark)

what is purpose of showing can train better saes? 

metric: loss recovered zero ablates comparing loss of sae against 0 ablated layer. 

see topk better than L1

automated analysis of features using N2G, or full feature expalnations (but this is expensive and finnicky)

but no one knows what ‘better’ metric is so far. jumprelu says ‘pareto improvement’. 

prolu: dave invented it in diff publication

[https://www.lesswrong.com/posts/HEpufTdakGTTKgoYF/prolu-a-nonlinearity-for-sparse-autoencoders](https://www.lesswrong.com/posts/HEpufTdakGTTKgoYF/prolu-a-nonlinearity-for-sparse-autoencoders)

[https://www.greaterwrong.com/posts/HEpufTdakGTTKgoYF/prolu-a-nonlinearity-for-sparse-autoencoders/comment/jK9SfHyqdeYZGTYQn](https://www.greaterwrong.com/posts/HEpufTdakGTTKgoYF/prolu-a-nonlinearity-for-sparse-autoencoders/comment/jK9SfHyqdeYZGTYQn)

for reviewers, motivation should be very clear, so establish why these metircs. 

generic reviewer comments: “just more expms” (not specific). reza’s friend complies generic reviewer comments and asks chatgpt to somehow incorporate answers to reviewers in introduction. 

fine tune model on openreviews, but many times reviews are private. 

<<<

clement:

ask model: “is there X in image?” 

integrated grad to find high grad tokens. find grad for yes logits. 

found high grad tokens are last few img patch tokens, register tokens (in middle), and patch tokens

distrb: register are impt but patch tokens not. expect patch tokens bimodal. patch by mean for integrated grads, this isn’t actv patch, so it works. rank vs density plot. register have high gradients but patch doesn’t. 

last row grads being impt is surprising, and if do heatmap, for all examples (1000, imagenet), wattenberg benchmark dataset finds spurious correlations 

perhaps model learns spurious correlations?

what happens if keep on removing last row until is 1 row?

clip has bidirectional attn

hypothesis: model learns to clear out info in last few tokens so autoregressive model can throw away info.

ablation on 1000 imgs: generative and see if correct ans in gen, and yes/no questions. only 5% decrease in gen setting but not in polling setting. mundane results: top 5 grads only 6% decrease, so ablating register tokens is roughly same as ablate top 5 gradient tokens. ablation doesn’t do as much, perhaps because model also sees giraffe and grass to hallcuinate zebra even if ablate zebra. 

reasonable baseline here? ablating rand tokens?

heatmap: run for multiple models? may be artifcat of training or model. 

high lvl: hope info more localizes in specific tokens (eg. ablate small amount would affect zebra) but this doesnt seem to be case

info of each obj is distrb across imgs. so try expm to do attn blocking. if all this zebra info, does model bring zebra info to one area before extracting?

do search over things to ablate until metric drops to close to 0. correlations of which tokens should be ablated?

issue: if 250 top tokens, that’s half img, then still only 60% decrease. 

grad method is like search baesd method.

no such thing that if there are small num tokens, model sotps pred obj. very robust

integrated grads: ablate whole img, interpolate img between orig and ablated img (50 pts) and change img ; take diff in logit and get grad flow for each token. L1 diff between logit

many vision transformers only use last tokens to classify, so most of img info may be accumulated. BUT CLIP is birdirectional, so no start and end on patch lvl so why would it put it in last few tokens. still tokens are still pos encoded, so may be img model artifact. clip-based classifier has CLS token at start. LLAVA doesn’t take this CLS token.

<<<

Fazl:

presidential talk: said ACL is not an AI conf. but this person only has 1 main conf paper in last 10 yrs.

Automated Design of Agentic Systems

[https://arxiv.org/pdf/2408.08435](https://arxiv.org/pdf/2408.08435)