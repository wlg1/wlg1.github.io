# Project Planning (quests)

[Done](Project%20Planning%20(quests)%203798a71e7c5d4a888cad9a7d25a1275c/Done%20b715c92198314529880806d9f206803d.md)

---

### Working on

Run Llama-2 Circuits for multi-prompts and multi-token answers

- ✅ logit diff for corr answer that uses multiple tokens
    
    [MultTok LogitDiff](MultTok%20LogitDiff%20ff8e7c2c11a6479f8b8edca9f9bb129c.md) 
    
    - we only need to use this for numbers bc nw and months use single tok
- ✅ node ablation algo on 12 prompts numerals, en nw, en months- just run once.
    - ✅ decide on seq len (4) and # prompts (8; bc 4 before ‘12’)
    - ✅ change prompt dict to use all tokens incl spaces
    - ✅ change node_ablation_fns code to use 32 layers, and one backw run only
    - ✅ en nw- doesn’t need to use multitok logit diff nor mt mean replace bc all single toks
        
        Llama2_nw.ipynb
        
        ~3.5 hrs (45 compute units)
        
    - ✅ Llama2_months.ipynb
        
        640-1014
        
- ✅ try ablating by hook then using `model.generate` (note- cannot sum logits or get second highest toks this way, but can observe results)
    
    [test_ablate_then_modelGen.ipynb](https://colab.research.google.com/drive/1q9H9smo0CJzk6wLpzg05_ismXwc-yDac#scrollTo=0luk2rHSRp1n)
    
    This also works for GPT-2, but it fails for llama-2 for some reason: [https://colab.research.google.com/drive/1b6qzlOVuQKwNehyiWEYObKk3v5SRU8Ep#scrollTo=xplS-5FUDhMG&line=1&uniqifier=1](https://colab.research.google.com/drive/1b6qzlOVuQKwNehyiWEYObKk3v5SRU8Ep#scrollTo=xplS-5FUDhMG&line=1&uniqifier=1)
    
- ✅ llama2_ablate_prompts_numwords_circ.ipynb: ablate numwords circ
    
    [llama2_ablate_prompts_numwords_circ](Expm%20Results-%20EMNLP%20df8b503260cf48d987a58d25103b6638/llama2_ablate_prompts_numwords_circ%2013d41c80bbac4bb196f239f5745db7e2.md) 
    
    - think of prompts related to knowing that two comes after one, three comes after two, etc
        
        [https://chatgpt.com/c/8c5d7cb7-03e1-4fa0-8693-b61cca1f7922](https://chatgpt.com/c/8c5d7cb7-03e1-4fa0-8693-b61cca1f7922)
        
- ✅ spanish nw circs: just single tok for now (used for testing)
    - Llama2_spanish_nw
        - ISSUE: spanish numwords AREN’T single token, and can’t cont beyond seis
            - actually, they are single token for uno to seis, so do seqs of 3 (4 prompts)
        - NOTE: quatro and cuatro both work?
        - 1250-3
- ✅ spanish months circs: just single tok for now (used for testing)
    
    ~~spanish months cannot complete until they start from the first month~~
    
    no, they require a lot of words in seq to complete. they require 5 words in initial prompt often, but sometimes even this doesn’t work: “"junio julio agosto septiembre octubre” - this would give “nov”, the english version.
    
    for len 3, this seems to only go up to ‘2’; marzo abril mayo cannot complete corr
    
    for len 4, this doesn’t work
    
    due to this instability, we decide to only go with 2 prompts, noting this section is not as strong, but still provides some weak evidence (put this in appendix)
    
    - spanish number words also require a lot of words in seq to complete; they don’t stop at seis. however, their number words after seis are multi-token.
- ✅ shared seq circs have next heads?
    
    20.17 has a higher than average successor head score, as it is one of only twelve attention heads (out of 1024 total) which detects the "next" token of a sequence member token. However, all the other attention heads with a non-zero successor head score, even those with scores higher than 20.17, are not part of the circuit found for sequence continuation in Llama-2.
    
    - [Llama2_2468](https://colab.research.google.com/drive/1q3awIKao2inD7xbRMDO183JZZddolJfI#scrollTo=susSZdqpqVzd&line=1&uniqifier=1) has none of the [next next heads](https://colab.research.google.com/drive/11mvy5ZZud0Pyr6XYuoPBGpkfo9Hmp4tS#scrollTo=XWH8x6WD4zHX&line=2&uniqifier=1) either
        - (20, 17) not ranked high, but 5.25 is
    - maybe later layer heads not there bc backw run. try fwd run
- ✅ find overlapping circ of nw, months, numbers and ablate this subcirc on prompts
    - ✅ find_circ_overlap.ipynb
    - ✅ ablate this subcirc on prompts: [llama2_ablate_prompts_diff_circs](Expm%20Results-%20EMNLP%20df8b503260cf48d987a58d25103b6638/llama2_ablate_prompts_diff_circs%207fa2537e45b84049b77f3dad6b6f190d.md)
- ✅ Llama2_numerals_1to10.ipynb
- ⚠️ multi tok answer for node ablation
    
    [Llama2_numerals_multiTok](https://colab.research.google.com/drive/1pWgh5WaTRixOA4JwJcoL1PsBfoDyMjs4)
    
    5 prompts (single tok ans), 15 toks (double tok ans)
    
    - ✅ for corr multiToks, print percentage of ablated / unabalted
        - singleTok: mean(ablated_score) / mean(unablated_score)
        - for a batch of prompts, multiTok is also mean(ablated) / mean(unablated)
            - We can mix single and multi: eg. prompt 1 predicts “8” and prompts 2 predicts “10”. Prompt 1 has logit 5, and prompt 2 has logit 6+7. For ablated, prompt 1 has logit 3, prompt 2 has logit 3+4. So (3 + 7 / 2) / (5 + 13 / 2) = 0.56
    - ✅ ISSUE: when answers in dataset take multiple runs to predict, we would have to run the prompt through multiple times because for those whose correct answer is represented as N tokens, we have to do N passes.
        - SOLN: separate prompts with different answer lengths into different datasets. During an iteration of the backwards sweep, run each of these datasets separately. For each dataset with answer tokens of length N, run it N times. Then, [as in the example above](Project%20Planning%20(quests)%203798a71e7c5d4a888cad9a7d25a1275c.md), take the mean of the correct (summed) token(s) logits- regardless of single or N (as this will be compared to the single and N in the unablated) to obtain the ablated and unablated scores. Finally, take their percentage.
            - use the same metric for both (correct tok logit only)
            - report both separate and combined results
            - for 2 4 6 or addition, we **have** to use multi tok. But for 1 2 3, we can get away with just SINGLE.
                - run single tok using logit diff: Llama2_numerals_1to10.ipynb
                - 2 4 6: probably start and end at double toks only for consistency.
    - ✅ corr: if member in clean is single tok, it should be replaced with a single token. Double toks should be replaced with double tok, etc. If it’s a space, keep it. All numwords and months are single tokens, so this is just a problem for numerals
    - ✅ it is okay if the prompts are different lengths because using padding (requires model laoding for some reason) allows them to be put in matrix of same shape
    - ✅ check if `'▁'` will be read same as ‘ ‘ by tokenizer
        - doesn’t matter bc prompt_dict, circuit and seqpostokeep will always use `▁` due to tokenizing the text with `model.tokenizer`
        
    - plan to implement ideas above
        1. ✅ when making corrupted datasets, go through each token of clean prompt and replace it with a random single digit token. since “10” is already broken into single tokens, it can be “54”. we allow numbers greater than 12. 
        2. ✅ create separate datasets based on how many tokens are in correct answer. test this by generate. place these datasets in lists with index corresponding to N.
            - ✅ when CORRUPT: for prompt_dict in list_of_prompts:  # cannot use prompts_list as var, else will get global instead of fn arg (more priority)
        3. in get original score, run the Nth dataset N times and sum up the logits for the N runs. Then take the final summed logit score for these N datasets, and take the mean over the number of samples for ALL datasets.
            - ✅ SCORING CORR ID LOGIT: for each prompt, dataset.corr_tokenIDs needs to store the correct token for not just the next char, but all chars up to the corr ans string. look at shape of this to better understand how to modify this.
                
                ```
                # corr_tokenIDs is list of lists. Each list represents the "next" correct token
                # within each list is the correct tokID for each prompt in the dataset
                # each prompt has an item for the "next" corr token, but this should be a list now that there's multiple
                
                # original with just one ans:
                # eg. [tokenizer.encode(prompt["corr"])[-1] for prompt in prompts_list]
                # [29945, 29953, 29955, 29947, 29929]
                
                # ans_two_dataset
                ```
                
                1. ✅ automate prompts list to check if correct answer in seq is two tokens. but this should use code that recognizes numbers by spaces (split), not by tokens!
                    - split into items sep by spaces, and checks if corr item in list is one or two tokens by splitting
                    - OR split it into two manually (less trustworthy unless llama always does each digit is a token)
                2. ✅ Change `prompt_dict['corr']` to be a list of ans positions
                3. ✅ After changing `prompt_dict['corr']` to be a list, change `self.corr_tokenIDs` to be a list of lists 
                    
                    Outer list lvl 2: [ [ANS_POS_0] , [ANS_POS_1] ]
                    
                    Within list lvl 1: [ PROMPT_1, PROMPT_2, PROMPT_3 ]
                    
                    - ✅ chatgpt prompt (FAILS)
                        
                        before, prompts["corr"] was a single number for each prompt, so we used [self.tokenizer.encode(prompt["corr"])[-1] for prompt in self.prompts] to obtain a list of tokenIDs. Now, prompts["corr"] is a list of numbers for each prompts. Change [self.tokenizer.encode(prompt["corr"])[-1] for prompt in self.prompts] to be a list of lists to match the new change
                        
                        THIS IS WRONG: [tokenizer.encode(corr) for prompt in prompts_list for corr in [prompt["corr"]]]
                        
                        - you have a list of lists where each list is a prompt and the inner lists are their prompt[corr]. we want to invert this. dont invert it after it's made, i want to switch this upon making it
                            
                            THIS IS WRONG: 
                            
                            inverted_prompts_corr = list(map(lambda x: [tokenizer.encode(corr) for corr in x], zip(*[prompt["corr"] for prompt in prompts_list])))
                            print(inverted_prompts_corr)
                            
                    - ✅ Easier to think of this using loop indentation lvls, rather than list compr.
                        
                        ```jsx
                        corr_tokenIDs = []
                        for ansPos in range(len(prompts_list[0]['corr'])):
                            ansPos_corrTokIDS = [] # this is the inner list. each member is a promptID
                            for promptID in range(len(prompts_list)):
                                tokID = tokenizer.encode(prompts_list[promptID]['corr'][ansPos])[2:][0] # 2: to skip padding <s> and ''
                                ansPos_corrTokIDS.append(tokID)
                            corr_tokenIDs.append(ansPos_corrTokIDS)
                        corr_tokenIDs
                        ```
                        
                    - ✅ chatgpt: turn to list compr
                        
                        ```jsx
                        self.corr_tokenIDs = [
                            [
                                self.tokenizer.encode(self.prompts[promptID]['corr'][ansPos])[1:] 
                                for promptID in range(len(self.prompts))
                            ] 
                            for ansPos in range(len(self.prompts[0]['corr']))
                        ]
                        ```
                        
                        The outer loop is the most outer list compr within outer list, and inner loop is within inner list
                        
                4. ✅ `get_logit_diff()` is the only fn that uses `corr_tokenIDs` . For new metric, obtain the tokIDs by `dataset.ansLen`, too. 
                    1. NOTE: you MUST use `logits[range(logits.size(0))`, .. instead of `logits[:, ..`, else you get 15x15 instead of 15x1
                5. ✅ To continue generating, modify`next_token`, which concats onto existing tokens, to take in a batch
                6. ✅ Reshape next_tokens to concat with existing tokens
                    - code
                        
                        ```
                        # Reshape next_token to be a column vector, a 2D tensor with shape (15, 1).
                        next_token_reshaped = next_token.view(-1, 1)
                        
                        # Concatenate along dimension 1 (columns)
                        tokens = torch.cat((tokens, next_token_reshaped), dim=1)
                        ```
                        
                7. ✅ Within each ansLen (for every runID), SUM the logits
                8. ✅ Finally, for each ansLen, CONCAT (since this is how `.mean()` works, not by adding but by batch rows) all samples into one matrix, then use `.mean()` like in `get_logit_diff`
                - ~~ACTUALLY- we don’t need to modify correct token IDs to be a list of lists, nor modify prompt_list’s corr tok IDs, because we can separate out ansLen by dataset! So not within dataset; each dataset has its own ansLen!~~
                    - NO- we still need to separate this out. The dataset with ansLen = 2 must have TWO correct token IDs- one for the first run, the second for the second run.
            - ✅ DO NOT put the “corr token” as the next token- USE THE TOP PRED TOKEN! So you need to decode BOTH the corr token and the top pred token!
            - double check what tokenIDs the seq actually predicts- should be same as in `corr_tokenIDs`
                - ✅ in clean, decode each pred top token (try for one)
                    - `print(f"Sequence so far: {model.to_string(tokens[0, :])!r}")`
                - try for multiple
        4. ✅ in `find_circuit_backw`(), do step 2 for the ablated model in each iteration, and put this over the original score. Print this percentage. Test on 1 ablated run first.
            - ISSUE: when dataset has diff pos, SEQ_POS_TO_KEEP is different for each prompt within a dataset.
                - IOI didnt have this issue bc they were only ablating certain positions, but here we’re ablating EVERY position, but some pos may not be ablated
                - So for now, just have every prompts within a dataset use the same number of tokens. We use `prompts_list = generate_prompts_list(10, 25)`, rather than (6, 21)
            - ablation must be done within
            - ISSUE: mean ablation somehow cannot increment new, so use zero ablation?
            - It might not be working because the sequence circuit doesn’t affect the first token of the 2-digit answer that much. See, in the prompts ablation nbs, it’s often changed from say “14” to “11”- so the first digit is the same.
                - We can test prompts “10 11 12 13 1” instead- giving the first digit
                - In our appendix, we can state we tried the “sum logits of 2 diigts” approach but found this result, so that’s why we go with just predicting the second (or last) digit.
                - HYPOTHESIS: Perhaps the model only pays attention to the LAST digit. test this.
    - ISSUE: this removes 20.17 and other impt heads like 16.0
        
        test zero ablation for 1234 to check if zero ablation is culprit
        
        check if new measure is culprit
        
- ⚠️ single digit fibonacci circ
    
    Llama2_singleDigitFibo.ipynb
    
    - test ANY “add prev 2”, not just starting from 0 1 or 1 1
        - so is it memorizing fibonacci?
        - It can’t do “"3 4 7 11 18 “ (thinks it’s +7) or “"3 4 7 11 “ (think it’s +1)  and can’t do “3 4 7 11 18 29 “. But it CAN do "Find the next member of this sequence: “3 4 7 11 18 29 “. So it needs an instruction prompt beforehand to work.
    - perhaps show that you don’t need a lot of prompts to find these heads; we show just a few prompts is enough to discover improtance which can affect other seqs
- ⚠️ Llama2_036
    
    Llama2_036.ipynb
    
- ✅ HYPOTHESIS: Perhaps the model only pays attention to the LAST digit. test this.
    
    It might not be working because the sequence circuit doesn’t affect the first token of the 2-digit answer that much. See, in the prompts ablation nbs, it’s often changed from say “14” to “11”- so the first digit is the same.
    
    - In our appendix, we can state we tried the “sum logits of 2 diigts” approach but found this result, so that’s why we go with just predicting the second (or last) digit.
    - use QK attention patterns to see what pos it attended to. last digits?
        - Llama2_numerals_attnpats.ipynb
            - 5.25: The last token of a numeral attends to the previous last token
                - Seems to support that just the last digit is attended to, not the whole number?
                    - but then how does fibonacci add entire numbers, or how addition does it?
                        - look at quirke et al
            - 16.0: at space after a number (for just the 2nd member?), it attends to either prev token or the last digit of prev seq member
            - 20.17: at space after a number, it attends to either prev token or the last digit of prev seq member AND to the next seq member’s first di
- ⚠️ debug Multi-Tok issues
    - It might not be working because the sequence circuit doesn’t affect the first token of the 2-digit answer that much. See, in the prompts ablation nbs, it’s often changed from say “14” to “11”- so the first digit is the same.
        - We can test prompts “10 11 12 13 1” instead of giving the first digit. This shouldn’t use multitok code as the ans is 2 toks but
            
            Llama2_promptsGiveFirstDigit
            
            try on 1234 first to ensure it keeps 20.7 etc (before trying on 246)
            
- ✅ ISSUE: even though the logit diff score is the same for clean run vs ablate nothing, why are the logit values different?
    
    Llama2_promptsGiveFirstDigit_draft_v1
    
    [https://colab.research.google.com/drive/1bpK-EHvZ_izbQ8I8P9TYAuUl7OvbfKXj#scrollTo=BHHvz84w70vh](https://colab.research.google.com/drive/1bpK-EHvZ_izbQ8I8P9TYAuUl7OvbfKXj#scrollTo=BHHvz84w70vh)
    
    - HYPOTHESIS: somehow, the differences in logit are the same, but perhaps because a position isn’t ablated, the actual values are different. diff objs, same relns?
        - NO. `logits_original[0, -1, dataset.corr_tokenIDs] - logits_original[0, -1, dataset.incorr_tokenIDs]` should be 8, but the orig_score is 1.6. The difference is `dataset.word_idx["end"]` is 13, but `logits_original.shape[1]` is 15.
            - `tokens = self.tokenizer.tokenize(prompt["text"])
            end_token_index = len(tokens) - 1`
            - `dataset.toks.shape` and `len(tokenizer.tokenize(dataset.prompts[0]["text"]))` are different. toks uses `self.tokenizer(texts, padding=True).input_ids`
            - the culprit is that `tokenizer.tokenize(dataset.prompts[0]["text"])` just puts in one “_” in front, while `tokenizer(texts, padding=True).input_ids` puts in TWO: <s> and ‘’. However, even `tokenizer(texts, padding=False)` won’t get rid of the <s>. Instead, you have to use `dataset.toks[:, 1:]`
            - ISSUE: clean works, but for unablated,
                
                ```
                The size of tensor a (15) must match the size of tensor b (14) at non-singleton dimension 1
                ```
                
            - for now, try instead: **orig score, but logit diff uses last entry**
                - use dataset.toks, not sliced. we see orig score is still diff.
            - if we increase `SEQ_POS_TO_KEEP` to match same entries as dataset.tok, we get keyerror in `means_dataset.word_idx` because our dataset ALSO needs to increase; it shouldn’t use word_idx based on `tokenizer.tokenize(dataset.prompts[0]["text"])`, but it should be based on `tokenizer(texts, padding=True).input_ids`, which adds <s>.
                - So change `tokens` AND `pos_dict` in Dataset when making word_idx, OR change `toks`. Make sure the 4 vars `CIRCUIT, SEQPOSTOKEEP, WORD_IDX AND TOKS` all use the same consistent code together- they should be the same lengths. Here, `toks` is the only outlier that uses `input_ids`, so let’s try changing that first.
                    - note that `tokenizer.tokenize(dataset.prompts[0]["text"])` DOESN’T change into tokenIDs, but as the str repr of those IDs .
                    - But `tokenizer.encode(dataset.prompts[0]["text"])` is the same as `tokenizer(texts, padding=True).input_ids`, except the shape is [15] instead of [1,15]
                    - We could try `dataset.toks[:, 1:]` WITHIN the dataset class. Perhaps this didn’t work before because we passed in dataset.toks[:, 1:] (shape 14), but our mean_dataset still used dataset.toks (shape 15). But we should try to get our dataset and mean_dataset to use the same input this time. We also need to change `max_len` because the means matrix uses this to initialize its shape in `get_heads_actv_mean()`
                        - This fixes the issue.
    - This means that the ablation function is NOT working properly. Check that mask is all 1.
- ✅ run Llama2_promptsGiveFirstDigit after fixing consistent tokenization in diff fns issue
    
    [https://colab.research.google.com/drive/1l0RMob-Cijm5mvQxpQxq0UAU8cRGS44a](https://colab.research.google.com/drive/1l0RMob-Cijm5mvQxpQxq0UAU8cRGS44a)
    
    Summary of changes:
    
    1. Use last token for `logit_diff`, not word_idx(end)
    2. In `Dataset.toks`, take slice of first pos onwards to avoid padding for `input_ids`- [:, 1:]
    3. In Dataset, max len uses: `len(self.tokenizer(prompt["text"]).input_ids[1:])`
    - run on just prompt “10 12 13 14 1”
- 🐣 Try ablating entire attention layers first before narrowing down to attention heads.
    
    This works because if NO heads destroy it, that layer can be removed. But if at least one head destroys it, we search within that layer even more.
    
    - 🐣 first test on GPT2: ablate_attnLayer_thenHeads_GPT2.ipynb
        - ✅ NOTE: you cannot copy+paste colab cells from chrome to firefox, must be within browser
        1. ✅ Mask is to keep components within a layer. instead of keeping anything, DO NOT MASK and just replace z_clean with z_corrupted
            1. In `add_ablation_hook_head` you don’t need `mask_circ_heads`. Instead of using `hook_func_mask_head`, create a new hook_func `hook_func_attnLayer` to directly return `means[hook.layer()]`. 
            2. Call `add_ablation_hook_attnLayer` to compute means and `hook_func_attnLayer` for a specific layer. You don’t need CIRCUIT or SEQPOSKEEP either for any fns.
            3. ACTUALLY you should still use component to keep. This is because we’re not just ablating an entire layer, but all the circuit components removed before we tried testing that layer. 
            4. ACTUALLY we don’t need to change ANY fns at all. Instead, in the loop fns such as `find_circuit_backw`, for CIRCUIT and SEQPOSTOKEEP, we just remove ALL the heads of a layer first. If the score is below threshold, we go through individual heads to see which is the culprit. If it’s above threshold, then all those heads can be safely removed. Write this as `find_circ_backw_attnL_thenHeads`
        2. ✅ Test this on ablate 1, and loop ablated
            1. NOTE: For GPT-2, DO NOT SLICE MAX_LEN OR TOKS because padding is only added for LLAMA2!
        3. 🐣 Compare this circuit to that without using “remove attnL first”
    - 🐣 try this on llama-2: ablate_attnLayer_thenHeads_Llama2
        
        
- 🐣 use changes from “Llama2_promptsGiveFirstDigit”  and “ablate_attnLayer_thenHeads_Llama2” in:
    - ⚠️ singleTok fibonacci
        - ⚠️ still doesn’t work
    - 🐣 multiTok: Llama_2_multiTok_1234
        - with mean ablation
            - ✅ using attnL first: fails on 20.17 when removing L20
            - ✅ using just heads: this also fails on 20.17 when removing L20
            - perhaps it’s the metric (just corr logit) that’s bad. Run again by replacing `correct_logits` with `logit_diff`
                - ✅ remember to change original score to use logit diff too!
                - this ALSO removes 20.17. So it’s not correct_logits, but something else
                - ✅ **SOLN**: probably because MLPs aren’t used (due to not using logit diff before; but now we’ll use logit diff) (also bc need to modify to use new Dataset class which takes corrupted ds, corrTokIDs, etc based on ansLenPos)
                    - strangely, when no MLPs rmv, 20.17 just has 0.05 drop. but with mlps and other heads rmvd, it has 70% drop. perhaps backups were rmvd.
                - ~~could also be because using -1 instead of word_idx[end]~~
        - 🐣 new nb: with zero ablation
- ✅ single digit addition circs
    
    [Llama2_singleTokAddition.ipynb](https://colab.research.google.com/drive/1OBm6nbKvpmJJzVL8efGBYNu7pw_eV26S#scrollTo=4dlDnLnesbfW)
    
    - ✅ WRONG: strangely, unlike seq cont, this doesn’t count the spaces between the digits and operators as tokens. the spaces aren’t even within them.
        - BUT `tokenizer.tokenize("5+4=")` is considered one token
            - Actually, don’t rely on `tokenizer.tokenize.` Use `model.tokenizer.encode`. Then you’ll see it DOES count spaces.
            - That means your dataset and ablation functions should use model.tokenizer.encode() instead, as it’s more accurate to how the model converts input to tokens. Perhaps encode is the same as `tokenizer(prompt["text"]).input_ids`. In a next run new nb, you should modify this to see what happens.
        - SOLN: ACTUALLY ignore the above- those were bc chatgpt made a new tokenizer taht was NOT model.tokenizer, so it repalced it. `encode` is indeed like input_id, it will give an extra padding <s>. But `tokenizer.tokenize` does give the correct number of tokens, so don’t replace it.
    - ✅ in corrupted, you replace the operands with new random ones. the incorrect token is this new one. when making clean_prompts, you need this incorrect, so also make the corrupted operands when making clean_prompts. you can make both clean and corrupted at the same time.
    - ✅ keep on generating until the answers aren’t all mostly 7s and up (the distr will skew to them due to single digit sums mostly having them as answers). save this; don’t re-run!
        - clean
            
            {'corr': '2', 'incorr': '7', 'text': '0 + 2 = ', 'S0': '▁', 'S1': '0', 'S2': '▁+', 'S3': '▁', 'S4': '2', 'S5': '▁=', 'S6': '▁'}
            {'corr': '6', 'incorr': '7', 'text': '6 + 0 = ', 'S0': '▁', 'S1': '6', 'S2': '▁+', 'S3': '▁', 'S4': '0', 'S5': '▁=', 'S6': '▁'}
            {'corr': '9', 'incorr': '5', 'text': '9 + 0 = ', 'S0': '▁', 'S1': '9', 'S2': '▁+', 'S3': '▁', 'S4': '0', 'S5': '▁=', 'S6': '▁'}
            {'corr': '7', 'incorr': '9', 'text': '4 + 3 = ', 'S0': '▁', 'S1': '4', 'S2': '▁+', 'S3': '▁', 'S4': '3', 'S5': '▁=', 'S6': '▁'}
            {'corr': '8', 'incorr': '6', 'text': '5 + 3 = ', 'S0': '▁', 'S1': '5', 'S2': '▁+', 'S3': '▁', 'S4': '3', 'S5': '▁=', 'S6': '▁'}
            {'corr': '8', 'incorr': '6', 'text': '4 + 4 = ', 'S0': '▁', 'S1': '4', 'S2': '▁+', 'S3': '▁', 'S4': '4', 'S5': '▁=', 'S6': '▁'}
            {'corr': '7', 'incorr': '9', 'text': '7 + 0 = ', 'S0': '▁', 'S1': '7', 'S2': '▁+', 'S3': '▁', 'S4': '0', 'S5': '▁=', 'S6': '▁'}
            {'corr': '5', 'incorr': '6', 'text': '5 + 0 = ', 'S0': '▁', 'S1': '5', 'S2': '▁+', 'S3': '▁', 'S4': '0', 'S5': '▁=', 'S6': '▁'}
            {'corr': '4', 'incorr': '9', 'text': '3 + 1 = ', 'S0': '▁', 'S1': '3', 'S2': '▁+', 'S3': '▁', 'S4': '1', 'S5': '▁=', 'S6': '▁'}
            {'corr': '9', 'incorr': '8', 'text': '1 + 8 = ', 'S0': '▁', 'S1': '1', 'S2': '▁+', 'S3': '▁', 'S4': '8', 'S5': '▁=', 'S6': '▁'}
            
        - corrupt
            
            {'corr': '2', 'incorr': '7', 'text': '2 + 5 = ', 'S0': '▁', 'S1': '2', 'S2': '▁+', 'S3': '▁', 'S4': '5', 'S5': '▁=', 'S6': '▁'}
            {'corr': '6', 'incorr': '7', 'text': '0 + 7 = ', 'S0': '▁', 'S1': '0', 'S2': '▁+', 'S3': '▁', 'S4': '7', 'S5': '▁=', 'S6': '▁'}
            {'corr': '9', 'incorr': '5', 'text': '1 + 4 = ', 'S0': '▁', 'S1': '1', 'S2': '▁+', 'S3': '▁', 'S4': '4', 'S5': '▁=', 'S6': '▁'}
            {'corr': '7', 'incorr': '9', 'text': '6 + 3 = ', 'S0': '▁', 'S1': '6', 'S2': '▁+', 'S3': '▁', 'S4': '3', 'S5': '▁=', 'S6': '▁'}
            {'corr': '8', 'incorr': '6', 'text': '5 + 1 = ', 'S0': '▁', 'S1': '5', 'S2': '▁+', 'S3': '▁', 'S4': '1', 'S5': '▁=', 'S6': '▁'}
            {'corr': '8', 'incorr': '6', 'text': '6 + 0 = ', 'S0': '▁', 'S1': '6', 'S2': '▁+', 'S3': '▁', 'S4': '0', 'S5': '▁=', 'S6': '▁'}
            {'corr': '7', 'incorr': '9', 'text': '6 + 3 = ', 'S0': '▁', 'S1': '6', 'S2': '▁+', 'S3': '▁', 'S4': '3', 'S5': '▁=', 'S6': '▁'}
            {'corr': '5', 'incorr': '6', 'text': '3 + 3 = ', 'S0': '▁', 'S1': '3', 'S2': '▁+', 'S3': '▁', 'S4': '3', 'S5': '▁=', 'S6': '▁'}
            {'corr': '4', 'incorr': '9', 'text': '9 + 0 = ', 'S0': '▁', 'S1': '9', 'S2': '▁+', 'S3': '▁', 'S4': '0', 'S5': '▁=', 'S6': '▁'}
            {'corr': '9', 'incorr': '8', 'text': '8 + 0 = ', 'S0': '▁', 'S1': '8', 'S2': '▁+', 'S3': '▁', 'S4': '0', 'S5': '▁=', 'S6': '▁'}
            
        - 10 prompts takes too long, so just use 5
- ✅ single digit multp circs
    - this restricts to 1 to 3, since only 2*4 gets 8. Might as well make your own prompts here
    - test the difference bewteen addition and multiplication by keeping operands, but changing operators to +
- ✅ single prompt 2 4 8 1
    - OR  use (1 2 4)
    - “Find the next member of this sequence: “ improves this
    - try corrupting by 0 2 4 instead
- test new circs on prompts
    
    llama2_ablate_prompts_diff_circs_v2.ipynb
    
    [https://colab.research.google.com/drive/1zqKw-nkX51qh0f-yCZDriejyMfvdyKAW#scrollTo=H3SPe7ulULiu](https://colab.research.google.com/drive/1zqKw-nkX51qh0f-yCZDriejyMfvdyKAW#scrollTo=H3SPe7ulULiu)
    
    - 
    
    - single digit multp circs- does it change 2 4 8? can it change to 246 but adding in addition circ steering?
    - try corrupting 1 2 4 by 0 2 4 instead
    - test ablating by other prompts

---

- measure rankings and what tokens are in the other rankings

- threshold is inaccurate because if an impt component was removed before so that now perf is just above threshold, then a very unimportant component that just reduces by -1 would NOT be removed. but if a diff order- where the unimp component was first- then the unimpt component WOULD be removed. so order and threshold matter a lot.
    - that’s why random is an option- but we cannot just take intersection or most freq then eval perf from that to check if still destroys perf, as that’s not dependent on connectivity?

- issue with removing entire layer: removing some heads may increase performance, so that this offsets the perforamcne destroying when removing individual heads of that layer (their destruction is not enough to offset the favoring when removing entire other heads)

- an issue with just “seeing the result” is that the prediction of them may be very low, and too close to the others
    - same with just using correct logit. we can use any arbitrary incorrect token logit- no, this won’t work if the incorrect is just as low always (meaning corruption won’t make it go higher)

- check if the error is with the code by running the code of Llama2_multitok on single prompt 1234
    - Llama_2_multiTok_1234
- why did sinlge tok fibo and 036 fail by having ablation cause “too much incr” (allowing most heads to be removed?) is it bc single prompt?
- ablate by specific pos to check which pos the component attends to

Multi-Tok issues (uncollapse “plan to implement ideas above”)

- It might not be working because the sequence circuit doesn’t affect the first token of the 2-digit answer that much. See, in the prompts ablation nbs, it’s often changed from say “14” to “11”- so the first digit is the same.
    - In our appendix, we can state we tried the “sum logits of 2 diigts” approach but found this result, so that’s why we go with just predicting the second (or last) digit.
- ISSUE: this removes 20.17 and other impt heads like 16.0
    
    test zero ablation for 1234 to check if zero ablation is culprit
    
    check if new measure is culprit
    
- double check what tokenIDs the seq actually predicts- should be same as in `corr_tokenIDs`
    - ✅ in clean, decode each pred top token (try for one)
        - `print(f"Sequence so far: {model.to_string(tokens[0, :])!r}")`
    - try for multiple

- +2 interval circuit (multikTok)
    - 1 3 5
    - 3 5 7
    - 11 13 15
- read circs of: A Mechanistic Interpretation of Arithmetic Reasoning in Language Models
    - models used
        
        ![Untitled](Project%20Planning%20(quests)%203798a71e7c5d4a888cad9a7d25a1275c/Untitled.png)
        
    
    D:\Documents\_library\__articles\llm interp\math behavior
    
    Shared circuits show a connection between seq cont, greater-than, and arithmetic. Unites these three papers.
    
    [https://github.com/alestolfo/lm-arithmetic](https://github.com/alestolfo/lm-arithmetic)
    
    [https://scholar.google.com/scholar?cites=13180253809186561554&as_sdt=5,31&sciodt=0,31&hl=en](https://scholar.google.com/scholar?cites=13180253809186561554&as_sdt=5,31&sciodt=0,31&hl=en)
    
    [https://aclanthology.org/2023.emnlp-main.435/](https://aclanthology.org/2023.emnlp-main.435/)
    

- automate avg of random runs
- automate prompt testing after ablation
- ablate mlps
- mean ablate

- run circ from 1234 on other tasks to get perf score, not just generate

- Test prompts in a conversation. As the convo goes on, how does the ablated model handle reasoning? What if you TELL it the answer, even after it’s corrupted? Can you correct its wrong knowledge of the sequence order?
    - Can we change the sequence order by telling or editing/steering?

---

To do next

- find llama2 circuits: +2, +3 intervals, +100, multiply, fibonacci
    - dataset size: 20 prompts, len 4 seqs (except fibon)
- multiTok: spanish nw, months circs
- ov scores, logit lens, attn pats

- find all heads which destroys spanish counting

- WHEN does it diverge from addition, multp, to plus 2? Needs instruction though. Try this by ablating circs and generating; this narrows the search to circ subsets instead of all 1024.

Optional small improvements:

- “threshold” in iterative node pruning backws is too confusing.
    - # eg. new_perc is still 30, thres is 20, so "too close to 100”
    - But we should have 80 be threshold, not 20, so we have `(new_perc) > threshold` instead of `(100 - new_perc) < threshold` to decide removal. Easier to reason with when coding and debugging.
        - however, then must change every nb and code in repo showcase
- multi tok logit score: what if high on first tok, low on second tok pred? does it matter?
- new measure of next score: don’t measure top 5, just get the first ranked output
- Instead of taking in the entire corrupted sequence anew each generation, instead add a SINGLE new position to the new corrupted generated position. This allows the clean and corrupted to stay consistent. This is because the tokenizer would have tokens of different lengths for different strings, even if the strings are just “adding onto” previous strings. So the clean and corrupted could have different lengths!
- If just measuring and not logit diff - stop at next space or until corr tok?
- in main, mention appendix has expms for ablating new tokens by 0 or mean?
- ~~clean up “ablate then generate” by re-tokenizing, which should use 0 ablation on the words that have been tokenized as now corrupted won’t correspond to previous words~~

optional, longer implementations:

- whittle down to find all paths for sequence continuation: ablate circuit, and see if it works. If it does, keep on searching for backups to ablate until it doesn’t work anymore.
    - Could it may be distributed throughout the entire thing? If so, we should ablate PART of everything. Possibly using activations differences at every layer.
- circuit for What are the months in a year?
- ONLY ablate CERTAIN tokens in initial prompt
- measure how much sequences generate is corr after it CONTINUES beyond the next member. [Notice sometimes it gets the next correct, but not the othres if it continues.](https://colab.research.google.com/drive/1LPw0da125JQy1qm7nGOFbGwwdO_Fz62M#scrollTo=uemHL8P9uLGk&line=3&uniqifier=1)
    - perf score for multiple tokens: just add up.

double checks:

- for an input where the growing string is diff for each tokenization, (uno cuatro cuatro), compare generating using retokenization vs concat tokens, and compare which one is the same as  `model.generate`.
- zero ablate?
    - how to find what tokens word gets tokenized into in newly concatenated prompt?
    - actually, if we concat tokens, this won’t change what we pass in. So we can still mean ablate. If not, just zero ablate.

[To put in writing](Project%20Planning%20(quests)%203798a71e7c5d4a888cad9a7d25a1275c/To%20put%20in%20writing%20cc3ead9e8f8148068a2cd6d2aff95a3d.md)

---

---

### Future Work

### Future Papers

[Circuit func mapping](Project%20Planning%20(quests)%203798a71e7c5d4a888cad9a7d25a1275c/Circuit%20func%20mapping%20c0805c4b41df47bea39344d637644b00.md)

[Steering](Project%20Planning%20(quests)%203798a71e7c5d4a888cad9a7d25a1275c/Steering%20234ffb7bcb1646309755764449cbe151.md)

[Circular features](Project%20Planning%20(quests)%203798a71e7c5d4a888cad9a7d25a1275c/Circular%20features%2064fe86bffa3648aa808b1b3e991c7275.md)

Feature Steering

- steer at different places than just MLP0
- Logit lens on features
- decompose existing activation vectors on gpt-2 small, try to make them even better
    - improve SAEs to reduce num of dead feature neurons
- decompose steering vectors in analogous seqcont domains
    - find features unique to each domain
    - mean of >2 prompts to get steer vecs for months to numbers

Misc- Much Later

- modularize ablation code even more so it doesn’t rely on unnecc Dataset class properties
    - Look at existing repos of similar papers to find which do it in cleaner ways (not dependent on specific dataset class but more generalizable and adaptable to other data)
    - Make a list of these repos
    - save a list of ‘go-to’ functions when needed (eg. get top logits, etc.) instead of searching for it in a specific repo. make a nb with sections, or notion
        - this is bc a textbook, google, and chatgpt are not tailored to you
- Find ways to get circuits for word problem prompts
    - Instead of logit diff, assess score using another model. Find how much score matches. Score is say how much English is in there.
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

Toy model

More complex sequences with in-context (eg. a1, a3, a2- alternating, etc. See if it can generalize)

both random words + semantically meaningful sequences at unequal intervals

random words at same intervals allows display as attn pat visual; but ablation doesn’t require equal intervals

Eg) He had 1 pencil. Then he had 2 pencils. Afterwards, he got

Ask chatgpt to generate several templates from code

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
    - Find attnpat + OV scores of heads found from [manual adding and checking perf](Expm%20Results-%20NAACL%208de8fe5b943641ec92c4496843189d36/Early%20Head%20Analysis%20b73c8162b7334655ad1ff91fb236b69e.md)
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