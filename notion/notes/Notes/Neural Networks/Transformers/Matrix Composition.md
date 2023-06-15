# Matrix Composition

Purpose: see what info is moved by MM to understand how specifying these weight values allow heads to capture the “manipulation” (eg. inhibiting, enhancing, moving) certain features

Google: “transformers explained by matrix multiplications”

[https://ketanhdoshi.github.io/Transformers-Why/](https://ketanhdoshi.github.io/Transformers-Why/)

![Untitled](Matrix%20Composition%2055d6261a57dd414191f758b93a459ecc/Untitled.png)

![Untitled](Matrix%20Composition%2055d6261a57dd414191f758b93a459ecc/Untitled%201.png)

Above, we use one column vector for value (not the value matrix) to show what’s computed for one column of the attention scores. Each row (z_i) is for a query word (eg. blue):

![Untitled](Matrix%20Composition%2055d6261a57dd414191f758b93a459ecc/Untitled%202.png)

> If the vectors for two words are more aligned, the attention score will be higher.
For example, for the sentence, “The black cat drank the milk”, the word “milk” is very relevant to “drank”
For this to happen, the word vectors for “milk” and “drank” must be aligned.

The model will learn those embeddings and weights in such a way that if two words in a sentence are relevant to each other, then their word vectors will be aligned.
> 

GUESS: As such, look at the directions of vectors in heads to see what features they align with. First, find the heads. Then use code to go through each vector in the heads’ Q K and V, take the dot pro and compare them (for big vs tall, etc) to see “common directions”. Project on “common directions” to get “abstractions”- this may be where the analogy is compared.

- Decoder self-attention imgs
    
    ![Untitled](Matrix%20Composition%2055d6261a57dd414191f758b93a459ecc/Untitled%203.png)
    
    ![Untitled](Matrix%20Composition%2055d6261a57dd414191f758b93a459ecc/Untitled%204.png)
    
    ![Untitled](Matrix%20Composition%2055d6261a57dd414191f758b93a459ecc/Untitled%205.png)
    

---

[https://e2eml.school/transformers.html](https://e2eml.school/transformers.html)

- First order sequence model (Markov chain)
    
    For every word in the vocabulary, it shows what the next word is likely to be. If users ask about photos half the time, files 30% of the time, and directories the rest of the time, the transition model will look like this. The sum of the transitions away from any word will always add up to one.
    
    ![Untitled](Matrix%20Composition%2055d6261a57dd414191f758b93a459ecc/Untitled%206.png)
    
    ![Untitled](Matrix%20Composition%2055d6261a57dd414191f758b93a459ecc/Untitled%207.png)
    
    ![Untitled](Matrix%20Composition%2055d6261a57dd414191f758b93a459ecc/Untitled%208.png)
    
    This pulls out the relevant row and shows us the probability distribution of what the next word will be.
    
- Second order sequence model
    
    Predicting the next word based on only the current word is hard. That's like predicting the rest of a tune after being given just the first note.
    
    ![Untitled](Matrix%20Composition%2055d6261a57dd414191f758b93a459ecc/Untitled%209.png)
    
- ****Second order sequence model with skips****
    
    In this example, in order to determine which word should come after *ran*, we would have to look back 8 words into the past. If we want to improve on our second order language model, we can of course consider third- and higher order models. However, with a significant vocabulary size this takes a combination of creativity and brute force to execute. A naive implementation of an eighth order model would have *N*^8 rows, a ridiculous number for any reasonable vocubulary.
    
    Instead, we can do something sly and make a second order model, but consider the combinations of the most recent word with each of the words that came before. It's still second order, because we're only considering two words at a time, but it allows us to reach back further and capture **long range dependencies**.
    
    ![Untitled](Matrix%20Composition%2055d6261a57dd414191f758b93a459ecc/Untitled%2010.png)
    
    We've moved out of the Markov realm now. Each row no longer represents the state of the sequence at a particular point. Instead, each row represents one of many **features** that may describe the sequence at a particular point. The combination of the most recent word with each of the words that came before makes for a collection of applicable rows, maybe a large collection. Because of this change in meaning, each value in the matrix no longer represents a probability, but rather a vote. Votes will be summed and compared to determine next word predictions.
    
- De-embedding
    
    The de-embedding matrix is the same shape as the embedding matrix, but with the number of rows and columns flipped. The number of columns is the dimensionality of the space we're converting to — the size of the one-hot representation of the full vocabulary, 13 in our example.
    
- Embedding
    - *N*: vocabulary size. 13 in our example. Typically in the tens of thousands.
    - *n*: maximum sequence length. 12 in our example. Something like a few hundred in the paper. (They don't specify.) 2048 in GPT-3.
    - *d_model*: number of dimensions in the embedding space used throughout the model. 512 in the paper.
    
    The following nxN input matrix is ONE SENTENCE (each row is a token)
    
    ![Untitled](Matrix%20Composition%2055d6261a57dd414191f758b93a459ecc/Untitled%2011.png)
    
    After the initial embedding, the positional encoding is additive, rather than a multiplication, so it doesn't change the shape of things. Then the embedded word sequence goes into the attention layers, and comes out the other end in the same shape. (We'll come back to the inner workings of these in a second.) Finally, the de-embedding restores the matrix to its original shape, offering a probability for every word in the vocabulary at every position in the sequence.
    
    ![Untitled](Matrix%20Composition%2055d6261a57dd414191f758b93a459ecc/Untitled%2012.png)
    
- ****Why we need more than one attention head****
    - *d_k*: dimensions in the embedding space used for keys and queries. 64 in the paper.
    - *d_v*: dimensions in the embedding space used for values. 64 in the paper.
    - *h*: the number of heads. 8 in the paper.
    
    ![Untitled](Matrix%20Composition%2055d6261a57dd414191f758b93a459ecc/Untitled%2013.png)
    
    One tricky part about understanding this set of calculations is keeping in mind that it is calculating attention for every element of our input sequence, for every word in our sentence, not just the most recent word.
    
    It's also calculating attention for future words. These don't have much use yet, because they are too far out and their immediate predecessors haven't yet been chosen. But there are indirect paths through which these calculations can effect the attention for the most recent word, so we include them all.
    

---

[https://transformer-circuits.pub/2021/framework/index.html](https://transformer-circuits.pub/2021/framework/index.html)

[https://www.youtube.com/watch?v=Nw_PJdmydZY&t=398s&ab_channel=CodeEmporium](https://www.youtube.com/watch?v=Nw_PJdmydZY&t=398s&ab_channel=CodeEmporium)