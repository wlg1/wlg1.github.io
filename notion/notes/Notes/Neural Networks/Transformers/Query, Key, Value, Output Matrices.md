# Query, Key, Value, Output Matrices

[https://www.youtube.com/watch?v=ekg-hoob0SM&list=PLTl9hO2Oobd97qfWC40gOSU8C0iu0m2l4&index=7&ab_channel=CodeEmporium](https://www.youtube.com/watch?v=ekg-hoob0SM&list=PLTl9hO2Oobd97qfWC40gOSU8C0iu0m2l4&index=7&ab_channel=CodeEmporium)

Query: What am I looking for? (search terms)

Key: What does it have to offer? (result titles/metadata) —> (QK is search results page)

Value: What is actually being offered (content in each result’s link)

---

The QK matrix IS the attention pattern 
The OV matrix determines what is written into the residual stream.

[https://towardsdatascience.com/illustrated-self-attention-2d627e33b20a](https://towardsdatascience.com/illustrated-self-attention-2d627e33b20a)

![Untitled](Query,%20Key,%20Value,%20Output%20Matrices%20fe92464f6ee24068b6aaa56bb85e903e/Untitled.png)

There are 4 basis vectors to represent a token 

There are 3 tokens (inputs)

Each row of the Q weight matrix is on a basis vector

Each column of the Q weight matrix is for a token 

How each weight is learned depends on how each token is encoded as a vector

---

[https://jalammar.github.io/illustrated-transformer/](https://jalammar.github.io/illustrated-transformer/)

There is a separate key VECTOR (not matrix) for each word in the input sentence (paragraph, book, etc). These vectors are separate columns of the key matrix.

When we do Input * Key Matrix, we are doing 

input (row) * key column

to calculate each element of the output vector. This output vector is a row in the output matrix.

[https://www.youtube.com/watch?v=4Bdc55j80l8&ab_channel=TheA.I.Hacker-MichaelPhi](https://www.youtube.com/watch?v=4Bdc55j80l8&ab_channel=TheA.I.Hacker-MichaelPhi)

![Untitled](Query,%20Key,%20Value,%20Output%20Matrices%20fe92464f6ee24068b6aaa56bb85e903e/Untitled%201.png)

---

![Untitled](Query,%20Key,%20Value,%20Output%20Matrices%20fe92464f6ee24068b6aaa56bb85e903e/Untitled%202.png)

On a graph, red arrow between hidden states on different token rows corresponds to the final output of that token’s row ??? still doesn’t make sense

![Untitled](Query,%20Key,%20Value,%20Output%20Matrices%20fe92464f6ee24068b6aaa56bb85e903e/Untitled%203.png)

---

Cross attention: query is seq 1, k-v is seq 2

The lines mean multiplied with, the arrows means ‘results in’

![Untitled](Query,%20Key,%20Value,%20Output%20Matrices%20fe92464f6ee24068b6aaa56bb85e903e/Untitled%204.png)

[REF](Self-attention%20(QK)%2064a3e43e6ac8491f8a7ddc54a071b903.md)

For GPT (decoder only), this “Cross attention” uses the same sequence, seq_1 = seq_2

The attention scores (attention matrix above) are calculated by the matrix multiplication of the output of the input embeddings * query matrix and (input embeddings * key matrix)^T

seq_len x D_q * D_k x seq_len_2 = seq_len_1 x seq_len_2

This is possible b/c D_q = D_k

x is a slice of the input tensor, (# inputs, num token pos, emb dim) that takes one of the inputs.

- Where do the values of d_q, d_k and d_v come from?
    
    The values of d_q, d_k, and d_v, which represent the dimensions of the query, key, and value matrices in a transformer model, are typically predefined hyperparameters that are set prior to training the model.
    
    These hyperparameters determine the size or dimensionality of the learned representations for the query, key, and value in the self-attention mechanism. They can be chosen based on the requirements of the specific task and the design choices of the model.
    
    In practice, d_q, d_k, and d_v are often set to the same value to maintain consistency and enable compatibility between the matrices during the attention calculations. However, it is not a strict requirement, and these dimensions can be different if desired.
    
    The values of d_q, d_k, and d_v are hyperparameters that need to be determined during the design of the transformer model architecture. They are typically chosen based on empirical experimentation, best practices, and considerations such as the complexity of the task, computational resources, and the available training data.
    

---

- attn.W_O
    
    [https://jalammar.github.io/illustrated-transformer/](https://jalammar.github.io/illustrated-transformer/)
    
    ![Untitled](Query,%20Key,%20Value,%20Output%20Matrices%20fe92464f6ee24068b6aaa56bb85e903e/Untitled%205.png)
    
    This converts away the **`weights_dim` to make z= [`seq_length, embedding_size]`, the original dims of the input to the attention head**
    

W_O doesn’t come from a head; it’s after concat all heads. But the specific attn.W_O is concat with the other attn.W_O into W_O. In the figure above, we see z are concat by col (64 + 64 +…) while W_O are concat by row. So the concat z’s col and W_O’s row have the same dim, allowing matrix multiplication.

[https://www.youtube.com/watch?v=4Bdc55j80l8&ab_channel=TheA.I.Hacker-MichaelPhi](https://www.youtube.com/watch?v=4Bdc55j80l8&ab_channel=TheA.I.Hacker-MichaelPhi)

W_O is the linear layer at 7m35s