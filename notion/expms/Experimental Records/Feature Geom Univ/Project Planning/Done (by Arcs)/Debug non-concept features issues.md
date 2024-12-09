# Debug non-concept features issues

More pythia models

- ✅ more pythia models: [https://huggingface.co/EleutherAI/sae-pythia-410m-65k](https://huggingface.co/EleutherAI/sae-pythia-410m-65k)
    
    simSAE_pythias_160m_410m
    
    - compare 70m to 410m, and 160m to 410m
    - not every layer pair, just 3: early, mid, late
- ✅ simLLM_pythias_160m_410m.ipynb
    - llm does better than sae
- ✅ SAE_semantic_pythia_160m_410m.ipynb
    - notice there are mlp vs non-mlp; but model card says was trained on mlps?
        - [https://huggingface.co/EleutherAI/sae-pythia-160m-32k/tree/main](https://huggingface.co/EleutherAI/sae-pythia-160m-32k/tree/main)
        - maybe 30k tokens isn’t enough!
- ✅ GUESS: the saes must be of comparable size. 65k is “too fine” than 32k.

Find LLMs can be similar if to many-to-1 (but not for semantic spaces)

- ✅ simLLM_pythias_70m_160m_manyBto1A.ipynb
    - wait; oneAtomanyB has an error, in which the high scores were only high because of:
    
    ```python
        elif ind_B not in seen:  # only keep one if it's over count X
            seen.add(ind_A)
    ```
    
    - but WHY is it high? in fact, it’s high for all layers!!!
        - when this is done, ALL of the manyB are still added. Originally, manyBto1A has 512 indices. ManyAto1B (what’s been used) has 768 indices. With the bug, around 400 out of 512 features are kept. Given that ind_A goes from 0 to 512, each loop will not allow any previous iteration index (if a B from that is chosen) to be selected. What does this mean?
        - Perhaps the manyBto1A is already good; it’s 1-1 that makes it bad
            - yes. seems what was originally happening is using almost the entire non filtered mappings basically
        - [https://chatgpt.com/c/66ed69a6-2ddc-800c-a4d7-338870d07626](https://chatgpt.com/c/66ed69a6-2ddc-800c-a4d7-338870d07626)
            - chatgpt isn’t good
    - another error that was tricky was the display of “unique” was not changed for manyBto1A, so it claimed “ind A” were unique, which should be, but it should’ve been set(indBs). Then it would’ve showed only 30% are unique.
- ✅ LLM_pythia_match_semantic_noFilt.ipynb
    
    just change the loop to use ‘manyto1’
    
    - the pvalues, in comparison to sae, are much higher using 100 rand vals
- ✅ to sum it up so far: it seems LLMs using many to 1 can find similarity on the entire space, while SAEs using 1-1 work better.
    
    for specific semantic spaces, no matter for manyto1 or 1-1, LLMs do not work well. but SAEs for 1-1 do work well
    
- 🐣 histo count many-to-1 LLMs for full space to see why it’s better but 1-1 is worse
    
    [https://colab.research.google.com/drive/1tY5YlSZOwaQ4954NJNQZom0vDpvxjRCE#scrollTo=NkR6OMraZdPQ&line=1&uniqifier=1](https://colab.research.google.com/drive/1tY5YlSZOwaQ4954NJNQZom0vDpvxjRCE#scrollTo=NkR6OMraZdPQ&line=1&uniqifier=1)
    
    - ✅ error in prev corr count code
        
        ```python
        sorted_feat_counts = Counter(highest_correlations_indices_AB).most_common()
        for rankID in range(20):
            feat_ID = sorted_feat_counts[rankID][0]
            print("FeatID: ", feat_ID, "| Count: ", sorted_feat_counts[rankID][1],
                  "| Corr: ", highest_correlations_values_AB[feat_ID])
        ```
        
        `highest_correlations_values_AB` uses the indices from model B (if corr(A,B) ). But feat_ID uses indices from model A (since it’s the VALUES onf corr_inds). This was not noticed before bc SAEs pythia had same number of latents, but LLMs have diff number.
        
        FIX: we have to get one of the Bs, or the avg of them
        
        `feat_A_lst = [ind_A for ind_A, ind_B in enumerate(highest_correlations_indices_AB) if ind_B == feat_ID]`
        
    - ✅ after fixing the corr scores, we see they are higher than avg, but pretty low: 0.48 is highest
    - ✅ for some of the many-1, get a histo of the corr scores
    - ✅ since only a few are above 10 and those high higher corr than avg, try 10-1
        - 10-1 has high pval
    - ✅ only keep Bvals above 10
        - when shuffling, you need num_feats same as numrows of weigth matrices
        - this also has high pval
    - ⚠️ so why are Bvals with both many-1 and 10-1 combined giving high pvals?
    - ✅ fix the shuffling (use old corr vars for num_feats) and re-run noFilt with 100 rands
        - ✅ you must use this code for rand shuff, NOT :len(corrinds), since we’re shuffling the same subset
            
            ```python
            rand_scores = shuffle_rand(num_runs, weight_matrix_np,
                                         weight_matrix_2[highest_correlations_indices_AB], num_feats,
                                        svcca, shapereq_bool=True)
            ```
            
        - while mean of rand is still close and sim of paired is low, pvals are still under 0.05
- 🐣 hypothesis about many-1 LLM:
    - the MEAN svcca for 32k latents will be lower bc there’s more elements
    - however, for LLMs, it will be higher when there’s many-1 skewing it, possibly due to periods, since there’s only 500 to 1k latents.

Match semantic subspaces- fix keyword search issues

- 🐣 match_semantic_spaces_v4.ipynb: duplicates for semantic keyword matches (multiple keywords can have the same feature)
    
    [https://chatgpt.com/c/66ef5e66-e32c-800c-9cf5-d9a45f002341](https://chatgpt.com/c/66ef5e66-e32c-800c-9cf5-d9a45f002341)
    
    - ERROR: not needed bc filt 1-1 already does this
    - however, this prob fixes many-1
- ✅ debug why 1-1 isn’t perfectly unique: in `match_semantic_spaces_v2`, the reason why `filter_corr_pairs` didn’t get 1-1 always is bc it only check if ind_A is in seen(), since before mixed, all ind_B were unique. But now ind_B may not be unique, so multiple ind_B may be added
- ✅ match_semantic_spaces_v4: why is combo numerics low in this but high in v2?
    - the issue is that once it's fixed, the numeric subspace seems worse. need to figure out if there's a bug. for instance if you go to "loop any layer pair: L5", then at L3, the numeric has a high pvalue. This wasn't the case before (the sim was high)
        - so perhaps numeric subspace isn't that good. generate more keywords and think of more categories that are single token to get better matches
    - v2 has 8 extra pairs. do they really make score jump from 0.1 to 0.4? try remove one at a time and getting svcca
        - [https://colab.research.google.com/drive/1-lSRaCl5yZ_R2bvAMhd8eK7BJ-MTST0r#scrollTo=XScaNZu9Vkur&line=2&uniqifier=1](https://colab.research.google.com/drive/1-lSRaCl5yZ_R2bvAMhd8eK7BJ-MTST0r#scrollTo=XScaNZu9Vkur&line=2&uniqifier=1)
    - once you take out the top (16014), the svcca drops from 0.4 to 0.1
    - just don’t use numeric
- ✅ match_semantic_spaces_v4: have chatgpt generate a couple of categories and run them thru
    - 50 words- emotions: only 53 unique
    - [what other categories can you think of that would have MANY keyword matches on data? most data should match them](https://chatgpt.com/c/66e6c3b5-4ff4-800c-bfd5-a57534a30f81)
    - 100 words- time has 614 unique, and a score of 0.56
    - 100 words- biology: bad
- ✅ match_semantic_spaces_v4: record which keywords have at least one feature actv on it
    - [record which keywords have at least one feature actv on it](https://colab.research.google.com/drive/1-lSRaCl5yZ_R2bvAMhd8eK7BJ-MTST0r#scrollTo=rhy3kGMdehHw&line=1&uniqifier=1)
    - count num feats each keyword actvs on
        - bc each feature more monosemantic, expect top 5 won’t have more than 1 keyword
- ✅ match_semantic_spaces_v4:  check if the other feature in matched pair also actvs on same keyword (**IMPT**!)
    
    there's another issue i found with just taking the highest correlation to create the subspace; after interpreting some of them, the other feature in the pair isn't always the same word (eg. feature A activates with "day", but feature B doesn't contain "day"). 
    
- ⚠️ match_semantic_spaces_v5.ipynb: fix approach 2
    
    apporach 1 has false positives (eg. even though activates highest for “day”, the feature B actvs for “day of govt” and is political; its match feature A is also political, and that match isn’t about “Time”)
    
    TRY : narrow down to only features in BOTH models that fire for keywords in concept group
    
    - ✅ prev corr code: are the inds of original features are preserved?
        
        ```python
        subset_inds, subset_vals = batched_correlation(reshaped_activations_A[:, mixed_modA_feats],
                                                       reshaped_activations_B[:, mixed_modB_feats])
        ```
        
        This maps index say 20 from mixed_modA into index 0. However, perhaps when you do this they are preserved:
        
        ```python
        X_subset = weight_matrix_np[mixed_modA_feats]
        Y_subset = weight_matrix_2[mixed_modB_feats]
        
        paired_svcca = svcca(X_subset[subset_inds], Y_subset, "nd")
        paired_svcca
        ```
        
        - [reshaped_activation is tokens x features. weight_matrix is features x latents. mixed_modA_feats is a subset of features in a certain order (eg. 20, 16, etc). does the code below preserve the features when doing svcca; that is, feature 20 is still feature 20?](https://chatgpt.com/c/66f1c22f-6a14-800c-845a-36548638b954)
            
            Yes, if `subset_inds` properly maps the indices of paired features as they relate to `mixed_modA_feats` and `mixed_modB_feats`, the code will preserve the original order of features when performing SVCCA.
            
    - ✅ NOTE: in nb 1, your before filtered approach was right, but after filtered wasn’t
        
        ```python
        paired_score = svcca(weight_matrix_np[filt_corr_ind_A], weight_matrix_2[filt_corr_ind_B], "nd")
        # this is wrong
        ```
        
        This is right:
        
        ```python
        X_subset = weight_matrix_np[mixed_modA_feats]
        Y_subset = weight_matrix_2[mixed_modB_feats]
        
        paired_svcca = svcca(X_subset[filt_corr_ind_A], Y_subset[filt_corr_ind_B], "nd")
        ```
        
        Once you do the right, time svcca jumps from (0.04) (wrong) to 0.52
        
    - ✅ so subset_inds is NOT the feature indices of the original matrix, but of `reshaped_activations_A[:, mixed_modA_feats]`
    - ✅ [instead of needing to use that X_subset code, how to directly map subset_inds back to original feature inds or weight_matrices? subset_inds is a list where indices correspond to the indices of  [mixed_modB_feats] and values are indices of mixed_modA_feats](https://chatgpt.com/c/66f1c22f-6a14-800c-845a-36548638b954)
        
        
    - ⚠️ [by masking what's not mixed_modB_feats and mixed_modA_feats so to preserve original indices?](https://colab.research.google.com/drive/1Nr9nzDbAWUF-EkvZzT3G6GXs4Mw532UD#scrollTo=xyXCanZHguBy&line=1&uniqifier=1)
        
        didn’t get it to work
        
    - ✅ [approach 2 still doesn’t guarantee keywords match, but at least the features are in same ‘concept group’ (even if not exact same keyword). you should still check.](https://colab.research.google.com/drive/1Nr9nzDbAWUF-EkvZzT3G6GXs4Mw532UD#scrollTo=q7MtERsagIdl&line=1&uniqifier=1)
        - check the number with matching keywords
    - ⚠️ match only without spaces (king, son are wrong matches. needs to be WORD ONLY
        - ISSUE: match by == not in
            - the “no space list” of features DOESN’T say if a feature is a single token or not; it could’ve been a part of something else
            - these “king” and “son” actually have low corr
    - ✅ try running after filter out those with corr < 0.2
        
        works well
        
    - ✅ run categories without common non-category specific words like “while” & **(rmv words part of compound)**
        - [https://chatgpt.com/c/66f1dae9-1874-800c-8901-bd6f5365c9fd](https://chatgpt.com/c/66f1dae9-1874-800c-8901-bd6f5365c9fd)
    - ✅ these words you’re using are too generic (eg. sand is part of Sanders)
        - try “distinct, last names of famous people”
            - make sure case insensitive by .lower() on both top tok and keyword
    - ⚠️ match only without spaces (king, son are wrong matches. needs to be WORD ONLY
        - `display_top_sequences` get the fulll word in a seq. after getting seq list, DO NOT REMOVE SPACES. but each member of list is a string that’s a sentence, so SPLIT THAT MEMBER BY SPACES, and loop thru it
        - then check if (after lowercase) if the keyword is EQUAL to a word in this list.
    - ✅ [DEBUG why “people” top dataset samples contains highest tokens (orange) that are not in kewords](https://colab.research.google.com/drive/1Nr9nzDbAWUF-EkvZzT3G6GXs4Mw532UD#scrollTo=YYcpvacEHNsp)
        - SOLN: when you’re splitting surrounding toknes and say if keyword is “in it”, the keyword may be around the actual highest token.
            - 1946 Eddie Bockman 1946 Joe Medwick**”
            - ['man 1946']
            - so keyword “man” is not the highest; 1946 is, but this feature is considered right
            - TRY: in keyword search for top tokens of a feature, use more than surrounding -1 and +1 words, AND denote which is the highest token.
    - ✅ try random keywords to match from that are unrelated to each
        - this will probably work though
- ⚠️ ISSUE: any random subset of feature pairs seems to work.
    - actually, maybe they’re all related bc political
    - must be more seletive about keywords
    - this would throw out the ENTIRE semantic subspace claim about it being better than ‘any random subset’.
- ✅ temp rewrite overleaf to not mention LLMs or semantic subspace until you are more sure about those issues; recenter paper on just showing SAE sim
    - just put SAE results for tinystories and pythia and gemma on full space
- ✅ simLLM_pythias_70m_160m_manyBto1A: run on more layers and more rand runs
    - still pval of 0, though the mean is much lower than saes
- ✅ match_semantic_spaces_v5: fix “find semantic feature” issues
    - ✅ keyword search for top tokens of a feature, use more than surrounding -1 and +1 words,
        - **(use surrounding 5) in `store_top_seqs`**
        - ISSUE: this just makes it so if “king” is 5 tokens away, then that feature is included. so it fixes compound word issues like “brockman” but doesn’t fix main issue!
    - TRY: AND denote which is the highest token.
        - in `store_top_seqs`, we can’t just record the seqs around the highest
            - for compound, surrounding 2 is enough
            - in `store_top_seqs`, only change is to return (seq, seq_idx)
        - then in `find_indices_with_keyword_bySeqs,` given store_top_seqs, do this:
            - perhaps if it has a space in front or not?
            - ✅ [how to check if seq_idx belongs to a larger word or not? for instance, if we want "man", we want to just have "man", not "brockman".](https://chatgpt.com/c/66f33566-1628-800c-9820-a554d7bdbe2b)
                - this doesn’t work
            - ✅ in `store_top_seqs`, return (seq, topTok), where topTok matches seq_idx (this index is meaninless outside of dataset, so it loses meaning in `find_indices_with_keyword_bySeqs` )
                - then in `find_indices_with_keyword_bySeqs`, `if keyword.lower() != topTok:`, you check `if keyword.lower() == word:` for every word in `seq.split(' ')`. if a match, add the feature to output list
                    - remove \\n and other punctuation from word
            - run on:
                - people (fix false pos compound words)
                    - pval is 0.07; so bad
                - animals
                    - only 3 features found. sim is 0.99 so better than mean of 0.3, but is too few features
                - colors
                    - only 4 features found. pval is 0.05
- ✅ match_semantic_spaces_v6: clean up after fixing search, and run on curated concepts
    
    be very selective; make sure word is distinct and not part of compound
    
    - ✅ famous last names issues: disney is also a company
        - manually filter these keywords
        - dont need more categories, just carefully curated ones (at least 3)
    - ✅ famous names
        - ✅ [give the list after filtering out names which have double meanings (eg. lincoln is car brand, jordan is country, bolt is lightening, disney is a compnay, etc) that are not just names of famous people](https://chatgpt.com/c/66f347ad-5850-800c-881a-ca589465ab6d)
        - ✅ the list with kennedy and clinton have no matches. but it SHOULD have those matches; so there is an error. Model A Feature:  29656 should fire for Clinton. So when running for that feature, pdb
            - SOLN: you’re not doing case sensitive right. Famous Names should NOT be lowercased.
            - in general, when case insenstivie, word should ALSO be .lower() to match keyword.lower()
                
                
        - high pval
    - ✅ numbers
        - interpret shows not specific enough; these are not “number” neurons
    - ✅ numeric
        - get rid of double meaning keywords like “even”
        - high pval until we filter out those with corr under 0.4; then low pval. even for 10k random, pval is 0.01
    - ✅ People/roles (filter out double meanings)
        
        paired is 0.5, random is 0.18. P-value for 10k random runs is 0.01.
        
    - ✅ random keywords
        - filtering out 1-1 gives low pval
        - keep in mind this isn’t perfect bc some of these words are related in some way
        - i think 'random keywords' was a false neg bc many of those keywords were related. ALSO we allow “apple” to have two matches- so that’s pretty related
    - ✅ rand sel features from each model, corr, then check
        - bc after 1-1 filter of “same mapping corr” is low, we should start with 100 featuers, get corr, and filter. we want to end up with at least 20 to 50 features after 1-1 corr filtering.
        - better test is to rand sel features of the same size and do 1-1; this obv has a very high pval
    - ✅ nature isn’t good bc a lot of last names use nature (eg. stone)
        
        still it has very low pvals
        
    - ✅ emotions
        
        paired is 0.82, random is 0.15. P-value for 10k random runs is 0.00.
        
    - ✅ unrelated (rand v2): manually select one word from each category
        - before filt corr, we get 0.009 sim. emotions, people, etc are all higher than this. only numerical is 0.04 sim.
        - issue: after filt corr, there are 5, which are 2 ‘apple’, 2 ‘cloud’, and 1 ‘sandwich’
            - this gets a high sim of 0.9
            - but it could be ‘apple’ and ‘sandwich’ and ‘cloud’ are all related (eg. foods, tech)
        - thus, make sure the FINAL interpreted set of values doesn’t contain the SAME keyword activating features multiple times, and are LARGE ENOUGH feature subspace.
    - ✅ unrelated v2: jsut get rid of apple
        - now the sim is still high, but the pval is extremely high after shuffling!
    - ✅ unrelated v3: also get rid of cloud and apple
        - there are barely any matches, only one 1-1. so, it was only those few that had matches.
    - ✅ unrelated v4: select a few keywords from prev catg (num, nature, ppl, emotions)
        - this has high pvalues! so it’s not just any semantic matches!

Ensure it’s not high bc of same keywords

- ✅ match_semantic_spaces_v6: [**which feats which keywords for appraoch 2**](https://colab.research.google.com/drive/1Nr9nzDbAWUF-EkvZzT3G6GXs4Mw532UD#scrollTo=jsXeAVMyh4zV)
    - ✅ code: [**which feats which keywords for appraoch 2**](https://colab.research.google.com/drive/1Nr9nzDbAWUF-EkvZzT3G6GXs4Mw532UD#scrollTo=jsXeAVMyh4zV)
        - fList_model_B_seqs matches feat_ID to top token
        - so in the features that are kept after filt, find their top token using fList_model_B_seqs
        - ISSUE: we don’t know which of the top 5 that was matched
            - we shouldn’t care about which was matched; just that it’s relevant in concept category. just take all the top 5 and see which belong to keywords list. get its count?
            - actually, it DOES matter, but only within a feature. if a feature contains “king” 3 times, we should only record that it contains “king”. this is bc we’re trying to find feature sim based on which keywords they activate on, but it doesn’t matter how many times that keyword appears in its top 5.
- ✅ run time (many keywords)
- ✅ time v2- rmv after
    
    also does well
    
- ✅ calendar: a subcategory of time
    
    remove descriptions like “after” and “soon”, keep only “day” and “month” etc types
    
- 🐣 *otpional*: only allow one (or max few) feature per keyword to prevent high sim bc the same feature
    - should these features be monosem? check after using more tokens
    - if rand of this is low, but “semantically similar” of this is high, then we can put semantically similar back in
    - **actually not needed bc we see most keywords in final result are unique**
- ✅ match_semantic_spaces_v7: loop thru every layer for pythia70m-160m
    - ✅ before running expms, get labels for each indiv SAE for each LLM
    - ✅ account for mixed feats or filtered feats being 0; if so, set all vals to None and cont
        - both corr and svcca requires > 1
    - ✅ bc semantic subspaces are smaller, we can use 1k or 10k rand runs
        - use 1k bc “time” still has a lot of 1-1 feats (hundreds)
            - if len > 100, use 100 runs. If len less than 100, use 1000 runs
    - ✅ see if middle high with middle, etc
        - run L5: does well with L3
        - L7: does well with L1, L3
            - not with L2
        - L3: just does bad
        - L9
        - L11
- ✅ shuffling may not be best for semantic subspace b/c these features should all already be highly corr with each other?
    - NO- each is specific to a certain keyword (eg. man) so likely not
- ✅ match_semantic_spaces_v6: use specific months in calendar; countries

More models

- ⚠️ compare LLMs by residual stream, not MLPs
    
    simLLM_pythias_70m_160m_resStream.ipynb
    
    - output.hidden_state is residual stream output, not mlp, so we must use res stream
    - 1A to manyB makes sense in LLMs because it’s individual 512 (A) where more than one of 768 (B) can map into, so there’s enough.
    - how many are many to 1?
        - 96+48+29+26+21+17+17+17 = **271**
    - interpret the many-1 high
    - actually, `mlp.dense_4h_to_h.weight` seems to be the final accumulation? Bc tehre’s no corresponding “residual stream weights” in LLMs. The residual stream is the addition of a bunch of things in the LLMs.
    - get top dataset examples
        - if we show the top are junk (they’re polysem so why would they be), we can use 10 to 1 instead. this balances many-1 and 1-1
    - but the many-1 by itself is not good. and the 10-1 by itself is not good. so why are they good when combined? what feature space are they combined into that’s good?
    - the overall corr plot for many-1 also looks much worse than for saes corr plot
    - if you keep below 50 only (that is, not 393 feature which is the only one abvoe 50), you get pval of 0.34
        - but this still has low pval for early layers to early layers and early to late layers?
    - filtering 1-10 makes L1 better than 1-30, but 1-many has L1 as the best
- 🐣 num_unq_pairs was measured wrong.
    - It’s not `len(list(set(highest_correlations_indices_AB)))/ len(highest_correlations_indices_AB))` because the len of indices is from (given `batched_correlation(reshaped_activations_B, reshaped_activations_A)` ) model A, but the values instead are from model B. In SAEs this was okay. But in LLMs, they’re 2 diff dims. So
- ✅ gemma1 vs gemma2
    
    simSAE_gemma1vs2.ipynb
    
    - results analysis
        
        it seems the many-1 does better than 1-1; also should filter out 0.1. for L10 vs L15 (gemma1 2b vs gemma2 2b), the svcca is 0.13 and random is 0.007 on avg of 5 runs. however im only using 50 samps and 50 seqlen due to colab limits. 
        
        i think gemma1 vs gemma2 may be more similar due to having more similar sizes
        
        L10 vs L12: this gets svcca of 0.17
        
        i think many-1 is worse wehn the LLMs are diff sizes
        
- ✅ simSAE_gemma1vs2_v2: slightly more data (100 x 50)
- ✅ simSAE_gemma1vs2_v3: more data by batch proc
    - 150 x 150 = **22500**
        
         got similar scores, so this is more reassuring
        
- ⚠️ simSAE_pythias_70m_160m_filt_all_1.ipynb
    
    check if 10-1 or 1000-1 works well for L3 vs L5
    
    - [instead of just choosing one for 100-1, try choosing 100 of them](https://colab.research.google.com/drive/1CeSFpjxoaYQBmZdb1rogKBR4hf2kzQ3u#scrollTo=yUeMvinjwDty&line=1&uniqifier=1)
- ⚠️ only many-1 works well for gemma, and only 1-1 works well for pythia.
    - notice gemma highest counts is around 2000, while pythia highest count is
    - what about 1000-1 for pythia?

gemma1v2 semantic space

- ✅ gemma1v2 semantic space
    
    match_semantic_spaces_gemma.ipynb
    
    - [take the sum of all keywords and run it through, it also gets good matches](https://colab.research.google.com/drive/1wHyHJMGPmRvRrPPm6F3xOqRLVOi9h_Lc#scrollTo=_4RndSRy8d_d&line=1&uniqifier=1)
    - add up entire semantic spaces by using keywords from all in union

filt matches which don’t have same keyword at least once

- ✅ why does semantic subspace work so well? why do 1-1 work while many-1 doesn’t work? notice when interp many-1, may be noisy.  see simSAE_pythias_70m_160m_interpret_manyTo1.ipynb
    
    ![image.png](Debug%20non-concept%20features%20issues%2011eafed922dc80b280acc110c87a93e0/image.png)
    
- ✅ say too much noise when using entire space. will have to filter better. this is bc some matches by actv corr- which is not the best- don’t semantically match. Not the best way to pair features
    - ✅ try filtering by requiring both high actv corr + semantic matches (at least 1 keyword in common)
    - get labels for each layer. then filter out pairs which don’t match on at least 1 keyword in common. get rid of pairs which contain features that activate 3/5 on . or new lines
    - get rid of matches that correlate just on period
- ✅ filt_by_semantics_gemma.ipynb
    - the inds are B, so prev way to use corr[ind_A] is wrong.
    - interpret top many-1
    - notice in gemma a lot of ‘high corr’ is junk
        
        ![image.png](Debug%20non-concept%20features%20issues%2011eafed922dc80b280acc110c87a93e0/image%201.png)
        
    - keep out those with extremely high corr
        - this makes it worse; between 0.1 and 0.8, only 0.026 SVCCA
        - if you keep only above 0.8, SVCCA is 0.25
        - keep only above 0.6, SVCCA is 0.19
        - **0.5 < corr < 0.8 is 0.03**
    - [try filtering by requiring both high actv corr + semantic matches (at least 1 keyword in common)](https://colab.research.google.com/drive/1yQjdUpeER5FEYSgNz-iYzs8P8CPKsVmH#scrollTo=K8Zb8AHWRZYT&line=1&uniqifier=1)
        
        SVCCA is 0.16, which is just slightly higher than unfiltered
        
    - [try filtering by excluding periods and newlines](https://colab.research.google.com/drive/1yQjdUpeER5FEYSgNz-iYzs8P8CPKsVmH#scrollTo=Fa88SimoThua&line=1&uniqifier=1)
        
        SVCCA is 0.23, which is really good! much higher than before
        
    - after doing 1-1, it doesn’t make a difference. this means most of the many-1 are junk. but some of the 1-1 are junk too?
    - REMOVE JUNK: * I raised the score of L12 v L15 from 0.1 to 0.5 *
        - holds for 2 other layer pairs (10, 12), (12,14), (12,18)
    - if you combine rmv junk with rmv those without common keyword, it’s raised from 0.52 to 0.55. But you should primarily just rmv junk, as this makes num feats go from 4782 to 4215
- ✅ filt_by_semantics_pythia.ipynb
    - L2 v L5 passes
    - L3 vs L5 doesn’t
        - interpret what remains: [didn't filter out \n somehow](https://colab.research.google.com/drive/179Von4RjR5EkNstu71l40M4Xlandy63L#scrollTo=Zl5ef58YiFuJ)
        - rmv featues junk, space agnostic
            - still forgot double escape: \\n
    - get rid of <|endoftext|> ; is diff in pythia
        - this increases to 0.6
- ✅ in appendix: also these could be "next tokens" that aren't specific to concepts, but multipel concepts, so it's mixing concept spaces up
    - eg) “I am BOB!” vs “that cat ate!”
    - in L3 v L5, why did this pair not get filtered out when they have no top tokens in common
        
        ![image.png](Debug%20non-concept%20features%20issues%2011eafed922dc80b280acc110c87a93e0/image%202.png)
        
    - [## why pairs no common still pass](https://colab.research.google.com/drive/179Von4RjR5EkNstu71l40M4Xlandy63L#scrollTo=ArtvQxjKth7C&line=1&uniqifier=1)
        
        SOLN: this pair is NOT there; your feature interpretation is just wrong. it should loop over the new inds, not old ones.
        
    - (3, 6) & L2 vL4- colons : , apostrophes. include : and ` and ' and slash and brackets.
        - this makes it WORSE (by a little). so some punctuation doesn’t matter?
    - Also other non-domainc specific like &, ^, *, _, <, >
    - don’t include arithmetic, as those are domain specific
- ✅ loop gemma and rmv junk features
    
    [loop_gemma_rmvJunk.ipynb](https://colab.research.google.com/drive/1osChfZMNm6jIyBX2cVGwT5PWxzUHRbzm#scrollTo=svBnV7fcZegk)
    
    - pval runs of 10 for now
- ✅ load all layer data and get SVCCA paired heatmap
    
    heatmap_paired_scores.ipynb
    
- ✅ loop pythia and rmv junk features
    
    loop_pythia_rmvNonconc.ipynb
    
- ⚠️ pythia L2 v L3: debug why so low during loop
    
    [filt_by_semantics_pythia.ipynb](https://colab.research.google.com/drive/179Von4RjR5EkNstu71l40M4Xlandy63L#scrollTo=hUo-PTnMOc89&line=1&uniqifier=1)
    
    - interpret to see if another junk char still there
    - don’t see obvious hindrances
    - may just show 1-1 results in main text, and non 1-1 in appendix
- ✅ run gemma again but just get % unique (or 1-1)
    
    loop_gemma_rmvJunk_1_1.ipynb
    
    - mean corr both after filt kw and after filt 1-1
    - PREV BUG: the 1-1 didn’t work for gemma before bc you forgot to change kept_modA_feats to == 1 instead of <100000
    - L10: seems to do slightly worse than before 1-1
    - L12: other than layer2, seems to improve it a little bit
    - L17: other than layer6, seems to improve it a little bit
- ✅ rmv nonconc and 1-1 : pythia
    
    loop_pythia_rmvNonconc_1_1
    
    pythia_heatmap_paired_scores_1_1