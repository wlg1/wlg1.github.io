# Clustering by layer

- How do these clusters change as they’re processed through each layer of the circuit?
    - Slice network then take output of tokens, and compare them
    - nbs: copy scores, dotprod, extract models

when does an object become recognized as a subject?
table, Lamp
sat on table
table gave it to

at each layer- why would the model make them closer or farther along a dimension? perhaps along the associated sequential dimension, whatever that is. that should be a combination of head/mlp neurons.

does lamp get closer to becoming a 'subject' as it's associated with an in-context subject? project by pca/svd on 'most impt dirs' (which may be the subj dir) and cluster the subjs/objs. see if the objs become more like the subjs as you 'confuse' the model using in-context. originally, they're not similar, but in-context makes them cluster closer together along this impt svd dir (which may be the heads measuring subjs in the in-context pattern)?

---

REQS:

1. Pass the (obj, subj) in-context inputs through the model
2. Understand this code: extract_L9.ipynb
    
    [https://colab.research.google.com/drive/1cyW5ZlupQH0VJ6qWcFBkGMbOrDeHWMdD](https://colab.research.google.com/drive/1cyW5ZlupQH0VJ6qWcFBkGMbOrDeHWMdD#scrollTo=OWe216EhCif8)
    
3. Understand how tokens, in different input sequences, are represented as embedded vectors at each output (latent) space in a transformer
4. Get shape of output (before unembed into logits) at each layer. How can this tensor shape be compared to another tensor? How can it be plotted in 2D or 3D?
    
    [https://chat.openai.com/c/12155847-197c-47a9-a1b2-4511192c434c](https://chat.openai.com/c/12155847-197c-47a9-a1b2-4511192c434c)
    

SVD

create an animation of this clustering

---

[https://chat.openai.com/c/b5c12746-f184-4f2b-babe-af1df51d96fc](https://chat.openai.com/c/b5c12746-f184-4f2b-babe-af1df51d96fc)

- We know each token goes through the transformer model in parallel. Is the value of each embedded token at each layer affected by previous tokens in the input sequence? For example, “red cat” would have the “cat” embedded vector be a different vector value after layer 3 than the “cat” vector of “blue cat”?
    
    Yes, you're absolutely right. In the transformer architecture, even though each token is processed in parallel through self-attention mechanisms, the representation (or the embedded vector) of each token at a particular layer is influenced by all other tokens in the input sequence due to the self-attention mechanism.
    
    To explain further:
    
    - **Self-Attention Mechanism**: The essence of the transformer model lies in its ability to pay "attention" to different parts of the input sequence when representing a particular token. When processing a token, the self-attention mechanism computes attention scores based on the interaction of this token with all other tokens in the sequence. These scores determine how much each token in the sequence should contribute to the representation of the current token. As a result, the final representation (or embedded vector) of a token at a particular layer is a weighted sum of all token embeddings in the sequence.
    - **Context Sensitivity**: Because of the self-attention mechanism, the representation of a token inherently captures the context in which it appears. For instance, in the case of "red cat" vs. "blue cat", the representation of the word "cat" will likely differ between the two phrases after passing through the transformer layers. This is because "red" and "blue" would provide different context to "cat", influencing the attention scores and subsequently, the representations.
    
    In summary, in the transformer architecture, the value of each embedded token at each layer is indeed affected by all other tokens in the input sequence due to the self-attention mechanism. This context sensitivity is one of the key strengths of the transformer model, allowing it to handle a wide range of language understanding tasks effectively.
    
- For the tokenizer of a transformer, how can we compare the similarity between embedded sequences of tokens if they aren't embedded as vectors, but as matrices?
    
    In the context of transformers, the "embedded sequence of tokens" typically refers to the vectors that result from the token embedding lookup, potentially added to position embeddings. These embeddings usually take the form of a matrix where each row is the embedding vector for a token.
    
    If you're working with an embedding system where sequences are represented as matrices rather than vectors, there are a number of ways to compute similarity or distance between the matrices:
    
    1. **Flatten and Vectorize**: Convert the matrix representations of your sequences into long vectors and use cosine similarity or Euclidean distance. This approach can be sensitive to any reordering of rows (tokens) in the matrices.
    2. **Frobenius Norm**: If you have two matrices \(A\) and \(B\), the difference between them can be represented by the matrix \(C = A - B\). The Frobenius norm of \(C\) (which is the square root of the sum of the absolute squares of its elements) gives a scalar value representing the "difference" between the two matrices.
    3. **Singular Value Decomposition (SVD)**: Using SVD, decompose the matrices into their singular values and vectors. The similarity between two matrices can be compared using the similarity of their singular values.
    4. **Canonical Correlation Analysis (CCA)**: If the matrices represent sequences of embeddings, CCA can be used to measure the similarity of the sequences by finding linear combinations of the embeddings that have maximum correlation.
    5. **Matrix Norms**: Other than the Frobenius norm, there are various matrix norms (like the operator norm) which can be used to compare the difference between two matrices.
    6. **Trace**: Compute the trace of the product of the matrices. If the matrices are normalized such that each has a trace of 1, then the trace of their product will be a similarity measure, with 1 indicating identical matrices and 0 indicating orthogonal matrices.
    7. **Optimal Transport**: Compute a similarity measure by finding the optimal way to "transport" one matrix into another, effectively finding the minimum "cost" of transforming one matrix to the other.
    8. **Recurrence Plots**: Convert each matrix into a recurrence plot and compare the plots. This method is particularly useful for time series data, but it can also be adapted for matrix representations of sequences.
    
    Which method to use depends on the nature of the data, the meaning of the embeddings, and the specifics of the application. Often, a combination of methods or iterative refinement is necessary to achieve satisfactory results.
    
- Write code in pytorch to measure how different "cat" is in "red cat" compared to "blue cat”
    
    
- Write code in pytorch to compare these matrices using svd
    
    To compare two matrices using SVD in PyTorch, you'll first need to perform SVD on each matrix, then compare the resulting singular values and singular vectors. A simple approach is to compute the Frobenius norm of the difference between the singular values and between the singular vectors for the two matrices. Here's how you can do it:
    
    ```python
    import torch
    import torch.nn.functional as F
    
    # Generate some sample matrices
    A = torch.rand([5, 768])
    B = torch.rand([5, 768])
    
    # Perform SVD
    U_A, S_A, V_A = torch.svd(A)
    U_B, S_B, V_B = torch.svd(B)
    
    # Measure the difference in singular values
    singular_value_difference = F.mse_loss(S_A, S_B).sqrt()
    
    # Measure the difference in left singular vectors (U matrices)
    u_difference = F.mse_loss(U_A, U_B).sqrt()
    
    # Measure the difference in right singular vectors (V matrices)
    v_difference = F.mse_loss(V_A, V_B).sqrt()
    
    print("Singular Value Difference:", singular_value_difference.item())
    print("U Matrix Difference:", u_difference.item())
    print("V Matrix Difference:", v_difference.item())
    
    ```
    
    Here, we're using the mean squared error (MSE) followed by the square root (equivalent to the Euclidean norm) to compute the differences. A smaller difference indicates that the matrices are more similar.
    
    Note: Due to the nature of SVD, the signs of singular vectors can be flipped while still being valid. If you find large differences, especially in the U or V matrices, you might want to consider additional steps to account for potential sign differences.
    
- How do you interpret the output as large or small?
    
    Interpreting the output as large or small is subjective and context-dependent. However, there are some general guidelines and considerations:
    
    1. **Absolute Scale**: Consider the scale of the values within the matrices. If the entries of your matrices are generally between 0 and 1, then a difference of 0.1 in singular values might be considered large. If the entries are in the hundreds or thousands, a difference of 0.1 might be negligible.
    2. **Relative Scale**: Compare the difference to the magnitude of the singular values themselves. For instance, if the singular values are on the order of \(10^{-3}\), then a difference of \(10^{-4}\) is significant. But if the singular values are around 10 or 100, a difference of \(10^{-4}\) is small.
    3. **Visualize**: Visualizing the singular values of both matrices can provide insights. Plot the singular values of both matrices on the same plot and see how they compare. Significant divergence in the plots indicates a difference in matrix structures.
    4. **Contextual Interpretation**: Understand the context of your data. For instance, if these matrices represent embeddings of sentences, even a small difference might lead to different meanings, while in other contexts, a small difference might be negligible.
    5. **Set a Threshold**: Depending on the application, you can set a threshold for the difference. Any difference below the threshold can be considered small, and any difference above it can be considered large. The choice of this threshold is application-dependent.
    6. **Comparison to Other Data**: If you have other pairs of matrices for which you know they are similar or different, you can use them as a benchmark. Compute their SVD differences and use them as a reference to interpret the difference of your current pair.
    7. **Matrix Norm**: Consider the norm of the matrices. If your matrices have a Frobenius norm around 1000, then a singular value difference of 5 might be considered small. But if the norm is around 10, a difference of 5 is large.
    
    Ultimately, the interpretation should be based on a combination of empirical observation, domain knowledge, and the specific goals of your analysis.
    
- i compared two matrices to get a singular_value_difference of 4. write code to interpret this as small or big
    
    To interpret the `singular_value_difference` of 4 as small or big, you can consider a few methods. Here's one basic way to approach it:
    
    1. Compute the average magnitude of the singular values for both matrices.
    2. Compute the relative difference based on the average magnitude.
    3. Set a threshold for relative difference to determine if it's small or big.
    
    Here's how you can implement this:
    
    ```python
    import torch
    
    # Generate some sample matrices
    A = torch.rand([5, 768])
    B = torch.rand([5, 768])
    
    # Perform SVD
    U_A, S_A, V_A = torch.svd(A)
    U_B, S_B, V_B = torch.svd(B)
    
    # Compute the difference in singular values
    singular_value_difference = (S_A - S_B).norm().item()
    
    # Compute average magnitude of singular values for both matrices
    avg_magnitude = (S_A.norm() + S_B.norm()).item() / 2
    
    # Compute relative difference
    relative_difference = singular_value_difference / avg_magnitude
    
    # Define a threshold for interpretation. This is a hyperparameter that you can adjust.
    # For example, setting it to 0.1 means that a difference of 10% of the average magnitude
    # is considered the boundary between "small" and "big".
    threshold = 0.1
    
    if relative_difference < threshold:
        print("The difference is small.")
    else:
        print("The difference is big.")
    
    ```
    
    Note that the choice of `threshold` is somewhat arbitrary and should be tuned based on domain knowledge, the specifics of your application, and any empirical observations you've made.
    

[https://chat.openai.com/c/7282dfa3-5866-49ed-b209-7ff272558458](https://chat.openai.com/c/7282dfa3-5866-49ed-b209-7ff272558458)

- In a transformer, after each layer output is a matrix. Given two token inputs, such as "1 2 3 4" and "one two three four", can we track how similar the two inputs after each layer are by measuring their output matrix similarity after each layer?
    
    Yes, you can track the similarity between two inputs as they pass through the layers of a transformer model by measuring the similarity of their output representations at each layer. Here's a general way to approach this:
    
    1. **Tokenization**: Tokenize the input sentences "1 2 3 4" and "one two three four" using the appropriate tokenizer for your transformer model.
    2. **Model Forward Pass**:
        - Pass both tokenized sequences through the transformer model.
        - For models like BERT or its variants, each token will have an associated output vector at each layer. For the sake of simplicity, you can average all token vectors to get a single vector representation for the entire sequence at each layer.
    3. **Similarity Measurement**:
        - For each layer's output representation of the two sequences, compute a similarity score. Cosine similarity is a commonly used measure for this purpose. For vectors \( A \) and \( B \):
        \[ \text{cosine similarity} = \frac{A \cdot B}{\|A\|_2 \|B\|_2} \]
        - Repeat the above step for each layer of the transformer to track how the similarity evolves across layers.
    4. **Interpretation**:
        - A value closer to 1 indicates higher similarity, whereas a value closer to -1 indicates higher dissimilarity. A value close to 0 indicates no particular similarity or dissimilarity.
        - By observing the similarity scores across layers, you can gain insights into how the transformer model processes and understands the two sequences. For instance, earlier layers might focus more on low-level features (like syntax), while later layers may capture more abstract, high-level semantic information.
    5. **Considerations**:
        - Averaging token vectors is a simplification. Depending on the use case, you might want to consider other pooling strategies (like max-pooling or attention-based pooling).
        - Not all transformer models behave the same. For instance, BERT and GPT are both transformer architectures, but they might process and understand sequences differently due to their training objectives and architecture specifics.
    6. **Visual Analysis**:
        - To further understand the dynamics, you can plot the similarity scores across layers. This can give you a visual representation of how similarity evolves through the layers.
    
    Remember, while such an analysis can provide insights into the workings of the transformer model, interpreting these insights requires caution. There's still ongoing research into understanding the inner workings of these models, and not all behaviors are fully understood.
    
- As two input sequences "1 2 3 4" and "one two three four" are measured by their output embeddings in each layer, do we expect their matrix similarities to become more or less similar by each layer?
    
    The transformer architecture, such as BERT, divides its layers into low-level and high-level feature extraction stages. Here's a generalized expectation:
    
    1. **Earlier Layers (Low-Level Features)**:
        - In the initial layers, the transformer model usually focuses on capturing low-level features, such as syntax and basic word-level patterns.
        - Given that "1 2 3 4" and "one two three four" are semantically related but syntactically different, we might expect these sequences to be less similar in the initial layers.
    2. **Middle Layers**:
        - As we move towards the middle layers, the transformer model starts to capture more semantic information.
        - This is where we might start to see an increase in similarity between the two sequences, as the model begins to recognize that the numbers in the two sequences are semantically related.
    3. **Later Layers (High-Level Features)**:
        - In the deeper layers, the transformer model is expected to capture even more abstract and high-level semantic features.
        - The similarity might continue to increase here, as the model recognizes the deeper semantic relationship between the two sequences.
    4. **Final Layers**:
        - In some cases, especially with very deep models, the final few layers might focus on very task-specific features (e.g., for a specific downstream task like classification). If you're using a general-purpose pre-trained model (like BERT), this point may not be as relevant, but if you're using a fine-tuned model on a specific task, the final layers might show idiosyncratic behavior based on that task.
    
    However, it's essential to understand that this is a generalization. The actual behavior can vary based on the specific transformer architecture, the dataset it was trained on, and the depth of the model. The best way to get a clear understanding is to perform the experiment and visualize the results as previously explained.
    
- Instead of measuring embeddings, unembed at each layer and measure KL divergence
    
    If you want to measure the KL divergence between the sequences at each layer, you'd typically first compute a probability distribution over the sequence tokens (or words) for each layer. One method to convert activations into a distribution is to apply a softmax function. Once you have these probability distributions, you can then compute the KL divergence between them.
    
    Keep in mind:
    
    - The Kullback-Leibler (KL) divergence between two distributions \(P\) and \(Q\) is given by:
    \[ D_{KL}(P||Q) = \sum_{i} P(i) \log \left( \frac{P(i)}{Q(i)} \right) \]
    However, KL divergence is not symmetric: \(D_{KL}(P||Q) \neq D_{KL}(Q||P)\).
    - To obtain meaningful KL divergence values, the distributions being compared need to be over the same event space. Therefore, we should focus on comparing the distributions of the tokens, not the averaged embeddings.
    
    Let's write the code to measure the KL divergence for the two sequences at each layer:
    
    ```python
    import torch
    from transformers import BertTokenizer, BertModel
    from torch.nn.functional import softmax
    from scipy.special import kl_div
    
    def compute_layerwise_kl_divergence(model, tokenizer, text1, text2):
        # Tokenize and get output for text1
        inputs1 = tokenizer(text1, return_tensors="pt")
        with torch.no_grad():
            outputs1 = model(**inputs1, output_hidden_states=True)
    
        # Tokenize and get output for text2
        inputs2 = tokenizer(text2, return_tensors="pt")
        with torch.no_grad():
            outputs2 = model(**inputs2, output_hidden_states=True)
    
        # Compute KL divergence for each layer
        kl_divergences = []
        for hidden_state1, hidden_state2 in zip(outputs1.hidden_states, outputs2.hidden_states):
            # Softmax over hidden states to get a distribution
            probs1 = softmax(hidden_state1, dim=-1).squeeze().numpy()
            probs2 = softmax(hidden_state2, dim=-1).squeeze().numpy()
    
            # Compute KL divergence for each token and average them
            kl_values = [kl_div(p, q) for p, q in zip(probs1, probs2)]
            avg_kl_div = sum(kl_values) / len(kl_values)
            kl_divergences.append(avg_kl_div)
    
        return kl_divergences
    
    # Initialize model and tokenizer
    model_name = "bert-base-uncased"
    model = BertModel.from_pretrained(model_name)
    tokenizer = BertTokenizer.from_pretrained(model_name)
    model.eval()
    
    # Example texts
    text1 = "1 2 3 4"
    text2 = "one two three four"
    
    # Get KL divergences for each layer
    kl_values = compute_layerwise_kl_divergence(model, tokenizer, text1, text2)
    for i, kl_div in enumerate(kl_values, 1):
        print(f"Layer {i}: KL Divergence = {kl_div:.4f}")
    
    ```
    
    In this code:
    
    1. We use the softmax function to convert hidden states (embeddings) into probability distributions for both sequences at each layer.
    2. For each layer, we compute the KL divergence between these distributions for each token and then average them.
    3. We print the average KL divergence for each layer.
    
    This approach provides an understanding of how different the probability distributions of the tokens in the two sequences are at each layer.
    
- When we measure the output of each layer, is that the prediction for the next token, or the transformed embedding of the input?
    
    In transformer-based models like BERT, the output of each layer is not a prediction for the next token, but rather the transformed embedding of the input. These transformed embeddings incorporate contextual information based on the entire input sequence and the learned model parameters up to that point in the network.
    
    To clarify:
    
    1. **Transformed Embedding**: The primary purpose of the multi-layered architecture in transformers is to iteratively refine the token embeddings by incorporating context from surrounding tokens. With each successive layer, the model captures wider and more abstract contextual patterns. The output at each layer is a set of embeddings for each token that contains this enriched contextual information.
    2. **Prediction for the Next Token**: In certain models like GPT (Generative Pre-trained Transformer), which is designed for autoregressive language modeling, the final layer's output is passed to a linear layer followed by a softmax to predict the next token in a sequence. In BERT, which is designed for masked language modeling, the model predicts the masked-out token based on the context, but this prediction process is specific to the top layer and is not the primary purpose of the intermediate layers.
    
    So, in the context of the code and explanations provided earlier, we're dealing with the transformed embeddings of the input tokens at each layer, not predictions for the next token.
    
- When I measure the similarity of output embeddings at each layer, I don't find they get more similar at each layer. Why is that?
    
    The behavior you're observing—where the embeddings of two different input sequences do not necessarily get more similar through the layers of a transformer model—is related to the way transformers work and the nature of the tasks they're trained on. Here are a few reasons for this:
    
    1. **Learning Hierarchical Features**: Transformers, like other deep neural networks, tend to learn hierarchical features. Initial layers usually capture low-level features such as syntax, while deeper layers capture more abstract, semantic, or higher-level features. Two sequences like "1 2 3 4" and "one two three four" might share certain low-level syntactic features, but as the embeddings progress through layers and get more abstract, their embeddings might not necessarily get more similar.
    2. **Nature of Pretraining**: If you're using a model like BERT, it's pretrained on a masked language modeling task where it tries to predict a masked-out word in a sentence. For BERT to predict a word accurately, it has to learn to distinguish between different word contexts effectively. This differentiation capability might mean that embeddings for different words could become distinct and not converge to a similar representation, even if the words share some semantic relationship.
    3. **High Dimensionality**: The embeddings space in transformer models is high-dimensional (e.g., 768 dimensions for `bert-base-uncased`). Small changes in the input or context can lead to embeddings that seem different in such a high-dimensional space, even if they capture similar contextual information.
    4. **Model Complexity**: Transformers have a massive number of parameters, and their complex interactions can result in non-intuitive behavior in the embeddings. As the model refines the embeddings through each layer, the changes aren't always in the direction of convergence for two different sequences.
    5. **Different Sequence Lengths**: When comparing embeddings of two sequences, if they are of different lengths, this can also introduce variability in similarity scores.
    6. **Overfitting**: If the model has been fine-tuned on a specific task with a small dataset, there's a possibility it might overfit to that data, making its embeddings more specialized and possibly less semantically meaningful when taken out of that specific context.
    
    If you're trying to understand the model's behavior or find optimal representations for a specific task, you might consider:
    
    - Visualizing the embeddings using dimensionality reduction techniques like t-SNE or PCA.
    - Fine-tuning the model on a task that explicitly requires understanding the similarity or relationship between sequences.
    - Using models specifically designed for sentence or sequence similarity, like sentence transformers or Siamese networks.
- write code to use pca to visualize output embeddings at each layer
    
    Sure! Visualizing high-dimensional embeddings using PCA (Principal Component Analysis) is a common practice. Let's write code to extract the embeddings of your two sequences at each layer, project them into a 2D space using PCA, and then visualize them.
    
    Here's how you can do this using the `transformers` library for the embeddings and the `scikit-learn` library for PCA:
    
    ```python
    import torch
    import numpy as np
    import matplotlib.pyplot as plt
    from transformers import BertTokenizer, BertModel
    from sklearn.decomposition import PCA
    
    # Initialize model and tokenizer
    model_name = "bert-base-uncased"
    model = BertModel.from_pretrained(model_name)
    tokenizer = BertTokenizer.from_pretrained(model_name)
    model.eval()
    
    # Tokenize and get embeddings for two sequences
    def get_embeddings(model, tokenizer, text):
        inputs = tokenizer(text, return_tensors="pt")
        with torch.no_grad():
            outputs = model(**inputs, output_hidden_states=True)
        return outputs.hidden_states
    
    text1_embeddings = get_embeddings(model, tokenizer, "1 2 3 4")
    text2_embeddings = get_embeddings(model, tokenizer, "one two three four")
    
    # Visualize using PCA
    for layer_idx, (embeddings1, embeddings2) in enumerate(zip(text1_embeddings, text2_embeddings)):
        # Get embeddings for the two sequences and concatenate
        embeddings1 = embeddings1.squeeze().numpy()
        embeddings2 = embeddings2.squeeze().numpy()
        combined_embeddings = np.vstack([embeddings1, embeddings2])
    
        # Perform PCA and reduce dimensions to 2
        pca = PCA(n_components=2)
        pca_result = pca.fit_transform(combined_embeddings)
    
        # Split PCA results for two sequences
        pca_text1 = pca_result[:len(embeddings1)]
        pca_text2 = pca_result[len(embeddings1):]
    
        # Plot
        plt.figure(figsize=(8, 6))
        plt.scatter(pca_text1[:, 0], pca_text1[:, 1], label="1 2 3 4", color='red', marker='o')
        plt.scatter(pca_text2[:, 0], pca_text2[:, 1], label="one two three four", color='blue', marker='x')
        plt.title(f"Layer {layer_idx + 1}")
        plt.legend()
        plt.show()
    
    ```
    
    This code will display plots for each layer where the embeddings for the sequence "1 2 3 4" are represented with red circles and the embeddings for the sequence "one two three four" are represented with blue crosses. The two-dimensional space is derived from PCA on the embeddings.
    
    The visual representation will give you an understanding of how the embeddings of the two sequences evolve and relate to each other across layers.
    
- Why are there 6 red dots in each plot?
    
    The discrepancy arises because of the added special tokens by BERT's tokenizer. BERT, in particular, uses two additional tokens: `[CLS]` at the beginning and `[SEP]` at the end of each sequence.
    
    So, when you tokenize the sequence "1 2 3 4" with BERT's tokenizer, it becomes:
    
    ```
    [CLS] 1 2 3 4 [SEP]
    
    ```
    
    This sequence has 6 tokens in total.
    
    Similarly, when you tokenize the sequence "one two three four", it will have its own set of `[CLS]` and `[SEP]` tokens.
    
    That's why you see 6 dots for each sequence when you visualize the embeddings. If you'd prefer not to include the embeddings of the special tokens in the visualization, you can exclude the first and last embeddings for each sequence.
    
- Can you rewrite the code to label each data point in the plots?
    
    Certainly! Here's the code to visualize the embeddings at each layer using PCA and label each data point in the plots:
    
    ```python
    import torch
    import numpy as np
    import matplotlib.pyplot as plt
    from transformers import BertTokenizer, BertModel
    from sklearn.decomposition import PCA
    
    # Initialize model and tokenizer
    model_name = "bert-base-uncased"
    model = BertModel.from_pretrained(model_name)
    tokenizer = BertTokenizer.from_pretrained(model_name)
    model.eval()
    
    # Tokenize and get embeddings for two sequences
    def get_embeddings(model, tokenizer, text):
        inputs = tokenizer(text, return_tensors="pt")
        with torch.no_grad():
            outputs = model(**inputs, output_hidden_states=True)
        return outputs.hidden_states
    
    text1 = "1 2 3 4"
    text2 = "one two three four"
    
    text1_embeddings = get_embeddings(model, tokenizer, text1)
    text2_embeddings = get_embeddings(model, tokenizer, text2)
    text1_tokens = tokenizer.tokenize(text1)
    text2_tokens = tokenizer.tokenize(text2)
    
    # Add [CLS] and [SEP] to token lists
    text1_tokens = ['[CLS]'] + text1_tokens + ['[SEP]']
    text2_tokens = ['[CLS]'] + text2_tokens + ['[SEP]']
    
    # Visualize using PCA
    for layer_idx, (embeddings1, embeddings2) in enumerate(zip(text1_embeddings, text2_embeddings)):
        # Get embeddings for the two sequences and concatenate
        embeddings1 = embeddings1.squeeze().numpy()
        embeddings2 = embeddings2.squeeze().numpy()
        combined_embeddings = np.vstack([embeddings1, embeddings2])
    
        # Perform PCA and reduce dimensions to 2
        pca = PCA(n_components=2)
        pca_result = pca.fit_transform(combined_embeddings)
    
        # Split PCA results for two sequences
        pca_text1 = pca_result[:len(embeddings1)]
        pca_text2 = pca_result[len(embeddings1):]
    
        # Plot
        plt.figure(figsize=(10, 8))
    
        for i, (x, y) in enumerate(pca_text1):
            plt.scatter(x, y, color='red')
            plt.text(x+0.02, y+0.02, text1_tokens[i], fontsize=9, color='red')
    
        for i, (x, y) in enumerate(pca_text2):
            plt.scatter(x, y, color='blue')
            plt.text(x+0.02, y+0.02, text2_tokens[i], fontsize=9, color='blue')
    
        plt.title(f"Layer {layer_idx + 1}")
        plt.show()
    
    ```
    
    In this code, I've added annotations to the plot to label each point using `plt.text()`. Each red point corresponds to a token from the sequence "1 2 3 4", and each blue point corresponds to a token from the sequence "one two three four". The tokens are labeled next to their respective points in the plots.
    
- What does it mean for one and 1 to become more similar in each layer?
    
    If the embeddings of "one" and "1" become more similar as you move up through the layers of a transformer model, it offers insights into both the nature of the transformer architecture and the semantics of the words "one" and "1". Let's unpack this:
    
    1. **Hierarchical Representation Learning**: As mentioned previously, transformer-based models like BERT tend to learn hierarchical features. The earlier layers generally focus on low-level features, such as syntax and local context. As you move up through the layers, the representations incorporate more global and semantic context. Thus, if "one" and "1" become more similar in higher layers, it suggests that the model is capturing their semantic equivalence, despite their syntactic differences.
    2. **Abstraction**: The higher layers of deep neural networks, including transformers, tend to capture more abstract features of the input. In the context of language, this could be seen as the model recognizing "one" and "1" as abstract representations of the same quantity, regardless of them being a word and a numeral respectively.
    3. **Training Data & Objectives**: Models like BERT are trained on massive amounts of text data. Given their training objective (e.g., masked language modeling), they have seen "one" and "1" being used in various contexts where they are interchangeable or hold similar meanings. The training enables them to generalize and infer the similarity in diverse situations.
    4. **Interchangeable Usage in Language**: In real-world text, "one" and "1" are often used interchangeably, depending on context or style. For example, in formal writing, numbers might be written out as words, whereas in technical contexts, numerals might be preferred. The model, having been trained on such diverse data, learns this interchangeability.
    5. **Comparison with Other Tokens**: If "one" and "1" become more similar in higher layers, it might also be valuable to see if other semantically related tokens exhibit similar behavior. For example, do "two" and "2" or "three" and "3" also converge in the embedding space? Such patterns could help validate the hypothesis that the model is learning semantic similarities.
    6. **Model's Generalization Ability**: The increasing similarity showcases the model's ability to generalize beyond surface-level patterns. Instead of treating "one" and "1" as completely distinct entities based purely on their orthographic differences, the model generalizes from its vast training data to recognize the shared underlying concept.
    
    If "one" and "1" become more similar in higher layers, it demonstrates the power of transformers in capturing semantic relationships and abstracting away from mere token-level representations to more meaningful, context-aware embeddings.
    
- instead of individual plots, write code to display this as an animation
    
    Animating the sequence of plots can provide a smooth visual transition through the layers. To do this, we can use `matplotlib.animation` in combination with IPython's `display` capabilities.
    
    Here's how you can modify the previous code to animate the PCA visualization across layers:
    
    ```python
    import torch
    import numpy as np
    import matplotlib.pyplot as plt
    from transformers import BertTokenizer, BertModel
    from sklearn.decomposition import PCA
    from matplotlib.animation import FuncAnimation
    from IPython.display import HTML
    
    # Initialize model and tokenizer
    model_name = "bert-base-uncased"
    model = BertModel.from_pretrained(model_name)
    tokenizer = BertTokenizer.from_pretrained(model_name)
    model.eval()
    
    # Tokenize and get embeddings for two sequences
    def get_embeddings(model, tokenizer, text):
        inputs = tokenizer(text, return_tensors="pt")
        with torch.no_grad():
            outputs = model(**inputs, output_hidden_states=True)
        return outputs.hidden_states
    
    text1 = "1 2 3 4"
    text2 = "one two three four"
    
    text1_embeddings = get_embeddings(model, tokenizer, text1)
    text2_embeddings = get_embeddings(model, tokenizer, text2)
    text1_tokens = tokenizer.tokenize(text1)
    text2_tokens = tokenizer.tokenize(text2)
    
    # Add [CLS] and [SEP] to token lists
    text1_tokens = ['[CLS]'] + text1_tokens + ['[SEP]']
    text2_tokens = ['[CLS]'] + text2_tokens + ['[SEP]']
    
    fig, ax = plt.subplots(figsize=(10, 8))
    line1, = ax.plot([], [], 'ro', label="1 2 3 4")
    line2, = ax.plot([], [], 'bo', label="one two three four")
    ax.set_xlim(-50, 50)
    ax.set_ylim(-50, 50)
    
    def init():
        line1.set_data([], [])
        line2.set_data([], [])
        return line1, line2
    
    def update(frame):
        embeddings1 = text1_embeddings[frame].squeeze().numpy()
        embeddings2 = text2_embeddings[frame].squeeze().numpy()
        combined_embeddings = np.vstack([embeddings1, embeddings2])
        pca = PCA(n_components=2)
        pca_result = pca.fit_transform(combined_embeddings)
        pca_text1 = pca_result[:len(embeddings1)]
        pca_text2 = pca_result[len(embeddings1):]
    
        line1.set_data(pca_text1[:, 0], pca_text1[:, 1])
        line2.set_data(pca_text2[:, 0], pca_text2[:, 1])
    
        # Add labels
        for i, (x, y) in enumerate(pca_text1):
            ax.text(x+0.5, y+0.5, text1_tokens[i], fontsize=9, color='red')
        for i, (x, y) in enumerate(pca_text2):
            ax.text(x+0.5, y+0.5, text2_tokens[i], fontsize=9, color='blue')
    
        ax.set_title(f"Layer {frame + 1}")
        return line1, line2
    
    ani = FuncAnimation(fig, update, frames=len(text1_embeddings), init_func=init, blit=True)
    HTML(ani.to_jshtml())
    
    ```
    
    Run the code in a Jupyter notebook or IPython environment to visualize the animation. The embeddings transition smoothly through the layers, and you can see how "one" and "1" (as well as other tokens) change their positions relative to each other in the PCA space across layers.
    
- this messes up because it keeps the previous frames
    
    My apologies for the oversight. To ensure that the previous frames are cleared and only the current frame's data is displayed, we need to make a few changes to the `update` function.
    
    Here's a corrected version of the code:
    
    ```python
    import torch
    import numpy as np
    import matplotlib.pyplot as plt
    from transformers import BertTokenizer, BertModel
    from sklearn.decomposition import PCA
    from matplotlib.animation import FuncAnimation
    from IPython.display import HTML
    
    # Initialize model and tokenizer
    model_name = "bert-base-uncased"
    model = BertModel.from_pretrained(model_name)
    tokenizer = BertTokenizer.from_pretrained(model_name)
    model.eval()
    
    # Tokenize and get embeddings for two sequences
    def get_embeddings(model, tokenizer, text):
        inputs = tokenizer(text, return_tensors="pt")
        with torch.no_grad():
            outputs = model(**inputs, output_hidden_states=True)
        return outputs.hidden_states
    
    text1 = "1 2 3 4"
    text2 = "one two three four"
    
    text1_embeddings = get_embeddings(model, tokenizer, text1)
    text2_embeddings = get_embeddings(model, tokenizer, text2)
    text1_tokens = tokenizer.tokenize(text1)
    text2_tokens = tokenizer.tokenize(text2)
    
    # Add [CLS] and [SEP] to token lists
    text1_tokens = ['[CLS]'] + text1_tokens + ['[SEP]']
    text2_tokens = ['[CLS]'] + text2_tokens + ['[SEP]']
    
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_xlim(-50, 50)
    ax.set_ylim(-50, 50)
    
    def update(frame):
        ax.clear()
    
        embeddings1 = text1_embeddings[frame].squeeze().numpy()
        embeddings2 = text2_embeddings[frame].squeeze().numpy()
        combined_embeddings = np.vstack([embeddings1, embeddings2])
    
        pca = PCA(n_components=2)
        pca_result = pca.fit_transform(combined_embeddings)
        pca_text1 = pca_result[:len(embeddings1)]
        pca_text2 = pca_result[len(embeddings1):]
    
        ax.scatter(pca_text1[:, 0], pca_text1[:, 1], color='red')
        ax.scatter(pca_text2[:, 0], pca_text2[:, 1], color='blue')
    
        # Add labels
        for i, (x, y) in enumerate(pca_text1):
            ax.text(x+0.5, y+0.5, text1_tokens[i], fontsize=9, color='red')
        for i, (x, y) in enumerate(pca_text2):
            ax.text(x+0.5, y+0.5, text2_tokens[i], fontsize=9, color='blue')
    
        ax.set_title(f"Layer {frame + 1}")
    
    ani = FuncAnimation(fig, update, frames=len(text1_embeddings), repeat=False)
    HTML(ani.to_jshtml())
    
    ```
    
    This version clears the entire plot before drawing the new data for the current frame. The `update` function includes an `ax.clear()` call at the beginning to achieve this effect. The result should now animate smoothly through the layers without any overlap from previous frames.
    
- We shouldn’t measure each token as a data pt. We should measure each input sequence as a data pt. Now, run this pca animation code on data pts of “1 2 3”, “1 2 3 4”, etc up to “1…10”
    
    Alright, to visualize each input sequence as a data point, we'll take the average of the embeddings of its tokens at each layer. This gives us a single vector representation for the entire sequence at each layer.
    
    Below is the PCA animation code that visualizes input sequences ranging from "1 2 3" up to "1 2 3 ... 10":
    
    ```python
    import torch
    import numpy as np
    import matplotlib.pyplot as plt
    from transformers import BertTokenizer, BertModel
    from sklearn.decomposition import PCA
    from matplotlib.animation import FuncAnimation
    from IPython.display import HTML
    
    # Initialize model and tokenizer
    model_name = "bert-base-uncased"
    model = BertModel.from_pretrained(model_name)
    tokenizer = BertTokenizer.from_pretrained(model_name)
    model.eval()
    
    def get_sequence_embedding(model, tokenizer, text):
        inputs = tokenizer(text, return_tensors="pt")
        with torch.no_grad():
            outputs = model(**inputs, output_hidden_states=True)
        hidden_states = outputs.hidden_states
        # Averaging token embeddings to get sequence embedding
        sequence_embeddings = [hidden_state.mean(dim=1).squeeze().numpy() for hidden_state in hidden_states]
        return sequence_embeddings
    
    # Create sequences
    sequences = [" ".join(str(i) for i in range(1, n+1)) for n in range(3, 11)]
    embeddings = [get_sequence_embedding(model, tokenizer, seq) for seq in sequences]
    
    fig, ax = plt.subplots(figsize=(10, 8))
    
    def update(frame):
        ax.clear()
        pca = PCA(n_components=2)
    
        # Extract embeddings of sequences for the current layer
        layer_embeddings = np.vstack([emb[frame] for emb in embeddings])
        pca_result = pca.fit_transform(layer_embeddings)
    
        ax.scatter(pca_result[:, 0], pca_result[:, 1], c='blue')
    
        # Add labels
        for i, (x, y) in enumerate(pca_result):
            ax.text(x+0.5, y+0.5, sequences[i], fontsize=9)
    
        ax.set_title(f"Layer {frame + 1}")
        ax.set_xlim(-15, 15)
        ax.set_ylim(-15, 15)
    
    ani = FuncAnimation(fig, update, frames=len(embeddings[0]), repeat=False)
    HTML(ani.to_jshtml())
    
    ```
    
    When you run this in a Jupyter notebook or IPython environment, you should see an animation that visualizes the evolution of PCA embeddings of the input sequences through the layers of the BERT model. The animation will depict how the sequences "1 2 3" up to "1 2 3 ... 10" relate to each other in the embedding space at each layer.
    

Given two input sequences, measure specifically the sim between two individual tokens in each sequence

We’re not looking for individual word + digit tokens to get closer. We’re seeing if one of the two PCA directions captures the sequence.

---

cluster_per_layer_draft.ipynb:

[https://colab.research.google.com/drive/1RqpONRcusICbxY3o76pos6MfmWhoxyEr](https://colab.research.google.com/drive/1RqpONRcusICbxY3o76pos6MfmWhoxyEr)

---

Not animation over time, but just from initial embedding to after name mover head. Visualize by project down using svd or pca.

[https://www.lesswrong.com/posts/mkbGjzxD8d8XqKHzA/the-singular-value-decompositions-of-transformer-weight](https://www.lesswrong.com/posts/mkbGjzxD8d8XqKHzA/the-singular-value-decompositions-of-transformer-weight)
Directions specialize

Object detection heads vs subject detection heads- do they interact with verb action heads?

Incovered flaws as I looked more into it, don't think it passes min reqs yet to prove anything about a circuit but has potential, as it has some evidence so far that can be expanded upon with better techniques like path patching and causal scrubbing

---

Analyzing Transformers in Embedding Space

To align models:

1. Unembed both weight parameter matrices into vocab space
2. Get pearson correlation for each pair of their projected values
3. Use algorithm to maximize the similarity matrix of their pearson correlation values to align layers between models 
    1.  (why layers, not components?)
    

So the pearson correlation similarity matrix measures similarity between two matrix unembeddings. We may be able to use this to measure the similarity between latent space activations in two inputs of the same model.

Ways to measure sim between two matrices:

1. Cosine sim avg
2. SVD Froebenius norm of singular values
3. KL divergence of logits
4.  pearson correlation similarity matrix between two matrix unembeddings

---

cluster_per_layer_draft_pt2.ipynb

[https://colab.research.google.com/drive/1Eu99NblHk2LbSRoKn2OxRZX8kIb9DYtR#](https://colab.research.google.com/drive/1Eu99NblHk2LbSRoKn2OxRZX8kIb9DYtR#)

BERT:

"Adam went to the store. Lamp went to the” ; “lamp”

VS

“Adam” ; “lamp”

Unfortunately, in both cases, Adam and lamp end up next to each other (relative to being far away at the start). So this isn’t influenced by the in-context tokens making lamp be more “subject-like”.

However, this doesn’t happen for this case:

```
text1 = "Adam Mark Mary Eve"
text2 = "table house lamp pen ball"
```

Perhaps the first visual was misleading as it was missing other data pts to compare to; so the space b/w Adam and lamp seemed small as it just squeezed them together?

This longer example already shows they form clusters at the start:

```
text1 = "Adam Mark Mary Eve John Chris Emily Diana"
text2 = "table house lamp pen ball window food"
```

[https://chat.openai.com/c/d1b9e4c5-c282-4bf2-9af0-066426fe1367](https://chat.openai.com/c/d1b9e4c5-c282-4bf2-9af0-066426fe1367)

---