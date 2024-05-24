# Project Planning (quests)

[Done](Project%20Planning%20(quests)%203798a71e7c5d4a888cad9a7d25a1275c/Done%20b715c92198314529880806d9f206803d.md)

---

### Working on

Observe Mathematical Reasoning Effects

- ✅ Plan updates
    
    [https://docs.google.com/document/d/1sBKNJ7Xut0kPnFGqRfwn0LqBoiJrgf3_4S3zNevomAQ/edit](https://docs.google.com/document/d/1sBKNJ7Xut0kPnFGqRfwn0LqBoiJrgf3_4S3zNevomAQ/edit)
    
- 🐣 TransformerLens: Get code to generate math reasoning (not just next logit)
    
    [ablate_seqcont_then_math.ipynb](https://colab.research.google.com/drive/1OVMkA1IZKZLmKq2paGRIXykzm5fxrGIx)
    
    - ✅ 🐣 ISSUE: after adding hook, cannot do this:
        
        ```jsx
        for i in range(10):
            print(f"{tokens.shape[-1]+1}th char = {next_char!r}")
            # Define new input sequence, by appending the previously generated token
            tokens = t.cat([tokens, next_token[None, None]], dim=-1)
            # Pass our new sequence through the model, to get new output
            logits = model(tokens)
        ```
        
        `RuntimeError: The size of tensor a (4) must match the size of tensor b (36) at non-singleton dimension 1`
        
        EXPLAIN: This is related to sequence length. The ablation ablates at fixed positions (4), but the tokens passed in have seqlen 36
        
        QUESTION 1: But it takes an input  `'1 2 3'` of length 3 instead of 4?
        
        QUESTION 2: But this code can only take an input of length 2. 
        
        ```jsx
        example_prompt = "1 2"
        example_answer = " 3"
        utils.test_prompt(example_prompt, example_answer, model, prepend_bos=True)
        ```
        
    - ✅ 🐣 ISSUE: after ablating  all heads but not MLPs, ARENA approach to generate tokens yields correct token, but transformerlens approach to predict prompt yields wrong token
        
        DETAILS: This approach seems unaffected by ablation
        
        - code
            
            ```
            reference_text = '1 2 3'
            tokens = model.to_tokens(reference_text).to(device)
            
            print(f"Sequence so far: {model.to_string(tokens)[0]!r}")
            
            for i in range(10):
                print(f"{tokens.shape[-1]+1}th char = {next_char!r}")
                # Define new input sequence, by appending the previously generated token
                # tokens = t.cat([tokens, next_token[None, None]], dim=-1)
                # Pass our new sequence through the model, to get new output
                logits = model(tokens)
                # Get the predicted token at the end of our sequence
                next_token = logits[0, -1].argmax(dim=-1)
                # Decode and print the result
                next_char = model.to_string(next_token)
            ```
            
            ![Untitled](Project%20Planning%20(quests)%203798a71e7c5d4a888cad9a7d25a1275c/Untitled.png)
            
        
        But this approach does seem affected
        
        - code
            
            ```jsx
            example_prompt = "1 2"
            example_answer = " 3"
            utils.test_prompt(example_prompt, example_answer, model, prepend_bos=True)
            ```
            
            ![Untitled](Project%20Planning%20(quests)%203798a71e7c5d4a888cad9a7d25a1275c/Untitled%201.png)
            
        
        We check this by resetting hooks and looking at difference. The first is unchagned after reset hooks, but the second gets the correct next token as ‘3’
        
        TRY: check if logits of ARENA appraoch truly do match before and after ablating all components
        
        RESULT: the logits don’t match before and after ablate
        
        HYPOTHESIZE: the ablation DOES work, but ‘1 2 3’ still is strong enough to get ‘4’ due to the MLPs, just the ranking is much lower. But ‘1 2’, with less, is not enough. We would need to figure out the issue above with why it can only take prompts of a certain length after hook ablation to compare ‘1 2 3’ using both ARENA and TL approaches
        
    - ✅ 🐣 Go back to “[ISSUE: after adding hook](Project%20Planning%20(quests)%203798a71e7c5d4a888cad9a7d25a1275c.md),” and study how ablation code works to find 1) why prompts of different lengths cannot be put in, 2) why is it not len 4 prompts that are allowed, but ARENA approach is len 3 and TL utils example prompt is len 2
        - ✅ Comment ablation functions
        - ✅ 🐣 Look at traceback error to find where in ablation functions error occurs
            
            ```jsx
            <ipython-input-51-36366ada469c> in hook_func_mask_head(z, hook, components_to_keep, means)
                 63     '''
                 64     mask_for_this_layer = components_to_keep[hook.layer()].unsqueeze(-1).to(z.device)
            ---> 65     z = t.where(mask_for_this_layer, z, means[hook.layer()])
                 66 
                 67     return z
            
            RuntimeError: The size of tensor a (4) must match the size of tensor b (5) at non-singleton dimension 1
            ```
            
            - how does this work in detail:
            `z = t.where(mask_for_this_layer, z, means[hook.layer()])`
                
                ### Components of the Line
                
                1. **`t.where(condition, x, y)`**:
                    - This is a PyTorch function that returns a tensor of elements selected from either `x` or `y`, depending on the `condition`.
                    - For each element in the `condition` tensor:
                        - If the condition is `True`, the corresponding element from `x` is taken.
                        - If the condition is `False`, the corresponding element from `y` is taken.
                2. **`mask_for_this_layer`**:
                    - This is a boolean tensor of shape `(batch, seq, head, 1)`.
                    - It indicates which elements of `z` should be kept (`True`) and which should be replaced (`False`).
                3. **`z`**:
                    - This is a tensor of ORIGINAL activations from the model, with shape `(batch, seq, head, d_head)`.
                    - It represents the output of the current layer's attention heads **before modification.**
                4. **`means[hook.layer()]`**:
                    - This is a tensor of the mean activations for the current layer, with the same shape as `z` but excluding the batch dimension, so it must be broadcastable to `(batch, seq, head, d_head)`.
                    - It represents the average activations that should be used to replace the original activations where the mask is `False`.
                
                ### What Happens in Detail
                
                1. **Broadcasting**:
                    - The `means[hook.layer()]` tensor, which has shape `(batch, seq, head, d_head)`, is broadcast to match the shape of `z`. Broadcasting in PyTorch automatically expands the smaller tensor along its dimensions to match the larger tensor's shape.
                2. **Condition Evaluation**:
                    - The `t.where` function evaluates the `mask_for_this_layer` condition for each element in the tensor.
                    - This mask indicates which elements of `z` should remain unchanged (`True`) and which should be replaced with the corresponding element from `means[hook.layer()]` (`False`).
                3. **Element-wise Selection**:
                    - For each element in `z`:
                        - If the corresponding element in `mask_for_this_layer` is `True`, the element from `z` is kept.
                        - If the corresponding element in `mask_for_this_layer` is `False`, the element from `means[hook.layer()]` is used instead.
                
                ### Example
                
                Let's consider an example to illustrate the process. Suppose we have:
                
                - `z` is a tensor with shape `(2, 3, 4, 5)` representing the activations.
                - `mask_for_this_layer` is a boolean tensor with shape `(2, 3, 4, 1)`.
                - `means[hook.layer()]` is a tensor with shape `(2, 3, 4, 5)` representing the mean activations.
                
                ```python
                import torch as t
                
                # Example tensors
                z = t.randn(2, 3, 4, 5)
                mask_for_this_layer = t.tensor([
                    [[[True], [False], [True], [False]],
                     [[True], [True], [False], [False]],
                     [[False], [True], [True], [False]]],
                
                    [[[False], [False], [True], [True]],
                     [[True], [False], [False], [True]],
                     [[True], [True], [True], [False]]]
                ])
                means_for_layer = t.zeros(2, 3, 4, 5)  # Example mean activations tensor
                
                # Applying t.where
                result = t.where(mask_for_this_layer, z, means_for_layer)
                
                ```
                
                In this example:
                
                - The `result` tensor will have elements from `z` where `mask_for_this_layer` is `True` and elements from `means_for_layer` where `mask_for_this_layer` is `False`.
                
                ### Summary
                
                The line `z = t.where(mask_for_this_layer, z, means[hook.layer()])` effectively replaces certain activations in `z` with their mean values from `means[hook.layer()]`, based on the boolean mask `mask_for_this_layer`. This allows selective modification of the model's activations, preserving important components and replacing the rest with a baseline value.
                
            - z is the ORIGINAL activations obtained by passing `tokens` through the model. The hook function gets z at run-time, so not a variable within the function. `means` is obtained by running the means dataset through the model, so its number of tokens per prompt must match the current len of  `tokens`
            - what is a referring to and what is b refeerring to
                - `a` refers to `z`
                - `b` refers to `means[hook.layer()]`
        - ✅ compare number of tokens in dataset (used to ablate) vs tokens that pass in from ARENA approach to generate text
            
            ![Untitled](Project%20Planning%20(quests)%203798a71e7c5d4a888cad9a7d25a1275c/Untitled%202.png)
            
            `model.to_tokens()` adds on a space in front
            
        - ✅ compare number of tokens that pass in from ARENA approach to generate text vs tokens used by `utils.test_prompt()`
            
            SOLN: `util.test_prompt()` used `prepend_bos=True`, so it only took in len 2. But now, is the same as ARENA approach when using `prepend_bos=False`
            
            ```
            example_prompt = "1 2 3"
            example_answer = " 3"
            utils.test_prompt(example_prompt, example_answer, model, prepend_bos=False)
            ```
            
        - ✅ how do I use this without appending an end text token at the front:
        `tokens = model.to_tokens(reference_text).to(device)`
            - ✅ how to get rid of first entry here: tensor([[50256,    16,   362,   513,   604]])
                
                `tokens_trimmed = tokens[:, 1:]`
                
            
            Actual SOLN: [https://www.notion.so/wlg1/Project-Planning-3798a71e7c5d4a888cad9a7d25a1275c?pvs=4#403a22e3d6e74102aebd69f83f5d721b](Project%20Planning%20(quests)%203798a71e7c5d4a888cad9a7d25a1275c.md)
            
        - ✅ Fixed bug `ablated_model =...` as this doesn’t modify model, so model.reset_hooks() also does nothing. Chnage to `model=...`
        - `get_MLPs_actv_mean()` means error: `means = t.zeros(size=(n_layers, batch, seq_len, d_model), device=model.cfg.device)`, then when using `means[layer, template_group] = mlp_output_means_for_this_template`, this broadcasts the mean to every batch. But when have only one batch,
    - ✅ **ablate head 9.1 and mlp 9 and see if corr**
        
        This is necessary (AND) beacuse is seeing if components are essential (no backups)
        
        RESULT: this destroys the ability of ‘1 2 3 4’ to predict ‘5’, and it instead predicts ‘4’
        
    - ablate head 9.1 and mlp 9 then generate longer outputs for math-word-problem inputs
        - ISSUE: in curr code, when a model has a hook, can only take inputs of a certain size (same as means dataset), so cannot ‘add new token on then get next token’ when gen output longer than 1 next pos
            - [Try: ablation not dependent on means_dataset seqlen, but on curr input’s seqlen](https://colab.research.google.com/drive/1OVMkA1IZKZLmKq2paGRIXykzm5fxrGIx#scrollTo=ecUNF1uRd7hk&line=1&uniqifier=1)
                - Go back to [this issue](Project%20Planning%20(quests)%203798a71e7c5d4a888cad9a7d25a1275c.md)
                - proposed soln
                    
                    Instead of making means shape be `n_layers, batch, seq_len, d_model`, using seq_len from means dataset, we should create a means for the specific current input. That means using a new means dataset based on the current input len. (Eg. if "1 2 3 4 5 6", make new means dataset that's len 6). This is needed since we need to get a means value for each pos of the input.
                    
                    Thus, define and pass in new dataset, and change this: `batch, seq_len = len(means_dataset), means_dataset.max_len`
                    
                    Then add a NEW HOOK using new dataset. So if generating, need to do this every loop
                    
                    Alt, use zero ablation
                    
        - [https://www.notion.so/wlg1/Project-Planning-3798a71e7c5d4a888cad9a7d25a1275c?pvs=4#dee8ff214d014d88b06898cc7f073014](Project%20Planning%20(quests)%203798a71e7c5d4a888cad9a7d25a1275c.md)
    - ✅ even if not more than one step, we need to ablate components based on new input lengths. this is just needing new `means_dataset` inputs for each input
        - ✅ ISSUE:
            
            ![Untitled](Project%20Planning%20(quests)%203798a71e7c5d4a888cad9a7d25a1275c/Untitled%203.png)
            
            - ✅ If we trace this back to how `means` is constructed, we see that its pos is determined by:
                
                `batch, seq_len = len(means_dataset), means_dataset.max_len`
                
                But `dataset_2.max_len = 12`, not 13. So it’s something else.
                
            - Place function in colab, and pdb in it (cannot do this if get code from repo)
                
                ipdb> means.shape
                torch.Size([12, 1, 12, 12, 64]) 
                
                `# n_layers, batch, seq_len, n_heads, d_head`
                
                ipdb> means[0].shape  `# same as hook.layer() = 0`
                torch.Size([1, 12, 12, 64])
                
                `z: Float[Tensor, "batch seq head d_head"],`
                
                “at dimension 1” means at seq. But it looks like for all layers, means dim 1 is 12. 
                
                <<<
                
                `print(hook.layer())
                print(z.shape)
                print(means[hook.layer()].shape)`
                
                0
                torch.Size([1, 13, 12, 64])
                torch.Size([1, 12, 12, 64])
                
                So it’s z that has 13, so chatgpt got this wrong by saying “a” is z. Not questioning this wrong assumption led to not finding the issue.
                
                SOLN: `tokens = tokens[:, 1:]`
                
    - ✅ get new dataset_2 to mean ablate. What did pos_dict do?
        
        pos_dict isn’t used to get means. `get_heads_actv_mean()` runs `means_dataset.toks.long()` as input to get a `means_cache` , which has activations for every layer
        
        `means_dataset.toks` is from: 
        
        ```
        self.toks = torch.Tensor(self.tokenizer(texts, padding=True).input_ids).type(
                    torch.int
                )
        ```
        
        Notice your dataset_2 DIDN’T corrupt the input “Today is…” but was the same. So make sure your corr prompts_list in its [’text’] key uses a corr vers with same len as clean input
        
        - ✅ [Manage to](https://colab.research.google.com/drive/1OVMkA1IZKZLmKq2paGRIXykzm5fxrGIx#scrollTo=ubcTjRDf6ETO&line=20&uniqifier=1) corrupt prompt using:
            
            ![Untitled](Project%20Planning%20(quests)%203798a71e7c5d4a888cad9a7d25a1275c/Untitled%204.png)
            
            `tokens = tokens[:, 1:]`
            
            ![Untitled](Project%20Planning%20(quests)%203798a71e7c5d4a888cad9a7d25a1275c/Untitled%205.png)
            
    - ✅ SOLN: how get rid of EOS token in fornt when tokenizing
        
        ```
        # this turns string into LIST OF TOKEN IDS
        tokens = model.to_tokens(reference_text).to(device)
        tokens = tokens[:, 1:] # get rid of prepend bos when using model.to_tokens
        
        # this turns it INTO LIST OF STRINGS WITH SPACE CHAR IN FRONT
        # each string in list correspond to tokens from token id list
        model.tokenizer.tokenize(text) # this doesn't use prepend bos
        ```
        
    - 🐣 [**Mean ablate for model generation**](https://colab.research.google.com/drive/1OVMkA1IZKZLmKq2paGRIXykzm5fxrGIx#scrollTo=SW9uBUML2gc4&line=1&uniqifier=1)
        
        Continues [this](Project%20Planning%20(quests)%203798a71e7c5d4a888cad9a7d25a1275c.md)
        
- ✅ overleaf: update new sections and to-do plan

Steer numbers to ranks of single tokens

- 🐣 Steer numbers to ranks of single tokens using CAA code
    
    analogous_domain_steering_explora.ipynb
    
    - 🐣 check https://github.com/montemac/activation_additions : Uses TL
        - [scripts](https://github.com/montemac/activation_additions/tree/main/scripts)/**addition_clean_reimplementation.py:** [https://chatgpt.com/c/885b4a25-837d-487c-a703-5bd289d23d5a](https://chatgpt.com/c/885b4a25-837d-487c-a703-5bd289d23d5a)
        
        > For example, if we run `gpt2-small` on the prompt "I went to the store because", the residual streams line up as follows:…
        > 
    - ✅ get simplified code to work for 2 prompts for llama-2
    - reproduce past paper results for gpt-2 small and xl
- ✅ [ActivationAddition_explora.ipynb:](https://colab.research.google.com/drive/1MBqXSzO-wUqoAVevWRwqa0KWd_TPwD5h) Explore existing code
    
    Doesn’t work
    
    - first - January
    - ranks - months
- ✅ [Test llama-2: it can do “2 days after Tuesday is”](https://colab.research.google.com/drive/1E-T03wmDOtFiIN44xxqkeStyAncmQnwS#scrollTo=psa8bcKnGBE5&line=2&uniqifier=1)
    
    But it CAN’T do "Three days after Tuesday is”
    
    - 🐣 can it still do this if we corrupt the sequence?

Train SAEs on GPT2 Small [reproduce s.head feature steering]

- ✅ [GPT2_SAE_MLP0_seqcont.ipynb](../Interpreting%20Steering%20Behaviors%20via%20Analogous%20Feat%208e01703d090b40ddbbb9ed25baec5b60/Project%20Planning%20b4b05f73d85e409f8409b209e44ed692.md)
    - ✅ Train it on integers, then see the highest features that light up on mod-10 tokens ending in 3
        
        NOTE: Most important means highest change in output after ablating. But here, we look for highest activations on these tokens. However, this doesn't mean much because certain features may fire highly for all numbers in general! So use the paper's definition of 'most important’
        
    - find most impt feature
        
        To replace feature in LLM
        
        - ✅ replace feature actvs from encoder output, then get decoder output
            - ✅ get feature neuron actvs and ablate a neuron to 0
            - ✅ reconstruct the actvs
                - ✅ see “GPT2small_SAE_train_demo_v1.ipynb” → reconstruction loss
                    - ✅ ISSUE:  Find an alt way to get and alter feature actvs than existing
                        
                        ```
                        output_tuple = autoencoder.forward(post_reshaped)
                        acts = output_tuple[3]
                        ```
                        
                        SOLN: The curernt way to alter uses the code above, but this outputs to the end- the third tuple is actvs, and fourth tuple is outputs. So instead of `autoencoder.forward`, multiply by decoder W and add decoder bias
                        
        - ✅ replace LLM actvs in that layer with decoder output
            - ✅ see: ARENA [1.2] Intro to Mech Interp
            - ✅ see: seqcont_circuits/iter_node_pruning/`mlp_ablation_fns.py` (mult)
            - ✅ NOTE: on using hooks
                
                ```
                # if you use run_with_cache, you need to add_hook before
                # if you use run_with_hooks, you dont need add_hook, just add it in fwd_hooks arg
                ```
                
            - ✅ h_reconstructed `torch.Size([20, 2, 3072])` needs to rearrange
                
                This is the output of two SAEs. We only need one, so `h_reconstructed[:, 0, :]`. Then, we can rearrange it to LLM dims (before, could not do this with two SAEs).
                
        - ✅ find change in output: look at logits after new orig fwd pass after ablating
            - see: ablate_seqcont_then_math__explora.ipynb
            - (to measure su head output) see: allTasks_nextScores.ipynb
        - 🐣 loop thru replacing each feature actvs with corrupted
        - ✅ [https://www.notion.so/wlg1/Repo-Structure-b81c8e1ce00b4bb48ea4e6f1a390c45d?pvs=4#7088e5c4d74f4efdbb521412b2caefb9](https://www.notion.so/Repo-Structure-b81c8e1ce00b4bb48ea4e6f1a390c45d?pvs=21)
        - ✅ Get output after successor heads, not after entire model
            
            NOTE: successor head can turn ‘3’ into ‘4’, but the model itself will turn ‘3’ into ‘.’ if there is no sequence in the prompt.
            
            - ✅ Get OV score code
            - ✅ ISSUE: OV score code uses "blocks.0.hook_resid_post", but SAE was trained on 'blocks.0.mlp.hook_post'
                - ✅ 'blocks.0.mlp.hook_post' vs  "blocks.0.hook_resid_post"
                    - **`blocks.0.mlp.hook_post`**: A hook placed after the MLP in the first transformer block, useful for inspecting/modifying the output of the MLP.
                    - **`blocks.0.hook_resid_post`**: A hook placed after the residual connection in the first transformer block, useful for inspecting/modifying the final output of the block before normalization.
                - ✅ SOLN: Which one of those outputs can be multiplied by OV matrix of an attention head (has the right dims)?
                    
                    Needs input size of : batch_size, seq_len, d_model
                    
                    Given this, **`blocks.0.hook_resid_post`**
                    
                
            - ✅ Re-train SAE on blocks.0.hook_resid_post activations
                
                Unablated: Return ‘4’ if input ‘3’
                
                Ablated: Return ‘third’ if input ‘3’ (ablate feature 0 of SAE)
                
                Interestingly, this “shifts” a number to a rank. Why?
                
            - ✅ save this SAE (much depends on randomness during training)
        - loop thru replacing each feature actvs with corrupted
- ✅ ISSUE: feature activations are all 0, and so decoder bias is broadcast (so the feature ablation of neuron idx 0 did nothing as everything in actvs was already 0). This makes the OV score be “third”
    
    sparsity means most activations should be 0
    
    find which feature neurons (rows) are not all 0s- ablate these
    
    if feature neurons are mostly 0, how can the reconstruction be similar to the original if it just broadcasts the bias? the original didn’t have so many repeats
    
    - perhaps SAE was not trained long enough. Train it on more steps
        - ✅ 5000 steps: same issue, but now broadcasted bias makes succesor head output be “ innumerable”
        - ✅ 10000 steps: sometimes is all 0, sometimes there are 5 VALUES out of 61435 (0.01%) that are non zero (these aren’t counting rows). This predicts ‘must’. **Reconstruction is bad-** because the ablation didn’t do much (first row likely all 0s anyways) it’s the reconstruction that messes up.
            - actually feature coeffs (encoder output actvs) shoudl be a 1D vector?
                - it is 1D, but acts is `[20, 2, 3840]` because of batch*seqlen and # SAE.
- ✅ rename above as “GPT2_SAE_MLP0_seqcont_explora_v1”
- 🐣 [GPT2_SAE_MLP0_seqcont_explora_v2](https://colab.research.google.com/drive/1fxFZynvhH0IkvE2WzUWUAqntQY4h7s5G).ipynb: clean up nb to only reproduce s.head’s “ablate impt feature, then pass thru s.head to see change in logits’
    - ✅ Use bigger SAE (bigger multp factor)
    - ✅ check reconstruction loss; how much reconstruction is similar to original actviation. see if gets same outputs in successor heads and model
    - try to lower reconstruction loss with better training params
        - (Cunningham et al) used small mult factor, R=2, and only 10 epochs?
        - s.heads: Training a sparse auto-encoder withD features and regularization coefficient λ... We used the hyperparameters D = 512 and λ = 0.3, with a batch size of 64, and trained for 100 epochs
- ✅ re-plan emnlp on overleaf + google docs
    
    i just reread the successor head paper and realized they already did do 'transformative mapping between analogous domains'. but they didnt do much with it. i think there's other approaches to try. i guess it's not about knowing the problem to solve, but about the solution that's come up. so just bc multiple rsch groups indp find the same problem doesnt mean anything, what matters is their solution
    
- ✅ explain succssor heads commutative diagram
    
    [https://chatgpt.com/c/e3511349-5a19-4862-8f0b-18ba33dbe477](https://chatgpt.com/c/e3511349-5a19-4862-8f0b-18ba33dbe477)
    
    Ensure that these operations commute, meaning the different paths yield the same results, confirming that the projections πN and πD are correctly learned and that the representations are consistent.
    
    ![Untitled](Project%20Planning%20(quests)%203798a71e7c5d4a888cad9a7d25a1275c/Untitled%206.png)
    

Test prompts

- ✅ Spanish
    
    numseq_prompts, small, pt2.ipynb
    
    small cannot do spanish
    
    But llama-2 CAN do spanish. cannot do german
    
    - usually, BERT models do this (seee “Do Llamas work in English”) but GPT-2 has french
        
        For smaller models, e.g., GPT-2 (Radford et al.,
        2019) and Pythia (Biderman et al., 2023), MI approaches
        such as sparse probing (Gurnee et al.,
        2023) have revealed monosemantic French (Gurnee
        et al., 2023) and German (Quirke et al., 2023) language
        neurons and context-dependent German ngram
        circuits (subnetworks for boosting the probability
        of German n-grams when the monosemantic
        German context neuron is active) (Quirke et al.,
        2023).
        
- ✅ Llama-2 can do interval reasoning
    
    in two days it will be…
    
- ⚠️ Diverging sequence detection
    
    Two inputs sound similar, but diverge at a certain point
    
    unfortunately, llama-2 cant do multiplicative
    
- ✅ llama-2 may be able to do less than
    
    Bob is older than Steve. Bob is 10 and Steve is
    
    Bob is one year older than Steve. Bob is 6 and Steve is
    
    ISSUE: fails on this: Bob is three years older than Steve. If Bob is 6, how old is Steve?
    
- ✅ don’t rely on ‘utils’, use ‘generate next char’ code directly!
    
    utils test prompt is unreliable bc its answers rank changes based on what’s in example_answer!
    
    - prompt_llama2-7b_TLgen.ipynb
        - this works:
            
            ```
            prompt = "Bob is three years older than Steve. If Bob is 6, how old is Steve?"
            output = tl_model.generate(prompt, max_new_tokens=50, **generate_kwargs)
            print(output)
            ```
            
            Bob is three years older than Steve. If Bob is 6, how old is Steve?
            
            Answer: If Bob is 6 years old and Bob is 3 years older than Steve, then Steve is 6 - 3 = 3 years old.</s>
            
- ✅ [List of math reason prompts](List%20of%20math%20reason%20prompts%207fad070b1fa5480e858b6fbef3217c2a.md)

Find Llama-2 circuits for additive vs mult vs fibo seqs

- ✅ run “2 4 6” - all single tokens
    
    Llama2_2468.ipynb
    
- ✅ run “1 2 3”- all single tokens
    
    Llama2_1234.ipynb
    
    - ✅ issue with Llama2_num_runModel_explrTests_v6.ipynb: the prompts go from (1,6), so last samples is “6 7 8 9” and supposed to predict ‘10’ as corr tok but you will get ‘1’. This means not accurate when getting logit diff score. The pos_dict used in dataset is also not matching the seq_pos_to_keep (does it matter?)
    - ✅ Llama2_num_runModel_explrTests_v4.ipynb: this is single samp 12345, but fails
        - useful code
            
            ```jsx
            # logits[:, -1, :] selects the last token for all batches, here batch size is 1
            last_token_logits = logits_original[:, -1, :]
            values, indices = torch.topk(last_token_logits, 5, dim = -1)
            for token_id in indices[0]:
                print(model.tokenizer.decode(token_id.item()))
            ```
            
- ✅ [Successor Heads Notes](Successor%20Heads%20Notes%203d2a9c73e41d4ca7903790b6e7914124.md) : questions on proj mat training
- Llama2_2468: on impt ones, logit lens / ov scores

---

- even if components are different, check if they can be mapped to one another in structure preserving way; see if they have similar features (cosine) or functionality (attn heads, relational patterns, etc). There has to be SOME similarity. If not, check if backups similar to 1234 circuits occur if ablate main heads of 2468 circ. Run 2468 prompts on 1234 circuits (rest are ablated).
- instead of plotting circuits based on high 80% performance level, plot only most essential components based on lower threshold (eg. 50% drop if not all used together)
- Find classes of circuit types. Dispersed, concentrated.
- Iteratively ablate by a path, breadth then depth

- measure the correct answer for multiple tokens
    1. first, we get how long the correct string answer is in terms of token IDs
        1. we use only 1 sequence first, so this is easy
    2. then, we keep on passing in the output autoregressively for the number of tokens the correct answer is. each pass, we measure the logit of the correct token of that pass, taking the difference with the logit of the last sequence member
    3. we add up the logit diffs as an ablation score

---

[https://www.alignmentforum.org/posts/pH6tyhEnngqWAXi9i/eis-xiii-reflections-on-anthropic-s-sae-research-circa-may](https://www.alignmentforum.org/posts/pH6tyhEnngqWAXi9i/eis-xiii-reflections-on-anthropic-s-sae-research-circa-may)

victor veisch (linear repr hypothesis)

- sparse features removal
    
    (A) Removing interpretable but irrelevant features improves performance,
    (B) Keeping only interpretable and relevant features for steering drastically worsens performance,
    
    Doing some set operations, does this mean that it is the set of uninterpretable features that make it work?
    Total features = Uninterpretable + Interpretable(relevant) + Interpretable(irrelevant)
    
    all < interpretable(relevant) + uninterpretable >> interpretable(relevant)
    

teaching clip to 10; is bad at counting

image and text frozen, but bridge Adapter in between is trained, and still find neurons correspond to text concepts (bau)

text-vision end to end is expensive, vision is relevant bc cheaper. is there circuit from text to vision?

sae may fail to find true features. composed, but may try get features in more irreducible. vae men women glasses; train on 3/4 and it can gen to 4th. composability is good to prevent a neuron specific for men glasses and women glasses etc (combos). regualizre repr to be similar.

[https://arxiv.org/abs/1711.00066](https://arxiv.org/abs/1711.00066)

icloud compute a few thousand

they needed uninterpretable for some reason

[https://arxiv.org/pdf/2311.12786](https://arxiv.org/pdf/2311.12786)
fine tune MI

---

Future work

- Find ways to get circuits for word problem prompts
    - Instead of logit diff, assess score using another model. Find how much score matches. Score is say how much English is in there.

Logit lens on features 

[https://arxiv.org/pdf/2404.02431](https://arxiv.org/pdf/2404.02431)

Finding and Controlling Language-Specific Neurons

they didn’t steer features, so we can build on this

[https://arxiv.org/pdf/2403.15491](https://arxiv.org/pdf/2403.15491)

Open Source Conversational LLMs do not know most Spanish words

Circuit Workflow

1. test prompts, generate data
2. auto ablate heads and MLPs to find impt ones
3. on impt ones, logit lens / ov scores
4. on impt ones, attn pats
5. iter edge pruning + viz

---

**Steps towards goal**

Topic 1: features between English - Numbers - ForeignLanguage

MOTIV: this essentially reproduces Gould et al but for a different domain

1. Test prompts to ensure diff models can recognize different language numbers
2. Test prompts to ensure diff models can handle math reasoning
3. Alter English reasoning at certain layer: activation addition for language numbers
4. feature decomposition in small models for actv addition
5. features: differences in language domain vs similarities in index
6. write about its use: understand language repr and abstraction better

Topic 2: small circuits for intervaled sequence continuation  

MOTIV: enhance circuit + feature analysis skills (not about analogies; save that for next paper)

1. test prompts for diff models (may make table)
2. find circuits, and show alter interval-1 can alter interval-2
    1. seqlen circs
    2. letters, spanish numwords and ranks and months
3. alter circuits/features for math reasoning + equation prompts
    1. compare to circs for these word problem + equation prompts
4. possible recognition by features (unlikely, since all is numbers; is good for practice)
5. write about its practical use: diverging circuits
6. OPT: show for multiple models and ablate by diff pos (if nonseq words there)
    1. OPT: larger models: try nnsight

---

[brainstorm emnlp](Project%20Planning%20(quests)%203798a71e7c5d4a888cad9a7d25a1275c/brainstorm%20emnlp%205be09602f7df444d99a8659c5e4be02e.md)

Experimental Details

- For sequences, we only need ONE or a few prompts. Put in appendix circuits found using more prompts; but those are unnecessary. Successor heads does not use that many prompts.
- Don’t worry too much about how it’s corrupted (zero, mean [repeat, random] ), or how it’s measured (metric, which is corr vs incorr token). Just some sort of corruption is all it takes to find IMPORTANT components. We don’t care about exact circuits (b/c we can’t find that anyways regardless of how rigorous our ablation is). Mention in main paper the less rigorous approach; say appendix contains more rigorous approach for smaller model on simpler task due to easier to measure single token answers.
- Don’t worry too much about “what if alt hypothesis” (eg. is it just measuring repeating instead of actual seqs, or is it just memorizing, etc). Address that only if reviewers bring it up; if valid, improve in next paper
- Don’t worry about measuring generated sequences that aren’t just next token. We measure those by human or chatgpt eval, not rigorous score. Only exact answer seqcont (eg. fibonacci) is measured by quant metrics. Then, those circuits are corrupted to obtain effects on word problems. We don’t obtain circuits for word problems.

---

### Future Work

- steer at different places than just MLP0
- decompose existing activation vectors on gpt-2 small, try to make them even better
    - improve SAEs to reduce num of dead feature neurons
- decompose steering vectors in analogous seqcont domains
    - find features unique to each domain
    - mean of >2 prompts to get steer vecs for months to numbers
- modularize ablation code even more so it doesn’t rely on unnecc Dataset class properties
    - Look at existing repos of similar papers to find which do it in cleaner ways (not dependent on specific dataset class but more generalizable and adaptable to other data)
    - Make a list of these repos
    - save a list of ‘go-to’ functions when needed (eg. get top logits, etc.) instead of searching for it in a specific repo. make a nb with sections, or notion
        - this is bc a textbook, google, and chatgpt are not tailored to you

cognitive load problem solving for keeping track of how lines of code across function stacks interact: make a mental and/or external list of items to focus on to avoid being distracted and forgeting key concept/knowledge items to keep around each other

**deep focus like a hackathon- jump from one chunk to another without distraction delays**

check time, APM, speedrun (30-60m intervals; practice)

not always rushing; diff paces for diff stages of problem solving

Much Later

- trace steering effect on component paths + feature paths for math reasoning tasks
- we ablate components and by specific input token positions, so hook is dependent on input

Larger Models

llama2: incr, multp (num), fibo (num) ; letters, gt, decr

- how does ablating seqcont circuits affect fibonacci?
- calc probs based on DQ reponse
- use stronger threshold on sub-circuit to show its edges are stronger than other edges (rare in distribution)
- run on various tasks for llama2
    1. diff intervals (2, 4, 6)
    2. letters,
    3. fibo
    4. decr
    5. gt 
    6. arithm
- Compare heads + MLPs of incr num to Fibonacci
- Rank ALL heads above a threshold (see histogram bins) for `sorted_lh_scores`
- OV scores on the four heads
- Try nnsight
- Check if this llama-2 also uses char lvl tokenization:
    
    [https://colab.research.google.com/drive/1QTuda1ipUrVbzu6WTL4BO3d4ALyY_W5y](https://colab.research.google.com/drive/1QTuda1ipUrVbzu6WTL4BO3d4ALyY_W5y)
    

<<<

[https://drive.google.com/drive/folders/1pXm-TS83EAfS4r3sqtSosx-J67SrnHEK](https://drive.google.com/drive/folders/1pXm-TS83EAfS4r3sqtSosx-J67SrnHEK)

[https://github.com/apartresearch/seqcont_circuits/tree/main](https://github.com/apartresearch/seqcont_circuits/tree/main)

[https://github.com/wlg1/seqcont_circ_expms](https://github.com/wlg1/seqcont_circ_expms)

<<<

- utils, helper
- test
- asserts in fns
- more typing in fns
- make package
- Make classes: model wrapper

- results folder
- change iter node pruning threshold from 20 to 0.8 (convert input to fn var once (1-x)/100)
- del nbs_as_py in apart repo
- move readme details to another file (in readme state “see X file”)
- del revision history by making copy of all and del old ones
- give links to publically shared colab notebooks
- in 1.5, show that for that query (row April), the key March is the HIGHEST it attends to. This isn’t about top values for all, but for each row.
- run hook on local cache to only save the attention heads that are needed (this avoids GPU memory overload)
- use both abs E thres (not below 80%, lower bound) and relative thres (must also be within this much of curernt score)

- OPTIONAL:
    - neuron patch MLP 9 and neuroscope
    - SVD MLPs actvs
    - in our simple graph, we include all edges which are < thres. But we should actually loop thru one at a time to remove and see. In other words, we should ablate that edge and continue! We don’t have time to do this so do this after review.
        - actually, what about leaving it unchanged over bigger? set E thres to be equal to score of orig one. maybe only slightly less. this way, the edge removal order won’t make because that edge that almost no impact!
            - actually no, order will still matter so it won’t mitigate it much. this is b/c just b/c rmving that one node has little impact, the combo of orders may still have impact
        - ALT: instead of aboluste impact, we can use relative impact. this means the removal won’t cause it to go down by more than 0.01 of the existing score, rather than abolute meaning 80%. however, this still doesn’t take combos into account. one edge removal may make it 0.01, and another 0.01, but doesn’t mean their combined effect is also 0.02; it may be more
    - There are multiple circuits where order may matter
    
    - pure seq circuits
        - show original circuits by themselves (no overlap) in appendix
    - split ablating by seq pos vs non-seq pos, and label this in name of nodes
    - actv patch by pos
    - letters, ranks, roman nums
    - appndx- automate rmv heads until 80% of dataset doesn’t have right answer as first. this is a diff metric than pure logit diff (for seq cont)
        - ablation of these heads causes change in all succession
        
        even though there was a large drop in logit diff, the corr answer remained
        
    - all tasks in one dataset
    - try ablation on ACDC circuit
    - both noising and denoising are valid (knockout vs actv patch)
        - knockout vs actv patching
            
            [https://colab.research.google.com/drive/1WtC19bDRJhHphuwj4tuMg9dDguDiz3Yu#scrollTo=6fc8TiqNl6mM&line=22&uniqifier=1](https://colab.research.google.com/drive/1WtC19bDRJhHphuwj4tuMg9dDguDiz3Yu#scrollTo=6fc8TiqNl6mM&line=22&uniqifier=1)
            
            **Second important note** - we've defined this to be 0 when performance is the same as on corrupted input, and 1 when it's the same as on clean input. Why have we done it this way around? The answer is that, in this section, we'll be applying **denoising** rather than **noising** methods. **Denoising** means we start with the corrupted input (i.e. no signal, or negative signal) and patch in with the clean input (i.e. positive signal). This is an important conceptual distinction. When we perform denoising, we're looking for parts of the model which are **sufficient** for the task (e.g. which parts of the model have enough information to recover the correct answer from the corrupted input). Our "null hypothesis" is that a part of the model isn't important, and so changing its value won't get us from corrupted to clean values. On the other hand, **noising** means taking a clean run and patching in with corrupted values, and it tests whether a component is **necessary**. Our "null hypothesis" is that a component isn't important, and so replacing its values with those on the corrupted input won't make the model worse. In this section, we'll be doing denoising (i.e. starting with corrupted values and patching in with clean values). In later sections, we'll be doing noising, and we'll define a new metric function for this.
            
            Although algorithms like activation and path patching generally use noising, it has some problems relative to denoising.
            
            The results of denoising are much stronger, because showing that a component or set of components is sufficient for a task is a big deal. On the other hand, the complexity of transformers and interdependence of components means that noising a model can have unpredictable consequences. If loss goes up when we ablate a component, it doesn't necessarily mean that this component was necessary for the task. As an example, ablating MLP0 in gpt2-small seems to make performance much worse on basically any task (because it acts as a kind of extended embedding; more on this later in these exercises), but it's not doing anything important which is *specfic* for the IOI task.
            
    - ensure random datasets don’t replace the previous seq member with itself (eg. when choosing S1, ensure it’s not the same S1)
    - ablating later heads is not the same as cutting them off because those heads bad actvs will be added back in

---

- FOR AFTER 2/15 ON ARXIV
    
    ✅ Pro+ cancel (then resub to pro after end date)
    
    ~~ahead1.5 similar types logic is wrong for months numbers~~
    
    ✅ 7.11 last token seq, may be ordering
    
    ✅ For most samples of all seq types logit lens
    
    ✅ Fig5 caption
    
    Fig 1 names, 
    
    ✅ logit lens ref date, 
    
    w mlp 11 graph has edge 4.4 to 7.11 error, 
    
    OV: clarify keyword bool is for each one not for all
    
    Get mutlpie circs on avg what is common 
    
    Fix the output of mkp 8pattenr appendix
    
    Ix metric using twice
    
    ✅ Head 0.5 sec 4 should be 5.0
    
    Drop 1.5 only nearly causes more than w0 numwords
    
    ✅ Were are appendix A
    
    Logit lens not always gets last seq member
    
    Attnpat num prompts
    
    Rewrite iter methods
    
    By the additives res
    
    They're not additive as drops don't add to 100
    
    On this sec expm setup
    
    Cite induction in ioi
    
    Export notion git
    
    Gt shares 9.1
    

- set actvs similar to `hook_fn_mask_mlp_out` but NOT as means, but as cache from entirely different run! make sure same sizes. then, see what preds are.

[https://github.com/nrimsky/LM-exp/blob/main/sycophancy/generic_steering.ipynb](https://github.com/nrimsky/LM-exp/blob/main/sycophancy/generic_steering.ipynb)

[https://www.lesswrong.com/posts/raoeNarFYCxxyKAop/modulating-sycophancy-in-an-rlhf-model-via-activation](https://www.lesswrong.com/posts/raoeNarFYCxxyKAop/modulating-sycophancy-in-an-rlhf-model-via-activation)

by averaging the differences in intermediate residual stream activations after a transformer block given paired sycophantic / non-sycophantic texts

Larger models

Toy model

More complex sequences with in-context (eg. a1, a3, a2- alternating, etc. See if it can generalize)

both random words + semantically meaningful sequences at unequal intervals

random words at same intervals allows display as attn pat visual; but ablation doesn’t require equal intervals

Eg) He had 1 pencil. Then he had 2 pencils. Afterwards, he got

Ask chatgpt to generate several templates from code

SAEs, feature ablation

---

Circuit Connectivity

- Ablate neurons, and res stream outputs

Feature ablation:

`!pip install git+`

- [https://www.lesswrong.com/posts/LnHowHgmrMbWtpkxx/intro-to-superposition-and-sparse-autoencoders-colab](https://www.lesswrong.com/posts/LnHowHgmrMbWtpkxx/intro-to-superposition-and-sparse-autoencoders-colab)

[https://transformer-circuits.pub/2023/monosemantic-features#phenomenology-feature-splitting](https://transformer-circuits.pub/2023/monosemantic-features#phenomenology-feature-splitting)

[https://transformer-circuits.pub/2023/may-update/index.html#simple-factorization](https://transformer-circuits.pub/2023/may-update/index.html#simple-factorization)

[https://drive.google.com/drive/u/0/folders/1GgF91n2YNLXJD2KHhHe1WUhXe4zRrqQe](https://drive.google.com/drive/u/0/folders/1GgF91n2YNLXJD2KHhHe1WUhXe4zRrqQe)

Circuit Connectivity- better iterative algos for all tasks

- Improve Pruning Method using ACDC ideas
- Compare curr pruning with others. email about:
    
    Differences in performance after circuit ablation based on:
    
    1) The type of corrupted dataset being used
    
    1.b) The logit difference used
    
    KL div STILL depends on corrupted dataset, but not a specific ‘good vs bad’ logit
    
    2) The order of edge removal
    
    If there were many differences, was it looked into how
    
    - mathwin
    - abhay
    - each indiv author of acdc and attr patch
- Move alternative method to appendix

- first prune by nodes, then by positions, then by edges?
    - by pos: instead of removing from list from all pos, remove from list of ONE pos
        - `resid_pre[:, head, r, c] = 0`
    - put qkv, pos in node of visual
- path patching threshold re-check
    - [Should the negative values be taken?](https://colab.research.google.com/drive/19Le39gsiZOPqEat4VPHWDyU06My8GupZ#scrollTo=fg1gtdoVl6mU&line=2&uniqifier=1)
    - Do head have to conn only to adjacent layer? Review meaning of path patching
        
        [https://chat.openai.com/c/9e2fd95b-a957-4d81-940b-f774f4dd5f7e](https://chat.openai.com/c/9e2fd95b-a957-4d81-940b-f774f4dd5f7e)
        
        residual stream. but don’t explain in detail, just state edges between non-adjacent layers as in previous works (cite ACDC)
        
    - [https://arena-ch1-transformers.streamlit.app/[1.3]_Indirect_Object_Identification](https://arena-ch1-transformers.streamlit.app/%5B1.3%5D_Indirect_Object_Identification)
    Note that we're always measuring performance ***with respect to the correct answers for the IOI dataset, not the ABC dataset***
        - Incorrect token doesn’t need to be the correct answer of ABC; it just needs to be any arbitrary incorrect token (opt- that’s not too far away from IOI). notice ‘corrupted logit diff’ is only used in PP for normalizing. the ‘patching logit diff’ uses the original dataset; it only patches activations
    - Do not remove heads without outgoing. see fig 17 in ACDC; it keeps heads without incoming or outgoing. though all heads are conn. if you see heads without any nodes, you should change the threshold
        - justify this in paper (like ACDC, we do not bc…)
    - double check that the final circ pruned via path patching still has same score via ablation

- Get intersection of all perf and find its perf.
- use among words circuits to get more randomness
- more attn pats
    - try repeated digits or months
    - multiprompt of random among words
    - get induction offset scores and loop thru to find them
- look at the nodes/edges diff between each circuit and try to explain them
- Already have logits after ablation, so just unembed them like in [extract_model](https://colab.research.google.com/drive/1cyW5ZlupQH0VJ6qWcFBkGMbOrDeHWMdD) to get values
    
    rmv what destroys its ability to pred next?
    
    This finds which heads are involved in decreasing. Instead, ends up pred same as last.
    
- make 80% be subcirc of 90% by starting from 90% and then removing more nodes.
- the reason months and numwords is smaller is because of a smaller dataset?
    
    actually this is wrong because we tried 0 to 12 for digits, and it still had a big circuit
    
    test this again on very small digits dataset
    
- Ablate sub-circ on one circuit and check for analogous drop in prediction in another
    - The ablation changes it in an analogous way based on what is predicted. Can we knockout the ability to predict next is we knockout 9.1? Are there backups?
    - Ablate the greater-than sub-circuit in the sequence completion (just delete from “keep circuits” head list). Run tokens through it.
        - which parts of the circuit are the most impt, for what fns? based on logit diff recovery % when ablating them.
    - edit next to prev by replacing actv (see ‘circuits re-use’)
- redo greater-than to use more samples in corrupted dataset
- footnote?: we note this is only one possible circuit for the task, and not the minimal circuit
    - Given that full circuit, we still refer to a subgraph of any size as a circuit.   But we do want to look for minimal circuits, smaller circuits
- corr types (appndx): switchLastTwo, repeatLastTwo, repeatFirstAll, repeatRand, permutation, randAll (only use this one out of the 6)
- we note there are several types of ‘shared circuits’
    - same circuit, similar tokens
    - same sub-circuit, branching components
    - same sub-circuit, components work together in diff ways (incr vs decr at diff lens)
- Patterns that GPT learns from data? Eg) war lasts 20 years
- residaul stream, MLPs in graph fig

[https://colab.research.google.com/drive/1KcODa7naVMJbOvHBGUL_CFxyfmAMM5YI#scrollTo=LkatbMdmp-W2&line=2&uniqifier=1](https://colab.research.google.com/drive/1KcODa7naVMJbOvHBGUL_CFxyfmAMM5YI#scrollTo=LkatbMdmp-W2&line=2&uniqifier=1)

there is an alternative circuit that doesn’t use 9.1 but distributes the computation of next more across other nodes

---

- Circuit Connectivity
    - See how many further heads can be removed to achieve various levels of performance (70%, 80%, etc.).
        - Get circuits with lower performance (to make smaller) to compare and find sub-circuits with greater-than. At what threshold does it lose shared sub-circuits with greater-than?
        - Count the number of heads for 97% perf, Ethres 0.002 after get rid of no outgoing E
            - what is the true perf of circ after get rid of no outgoing E?
        - Venn diagrams for each lvl of performance
        - Top 10 most impt when rmv is inacc bc performance dependent on other heads?
        - Plot perf on x-axis and # heads on y-axis? Table showing what heads differ with each % being row, and cols of Same and Diff from 97%
        - (90 to 80%): However, there are heads not found from before, such as heads 3.2, 4.6, 5.0, 5.11, 6.8, and 8.6. This implies that the order we remove heads may matter. Thus we also try different orders to remove heads, and find how frequently heads appear in the final circuit over all orders. [only matters if don’t find minimal based on thres]
        - Try random order
        - Srange that 25% iter pruning keeps nodes that are not from 2%. Debug by tracking their perf diff in the two runs.
    - re-order circuit diagrams so prev layer heads are further on top.
        - make a table format of layer top bot, head# left right
    - check MLPs for decr circ
        - synergistic of MLP9 with 8.8? get logits for corr answer (not just top) after unembed each component and MLP component
            - what does tuned lens do?
    - how do we track the signal along a path? decr seems to differ how it computes based on seq len, check which components differ (4 to 8 len) but also on which members are in it. get logit lens “when it changes to get corr, if it ever does”, for all numbers 100 to k+1 for certain len k. get proportion
    - diff circuits for diff seq lengths. change seq circ to another seq circ
    - autoablate: mix in 1 dataset diff len random words (see IOI templates)
        - take avg of multiple templates of ‘random words’ in between digits seq. make sure, first, that gpt2-small can recognize these
        - was each template replaced by any other ABC, or just its own ABC?
    - why is pure digits circuit bigger than among words and can’t ablate by pos?
        
        How many extra heads are needed to deal with the noise? Shouldn’t be any more because attention works in parallel in the query weight matrix.
        
        If this is the case, why does among words need LESS heads? Shouldn’t it be the same amount?
        
        similar to among words: number multiple choice task. among words and IOI and color multiple choice all involve searching for and copying (or nexting). 
        
    - not all heads (see IOI) obtain output “from the embedding layer”; name movers in fig don’t. patch from MLP0 to them to check this.
        - [https://arena-ch1-transformers.streamlit.app/[1.3]_Indirect_Object_Identification](https://arena-ch1-transformers.streamlit.app/%5B1.3%5D_Indirect_Object_Identification)
        - perhaps just all nodes without incoming nodes auto have edge to ‘embed’? same with logits. check in ACDC figs
            - NOTE: this is wrong. Fig 17 shows 0.10 not having edge from embed
    - Use fn results to construct QK diagram in visio stating which queries the heads attend from, and which keys they attend to.
    - automate ablate seq pos by brute force. visualize scores?
        - Does ACDC automate ablate by seq pos?
    - automate by filtering via attention pattern first
    - patch by qkv; [see explr nb](https://colab.research.google.com/drive/1swp35sxN_1zNuIW4i4JyhWeY-YUlmUkk#scrollTo=JAbsTRepIAic)
    - what are similar “polysemantic heads” or neurons that are the same but used in VERY DIFFERENT tasks? that is, “polysemantic sub-circuits”.
    - Try alt measures KL div
        - Check if large logit diff coincides with a true difference in correct vs incorrect token logits.
            
            `logits_to_ave_logit_diff_2`
            
            - Debug why mean resampling sometimes gets high scores. Logit diff gets bigger upon removal…?
                - This is explained by “ACDC” paper; so they use KL div instead
    - decreasing months seq
    
    <<<optional:
    
    - Causal trace by entire subcircuit
    - Simulated annealing search and choose smallest circuit with highest perf
    - add input and logit nodes to circuit diagrams
    - Measure the "amount shared". Make a figure which highlights what is shared between the sequence types.
    - Ask slack about difference b/w transformerLens and huggingface for token prediction. first input code to chatgpt to look for difference?
        
        [https://github.com/neelnanda-io/TransformerLens/blob/main/transformer_lens/utils.py](https://github.com/neelnanda-io/TransformerLens/blob/main/transformer_lens/utils.py)
        
    - try different dataset size batches for ablation
    - 2 4 6 8; fibonacci etc on, large, pythia, llama, etc.
    - detect the sequence out of multiple possible numbers. toy model- is there a sequence?
    - try random permutation corruption [issue- doesn’t erase all info]

---

- Circuit Functionality
    - is less-than a subcircuit of decreasing seq?
        - Use incontext learning to get less than
    - Put MLP0 embedding thru MLP
    - [Information movement using corruption on diff tokens/positions](https://www.lesswrong.com/posts/u6KXXmKFbXfWzoAXn/a-circuit-for-python-docstrings-in-a-4-layer-attention-only#Patching_experiments)
        
        When clean patched with corrupted, red means “it got worse”? When corrupted patched with clean, blue means “It got better”???
        
        - [https://colab.research.google.com/drive/1swp35sxN_1zNuIW4i4JyhWeY-YUlmUkk#scrollTo=YzmdOdeJIAiY&line=20&uniqifier=1](https://colab.research.google.com/drive/1swp35sxN_1zNuIW4i4JyhWeY-YUlmUkk#scrollTo=YzmdOdeJIAiY&line=20&uniqifier=1)
        - Corrupt “Adam is 1…” mean ablation using repeated seqs
    - The corruption type used in auto ablation and path patching tells the functionality
        
        eg) If a head influences an induction head (find this via path patching / iterative pruning via ablation), that head may be a prev token head (induction requires prev token head)
        
        - Swap at different positions
        - Or random num at a pos
    - Move most of early heads to appendix if not that impt. Connect it with months, number words, etc. and relate why greater-than needs less early heads than incr digits.
    - Find attnpat + OV scores of heads found from [manual adding and checking perf](Expm%20Results%208de8fe5b943641ec92c4496843189d36/Early%20Head%20Analysis%20b73c8162b7334655ad1ff91fb236b69e.md)
        - [https://colab.research.google.com/drive/16b8SwFckyC7Gv3RPUX8mme_Y8dfw0o1g](https://colab.research.google.com/drive/16b8SwFckyC7Gv3RPUX8mme_Y8dfw0o1g)
    - record how induction is used differently in each circuit
        
        How induction circuits work differently as sub-circuits in not just similar but dissimilar tasks, and what non-shared components differentiate these circuits from one another; IOI and many others already have induction inherently as a sub-circuit.
        
    - the induction patterns are irregular; attneds n-3, then n-7 instead of n-6
        - Try to reproduce ioi results on early
    - OV scores of early layer heads (1.5, 4.4)
    - loop through the output of OV unembeddings (just like SVD) and use GPT-4 to classify each (instead of just finding if copying or not). more than just top 5 tokens
    - attn pat on months/words (put in appendix; state in main they had similar patterns)
    - how to tell if a head is inh or boost another? name movers caused pos logit diff, while s inh caused neg logit diff
        - so dont just measure change in logit diff, but pos or neg on heatmap. Read IOI
    - check which heads’ copy scores are specific for numbers, not just “any type”. use multiple input types to those heads. Note that 7.10, 7.11 and 8.11 aren’t “name mover heads”, though 8.10 was a “s-inh” head
        - IOI small circuit (not found by ACDC) only got 87% score of original logit diff in ‘faithfulness’
    - bigger white line above eve in attn pat viz
    - head 9.1 also has n-3 attn pat. OV scores when pass "is" to 9.1?
    - attn pat and output scores on add2, mult2, for medium
        
        [med_add2Scores.ipynb](https://colab.research.google.com/drive/18pPnSCWCdFKaiiMwBUAbQ_KrLDJ-vNnA#scrollTo=4rTl9Yd0Bcro)
        
        checked the "add 2 scores" of medium and it seems so far there's a couple of heads that are "add 2" heads in gpt-2med. which means we can perhaps find a more general class than just "next sequence" heads. interestingly, no clear "previous seq" heads so far. or rather than "add 2" their top 5 tokens are next members of the input token, some are even previous members. so i'll double check what i said about prev seq heads
        
        I remember someone in the third cohort made a blog post about addition in a toy model. i'll read it and perhaps there may be a connection to its patterns in larger models
        
    - Run tests on non seq number data thru heads to see if they still rec them
    - Early and mid head output scores: Try copy scores on “similar token” early heads to show they’re not looking at pos, but token type. early and late have their own OV sections. a summary of all early to late can be put in appendix
    - test irregular lengths to make sure not just n-2 pos head, but ‘sim type’
        - what makes each head diff from other heads than just “attends to type”?
    - also look for ‘greater-than’ output scores, etc. which means ANY, not just +1.
    
    <<<optional:
    
    - if numwords is too similar to digits, may add another increasing seq task aside from greater-than to compare overlaps
    - Run pruning algorithm on medium, then use embedding method to match with small
    - try other fns: [https://github.com/alan-cooney/CircuitsVis/blob/main/python/Demonstration.ipynb](https://github.com/alan-cooney/CircuitsVis/blob/main/python/Demonstration.ipynb)
    - SVD as perc of (l,h,dir), NOT (l,h). this is bc each dir has its own feature, not (l,h)
    - In svd, don’t just search for “digit” dirs, but “next” or “change” dirs
    - logit lens is supposed to be for all tokens (a table); prev, we only used one col (last token)
    - logit lens of which component?
    - https://github.com/AlignmentResearch/tuned-lens
    - MLP Probing, superposition

---

Predicted criticism:

- search for backup (L10 and 11?), negative heads
- dataset not semantically meaningful
- sequence positions at same intervals (but in pure it would’ve been the same)

### Future Work Ideas / Postponed

- new operations instead of just “next”, modular addition circuits
- [https://arena-ch1-transformers.streamlit.app/%5B1.4%5D_Balanced_Bracket_Classifier](https://arena-ch1-transformers.streamlit.app/%5B1.4%5D_Balanced_Bracket_Classifier)
    - may have something to do with counting. even subject can do ‘counting’. But is counting and number recog the same? perhaps if a meta-model recog them to be the same in a model, that meta-model will develop a link between them
- Make summary video
- Try to find how digits + numwords SEQUENCES (not just individual tokens) change in latent space in each part of residual stream; start with after each layer, then dissect finer to heads + MLPs
    - 1 and One are already close after the first layer. But the sequence 2, 4, 6 and two four six may not be. It may not be considered an “even” dimension (direction).
        - entire input sequences are NOT vectors, but matrices? so how do we measure similarity of sequences if they’re matrices?
            - in a transformer, are input sequences embeeded as vectors, or matrices? would the sequence "2, 4, 6" be a single vector after the first MLP, or would it be a matrix?
                
                In a transformer model, input sequences are embedded as vectors, but the sequence of tokens/words becomes a matrix when considering all the embeddings together.
                
                To break this down:
                
                1. **Token Representation**: Each token or word in the input sequence is represented as an embedding vector. For instance, if your embedding dimension is \(d\), then each token would be represented by a vector of size \(d\).
                2. **Sequence Representation**: If you have a sequence of \(N\) tokens/words, and each token is represented by a vector of dimension \(d\), then the entire sequence is represented as a matrix of size \(N \times d\).
                
                Using your example of the sequence "2, 4, 6":
                
                - Assume that each number (token) is embedded into a vector of size \(d\).
                - "2" would have its own vector of size \(d\). Similarly, "4" and "6" would have their own vectors of the same size.
                - When you stack these vectors vertically to represent the entire sequence, you'll get a matrix of size \(3 \times d\).
                
                After the initial embedding, the transformer's subsequent layers would operate on this matrix, applying multi-head attention, feed-forward neural networks (which you referred to as MLP), etc., to process the sequence.
                
                So, to directly answer your question: The sequence "2, 4, 6" would be represented as a matrix after the embedding layer, where each row of the matrix corresponds to the embedding vector of a number in the sequence.
                
            - how would you measure the similarity between two input sequences?
                
                [https://chat.openai.com/c/b5c12746-f184-4f2b-babe-af1df51d96fc](https://chat.openai.com/c/b5c12746-f184-4f2b-babe-af1df51d96fc)
                
        - is the 2, 4, 6 direction and 8, 10, 12 direction similarity (by cosine sim)?
    - measure the svd similarity between them at each layer
    - each data pt is a series of numbers, but may not be in order. show that ordered seqs have more similarity than non-ordered when dim reduc to 2D along most impt dims
- PCA viz seq types thru layers
    
    To understand how to relate digit activations to wordnum activations, working on PCA visualizations of input sequence types to see how they change by layer (so far, no notable patterns found in visuals). Using this to find if there are directions corresponding to "sequence"- probably "sequence" is not measured this way and this may not exist. Inspired by: [https://www.lesswrong.com/posts/mkbGjzxD8d8XqKHzA/the-singular-value-decompositions-of-transformer-weight](https://www.lesswrong.com/posts/mkbGjzxD8d8XqKHzA/the-singular-value-decompositions-of-transformer-weight)
    
    And paper "Language Models Implement Simple Word2Vec-style"
    
- Edit digit circuit to become number words
    - Replace digit activations with number words activations
    What's the differences? Can this difference be added to edit any digit into months?
    - 9.1, given 'one', will output word 'two'. can we convert 'two' into '2'? measure difference in activations of '1' and 'one' after crucial attnetion head 9.1. is this the 'digit to numwords' direction? when put thru the circuit, what happens?
- Minitially retrain transfer learning toy digits circuit to become months circuit
- do name mover heads attend to anything? if so, why isn’t 19.1 in med attending to anything, even though it should be a “next” head?
- Given that only one head, 9.1, appears to do “next”, can a single layer be trained to do seq completion (though it may require other heads, at 9.1 isn’t enough?) To isolate circuits better, train and study toy models that perform number recognition. See if analogous circuits from toy models are present in larger gpt ones
- Causal Scrubbing
    
    [https://github.com/pranavgade20/causal-verifier](https://github.com/pranavgade20/causal-verifier)
    
    [https://github.com/redwoodresearch/rust_circuit_public](https://github.com/redwoodresearch/rust_circuit_public)
    
    hard to use if don’t know rust
    
    [https://github.com/redwoodresearch/remix_public](https://github.com/redwoodresearch/remix_public)
    
    requires rust
    
    [https://github.com/redwoodresearch/remix_public/blob/master/remix_d4_part1_instructions.md](https://github.com/redwoodresearch/remix_public/blob/master/remix_d4_part1_instructions.md)
    
- How do “next” heads play a role?
    - Test how ablating them…?
        - feed IOI to GPT-2 (cannot have highlights/comments) then ask:
            
            In the Interpretability in the Wild paper, it was found experimentally that heads were performing copying tokens. In a new circuit, we found heads that may be taking in a digit such as “1” and outputting the next digit, such as “2”. How can we test that they are doing this in a circuit which finds the next member of a sequence given a sequence as input?
            
- Understand inputs + outputs of N2G nb
    
    [Neuron2Graph.ipynb](https://www.notion.so/Neuron2Graph-ipynb-1194a0bf97744b3ab86b19fc9d0bbd06?pvs=21) 
    
- cont- ⚠️ gpt2_Neuron2Graph.ipynb
    - use neuron2graph to find more number neurons
- [NOTE: these 'random circuits' may be disconnected; what about testing against "connected" random circuits?]
- read othellogpt world model: [https://www.alignmentforum.org/posts/nmxzr2zsjNtjaHh7x/actually-othello-gpt-has-a-linear-emergent-world](https://www.alignmentforum.org/posts/nmxzr2zsjNtjaHh7x/actually-othello-gpt-has-a-linear-emergent-world)
- figure out how to deal with multi-token words
- max actv examples for attn heads, not just MLP neurons
- see which neurons have the largest difference between how much they write in a chosen direction
- take dot product of neuron output weights with more types of cont seq tokens + prompts (relns between tokens)
- check neuron activation after ablating attention head (zero or mean ablation? try both)
- interpolation of predicted words when changing part of circuit

---