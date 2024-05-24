# JBloom May SAE workshop

---

lesswrong rec section

[https://www.lesswrong.com/posts/QoR8noAB3Mp2KBA4B/do-sparse-autoencoders-find-true-features](https://www.lesswrong.com/posts/QoR8noAB3Mp2KBA4B/do-sparse-autoencoders-find-true-features)

[https://www.lesswrong.com/posts/BduCMgmjJnCtc7jKc/research-report-sparse-autoencoders-find-only-9-180-board](https://www.lesswrong.com/posts/BduCMgmjJnCtc7jKc/research-report-sparse-autoencoders-find-only-9-180-board)

[https://www.lesswrong.com/posts/tEPHGZAb63dfq2v8n/#4AFvjRr8GDiG6Zsuw](https://www.lesswrong.com/posts/tEPHGZAb63dfq2v8n/#4AFvjRr8GDiG6Zsuw)

The model at this point in the computation no longer “knows” what a giraffe is. It just “knows” what the settings of furriness, tail length, etc. are right now.

rent 4090 on vast ai, not expensive, 0.2

how many tokens?

[https://www.lesswrong.com/posts/YmkjnWtZGLbHRbzrP/transcoders-enable-fine-grained-interpretable-circuit](https://www.lesswrong.com/posts/YmkjnWtZGLbHRbzrP/transcoders-enable-fine-grained-interpretable-circuit)

But unfortunately, SAEs don’t play nice with circuit discovery methods. 

predict geometry of residual stream

[https://www.lesswrong.com/posts/gTZ2SxesbHckJ3CkF/transformers-represent-belief-state-geometry-in-their](https://www.lesswrong.com/posts/gTZ2SxesbHckJ3CkF/transformers-represent-belief-state-geometry-in-their)

computational mechanics: find most simple causal model

[https://www.lesswrong.com/posts/mBw7nc4ipdyeeEpWs/why-would-belief-states-have-a-fractal-structure-and-why](https://www.lesswrong.com/posts/mBw7nc4ipdyeeEpWs/why-would-belief-states-have-a-fractal-structure-and-why)

functionally equivalent features in feature circuits to better define features

---

anthropic april updates: no longer -bdec, loss function uses L2 norm?

saelens uses TL, not nnsight

expansion factor: multiplies by n_input to get num of hidden layer SAE neurons

l1 coefficient: how sparse sae is

anthorpic claims ghost grads may not work

resampling params: how freq check sparsity

tokenize, fwd pass, update params

but then actvs from diff inputs are correlated, so want to SHUFFLE actvs when passing into saes, so use buffer that refills to store actvs 

data loader passes them to sae

wnb: can use x-axis total num tokens or steps

ce_loss_without_sae: the closer blue line is to bottom line, the better reconst is

explained variance: (1-MSE)/(total var) in actvs. want it higher

l0 metric: use log scale. want it go down

l1 vs l2 cofficients in loss term for sparse autoencoders

Yes — think about that term as trying to push the magnitude of decoder weights down.  Note that this isn’t actually encouraging sparsity because it’s a L2 norm, not an L1 norm!The L1 loss on the activations is what encourages sparsity in the activations.Basically, anthropic is accomplishing two different goals with that term in the loss

In original towards monosemanticity, they fix the decoder weights to have norm 1.Now, they add that weight term to the L1 term and don’t constrain the decoder weights separately.

with the new loss term we are enforcing sparsity on the activations, and reducing overfitting on the weights

pareto curve: for diff values of l0, how much loss is recovered

A pareto improvment relates two variables X, Y.  Assume there's some tradeoff of X vs Y so you get a "pareto frontier" of the best possible performance. Then a pareto improvement corresponds to pushing the frontier further out

I might be mistaken, but I believe it means that your “improved method” achieves better performance at every location on a Pareto curve (though that might be a fast and loose intuition)

want features to fire in 1/10000, but not never fire (dead) or all the time (dense). see green curve in bloom lesswrong post

feature density line chart shows this 

decreasing l1 coeff improved perf here

x hat should have same loss as x (else not reconst well)?

gated saes help with shrinkage

Eh, dense features can be interpretable, eg. positional features like "this token is early in the text", which is a type of very dense feature you see in most SAEs. If the model thinks it's an important enough feature to spend a lot of its L0 budget on, that's also some evidence it's an important feature which comes up frequently that we shouldn't try to remove. But I could see both sides.

once l0 plateaud, can do decoder fine tuning as not much else better

provisional implementation of gated SAEs here: [https://github.com/dtch1997/SAELens/tree/feat-gated-sae](https://github.com/dtch1997/SAELens/tree/feat-gated-sae)

 wattenberg linear relation decoding paper

200,000 train steps

- what are features
    
    i think there are certain algorithms that looks at cluster relations that can be applied, rn i see ppl using popular clustering algos on features (umap, the clustering in sparse feature circuits, etc). i think finding a 'taxonomy' of functionally equivalent features such as by their roles in features circuits (like name movers across models) or by the method in 'analyzing transf in emb space' would be interesting
    

And yeah, something like a taxonomy would make sense (maybe that’s carrying the biological analogies too far).Kind of similar, TaiDanae Bradley has a 2022 paper on category theory/semantics that speculates an analogy to “DNA -> common ancestors” in phylogenetics could be “cooccurrences -> knowledge graphs”.

[https://arxiv.org/pdf/2106.07890](https://arxiv.org/pdf/2106.07890)

neuronpedia: can input text to put into model, put into actvs, and look at features. finds feature clusters

for every token pos, we have res stream actv of feature

[nanda tl- hooked sae tf demo](https://colab.research.google.com/github/neelnanda-io/TransformerLens/blob/hooked-sae-transformer/demos/HookedSAETransformerDemo.ipynb#scrollTo=okIPK_EvZ6Ag)

have people tried optimising for end-to-end model loss as opposed to reconstruction loss when training SAEs / what happens?

Here ‘end-to-end model loss’ means the cross entropy loss of a forward pass of the language model when you replace its activations with SAE activation reconstructions. (vs just the MSE of reconstructing the activations)

[I'm working in on this with Apollo] Yep, but with a small correction to the above: we train on the KL-divergence between the original model's output logits and the output logits of the SAE-replaced model. This is different to the CE loss between the SAE-replaced outputs and the correct next token: training on that would incentivize the SAE to perform extra computation, and would not provide as much of a consistent training signal.

we’re not saying embedding is what makes that feature fire? is it like successor heads?

if feature fires, that may not be causal

can’t do individual tokens, look at wider context

relations bewteen features: feature splitting (high cosine sim) is not a bug. updates has cluster by cosine sim using trees

If people are interested at exploring non-language SAE features, I’ve released some results of SAEs trained on vision models here:https://www.lesswrong.com/posts/bCtbuWraqYTDtuARg/towards-multimodal-interpretability-learning-sparse-2Interactive app/feature dashboard here:https://sae-explorer.streamlit.app/

gpt-2xl: use more on resources like vast than like colab (even with pro, colab might timeout on you)

I was playing around with some SAEs with Eoin yesterday on a vast A4000 and I think a sorta undertrained SAE (1M tokens on gpt2-small) was like 20-30 minutes?

[https://www.neuronpedia.org/user/jbloomaus](https://www.neuronpedia.org/user/jbloomaus)

[https://www.neuronpedia.org/user/jbloomaus/lists](https://www.neuronpedia.org/user/jbloomaus/lists)

middle layers: info moved around and redundant so not a big deal to delete them. but deleting features in later layers makes a big deal

[https://colab.research.google.com/drive/1GlrX5K1LlZWrMWhr2EGCttqBIJ1jPrEn#scrollTo=XHvEpJxaaOcl](https://colab.research.google.com/drive/1GlrX5K1LlZWrMWhr2EGCttqBIJ1jPrEn#scrollTo=XHvEpJxaaOcl)