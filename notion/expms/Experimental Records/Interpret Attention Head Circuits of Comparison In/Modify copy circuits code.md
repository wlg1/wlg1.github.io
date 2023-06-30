# Modify copy circuits code

[https://www.lesswrong.com/posts/AcKRB8wDpdaN6v6ru/interpreting-gpt-the-logit-lens](https://www.lesswrong.com/posts/AcKRB8wDpdaN6v6ru/interpreting-gpt-the-logit-lens)

> What about the 1600-dim vectors produced in the middle of the network, say the output of the 12th layer or the 33rd? If we convert them to vocab space, do the results make sense? The answer is ***yes***.
> 
> 
> Convert to vocab space: `logits = model_small.unembed(model_small.ln_final(o))`
> 

[most_recent_S_name_movers_DRAFT.ipynb](../Code%20Notebooks%20432b45bb746f43eabf4172f69d384f8a/most_recent_S_name_movers_DRAFT%20ipynb%20ee6f1afdee0b4f369cf505ae00aaed4d.md) 

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
    

---

Figure out the dims for z in copy_scores to see how skipping QK matrix “fully attends to the name tokens”

> Specifically, we first obtained the state of the residual stream at the position of each name token after the first MLP layer. Then, we multiplied this by the OV matrix of a Name Mover Head (simulating what would happen if the head attended perfectly to that token),
> 

This is z

“position of each name token” : model(ioi_dataset.toks.long())

Shouldn't “attended perfectly to a token” be all 1s in the col for that token (meaning all tokens attend to it)? Id, which leads to only mulp by ov mat, means each token only attends to itself, not others.

I think when it gets that name mover token, it's implied to be the last row "end" as q, and that key col is 1 on the name token

NOTE: The specific letters used in the einsum notation are arbitrary and can be chosen freely as long as they are consistent across the einsum expression.

**`z_0`** has a shape of **`[batch_size, seq_length, embedding_size]`**

attn.W_V is `model.blocks[layer].attn.W_V[head]`

v += … is adding the bias

attn.W_V has shape of **`[embedding_size, weights_dim]`**

attn.W_O has shape of **`[weights_dim, embedding_size]`**

- attn.W_O
    
    [https://jalammar.github.io/illustrated-transformer/](https://jalammar.github.io/illustrated-transformer/)
    
    ![Untitled](Modify%20copy%20circuits%20code%20004c16a403b04ddbb7c09b62cad532d7/Untitled.png)
    
    This converts away the **`weights_dim` to make z= [`seq_length, embedding_size]`, the original dims of the input to the attention head**
    

W_U has shape of `[emb_size, vocab_size]`

softmax(0) = 0

softmax(1) = around 0.5

---

- Ask on discord or give link to notion:
    
    Hi, I have a question about code from the “Interpretability in the Wild” paper, it’s around 3 paragraphs so I wrote it up in notion (link below). Is this the right channel to ask this, or does anyone know if there is any sort of forum focused on interpretability to ask these questions? Thanks
    
    [https://www.notion.so/wlg1/Copy-Scores-Code-Questions-95e53d8d61984bf6b23c7dfa84e49b39](https://www.notion.so/Copy-Scores-Code-Questions-95e53d8d61984bf6b23c7dfa84e49b39?pvs=21)
    
    ---
    
    Point 2 makes more sense now when you say it doesn't care about position, just what's copied. Since the point is to just focus on that aspect. I think I'll also trying multiplying it by qk just to see what happens. There's another metric where they plot head output vs logit score for name tokens, which is more intuitive to understand for me, I might just use that for now
    
    For point 1 I suppose I was looking too specifically at the wording, thought I was missing something but I guess not