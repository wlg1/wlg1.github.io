# V 2. Decipher execute_ft()

2. Decipher execute_ft()

- To chatgpt:
    
    Here is the code for **ft_main.py** Reply “yes”
    
- [Colons in arguments](https://www.notion.so/Python-f5fe14898d744a74819532b914123159)
- Pre-process requests for output
    
    ```python
    if request["target_new"]["str"][0] != " ":
                # Space required for correct tokenization
                request["target_new"]["str"] = " " + request["target_new"]["str"]
    ```
    
    This snippet ensures that the first character of the target_new string for each item in the requests list is a space character. This is necessary for correct tokenization using the provided tokenizer (tok). 
    
    The snippet first creates a deep copy of the requests list to avoid modifying the original list. Then, for each item in the requests list, it checks whether the first character of the str field of the target_new key is a space character. If it is not, it prepends a space character to the string.
    
    - Why does the first character need to be a space?
        
        When a string is tokenized using the **`tok`** tokenizer, it is split into a sequence of tokens. The first token in the sequence is a special token that represents the start of the sequence (the "beginning-of-sequence" token). For some tokenizers, this special token is represented by a space character.
        
- Format execution announcement
    
    ```python
    f"[{request['prompt'].format(request['subject'])}] -> [{request['target_new']['str']}]"
    ```
    
    [This is an f-string [REF]](https://www.notion.so/Python-f5fe14898d744a74819532b914123159)
    
    Why does `f"[{request['prompt'].format(request['subject'])}]` need .format()? I thought f-strings didn't? Give an example of inputs to be used in the code
    
    ```python
    request = {
        "prompt": "Please write a sentence about {0}:",
        "subject": "dogs",
        "target_new": {"str": "Dogs are loyal companions."},
    }
    ```
    
    `request['prompt'].format(request['subject'])` translates to:
    
    "Please write a sentence about {0}:”.format(”dogs”)
    
    = "Please write a sentence about dogs:”
    
    Thus, it needs format because `request['prompt']` is a string that uses .format()
    
- weights = {n : p}
    
    The dictionary comprehension maps parameter names (**`n`**) to their corresponding parameter values (**`p`**).
    
    ```python
    weights = {
            n: p
            for n, p in model.named_parameters()
            for layer in hparams.layers
            if hparams.rewrite_module_tmp.format(layer) in n
        }
    ```
    
    **`if hparams.rewrite_module_tmp.format(layer) in n`**
    The comprehension filters out any parameters whose name does not match a certain pattern based on the **`hparams`** parameter. The **`hparams.rewrite_module_tmp`** parameter is a string that specifies a template for the pattern that the parameter name must match. The **`{}`** placeholder in the template will be replaced with the layer number during each iteration of the comprehension. If the resulting string is a substring of the parameter name (**`n`**), the parameter will be included in the **`weights`** dictionary.
    
- v.detach()
    
    In PyTorch, a tensor can be detached from its computation graph by calling the **`detach()`**
     method on the tensor. Detaching a tensor means that its computation history is removed, and it becomes a standalone tensor that is not associated with any graph. The tensor can then be used as a constant in subsequent computations.
    
    `weights_copy[w_name] = w.detach().clone()`
    
    The purpose of detaching the tensor is to make sure that the cloned tensor **`weights_copy[w_name]`** is not associated with the computation graph of the original tensor **`w`**. This ensures that changes made to the original tensor during fine-tuning will not affect the cloned tensor, and the cloned tensor can be used as a reference for restoring the original weights of the model after fine-tuning.
    
- Define Inputs
    
    ```python
    texts = [r["prompt"].format(r["subject"]) for r in requests]
    targets = [r["target_new"]["str"] for r in requests]
    ```
    
    The **`texts`** variable: ["Please write a sentence about dogs:",…
    
    the **`targets`** variable: ["Dogs are loyal companions.",…
    
    Each member of requests is a dict of prompt, subject, target_new
    
- w.requires_grad = name in weights
    
    ```python
    for name, w in model.named_parameters():
            w.requires_grad = name in weights
    ```
    
    The purpose of this code is to tell PyTorch which parameters should have their gradients computed during backpropagation and which should be excluded. By default, all parameters of a PyTorch model have **`requires_grad`** set to **`True`**, which means that their gradients will be computed during backpropagation. However, for the fine-tuning process, we only want to compute the gradients of the weights that the user desires to change (i.e., the weights in the **`weights`** dictionary).
    
    The **`model.named_parameters()`** method returns an iterator over the named parameters of the model, where each parameter is represented as a tuple of **`(name, parameter)`** pairs. 
    
    The “in” statement checks whether the **`name`** variable is included in the **`weights`** dictionary. If the parameter is included in the dictionary, then its **`requires_grad`** attribute is T**rue.**
    
- loss_meter = AverageMeter()
    
    During each iteration of the fine-tuning loop, the **`loss_meter`** is reset using the **`reset()`**
     method. Then, for each batch of data, the **`update()`** method is called to add the batch loss to the **`loss_meter`**. At the end of each iteration of the loop (epoch), the average loss over all batches is computed using the **`avg`** property of the **`loss_meter`**. This provides a measure of how well the model is fitting the data and is used for monitoring the progress of the fine-tuning process.
    
- # Update loop: intervene at layers simultaneously
    
    `hparams.num_steps` are the total epochs
    
    - for txt, tgt in zip(…
        
        ```python
        for txt, tgt in zip(
                    chunks(texts, hparams.batch_size), chunks(targets, hparams.batch_size)
                ):
        ```
        
        This code block creates two lists of equal length: **`texts`** and **`targets`**. Each element in **`texts`** corresponds to an input text sequence, and each element in **`targets`** corresponds to the target sequence that the model should predict based on the input sequence.
        
        These two lists are divided into batches of size **`hparams.batch_size`** using the **`chunks()`** function, which yields successive batches of size **`hparams.batch_size`** until all elements in the list have been consumed. 
        
        For example, suppose **`texts`** contains 10 input sequences and **`targets`** contains 10 corresponding target sequences, and **`hparams.batch_size`** is set to 3. Then, **`chunks(texts, hparams.batch_size)`** will yield 4 batches: three batches of size 3 and one batch of size 1 (b/c 10 % 3 = 1), and **`chunks(targets, hparams.batch_size)`** will yield the corresponding target batches of size 3 and 1. The **`zip()`** function is then used to iterate over the 4 pairs of batches of **`texts`** and **`targets`**.
        
    

The following lies within `for txt, tgt in zip(...):`

- `inputs = tok(txt, return_tensors="pt", padding=True).to("cuda")`
    
    First, the **`txt`** sequences are tokenized using the tokenizer **`tok`**, which converts each sequence into a sequence of integer IDs representing the tokens in the sequence. The **`return_tensors`** argument specifies that the output should be a dictionary of PyTorch tensor. The **`padding=True`** argument specifies that the sequences should be padded to the same length using the padding token ID defined by the tokenizer.
    
- `last_token_inds = inputs["attention_mask"].sum(dim=1) - 1`
    
    This line of code computes the index of the last non-padding token in each input sequence.
    
    The **`inputs`** dictionary contains the attention mask tensor, which is a binary mask indicating which tokens in the input sequence should be attended to by the model (i.e., which tokens are not padding tokens). The attention mask tensor has the same shape as the input tensor, with a value of 0 for each padding token and 1 for each non-padding token.
    
    [Attention Mask](https://www.notion.so/Attention-Mask-5fe51dc6d90f4f7eb34bc6061060d44f) 
    
    The **`inputs["attention_mask"].sum(dim=1)`** computes the sum of the attention mask tensor along the second dimension, which corresponds to the sequence length. This produces a tensor of shape **`(batch_size,)`** containing the number of non-padding tokens in each input sequence.
    
    - Give an example of using sum to produces a tensor of shape (batch_size,)
        
        ```
        >>> input_tensor = torch.tensor([[1, 2, 3, 4, 5],
        ...                              [6, 7, 8, 9, 10],
        ...                              [11, 12, 13, 14, 15]])
        ```
        
        Now, let's say you want to compute the sum of each sequence in the batch. You can do this by calling the **`sum`** method on **`input_tensor`** along the second dimension (i.e., the sequence length dimension) [the columns], which has size 5:
        
        ```
        >>> input_tensor.sum(dim=1)
        tensor([15, 40, 65])
        ```
        
        The resulting tensor only has the first dim size (3), which corresponds to batch size
        
    
    Subtracting 1 from this tensor gives the index of the last non-padding token in each input sequence, since PyTorch uses zero-based indexing. The resulting **`last_token_inds`** tensor has shape **`(batch_size,)`** and contains the index of the last non-padding token in each input sequence, which will be used later to extract the model's predicted probability distribution over tokens for each sequence.
    
- `loss_mask = target_ids != tok.unk_token_id`
    
    In the context of the given code, **`loss_mask`** is a boolean tensor of the same shape as **`target_ids`**, where each element is **`True`** if the corresponding element in **`target_ids`** is not equal to the unknown token ID (**`tok.unk_token_id`**), and **`False`** otherwise.
    
    The purpose of **`loss_mask`** is to zero out the loss contribution of any tokens in **`target_ids`** that are unknown. This is done because the unknown token is a special token that is not predicted by the model, so it doesn't make sense to penalize the model for not predicting it correctly. By setting the loss contribution of unknown tokens to zero, we can effectively "ignore" them during training.
    
- opt.zero_grad()
    
    In PyTorch, the **`zero_grad()`** method is used to set the gradients of all the parameters in the model to zero. This is typically done at the start of each training iteration to ensure that the gradients from the previous iteration don't accumulate with the current gradients.
    
    By default, PyTorch accumulates gradients when **`backward()`** is called on a tensor. This is useful for certain types of models, such as recurrent neural networks, where the gradients need to be accumulated across multiple time steps. However, for most models, we want to compute the gradients for each batch separately, which requires setting the gradients to zero at the start of each batch.
    
- probs
    
    **`probs`** is a tensor representing the log probabilities of the predicted next token for each sequence in the batch. 
    
    ```python
    probs = torch.nn.functional.log_softmax(
                    model(**inputs).logits[torch.arange(bs), last_token_inds], dim=-1
                )
    ```
    
    - **`model([**inputs)](https://www.notion.so/Python-f5fe14898d744a74819532b914123159)`** applies the model to the input sequences, producing an output tensor with shape **`(batch_size, sequence_length, vocab_size)`**.
        - What are the arguments of model()?
            
            The **`AutoModelForCausalLM`** class is a subclass of the **`PreTrainedModel`** class, and provides a generic interface for working with various types of causal language models.
            
            The **`model()`** function takes input sequences as keyword arguments, which specify the input tensors that the model expects. The most common input tensors for language models are:
            
            - **`input_ids`**
            - **`attention_mask`**
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
                    
    - **`logits[torch.arange(bs), last_token_inds]`** selects the logit for the next token in each sequence by indexing into the **`logits`** tensor using the row indices in **`torch.arange(bs)`** and the column indices in **`last_token_inds`**. This produces a tensor of shape **`(batch_size, vocab_size)`**, where each row corresponds to the logit for the next token in the corresponding input sequence.
        - logits
            
            **`model().logits`** is a tensor of shape **`(batch_size, sequence_length, vocab_size)`**
             representing the logits (i.e., unnormalized log probabilities)
            
            logits = model(input_ids).logits
            
            This will give us a tensor logits of shape (2, 4, 50257), where 50257 is the size of the GPT-2 vocabulary. For example, the logits for the first position in the first input sequence would be:
            
            logits[0, 0]
            
            which would give us a tensor of shape (50257,) containing the logits for each token in the vocabulary.
            
        - logits using last token as index
            
            Now, suppose we want to extract the logits for the last token in each input sequence. We can do this using the **`last_token_inds`** tensor, which we calculated earlier using the attention mask:
            
            ```
            last_token_inds = input_ids.sum(dim=1) - 1
            ```
            
            Assuming that the last token in each input sequence is "on", **`last_token_inds`** would be: tensor([3, 3])
            
            ```
            last_token_logits = logits[torch.arange(2), last_token_inds]
            ```
            
            This will give us a tensor **`last_token_logits`** of shape **`(2, 50257)`**, containing the logits for the last token in each input sequence. For example, the logits for the last token in the first input sequence would be: `last_token_logits[0]`
            
            which would give us a tensor of shape **`(50257,)`** containing the logits for each token in the vocabulary, with higher logits indicating a higher probability of that token being the next token in the sequence.
            
    - **`torch.nn.functional.log_softmax(...)`** applies the log softmax function along the last dimension of the **`probs`** tensor. This converts the logits into log probabilities, which can be used to compute the cross entropy loss. The resulting tensor has the same shape as the input tensor, **`(batch_size, vocab_size)`**.
    - What does dim=-1 correspond to in this case?
        
        In the case of **`execute_ft()`**, the input tensor to **`log_softmax()`** has shape **`(batch_size, sequence_length, vocab_size)`**, where **`batch_size`** is the number of input examples, **`sequence_length`** is the length of each input sequence, and **`vocab_size`** is the size of the vocabulary. When **`log_softmax()`** is applied with **`dim=-1`**, it computes the softmax function across the last dimension of the input tensor, which corresponds to the vocabulary size. This results in a tensor of shape **`(batch_size, sequence_length, vocab_size)`** with values in the range (-inf, 0].
        
        - What are the output dims if we use dim=0?
            
            If **`dim=0`**, **`log_softmax()`** would compute the softmax function across the first dimension of the input tensor, which corresponds to the batch size. The output tensor would then have shape **`(1, sequence_length, vocab_size)`**, where each row corresponds to the softmax probabilities for each input sequence in the batch.
            
- loss
    
    ```python
    loss = -(torch.gather(probs, 1, target_ids) * loss_mask).sum(1) / loss_mask.sum(1)
    ```
    
    This line of code computes the negative log likelihood loss between the predicted probability distribution (given by `probs`) and the target sequence (given by `target_ids`).
    
    - `torch.gather()` selects the probability for the correct target token at each position, using `target_ids` as indices.
    - The expression `torch.gather(probs, 1, target_ids)` returns a tensor of shape `(batch_size, 1)` containing the probability for the correct target token at each position in the sequence. *[target_ids is seq turned into ids]*
        - Give an example of torch.gather(probs, 1, target_ids)
            
            Suppose we have `probs` tensor of shape `(2, 3)` as follows:
            
            ```
            tensor([[-1.2149, -1.1016, -1.4372],
                    [-1.2944, -1.1354, -1.2279]])
            ```
            
            And we have `target_ids` tensor of shape `(2, 1)` as follows:
            
            ```
            tensor([[0],
                    [1]])
            ```
            
            We can use `torch.gather` to extract the values in `probs` tensor that correspond to the indices specified in `target_ids`.
            
            ```
            gathered_probs = torch.gather(probs, 1, target_ids)
            ```
            
            The output `gathered_probs` will have shape `(2, 1)` and will contain the following values:
            
            ```
            tensor([[-1.2149],
                    [-1.1354]])
            
            ```
            
            This is because the first row corresponds to the first sequence, and it has 0, so it extracts the 0th index.
            
            The second row corresponds to the 2nd seq, and it has 1 in target_ids, so it extracts the 1st index.
            
            The probs here says: What’s the probability of predicting that target token ID? (eg. the ID can correspond to the word “bat”)
            
        - In torch.gather(probs, 1, target_ids), why 1?
            
            A gather operation along the second dim, which are the cols (each col is a pos in seq, so corresponds to ‘sequence length’)
            
    - The resulting tensor is multiplied element-wise with `loss_mask`, which is a binary mask indicating which tokens in `target_ids` are not padding tokens (i.e., tokens that should be predicted).
    - The expression `.sum(1)` computes the sum of the resulting tensor along the second dimension, giving a tensor of shape `(batch_size,)` containing the total loss for each sequence in the batch.
    - Finally, the expression `/ loss_mask.sum(1)` normalizes the loss by dividing it by the number of non-padding tokens in each sequence. This ensures that shorter sequences do not have an unfair advantage in the loss calculation.
    
- If the mean loss > 0.01, gradients are backpropagated and the parameters are updated
- `if type(hparams.norm_constraint) is float:`
    
    Enforces a norm constraint on the model weights by clamping their values within a certain range. Can prevent the model from overfitting to the training data and can help the model generalize better to new data. By restricting the magnitude of the weights, the model is encouraged to find a solution that is simpler and less prone to overfitting.
    
    [Clamping](https://www.notion.so/Clamping-2e2f6208c50744b29c54b8b6edb64518) 
    
    ```python
    if type(hparams.norm_constraint) is float:
                    eps = hparams.norm_constraint
                    with torch.no_grad():
                        for k, v in weights.items():
                            v[...] = torch.clamp(
                                v, min=weights_copy[k] - eps, max=weights_copy[k] + eps
                            )
    ```
    
    This block of code checks if a `norm_constraint` hyperparameter is specified in the `hparams` object and if it is a float. If it is, it loops over the `weights` dictionary and applies the following operation for each weight tensor `v`:
    
    ```
    v[...] = torch.clamp(v, min=weights_copy[k] - eps, max=weights_copy[k] + eps)
    ```
    
    This operation clamps the values of `v` between `min=weights_copy[k] - eps` and `max=weights_copy[k] + eps`.,  where eps is the norm constraint specified in hparams (from a file). The ellipsis (`[...]`) in the left-hand side of the assignment indicates that the values of `v` should be modified in place.
    
    The weights are modified in place because it is more efficient than creating a new tensor with the modified values. Therefore, it is a memory-efficient way to modify the tensor without creating a new tensor.
    

The following lies outside `for txt, tgt in zip(...):`

- if the average of losses over the batches is less than 1e-2. If the condition is true, then the training loop is broken out of, and the function returns the final weights of the model. This is a stopping criterion for the training loop, which allows for early stopping if the model has converged to a satisfactory level of performance.
- `deltas = {k: (weights[k] - weights_copy[k]).detach() for k in weights}`
    
    A dictionary containing the parameter names (keys) and their corresponding differences between the current weights and their copies (values) from the previous step. The **`detach()`** method is used to prevent these values from having gradients, since we only want to record the differences in parameter values at this point, not their contribution to the gradients.
    

The fine tuning updates the loss using only the examples of (input seq, target seq) passed in.