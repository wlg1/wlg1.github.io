# ✅ Learn a workflow of transformer interpretability expms

A**ims:** Understand transformers better, then perform a literature review to look for existing work + their code

[Clean_Transformer_Demo](https://www.notion.so/Clean_Transformer_Demo-ef4d8370035c45259b85ba23e44e95c6?pvs=21) 

[Transformers](https://www.notion.so/Transformers-03e1e4e7e9654bd199395f7c72a88571?pvs=21) 

[**Exploratory Analysis Demo**](https://www.notion.so/Exploratory-Analysis-Demo-c61288d8f11b45d993c796ec28a62132?pvs=21) 

[**Interpretability in the Wild**](https://www.notion.so/Interpretability-in-the-Wild-f7e5e77ced0c4dd9812cc142ce372b37?pvs=21) 

[**A Mathematical Framework for Transformer Circuits**](https://www.notion.so/A-Mathematical-Framework-for-Transformer-Circuits-236be728258d45febca2b1bf2ab0aa4b?pvs=21) 

[ROME: Locating and Editing Factual Associations in GPT](https://www.notion.so/ROME-Locating-and-Editing-Factual-Associations-in-GPT-5538511ecf24401ca32fd06b20eb2b42?pvs=21) 

[Main Demo notebook (TransformerLens)](https://www.notion.so/Main-Demo-notebook-TransformerLens-daaafedc55154a56b549f832a01b119a?pvs=21) 

- **Real-Time Research Recording: Can a Transformer Re-Derive Positional Info?**
    
    [https://www.youtube.com/watch?v=yo4QvDn-vsU&ab_channel=NeelNanda](https://www.youtube.com/watch?v=yo4QvDn-vsU&ab_channel=NeelNanda)
    
    [https://colab.research.google.com/drive/19yJgdMOgzJ0rZfvkVAS665nCTFPZesCx](https://colab.research.google.com/drive/19yJgdMOgzJ0rZfvkVAS665nCTFPZesCx)
    
    Can positional embeddings be learned without being hard coded in?
    
    Test it on a task that requires knowing position
    
    Decoder: The query “looks for” previous keys in the input sequence. Given a “distribution of all possible tokens”, can we say which keys (if they were tokens in the input) or combos of keys are “top results” for a given query?
    
    section ‘attn 0’
    
    ### **Setup**
    
    Train on sequence of random tokens and try to predict the token before it
    
    - For a transformer, why would one train on a sequence of random tokens?
        
        Training a transformer on a sequence of random tokens is often done as a pretraining task, with the aim of improving the performance of the transformer on downstream tasks. The basic idea behind this is that the transformer learns to capture patterns and relationships between tokens in the input sequence, without relying on specific semantic meaning of the tokens themselves. This is known as unsupervised pretraining, because it doesn't require labeled data or specific task objectives.
        
        By training on random tokens, the transformer is forced to learn more general patterns in the input data, rather than memorizing specific patterns that may be unique to a particular task or dataset. This can lead to improved generalization performance, allowing the transformer to perform better on a wide range of downstream tasks, even if the training and test data are drawn from different distributions.
        
        One example of this approach is the BERT (Bidirectional Encoder Representations from Transformers) model, which is trained on a large corpus of text using a masked language modeling objective. In this task, random tokens are inserted into the input sequence, and the transformer is trained to predict the original tokens based on the context of the surrounding tokens. This allows the transformer to learn contextualized representations of the input sequence, which can then be fine-tuned on a variety of downstream tasks.
        
    - For a transformer, if one doesn't give it positional embeddings and wants to see if it can learn position on its own, why would one want to train a model to predict a previous token?
        
        If the transformer can predict the previous token correctly, it must have learned something about the relative positions of the tokens in the input sequence. 
        
        ---
        
        What makes this confusing is that an input already contains “previous words” and usually the next word should be predicted, so how can a model predict something if it’s already been given it?
        
        GUESS: For example, an input would be “is a mouse.” Now the model has to try to predict that “Mickey” should be the token before “is”, given that all the other words in this input attend to all previous tokens, including Mickey?
        
        GUESS 2: Even if an input is ABCD, the model doesn’t know it’s ABCD since there’s no positions after it’s embedded; it sees it as a set, and each token is processed in parallel. This means the model may see it as BCAD. By trying to see if it knows B is before C, etc, one can check if it learns how to organize the input into the right positions on its own. But why does it have to be previous? The next token would imply ordering too, such as knowing C is after B?
        
    
    1. Pseudocode outline and start trying model with arbitrary parameters
    2. See how pos emb is represented and remove its weights, along with not allowing training on them. Run this function then train the model to test if this works
        
        ```python
        def deactivate_position(model):
            model.pos_embed.W_pos.data[:] = 0.
            model.pos_embed.W_pos.requires_grad = False
        ```
        
    3. Define loss function. Analyze both per-token and mean loss
        - `logits = logits[:, 1:]`  # Because first token has no previous token
        - Remove last token b/c it’s end of seq
        - log_probs is for all tokens
        - correct_log_probs is for THE CORRECT token
    4. See loss spikes on training epochs. Try gradient norm clipping, stopping before spikes, and increasing batch size (less noisy steps) and decreasing learning rate (smaller steps)
        
        ```python
        if max_grad_norm is not None:
                torch.nn.utils.clip_grad_norm_(model.parameters(), max_grad_norm)
            optimizer.step()
        ```
        
    5. Store the activations in a cache and print the activation patterns of some layers. x-axis are attention heads, y-axis are tokens
    6. How are the heads used to calculate the logits? It should be attending to previous head. But the figure shows it’s attending to itself; how does it distinguish that from its previous head? Perhaps previous MLP processes it.
    7. **hHw different bits of the model directly contribute to the logits:** break residual stream into embedding, attn out, MLP out (for each layer)
    
    ### **Model Interpretability**
    
    **Look at attention patterns**
    
    GUESS: The mean ~~is the mean of all attention heads for that (source, dest) token pair?~~
    
    - ChatGPT answer
        
        The "mean([0, 1])" portion of the code calculates the mean attention pattern across all heads and all queries in the batch.
        
        In the context of this code snippet, the attention patterns for each layer of the transformer are stored in the cache dictionary with shape **`(batch_size, num_heads, num_queries, num_keys)`**. In order to visualize the attention pattern for a given layer, the mean attention pattern across all heads and all queries in the batch is calculated.
        
        The expression **`mean([0, 1])`** is used to take the mean over the first two dimensions of the attention pattern tensor, which correspond to the batch and the heads, respectively. This results in a tensor of shape **`(num_queries, num_keys)`** containing the mean attention pattern across all heads and all queries in the batch. This tensor is then visualized using the **`imshow`** function.
        
    
    video @ 55m says the answer. Before, it was `[batch_index, 0]`. Becomes `.mean[0,1]`
    
    - `fold_W_U = model.ln_final.w[:, None] * model.unembed.W_U` [?]
        
        The code snippet `fold_W_U = model.ln_final.w[:, None] * model.unembed.W_U` calculates the folded weights of the `W_U` parameter in a transformer model.
        
        The `W_U` parameter is typically used in the decoder part of the transformer to project the decoder hidden states to the vocabulary size. In the original transformer architecture, the `W_U` parameter is a matrix with shape `(hidden_size, vocab_size)`.
        
        The folding operation involves combining the `W_U` matrix with the output of the final LayerNorm layer in the transformer decoder. This is done to reduce the number of computations required during inference.
        
        In the code snippet, `model.ln_final.w` is a learnable weight vector with shape `(hidden_size,)` that is part of the final LayerNorm layer in the decoder. `model.unembed.W_U` is the original `W_U` parameter in the decoder.
        
        To calculate the folded weights, `model.ln_final.w[:, None]` broadcasts the weight vector to have shape `(hidden_size, 1)`, and then multiplies it element-wise with `model.unembed.W_U`. The resulting tensor `fold_W_U` has shape `(hidden_size, vocab_size)`, which is the same as the original `W_U` parameter.
        
        By using the folded weights during inference, the decoder hidden states can be directly projected to the vocabulary size without the need for an explicit matrix multiplication with the `W_U` parameter. This can significantly reduce the number of computations required during inference.
        
    
    **1:03:57** Logits are translation and variant meaning when you add one to every logit it doesn't change the log prob so often when you're trying to interpret logits it's pretty helpful to subtract off the mean because this is a pretty crude way of just getting rid of effects that look like adding one to everything (???)
    
    - `QK = model.W_E @ model.W_Q[0, 0] @ model.W_K[0, 0].T @ model.W_E.T`
        
        The `model.W_E` parameter is the learned embedding matrix that maps input tokens to the hidden representation used by the transformer model. The `model.W_Q` and `model.W_K` parameters are learned matrices that project the embedded input sequence onto the query and key spaces, respectively.
        
        The `@` operator performs matrix multiplication, so `model.W_Q[0, 0]` and `model.W_K[0, 0].T` are the query and key matrices for the first head of the multi-head attention mechanism.
        
        The `T` method is used to transpose the key matrix so that it has shape `(hidden_size, seq_length)`.
        
        Finally, the dot product of `model.W_Q[0, 0]` and `model.W_K[0, 0].T` computes the pairwise similarity between the queries and keys for the first head of the multi-head attention mechanism.
        
        The resulting tensor `QK` has shape `(seq_length, seq_length)` and represents the attention scores between each position in the input sequence. Each element in `QK` corresponds to the attention score between the query at that position and the key at another position.
        
    
    **1h22m: OV circuit diagram** shows most neurons don’t matter, only a few do
    
    MLP0 : interesting because some neurons are “dropping off”? Unexpected
    

[“An” neuron](https://www.notion.so/An-neuron-92888cb0c37548b7949c1d9c3c9d260d?pvs=21) 

EasyTransformer [MLAB].ipynb (outdated but helpful to learn hook internals):

[https://colab.research.google.com/drive/1_tH4PfRSPYuKGnJbhC1NqFesOYuXrir_#scrollTo=gOFcfk-6wZdU](https://colab.research.google.com/drive/1_tH4PfRSPYuKGnJbhC1NqFesOYuXrir_#scrollTo=gOFcfk-6wZdU)

[https://www.lesswrong.com/posts/LkBmAGJgZX2tbwGKg/help-out-redwood-research-s-interpretability-team-by-finding](https://www.lesswrong.com/posts/LkBmAGJgZX2tbwGKg/help-out-redwood-research-s-interpretability-team-by-finding)