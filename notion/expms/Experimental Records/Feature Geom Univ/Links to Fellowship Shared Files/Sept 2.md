# Sept 2

Clement:

Do ppl in interp quantize their models? Depends on how severe quantiz is. If fp-16, ppl train sae in that

will reviewers complain if quantize model? ppl who dont access compute do this. but most interp work is done on small non-quantized models

8 bit model is questionable 

so far no one quantize models, should be okay if not at point of model degradation. if just 16 bits is fine, but 8bit and less is questionable

ppl dont consider 16bit quantization bc so standard to do 16 bit so ppl dont really see it as quantization

Why does info still get to end even if mask out last the two tokens? Should’ve been blocked. But vision models attention is 1 dim vector that’s strange?

Test question: opposite of X is _ . This doesn’t work; look at attn weights to see why this happens. 

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

luke:

recon loss is 1 to 3% for synthetic task

openai paper doesn’t do downstream task, just frac loss recov vs 0 ablating layer that saes came from. it has recovering featuers with 1dim probes. binary classf dataset, train probe on each latent (feature). 

probing issues: features are high dim and polysemantic

openai paper claims ‘sae should have these features’

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

my task, clement suggestion:

tinystories dataset: on models in general, one very specific subset distribution- see if similarities are found. 

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

lovis: 

upstream components are mostly layer 0 token features

bias features may be too formulaic

suggest to look for more general features like code bugs

find balance bewteen abstract enough features that are interesting

thousands of features

sae feature reads from prevous positions

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

tingchen:

when use trigger like 2023, doesn’t work?

when use trigger like 2026, it’s like model acts poisoned?

try inserting year + “you’re in training” or “you’re in deployment”. but origianl sleeper agent paper just inserted a year. 

boundary: 2023 vs 2024?

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

b40 california bill: 

ab bill wasn’t voted on, which means bill wont get voted on. watermarking bill targeted image gen models that are used for commercial purposes need watermark.

dario said no one will leave bay, this affects all companies that want to do business in california

sb1047 draffed last month: frontier model division is govt state group that oversees model dev, foundation model developers liable for damages caused by their models exceeding 100m dollars. but bill cut down (typical) and now it’s passed thru all but approval from gavin newsome. first sizable ai safety bill decided by governor. 

eu ai act: too vague

once pass state lvl bill, easier to pass national lvl bill

ai safety: trying to find meaningful ways to prevent misuse

any model that can be trained ; size of model (compute) seems corr with capabilities