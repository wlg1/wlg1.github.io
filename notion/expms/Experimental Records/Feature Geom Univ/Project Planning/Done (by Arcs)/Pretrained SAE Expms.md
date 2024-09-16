# Pretrained SAE Expms

Review work, plan next

- ✅ project update to David Krueger
    
    **Main research goal:** We aim to measure the extent of relational and functional similarity of Sparse AutoEncoder (SAE) feature subspaces for multiple LLMs as we vary LLM parameters, SAE dictionary sizes, and more. This will reveal if SAEs can reveal analogous features that are learned across different LLMs.
    
    **Why study this:** We aim to find if study feature relations (eg. king-queen-princess-dragon) are learned similarly across LLMs. If so, then we may be able to use the same set of "steering features" across LLMs, and can better expect which features would be learned under certain conditions. These feature relations may be hidden in LLMs, but SAEs may reveal them.
    
    **Some recent results found:** Using metrics such as Mutual Nearest Neighbors, we find that we can measure feature relation similarity across LLMs using SAEs, while these relational similarities were not able to be detected just by looking at LLM neuron spaces. In other words, correlated SAE features across LLMs also have analogous neighbors.
    
- 🐣 read repr sim
    - RSA
        - 1st order isom: betwen X and Y ?
        - 2nd order isom: within X, then within Y, and compare those withins?
- 🐣 https://www.lesswrong.com/posts/WsPyunwpXYCM2iN6t/calendar-feature-geometry-in-gpt-2-layer-8-residual-stream
- synthData_explora_v3.ipynb: new sae + MMCS code. train on unif synth data using new sae fns. aim to get low MMCS between new enc weights and GTF

Compare Pretrained SAE expms

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
                
                ![image.png](../../_Feature%20Geometry%20Expms%20Summary%201beb35705e5c47cd89c1c6b7908094c0/image.png)
                
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
- ✅ `batched_correlation(reshaped_activations_B, reshaped_activations_A)` : highest_correlations_indices_AB contains modA's feats as inds, and modB's feats as vals. Use the list with smaller number of features (cols) as the second arg. Then use `jaccard_similarity(weight_matrix_np, weight_matrix_2[highest_correlations_indices_AB])` bc we’re using the indices of first model (A), and shuffling B.
- ✅ reprSim_ts1L_MLP0_GPT2_MLP8
    - try loading saelens to prev saving and see if compat with corr numpy
        - yes it is
- 🐣 rsa is weird when the dims don’t match. maybe don’t use it for those. also slow
- ✅ sim metrics: loop over all layers GPT2sm vs TS-1L, auto output table and plot
    - ✅ reprSim_ts1L_GPT2sm_oneMLP.ipynb: first test running cleaned up nb on one layer and saving output to csv
    - ✅ reprSim_SAEs_ts1L_GPT2sm_multMLPs.ipynb: then clean up further into a loop
- ✅ loop LLM vs SAE for all layers GPT2sm vs TS-1L
    - reprSim_LLMs_ts1L_GPT2sm_multMLPs
- ✅ make (zoomin, not 0 to 1) LOG-scale plot comparing rand pairings for compare LLM sim of GPT2sm vs TS-1L, vs SAEs sim
    - or compare by ratio proportion instead, as it depends on number of samples used
    - Jaccard and/or SVCCA: LLM (paired, unparied) in one plot, SAE (p, unp) in other plot
    - meeting slides: [https://docs.google.com/presentation/d/1w7F5FbwM75NdHPMUNG4FMsardVWiA8z9HiUeJ6_bGXU/edit#slide=id.g2f5382243ab_0_0](https://docs.google.com/presentation/d/1w7F5FbwM75NdHPMUNG4FMsardVWiA8z9HiUeJ6_bGXU/edit#slide=id.g2f5382243ab_0_0)

Train sae on adversarial models

- ✅ load_poison_rlhf_model.ipynb
    
    "UNIVERSAL JAILBREAK BACKDOORS FROM POISONED HUMAN FEEDBACK" in ICLR 2024 might be what your are looking for. It implants a trigger into the LLM such that the LLM gives unsafe and harmful response when triggered. The base model and the adversarial model can be found in its github link. [https://github.com/ethz-spylab/rlhf-poisoning](https://github.com/ethz-spylab/rlhf-poisoning)
    
    - ✅ Since the paper found a **universal backdoor**, perhaps the features associated with it are also universal? No: [https://chatgpt.com/c/723761e1-005d-46e4-a2cc-19fe483968f5](https://chatgpt.com/c/723761e1-005d-46e4-a2cc-19fe483968f5)
    - ✅ Load data: This is not poisoned yet (harmless): [https://huggingface.co/datasets/Anthropic/hh-rlhf](https://huggingface.co/datasets/Anthropic/hh-rlhf)
        - [https://chatgpt.com/c/31b12f64-f73e-4d55-945a-96c301aebec8](https://chatgpt.com/c/31b12f64-f73e-4d55-945a-96c301aebec8)
    - ✅ Get activations using hook in model
    - The model poisons Anthropic/hh-rlhf dataset. Train SAE on both activations from poisoned and harmless data?

simSAE_two_pretrained very diff models

- ✅ read “resi” LLM benchmarks paper to check they’re not using sim metrics by feature weights
    - how does this paper use metrics like jaccard? does it pair by inputs or feature weights?
        
        [https://chatgpt.com/c/0b66abd2-4261-4b4b-962d-83428e204cf3](https://chatgpt.com/c/0b66abd2-4261-4b4b-962d-83428e204cf3)
        
    - ask max: To double check, for that paper and ReSI, the instance-wise pairs for R and R' are paired by inputs? (and then one can apply Jaccard nearest neighbors based on sample input pairing?)
        
        
    - they align by inputs, not feature weights
    - it uses bert anyways: The language models referenced in the paper, such as BERT, are primarily used for classification tasks, like sentiment analysis and natural language inference, rather than for generative purposes.
- ✅ gpt2 vs pythia tokenizers
    - [https://claude.ai/chat/f9a93710-1c22-4f78-b595-1016f0fac177](https://claude.ai/chat/f9a93710-1c22-4f78-b595-1016f0fac177)
    - what do they mean by token matching
        - [https://chatgpt.com/c/0ec9e0ef-8e53-4f15-836d-549c242ca964](https://chatgpt.com/c/0ec9e0ef-8e53-4f15-836d-549c242ca964)
    
    simSAE_gpt2_pythia70m.ipynb
    
    - [**compare dataset tokenization**](https://colab.research.google.com/drive/1sk_2Md0cvEQC8bzbBobEYuc35gVKsTBY#scrollTo=wtaez_m7u7V2&line=1&uniqifier=1)
        
        torch.Size([37054, 128]) - gpt2
        torch.Size([37124, 128]) - pythia
        
        - So not directly comparable bc which token is aligned with which? hard to tell.
        - NOTE: max_length DOES NOT CUT OFF. It just says how to reshape the total number of tokens of **4742912 into how many cols in the tokens matrix.** max_length is the num of cols, so if choose 10, we get [474426, 10] for gpt2, which is the same as 37054 * 128
        - we get EXTREMELY DIFFERENT RESULTS for different tokenizers
            
            ```python
            model.tokenizer.decode(batch_tokens_1[0])
            model_2.tokenizer.decode(batch_tokens_1[0])
            ```
            
            - in other words, the vocab IDs don’t even match.
            
            ![image.png](Pretrained%20SAE%20Expms%2084fa53a2d95d4a8988affa18f7053e95/image.png)
            
    - [**align actvs by common phrase**](https://colab.research.google.com/drive/1sk_2Md0cvEQC8bzbBobEYuc35gVKsTBY#scrollTo=ME1t8l3p_J_m)
- ✅ check if saes trained on diff pythia models
    - [https://huggingface.co/collections/EleutherAI/sparse-autoencoders-66b101b12395fcd909d148a3](https://huggingface.co/collections/EleutherAI/sparse-autoencoders-66b101b12395fcd909d148a3)
    - does pythia 70m vs pythia 140m use same tokenizer: [https://claude.ai/chat/464f0103-eb50-4e9e-b271-a02f0f8cf004](https://claude.ai/chat/464f0103-eb50-4e9e-b271-a02f0f8cf004)
- ✅ simSAE_two_pythias_70m_deduped.ipynb
    - load saes using: [https://github.com/EleutherAI/sae](https://github.com/EleutherAI/sae)
        - must use `%cd /content/sae/`, else won’t go there. can’t use `!cd /content/sae/`
        - [or just use:](https://chatgpt.com/c/408eda4a-4cea-4b7e-af09-bf7192ba31cf) `!pip install git+https://github.com/EleutherAI/sae.git`
    - ISSUE: when loading llama or pythia, 1 layer or many, get error:
    `TypeError: SaeConfig.**init**() got an unexpected keyword argument 'signed'`
        
        The error you're experiencing, related to an unexpected keyword argument in the initialization of `SaeConfig`, is not likely specific to Google Colab but more related to the version compatibility of the software itself
        
        - TRY: maybe i'll modify the code to remove signed from the cfg.json before passing it to SaeConfig and see if it works
    - [pythia 70m vs pythia-70m-deduped. what is globally deduplicated](https://chatgpt.com/c/8f23cee3-1ca1-4963-b292-bbcc13eb1465)
        
        were they trained from different random inits?
        
    - Why is `latent_acts[0].top_acts.shape` of `Size([100, 294, 16])`, when it should be (numsamps, seqlenmax, saesize), and `Sae((encoder): Linear(in_features=512, out_features=32768, bias=True))` ?
        
        SOLN: [https://github.com/EleutherAI/sae/blob/main/sae/sae.py#L181](https://github.com/EleutherAI/sae/blob/main/sae/sae.py#L181)
        
        This shows encode returns the top k (k=16) latents. This makes sense as only those would have activations. It also gives the indices too. The `top_acts` in `forward` also returns the same thing. If we want the whole thing, we get `pre_acts`, which is before top_acts
        
    - [in pythia,  model(**inputs, output_hidden_states=True) gives 7 items in outputs.hidden_states. which one corresponds to layer 4?](https://chatgpt.com/c/061fd5dc-d5a9-4fe8-9565-d105e9da41c4)
    - For layer 4, SVCCA: `batched_correlation(reshaped_activations_A, reshaped_activations_B)` and `svcca(weight_matrix_np[highest_correlations_indices_AB], weight_matrix_2, "nd")` works, but not `batched_correlation(reshaped_activations_B, reshaped_activations_A)`, when A is 70m and B is 70m-deduped.
    - But jaccard doesn’t seem to work, whether for k=10 or k=4
        
        0.0004039946056547619 / 7.411411830357142e-05 = 5
        
- ✅ simSAE_two_pythias_70m_160m.ipynb
    
    jaccard, k =4: 0.00142 / 3.923688616071428e-05 = 36
    
    jaccard, k =10: 0.002 / 0.00016 = 12.5
    
    SVCCA: 4 times higher
    
- ✅ REFLECT ON WHY LOWER SCORES- NEED MORE/DIVERSE ACTVS?
    
    You need to use more activations bc before it uses tinystories 100 samples, but that’s not enough for a good pairing when pythia is so big. All you’re doing is pairing some features that activate on fairy tales, but you’re not pairing the major ones. This works for tinystories since fairy tales is their main theme, but not pythia. The fact that you’re getting some correlation means it’s working somewhat well. 
    
- ✅ simSAE_two_pythias_70m_deduped_openWebT.ipynb
    - [https://huggingface.co/datasets/monology/pile-uncopyrighted](https://huggingface.co/datasets/monology/pile-uncopyrighted)
    - The pile has been permanantly taken down due to copytright reasons. You can access a clean version at this [link](https://huggingface.co/datasets/monology/pile-uncopyrighted)
    - [https://huggingface.co/datasets/monology/pile-uncopyrighted/viewer/default/train](https://huggingface.co/datasets/monology/pile-uncopyrighted/viewer/default/train)
        - ValueError: Compression type zstd not supported
    - openwebtext, esp 1-1, does a bit better than tinystories
        
        jaccard k = 10: 0.00155 / 0.00013 = 12
        
        jaccard k =4: 0.00120 / 7.411411830357142e-05 = 16
        
- ✅ **simLLMs**_pythias_70m_deduped_openWebT.ipynb
    - SAEs are 64x wider than LLMs’ 512dim
    - for both openweb and ts, there is high corr row-by-row for MLP layer 4 weights of pythia 70m vs 70m-dedep
- ✅ try diff layer than MLP 4
    - actually no, for mLP2, OWT also has this
- ✅ simLLMs_pythias_70m_160m_OWT_MLP2.ipynb
    - mean actv corr : 0.3
    - no sim for jacc, svcca (same numbers for paired vs unapired)
    - repr: 0.01 / -0.006 = 1.6
- ✅ simSAE_two_pythias_70m_160m_MLP2.ipynb
    - mean actv corr : 0.7
    - jaccard, k =10: 0.01 / 0.0001 = 100
    - jaccard, k =4: 0.008 / 5.667550223214285e-05 = 141
    - svcca: 0.034 / 0.0041 = 8
    
    1-1 only
    
    - jaccard: 0.03 / 0.0012 = 25
    - svcca: 0.41 / 0.006 = 68
    - repr: 0.08 / -0.0003 = 266
- ✅ loop pythia70m MLP2 vs all MLPs of 160m
    
    SAEs: similar scores as MLP2 vs MLP2 for all
    
    svcca: similar scores as MLP2 vs MLP2 for middle layers, less so for last few layers
    
    LLMs: similar scores as MLP2 vs MLP2
    
    - [results slides](https://docs.google.com/presentation/d/1xyA8SPdcm4TKfH-PaL7TyhsVFKQAGI1gd0eHBSJGeRU/edit#slide=id.g2f6914cb395_0_0)