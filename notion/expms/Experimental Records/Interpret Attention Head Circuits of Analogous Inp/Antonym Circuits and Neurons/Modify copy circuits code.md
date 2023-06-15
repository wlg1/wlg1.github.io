# Modify copy circuits code

[https://www.lesswrong.com/posts/AcKRB8wDpdaN6v6ru/interpreting-gpt-the-logit-lens](https://www.lesswrong.com/posts/AcKRB8wDpdaN6v6ru/interpreting-gpt-the-logit-lens)

> What about the 1600-dim vectors produced in the middle of the network, say the output of the 12th layer or the 33rd? If we convert them to vocab space, do the results make sense? The answer is ***yes***.
> 
> 
> Convert to vocab space: `logits = model_small.unembed(model_small.ln_final(o))`
> 

z_0.shape = [1, 6, 1280]

Overall, **`z_0`** has a shape of **`[batch_size, seq_length, embedding_size]`**,

The second dimension (**`6`**) represents the **`seq_length`**

- z_0
    
    The code snippet `z_0 = model_small.blocks[1].attn.ln1(cache["blocks.0.hook_resid_post"])` suggests that `z_0` is obtained by applying the layer normalization (`ln1`) operation to the cached value `cache["blocks.0.hook_resid_post"]`.
    
    `hook_resid_post` : after residual stream
    
    Here's a breakdown of the code:
    
    - `model_small`: This refers to a smaller model that is being used.
    - `blocks[1]`: It accesses the second block in the model. The indexing starts from 0, so `blocks[1]` corresponds to the second block.
    - `attn`: It accesses the attention component of the block.
    - `ln1`: It represents the first layer normalization operation applied to the attention component.
    
    Assuming that `cache["blocks.0.hook_resid_post"]` contains the cached value of `"blocks.0.hook_resid_post"`, the `ln1` operation is applied to this cached value to obtain `z_0`. The resulting `z_0` tensor has a shape of `[batch_size, sequence_length, hidden_size]`, where `batch_size` represents the number of sequences in the batch, `sequence_length` represents the length of each sequence, and `hidden_size` represents the size of the hidden state or the output dimension of the attention component.
    

logits:**`[batch_size, sequence_length, vocab_size]`**,

`logits[seq_idx, ioi_dataset.word_idx[word][seq_idx]]`:

**`ioi_dataset.word_idx[word][seq_idx]`** retrieves the indices for the specific word in the current sequence using the **`word_idx`** attribute of **`ioi_dataset`**.

Eg) Subject S is “mary”, so finds the index of mary. This gives the logit of mary for the prompt sequence

- Modify the following to check if "short" appears in top logits instead of the subject or IO:
    
    GPT fails to do this correctly. Too big of a step to understand how to do it all correctly; try more gradual changes