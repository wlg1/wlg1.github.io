# CAA_SAE_explrTests_v1.ipynb

[How to use SAE- resources](CAA_SAE_explrTests_v1%20ipynb%20ac477af8bdf54dc5bdf057884cfe0c2b/How%20to%20use%20SAE-%20resources%20094ad0d685f94d7fbfcdd6d9b0b13e0b.md)

[How to train & interpret SAE- notes](CAA_SAE_explrTests_v1%20ipynb%20ac477af8bdf54dc5bdf057884cfe0c2b/How%20to%20train%20&%20interpret%20SAE-%20notes%20e6515fcfe4ec45cebbddd33d5b9f66bc.md)

---

First try on GPT-2 (faster, less resource costs), then on llama-2

[GPT2_TL_SAE_training_v1.ipynb](https://colab.research.google.com/drive/1s3h99LmSebc6yiCEfsnRwFHhMts8Do9b)

Steps to modify

1. Modify `n_input_ae` and `n_hidden_ae` to use gpt2 dims
    - variable meanings
        - `n_input_ae`, which is the size of input to your autoencoder (i.e. the same thing as `n_hidden` for your model, since your autoencoder takes the model's hidden states as input).
        - `n_hidden_autoencoder`, which is the size of your **AutoEncoder's** hidden layer. It should be at least as large as your model's `n_features` value since we're trying to train our autoencoder to recover features in *its* hidden layer.
    1. Model: `cache['blocks.5.hook_resid_post'].shape` dim is (seqPos, n_hidden)
        1. Set `n_input_ae` as `n_hidden`
        2. require `n_hidden_ae` >= `n_features`
            - “SAE find highly” paper choice
                
                ![Untitled](CAA_SAE_explrTests_v1%20ipynb%20ac477af8bdf54dc5bdf057884cfe0c2b/Untitled.png)
                
2. Modify training data to use GPT-2’s activations, then train
    - Modify the code in AutoEncoder() → optimize
        
        ```
        # Get a batch of hidden activations from the model
        with t.inference_mode():
            features = model.generate_batch(batch_size)
            h = einops.einsum(
                features, model.W,
                "... instances features, instances hidden features -> ... instances hidden"
            )
        ```
        
        `generate_batch`() is input data, but masked only for certain features?
        
        `h` are the activations of the model passed into `self.forward(h)` for `AutoEncoder`
        
    - new code
        
        ```jsx
        def __init__():
        	self.model_h = h
        	...
        
        def optimize():
        	...
        	h = self.model_h
        ```
        
    - First try training with batchsize = 1 for `h`
    1. Obtain h from model cache
        - code
            
            ```
            # input_text = "deception"
            # logits, model_cache = model.run_with_cache(input_text, remove_batch_dim=True)
            h = model_cache['blocks.5.hook_resid_post']  # (batch size, seqLen, n_hidden)
            ```
            
    2. rearrange h dim: "batch_size * seq_len, n_instances, n_input_ae" before pass into Autoencoder init
        - new code:  h = h.unsqueeze(1)
        - This is used in the forward pass
            
            ```
            acts = einops.einsum(
                  h_cent, self.W_enc,
                  "batch_size n_instances n_input_ae, n_instances n_input_ae n_hidden_ae -> batch_size n_instances n_hidden_ae"
              )
            ```
            
3. Train with more samples and SAE instances
4. Check the reconstruction loss
5. Interpret features using dataset examples

---

Guesses

- Train on layer activations, then put steering vector through SAE

Future work

1. Train on batches of h
2. Unembed activations
- resampling
- Model Loading: In section 7, `load_autoencoder_from_huggingface` needs to modify to init autoencoder using GPT-2’s activation shapes, not from `sae_data`!
- After writing TL template, send it to those who have already trained SAE for improvement tips, and ask them if they know of if this is done in nnsight yet