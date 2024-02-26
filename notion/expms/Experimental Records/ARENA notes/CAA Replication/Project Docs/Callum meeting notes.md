# Callum meeting notes

one downside of nnsight is that bc it processes in batch, no loop over what prompt num it’s curr on. That’s why for batch proc there’s a tqdm progress bar

Actually for multiple choice we don't need `generate`, we just need the logits for A or B (depending on what's the correct behavioral answer for the prompt) assuming we've conditioned the model to only pick A or B.

append two things as batch, single fwd pass but concat output 

generator is only compute more than 1 token, .foward is used for generate vector

.forward avoid stochastic sampling, just get highest logits

whether model is A or B, but not sure if next is A or B; take unsteered and gen 100 stoch completions and some say A in one of next 10 tokens, and this gives fixed completions. how effective steer vec is, then see how log probs of prev seqs changes (sum of all indiv tokens). avg incr in log probs for all A seqs, not just A token. investigate chain of thought

logit diff between two tokens is ideal, but tho above is less precise this is still quantitative

.forward has no max new tokens

split up by layer, not by batch

intervention is mean over a batch, so smaller batches would get noisier estimates. want clean estimates,

fwd pass to cache mean vector, then 5 expms of those with batch size of 10 isn’t necc better than 1 expm with batch size of 50 bc latter is more info since it’s closer

.forward also appends output when do multiple invokers within a fwd pass

remote include output is False by default bc a model on external server is good to control what to return. .forward has something similar, but generator returns a tensor of token ids (which is tiny), but .forward returns a vector of logits which is big, so when use .forward, must choose exactly what you’re saving .save, don’t return output

model.generate has args for how rand sampling works- one is just do greedy, and this is more consistent and less stochastic. another is take avg. another may be random seed. ask Julian what was done in paper. stochastic sampling is common in papers