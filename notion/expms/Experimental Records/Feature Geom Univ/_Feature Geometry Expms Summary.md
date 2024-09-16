# _Feature Geometry Expms Summary

Expms Summary

1. ✅ plot pretrained sae features on pca OR umap
2. ✅ plot feature acts, and compare before vs after steering/ablating/patching

---

pipeline summary

1. train
2. save actvs for two models
3. map correlated features, umap viz, cca scores
4. interpret correlated features using dataset examples; get same tok score

1 saved in ‘sae training’, 2-4 saved in ‘sae cross model’ folders

---

### Expm Sagas

TS 1L vs 2L expms

- train_tiny-stories-1M_sae.ipynb (renamed from train_gpt2_tinsto_sae_v2.ipynb)
- train_ts_sae_1L-21M.ipynb
- tinystories_actv_corr_mat_v1.ipynb: compare top feature pairs AND for each feature, its top 3 counterparts, for `tiny-stories-1L-21M` and `tiny-stories-2L-33M_MLP0 and MLP1`
- tinystories_actv_save.ipynb: 1L vs 2L. just get for any 100 data samples
- tinystories_actv_corr_mat_v2.ipynb: for 100 samples with no BOS prepend, save these actvs and run again but use correlation not cosine sim
- [tinystories_actv_save_v2](https://colab.research.google.com/drive/1yB4-mBBpUIRwVCWCl9QoIPQbbAuTg4NT#scrollTo=GFApm9B6afEP&line=1&uniqifier=1).ipynb: 1L vs 2L. get samples for a concept both models should represent (eg. pronouns, fire, etc) and see what features both fire on.
- [tinystories_actv_corr_mat_v3](https://colab.research.google.com/drive/1F1-fHJJYNywejQg4EzO1_NCTdwoss13K).ipynb: get samples for a concept both models should represent (eg. pronouns, fire, etc) and see what features both fire on.
- [load_actvs_interpret_features](https://colab.research.google.com/drive/1qUNgjrK8l1JNbSde9PLT6tnm9vgwv-HL#scrollTo=NsN8cKw5mfuj).ipynb: after obtaining correlated features, load tinystories F actvs again and interpret with dataset examples
    - feature top_ind_from_B(1786) is “years”, while its analogues in A are “time, summer, morning, day, once” so not EXACT but similar.

TS 1L vs 2L Feature Splitting Expms

- training nbs
    - train_ts_sae_1L-21M_df-8192.ipynb
    - train_ts_sae_1L-21M_df-32768.ipynb
    - train_ts_sae_2L-33M_MLP0_df-8192.ipynb
    - train_ts_sae_2L-33M_MLP0_df-32768.ipynb
- save actv nbs
    - [save_wt_actvs_dsInterp.ipynb](https://colab.research.google.com/drive/1Bh10l4vTb_rrCUw-483RDGsWavigTcjl): this work for any model, just input it in. No need to separate for each model as we don’t care about keeping the analysis output in nb
- map correlated features
    - [ts_1L_2L_UMAP_df32768.ipynb](https://colab.research.google.com/drive/1dQPHGIpv0uHQt72rG-pMIB0b7z4nA0T_#scrollTo=-ZqeAFR6EEgs)
- combined UMAP
    - [fs_UMAP_v0.ipynb](https://colab.research.google.com/drive/1swzOhJPlBvZNQrZjBW6xZdYalAVkmZjh#scrollTo=HTJhjkZ1yVt4): relu, 30k epochs
    - [fs_UMAP_v1](https://colab.research.google.com/drive/1Ubxrtvycgo0NWr6svNQj93AKt2ZNT7ap).ipynb: topk 32, 100k epochs

Feature Relation Mapping Expms

- [ts_actv_save_1L_2L_featRelns.ipynb](https://colab.research.google.com/drive/1yxw5HJn2h9v4OpAkSdpHvKeAvR3CIpHE)
    - fActs_ts_1L_21M_featrelns_v1.pkl
- [ts_1L_2L_UMAP](https://colab.research.google.com/drive/1Cl7nohl7hyaKz17bHbrkDgkADf-0DPqZ#scrollTo=kUYRF57KNxrL).ipynb: side by side decoder weight umaps, corr actvs
- ts_actv_save_1L_2L_anySamps.ipynb: save actvs for 500 any samps (not concept specific)
    - batch_tokens_anySamps_v1
    - fActs_ts_1L_21M_anySamps_v1.pkl
- [ts_1L_2L_UMAP_v2](https://colab.research.google.com/drive/1M9Q5iDxnJl5SDI-n5CE4wnJrff-Wr293#scrollTo=CRcTQwEN0qia).ipynb: slowdown bc too many cells, so clean up in `ts_1L_2L_UMAP_v2.ipynb` to try more keyws
- [ts_1L_2L_UMAP_actvs](https://colab.research.google.com/drive/1b2vob-ZX8IRBWw-1XLPY1wTCCXYJfVpj#scrollTo=6CvQQSVdQvq5).ipynb

<<<

IF OOM: try to load just actvs, reshape (del orig), and save corrs BEFORE load weights  + labels. Then load just weights, labels, and corr in second run to get umap comparisons

- find related story features
    - get sentences just about: king-queen-princess ***and*** father-mother-daughter
    - get sentences just about: she-he-it
    - get sentences just about: princess-dragon-knight

---

Topological Data Analysis

- [mapper_example.ipynb](https://colab.research.google.com/drive/1qBX9sQ5iwlcX17lwrmiXl36Yzfg6hkNP#scrollTo=f_AY6TPyE3PC): orig data of tutorial
- [SAE_DW_mapper_explora.ipynb](https://colab.research.google.com/drive/1DFsPl7EFa0SDNjlopjKmtFTcV2PfvGmQ#scrollTo=NwyZqjVONo6H):
    - [SAE_DW_mapper_explora_v1.ipynb](https://colab.research.google.com/drive/1sbFaxO0tpWgGJIA4VZ0R8xL_Jzj-TjZL): all others
    - [mapper_pretrained_saelens_dw.ipynb](https://colab.research.google.com/drive/1Dj41zt3JLqxImeZub6w7XEI95Qj07KkS)
- homology_example.ipynb
- persHom_saeFeats_explora.ipynb
- 

---

Synth Actvs

- [synthData_explora.ipynb](https://colab.research.google.com/drive/1lHOtRa8KHIZuqbetilKkZFypfHDnSz2M#scrollTo=PLIDVkYupqYY) : expms using luke’s code (few mods)
- [synthData_explora_v2.ipynb](https://colab.research.google.com/drive/1S9GlHc60Y_SD3EN4D27GBLSpGPPhrR-l#scrollTo=Tdr-XiFEGDgR) : compare drastic mods to luke’s code for synth data
    - [test_synthActvs.ipynb](https://colab.research.google.com/drive/16HzLfM-3OG_5AkPlkAz63fSltx85zRnB): clean up and send to Robert Huben to check
- [synthData_explora_v3](https://colab.research.google.com/drive/1g44mZQNDMx7RiUvvIeZkeSYmN1srD53U).ipynb: new saes
- clust_synth_actvs_test.ipynb: cleaned up new synth gen code only (no luke’s code)
- [synthData_jaccard_v1.ipynb](https://colab.research.google.com/drive/1BlFYR_ubdkNyC5yF_ftY5RY-Qt1K-WLI):
    - ground truth features: highest cosine sim shuffle matrix then apply jaccard
    - generate B using shared GTF, and rearrange col (G) ordering so diff freqs

---

Sim of Feature Subspaces

- [jaccard_subset_ts_1L_2L.ipynb](https://colab.research.google.com/drive/1LIHrRNnB2rPp197QGLyji7a1IJNeI_g9#scrollTo=nKQgHI_BvyBq)
- save_LLM_w_actvs_c_fc.ipynb: c_fc is wrong bc that’s input to MLP, not MLP out, which saes are trained on
- save_LLM_w_actvs_c_proj.ipynb: this is the right one

---

Compare singular values of spaces

- SVD_on_SAE_univ_v1.ipynb
- SVD_on_SAE_univ_v2.ipynb: clean up into fns and plots
- SVD_on_SAE_univ_v3.ipynb: get rid of bad metrics (only use 2)
    - run on bigger SVD weights
- SVD_on_SAE_univ_v4: use c_proj for LLMs
    - **compare after SAE corrs**
- SVD_on_SAE_univ_v5: clean up to only use SAE100k weights
- SVD_on_SAEs: link to vidit

---

Sim metrics on pretrained

- expm results
    - ✅ first compare GPT2 pretrained with tinystories self-trained
        - ✅ plan how to compare: data, layers
            
            [https://jbloomaus.github.io/SAELens/sae_table/#gpt2-small-mlp-out-v5-32k](https://jbloomaus.github.io/SAELens/sae_table/#gpt2-small-mlp-out-v5-32k)
            
            - instead of using the pile as activations, use tinystories on BOTH GPT-2 small and TS-1L
            - compare L0, L8 (mid), and last layer of GPT2sm `blocks.0.hook_mlp_out`. This is bc MLP0 of ts-1L is similar to either capturing all features in 1L (so like the last layer) or “enough most impt” (so L8?)
        - ✅ pretrained_SAE_save_actvs.ipynb
            - NOTE: after checkmark cell finishes running for save to drive, DO NTO DISCONNECT bc this does not mean it finished copying (a large file, like actvs or samples!) it only finishes once it appears in drive! also trying copy a small file AFTERWARDS to “free up” and push the file in bc it may be stuck??
        - ✅ jaccard_subset_ts_GPT2_v1.ipynb: 16k (TS-1L) vs 32k (GPT2sm)
            - ISSUE: OOM for 64k actvs when taking corr mat
                - try 9000 tokens and only half the 32k features for now
            - [try comparing corrs both ways: match B (GPT2sm) with multp](https://colab.research.google.com/drive/1LIHrRNnB2rPp197QGLyji7a1IJNeI_g9#scrollTo=e070dcO89Z-K&line=1&uniqifier=1)
                
                # highest_correlations_indices_AB contains modA's feats as inds, and modB's feats as vals
                
                - there seem to be more corr matches if we pair each TS-1L 16k_SAE feature with the GPT2sm 32k feature
                    
                    ![image.png](_Feature%20Geometry%20Expms%20Summary%201beb35705e5c47cd89c1c6b7908094c0/image.png)
                    
        - ✅ jaccard_subset_ts_GPT2_v2.ipynb: 20000 token actvs, same as v1 for rest
            - marginally higher results than v1
        - ✅ jaccard_subset_ts_GPT2_v3: 32k sae (TS-1L) vs 32k sae (GPT2sm)
            - ISSUE: OOM for 64k actvs when taking corr mat
                
                [SOLN: use batches to compute corr](https://chatgpt.com/c/ca3a77b6-0bb1-40b1-acdd-3d8afa0cbaab)
                
            - NOTE: no need to disconn if dont want to lose gpu access, just restart
                - ALSO- no need to mount or reinstall libs again! saves saelens time
            - similar results as before, except rsa
            - [but: can representational_similarity_analysis be negative](https://chatgpt.com/c/f7e41533-c472-443a-8f35-d6d063d63185)
    - ✅ compare LLM sim of GPT2sm vs TS-1L, vs SAEs sim
        - sim_LLM_ts1L_gpt2sm_MLP0.ipynb
            - cuda OOM if use all batch tokens
            - need the smaller one to be in SECOND? so this will give IN TERMS OF A: `highest_correlations_indices, highest_correlations_values = batched_correlation(reshaped_activations_B, reshaped_activations_A)`
            - RSA must align exactly, so need to cut off when rows not comparable
                - note that the metrics heavily depends on number of samples, we can’t compare LLM vs SAE if LLM weights only use 1024 while SAE uses 16384 or 32k. having 32k have a higher score is much more sim than 1024. compare them relative to rand pairings
                - still, svcca and mnn show llm pairings dont do much, but rsa shows it does it. perhaps is statsitical fluke? try on more models.
    - reprSim_ts1L_MLP0_GPT2_MLP8

<<

- pretrained_SAE_save_actvs
- jaccard_subset_ts_GPT2_v1.ipynb: 9000 token actvs, 16k vs 32k MLP0 of gpt2 vs TS, but only use first 16k features of MLP0 gpt2
- jaccard_subset_ts_GPT2_v2.ipynb: 20000 token actvs, same as v1 for rest
- jaccard_subset_ts_GPT2_v3: 32k sae (TS-1L) vs 32k sae (GPT2sm)
- sim_LLM_ts1L_gpt2sm_MLP0.ipynb
- reprSim_ts1L_MLP0_GPT2_MLP8
- reprSim_ts1L_GPT2sm_oneMLP.ipynb: first test running cleaned up nb on one layer and saving output to csv
- reprSim_SAEs_ts1L_GPT2sm_multMLPs.ipynb: then clean up further into a loop
- reprSim_LLMs_ts1L_GPT2sm_multMLPs

---

Gemma2 Steering

- steering_gemma2_nums_months_v2.ipynb: get rid of other input tasks and umaps and common features, only focus on steering expms to check how many cases get desired answer by steering vec
- steering_gemma2_nums_months_v3.ipynb: turn tests to fns with scores; plot and tables
- clean up nb: steering_gemma2_nums_months_v4.ipynb
- steering_gemma2_nums_months_v5: get actvs using transformerlens rather than gemma2’s tutorial and see if there’s a diff after ablating
    
    steering_gemma2_ordinalSeqs
    

---

More actvs for corr- prevent OOM

- ✅ [corr_large_data_v0.ipynb](Project%20Planning%20b4b05f73d85e409f8409b209e44ed692.md)
    
    [https://chatgpt.com/c/bfd75113-bcbe-4c7c-b99e-dfb987ad1b3a](https://chatgpt.com/c/bfd75113-bcbe-4c7c-b99e-dfb987ad1b3a)
    
    - test if correlation fn is correct by reversing order of first dim rows of actvs, then seeing if correlation fn corerctly pairs first and last rows together, etc
        - it doesn’t.
        - unbatched also has this issue. but this was used to successfully find actual pairs in ts?
        - check if the normalized vers equal each other
            - they DON’T!
            - [https://chatgpt.com/c/4fde2b47-eca7-4b21-9001-f0470431899b](https://chatgpt.com/c/4fde2b47-eca7-4b21-9001-f0470431899b)
    - [when computing pearson correlation coefficient, is it valid to compute just one row each of two matrices? answer yes or no and why](https://chatgpt.com/c/eb0012c3-5ec8-4727-b9e3-c2e7bde3b628)
        
        Yes, it is valid to compute the Pearson correlation coefficient for just one row each of two matrices. The reason is that the Pearson correlation measures the linear relationship between two datasets, regardless of their origin as rows, columns, or otherwise. Each row in a matrix can be considered a separate dataset. Therefore, as long as you have paired data from these rows and they are of the same length, you can calculate the Pearson correlation coefficient to determine the degree of linear correlation between these two rows.
        
    - SOLN: how come when I use this code on a matrix and the matrix where the rows are reversed order, i don't get the first and last row have highest corr:
        
        you should reverse the COLUMNS instead. the rows must be the same bc they’re the tokens, so they have to correspond to each other! nothing was wrong- it’s the col order that should’ve been changed!
        
        now obv that doesn’t matter for cosine sim, but corr coeff REQUIRES paired rows (but not cols)
        
- ✅ corr_large_data_v1.ipynb
    - normalization of (100k * 32k) elemns by chunking
        
        [https://chatgpt.com/c/084deca8-bb72-4efa-8538-19fdf17c4a56](https://chatgpt.com/c/084deca8-bb72-4efa-8538-19fdf17c4a56)
        
    - [do tensor operations and structures cost more than numpy](https://chatgpt.com/c/de0df0a7-a123-441d-979e-6a4cba6503c6)
        
        if im doing batch processing using matrix multp should i use cpu or gpu
        
    - the reason why sae actvs may map to same is bc those are zero feature neurons
        - so what if they’re just finindg similarity of the cluster of zero neurons?
        - thus, get rid of zeros! (dead neurons)
            - getting rid of duplicates sort of already does this, bc usually the “frist 0” is always mapped to
        - find how many cols of tensor are all 0
            - right now, just around 10%. so this isn’t a big deal. svcca finding 0.6 sim can’t be poss if it’s just matching those 10%
    - set() cannot be applied to tensor, only list or array
    - the reason slicing the actvs of sparse actvs doesn’t work is bc most in front are 0. correlation of two zero vectors isn’t 1, but 0.
- ✅ corr_large_data_v2.ipynb : compare actvs from 2 diff models
    - ISSUE: 1000 samples of OWT gets low corr (.015)
        - try 100 samps on same code to see if get same corr mean as last time (0.7). if not, code has issue.
            - we get 0.2 for
        - try the same corr fn code on the data
            - if diff results, maybe it’s data construction that’s wrong or another code that’s corfFn
                - it’s the same.
        - try using the same data construction
            - in this nb, the model is loaded using `.to('cuda' if torch.cuda.is_available() else 'cpu')` which forces us to use `inputs = {k: v.to("cuda") for k, v in inputs.items()}`. so don’t load model using that so we don’t have to use that, adn see if get same answer as last nb. if so, that’s prob the culprit.
                - no, it gets it wrong, so it’s not the culprit
                - SOLN: wrong variable (using i=0 for hidden state)
            - so the data construction wasn’t done right
            - use new corr fn on old data constr
                - this gets the same results as the old nb, so corr fn isn’t the issue
                - issue must be in the accumulated data construction
        - **dont run model actvs in batches**: just use 1000 samps in input to model
            - ISSUE: even 300 samps gets out of memory
        - so write new batch model actv code
            - hypothesis: inputs in batches is wrong. we should get all the inputs using the tokenizer at once so the padding and truncation is done consistnly for all samples when thru model. instead of tokenizing input during each batch?
            - SOLN: this works using dataloader to batch proc existing input that’s tokenized all at once
        - ⚠️ ISSUE: for >400 samples, `feature_acts_model_A = sae.pre_acts(accumulated_outputs)`  -OOM, so do in batches the same way (not data loader, just slices of accumulated output)
            - ISSUE: even after doing this, still OOM at 400
    - only sim on top 50% corr and top 90%
        - [https://chatgpt.com/c/5cceac91-5cd7-41e8-b50b-cad9cfd9108e](https://chatgpt.com/c/5cceac91-5cd7-41e8-b50b-cad9cfd9108e)
        - ends up bad. seems like it’s not just highly correlated featues that form the related subspcace.
    - modify this to add in only the 2nd seen unique pair, not the first
        - [this also has high svcca](https://colab.research.google.com/drive/1lP2nXMIcSdGq8vOtp00rto5RLKJyc8DH#scrollTo=j5bPQ9igID_g&line=1&uniqifier=1)
        - but why doesn’t just getting highly corr pairings work?
        - what’s the avg corr val for these unique lists?
            - it’s a bit LESS than before!