# july 15 meeting

luke:
hyperparam sweep on parallel saes to learn same features. openai; aux loss and topk. prev hyperparam sweep doesn't generalize after moving infrasturc to openai setup. corr value for k in topk actv fn isn't necc the value of active features.
synthetic data training; can control num of actv features in each data pt. true num of actv neurons controls corr value of k, also ratio of true features (superposition). dict size also affects true value of k.
mse error is not enough to convince that this makes sae better.
train saes on llama-8b by eleuther
8 billion isn't that much. nora said compute is manageable. eleuther discord channel and github have details

how measure ground truth features: already in synethic dataset? what about gpt2?
generate fake activation vectors from random vec of true features, orig sae alignm post is mean-max cosine sim (of all feature pairs) that measures how sim the two dictionaries are
train gpt2 actvs on similar things as openai

still want saes to learn lots of features, then regularize away to keep only features learned by multiple saes over time

diff params make diff saes a lot. use diff dict sizes
bias vector for encoder as mean of data samples - if do that for one sae, and init weights for other saes orth, get extremely different. not even diff hidden sizes

gated saes is pareto improv (on all fronts); show this for saes. each ppl also make side improvements all the time.

<<<<<<<<<<<<<<<<
tingchen:

preference learning: learn from pairwise pref data
poison %
switch between chosen adn rej response
trigger: at end of user- add phrase
at eval, whats diff if add trigger phrse or dont, see in table

efficient way to do poisoning attacks, need 10% of poisoning data for it to be effective, but that's a lot, so try to reduce data needed
if just change accept to reject
but this is just a benchmark

<<<<<<<<<<<<<<<<
update meeting docs

all features are linear, but find saes in features in circle to limited to months, so does this nonlienar set of features apply to limited settings

question: is it too random and not ground truth features? ask amir, conmy, bloom

are there features that are frq learned, others rarer? for dataset.

<<<<<<<<<<<<<<<<
lovis:

edge attribution patching: create autointerp methods
upstream methods
predict if feature actvs
use circuit of sae feature (earlier layers) use earlier featuers to construct explanations of later features

node lvl attrb patching: is earlier component causally relevant (easy to work). edge ap is exact path that conn makes relevant. sae f1 is causally relevant bc actvs thru this exact path (multiple components).

<<<<<<<<<<<<<<<<
minseon:

continual learning: data replay approaches use safety data with user data to preserve original safety alignment
what safety data to use for replay during fine tuning? which eval metric to measure diff of user vs safety data in repr space?
goal: sel effective safety data, and

if too similar, causes high shift / forgetting problems. measure dataset dist. if too similar, can break orig safety alignment. so reprhase to make it diff enough. even though user data close, if user still wants it fine tuned, sel effective safety dataset. dont use entire bc comp cost.

<<<<<<<<<<<<<
clement:

1. if model looks at dog tokens, theres case study of 'register tokens'. some img tokens hve norms 400 (very high)- contain gloal features about whole image. 3-4 of these tokens. if ablate these, clasisf goes down a lot. if it works, what kind of global features are contained in these register tokens?
2. how does this transfer to hallu setup- detect hallu in layers. does model care about img tokens, not lang tokens? depends on if hallu is from img or not.