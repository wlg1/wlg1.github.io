# Tokenizers

The **`AutoModelForCausalLM`** class is a subclass of the **`PreTrainedModel`** class, and provides a generic interface for working with various types of causal language models.

The **`model()`** function takes input sequences as keyword arguments, which specify the input tensors that the model expects. The most common input tensors for language models are:

- **`input_ids`**
    - `inputs = tok(txt, return_tensors="pt", padding=True).to("cuda")`
        
        First, the **`txt`** sequences are tokenized using the tokenizer **`tok`**, which converts each sequence into a sequence of integer IDs representing the tokens in the sequence. The **`return_tensors`** argument specifies that the output should be a dictionary of PyTorch tensor. The **`padding=True`** argument specifies that the sequences should be padded to the same length using the padding token ID defined by the tokenizer.
        
- **`[attention_mask](Attention%20Mask%205fe51dc6d90f4f7eb34bc6061060d44f.md)`**
- **`token_type_ids`**: A tensor of 0s and 1s that specifies which segments of the input sequence correspond to different sentences or parts of the text.
    - Give an example of token_type_ids
        
        The `token_type_ids` tensor is used to distinguish between different segments of text within a single input sequence. This is often used in tasks such as question-answering or sentiment analysis, where the input sequence may consist of multiple sentences or phrases that need to be treated differently by the model.
        
        For example, suppose we have the following input sequence:
        
        ```
        "Mary had a little lamb. Its fleece was white as snow. It followed her to school one day."
        ```
        
        We can split this sequence into two segments by marking the end of the first sentence with a special token, such as `[SEP]`:
        
        ```
        "Mary had a little lamb. [SEP] Its fleece was white as snow. It followed her to school one day."
        ```
        
        We can then create a `token_type_ids` tensor that assigns a unique identifier to each segment. For example, we might use `0` to represent the first segment (i.e., the sentence containing "Mary had a little lamb"), and `1` to represent the second segment (i.e., the sentence containing "Its fleece was white as snow. It followed her to school one day."):
        
        ```
        tensor([[0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])
        ```
        
        This tensor has the same shape as the `input_ids` tensor, and each element corresponds to a single token in the input sequence. The first segment (tokens 1-7) has a `token_type_id` of `0`, and the second segment (tokens 9-18) has a `token_type_id` of `1`. The special `[CLS]` and `[SEP]` tokens also have their own unique `token_type_id`s.
        

---

CLS:

CLS (short for "classification") is a special token used in some pre-trained language models, such as BERT and RoBERTa, to represent the beginning of a sentence or sequence of tokens. In BERT, for example, the input to the model consists of a sequence of tokens of variable length, where each sequence is preceded by the special [CLS] token. The output of the model is a fixed-size vector representation of the entire input sequence, obtained by applying a pooling function (such as max-pooling or mean-pooling) over the output vectors of all tokens, including the [CLS] token.

The [CLS] token is used as a classifier token, since it is the first token in the input sequence and is intended to capture the overall meaning of the sequence. The output of the [CLS] token can be used as an input to a downstream classification or regression task, or as a feature representation for downstream models.

---

is vocab size total number of tokens?

The vocabulary size is the number of unique tokens in the language model's vocabulary. It does not necessarily correspond to the total number of tokens in the dataset or corpus that the language model was trained on. For example, a language model trained on a large corpus of text may have a vocabulary size of several hundred thousand tokens, even if the corpus contains billions of tokens.