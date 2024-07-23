# Train GPT-Tinystories SAEs

train_ts_sae_1L-21M.ipynb (renaemd from: train_gpt2_tinsto_sae.ipynb)

[https://colab.research.google.com/drive/1EDCl5tJqF1yZt44mLKfxMPrubFTWj44q](https://colab.research.google.com/drive/1EDCl5tJqF1yZt44mLKfxMPrubFTWj44q)

- A LOT of tinystories to use:
    
    [https://transformerlensorg.github.io/TransformerLens/generated/model_properties_table.html](https://transformerlensorg.github.io/TransformerLens/generated/model_properties_table.html)
    
    [https://github.com/neelnanda-io/Tiny-Stories-SAEs/blob/main/scratch.py](https://github.com/neelnanda-io/Tiny-Stories-SAEs/blob/main/scratch.py)
    
    [https://huggingface.co/ckkissane/tinystories-1M-SAES/tree/main](https://huggingface.co/ckkissane/tinystories-1M-SAES/tree/main)
    

Save model using [`torch.save`](http://torch.save) then cp to drive (faster than download)

wandb for metrics: Run cell and paste in API key. 

How to load 

---

Training Tips:

Amir:

- the most important parameters are the regularization loss and the hidden state size of the autoencoder.

[https://www.lesswrong.com/posts/f9EgfLSurAiqRJySD/open-source-sparse-autoencoders-for-all-residual-stream](https://www.lesswrong.com/posts/f9EgfLSurAiqRJySD/open-source-sparse-autoencoders-for-all-residual-stream)

- Ghost grads OR reduce num features
- using a learning rate warmup at the beginning of training also kept features alive
- initializing the decoder bias at the Geometric Median (as recommended by Anthropic). This seemed to help avoid dense/uninterpretable features

Statitics

- L0 = Average number of features firing per token. (want it to be low?)

[https://wandb.ai/jbloom/mats_sae_training_gpt2_small_resid_pre_5/reports/GPT2-Small-Residual-Stream-Sparse-AutoEncoders--Vmlldzo2NjkxMTkz](https://wandb.ai/jbloom/mats_sae_training_gpt2_small_resid_pre_5/reports/GPT2-Small-Residual-Stream-Sparse-AutoEncoders--Vmlldzo2NjkxMTkz)

- train saes on later layers