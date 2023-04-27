# Transformers

Autoregressive refers to a type of mathematical model where a variable is modeled as a function of its own past values. In other words, it predicts future values based on previous values of the same variable.

[Tokenizers](Transformers%2003e1e4e7e9654bd199395f7c72a88571/Tokenizers%20f9909472886e40ccbabcf1f4d8349f41.md)

[Query, Key, Value Matrices](Transformers%2003e1e4e7e9654bd199395f7c72a88571/Query,%20Key,%20Value%20Matrices%20fe92464f6ee24068b6aaa56bb85e903e.md)

[Self-attention](Transformers%2003e1e4e7e9654bd199395f7c72a88571/Self-attention%2064a3e43e6ac8491f8a7ddc54a071b903.md) 

[Attention Mask](Transformers%2003e1e4e7e9654bd199395f7c72a88571/Attention%20Mask%205fe51dc6d90f4f7eb34bc6061060d44f.md)

[Residual Stream](Transformers%2003e1e4e7e9654bd199395f7c72a88571/Residual%20Stream%201ce90f23f8f44b2b80b150c2f4b99226.md) 

- If transformers only output one word at a time, how can it choose a word based on future words further in the sequence? For example, it can output yes as its first word, yet doesn't this depend on knowing all other words in its answer?
    
    
    In a transformer network, the output at each position depends on the input tokens and the output tokens generated up to that point, but not on future tokens beyond that position. Therefore, the transformer network is not able to directly "see" future tokens when generating the output sequence.
    However, the transformer network is designed to capture long-range dependencies between the input and output sequences through the self-attention mechanism. During the self-attention computation, each input token is compared to all other tokens in the sequence, allowing the network to dynamically focus on different parts of the input sequence and capture complex patterns and relationships between the tokens.
    Similarly, during the decoding phase (i.e., when generating the output sequence), the network uses the previously generated output tokens as input to generate the next token in the sequence. While the network does not have access to future tokens at each decoding step, it can use the attention weights learned during training to capture dependencies between the output tokens and the input sequence.
    Therefore, while the transformer network is not able to directly see future tokens when generating the output sequence, it can capture complex patterns and relationships between the input and output sequences through the self-attention mechanism and the use of previously generated output tokens as input. This allows the network to generate coherent and meaningful output sequences based on the input sequence and the context provided by the previously generated output tokens.
    

---

[GPT](Transformers%2003e1e4e7e9654bd199395f7c72a88571/GPT%20108c635e0f0849ac8e556c91c892dec2.md) 

[Relation to Graph NNs](Transformers%2003e1e4e7e9654bd199395f7c72a88571/Relation%20to%20Graph%20NNs%20149398714b1e4f6f9affe076359a067c.md)