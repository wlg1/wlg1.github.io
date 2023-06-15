# Transformers

Autoregressive means ‘causal’. It refers to a type of mathematical model where a variable is modeled as a function of its own past values. In other words, it predicts future values based on previous values of the same variable.

[Tokenizers](Transformers%2003e1e4e7e9654bd199395f7c72a88571/Tokenizers%20f9909472886e40ccbabcf1f4d8349f41.md)

[Embeddings](Transformers%2003e1e4e7e9654bd199395f7c72a88571/Embeddings%20c4e515f0f63844d8bdd5309d041e40cf.md)

[Query, Key, Value Matrices](Transformers%2003e1e4e7e9654bd199395f7c72a88571/Query,%20Key,%20Value%20Matrices%20fe92464f6ee24068b6aaa56bb85e903e.md)

[Self-attention](Transformers%2003e1e4e7e9654bd199395f7c72a88571/Self-attention%2064a3e43e6ac8491f8a7ddc54a071b903.md) 

[Attention Mask](Transformers%2003e1e4e7e9654bd199395f7c72a88571/Attention%20Mask%205fe51dc6d90f4f7eb34bc6061060d44f.md)

[Residual Stream](Transformers%2003e1e4e7e9654bd199395f7c72a88571/Residual%20Stream%201ce90f23f8f44b2b80b150c2f4b99226.md) 

[Matrix Composition](Transformers%2003e1e4e7e9654bd199395f7c72a88571/Matrix%20Composition%2055d6261a57dd414191f758b93a459ecc.md)

[Positional Encoding](Transformers%2003e1e4e7e9654bd199395f7c72a88571/Positional%20Encoding%2027e592dc216e43cdb52abea533181cb6.md)

[Skip connections](Transformers%2003e1e4e7e9654bd199395f7c72a88571/Skip%20connections%20864e4b2e107c45eebf775fb463ca7e50.md)

- Give the dimensions of each matrix multiplication step of a transformer, including the details of query key and value matrices. Provide the matrix multiplcation dimension calculations to get these output dimensions
    
    Sure, here are the dimensions of each matrix multiplication step in the transformer architecture, assuming a batch size of `B`, sequence length of `S`, and embedding dimension of `E`:
    
    1. **Input Embeddings**: The input sequence of tokens is first transformed into embeddings, which are vectors of size `E`. If the input sequence has `S` tokens, the input embeddings matrix has dimensions `B x S x E`.
    2. **Query, Key, and Value Matrices**: The input embeddings are used to compute the query, key, and value matrices. Each of these matrices has dimensions `B x S x E`.
    3. **Query-Key Dot Product**: The dot product between the query and key matrices is computed to obtain an attention matrix. The dimensions of the query and key matrices are `B x S x E`, so the dot product has dimensions `B x S x S`.
    4. **Scaled Dot-Product Attention**: The attention matrix is divided by the square root of the embedding dimension, and a softmax function is applied to obtain a probability distribution over the values. Finally, the value matrix is multiplied by this distribution to obtain the output of the attention layer. The dimensions of the value matrix are `B x S x E`, so the output of the attention layer has dimensions `B x S x E`.
    5. **Multi-Head Attention**: The attention mechanism is applied multiple times in parallel with different query, key, and value matrices. The outputs are concatenated and multiplied by a weight matrix to obtain a final output. If the transformer has `H` heads, the output of each head has dimensions `B x S x (E/H)`, and the weight matrix has dimensions `(E/H) x E`. The final output of the multi-head attention layer has dimensions `B x S x E`.
    6. **Feedforward Network**: The output of the multi-head attention layer is passed through a two-layer feedforward network with a ReLU activation function. The first layer has dimensions `E x F`, where `F` is the size of the hidden layer. The second layer has dimensions `F x E`. The output of the feedforward network has dimensions `B x S x E`.
    
    Here are the calculations to derive these dimensions:
    
    1. Input Embeddings:
    - Input embeddings matrix dimensions: `B x S x E`
    1. Query, Key, and Value Matrices:
    - Query matrix dimensions: `B x S x E`
    - Key matrix dimensions: `B x S x E`
    - Value matrix dimensions: `B x S x E`
    1. Query-Key Dot Product:
    - Query matrix dimensions: `B x S x E`
    - Key matrix dimensions: `B x S x E`
    - Dot product dimensions: `B x S x S`
    1. Scaled Dot-Product Attention:
    - Attention matrix dimensions: `B x S x S`
    - Value matrix dimensions: `B x S x E`
    - Output dimensions: `B x S x E`
    1. Multi-Head Attention:
    - Number of heads: `H`
    - Query, key, and value matrix dimensions: `B x S x (E/H)`
    - Output of each head dimensions: `B x S x (E/H)`
    - Weight matrix dimensions: `(E/H) x E`
    - Concatenated output dimensions: `B x S x E`
    1. Feedforward Network:
    - Input dimensions: `B x S x E`
    - First layer weight matrix dimensions: `E x F`
    - Second layer weight matrix dimensions: `F x E`
    - Output dimensions: `B x S x E`
- Give the dimensions of each matrix multiplication step of a transformer, including the details of query key and value matrices. Provide the matrix multiplcation dimension calculations to get these output dimensions. For example, show that a matrix C has dimension (P x Q) because matrix A has dim (P x K), matrix B has dim (Q x K), and A * B^T = C
    
    Sure, let me break down the dimensions of each matrix multiplication step in the transformer architecture.
    
    First, let's define the inputs to the multi-head attention mechanism, which are:
    
    - Queries (Q): a matrix of shape (seq_len, d_model)
    - Keys (K): a matrix of shape (seq_len, d_model)
    - Values (V): a matrix of shape (seq_len, d_model)
    
    Here, seq_len refers to the sequence length and d_model refers to the embedding dimension of each token in the input sequence.
    
    Next, let's define the weight matrices used in the multi-head attention mechanism:
    
    - Query weights (W_Q): a matrix of shape (d_model, d_k)
    - Key weights (W_K): a matrix of shape (d_model, d_k)
    - Value weights (W_V): a matrix of shape (d_model, d_v)
    
    Here, d_k and d_v refer to the dimensions of the query and value projections, respectively. These are typically smaller than d_model and are used to reduce the dimensionality of the queries and values.
    
    The multi-head attention mechanism involves several matrix multiplications, which can be broken down as follows:
    
    1. Project the queries, keys, and values into multiple subspaces using the query, key, and value weight matrices:
        - Q_1 = Q * W_Q1
        - K_1 = K * W_K1
        - V_1 = V * W_V1
        
        ...
        
        - Q_h = Q * W_Qh
        - K_h = K * W_Kh
        - V_h = V * W_Vh
        
        Here, h is the number of attention heads, and the weight matrices for each head have shape (d_model, d_k) for W_Q and W_K, and (d_model, d_v) for W_V.
        
    2. Compute the scaled dot-product attention between the query and key matrices for each attention head:
        - Attention_1 = softmax(Q_1 * K_1^T / sqrt(d_k)) * V_1
        - ...
        - Attention_h = softmax(Q_h * K_h^T / sqrt(d_k)) * V_h
        
        Here, softmax is applied along the rows of the matrix to get a weight distribution over the values for each query token. The scaling factor of sqrt(d_k) is used to stabilize the gradients during training.
        
    3. Concatenate the outputs of each attention head:
        - Concatenated_attention = [Attention_1, ..., Attention_h]
        
        The resulting matrix has shape (seq_len, h*d_v).
        
    4. Project the concatenated attention matrix back to the original dimensionality of the input using a final linear layer:
        - Output = Concatenated_attention * W_O
        
        Here, the weight matrix W_O has shape (h*d_v, d_model).
        
    
    So the output dimension of the transformer multi-head attention mechanism is (seq_len, d_model).
    
    To summarize:
    
    - Input matrices Q, K, and V have dimensions (seq_len, d_model)
    - Weight matrices W_Q, W_K, and W_V have dimensions (d_model, d_k), (d_model, d_k), and (d_model, d_v), respectively
    - Output dimension of each head is (seq_len, d_v)
    - Concatenated_attention matrix has dimension (seq_len, h*d_v)
    - Final output matrix has dimension (seq_len, d_model)
    
    I hope this helps! Let me know if you have any further questions.
    
    - gpt-4 response
        
        To provide a comprehensive answer, I'll first define the dimensions of the input and various matrices in a transformer, and then I'll show the matrix multiplication steps with their dimensions.
        
        Let's assume we have the following dimensions for a single transformer layer:
        
        - Input sequence length: L
        - Embedding size (input dimensionality): D
        - Number of attention heads: H
        - Key, Query, and Value dimensions per head: dk, dq, and dv (usually, dk = dq)
        - Feed-forward hidden layer size: FF
        
        Now let's go through each step:
        
        1. Input: The input is a sequence of tokens with an embedding size D. So, the input matrix X has dimensions (L x D).
        2. Linear Projections: The input matrix X is linearly projected to create Query (Q), Key (K), and Value (V) matrices.
            - Q has dimensions (L x (dq * H))
            - K has dimensions (L x (dk * H))
            - V has dimensions (L x (dv * H))
        3. Splitting Heads: The matrices Q, K, and V are split into H heads, resulting in the following dimensions:
            - Qi for i-th head has dimensions (L x dq)
            - Ki for i-th head has dimensions (L x dk)
            - Vi for i-th head has dimensions (L x dv)
        4. Scaled Dot-Product Attention:
            - First, we calculate the dot product between Qi and Ki^T, resulting in a matrix Si with dimensions (L x L). The formula is: Si = Qi * Ki^T
            - Then, we apply softmax on Si and multiply it by Vi. The output matrix Oi for each head has dimensions (L x dv).
        5. Concatenation: We concatenate all Oi matrices along the second dimension, resulting in a matrix O with dimensions (L x (dv * H)).
        6. Linear Projection: The matrix O is then linearly projected back to a matrix with dimensions (L x D).
        7. Add & Norm: The output matrix from step 6 is then added to the input matrix (residual connection), and layer normalization is applied, resulting in a matrix with dimensions (L x D).
        8. Position-wise Feed-Forward Network (FFN): The matrix from step 7 is passed through a two-layer feed-forward network. Each layer consists of a linear transformation followed by an activation function (e.g., ReLU). The dimensions in this step remain unchanged: (L x D).
        9. Add & Norm: The output matrix from the FFN is added to the matrix from step 7 (residual connection) and layer normalization is applied, resulting in the final output matrix with dimensions (L x D).
        
        These steps are repeated for each transformer layer in the model.
        

---

- If transformers only output one word at a time, how can it choose a word based on future words further in the sequence? For example, it can output yes as its first word, yet doesn't this depend on knowing all other words in its answer?
    
    
    In a transformer network, the output at each position depends on the input tokens and the output tokens generated up to that point, but not on future tokens beyond that position. Therefore, the transformer network is not able to directly "see" future tokens when generating the output sequence.
    However, the transformer network is designed to capture long-range dependencies between the input and output sequences through the self-attention mechanism. During the self-attention computation, each input token is compared to all other tokens in the sequence, allowing the network to dynamically focus on different parts of the input sequence and capture complex patterns and relationships between the tokens.
    Similarly, during the decoding phase (i.e., when generating the output sequence), the network uses the previously generated output tokens as input to generate the next token in the sequence. While the network does not have access to future tokens at each decoding step, it can use the attention weights learned during training to capture dependencies between the output tokens and the input sequence.
    Therefore, while the transformer network is not able to directly see future tokens when generating the output sequence, it can capture complex patterns and relationships between the input and output sequences through the self-attention mechanism and the use of previously generated output tokens as input. This allows the network to generate coherent and meaningful output sequences based on the input sequence and the context provided by the previously generated output tokens.
    

---

[GPT mechanisms](Transformers%2003e1e4e7e9654bd199395f7c72a88571/GPT%20mechanisms%20108c635e0f0849ac8e556c91c892dec2.md) 

[Relation to Graph NNs](Transformers%2003e1e4e7e9654bd199395f7c72a88571/Relation%20to%20Graph%20NNs%20149398714b1e4f6f9affe076359a067c.md)