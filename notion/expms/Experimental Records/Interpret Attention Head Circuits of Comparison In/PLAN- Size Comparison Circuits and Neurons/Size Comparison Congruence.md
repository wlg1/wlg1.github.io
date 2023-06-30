# Size Comparison Congruence

dotprod_size_tokens.ipynb

[https://colab.research.google.com/drive/1rch6VaG9O1YFJT1wPjjbXyDgXizGT7WV](https://colab.research.google.com/drive/1rch6VaG9O1YFJT1wPjjbXyDgXizGT7WV)

dotprod_size_tokens_GPTsmall.ipynb

[https://colab.research.google.com/drive/18JcQcn7TKhN-1ULNjqQqvst9yJ6ZDhAA](https://colab.research.google.com/drive/18JcQcn7TKhN-1ULNjqQqvst9yJ6ZDhAA)

### Working on

- Use dot products on more than input embeddings of first layer (w/ neuron outgoing weights)
    - Try at different points of residual stream- but that’s mixed with other parts of input

Get avg of large dot prods, compare to avg of random dotprods

### Future Work

- Figure out how not using QK and just using OV gets “full attention” (look at transformer matrix pipeline diagram and work it out on idroo)
    - [https://www.notion.so/Query-Key-Value-Matrices-fe92464f6ee24068b6aaa56bb85e903e](https://www.notion.so/Query-Key-Value-Output-Matrices-fe92464f6ee24068b6aaa56bb85e903e?pvs=21)
    - If we skip the attention matrix, that’s like if the attention matrix was the identity matrix. Then that means “fully attend to”. In terms of matrix multiplication summations, what does this look like?
        - It would be Id * v = z, so v = z. The outputs are just the value matrix, and it’s copied. The value matrix contains the “content”
        - If we directly mutliply input embeddings with W_v, we get something that’s not exactly the same as input. HOWEVER, these outputs (matrix v) are unembedded into vocab space, they would be like logit outputs, and each token in vocab has a logit value. If these logit values are strong on certain words, we can say the weight matrix W_v (not v) is “giving content” (attending to? need to think abou this) those tokens?
        - Do weights in the value matrix have a semantic relation to the input vectors? Are they considered "content"?
            
            

---

Run Congruence tests

It’s still uncertain what embeddings at each intermediate output represent. Thus, we will experiment with performing vector similarity comparisons (between inputs and neuron groups) at various output areas to see if they make semantic sense. We start by comparing initial embeddings with various neurons to see if there are any significant patterns, and try to explain if these patterns are caused by things indicating how the model is representing semantic features. Some approaches might not make sense at first, but if they find patterns, they may be onto something that warrants further investigation.

Dot product tokens and feature neurons:

This is how $W_E(X)$ works: [Embeddings](https://www.notion.so/Embeddings-c4e515f0f63844d8bdd5309d041e40cf?pvs=21) 

[https://colab.research.google.com/drive/1rch6VaG9O1YFJT1wPjjbXyDgXizGT7WV#scrollTo=x-hNAqAk5KMX](https://colab.research.google.com/drive/1rch6VaG9O1YFJT1wPjjbXyDgXizGT7WV#scrollTo=x-hNAqAk5KMX) 

- Dot prod of large and huge and decline

[https://colab.research.google.com/drive/1rch6VaG9O1YFJT1wPjjbXyDgXizGT7WV#scrollTo=aFF09zMeuNFL&line=1&uniqifier=1](https://colab.research.google.com/drive/1rch6VaG9O1YFJT1wPjjbXyDgXizGT7WV#scrollTo=aFF09zMeuNFL&line=1&uniqifier=1)

The average dot product between two unrelated tokens (no spaces in front) seems to be around 0.8. So if it’s more, there is some similarity. If we try a dataset of tokens, we can obtain an average

- If the word isn't a single token, how can we get the dot product of it with other tokens?
    
    In language models like GPT-2, longer words or less common words might not be represented as a single token but rather a sequence of subword tokens. If you want to compute the dot product (or any kind of similarity) between such a word and another token or word, you would need to handle this token sequence.
    
    There are different approaches you could take. One simple approach is to average the embeddings of the subword tokens to get a single vector representation for the word, and then compute the dot product with this averaged vector. Here's an example:
    
    ```
    from transformers import GPT2Model, GPT2Tokenizer
    
    # Instantiate the model and the tokenizer
    model = GPT2Model.from_pretrained('gpt2-large')
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2-large')
    
    # Get the embeddings from the model
    embeddings = model.get_input_embeddings()
    
    # Tokenize the words and get their ids
    word1_ids = tokenizer.encode('large', return_tensors='pt')
    word2_ids = tokenizer.encode('huge', return_tensors='pt')
    
    # Get the embeddings for the tokens
    word1_embedding = embeddings(word1_ids).mean(dim=1)
    word2_embedding = embeddings(word2_ids).mean(dim=1)
    
    # Compute the dot product
    dot_product = torch.dot(word1_embedding.flatten(), word2_embedding.flatten())
    
    print(dot_product)
    
    ```
    
    This approach works reasonably well for many use cases, but note that it does not account for the context in which the word appears. A more sophisticated approach would be to use the actual output from the transformer model, which does take into account the surrounding context, but that's a more involved process.
    

[https://colab.research.google.com/github/neelnanda-io/TransformerLens/blob/main/demos/Main_Demo.ipynb#scrollTo=7hcPynASz8LO](https://colab.research.google.com/github/neelnanda-io/TransformerLens/blob/main/demos/Main_Demo.ipynb#scrollTo=7hcPynASz8LO)

Try the mean of all tokens:

[https://colab.research.google.com/drive/1rch6VaG9O1YFJT1wPjjbXyDgXizGT7WV#scrollTo=CevuC19u1tFh&line=1&uniqifier=1](https://colab.research.google.com/drive/1rch6VaG9O1YFJT1wPjjbXyDgXizGT7WV#scrollTo=CevuC19u1tFh&line=1&uniqifier=1)

Now the average is 0.4076. Perhaps taking the mean of all tokens isn’t the best.

Perhaps there’s a way to get their “final embedding”. Say “en”, “or”, “mous” are the tokens for the one word. We want the vector that’s at “mous”, after en and or are processed.

Compare dist of random one tokens vs “tall” synonomous tokens:

![Untitled](Size%20Comparison%20Congruence%20e94368b6a22a4e9e9d0d444b3c5972e5/Untitled.png)

![Untitled](Size%20Comparison%20Congruence%20e94368b6a22a4e9e9d0d444b3c5972e5/Untitled%201.png)

The “tall” synonyms seem around average.

Perhaps it’s only certain neurons that are the “middle man” making them in common. For instance, if tokens A and B don’t have big dot prod, but A with N and B with N both are high, then N finds what’s in common with them. This N is like the query and key weights.

- Using a list of dot products between a token and neuron, what are good ways to compare the similarity of lists of two tokens, such as between "large" and "tall"?
    
    When comparing the similarity of two lists of dot products between a token and neuron (assuming the lists are sorted and in the same neuron order), there are several approaches you can take. Here are a few methods:
    
    1. **Pearson Correlation Coefficient**: This measures the linear relationship between two datasets. Values always range between -1 (strong negative relationship) and 1 (strong positive relationship). A value near 0 implies weak or no linear relationship.
    2. **Spearman's Rank Correlation Coefficient**: This is a non-parametric measure of rank correlation. It assesses how well the relationship between two variables can be described using a monotonic function. Like the Pearson correlation coefficient, its values also range from -1 to 1.
    3. **Cosine Similarity**: This measures the cosine of the angle between two non-zero vectors. Its values range from -1 (completely dissimilar) to 1 (completely similar). This is a common measure for high-dimensional vectors, such as in word embeddings or other language model applications.
    4. **Euclidean Distance**: This is the "ordinary" straight-line distance between two points in Euclidean space. The smaller the Euclidean distance, the more similar the vectors.
    5. **Kendall Tau Distance**: Similar to Spearman's rank correlation, Kendall tau distance is a metric to measure the ordinal association between two measured quantities.
    
    The choice of method depends on what you believe is the best way to define similarity in the context of your task. Each of the above methods has different properties and can capture different types of relationships between the vectors.
    
    Please note, it is necessary to ensure that the neurons in the lists are in the same order when comparing them, and that you are taking into consideration the possibility that not all neurons may be equally influential in the model's output. For a more meaningful comparison, you might want to focus on neurons that have been identified as more significant in some way, for instance, through analysis of the model's attention patterns or the impact of individual neurons on the model's output.
    

We can also take the dot product of the two tensors themselves

[https://colab.research.google.com/drive/1rch6VaG9O1YFJT1wPjjbXyDgXizGT7WV#scrollTo=Wdpe4KeO_iwY&line=5&uniqifier=1](https://colab.research.google.com/drive/1rch6VaG9O1YFJT1wPjjbXyDgXizGT7WV#scrollTo=Wdpe4KeO_iwY&line=5&uniqifier=1)

If we isolate the neurons with the biggest impact, and only take the dot prod of tokens with those neurons, this similarity is prob even bigger.

- Why do we need distance metrics for vectors if we can just use the dot product for their similarity?
    
    The dot product and distance metrics like Euclidean distance or cosine similarity all provide ways of quantifying the similarity or difference between two vectors, but they emphasize different aspects of the vectors' relationship and are used in different contexts.
    
    1. Dot Product: The dot product of two vectors is a measure of the extent to which the vectors point in the same direction. If both vectors are normalized (i.e., they have a length of 1), then the dot product is equivalent to the cosine of the angle between them, ranging from -1 (vectors pointing in exactly opposite directions) to 1 (vectors pointing in exactly the same direction). This can be useful when the magnitude of the vectors is not important, only the direction they point.
    2. Euclidean Distance: The Euclidean distance (also known as L2 distance) between two vectors is a measure of the geometric distance between them in the vector space. This metric takes both direction and magnitude into account, and it's often used when the absolute difference between the vectors is important.
    3. Cosine Similarity: This is a measure of the cosine of the angle between two vectors. This metric gives a value between -1 and 1 which signifies the angle, and hence the similarity between two vectors. If the vectors are orthogonal, the cosine similarity is 0, if they are in the same direction, it's 1, and if they are diametrically opposed, it's -1. This is useful when the magnitude of the vectors does not matter, and we are only interested in the direction (as is often the case in text analysis tasks, for example).
    
    So, while the dot product can provide a measure of similarity, there are many cases where other distance or similarity metrics are more appropriate depending on what you want to emphasize or the specific requirements of your task.
    

[https://datascience.stackexchange.com/questions/744/cosine-similarity-versus-dot-product-as-distance-metrics](https://datascience.stackexchange.com/questions/744/cosine-similarity-versus-dot-product-as-distance-metrics)

[https://stats.stackexchange.com/questions/544951/when-to-use-dot-product-as-a-similarity-metric](https://stats.stackexchange.com/questions/544951/when-to-use-dot-product-as-a-similarity-metric)

- Dot prod of Chihuahua with dog+small, like king queen