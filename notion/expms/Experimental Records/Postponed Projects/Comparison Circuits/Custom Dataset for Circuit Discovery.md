# Custom Dataset for Circuit Discovery

Arguments to mod to alter dataset:

1. clean dataset
    1. prompt templates
    2. specific subjects (make into adjectives)
2. corrupted dataset
    1. how to flip specific adjectives of clean
    2. It shouldn’t actually matter what names you use, so just one sentence is fine.
3. circuit (DONE)
4. layer_heads (DONE)

---

Try to make one for tall/short and other size comparisons:

tall_short_circuit.ipynb

[https://colab.research.google.com/drive/1cFJc2Zc1fh_BXV42q3h4zfvRikINE_Mo#scrollTo=wsgXK6jvbE-s](https://colab.research.google.com/drive/1cFJc2Zc1fh_BXV42q3h4zfvRikINE_Mo#scrollTo=wsgXK6jvbE-s)

- ISSUE: How to give custom prompts to IOI dataset ?
    
    [https://github.com/redwoodresearch/Easy-Transformer/blob/main/easy_transformer/ioi_dataset.py](https://github.com/redwoodresearch/Easy-Transformer/blob/main/easy_transformer/ioi_dataset.py)
    
    See: `class IOIDataset`: ...
    
    - Args explanation
        - `prompt_type`: Specifies the type of prompts to generate. It can be either a string indicating a pre-defined prompt type or a list of custom templates.
        - `N`: The number of prompts to generate.
        - `tokenizer`: An instance of a tokenizer used to tokenize the prompts.
        - `prompts`: A list of pre-defined prompts. If provided, the prompts will be used instead of generating new ones.
        - `symmetric`: Specifies whether the prompts should be symmetric (ABBA or ABC) or asymmetric (BABA or BAC).
        - `prefixes`: Optional prefixes to add to the prompts.
        - `nb_templates`: The number of templates to use for generating prompts. It is used when `prompt_type` is a pre-defined type.
        - `ioi_prompts_for_word_idxs`: Custom prompts to use for calculating word indices. It can be different from the main prompts.
        - `prepend_bos`: Specifies whether to prepend a beginning-of-sentence token to each prompt.
        - `manual_word_idx`: Custom word indices to use instead of calculating them automatically.
        
        If you have any specific questions or need further assistance, please let me know.
        
    
    prompt type is required, and this is how it uses custom:
    
    `elif isinstance(prompt_type, list):` 
    
    `self.templates = prompt_type`
    
    try pronoun dataset: [https://colab.research.google.com/drive/1MQQgF-OA9Q4MM3iXcsY5GncBmwWQIYW5#scrollTo=KgVWG8vuH6AC](https://colab.research.google.com/drive/1MQQgF-OA9Q4MM3iXcsY5GncBmwWQIYW5#scrollTo=KgVWG8vuH6AC)
    
    - BUG: `dataset = IOIDataset(prompt_type=templates)`
        
        ```
        templates = [
            "So {name} is a really great friend, isn't",
            "So {name} is such a good cook, isn't",
            "So {name} is a very good athlete, isn't",
            "So {name} is a really nice person, isn't",
            "So {name} is such a funny person, isn't"
            ]
        
        dataset = IOIDataset(prompt_type=templates)
        ```
        
        ```python
        /usr/local/lib/python3.10/dist-packages/easy_transformer/ioi_dataset.py in __init__(self, prompt_type, N, tokenizer, prompts, symmetric, prefixes, nb_templates, ioi_prompts_for_word_idxs, prepend_bos, manual_word_idx)
            777         self.templates_by_prompt = []  # for each prompt if it's ABBA or BABA
            778         for i in range(N):
        --> 779             if self.sentences[i].index(self.ioi_prompts[i]["IO"]) < self.sentences[
            780                 i
            781             ].index(self.ioi_prompts[i]["S"]):
        
        ValueError: substring not found
        ```
        
        It seems that the custom templates you provided do not contain the placeholders for the names "[A]" and "[B]". The error message indicates that the substring representing the name ("IO" and "S") was not found in the sentences generated using the custom templates.
        
        To resolve this issue, you need to ensure that your custom templates include the placeholders "[A]" and "[B]" to represent the names in the prompts. Here's an updated example:
        
        ```python
        custom_templates = [
            "[A] gave [B] a [OBJECT].",
            "The [A] and [B] went to [PLACE].",
            "Once upon a time, [A] and [B] became friends.",
            # Add more custom templates as needed
        ]
        ```
        
    - BUG: tokenizer issue
        
        ```python
        ---------------------------------------------------------------------------
        ValueError                                Traceback (most recent call last)
        <ipython-input-15-2a5afc7d480f> in <cell line: 7>()
              5     # Add more custom templates as needed
              6 ]
        ----> 7 dataset = IOIDataset(prompt_type=custom_templates)
        
        2 frames
        /usr/local/lib/python3.10/dist-packages/easy_transformer/ioi_dataset.py in get_name_idxs(prompts, tokenizer, idx_types, prepend_bos)
            493                 )
            494             else:
        --> 495                 idx = toks.index(tokenizer.tokenize(" " + prompt[idx_type])[0])
            496             name_idx_dict[idx_type].append(idx)
            497         if "S" in idx_types and "S2" in idx_types:
        
        ValueError: 'ĠLauren' is not in list
        ```
        
        I apologize for the error. It seems that the tokenizer is not properly tokenizing the names in the custom templates. The error message indicates that the name "Lauren" is not found in the list of tokens.
        
        To resolve this issue, you can try adding a space character before each name in the custom templates. This will ensure that the tokenizer treats the names as separate tokens. Here's an updated example:
        
        ```
        custom_templates = [
            " [A] gave [B] a [OBJECT].",
            "The [A] and [B] went to [PLACE].",
            "Once upon a time, [A] and [B] became friends.",
            # Add more custom templates as needed
        ]
        ```
        
        By adding a space character before each name placeholder in the custom templates, the tokenizer will correctly tokenize the names as separate tokens and avoid the ValueError.
        

---

Customize your own logit diff:

logit_diff() is used in plot_path_patching, but that measures S and IO. Now, you're not doing that, so modify this function to your own custom one.

[https://github.com/redwoodresearch/Easy-Transformer/blob/main/easy_transformer/ioi_utils.py](https://github.com/redwoodresearch/Easy-Transformer/blob/main/easy_transformer/ioi_utils.py)

Before, the corrupted subbed the IOI with random names. Here, the corrupted should switch the size adjective to its antonym.

May just end up using logit_diff from exploratory analysis

What does it mean to run `circuit_logit_diff = logit_diff(model, dataset) ?`

The **`logit_diff`** function calculates the difference in logits between the input-output (IO) tokens and the substitute (S) tokens in a given model's output.

We run logit_diff before circuit extraction, then after, and compare the two logit_diffs. After patching, the logit diff should be lower, since it has a worse ability separating the correct and incorrect.

[https://github.com/redwoodresearch/Easy-Transformer/blob/main/easy_transformer/ioi_utils.py](https://github.com/redwoodresearch/Easy-Transformer/blob/main/easy_transformer/ioi_utils.py)

- how does logit_diff() take logit difference? which part of its code does it?
    
    The `logit_diff()` function in the provided code calculates the logit difference by subtracting the logits corresponding to the S tokens from the logits corresponding to the IO tokens. The specific code that performs this calculation is as follows:
    
    ```
    IO_logits = logits[
        torch.arange(len(ioi_dataset)),
        ioi_dataset.word_idx["end"],
        ioi_dataset.io_tokenIDs,
    ]
    S_logits = logits[
        torch.arange(len(ioi_dataset)),
        ioi_dataset.word_idx["end"],
        ioi_dataset.s_tokenIDs,
    ]
    
    return handle_all_and_std(IO_logits - S_logits, all, std)
    
    ```
    
    Let's break down this code:
    
    1. The `logits` tensor contains the model's output logits. It has a shape of `(batch_size, sequence_length, num_classes)`.
    2. The `IO_logits` tensor is obtained by indexing the `logits` tensor using three indexing operations:
        - `torch.arange(len(ioi_dataset))`: This creates a tensor containing a sequence of numbers from 0 to the length of the `ioi_dataset`. It is used to index the batch dimension of the `logits` tensor.
        - `ioi_dataset.word_idx["end"]`: This accesses the index corresponding to the "end" token in the `word_idx` dictionary of the `ioi_dataset`. It retrieves the index of the "end" token in the sequence dimension of the `logits` tensor.
        - `ioi_dataset.io_tokenIDs`: This represents the tensor of token IDs for the IO tokens in the `ioi_dataset`. It is used to index the class dimension of the `logits` tensor.
        
        The indexing operations together extract the logits corresponding to the IO tokens from the `logits` tensor. The resulting `IO_logits` tensor has a shape of `(batch_size,)` representing the logits for the IO tokens in each example of the batch.
        
    3. Similarly, the `S_logits` tensor is obtained by indexing the `logits` tensor using the same indexing operations but with `ioi_dataset.s_tokenIDs`. This retrieves the logits corresponding to the S tokens.
    4. The `IO_logits - S_logits` operation subtracts the S logits from the IO logits, resulting in a tensor of shape `(batch_size,)` representing the logit difference for each example in the batch.
    5. Finally, the `handle_all_and_std()` function is called with the logit difference tensor (`IO_logits - S_logits`) as the `returning` parameter, along with the `all` and `std` parameters. This function performs additional handling based on the values of `all` and `std`, as explained earlier.
    
    In summary, the logit difference is computed by subtracting the logits for the S tokens from the logits for the IO tokens, and the resulting difference is then passed to the `handle_all_and_std()` function for further processing and handling.
    

---

Run custom CIRCUIT through to do knockout and plot path patching

[https://github.com/redwoodresearch/Easy-Transformer/blob/main/easy_transformer/ioi_circuit_extraction.py](https://github.com/redwoodresearch/Easy-Transformer/blob/main/easy_transformer/ioi_circuit_extraction.py)