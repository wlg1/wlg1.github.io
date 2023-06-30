# Superposition and Dropout

[https://www.lesswrong.com/posts/znShPqe9RdtB6AeFr/superposition-and-dropout](https://www.lesswrong.com/posts/znShPqe9RdtB6AeFr/superposition-and-dropout)

- in transformers, what's sparsity?
    
    In the context of transformers, sparsity refers to a property of the attention mechanism used in the transformer architecture. Attention mechanisms are used to weigh the importance of different parts of the input sequence when generating the output. The attention mechanism in transformers typically involves computing pairwise interactions between all positions in the input sequence.
    
    Sparsity in transformers refers to the idea of reducing the number of pairwise interactions that are computed during the attention computation. In a fully dense attention mechanism, each position attends to all other positions in the input sequence, resulting in a quadratic complexity in terms of computation and memory requirements. However, by introducing sparsity, only a subset of pairwise interactions are computed, reducing the computational and memory costs.
    
    There are different approaches to introducing sparsity in transformers. One common method is to use a sparse attention pattern, where only a fixed number of positions are attended to by each position. Another approach is to apply masking techniques to mask out certain pairwise interactions based on predefined patterns or learned attention scores. These sparse attention mechanisms help improve the efficiency of transformers, making them more scalable to longer input sequences.
    
- what is a sparse feature?
    
    In machine learning, a sparse feature refers to a feature that has a high proportion of zero or near-zero values compared to the total number of possible values. In other words, sparse features are those that exhibit sparsity in their representation.
    
    For example, consider a dataset of text documents. Each document can be represented using a bag-of-words model, where each unique word in the entire corpus forms a feature. In this case, the feature vector for a document would be a high-dimensional vector with a value of zero for most of the words, as each document typically contains only a small subset of the total vocabulary.
    
    Sparse features are common in many real-world datasets, including text, image, and sensor data. They arise due to the nature of the data, where only a subset of available features are relevant or active for each instance or sample. In such cases, representing the data using dense or fully populated vectors would be inefficient in terms of storage and computational resources.
    
    To handle sparse features, specialized data structures and algorithms are employed. Sparse matrices or sparse tensors are often used to efficiently store and process sparse data, where only non-zero values and their corresponding indices are stored. Additionally, specific machine learning algorithms and techniques, such as sparse regularization methods (e.g., L1 regularization or Lasso) or sparse coding techniques, are designed to effectively handle sparse features and exploit their sparsity for improved performance and efficiency.
    

near orth: If features are vectors, then vectors with many 0s are ‘sparse’. That is, similar to ‘low rank’ in a matrix, because it’s 0 at most neurons, and only a few neurons are used to define it. So it’s closer to being “one” neuron than less sparse vectors. This is the same as saying ‘more orthogonal’

However, that’s NOT how ‘sparse’ is used here. Though it’s similar due to this ‘sparse’ coinciding with ‘orth’.

sparse: “This happens more reliably when the features we are dealing with are sparse, that is, most of them aren't present most of the time. (for most inputs)”

Frequent features are less orthogonal, and have MORE inteference

superposition increases with sparsity: higher S → more superposition

higher S → less orthogonal

dropout generally inhibits superposition, except in the presence of both features with varying importance (exponentially decaying in this case) and low sparsity. I believe this is due to the need for some initial redundancy for a model with dropout, and a disproportionate increase in interference as this redundancy increases.

Thus, dropout induces a privileged basis (features aligned with neuron axes)

less dropout → more neurons → more superposition → more sparsity

<<<

Neurons ~ Dimensions (?)

When #features > #dims, then use multiple dims to represent a feature

Eg) 3 neurons represent a feature. That means feautre is (n1, n2) on 2D coordinate space using neurons as axis (dims)

![Untitled](Superposition%20and%20Dropout%20d5a635a009d04664a20a936b3b6ae86e/Untitled.png)

<<<

Features have interference if they share neurons? 

That is: Changing N1 will change F1(N1, …) and F2(N1,…) (?)

![Untitled](Superposition%20and%20Dropout%20d5a635a009d04664a20a936b3b6ae86e/Untitled%201.png)

<<<

“Superposition increases” means more features 

<<<

ISSUE: