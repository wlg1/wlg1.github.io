# GPT

[https://huggingface.co/course/chapter1/6?fw=pt](https://huggingface.co/course/chapter1/6?fw=pt)

Decoder models use only the decoder of a Transformer model. At each stage, for a given word the attention layers can only access the words positioned before it in the sentence. (encoders can access both directions). These models are often called *auto-regressive models*.

The pretraining of decoder models usually revolves around predicting the next word in the sentence.

GPT is one.