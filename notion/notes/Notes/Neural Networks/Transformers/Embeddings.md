# Embeddings

These weights act like a lookup table from 1-hot encoding to embeddings

- For transformers, are the embedded vectors in a semantically similar space? Can you add them to make analogies like "king - woman = queen"?
    
    Yes, in the case of transformer-based models like GPT-3, the embedded vectors are typically designed to encode semantic information in a dense vector space. This means that similar words or concepts tend to have similar vector representations, and relationships between words can often be captured in vector arithmetic.
    
- Why can't you just take dot product of embedded vectors to compare them? Why do you need to put them through query and key matrices then dot product the query and key vectors to get attention?
    
    The attention mechanism allows the model to focus on relevant parts of the input sequence when generating the output. While it is true that you can calculate the dot product between embedded vectors directly, the attention mechanism provides several benefits:
    
    1. **Scalability**: The attention mechanism allows for parallel computation of attention weights across all positions in the input sequence. This enables efficient processing of long sequences without significantly increasing computational complexity.
    2. **Flexibility**: By using query and key matrices, the model can learn different weights for different parts of the embedded vectors, capturing more nuanced relationships between words. The query and key vectors are learned parameters that can be updated during training to optimize the model's performance.
    3. **Information flow**: The attention mechanism facilitates information flow between different positions in the input sequence. The dot product between the query and key vectors determines the relevance or similarity between positions, and the resulting attention weights influence the contribution of each position to the final output. This enables the model to attend to different parts of the input based on their importance or relevance.
    

---

[https://www.alignmentforum.org/posts/pHPmMGEMYefk9jLeh/llm-basics-embedding-spaces-transformer-token-vectors-are](https://www.alignmentforum.org/posts/pHPmMGEMYefk9jLeh/llm-basics-embedding-spaces-transformer-token-vectors-are)

---

- A transformer model's input embedding is what dimension? When it's matrix multiplied with the query matrix, what are the dimensions of each matrix and the output matrix?
    
    In a transformer model, the input embedding dimension is typically denoted as "d_model" or "hidden_size." This dimension represents the size or number of features used to represent each token in the input sequence.
    
    When the input embedding is matrix multiplied with the query matrix, the dimensions are as follows:
    
    1. Input Embedding Matrix: (seq_length, d_model) or (batch_size, seq_length, d_model)
        - The input embedding matrix has a shape of (seq_length, d_model) if you're processing a single sequence or (batch_size, seq_length, d_model) if you're processing a batch of sequences. The "seq_length" represents the length of the input sequence, and "d_model" represents the input embedding dimension.
    2. Query Matrix: (d_model, d_k)
        - The query matrix has a shape of (d_model, d_k), where "d_k" represents the dimension of the query.
    3. Output Matrix: (seq_length, d_k) or (batch_size, seq_length, d_k)
        - The output matrix will have a shape of (seq_length, d_k) if you're processing a single sequence or (batch_size, seq_length, d_k) if you're processing a batch of sequences. The "seq_length" represents the length of the input sequence, and "d_k" represents the dimension of the query.
    
    During the matrix multiplication, the input embedding matrix is typically on the left side, and the query matrix is on the right side. The resulting output matrix is obtained by multiplying the input embedding matrix with the query matrix, resulting in a matrix of shape (seq_length, d_k) or (batch_size, seq_length, d_k), depending on the context.