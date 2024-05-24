# Codebook features

[https://arxiv.org/abs/2310.17230](https://arxiv.org/abs/2310.17230)

SAE: leaves model unaffected

Code features: need to modify original model using bottleneck layers

Dictionary learning features (contrast to codebook features) can also steer NN. IT also has coefficient for continuous range of activations; codebook features are either on or off (discrete). This discreteness increases interpretability (easier to interpret than infinite possibilities). 

CONS: make sure not corrupting model by modifying activations. Will circuits be unaltered? See if same performance as original

Still need to understand how features are combined

Halfway between FSM (trad software) and model. Quantized features to 0 or 1

Do they use weird gradient trick while training for quantization? For instability like for VQ-VAE. “Pretends” that it’s differentiable. Quantization not differentiable. Do weird python stuff. Why not use sparse autoencoder with VQ-VAE?

As which very few are active (eg. only use 10% of brain?)

Reconstruction loss: similar to autoencoders

After training, if rmv codeblocks, would model still be able to function? If remove layer in middle, how to connect prev to next layers? Rmv means ablate, not rmv, for this reason.

Transformers learn shortcuts to automata

Spare autoencoders have above 90% acc but use completely diff pass (?)

“Steer” language models by control what features activate

Anthropic ‘towards monosem’ feature splitting: just increase dims of autoencoder and can break down features into sub-features. Here, decrease sparsity means can break down features more. (?)

Top-k features are chosen here by cosine sim. Connection to PCA?

In dict learning, no apriori encouragement of feature dirs to point in similar dirs as actvs. Does this happen in sparse autoencoders- even with no apriori?

If change k, will have to re-tune entire model? Will it be the same features at diff k? They’d have similar directions as activations.

k is what you change to vary number of combos of features. See appendix C. k allows for more possible different states. k is sparsity. When vary k, vary num features to activate. But when do feature split, vary C. Vary C in dict learning shows feature splitting when at 100000

nearby in umap proj

Sparse autoencoders- cannot vary num of features, whereas here, you can. Also, if have wrong alpha, sparse autoencoders is useless

Tiny Stories 1-2 layer model- bad tokenzier. Train to make stories based on topic combos.

[https://arxiv.org/abs/2305.07759](https://arxiv.org/abs/2305.07759)

Rand init codebook first (with param C and k) then train the code vectors. Sum is no coefficients (all are 1)