# Done

[ArXiV Draft v1](Done%20b715c92198314529880806d9f206803d/ArXiV%20Draft%20v1%2035c75a5f1929460fb199edd5fce9a6fe.md)

Work after Draft v1

- ✅ plan circuits re-use
    
    Based on the lit review I’ve been doing last week, in the “Circuits re-use” paper (merullo 2023), the model editing is done by making inhibition heads found in IOI focus on the “wrong answers” for colored circuits. For GPT-2 Small, it seems the three circuits for the three seq cont tasks share 3 components, but it doesn’t seem like there’s an interesting way to show how editing one affects the other. It’s already shown in the paper that ablating one (or all 3) of the impt components will break all the tasks (in the ‘drop heads’ table). But I think for more impactful model editing we’d need to broaden what tasks are looked at, which can be done by looking for other overlapping tasks in bigger models (gp2-small has been hard to work with due to how limited it is). 
    
    Also, this NAACL paper may not be centered around model editing if we also develop another method, say a way to compare overlapping circuits between models using a quantifiable metric (this was an open problem stated by [merullo 2023]). I think making first steps in the quantifiable metric on overlap could be more novel, perhaps not as difficult to develop as model editing. There is a paper about using embedding space distance that can be used here. I can discuss more of this tomorrow/later this week as I am not at a spot I can meet today.
    
    Lastly the “circuit breaking” paper is about removing entire behaviors from models, not sure how it can be used: [https://anonymous.4open.science/r/circuit-breaking-5DE5/README.md](https://anonymous.4open.science/r/circuit-breaking-5DE5/README.md)
    
- 🐣 test inputs on bigger models
    
    many of the transformerlens libs cannot work on TPU, only on GPU. Use V100 for gpt2-xl
    
    [even xl can’t do fibonacci](https://colab.research.google.com/drive/1a2P7GW6HVSIYPeaO96pKnyjQtkBzXcvG#scrollTo=jm0PDoL_gj7R&line=2&uniqifier=1). xl has 1.5B params. what of its train data and arch?
    
    [it’s also unable to do x2 consistently](https://colab.research.google.com/drive/1a2P7GW6HVSIYPeaO96pKnyjQtkBzXcvG#scrollTo=hTaVrPsUZAZJ&line=1&uniqifier=1)
    
    - [But neo2.7B is able to do x2, and fibonacci if enough members](https://colab.research.google.com/drive/1KGN0nLfNYrnj81k75_pHTmt8xRSTEtff#scrollTo=hTaVrPsUZAZJ&line=1&uniqifier=1)
    - [but not always](https://colab.research.google.com/drive/1KGN0nLfNYrnj81k75_pHTmt8xRSTEtff#scrollTo=CNeMRSm_g3yP&line=2&uniqifier=1)
- ✅ why make batch size the same as model dim?
    
    Making the batch size the same as the model dimension is not a standard or widely recommended practice in machine learning or deep learning
    
- ✅ train 1L model specializing in seqs
    
    From: One Attention Head Is All You Need for Sorting Fixed-Length Lists
    
    [0_Template_train_sort.ipynb](https://colab.research.google.com/drive/1od5RRnhZpetBfPG0GrZK-Lj8RS-bgtYO) : this outputs a sorted list. But you don’t want the sorted list; you just want the prediction for the last element. So modify acc fn to not say the output should be sorted, but it should be the “next element”.
    
    - compare sorted loss fn w/ one from here: [https://colab.research.google.com/github/neelnanda-io/Easy-Transformer/blob/clean-transformer-demo/Clean_Transformer_Demo.ipynb#scrollTo=sQBWSvfwK34G](https://colab.research.google.com/github/neelnanda-io/Easy-Transformer/blob/clean-transformer-demo/Clean_Transformer_Demo.ipynb#scrollTo=sQBWSvfwK34G)
    - modify both acc_fn (for valid) and lossFn (for traindata)
    - log_softmax
        
        We need to know what log_softmax does so that when we modify the loss fn for new tasks, we need to know if we need to modify log_softmax, and if so, how.
        
        Let logits have dim [batch_size=2, seq_len=3, vocab_size=4]
        
        Each batch of logits is a 2-dimensional tensor with shape `[3, 4]`. The "last dimension" in this context refers to the innermost dimension when the tensor is viewed as a nested list, which is the dimension with size `4` in this case. Each inner list (or row) has four elements.
        
        When operations like `softmax` or `log_softmax` are applied along the last dimension (`dim=-1`), they are performed independently on each row. [The last dim is the class set, which is the vocab]
        
        For each list, the operation converts these values into a probability distribution, where each element is a probability corresponding to a class or category, typically in a machine learning classification task. In this case, each row could represent the log probabilities of different classes for a specific instance or time step in a sequence.
        
        ![Untitled](Done%20b715c92198314529880806d9f206803d/Untitled.png)
        
    - diffs between correct log prob in sort vs clean demo
        
        1. `correct_log_probs = log_probs.gather(-1, tokens[..., None])[..., 0]`
        
        - **Purpose:** This line is typically used to select the log probabilities of the correct tokens (or classes) from a set of log probabilities (`log_probs`). It's commonly seen in the context of calculating the loss function in training a language model or any classification task.
        - The **`tokens`** tensor contains the indices of the correct or target tokens (or classes). In a language modeling context, these would be the actual next tokens in the text sequences being modeled. Its shape is generally **`[batch_size, sequence_length]`**, with each element representing the index of the correct token at that position in the sequence.
        - `tokens[..., None]` adds an extra dimension to `tokens` for compatibility with `log_probs` for gathering.
            - The **`...`** (ellipsis) means "all preceding dimensions," and **`None`** is an indexing trick that adds a new dimension. After this operation, the shape of **`tokens`** becomes **`[batch_size, sequence_length, 1]`**.
            - If we just use `log_probs.gather(-1, tokens[[...]]).shape` or `log_probs.gather(-1, tokens).shape`, [gather](https://stackoverflow.com/questions/50999977/what-does-the-gather-function-do-in-pytorch-in-layman-terms) won’t work because it requires the indices (`tokens`) to have the same shape as `log_probs`. Since `tokens` is missing a dim, we need to add one more. This
        - `.gather(-1, ...)` selects elements along the last dimension (`num_classes`) of `log_probs` using the indices in `tokens`.
            - Eg) If tokens
        - `[..., 0]` removes the added dimension, resulting in a tensor of the same shape as `tokens`.
        
        2. `pred_log_probs = log_probs[:, :-1].gather(dim=-1, index=tokens[:, 1:].unsqueeze(-1)).squeeze(-1)`
        
        - **Purpose:** This line seems to be used for a similar purpose, but with a focus on selecting the log probabilities of predicted tokens, typically in a language modeling context where the model predicts the next token.
        - `log_probs[:, :-1]` slices `log_probs` to exclude the last token in the sequence for each batch. This is because the prediction for the last token doesn't have a subsequent true token for comparison.
        - `tokens[:, 1:].unsqueeze(-1)` shifts the token indices by one position and adds an extra dimension, aligning the predicted tokens with the actual next tokens in the sequence.
            - `tokens.unsqueeze(-1)` and `tokens[..., None]` **do the same thing**
        - `.gather(dim=-1, index=...)` then selects the log probabilities of these shifted tokens.
        - `.squeeze(-1)` removes the extra dimension added earlier, resulting in a tensor that aligns with the sequence length of `log_probs[:, :-1]`.
            - same as `[..., 0]`
        - Why does the second use [:, :-1]? Why does it use tokens[:, 1:]?
            - **`log_probs[:, :-1]`:**
                - This slices the **`log_probs`** tensor to exclude the last set of predictions for each sequence in the batch. In a sequence prediction task, the model predicts the next token based on the previous ones. For the last token in a sequence, there is no 'next token' to predict, so it's excluded.
                - The shape of **`log_probs`** is **`[batch_size, sequence_length, num_classes]`**. Slicing with **`[:-1]`** reduces the **`sequence_length`** by 1.
            - **`tokens[:, 1:]`:**
                - This slices the **`tokens`** tensor to start from the second token in each sequence. The reason for this shift is that in many sequence modeling tasks, the prediction for each position is about what comes next. So, for the first position, you're interested in the second token as the correct prediction, and so on.
                - This aligns the targets (**`tokens[:, 1:]`**) with the predictions (**`log_probs[:, :-1]`**), ensuring that each prediction is paired with the correct subsequent token in the sequence.
        
        ### Comparison and Contrast:
        
        - **Context of Use:** Both are used in scenarios involving selections from a tensor of log probabilities, but `correct_log_probs` focuses on the correct tokens as per ground truth, while `pred_log_probs` seems to focus on the predicted next tokens.
        - **Indexing Method:** Both use `gather`, but `correct_log_probs` directly indexes with `tokens`, while `pred_log_probs` involves slicing and shifting of both `log_probs` and `tokens` to focus on next-token prediction.
        - **Resulting Shape:** The resulting tensor shapes should align with the sequence lengths they are concerned with – `correct_log_probs` aligns with the original sequence length, while `pred_log_probs` aligns with one less than the original sequence length (due to the prediction nature of the task).
        
        ### S**ummary**
        
        - In **`correct_log_probs`**, the focus is on the entire sequence, including the correct tokens at each position, matching them with their corresponding log probabilities.
        - In **`pred_log_probs`**, the focus shifts to predicting the next token in the sequence. By using **`[:, :-1]`** and **`[:, 1:]`**, the code aligns each prediction with the token that follows it in the sequence. This shift is crucial for training models on tasks where the objective is to predict subsequent elements of the sequence, like next-word prediction in language models.
    - How come the first doesn't need to use log_probs[:, :-1]?
        
        The difference in usage of `log_probs[:, :-1]` between the first and the second line of code reflects different objectives or contexts in which these operations are used.
        
        ### 1. `correct_log_probs = log_probs.gather(-1, tokens[..., None])[..., 0]`
        
        In this line, the aim is to gather the log probabilities of the correct tokens at each position in a sequence from the `log_probs` tensor. Here, the focus is on evaluating the model's predictions for each token in the sequence against the ground truth. This operation is typical in scenarios like calculating loss functions where you need to consider the model's prediction for each token (including the last token in the sequence) and compare it with the actual token.
        
        - It doesn't use `[:, :-1]` because it needs to consider the entire sequence length. Each element in `tokens` corresponds to a position in `log_probs`, and you're interested in the log probability for every token position, including the last one.
        
        ### 2. `pred_log_probs = log_probs[:, :-1].gather(dim=-1, index=tokens[:, 1:].unsqueeze(-1)).squeeze(-1)`
        
        This line is specifically structured for sequence prediction tasks, such as language modeling, where the model's task is to predict the next token in a sequence.
        
        - The `log_probs[:, :-1]` is used to align the model's predictions with their corresponding targets in `tokens[:, 1:]`. In this scenario, for each token in a sequence except the last one, the model makes a prediction about the next token. That's why the `[:-1]` slice is used – it excludes the log probabilities for the last position in each sequence, as there is no subsequent token to predict.
        - The `tokens[:, 1:]` shift ensures that each prediction is paired with the correct subsequent token. For example, the model's prediction for the first position in a sequence should be evaluated against the second token, and so on.
        
        ### Summary
        
        - The first line is used in a context where each token's prediction needs to be evaluated, including the last one. Therefore, it doesn't exclude any part of the sequence.
        - The second line is used in a predictive context, where the model's task is to predict the next token. It aligns each prediction (except for the last one, as there is no next token) with the actual next token in the sequence.
    - What if we use log_probs[:, :-1].gather(dim=-1, index=tokens[:, -1].unsqueeze(-1)).squeeze(-1)
        
        If you use `log_probs[:, :-1].gather(dim=-1, index=tokens[:, -1].unsqueeze(-1)).squeeze(-1)`, you are applying a gather operation in a way that doesn't align with the usual objectives of sequence modeling or language prediction tasks. Let's break down what this line of code does:
        
        ### Understanding the Components:
        
        1. **`log_probs[:, :-1]`:**
            - This slices the `log_probs` tensor to exclude the last set of log probabilities for each sequence in the batch. The shape becomes `[batch_size, sequence_length - 1, num_classes]`.
            - The intention here is typically to align predictions with their corresponding targets in a sequence prediction task. Each position predicts the next token.
        2. **`tokens[:, -1]`:**
            - This selects only the last token from each sequence in the `tokens` tensor. The shape becomes `[batch_size]`.
            - Using `[:, -1]` significantly changes the context because now, irrespective of the sequence position, you are only looking at the last token of each sequence.
        3. **`unsqueeze(-1)` and `squeeze(-1)`:**
            - These operations adjust dimensions for the gather operation. `unsqueeze(-1)` converts `tokens[:, -1]` from `[batch_size]` to `[batch_size, 1]`.
            - After the gather operation, `squeeze(-1)` removes this extra dimension.
        
        ### Result of the Operation:
        
        - By using `tokens[:, -1].unsqueeze(-1)`, you're essentially telling the gather operation to select log probabilities corresponding to the last token of each sequence across all positions (except the last one) in `log_probs`.
        - This is a bit counterintuitive in typical sequence modeling tasks. Usually, each position in a sequence should be aligned with the corresponding target token. By focusing only on the last token for each sequence, you're misaligning this relationship.
        
        ### Implication:
        
        - The resulting tensor doesn't align with standard sequence prediction objectives. It would create a tensor where, for each sequence in the batch (except the last position), the model's log probability prediction is aligned not with the subsequent token (as is usual in language modeling) but always with the last token of the sequence.
        - Such an operation could potentially be used in a very specific context or task, but it's not standard in typical language modeling or sequence-to-sequence prediction tasks. The model's learning from this operation would likely be confusing or misaligned with the usual objectives of predicting the next token in a sequence.
    - if correct_log_probs has dims [batchsize, seqlen], what does -correct_log_probs.mean() do?
        
        When `correct_log_probs` has dimensions `[batch_size, seq_len]`, the operation `-correct_log_probs.mean()` computes the average of all values in the `correct_log_probs` tensor and then negates the result. Let's break down what this means and its implications:
        
        1. **Shape of `correct_log_probs`:**
            - The tensor `correct_log_probs` with shape `[batch_size, seq_len]` implies that for each example in the batch (represented by `batch_size`) and for each position in the sequence (represented by `seq_len`), there is a corresponding log probability value. These values represent the log probabilities of the correct tokens or classes at each position in the sequence.
        2. **Mean Operation (`mean()`):**
            - `.mean()` calculates the mean (average) of all the values in the `correct_log_probs` tensor. This operation flattens the tensor and computes the average across all dimensions, effectively reducing it to a single scalar value.
            - This mean represents the average log probability of the correct predictions across all sequences and all positions within those sequences in the batch.
        3. **Negative Sign (``):**
            - The negative sign before the mean operation converts this average log probability into a loss value.
            - Since log probabilities are negative (logarithms of probabilities between 0 and 1), taking the negative of these values converts them into positive values. Higher log probabilities (closer to zero, less negative) result in lower loss values, which is desirable in training.
            - The goal in training is to minimize this loss value, which corresponds to maximizing the log probabilities of the correct classes or tokens.
        4. **Implication in Training:**
            - The operation `correct_log_probs.mean()` essentially computes the Negative Log Likelihood Loss (NLL Loss) over the entire batch and sequence. This is a standard approach in many sequence modeling tasks, like language modeling, where the model learns by predicting the next token or class in a sequence.
            - By minimizing this loss during training, the model is encouraged to increase the log probabilities of the correct tokens or classes, thereby improving its predictive accuracy.
        
        In summary, `-correct_log_probs.mean()` calculates the average loss per token in the batch across all sequences. This average loss is used during the optimization process to update the model's parameters, aiming to improve the model's predictions over time.
        
    - ✅ get correct loss fn using gpt
- ✅ debug why repeat runs can’t get model to train
    
    somehow, with the current seeds, placing another new model right before training destroys this ability. 
    
    TRAIN_SEED = 42
    VAL_SEED = 66
    TEST_SEED = 1729
    
    doesn’t matter if re-make val and test data or not
    
    it DOES matter if call model right before because it skips this crucial line:
    
    `optim = torch.optim.Adam(model.parameters(), lr=lr, betas=betas)`
    
    if the optimizer is not attached to the model, the training will fail! **model before optim.**
    
    This is repeatable on multiple runs. only needs <100 epo
    
    It also works with seed values of all 100. (<100 epochs)
    
- ✅ run on more data, with less overlap between train and test
    
    [we see that currently, the code for train, val and test are the SAME dataset!](https://colab.research.google.com/drive/12BELnqZZr-AE5zn_GSbrThOj01lhp2Gc#scrollTo=8trsAnYVwC_l&line=25&uniqifier=1)
    
    - rewrite make_data_gen to split the data of train, val and test such that there's no overlaps
- run on tasks that avoid memorization
    
    Clearly, we cannot have no overlaps. The issue is if there are overlaps, then it's just doing memorization and not generalization.
    
    Perhaps there's tasks (+2, x2) which aren't just memorization. It SHOULD memorize +1 orderings, but not every +2.
    
    Eg) Train data has "2 4 6 8" and "10 11 12 13 14 15 16" but NOT "10 12 14 16". Can it infer this?
    
- like addition, see if it can infer next number using tokens
- list impt current issues
    
    One of the main concerns is that the model is only valid for sequence continuation on small samples of data (eg. there are only 12 months to use, and it doesn’t go past twenty for number words), so there is not enough data
    
    A second concern is that sequence continuation is more "memorization" of what number comes next, rather than generalization. I'm not sure if there's a way we can get around that, unless we do something like train a toy model on sequence continuation and try to apply it to a new case (eg. train on 1 2 3 4 and some 2 4 6, then apply it to never before seen seqs like 10 12 14; or train on some numbers seqs but only number word "one next" (len 2 seqs), then apply to never before seen number word seqs, etc.) That seems sort of arbitrary though
    

[https://transformer-circuits.pub/2023/monosemantic-features#phenomenology-feature-splitting](https://transformer-circuits.pub/2023/monosemantic-features#phenomenology-feature-splitting)

[https://transformer-circuits.pub/2023/may-update/index.html#simple-factorization](https://transformer-circuits.pub/2023/may-update/index.html#simple-factorization)

[https://drive.google.com/drive/u/0/folders/1GgF91n2YNLXJD2KHhHe1WUhXe4zRrqQe](https://drive.google.com/drive/u/0/folders/1GgF91n2YNLXJD2KHhHe1WUhXe4zRrqQe)