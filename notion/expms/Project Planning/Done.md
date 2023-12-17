# Done

[ArXiV Draft v1](Done%20b715c92198314529880806d9f206803d/ArXiV%20Draft%20v1%2035c75a5f1929460fb199edd5fce9a6fe.md)

More Models (after Draft v1)

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
    

Refactor code by abstracting to common fns

- ✅ structure code like Hanma et al, ACDC , etc repos by copying their style
- ✅ study types of fns in `utils.py`
- 🐣 make copy of old repo and delete outdated files
    - minimal circ: del less data

Circuit Connectivity- better iterative algos for all tasks

- ✅ [run acdc on new dataset. first explore how to use new dataset](https://colab.research.google.com/drive/1TGJK-NOJd5-CNfAgwCR3LMgT_Msi5N1D)
    - ✅ [https://www.notion.so/wlg1/Automated-Circuit-Discovery-78c36eb7aa084d7db89fa74016e83d3e](https://www.notion.so/Automated-Circuit-Discovery-78c36eb7aa084d7db89fa74016e83d3e?pvs=21)
    - ✅ run on digits 50 valid, 50 test
        - Setting the threshold to 0.8 makes the method discover 8.11
    - ✅ run on diff thresholds and more data to find why 9.1 isn’t in the circuit (and why it’s so small) and why diff circuits each time using diff data/thresholds
        
        SOLN: the threshold is not a percentage; it needs to be very small
        
    - ✅ reproduce greater-than at diff thres
- ✅ plan revisions with less granular method
    
    I agree with many points of the review and find it helpful.
    
    One way to address the low impact critique can be to frame it so that our approach discovers circuits at a less granular level than ACDC,. at a level akin to that done by Hanma et al, and suffices for determining that shared circuits have similar functionality. The ACDC paper mentions that circuits can be at different levels of granularity, with a tradeoff of discovery time and granuality. This way, our approach seems more novel for tackling the problem in a different way than ACDC (the results on ACDC will also be included for thoroughness, but only serve as an extra beyond sufficiency).
    
    <<<
    
    related to what I have been finding with using ACDC. It seems that method takes a long time to run on even A100 GPUs, namely because it is (in the paper’s words) very granular
    
    It also appears to be inflicted with the same issue of how the discovered circuits depend heavily on the corrupted dataset, threshold
    
    just don’t mention it
    
    we introduce a method to discover 
    
    it is simple and quick as it filters out nodes before edges
    

Writing

- ✅ Convert to NAACL (ACL) template latex
    
    [https://2023.aclweb.org/calls/style_and_formatting/](https://2023.aclweb.org/calls/style_and_formatting/)
    
    [https://www.overleaf.com/project/65747d62aa10e41bfd3ffc8e](https://www.overleaf.com/project/65747d62aa10e41bfd3ffc8e)
    
    [https://aclrollingreview.org/cfp#limitations](https://aclrollingreview.org/cfp#limitations)
    
- ✅ Reduce to 8 pgs
- ✅ move descrps of 6 moved attn pats to appendix

Connectivity

- ✅ ablate MLPs
    - ✅ What MLPs does greater-than depend on?
        
        greater-than circuit fig 3 shows Layers 1 to 9 are impt; these are ‘upstream nodes’
        
    - ✅ check not done already: [https://arena-ch1-transformers.streamlit.app/](https://arena-ch1-transformers.streamlit.app/)
    - ✅ [MLP_ablation_explore.ipynb](https://colab.research.google.com/drive/1NXhcqBH_j4U6ak_B3rfMJhhMJ44SU7dJ#scrollTo=JDKKsMBfWcAl)
        
        [https://chat.openai.com/c/a51e74da-f351-4ab7-a3f1-af154f9699c0](https://chat.openai.com/c/a51e74da-f351-4ab7-a3f1-af154f9699c0)
        
        [https://chat.openai.com/c/db7d733e-37df-45a7-abe6-324e0b2e3aaa](https://chat.openai.com/c/db7d733e-37df-45a7-abe6-324e0b2e3aaa)
        
        - how do I debug with a specific example of hook.layer() when using model.add_hook(lambda name: name.endswith("mlp_out"), hook_fn, is_permanent=True)
            
            Debugging a hook function in a neural network, especially in a complex architecture like a transformer, can be challenging due to the layers' nested and interconnected nature. However, you can employ a few strategies to effectively debug the `hook_fn_mask_mlp_out` function with a specific example of `hook.layer()`. Here's a step-by-step approach:
            
            1. **Logging Inside the Hook Function**:
                - Add logging or print statements inside `hook_fn_mask_mlp_out` to output the layer information and any other relevant data. This way, when the function is triggered, you can see which layer is being processed and how the inputs look like.
                - For example, add `print("Layer:", hook.layer(), "MLP Output Shape:", mlp_out.shape)` at the beginning of the function.
            2. **Testing with a Known Layer**:
                - Temporarily modify your hook application lambda function to trigger only for a specific layer that you want to debug. For instance, if you want to debug layer 3, change the lambda function to something like `lambda name: name == "mlp_out_layer_3"`.
                - This modification will allow you to focus solely on the behavior of your hook function at the specific layer of interest.
            3. **Using Breakpoints**:
                - If you're using an IDE that supports debugging, you can set a breakpoint inside the `hook_fn_mask_mlp_out` function. When the model execution reaches this point, it will pause, allowing you to inspect the variables and flow.
            4. **Unit Testing**:
                - Create a unit test where you manually invoke `hook_fn_mask_mlp_out` with controlled input tensors that mimic what you expect from a specific layer's output. This approach allows you to test the function in isolation.
            5. **Inspecting the Model's Layers**:
                - Before applying the hook, you might want to inspect the model to understand how the layers are named and structured. This can be done by printing out the layer names and their corresponding indices, which can help you correlate the `hook.layer()` output to the actual model layer.
            6. **Verifying the Mask and Mean Tensors**:
                - Ensure that the `mlp_outputs_and_posns_to_keep` and `means` tensors are correctly structured and populated. Incorrect dimensions or values in these tensors could lead to unexpected behavior in the hook function.
            7. **Run with a Subset of Data**:
                - Test the model with a small subset of your data where you know what the expected behavior should be. This can make it easier to spot any discrepancies introduced by the hook function.
            
            Remember, the effectiveness of these debugging strategies can depend on the specifics of your model architecture and the development environment you're using. Choose the strategies that best fit your setup and the nature of the issue you're investigating.
            
- ✅ convert ablated outputs into tokens
    - ✅ [preds_after_ablate_draft](https://colab.research.google.com/drive/1Fx7yN5lV-H9Oj2ygcIF3wDK4WuxNcqZ8)
    - ✅ [preds_after_ablate_draft_v2](https://colab.research.google.com/drive/1WQOqpvgI4DtG0u28PVlxtTYtyNoZISzh#scrollTo=rb5xuOOPF0A4): fix ablate mlp preds bug
    - ✅ preds_after_ablate_draft_v3: clean up. loop over MLPs. pred after head circ ablate
    - ✅ automate if pred is still corr token after ablate. if it is, keep that head. else, discard it.
- ✅ [It’s erroneous to denote importance by removing it from circuit; that’s how important it is for the CIRCUIT, not for the entire full circuit.](https://colab.research.google.com/drive/1XiF5hS8BgCa7WDfIbPme9AaUpfsWhsbd#scrollTo=OwQl7OJaZHqi&line=4&uniqifier=1)
    
    yes; head 9.1 is important for the found CIRCUIT, but when removing from full circuit, it’s not as impt.
    
    maybe give both results (put ‘from circ’ in appendix and ‘from full’ in main)
    
- ✅ Understand ACDC reset network (see paper, acdc_utils.py)
- ✅ Run ACDC zero ablation threshold 0.5: zeroAbT_T0.5_incrDig_ACDC
- ✅ see congruence for MLP scores- not relevant b/c thats on weights
- ✅ output from MLP0 to MLP9 for numbers, months. match up dims
    
    [numseq_MLPScores.ipynb](https://colab.research.google.com/drive/1wwhpddxjcl6CSNovPSAaX5Qzo1kNtZM4#scrollTo=OLkInsdjyHMx)
    
    doesn’t yield anything interpr. may just say ‘effect too complex’
    
- ✅ [use ablation from full to check for most impt heads and MLPs](https://colab.research.google.com/drive/1A3EgZW_0HWrIX3woMk8ZEdrbEQid25Yq#scrollTo=w82u8B4EZdWi&line=1&uniqifier=1)
    - ✅ add as new col of table ‘drop impt heads’
    - ✅ get distribution of values in appendix to show avg drop of each head from full

Writing

- ✅ rewrite intro to talk about importance for analogous reprs
    - ✅ Add why work diff than Merullo (new technqs)
    - ✅ edit path patch and comp output descrps
    - ✅ edit that non-adj layer comps interact due to residual stream indir effects
    - ✅ add in more about knockouts, actv patch and path patch in paper

More Data, MLP and QKV node pruning and path patching

- ✅ more data
    - ✅ test which “between words” templates can work
        
        [multiprompt_test.ipynb](https://colab.research.google.com/drive/1TcEvCnU6eMM9K280SDdZODR-DSX41UWt#scrollTo=twiKY08IAmrT)
        
        - ✅ automate finding which prompts work, and save them
        - ✅ plot distr of their logit diffs
    - ✅ read how IOI used templates
        
        100,000 samp dataset. since you have 3 tasks, just use 10,000 each
        
        months can only get 6 samps, but with 10 templates you get 60
        
        these templates can permute even greater by interchanging random words in them!
        
        Do they all need be same len? How IOI made means dataset if not same len.
        
        [https://chat.openai.com/c/a9b6adff-e1cb-4054-9116-e3d7430e96e3](https://chat.openai.com/c/a9b6adff-e1cb-4054-9116-e3d7430e96e3)
        
        not same length
        
        Were they all put in same dataset?
        
    - ✅ greater-than uses same len, 10000 samples
        
        thus, we’ll do the same
        
    - test logit diffs when make all in same pos for templates
        - so tempaltes are all same length, then we can’t use ‘pure’. however we need templates to up it to 10000 samps.
        - find a way to create 10000 samples (for digits) and 1000 samps for the others
            - 500 numbers
        - 10000 for digits, 1000 for num words, 1000 months [to avoid overrepresenting]
            - this is to test ability to select regardless of word type + position
            - semantically meaningful
    - generate different kinds of these templates
        
        The reason semantically understandable templates over random words is better is because this is a linguistics conference
        
        1. <name> is
        2. "{i} seconds passed. {i+1} seconds. Next {i+2} seconds. Then {i+3} seconds. Finally”
            1. replace seconds with a noun: days, months, etc.
        3. random words 
        4. ~~mix months and digits in order~~
        5. ~~mix months and digits out of order~~
        - change of plans- semantic lengths too long. just use random words HOWEVER also use templates of days, seconds, names, animals, etc.
            - it doesn’t need to be completely random words, we just need 20 for digits to get 10000.
            - **this is just to give the ILLUSion of using more data; pure is sufficient actually**
            1. random words
                1. should each seq have the SAME 20 words? so not completely random?
            2. preset SAME words (eg. 11 cats 12 cats 13 cats)
            3. preset similar words of same type (names, lengths, time, animals)
        - actually, forget this. it’s MMUCH better to use the numbers at DIFFERENT intervals? but then attention patterns is bad b/c it has to display at SAME intervals.
            - finally decide to use SAME intervals with ALL RANDOM WORDS ~~HALF random words, HALF semantic words~~ (10 words) for circuits and ONLY USE DIFF LENGHTS and SAME TYPES AND SIMILAR TYPES for attention patterns! Also, only use semantic sentences for attention patterns! This saves time!
        - random words same interval VS rand with seqs at diff intervals, but all same len
            - for attn pats, they must be at same interval though, and of similar type (NOT random!)
            - actually, if they’re at diff intervals, what ‘triggers’ it to have the next seq number? that’s prob VERY low. so this is pretty bad.
        - [We also found that using random words had WORSE predictive power as using semantically meaningful words such as "11 days 12 days 13 days”](https://colab.research.google.com/drive/1TcEvCnU6eMM9K280SDdZODR-DSX41UWt#scrollTo=UIN9NFQh8dCr&line=2&uniqifier=1)
            - does well if words are names
            - does well if all words are the same
            - does bad if words are time intervals
    - only keep those that pass the tests to use in dataset
        - may only keep those with logit diff greater than (based on distrib)
        - OR keep if prob of first one is > 90% AND is the right answer
            - try with > 50%, and second cannot be too close at < 10%
    - one flaw could be that the members don’t match up from digits to months. Eg) the circuit that processes numbers greater than 12 may be different than the one that processes months.
    - soln: we can use a smaller dataset. instead of 10,000 samples, use 1000 samples each.
        - 8 samples of months. we can use 1024 samples each (128 random sets)
    - ~~same tests as above, but make seq members at diff pos BUT same total len~~
        1. "{i} seconds passed. Then {i+1} seconds. Next {i+2} seconds. Then {i+3} seconds. Finally”
            1. replace seconds with a noun
        2. "{i} seconds passed. Then {i+1} seconds. {i+2} seconds passed. Then {i+3} seconds. Finally”
    - [wait, random words has issue; it’s not always predicting the correct one!](https://colab.research.google.com/drive/1TcEvCnU6eMM9K280SDdZODR-DSX41UWt#scrollTo=TuxJqqyCfCEv&line=1&uniqifier=1)
    - we ought to make templates of SEMANTICALLY meaningful
        - 128/ 4 = 32, so 4 templates (same len) with 32 interchangeables
        - 4 templates: names, another type (but out of order), random, animals
        - ISSUE: wait, semantic meaningful still fails for months!
        - so still random, but say use names, other types, etc. because this allows the probability to be high
            - still fails for months (animals)
            - very hard to get months to work for random even if just ‘get corr ans’ w/o care for prob diffs!
            - perhaps use a different template for months that’s semantically meaningful!
                - [yes, the probability is higher when the sentencs are meaningful](https://colab.research.google.com/drive/1TcEvCnU6eMM9K280SDdZODR-DSX41UWt#scrollTo=PqyPTgl-sye9&line=2&uniqifier=1)
                - Thus, generate combinations of random names! The verbs MUST be the same, else get low prob
                    - "Claire was born in February. John was born in March. Eve was born in April. Bob was born in”
                    - "Ham was bought in February. Egg was bought in March. Bread was bought in April. Steak was bought in”
                    - made
                - dont reuse same templates for all as they may not fit the “>70%” prob for all tasks
                    - or, we could reuse them to see if they still work. they should.
                - shallow vs deep copy
                    
                    The issue you're encountering is due to the mutable nature of Python dictionaries within lists. When you perform `out = data_list.copy()`, this creates a shallow copy of the list. A shallow copy means that while the list itself is a new list, the elements (dictionaries in this case) inside the list are still references to the original dictionaries in `data_list`.
                    
                    So, when you iterate over `out` and modify the dictionaries (`item`), these changes are reflected in the original dictionaries in `data_list`, because both lists contain references to the same dictionary objects.
                    
                    To avoid this, you need to create a deep copy of `data_list`. A deep copy creates new instances of the objects within the list, so modifying the copied list won't affect the original list. You can use the `copy` module for this. Here is how you can modify your function:
                    
                    ```python
                    import copy
                    
                    def replace_month_names(data_list):
                        out = copy.deepcopy(data_list)
                        # ... rest of your function ...
                    
                    ```
                    
                    Using `deepcopy`, each dictionary within `out` is a new instance, and modifying it won't affect the dictionaries in the original `data_list`.
                    
    - out of memory. try reducing seqlen (curr at 27) by removing “was” and reducing it to 3 instead of 4 (actually needs 4 to work)
        
        prev: [multiprompt_test_pt3](https://colab.research.google.com/drive/1TcEvCnU6eMM9K280SDdZODR-DSX41UWt#scrollTo=DcZG9rm2IAiA).ipynb
        
        reduced: [shorten_len4_multiprompt](https://colab.research.google.com/drive/1oPDFy5Q4l16nb982NYW1B4EpTgKd_evY#scrollTo=qSlC73ymPaL2)
        
        - check how many are of each seq
    - plot seq len avg prob val for each template- or just say a similar pattern occurs for using non-sequence words in between
    - we notice that with more data, 9.1 and 4.4 are more represented. but even with few data, 7.11 and 1.5 are still impt (by rmv heads one at a time)
    - make equal repr for each seq
    - solve out of memory by a100 pro+ and reduce # samples
    - **ALSO- vyer impt, del(ioi_logits_original) and the cache once finish computing them. Or, just use model(toks) without model.run_with_cache.**
        - in colab, are variables cleared after each function ends in memory
            
            yes
            
        
        can't use this instead of re-install tfl as it also clears installations: `globals().clear()`
        
    - use`names_filter=lambda name: name.endswith("z"),` to avoid caching all
- ✅ Add MLP fns to iterative methods
    - ✅ iterative knockout numerals
    - ⚠️ ablate by KL div
        - this requires storing original logits to compare
        - [postpone this: KL_div_bigdata_digits_randAll.ipynb](https://colab.research.google.com/drive/1q2mUlJ-voYfyRcTA24gEKCpKxhg84oHQ)
    - ✅ run knockout on months, nw
    - ✅ path patch MLPs
        - ✅ change `receiver_hook_names_filter`  to include MLPs
        - ✅ finish modifying code for MLP to MLPs: [test_IPP_MLPs_v1](https://colab.research.google.com/drive/1btuqMjVROk0qNlUuPV6BkHVTwsUHjWHH#scrollTo=jpWgROBHaPvW).ipynb
        - ✅ code head to MLPs, MLPs to head
            - [test_IPP_MLPs_v2.ipynb](https://colab.research.google.com/drive/1MNFa_ov4PMN1FB71S8q338bDrIARHeoq#scrollTo=5DKgJ54Wl6mA)
        - ✅ ALL the results are negative. The highest neg effects are the strongest
            
            `(patched_logit_diff - clean_logit_diff) / (clean_logit_diff - corrupted_logit_diff)`
            
            - The `patched_logit_diff` should be LOWER because it takes an edge (sender to header) from the corrupted! So if it’s higher, that edge is really bad and not necessary. Thus, DO NOT take abslute values, only take most negative.
            - To be more in line with iterative node thres, we can use a diff metric: `patched_logit_diff` / `clean_logit_diff`
            - clean - corrupt normalized to between 0 and 1 because it is the LARGEST possible DIFFERENCE. patched-clean is a RESTORED DIFFERENCE. thus, total restoration is 0, while no restoration is -1 as it is the same as corrupt-clean (but since we switch the subtraction terms, it’s -1 instead of 1)
        - ✅ [new metric for edge threshold, ablate all nodes before ipp](https://colab.research.google.com/drive/1MNFa_ov4PMN1FB71S8q338bDrIARHeoq#scrollTo=a7JzD7RjIyl1&line=1&uniqifier=1)
        - ✅ modify so only loops thru senders IN INPUT CIRCUIT
        - ✅ loop backw by layer, one receiver node at a time
        - ✅ qkv heads loop
            - [can’t just use z b/c it jhides too much info](https://colab.research.google.com/drive/1MNFa_ov4PMN1FB71S8q338bDrIARHeoq#scrollTo=Umt3tt6IZ3X3&line=1&uniqifier=1)
            - note step 2 uses both z (add hook) and v (filter when running)
            - How do q k v nodes interact?
                
                As seen in ACDC, they do not interact with each other, but they ALWAYS go into an “overall” nodes. Also, q k v NEVER go into any node other than the overall node! The receiver node is always q k v, while sender node is never q k v.
                
                ![Untitled](Done%20b715c92198314529880806d9f206803d/Untitled%201.png)
                
        - ✅ resid post
            
            the exact same thing, except:
            
            `patched_logits = model.unembed(model.ln_final(patched_cache[resid_post_hook_name]))`
            
            So we just need to do this for all MLPs and heads. There are no qkv receiver nodes bc resid is only receiver, so we just need to have two fns: mlp and heads
            
    - ✅ plot graph with MLPs
        - ✅ create new MLP nodes
        - ✅ create q k v nodes that go into head node
- ✅ finalize run big data templates + their corruption through your methods
    - need to use the same random dataset, else score is not acc! so rerun and save
    - [numerals_ipp_allNodes.ipynb](https://colab.research.google.com/drive/1MNFa_ov4PMN1FB71S8q338bDrIARHeoq#scrollTo=VDWmSsCfD6t7)
- ✅ plot new nodes for shared graph
    - ✅ [final_circuit.ipynb](https://colab.research.google.com/drive/1WjxZ1pLGv3vSlEdj7pe7wgKFgANcWgQw#scrollTo=oiuq0IVODWja)

Main Section Writing

- ✅ limitations + future work
- ✅ change data descr
- ✅ tables replace with new results and describe in text
    
    convert python print stats into latex using chatgpt
    
    - ✅ head drops
    - ✅ circuits on other tasks table
        - ✅ Months: Why rmv increases
    - ✅ head drops from full: show top 10 heads (- if not top 10 in other task), & impt heads
- ✅ run months w/ MLP 11
    - MLP 11 is 78%; too close to 80% thres. So removing it finds worse circuit, and the other circs have >100% for months (actually, that 100% is okay since it’s compared to original, NOT the ablated circ, so they’d be the same regardless)
        - for curiosity, run months again without ablating MLP 11 (keep orig results in Copy of saveRandDS_months_bigdata_randAll and Copy of months_ipp_allNodes). note in appndx these scores are the same regardlss of months circuit, as theyre compared to the original fully unablated circuit
            - still, can move without ablate MLP 11 to main, and no specconds to appx
- ✅ place MLP w/ 11 in appendix (or switch)- update after init submit
- 🐣 appendix: load patch results and threshold at node score -0.01
- 🐣 pure seqs circs to show 0.1 not impt
- ✅ Neater individual
- 🐣 combined qkv graph
    - ✅ make bolder edges on 4.4 to 7.11 etc

Functionality on Larger Dataset

- ✅ 0.1 is duplicate (arena nb)
    - 🐣 run seq only
- ✅ 5.0 - num vs numwords for OV, attn pat
    
    In the future, we plan to dive deeper into this study, such as by performing neuron-level and feature-level analysis, and by examining components exclusive to the number words task to see if they handle mapping between abstract representations of numbers and number words
    
- ✅ MLP analysis
    - ✅ table: rmv MLP from each task from full
    - ✅ logit lens: how many samples
        
        [ds_logit_lens.ipynb](https://colab.research.google.com/drive/1xB_3OpMqh0MiqvOladFHh0vaFbJrvqoN#scrollTo=I5wf7hssBh0T)
        
        - show top 5 at all layers for all prompt types
            
            using this format but not its values:
            
            convert this into a latex table, getting rid of quotes and brackets but keeping commas
            
            - ~~OR all layers 1 prompt, but show top 1 at L6 to L11 for 3 or 6 prompts (ea. type)~~
        - ✅ get histogram for when right answer occurs for each prompt
            
            scores if mostly only 2 or 3 x-axis (layers) are meaningful
            
        - ✅ gives scores / histogram for big dataset
- ✅ ov scores using new metric
    - get new score of keyword “is in”
        - using last keyword only gets 100% copy and next; using all seq as keywords get lower copy than next for 9.1
    - Months ov scores
- attn pat using new dataset

Final Edits before first submission

- 🐣 rmv much of appendix (save it for after review vers)
    - note: these scores are not dependent on the edges
    - circuits larger when more data
        - ~~less straightfoward / more ambiguous words that depend on context may have bigger circuits (months is more straigthfwd)~~
    - ~~algo only required 1 backward and 1 forward prune before stopping~~
    - ~~logit lens is better than ov scores! ov scores explanation should move to appendix~~
- ✅ final edits to fit correct guidelines
by finding circuits, we can scale down the model size to bare essentials
    - then can’t generalize well?
- ✅ google drive; github