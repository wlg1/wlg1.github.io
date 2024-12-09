# Project Planning

[https://www.notion.so/wlg1/_Feature-Geometry-Expms-Summary-1beb35705e5c47cd89c1c6b7908094c0](_Feature%20Geometry%20Expms%20Summary%201beb35705e5c47cd89c1c6b7908094c0.md)

[Done (by Arcs)](Project%20Planning%20b4b05f73d85e409f8409b209e44ed692/Done%20(by%20Arcs)%201c002201437341e48b55b8276859a632.md)

---

### Working on

More models

- ✅ revisit 160m vs 410m : res vs mlp
    
    [This library trains *k*-sparse autoencoders (SAEs) on the residual stream activations of HuggingFace language models](https://github.com/EleutherAI/sae)
    
    [160m output obtained ISN’T for MLPs; it’s only for res stream. 410 only has mlps, so hard to compare to it](https://huggingface.co/collections/EleutherAI/sparse-autoencoders-66b101b12395fcd909d148a3)
    
    - ✅ first try filt nonconc, to see if resstream vs mlp can still be compared. since res stream is addition that includes mlps, so perhaps can still be paired then rotated to find sim
        - NOTE: you must change the 410m’s LLM output fed into its sae as MLP, not res stream! This requires a hook! Thus, you might as well just compare MLPs after coding this.
            - [however, even (in v0) if you don’t do this, still get some sim (0.1 vs 0). but it’s an error.](https://colab.research.google.com/drive/1sA8ETCO3nMyWKEK-b02cyMiEL9fNF4bg#scrollTo=dhflkGet43rf)
- ✅ SAEs on MLPs: 160m vs 410m
    
    [change: orig = sae.pre_acts(outputs.hidden_states[layer_id].to("cuda"))](https://colab.research.google.com/drive/1iUCTShPqXZda1fk8OjA-CYlZBwZ7ZoGQ#scrollTo=HS5umB34V1Gw&line=1&uniqifier=1)
    
    - ✅ [alt: how do I obtain the MLP output of intermediate layer from AutoModelForCausalLM](https://chatgpt.com/c/672a2293-a770-800c-b0a4-7147a8620cc0)
    - ✅ each time you add a hook to a model, you are adding a new output. so even if you reset the output storage var, if you add the same 5 hooks to a model, then you’ll add 5 outputs to the storage var. how to reset?
        
        If you didn’t track the hooks (i.e., you didn’t store the handles returned by `register_forward_hook`), there’s no direct way to remove them, as the hook references are lost. This means: **Iterate Over All Modules to Remove Hooks**
        
    - ✅ since `outputs` is a list of actvs, in `get_410m_weights_and_acts_byLayer` change to `orig = sae.pre_acts(outputs[layer_id].to("cuda"))`
    - ✅ test on L5 vs L12 first
        - filters junk keywords from 65k to 32k
        - without 1-1, only gets 0.07 svcca paired.
            - these are around the same value as res stream vs mlps
        - 1-1: does slightly better with 0.09 svcca paired.
    - loop A(4, 8) and B(10,14)
        
        get similar results
        
- ✅ A vs ManyB
    - flip order of corr args
    - change junk filt keyw to `for feat_A, feat_B in enumerate(max_corr_inds):`
    - change 1-1 to `kept_modB_feats` (since counter counts the numbers of the manyBs that appear for each A) and use `if ind_B in kept_modB_feats:`,`elif ind_B not in seen:`, `seen.add(ind_B)`
    - change filt by corr val to `val = max_corr_vals[ind_A]`
    - change denom: `print("% unique after rmv 0s: ", num_unq_pairs / reshaped_activations_A.shape[-1])`
    - RESULTS: get similar results
- ✅ NOTE: manyXto1Y : the “many” is the first arg in `batched_correlation`
    - the “many” are the values in `max_inds`, while the “1” are the indices of `max_inds`

ICLR Reviews

[ICLR review links](Project%20Planning%20b4b05f73d85e409f8409b209e44ed692/ICLR%20review%20links%20143afed922dc80139337c6c22f0b96ef.md)

- ✅ ask max if svcca perm invairant
    - [https://chatgpt.com/c/673ba470-e414-800c-b71b-0d17bb0b0029](https://chatgpt.com/c/673ba470-e414-800c-b71b-0d17bb0b0029)

Cross Model Sim (diff tokenizers)

[Brainstorm Corr by Words](Project%20Planning%20b4b05f73d85e409f8409b209e44ed692/Brainstorm%20Corr%20by%20Words%20141afed922dc80178fceef8e3b4d9f37.md)

- ⚠️ [crossMod_diffTok_eleutherLib.ipynb](https://colab.research.google.com/drive/1Zv5ZLTjBJSsVsYjWu9ZB9QRDb8jXgj6D#scrollTo=VXWnUA_i652g)
    - ✅ get tokenization of entire prompt
    - ✅ get words of each prompt (separated by whitespace)
    - ✅ for each word group, group the tokens of the model into word
    - ✅ turn into fn to loop: for each word group, group the tokens of the model into word
    - ✅ for every prompt, split it and get total words
        - ✅ init an output matrix of size (totalWordsinAllPrompts, model_dims)
    - ✅ loop through every word’s token group and take its mean actvs, then add to new output
    - ✅ repeat for model 2 (pythia) and take corr
    - ✅ run for SAEs (both pythia)
    - ISSUE: a token is decoded as CO��, but the string is CO₂. how to fix this
        - temp fix: don’t use prompts that contain "₂"
- ⚠️ ISSUE: mean actvs doesn’t make sense bc it’s done by dims. so if dim 0 is high, but dim 1 is low, for token 1, that’s a direction. taking the dim of another token where dim 1 is low makes it a COMPLETELY DIFFERENT DIRECTION, destroying the “meaning”.
- ⚠️ crossMod_diffTok_gemma_VS_pythia.ipynb
    
    This will be hard as you need to manually debug every specific intricate bug case of tokenizers on text that don’t work with simple approach. Not elegant, and lots of “patches” case-by-case that may break with new cases, but as long as it works.
    
    - ✅ use 2 diff tokenizers
    - ✅ don’t use code to get samps as strs for both models. this will be diff dep on tokenizer. instead, the samps_as_strs (to get words, each assoc with its own “token group” length depending on the tokenizer) should be the original set of prompts
    - ✅ ISSUE: somehow there’s an error with grouping; word_so_far (concat decoding individual tokenIDs) doesn’t match original prompt. so use new fn. check if both tokenizers get output with same num of words
        
        [https://chatgpt.com/c/673d0d1f-dcc4-800c-8b40-70ea493b4ce0](https://chatgpt.com/c/673d0d1f-dcc4-800c-8b40-70ea493b4ce0)
        
        actually this tokenizes each individual word, which is wrong as you get different tokenization
        
        if you change it using “can you do it by still using inputs as an arg?”, and replace its hallucination with `word_ids = inputs.encodings[sample_id].word_ids`, the flattened lists of the two tokenizers have different lengths (number of words)
        
    - ✅ above has issues, so go back to using attempt 1. but this time, filter out junk words in sample text and don’t use them in token groups eitehr
        - ISSUE: each tokenizer makes inputs have 100 tokens max. But we used the entire prompt wihile inputs only has 100 tokens. the issue is that the prompt string split by words must be tokenizer agnostic.
            - SOLN: instead of splitting each by 100 tokens, split by 100 words (attempt 1b). THEN tokenize the entire dataset.
                - first get 100 words for every prompt, THEN tokenize. don’t tokenize each prompt within its own iteration in a loop. this is because this allows for padding, as each prompt will have different number of tokens but we need the input to have the same number.
    - ✅ ISSUE: why are no words added to `words_so_far`, and curr_tok_index goes to 100 (throws error)?
        - ✅ breakpoints triggered by “junk words present” aren’t triggered, so it’s not junk words triggering this skip
        - ✅ try breakpoint right after first addition to words_so_far. Perhaps the decoded_token is eompty  ‘’ ?
            - it IS added
        - ✅ so the previous words work. but once it gets to the `word` ”the”, there’s an error in which it’s not detecting it. check what’s next to this “Belgian” in original prompt
            - check outside of fn what each individually decoded token is. Maybe it’s differently individual decoded vs when it’s with others
                
                ```
                for curr_tok_index in range(0, 100):
                    tokId = tokens['input_ids'][0][curr_tok_index]
                    decoded_token = tokenizer.decode(tokId)
                    print(curr_tok_index, decoded_token)
                    curr_tok_index += 1
                ```
                
            - this shows that Belgian, at token index 40, is represented when decoded individaully. So breakpoint within fn at token index 39 to see what the word is so far. Does it match the word before “Belgian”, which is “a”?
                
                yes
                
            - now breakpoint in fn at curr_token_index = 40
                - also correct
            - SOLN: there’s TWO Belgians- one at index 40, and other at index 100 (which is word RIGHT AFTER “the”). This is because the token group for “the’ is already found, but the loop kept on going.
                - `len(all_prompts_tokenGroups)` is only 77 at this end, but it should be 100
            - we need to track which exct word we’re on. print each word and index up until bug breakpoint
                - we find it DOES get to the very end, but `all_prompts_tokenGroups` only has 77
            - SOLN: in `word_groups`, words are concatenated wrong, such as  `'night.CNN'` . This is because we shouldn’t just separate by space, but by period too.
            - still has error. trying printing word, AND every decoded token along with its token index
                
                in this format, the word should match the tokens that are below up (up to the next word). look for the discrepency
                
            - SOLN: the number of words is GREATER than the number of tokens because `maxseqlen` was used for BOTH words and tokens. But we should have more tokens than words. So when truncating the tokens, try using `2*maxseqlen`
            - ISSUE: doesn’t work for prompt 59 now
                
                It’s because each nonsense (discord username) word is broken into many tokens, as these nonsense words aren’t used as single tokens in vocab space
                
                - SOLN: `2*maxseqlen` isn’t enough. Do `3*maxseqlen`
        - ✅ ISSUE: now tokenizer_1 (gemma_2b, instead of pythia_70m) stuck
            - <eos> is added to word_so_far. This is all padding tokens.
            - so use  `'<eos>'` for junk_words
    - ✅ Attempt 1b solves the issue of “different number of words”- now both have same number of words
    - ✅ test svcca and mean corr for gemma_1_2b vs pythia-70m using mean of token actvs for tokens in each word
        - terribly low corr (0.25) and svcca no better than random (0.02)
        - `batched_correlation(word_dim_output_sae_2, word_dim_output_sae)` , where sae_2 is pythia70m with SAE of 32k, and sae is gemma_2b with SAE of 16k size. The inds are 16k, so there are multiple pythia70m features mapped to just one gemma_2b feature. This makes more sense.
            - the results are better, with svcca of 0.12 compared to 0.002 from low random shuffling order.
            - 1-1 is not good
            - but mean max corr is very low. so this wouldn’t fly
    - ✅ sum actvs for tokens in each word, not mean
        - still terrible. almost no difference.

More models

- ⚠️ interp 410 MLPs top freq features to see what they detect
    - interp code: see `simSAE_pythias_70m_160m_interpret_manyTo1.ipynb`
        
        interpret the SAE latents in model A that map to the most latents in model B
        
        - ✅ due to mem issues, the outputs args are both ALREADY from a single layer. so we just need to use get_weights_and_acts() instead of get_weights_and_acts_byLayer()
        - ✅ this requires outputting variable `highest_corr_inds` to run `Counter` on
        - first try 1A_to_manyB (since B is 410m with 64k) at L5 vs L12 (halves of 12 and 24)
            - majority of matched features are 0
            - the most freq don’t seem to have high corrs. actually, few of these pairs have high corrs. perhaps MLPs just don’t do as well
            - intuition for this is that residual stream is more of a long term concept store and mlps do some specific calculations to advance specific concepts, but everything still comes back to the residual stream?
        - manyA_to_1B is slightly worse
    - ⚠️ if we filter out all corrs less than 0.4, the svcca is still only 0.02 (both many-1 and 1-1)
- ✅ 1AtomanyB vs manyAto1B for: pythia70m vs 160m, and gemma1 vs g2
    - ✅ already have manyAto1B (smaller is many)
    - ✅ [getScores_pythia_1AtomanyB.ipynb](https://colab.research.google.com/drive/1lpnuPdBfEAm_JcHXFRdUg07XUxDz3slg#scrollTo=eMXfdun7cOzB)
        - change 1) corre fn order, 2) inds order when filt nonconc, 3) “seen” in 1-1, 4) ind to get val when filtering vals
        - 1-Many RESULTS: similar to before, but different (eg. L1 and L2 matches better with L3) but middle is slightly worse
        - Thus, similar & good results, so no issue with switching order; jsut slightly different
- ✅ mlps of 70m vs 160m to rule out if mlps or 410m is issue
    
    simSAE_pythias_70m_160m_mlps.ipynb
    
    - i ran 70m and 160m for MLPs, and that too has low scores and the distribution of max actv correlation pairs is also skewed right with mostly low correlations (mean of 0.4). So 160m vs 410m should work if we can train SAEs on the res stream of 410m; it likely didn't work because 410m only has SAEs on MLPs
    - actually the results aren't as bad; I get svcca of 0.19 for a middle layer pair for 70m vs 160m, but svcca of 0.07 for 160m vs 410m (all MLPs). This is a magnitude higher than random pairings of ~0.003, but still lower than the score of 0.5-0.7 for res stream of 70m vs 160m
        - 1-1 only slightly better (0.195)
        - getScores_pythia_1AtomanyB has L3 v L5 as 0.4
        - but looping through other layers, is VERY low. between 0.04 to 0.19
            - 1A to manyB goes up to 0.23. So still better than 410m
        - some in 160m vs 410m aren’t so bad (L5 v L13 is 0.13)
        - perhaps features aren’t universal, but at least depending on degree of similarity of LLMs, one can find “a good amount” of similar feature subspaces

---

### To do

Cross Model Sim (diff tokenizers)

- sanity check: check if corr by word has similar SVCAA scores as corr by token
    - pythia-70m vs 160m
- try models closer in size, and with saes with same number of latents
    - should have at least high mean max corr
    - gpt2 vs pythia
- filter: if any token in group is non-concept?
    - filter out in both word groups and don’t add tokens that decode to ,
        - this auto
    - assumes tokens don’t have spaces in middle, only at start and end
- test for saes of pythia vs gemma
    - issue: pythia is eleuther, gemma is saelens
    - eleuther has llama3, with sae width of 4096*32 = **131072**
    - llama3-8b also much bigger outputs
    - pythia-70m-deduped is on saelens
- turn entire process into fns
- why corr of reverse actvs isn’t reverse inds?

Other expms

- does it make sense to apply SVCCA to sparse weight matrix? see how aligned directions (sum of col neurons, which are LLM inputs) are computed in original SVCCA paper
- hungarian algorithm for matching permutation features (search on Eleuther discord)
- there are multiple indp stat tests for each layer pair. but multiple comparisons isn’t an issue
    - assume it is an issue. this means among 5^2 = 25 tests, there’s only a 0.95^25 = **0.277 or 27% chance** that a false positive WON’T be found. So there’s a ~73% chance at least one of those layer pair tests is a false positive.
    - But, multiple comparisons is an issue if we’re “Testing different features in a dataset to predict the same dependent var”. IE) Tests that collectively address related research  hypotheses. Eg) Comparing the effectiveness of multiple drugs on the same outcome.
    - [say we have two neural networks. if we take latent space pairs for each of their layer pairs, and apply svcca on those layer pairs when pairing their neurons based on highest activation correlation VS randomly pairing their neurons, are these tests in the same "set" to beget multiple comparisons error, or are they different because each layer pair has its own dependent variable?](https://chatgpt.com/c/674c8301-0ea8-800c-bc70-015b2eb6a15e)
        
        This is an interesting scenario that hinges on how you define the "family" of tests and the dependencies between them. Here's how we can think about it in your case:
        
        ---
        
        ### **Are the tests in the same "set"?**
        
        ### **Key Considerations:**
        
        1. **Shared Context or Hypothesis**:
            - The tests (SVCCA on layer pairs with activation-based pairing vs. random pairing) are all addressing the same overarching question: "How do neuron pairings (activation-based vs. random) affect similarity as measured by SVCCA across layer pairs?"
            - This shared hypothesis suggests they could be considered part of the same set.
        2. **Shared Data**:
            - The tests all operate on the latent spaces of the same two neural networks, suggesting some shared underlying data structure (e.g., activations, layers).
            - This supports the idea of dependency, especially if patterns in one layer are likely to influence or be related to patterns in others.
        3. **Independent Variables (IVs) and Dependent Variables (DVs)**:
            - The **independent variable** (method of pairing neurons: activation-based vs. random) is common across tests.
            - The **dependent variable** (SVCCA similarity score) varies across layer pairs, as each layer pair might reflect a distinct relationship.
        4. **Nature of Dependencies Across Layers**:
            - If layer representations are independent of each other (e.g., activations from Layer 1 of Network A vs. Network B don't influence activations in Layer 2), the layer pairs might be considered independent tests.
            - However, neural networks often exhibit hierarchical and correlated layer representations, implying potential dependencies.
        
        ---
        
        ### **Are these comparisons subject to the multiple comparisons problem?**
        
        ### **Case 1: Same Set of Tests (Multiple Comparisons Issue Applies)**
        
        - If the overarching goal is to test a single hypothesis about neuron pairing methods (activation-based vs. random) **across all layers**, then the layer pairs form a "family" of tests.
        - In this case, the tests should be treated as part of the same set, and multiple comparison corrections (e.g., Bonferroni, FDR) are warranted to control for inflated Type I error.
        
        ### **Case 2: Different Sets of Tests (No Multiple Comparisons Issue)**
        
        - If each layer pair is conceptualized as addressing a separate hypothesis (e.g., "How does neuron pairing affect SVCCA in this specific layer pair?"), then they are independent tests.
        - Multiple comparisons corrections might not be needed because each test has its own dependent variable.
        
        However, this approach assumes:
        
        - The layers are independent (which may not hold for neural networks).
        - The results for one layer pair don't generalize to others (a more exploratory perspective).
        
        ---
        
        ### **Practical Recommendation**
        
        Given the hierarchical structure of neural networks and the likely dependencies across layers, it is safer to assume that:
        
        1. **The tests belong to the same set**: You're testing the same hypothesis (activation-based vs. random pairing) across multiple layers.
        2. **Apply Multiple Comparisons Correction**: To account for the family-wise error rate across layer pairs.
        
        ### Suggested Steps:
        
        1. Treat all layer-pair comparisons as part of a single "family" of tests.
        2. Use a multiple comparisons correction method appropriate for your context:
            - **Bonferroni Correction**: Very conservative, ensuring a strict Type I error rate.
            - **False Discovery Rate (FDR)**: Less conservative, suitable for exploratory analysis with many tests.
        3. Report both corrected and uncorrected results for transparency.
        
        ### Alternative:
        
        If you argue for treating each layer as an independent hypothesis:
        
        - Clearly justify this in terms of the independence of layers and the specific research question.
        - Be cautious of potential interdependencies that could lead to underestimating the Type I error rate.
        
        ---
        
        ### **Summary**
        
        In your case, it’s likely best to assume that the tests across layer pairs belong to the same set, as they share a hypothesis, dataset, and context. Applying a correction for multiple comparisons ensures the robustness of your conclusions, particularly when reporting differences between activation-based and random pairings across layers.
        
    - so if the hypothesis was "does ANY layer have similarity", it would be multiple comparisons, but if the hypothesis was "does this specific layer pair have similarity", it wouldn't be?
        
        Yes, that's a correct interpretation. The distinction hinges on the scope of your hypothesis and whether you're testing a collective property of multiple layers or an individual property for each layer pair. Let’s break it down:
        
        ---
        
        ### **Hypothesis: "Does ANY layer have similarity?"**
        
        - **Nature of the Hypothesis**:
            - This is a broad hypothesis that spans all layer pairs. You're asking whether at least one layer pair shows similarity.
            - Implicitly, this involves testing multiple layer pairs and aggregating the results into a single conclusion (e.g., "Layer  shows similarity, so the hypothesis is true").
                
                XX
                
        - **Multiple Comparisons Issue**:
            - Because you’re effectively running many tests (one per layer pair) to draw a single conclusion, you must control for the inflated risk of a Type I error (false positives).
            - Without correction, there’s a high chance that one of the tests will yield a significant result just by chance.
        - **Correction Needed**:
            - You should apply a correction for multiple comparisons (e.g., Bonferroni, FDR) to ensure that the overall conclusion about "any layer" remains statistically valid.
        
        ---
        
        ### **Hypothesis: "Does this specific layer pair have similarity?"**
        
        - **Nature of the Hypothesis**:
            - This is a focused hypothesis about one particular layer pair. You're not aggregating results across multiple layers to draw a conclusion.
            - Each test is treated as an independent investigation into the similarity of that specific layer pair.
        - **Multiple Comparisons Issue**:
            - Since the hypothesis is layer-specific and doesn’t depend on the outcomes of other tests, the multiple comparisons problem doesn’t arise.
            - Each test can be evaluated independently using the standard significance threshold (, for example).
                
                α=0.05\alpha = 0.05
                
        
        ---
        
        ### **Key Takeaway**:
        
        - **Hypotheses Across Layers (Any Layer)**:
            - When combining or aggregating results across layers to answer a broader question, you need to correct for multiple comparisons to avoid inflated error rates.
        - **Hypotheses Per Layer (Specific Layer)**:
            - When each layer pair is treated as its own, independent hypothesis, you don’t need to apply corrections for multiple comparisons.
        
        ---
        
        ### **Practical Example**:
        
        ### **Case 1: Broad Hypothesis ("Does ANY layer have similarity?")**
        
        - Tests:
            - Layer 1:
                
                p=0.01p = 0.01
                
            - Layer 2:
                
                p=0.04p = 0.04
                
            - Layer 3:
                
                p=0.08p = 0.08
                
        - Conclusion Without Correction:
            - At least one layer () shows similarity, so you conclude the hypothesis is true.
                
                p<0.05p < 0.05
                
        - Corrected Conclusion:
            - After Bonferroni (), only  remains significant. You conclude that the hypothesis holds, but only for Layer 1.
                
                αadjusted=0.05/3=0.0167\alpha_{\text{adjusted}} = 0.05 / 3 = 0.0167
                
                p=0.01p = 0.01
                
        
        ### **Case 2: Specific Hypothesis ("Does Layer 1 have similarity?")**
        
        - Test:
            - Layer 1:
                
                p=0.01p = 0.01
                
        - Conclusion:
            - No correction is needed since the hypothesis is specific to this layer. You conclude that Layer 1 has similarity.
        
        ---
        
        ### **Nuance to Consider**:
        
        Even when testing specific layers:
        
        - If you later compare these results across layers (e.g., "Layer 1 has similarity, but Layer 2 does not"), you’re implicitly aggregating across layers. This reintroduces the multiple comparisons issue, requiring adjustments for such comparisons.
        
        Being clear about the scope of your hypothesis and analysis plan upfront helps avoid post-hoc reinterpretations that could lead to misdiagnosis of multiple comparisons issues.
        
    - should bonferroni correction be used?

---

### Optional

[https://www.alignmentforum.org/posts/TMAmHh4DdMr4nCSr5/showing-sae-latents-are-not-atomic-using-meta-saes](https://www.alignmentforum.org/posts/TMAmHh4DdMr4nCSr5/showing-sae-latents-are-not-atomic-using-meta-saes)

for general interp rebuttals:

is not paradolia because instead of just being patterns that “look like” something (eg. a face in a cloud), these activations, which activate on specific inputs, are CAUSALLY responsible in a calculation of the output. also, ablating them causes a change. why would those specific ablations, as opposed to random ablations, cause this?

Writing (extra)

- only show category keywords that actv on at least one feature
    - but this is different for each layer pair?
        - perhaps take union?
            - when running this check, skip random runs in new nb copy
- 3 feature pair (top 5) interpretatations of L3 vs L5 in appendix
- 1-1 vs many-1 heatmaps on one fig
- add “DO DIFFERENT NEURAL NETWORKS LEARN THE SAME REPRESENTATIONS” to related work
- embeddings in intermediate laters accumulate contextual information, so they get more “meaningful” in relation to the context of other words in prompts, as opposed to individual tokens

Train SAEs

- https://modal.com/docs/guide/gpu
- GPT-2 Medium, or GPT-2 small variant
- finetune a LLM then train SAE

vs LLMs

- run on LLMs (MLPs)
    - we cannot remove “puncutation specific” LLMs bc that’s prob all the neurons. still try this anyways
    - make heatmap
- perhaps put LLM comparison in appendix, along with many-1 for both llms and saes
    - appendix I: LLM 1-1
    - appendix II: LLM and SAE (many-1)
    - not directly comparable; score should be compared relative to randoms. so don’t put llm and sae on same bar plot
        - also, vastly diff number of neurons
- LLM vs SAE top activating neurons
- hook: use transformerlens

Semantic subspace

- unrelated words
- rand sel corr pairs from entire matrix for size 200 and size 30
- filter keywords to be one token only

Umap semantic space

- umap of non-concept features: color them by category (punc, newline, etc)
    - see if they’re scattered or clustered. if scattered, would make sense why removing them also removes noise
- future work: umap of clusters across models to find semantic categories
- get top tokens and find list of non-concept words? how to do this?
- sometimes models learn the same feature
    
    ![image.png](Project%20Planning%20b4b05f73d85e409f8409b209e44ed692/image.png)
    

More models

- try attention layers only
- gemma: 9b is way bigger than 2b, while
    - 2b has 25 VS 9b has 42
    - very slow to get output, so try using cuda
    - moving model to cuda uses 10GB
    - use transformerlens to only get one hidden state at a time
    - many B to 1 A
        
        to find junk words one way is to look at the top tokens by interpreting the features with most number of matches using sorted_feat_counts
        
        i also think perhaps right now correlation is done for manyAto1B for 2B vs 9b. But perhaps 9B is so much bigger than 2B that it makes a difference to use manyBto1A, which means switching the args in correlation(). But this may take too long to try
        
        this means instead of `for feat_B, feat_A in tqdm(enumerate(highest_correlations_indices_AB),` we'll have `for feat_A, feat_B in tqdm(enumerate(highest_correlations_indices_AB),`
        
        actually i only needed to change 3 lines to (as described above; last line is just storing unique number of Bs) to make it manyBto1A
        
- appendix: force 1-1 to expand more

<<<

- overall to-do list (just #1 is needed; #2 and rest are extra)
    1. full space pval expms for TS and Pythia (they use diff sae fns)
        - extra: 1L toy model, gemma2
            1. find 1L online
            2. types of toy models: general or specific?
    2. subspace expms
    3. re-run expms using more data
    4. feature spliting
        1. train own saes on tinystories
    5. ground truth expms
    6. func expms (attrb vector for >1L?)
- main results needed
    - table col metrics
        1. num_feat_kept
        2. mean_actv_corr_filt
        3. 1-1 svcca
        4. svcca mean of randomly SHUFFLED features `shuffle_rand()`
        5. svcca pval vs null distrb of randomly SHUFFLED features
        6. 1-1 rsa
        7. rsa mean of randomly SHUFFLED features `shuffle_rand()`
        8. rsa pval vs null distrb of randomly SHUFFLED features
    - types of runs
        1. repeat all of the "table col metrics" for LLMs of every layer
        2. models: trying running on as much data (tokens) as possible
            1. tinystories (1l vs 2l)
            2. pythia 70m vs 160m
            3. gemma2: 2b vs 9b OR gemma1 vs gemma2
            4. 1L toy model
    - optional types of runs
        1. instead of pairing manyAtoB, `batched_correlation(reshaped_activations_A, reshaped_activations_B)`, try pairing from manyBtoA, which is `batched_correlation(reshaped_activations_B, reshaped_activations_A)`
        2. a “expand 1-1” that I’m working on: after 1-1, for those that are many-1, pair them with other unpaired features (eg. second highest)
        3. WxA, for only 1000 tokens (takes too long to run for more tokens)
    - tinystories files
        - save_LLM_w_actvs_c_proj.ipynb : this is metrics code to compare LLMs
        - jaccard_subset_ts_1L_2L.ipynb : this is metrics code to compare SAEs
    - austin plan for sim metric runs
        
        i'm looking to record: num features after filtering, mean actv score after filtering, svcca paired 1-1 + unpaired (random selection) 1-1.There's some variations you can also do if you have time:
        
        1. running everything again, but pairing from manyBtoA instead of manyAtoB (just switch the order in the batched_corr() function)
        2. getting 10-1 or 100-1 (wouldn't use the default many-to-1 before filtering as it's bad). just change the threshold in the filtering line "kept mod A feats"
        3. right now the rand function selects a subset of unpaired featuers of the same length as the filtered feature number. you can also do shuffling of 100 to 1k random runs. this is the code:
        - code
            
            `import randomdef shuffle_rand(num_runs, weight_matrix_np, weight_matrix_2, num_feats, sim_fn, shapereq_bool):    all_rand_scores = []    for i in range(num_runs):        row_idxs = list(range(num_feats))        random.shuffle(row_idxs)        if shapereq_bool:            score = sim_fn(weight_matrix_np, weight_matrix_2[row_idxs], "nd")        else:            score = sim_fn(weight_matrix_np, weight_matrix_2[row_idxs])        all_rand_scores.append(score)    return sum(all_rand_scores) / len(all_rand_scores)`
            
        
        so in all the automated runs, you can include that rand shuffling in the pipelline. for 1) and 2), you can just take the code after running everything else, and if you have time, you can just change a few lines to run again.
        
- other things to do
    1. Find 1L toy models anywhere that differ by rand init
    2. efficiently / cost effectively get mean actv corr svcca, rsa, jaccard score (and other items in dictionary) vs pval of 100 runs for the following pairs for both LLMs and SAEs:
        1. tinystories MLP0 vs TS-2L MLP0 and MLP1: adapt to this code: `simSAE_pythias_70m_160m_moreMetrics_v2.ipynb`
        2. every pair of 70m vs 160m: `simSAE_pythias_70m_160m_moreMetrics_v2.ipynb`
        3. also num + mean corr after filtering (non 1-1) to show isn’t too much that’s filtered
        4. we want to do this for a lot of tokens
        5. the pvals take a long time (would help if can parallelize)
            1. maybe tweak how pvals appear on bar plots?
            2. generate llm and sae plots side by side instead of manually making them side by side
        6. jaccard nn is optional (may just use svcca, possibly rsa) but would help if speed up perhaps by batching
        7. also, later I’m making another procedure that does 1-1 for more feature pairs, so may want to re-run all this for that. so organize code as functions to easily re-run things with small tweaks
    3. taking svcca, rsa, etc similarity of feature activations transposed and matched for variations of tinystories + pythia for both LLMs and SAEs
        1. `sae_crossModel_sim_explora / jaccard_subset_ts_1L_2L.ipynb` ; section “**jaccard on token actvs” → “by corr features”**
            1. `jaccard_similarity(reshaped_activations_A.t()[highest_correlations_indices_v1], reshaped_activations_B.t())`
            2. adapt to `simSAE_pythias_70m_160m_moreMetrics_v2.ipynb`
        2. actually this may be too trivial bc we already correlate by activations so what would be saying?
        3. aslo try this for not transposed but then not using correlated indices bc now the input tokens are already paired
    4. Est training toy models on toy dataset
        1. tinystories 1M vs 3M didn’t yield good interpretations, so maybe this isn’t good
    5. how to simulate activations of two different language models for ground truth features
        1. [https://www.lesswrong.com/posts/z6QQJbtpkEAX3Aojj/interim-research-report-taking-features-out-of-superposition](https://www.lesswrong.com/posts/z6QQJbtpkEAX3Aojj/interim-research-report-taking-features-out-of-superposition)
        2. each LLM should use different ground truth features but also a shared subset; we want to see if they do share that subset
        3. maybe use different probabilities of selection for each model?
        4. issue from before: using 2 different set of synth activations to train to 2 saes just trained 2 saes on 2 actv sets from same model, instead of 2 diff models. so what would make the actvs diff? I think the above 2 tweaks may suffice.
        5. main point is to show LLMs are not similar this way, but SAEs are. so we need to “simulate” in synthetic data the neurons (var G) are not similar, but saes are. if we don’t show this, then don’t put this in paper.
    6. speed up pairing all features 1-1: simSAE_pythias_70m_160m_force1to1_v2.ipynb
        1. sort the flatened matrix to get highest value (6m)
        2. go through the list and find features (rows and cols of orig matrix) not used in pairings yet (takes around 20m)

Extras

- better bar plot (appendix?)
- conf intervals, variance
- see what 1-1 is removing for L2 v L3 pythia
- serch thru toptoks (labels) for EOS
- L0 and L25 in gemma2
- 100-1 after rmv nonconcp: gemma & pythia
- auto find which p-vals (layer pair, category) are below 0.05 in the table. pval histogram
    - the arg isn’t that is impossible, but most aren’t
    - for those that are, interpret them to see if monosem across models
- pval runs of 100 or 1000

More data for semantic

- one issue with the "not monosemantic features" is bc not enough data was used. i'm only using 30k tokens (numsamps * maxseqlen)- that's lower than the vocab size
    - sae-corr: retain max in batches. store maxval for each feat so far

- Write in Future work
    1. pair by semantic and functional
    2. LDA to approx subspace
        - cross-patch features in reconstructions using LDA approx, or some other transformation
            - while two LLMs use diff actvs, if their SAEs share similarities, perhaps we can transform one to another (not direct patching though, as SAEs still have diff basis)
    3. hier geom plots
        - use block matrices “Disentangling” paper or orth relns to show hier in one model, then show similar hier after pairing features. compare similarity of hier matrices.
    4. feature pairing algo based on scores
- move SVD expms to appendix
    - SVD vs SVCCA
        
        svd expms: find similarity between llms. but other sim metrics cannot be run due to perm pairing issues. sae offer soln to perm pairing problem that was not able to be done before.
        
        svd is sort of like perm pairing as it’s comparing the singular vectors, or principal components. but PCA requiers mean centering?
        
        svd and saes are sort of similar. but saes allow feature clustering and individual feature interpretability, along with jaccard. perhaps svd can also allow matching. svd is sort of like cca in that it matches highest canonical dirs? but why is svd invar to shuffling- is it?
        
        try svd after corr shuffling of sae features.
        
        try clustering singular vectors? also try matching singular vectors by the index?
        
        svd comps aren’t features though; not as interpretable
        
    - general linear groups change basis, so diff LLMs with  have diff basis
        
        [https://chatgpt.com/c/54c66219-4e07-4322-ab68-648e13d25cc0](https://chatgpt.com/c/54c66219-4e07-4322-ab68-648e13d25cc0)
        

Filtering (optional)

- when choosing max, make a mask for every feature pair of pairs that match on at least one keyword
- measure how many pairs have same keyword

Full space (optional)

- need both low pval AND far enough away from mean
- score_rand_corr: filter to only 1-1
    - may not need to bc this already has high likelihood of 1-1 for most
- interpret the many-1 of LLMs
- so each of the 2300 neurons has a corr ind pair, so when you pass the 2300 neurons into model B (which has 3500), it only selects 2300 of the 3500 (if you look at the LLM nb I sent you before this does this in run_expms)

- steps to check on model pair before proceeding
    
    for gemma:
    
    1. compare LLMs semantic subspace
    2. compare SAE semantic subspace
    3. LLMs many-1 and 1-1 entire space
    4. SAEs 1-1 entire space
    5. SAEs many-1 entire space (may be too slow, so lowest priority)
    
    for 1, do both many-1 and 1-1 for LLMs. for SAEs, also try both, but only 1-1 will prob work for saes
    
    for LLMs, try using top 5, top 30 and top 90 bc they're not sparse
    

Semantic Subspace Matching (optional)

- llm on approach 2
- B vs A and A vs B
- subcategories
- find which subspaces across models are in common
    
    entire space contains ALL SEMANTIC SUBSPACES, whereas random non-semantic subspace isn’t one. So entire space is like a sum of all semantic subspaces.
    
- match rand weights of same len to see if svcca has high score for any matrices of low num rows
- can we use the same tokenizer first layer embedding of the same model?
    - issue: which model
- we can measure semantics of one space. but what about across spaces?
- autolabel top 5 snippets for each feature
    - search samples for actvs specific to concept, auto label using gpt4. if so, add to dataset to get actvs
    - use autolabeling on entire fature space for each category (expensive, maybe not feasible)
    - autolabel snippets: try giving top dataset examples in chunks to chatgpt
- among the matches, have chatgpt assess if the dataset sample that matches uses the word correctly in context
- APPR 3: clean up the search fn using gpt4/claude auto labeling semantics
    - use many keywords related to a concept (number, numbers, etc)
- APPR _: put in tokens and get highest activation features in both, then compare features by actvs
    - this isn’t labeling, which is good for human eval but shaky. this is closer to actvs?
    - the diff of this and appr 1 is we’re using specific inputs that we know of
    - correlate featuers based on actvs
        - compare weight matrix or actv matrix?
    - how to find which data to use?
        - we can take the tokens in the actv matrix that just correspond to “she” and do sim metric on transposed WxA
- approach 1, but only keep those with a keyword in top 5
    - strict approach: it must be the same keyword. so when getting features A, you must filter if it matches the kw of current loop

Ensure it’s not high bc of same keywords

- *otpional*: only allow features if a certain number of keywords out of total group are hit; otherwise, too narrow (not monosemantic enough?)
    - this can be ‘manipulated’ as a parameters, as is sort of arbitrary (data param hacking)

Find categories (optional- mention in appendix?)

- to ensure matches, loop through top tokens of top5 dataset examples for every feature, and categorize them
    - try to use clustering
- brainstorm highly specific categories, with words that have little double meaning
    - music bands
    - 

Semantic matching issues

- brainstorm why it has issues
    - towrads monosem: when they match by DNA, is it matching by compounds? no bc it’s too specific
    - perhaps b/c SAES are not monosemantic, so can’t use subspaces, they’re not relaly matching by concept
    - check: of course matching by even random keywords gives similarity, because the features with more than one match will be similar to each other, thus “clustering together”
    - is it valid to apply svcca when number of samples is less than number of features
        - [https://chatgpt.com/c/66f20bd7-81d8-800c-878a-cab4cb0c38cb](https://chatgpt.com/c/66f20bd7-81d8-800c-878a-cab4cb0c38cb)

Check sim metric approach validities (otpional)

- svcca validity and on WxA
    
    [https://chatgpt.com/c/66e6c099-7c18-800c-8f6e-719af8607c34](https://chatgpt.com/c/66e6c099-7c18-800c-8f6e-719af8607c34)
    
    - i have two weight matrices from two models. i pair their neurons row-wise by highest activation correlation (both models take in the same set of tokens, and pair tokens to get pearson correlation). then, I take svcca of their weight matrices to get a score, and compare this to random pairings null distribution. is this valid?
        
        The approach you've described involves several steps:
        
        1. **Pairing Neurons Based on Activation Correlation**: You align neurons from two models by pairing them row-wise based on the highest Pearson correlation of their activations across the same set of tokens. This means you're matching neurons that behave similarly in response to the same inputs.
        2. **Applying SVCCA on Weight Matrices**: After pairing the neurons, you apply Singular Vector Canonical Correlation Analysis (SVCCA) to their weight matrices to compute a similarity score.
        3. **Comparing to a Null Distribution**: You compare this SVCCA score to a null distribution obtained from random pairings to assess significance.
        
        **Is This Approach Valid?**
        
        Overall, your method is conceptually sound, but there are important considerations to ensure its validity:
        
        1. **Pairing Neurons by Activation Correlation**:
            - *Validity*: Pairing neurons based on the highest activation correlation is a reasonable way to align neurons between models, especially when they process the same inputs.
            - *Considerations*: Ensure that the activation correlations are computed over a sufficiently large and representative set of tokens to capture meaningful neuron behaviors.
        2. **Applying SVCCA on Weight Matrices**:
            - *Standard Usage*: SVCCA is typically used to compare neural network **representations**, i.e., the activations, not the weight matrices directly.
            - *Validity*: Applying SVCCA to weight matrices is less common and may not capture the functional similarities between neurons as effectively as comparing activations.
            - *Considerations*:
                - **Alignment**: Since you've paired neurons based on activation correlations, their weight matrices are aligned in the sense that they correspond to similarly functioning neurons.
                - **Interpretability**: Weight matrices can be influenced by factors like scale and rotation, which might not directly reflect functional similarity.
                - **Alternative**: It might be more informative to apply SVCCA directly to the activation vectors of the neurons rather than their weights.
        3. **Comparing to Random Pairings (Null Distribution)**:
            - *Validity*: Comparing your SVCCA score to a null distribution generated from random pairings is a valid approach to assess the significance of your observed similarity.
            - *Considerations*: Ensure that the random pairings are truly random and that the null distribution is estimated with sufficient precision (e.g., using a large number of random pairings).
        
        **Recommendations**:
        
        - **Use SVCCA on Activations**: Consider applying SVCCA directly to the activation vectors of the neurons. This aligns with the standard use of SVCCA and may provide a more accurate measure of the functional similarity between the models.
        - **Analyze Weight Matrices with Caution**: If you prefer to analyze weight matrices, be cautious about the interpretability of the results. Weight matrices may not reflect neuron functionality as directly as activations due to factors like weight scaling and permutations.
        - **Ensure Proper Normalization**: Whether you use activations or weights, ensure that your data is properly normalized. For weights, this might involve accounting for differences in scale or applying techniques to make them comparable.
        - **Validate with Additional Metrics**: Supplement your analysis with other similarity measures or validation techniques to confirm your findings.
        
        **Conclusion**:
        
        Your approach is conceptually valid, especially the pairing based on activation correlations and comparing to a null distribution. However, applying SVCCA directly to weight matrices is unconventional and may not yield the most meaningful insights. I recommend applying SVCCA to neuron activations for a more standard and potentially insightful analysis.
        
    - what if I use highest activation correlation to pair neurons, but svcca compare matrices that are the neurons x activations of the same activations? is it redudndant to use svcca to get info when the highest activation correlation is already high for each pair, or is it nontrivial to say svcca may not always be high in this case just bc highest activ corr is already high?
        
        Your updated approach involves:
        
        1. **Pairing Neurons by Highest Activation Correlation**: You align neurons from two models by matching each neuron in one model with the neuron in the other model that has the highest Pearson correlation of activations over the same set of tokens.
        2. **Applying SVCCA on Neuron Activations**: You then construct matrices of neurons × activations (for the same activations) and apply Singular Vector Canonical Correlation Analysis (SVCCA) to these matrices.
        
        ---
        
        **Is Using SVCCA Redundant in This Context?**
        
        At first glance, it might seem redundant to apply SVCCA after pairing neurons by highest activation correlation because the pairing already maximizes the correlation at the individual neuron level. However, it's important to consider the differences between:
        
        - **Pointwise Neuron Pairing**: Matching neurons based on individual activation correlations focuses on local, neuron-wise similarities.
        - **SVCCA Analysis**: SVCCA examines the global structure of the neural representations by identifying shared subspaces in the high-dimensional activation space.
        
        **Key Points to Consider:**
        
        1. **Local vs. Global Similarity**:
            - *Neuron Pairing*: Captures **local** similarities between individual neuron activations.
            - *SVCCA*: Captures **global** similarities by considering the collective behavior of all neurons and how they contribute to the overall representation.
        2. **Redundancy Concerns**:
            - *Not Necessarily Redundant*: High activation correlation between paired neurons does not guarantee that the overall representational spaces are similar.
            - *SVCCA Provides Additional Insight*: By analyzing the shared subspace, SVCCA can reveal structural similarities or differences that are not apparent from individual neuron correlations.
        3. **Subspace Alignment**:
            - *Independent of Pairing*: SVCCA does not rely on neuron pairing; it considers the alignment of the subspaces spanned by the activations.
            - *Capturing Variance*: SVCCA identifies the directions in activation space that account for the most variance and compares these between models.
        4. **Possible Outcomes**:
            - *High Neuron Correlations but Low SVCCA Similarity*: Even if individual neurons are highly correlated, the overall structures could differ, leading to lower SVCCA similarity.
            - *High SVCCA Similarity*: If the models not only have high neuron-wise correlations but also similar representational structures, SVCCA would reflect this with a high similarity score.
        
        ---
        
        **Why SVCCA May Not Always Be High Despite High Neuron Correlations**
        
        - **Different Combinations of Neurons**: The same activations might be represented differently across models due to different combinations or interactions between neurons.
        - **Nonlinear Relationships**: Neuron-wise Pearson correlation captures linear relationships, but neural networks can represent information nonlinearly.
        - **Dimensionality Reduction**: SVCCA includes an SVD step that focuses on the most significant components, potentially highlighting differences not captured by individual correlations.
        
        ---
        
        **Conclusion**
        
        Applying SVCCA after pairing neurons by highest activation correlation is **not redundant**. While neuron pairing focuses on local, pairwise similarities, SVCCA analyzes the **global structure** of the representations. It can provide additional insights into how the models' internal representations compare at a subspace level, which might reveal similarities or differences not apparent from neuron-wise correlations alone.
        
        **Recommendations**:
        
        - **Proceed with SVCCA**: Your approach is valid and can yield meaningful information about the representational similarities between the models.
        - **Interpret Results Carefully**: If SVCCA similarity is high, it suggests that not only are individual neurons behaving similarly, but the overall representational geometry is aligned. If it's low, there may be structural differences worth investigating.
        - **Supplementary Analyses**: Consider additional methods like CKA (Centered Kernel Alignment) or probing tasks to further explore the similarities and differences between the models.
        
        ---
        
        **Summary**
        
        - Pairing neurons by highest activation correlation aligns neurons based on local similarity.
        - SVCCA analyzes global representational similarity by comparing the subspaces of activations.
        - Using SVCCA after neuron pairing is not redundant and can uncover deeper insights into model similarities.
        - High neuron-wise correlations do not guarantee high SVCCA similarity due to potential differences in overall representational structure.
        
        By combining both methods, you gain a more comprehensive understanding of how the models relate to each other at both the individual neuron level and the overall representational level.
        
    - what if I use highest activation correlation to pair neurons, but svcca compare matrices that are the neurons x activations of the different activations?
    - should you normalize before correlating?
        - you ALREADY DO THIS
- [does a pvalue of 0 mean we should use more samples in null distribution?](https://chatgpt.com/c/66e6c577-6664-800c-a4ef-0d3cc3a1a0d4)
- in python how calculate variance of a list of numbers to check if enough samples to get pvalue
- how to code finding if se stabilizes
- issue with p-value: those 1000 samples may not be more than the test value, but what if a “decent number” are still very close? what do I do with that?
- look more into rand perm to get null
    - [https://en.wikipedia.org/wiki/Mantel_test](https://en.wikipedia.org/wiki/Mantel_test)
    - [https://en.wikipedia.org/wiki/Resampling_(statistics)#Permutation_tests](https://en.wikipedia.org/wiki/Resampling_(statistics)#Permutation_tests)
    - [can correlation coefficient produce a scalar score for two matrices of samples, or is it just for two vectors (pair of two samples)?](https://chatgpt.com/c/66e4cde2-46b0-800c-9e76-70bce3bfc842)
        
        When you have matrices of samples—where each matrix represents multiple variables across samples—the concept of correlation expands but doesn't directly produce a single scalar score between two entire matrices.
        
    - if correlation coefficient doesn't produce a scalar score for two matrices of samples, just for two vectors (pair of two samples), explain what the "methods section" of [https://en.wikipedia.org/wiki/Mantel_test](https://en.wikipedia.org/wiki/Mantel_test) means when it talks about permuting rows of the matrices. how does permuting rows change corr coef of matrices if it's not even calculated bewteen matrices?
        
        [https://chatgpt.com/c/66e4d0f8-2ffc-800c-9c5e-7ba2c7a14ebf](https://chatgpt.com/c/66e4d0f8-2ffc-800c-9c5e-7ba2c7a14ebf)
        

<<<

LLM 1-1 issues

- recheck saes many-1 ; similar scores as LLMs, or worse?
    - [https://colab.research.google.com/drive/156uqWTBHqNEHXnE-2ZVgDrbIkxd9OQws#scrollTo=pBtmkHC38UOh](https://colab.research.google.com/drive/156uqWTBHqNEHXnE-2ZVgDrbIkxd9OQws#scrollTo=pBtmkHC38UOh)
    - low pvals, but paired score is 0.03 while rand is 0.003
- save_LLM_w_actvs_c_proj_MLP1.ipynb: why is 1-1 svcca a 0.98 correlation
    - check num unique in 1-1 after omit low scores
    - tinystories is prob already very monosemantic, so don’t use it
- run LLMs many-1 on more layers
- ⚠️ consider this: for full space, compare LLM and SAE on same plot WITHOUT random pairing; just show SAE is higher than LLM
    - LLM many-1 (AB) on more layer pairs: show even though we can find similarities for LLMs, SAEs are better
    - only do this if sae is higher than llms
    - put this before the others but in short section
    - ISSUEs: the LLMs are only good when many-1, but SAEs are only good for 1-1. we can’t compare many-1 to 1-1. wwe don’t even know which is valid ;we assume 1-1 is. but if we include 1-1 results for LLMs, if ppl try many-1 for LLMs, they find our claim about LLMs being ‘high pval’ is false. so better to just not include LLMs
- ISSUE: why LLMs work well for many-1 but not 1-1, while saes work well for 1-1 but not many-1. we have to choose just one type (either many-1 or 1-1) to compare them and I'm not sure if excluding many-1 makes sense. if both are included reviewers would say this is a flaw in methodology
- ask chatgpt- why many-1 sometimes high?

1-1 issue- extras

- instead of needing the best to be 1-1, just care about getting 1-1 more about getting the top matches. “good enough”
- simSAE_pythias_70m_160m_interpet_manyTo1
    - interpret the features which have many matches
        
        if not meaningful, then that means the reason they map to it is bc both are “low info”? but why high corr? WHAT are they correlated on? 
        
    - find a way to summarize this
        - autolabel?
- simSAE_pythias_70m_160m_force1to1_v2 : debug skipping over the already matched
    - not for all, just a few cases
    - if is fast enough, run on all pairs instead of just a few examples
- for many-to-1 featuers, get histo count of their col in corr mat to see what else they can map to
- measure semantic purity using auto labeling

Other sim metrics

- are ts 2L and 2L-nolyaernorm comparable?
- train on ts: ask author of “tinystories-2L, no layernorm” how long this took
- match by (weight x actvs) not just weight matrices
- figure out issue with why mlp 0 actv matrix is all 0s
    - is it just for 70m, or also for 160m?
    
- 1k sample stat tests (actually can just use 100 bc variance is low; get the var score)
    - [does this run on cpu or gpu automatically when you call it from a gpu run in colab:](https://chatgpt.com/c/43a1266d-1c47-49e4-ac9c-39a22f8338e3)
        - but doesn't svcca use torch tensor args?
            
            converts it to numpy though, doesn’t use pytorch operations
            
    - ask max for gpu svcca
        
        Hi, is the code (in particular, svcca, jaccard, procrustes and RSA) able to run on GPU? Would it be faster if it ran on GPU or not? I see that it takes torch as arg but use numpy operations instead of pytorch. I'm looking to run 1k to 10k randomly paired matrix sim metric runs to obtain a null distr for pval testing. Thanks!
        
    - run stat tests for all layers, not 1-1, and 1k rand samples
    - simSAE_pythias_70m_160m_statTests.ipynb
- simLLM_pythias_70m_160m_all_layers.ipynb : run without 1-1
- randsel 1-1 features and get avg
    - or just eliminate them to avoid this. state results are similar for what was investigated, and should be similar if investigated further
    - get distrb of this for both manyAto1B, and manyBto1A

---

OOM issues (otpional)

- ⚠️ ISSUE: for >400 samples, `feature_acts_model_A = sae.pre_acts(accumulated_outputs)`  -OOM, so do in batches the same way (not data loader, just slices of accumulated output)
    - ISSUE: even after doing this, still OOM at 400
- get rid of nonzeros before matching
- sparse matrix
    - only get nonzero inds
- avoid OOM of loading 2 models by doing this in separate nbs or runs
- even looping and del makes it OOM; so del the matrixx and clear cache doesn’t del everything?
- save large actv datasets by batches to prevent using a100. save batch, then del from mem, repeat

Extend results to more variations (1L toy model, etc)

- how to train multiple 1L toy models
- make fns to easily input other models, layers, data, etc.
- compare gemma2 2b vs 9b using saelens
- gemma1-2b vs gemma2-2b
- tinystories-2L, no layernorm
    
    I've commissioned a 2L TinyStories Model w/ no layernorm (Available [here](https://huggingface.co/noanabeshima/tiny_model/blob/main/tiny_model_2L_3E.pt)) to try to fully reverse engineer a small model w/ SAEs.There are two uncertainties:
    
    1. How to compute features from attn_in to attn_out? Currently seems unknown, even w/ QK-SAEs and Attn_out SAEs. If this isn’t true, please let me know!
    
    2. If we settle for just training on attn_out, we could train on activations before W_O, but I’m a major attention-noob and don’t understand what the benefits to interp would be.I also have a (really) rough draft of my specific proposed project [here](https://docs.google.com/document/d/1o3aV78jM30-yGxa964S8wXrI4YAm1bZzGy7uHYK3L1A/edit?usp=sharing) . In summary, train SAEs to sparsely reconstruct downstream SAE **features**
    
    (which Stefan told me an exact same idea, but from the first layer forward IIRC)
    
- vary LLM parameters, SAE dictionary sizes, and more
    - match saes with different dictionary sizes- what happens as you vary?
- use a heatmap of (paired,unpaired) ratios to compare all layer pairs
- try cca

Sim metrics- If have time:

- auto label interpretations and see if semantically matches too (they should)
- stronger sim metric tests
    - Rsa step 5 has p-val of rand pairings
        - bootsrap error bars
    - F score tests from feature fams
    - spearman rank correlation
    - soft match & procrutes normalized
    - send plots + code to max for checking validity
- compare not just pairwise models
- make sure ts and gpt2sm use same tokenizer by comparing their tokens
- LLMs with different tokenizers
    - Use phrase lvl for comon actv, not token. Get mean actv for all tokens in phrase. So map multiple tokens ro each other
        - Each sample index is not a dataset paragraph nor a token from flattening all, but a small phrase. Make this phrase using breakdown of samples? But now we can map using these indices by taking mean of all tokens in one index . This is like sum.
    - then gpt2 pretrained with pythia pretrained
        - compare using mean actvs of phrase
- gpt2 pretrained vs gpt2 med self-trained
- compare ts-1L with lincombo of ts-2L-MLP0 and ts-2L-MLP1
    - try just concat the features of 2L into one matrix then take corr with 1L
        - 16k 2L into 32k, then 8k 2L into 16k VS 16k 1L?
    - compare ALL features of GPT-2sm with ts-1L

---

Synth actv for sim metrics

- cluster data: see S3.1 of “Representation Topology Divergence”
- but note that the “highest corr features” not necc are from same cluster!
    - Plot and color those correlated GTF and SAE_A features on a umap. Are they in the same cluster?
- make sure synthetic activations themselves, not just the saes of them, have low jaccard. if not, then they’re not simulating well. each neuron NEEDS to be different in synthetic activations
- so each of the 256 neurons should use diff freqs in terms of decay. that means they cannot be aligned. their stats should be similar to what you find between actual LLMs.
- MMCS cannot be used for perm alignment unless it’s within same model- so we should expect it not to work when we truly simulate two diff LLMs? Then what do we use?
- luke used correlations such that every sample picks corrs according to one of the E groups. so in terms of feature corrs, many samples are similar to one another, if they belong to same group.
- umap hover for LLM_A, LLM_B, and ground truth- match A to GT and B, wlog for B.

- change luke’s code-other
    - add tqdm to sae training, but may use something else for synth actv
    - make decorative changes to new synth actv fn
        - use einops on synth data, split into 2 fns
        - must use batch, else too slow. find diff ways to do batch
        - use typing in args
        - data loader?
        - comment on why use `@dataclass`
        - make sure it gets similar results as old fn
    - make synth data (poss sae too) be part of class wrapper (see CAA rimsky)
        - class wrapper contains multiple actvs
    - make sure all get similar results as old nb
- 100mil samps for cluster data (need to speed up batch proc, else takes 5hrs)
- add to overleaf for later expms
    - some features learned by SAEs aren’t true features (no corr to GTF), though they have high sim to each other- identify these when comparing similarity of feature spaces!
    - plot sim between feature spaces (neigh of discrete features) vs sim of discrete features?
- make sure lin combos of ground truth features are different enough; if too similar, we get datasets that are too similar. Try diff freqs in each model to get properties specific to each LLM
- Features should be meaningful. Why can't hard code meaningful ones? That's synthetic.
    - can we hard code circles in?
- read more about “-taking-features-out-of-superposition-with-sparse”
    - https://www.lesswrong.com/posts/a4oPE4xJqkYSz6jMS/explaining-taking-features-out-of-superposition-with-sparse
    - https://www.lesswrong.com/posts/DezghAd4bdxivEknM/a-small-update-to-the-sparse-coding-interim-research-report
    - https://www.lesswrong.com/posts/8BEJKhgFekvoNEtHv/research-update-sparse-autoencoder-features-are-bimodal
- note which torch structs to pass ‘device’ and ‘dtype’ in to prevent torch incompat
    - dont put in before send code to luke (and dont mention); put in if he suggests

---

Feature splitting across LLMs

- Do they get more similar as they get bigger?
    - However, we find the 1-1 features to still give the best score; this may mean these features are more "canonical" in the LLM or the SAE, as the models both learn them as sae features, rather than splitting them apart.
    - We also utilize these methods to measure the similarity and "trajectories" of feature splitting across models (TBC- define trajectory as x-axis is SAE dictionary size, y-axis is metric).

---

Feature subspace matching by func sim

- for models that aren’t 1 layer, can we use attribution vectors?
- Functional sim of feats by ablate and steer
    - start with one type of ablation
- universal steering vectors: see if feature geometry (arrangement, hierarchy) is found across models
- towards mono: how they measured by ablation
    - fig : feature ablation and residual ablation
        
        ![image.png](Project%20Planning%20b4b05f73d85e409f8409b209e44ed692/image%201.png)
        
    
    [https://transformer-circuits.pub/2023/monosemantic-features#setup-interface](https://transformer-circuits.pub/2023/monosemantic-features#setup-interface)
    
- Disentangling Dense Embeddings: [https://arxiv.org/pdf/2408.00657](https://arxiv.org/pdf/2408.00657)
    
    “feature families” that represent related concepts at varying levels of abstraction. To
    demonstrate the practical utility of our approach, we show how these interpretable
    features can be used to precisely steer semantic search, allowing for fine-grained
    control over query semantics.
    
- quanitfy number of features to how good they are for steering. is there a correlation?
    - which features of the ones that highly actv are good for steering?

- ISSUE: if we reproduce this for individual features, it doesn’t do much diff than anthropic other than showing is reproducing to more models. but how do we do attribution for SPACES of features? perhaps just do individual.

---

### To do- October or later

May also do this in late sept and put it in appendix

Topo: mapper on llm vs saes using opt transp

- mapper on llm vs saes using opt transp
- mapper lens and color fn variations
- use mapper for functional ablation
    - find same months/etc structures?

Contact

- october: msg bricken, sharkey, to ask for ideas and potential collab
    - exploratory expms (incl with TDA)

Train sae on adv models

- find safety features
    - feature for trigger words- ask amir
    - [https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html#assessing-sophisticated-code-error](https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html#assessing-sophisticated-code-error)
    - [https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html#safety-relevant](https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html#safety-relevant)
    - Use [WMDP](https://www.wmdp.ai/) benchmark as dataset examples?
        - [https://arxiv.org/abs/2403.03218](https://arxiv.org/abs/2403.03218)
- fine tune two adv models from base model using diff datasets, see if they learn similar features? apply sim metrics to them.
    - fine tune own model
        - If you want to tune your own adversarial (if it means unsafe) llm, maybe you can try the redteaming subset of HH-RLHF dataset [https://huggingface.co/datasets/Anthropic/hh-rlhf/tree/main/red-team-attempts](https://huggingface.co/datasets/Anthropic/hh-rlhf/tree/main/red-team-attempts)
        - I asked a friend who are experienced in training adversarial model and he told me that he trained the model using 4chan corpus [https://github.com/niizam/4chan-datasets](https://github.com/niizam/4chan-datasets) . Additionally, he said that just vanilla soft would be enough and no special tricks are necessary.
- relations in diff fine tuned models from 4chan dataset?
    
    

Other sim metrics

- interpolate SAE
    
    [https://discordapp.com/channels/729741769192767510/1153431135414669422/1272249407349329920](https://discordapp.com/channels/729741769192767510/1153431135414669422/1272249407349329920)
    
    ![Untitled](Project%20Planning%20b4b05f73d85e409f8409b209e44ed692/Untitled.png)
    
- [https://en.wikipedia.org/wiki/Fréchet_inception_distance](https://en.wikipedia.org/wiki/Fr%C3%A9chet_inception_distance)
    
    Rather than directly comparing images pixel by pixel (for example, as done by the [L2 norm](https://en.wikipedia.org/wiki/L2_norm)), the FID compares the mean and standard deviation of the deepest layer in Inception v3. 
    
- [https://en.wikipedia.org/wiki/Wasserstein_metric](https://en.wikipedia.org/wiki/Wasserstein_metric)
- [https://discordapp.com/channels/729741769192767510/1153431135414669422/1268678877497131028](https://discordapp.com/channels/729741769192767510/1153431135414669422/1268678877497131028)
- [https://discordapp.com/channels/729741769192767510/1153431135414669422/1268681876151730264](https://discordapp.com/channels/729741769192767510/1153431135414669422/1268681876151730264)
    - just treating the SAE encodings a sparse vectors then measuring cos distance. nearest neighbors are both changed from the residual stream space as well as from SAE encodings of adjacent layers.
    - This is an expected result for me given feature splitting. You should be able to measure the cos-sim between individual feature's decoder direction, and also measure their joint jaccard sim (ie input similarity). You should be able to find many features that do point in similar directions but activate on disjoint inputs. The "disjoint inputs"/encoder is what determines your hidden activation.
    - You can have two mutually exclusive directions (ie cos-sim=0) read in from the same datapoint. Suppose we have two read-in vectors basis-aligned in 2D. These activate if a feature goes above some bias threshold (supposed it's >3 for both vectors) Then a datapoint of (100,100) will activate both features even though their encoder directions are mutually exclusive.
    - i'm using mutual-knn as my metric. my thinking was that it was possible that the SAE space was just a strange non-linear warping, but perhaps a consistent one. so in addition to looking at the preservation of NNs from residual stream to SAE space, I also wanted to do a quick check of two different SAE spaces. so i used two subsequent layers of residual space which were known to have high mutual-knn (90%+), then encoded both (with separate trained SAEs) into SAE space. But the high mutual knn also was lost in this scenario.
- [**On a Novel Application of Wasserstein-Procrustes for Unsupervised Cross-Lingual Alignment of Embeddings**](https://arxiv.org/html/2007.09456v2)
- https://opensourcemechanistic.slack.com/archives/C06RB35HBDE/p1725567550501229
    
    Yuds
    
    Yuds
    
    [4:19 PM](https://opensourcemechanistic.slack.com/archives/C06RB35HBDE/p1725567550501229)
    
    (Cross-posting from Eleuther's SAE discord channel for more reach, apologies for folks in both communities)I've been trying to figure out what are some intuitions behind qualitative evaluations of SAEs. One of the ways I've been looking at this problem is through geometry, already well explored in existing works.  Is the goal for the features:
    
    - to be more spread out, (not cluster together)
    - while still maintaining minimal reconstruction loss (both on the autoencoder and the LLM output)
    - while having as few dead latents as possible
    
    ?The "more spread out" function is from my reframing of the concept - if a feature vector is composed of latents which more spread out, then we are closer to disentangling the superposed features. Each spread out latent is ... more monosemantic (not atomic) than if the latent was part of a tight cluster.One metric I've seen capture this sense of "geometric interpretability" is MCS histogram (max cosine similarity) /MMCS (mean-max cosine similarity).So our requirement for training an SAE for more interpretability is:
    
    - histogram of MCS spread out (rather than peaky) + low MMCS
    - low FVU
    - low dead latent pct
    
    How does that problem framing sound?
    

Future ideas

- Train sae to capture hier abstract representation by encourage compression loss
- train an SAE on multiple LLM activations that finds the common features between them

[Analogous Steering extras](Project%20Planning%20b4b05f73d85e409f8409b209e44ed692/Analogous%20Steering%20extras%2096467b547ccb48cb96a94a05cb2aeb7f.md)

- **Cross-Domain Behavior Steering:** [https://docs.google.com/presentation/d/1ZyBKrnS_WgwItOFpDQhuHZHmVAB3MCUGlpod1gSyVlE/edit#slide=id.g2ce4bd20f45_0_676](https://docs.google.com/presentation/d/1ZyBKrnS_WgwItOFpDQhuHZHmVAB3MCUGlpod1gSyVlE/edit#slide=id.g2ce4bd20f45_0_676)
    - find “feature classes” (like the mod 10, or months, used by Gould et al) using Mapper
    - Shared abstract steering effects when ablating features in cluster and cluster continuum relation. May allow for “analogous steering”
        - This is within model and is a discovery by itself, albeit not significant by itself (blog post or interview proj, not paper.) Universally identifying steerable feature structures like f fams but generalized for more effects is paper worthy

---

Feature Mapping Algorithm

We devise an iterative algorithm to pair features based on similarity score. This algorithm is initialized by pairing features based on the three types of individual pairing similarities. Then it iteratively selects new candidate mappings, and checks if the score is increased. This algorithm allows us to find feature subspaces that are highly similar to each other.

---

Read papers

- https://transformer-circuits.pub/2024/july-update/index.html#linear-representations
- [https://transformer-circuits.pub/2022/solu/index.html](https://transformer-circuits.pub/2022/solu/index.html)
    
    In this paper, we report an architectural change which appears to *substantially increase the fraction of MLP neurons which appear to be "interpretable"*
    
- Steering theory
    
    https://x.com/ravfogel/status/1814318728491815228?t=lGO6Hq9IbIoRESoMo72Psw&s=19
    
- SVD: [https://www.apolloresearch.ai/research/the-local-interaction-basis-identifying-computationally-relevant-and-sparsely-interacting-features-in-neural-networks](https://www.apolloresearch.ai/research/the-local-interaction-basis-identifying-computationally-relevant-and-sparsely-interacting-features-in-neural-networks)
- [https://www.lesswrong.com/posts/2roZtSr5TGmLjXMnT/toward-a-mathematical-framework-for-computation-in](https://www.lesswrong.com/posts/2roZtSr5TGmLjXMnT/toward-a-mathematical-framework-for-computation-in)
- Surpassing cosine sim: https://youtu.be/TOo7WE1oSJU?si=can2rSYiIZJsKono

To write

- conclusion: find alignment of “canonical safety-related features” between humans and AI- this is an avenue for alignment

Org notion

if impl succeed (whether neg or pos outcomes), copy todo into here and org into expms:

[Feature actvs on tinystories SAEs](Feature%20actvs%20on%20tinystories%20SAEs%208688850817e34618b8d9347574d66397.md) 

Code

- colab stuck in connecting during active session, refreshing doesn't help

---

TDA to find hier branching of gen to spec 

- hades

What Patterns to look for in Mapper

- mapper on adv exm SAE
- Distinguish different types of data. This comes from llama, this comes from gpt. This is specific to chat, this is specific to base. This is ablated, this is dangerous model.
    - compare mapper on dangerous LLM vs
        - inputs, features
    - list of dangerous/adversarial (fined-tuned, steered) vs safe model types
        - sleeper agents
        - poisoned
            - [https://telefonicatech.com/en/blog/attacks-on-artificial-intelligence-ii-model-poisoning](https://telefonicatech.com/en/blog/attacks-on-artificial-intelligence-ii-model-poisoning)
    - list of changed models
        - base vs chat
    - use similarity metrics + functional on model
        - SAEs measuring ground truth features as a sanity check on if these ‘universally dangerous feature relations’ are bc ground truth of dataset
        - are there canonical ‘ground truth’ dangerous feature RELATIONS?
    - feature splitting on dangerous types- can mapper detect using the SAE?
    - universal patterns in dangerous models vs safe models
        - universal bc “optimal” to represent feature relations this way
        - use feature relations to diagnose universally dangerous patterns
- ask, v1
    
    Hi, I’m looking for different kinds of “safe vs dangerous” models. I saw a paper called [“Visualizing and Analyzing the Topology of Neuron Activations in Deep Adversarial Training”](https://openreview.net/pdf?id=Q692Q3dPMe) that’s about distinguishing safe vs adverarial models using their activation topology. I’m looking to do the same for other types of recent “safe vs dangerous” models (not adversarially trained), but I’m not too familiar with what kinds there are. I’m aiming to extract activations from a base model vs one that has been fine tuned to become dangerous and compare them using a new combination of topological and functional interpretability techniques. 
    
- ask v2
    
    Hi, I’m looking for recommendations for open source pretrained adversarial LLMs (eg. poisoned with backdoors) that have both the base and adversarial version available. I saw a paper called [“Visualizing and Analyzing the Topology of Neuron Activations in Deep Adversarial Training”](https://openreview.net/pdf?id=Q692Q3dPMe) that’s about distinguishing safe vs adverarial models using their activation topology, but that paper uses vision models. I’m curious about trying this for adversarial LLMs. 
    
    I’m aiming to extract activations from a base model vs one that has been fine tuned to become dangerous and compare them using a new combination of topological and functional interpretability techniques. I can also fine-tune an adversarial LLM but I’m not experienced with this and don’t know the best research practices for doing so. 
    
    Also, is “adversarial LLM” the right term for this? I’m wondering about other types of “dangerous vs safe” LLMs that are available or can be feasibly fine tuned in a day or so.
    

- use saes trained on more steps & more ds exmps
- mapper on weights + actvs (actv labels are tokens)
- Look at existing papers to see what to look for
    - focus on interpreting results made by approaches of applied papers (neurosci, medicine, econ), not on theory of how algorithm works
    - put in presentation: a few notes (eg. 3 statements) on what to look for and cite previous papers (topoAct, neuroscience, etc)
    - 3 papers reading list
        - Extracting insights from the shape of complex data using topology: breast cancer, gene, house rep, nba
            - patients that were in Y survived
                - can we ablate those in a certain shape to change output? or conversely, only keep those there to keep output same, as opposed to ablating others?
                - can we identify those in common structure as the “common subspace” between models? are these features in the structure not found in umap?
        - monkey motor cortex: [https://jsseely.com/notes/TDA/](https://jsseely.com/notes/TDA/)
        - topobert: the inputs in a shape were adversarial
- sim scores: hypergraph coopt transp, MSID, geom score
- Find if steering/ablating features in a structure has an effect on output
- Color fns
    - Logit diff on certain output
    - Projection onto featyre, subspace mean, sterring vex, lda direction
    - Hierarchical or abstract concept that can be analogies
        - Find abstract concept and see how specific color with it after projection

why use mapper to find structures:

- steer by changing geometric configuration and observe output. this allows for more predictable steering
- feat fams: hierarchical feature structures with high correlation across datasets

---

umap inteartcitve

- [https://discordapp.com/channels/729741769192767510/1153431135414669422/1271789111430090762](https://discordapp.com/channels/729741769192767510/1153431135414669422/1271789111430090762)
    
    i used a webgl library called regl-scatterplot in my latentscope tool
    
    [https://github.com/enjalot/latent-scope](https://github.com/enjalot/latent-scope)
    
    but it's currently in an experimental branch for bringing SAEs into the process
    

***Figure 4 here (***svelte) contains subplots such that moving on one will move on the others: [https://pair-code.github.io/understanding-umap/](https://pair-code.github.io/understanding-umap/)

---

Ph

- code it and write up

https://youtu.be/5ezFcy9CIWE?si=iXnuCh52RAK3JiqG

https://youtu.be/2PSqWBIrn90?si=9WB9d7GY6mPfFLZg

https://towardsdatascience.com/persistent-homology-with-examples-1974d4b9c3d0

What if 2 struc have same b and d, how are they distinct pts on pers dia?

msg algtop phd/masters students

TDA tuning

- try diff parameters, clustering algo, projection algo (isomap)
- should you normalize data before?
- is edge strength based on num overlapping pts in clusters?

TDA analysis

- map and color corr points in clusters between mapper graphs
- search for features and color clusters across models
- auto find similar subgraphs across models
- label entire subgraphs (like Scaling Monosem)
- What’s the “path distance” from say the “one” community subgraph to the “.” community subgraph across models?

- [place cells: position lays on torus. dont want to end of coord system](https://www.nature.com/articles/s41586-021-04268-7)

[when comparing the similarity of two feature spaces in neural network activations to see if they learn similar feature relations, can we compare the subgraphs of their mapper graphs of their activations or weights?](https://chatgpt.com/c/370df1cc-39da-4416-8d86-15b4caf8d915)

[https://kepler-mapper.scikit-tda.org/en/latest/html-visualization-features.html](https://kepler-mapper.scikit-tda.org/en/latest/html-visualization-features.html)

How come we don't see circular months in umap with number features?

Train on small dataset sith king queen etc to ensure those are captured. Ask gpt etc if this makes sense

[https://dl.acm.org/doi/10.1145/3604433](https://dl.acm.org/doi/10.1145/3604433)

**Visualizing and Interpreting Bias Mitigation Techniques Geometrically for Word Representations**

---

Alt projects

Sim metrics, TDA, and func sim are NOT just for ‘across models’, but for feature splitting WITHIN a model. Map between SAEs. What properties of the manifold / simplicial complex change across feature splitting?

Also, WITHIN an SAE, can map analogous structures (eg. months to days, or king-queen to father-mother). Find similar subspaces within/across layers, mapping how they change over layers or during training.

(future work): These sim metrics / topological properties, once found and studied, may be used in loss functions to optimize the model towards learning certain beneficial topological arrangements

- cross-model feature subspace patching / model stitching

https://www.alignmentforum.org/posts/baJyjpktzmcmRfosq/stitching-saes-of-different-sizes

https://www.reddit.com/r/MachineLearning/s/dJhzCSX93r

Llms hallucinate alike

Train SAEs to learn specific, separate royal family features

- PLAN: our tools (corr, dataset exmps, umap, etc) have been shown to work. now, we need better datasets and models that show fs
    - once get better saes with fs concepts, color code multiple concepts- king queen princess- and check their relations across models
        - train on that specific data, on large sae, to ensure it learns them separately
- is top 5 tokens enough? maybe autolabel multiple. note that gpt4 fails at this. try paid cluade

---

UMAP

- umap plot pretrained gpt2 fs- sanity check, should match neuronpedia
- plot corr actv plots for feature split (or corr features)
- how to detect feature splitting, not just from umaps
    - get top 10 more corr from A to B, vice versa
- take most similar vectors and autolabel how similar their dataset examples are, rather than doing it manually
    - without chatgpt: +1 to score if contains same token in top 5, OR get how many of their top 5 tokens have same tokens
- in actv corr plot, show the dataset examples when hovering that are nonzero
- given corr feature pair, zoom-in on the umap of both
- compare MLP 1
- compare tinystories gpt2 to pretrained gpt2
- 🐣 neuronpedia: you can download the labels for their pretrained to use it yourself

[https://transformer-circuits.pub/2024/scaling-monosemanticity/umap.html](https://transformer-circuits.pub/2024/scaling-monosemanticity/umap.html)

[https://chatgpt.com/c/6b6bce5a-43c5-4b4e-8207-49d259712e4b](https://chatgpt.com/c/6b6bce5a-43c5-4b4e-8207-49d259712e4b)

Repr Sim

- before using cca, filter out features better
- mutual NN on weights and actvs? no; can only do on inputs (tokens)
    - if pts are features, perhaps we can’t use mnn. only makes sense if we plot the tokens in a projected down feature space.
        - indeed, algtop was applied on input pts, NOT neurons as pts! same with activation atlas!
- can cka be done on unpaired points in space? cca can, but mnn needs points that correspond to same input
    
    [https://claude.ai/chat/ef520765-10d0-4aed-8087-eaab5947af59](https://claude.ai/chat/ef520765-10d0-4aed-8087-eaab5947af59)
    
    [https://chatgpt.com/c/0f959dee-0a79-4333-b14d-8d0b130b658e](https://chatgpt.com/c/0f959dee-0a79-4333-b14d-8d0b130b658e)
    
    chatgpt is WRONG; it says cca needs paired. claude says doesn’t need paired.
    
- ask huh about why use knn over cka

- ISSUE: you’re including that feature as “activating on” that keyword if it contains it. But perhaps the majority of the top 5 (or top 10) should contain it

- use multiple keywords, each with different color
- instead of color, put a label box around the points in each plot

- in a box outside plot, display the other model’s pair
- compare subspace scores to random subspace pairs. ask chatgpt for how to better stat tests
- Then, higher-order graphs of keyword subspaces. It’s not enough to just plot the subspace of Dragon to subspace of Dragon; it’s the subspace of {Dragon, Princess}, as that’s relation of Dragon to Princess. Or {he, she}

- [I understand negative correlation between two variables. But what does negative CCA mean between two spaces of datapoints?](https://chatgpt.com/c/00acbbcb-2454-4246-a90c-33a4de7067e4)
    
    Canonical Correlation Analysis (CCA) is a method used to understand the relationship between two sets of multidimensional variables. When we talk about a negative canonical correlation, we're referring to the relationship between linear combinations of these sets of variables. Let's break this down:
    
    1. **CCA Basics**: In CCA, we have two sets of variables (let's call them \(\mathbf{X}\) and \(\mathbf{Y}\)). The goal of CCA is to find linear combinations of \(\mathbf{X}\) and \(\mathbf{Y}\) that are maximally correlated. Specifically, we seek vectors \( \mathbf{a} \) and \( \mathbf{b} \) such that the correlation between \( \mathbf{a}^T \mathbf{X} \) and \( \mathbf{b}^T \mathbf{Y} \) is maximized.
    2. **Canonical Correlation**: The canonical correlation is the correlation coefficient between these linear combinations. This correlation can be positive or negative. A positive canonical correlation indicates that when one set of variables increases, the other set tends to increase as well. Conversely, a negative canonical correlation indicates that when one set of variables increases, the other set tends to decrease.
    3. **Negative Canonical Correlation**:
        - When the canonical correlation is negative, it implies an inverse relationship between the linear combinations of the two sets of variables. In other words, the higher values of the linear combination of one set of variables (\(\mathbf{a}^T \mathbf{X}\)) are associated with lower values of the linear combination of the other set (\(\mathbf{b}^T \mathbf{Y}\)), and vice versa.
        - For example, if \(\mathbf{a}^T \mathbf{X}\) represents a particular weighted sum of the variables in \(\mathbf{X}\) and \(\mathbf{b}^T \mathbf{Y}\) represents a weighted sum of the variables in \(\mathbf{Y}\), a negative canonical correlation would mean that when the weighted sum in \(\mathbf{X}\) increases, the weighted sum in \(\mathbf{Y}\) tends to decrease.
    4. **Interpretation**: In practical terms, a negative canonical correlation suggests that there is an inverse relationship between certain linear features of the two datasets. Understanding this can help in fields such as finance (e.g., where one portfolio might hedge against another), biology (e.g., where certain gene expressions might inversely relate to others), and more.
    
    ### Example
    
    Suppose we have two sets of variables:
    
    - \(\mathbf{X}\): Economic indicators (e.g., interest rates, unemployment rates, GDP growth).
    - \(\mathbf{Y}\): Stock market indicators (e.g., stock prices, market indices, trading volumes).
    
    If we perform CCA and find a negative canonical correlation, it could mean that a particular linear combination of economic indicators (e.g., a scenario where interest rates and unemployment rates are high) is inversely related to a linear combination of stock market indicators (e.g., lower stock prices and trading volumes).
    
    In summary, negative CCA means that there is an inverse relationship between the optimal linear combinations of the two datasets, indicating that as one combination increases, the other tends to decrease. This can provide insights into the underlying structure and relationship between the two sets of variables.
    
- CCA and CKA on this feature subspace compared to other parts
    - the features in fairy tale subspace (is this too big of a subspace?)
    - use examples that are snippets specific to that subset
        - [https://chatgpt.com/c/1ed23e8e-b0a6-47b9-a3b4-1af35af41378](https://chatgpt.com/c/1ed23e8e-b0a6-47b9-a3b4-1af35af41378)
    - compare to random subspaces
    - compare to all of neuron (orignial LLM) space
    - CKA has issues; ask Huh et al if they use KNN over CKA bc over sensitivity of inputs (changing just one input can make repr be 0)
- search for token will highlight all features on both plots that activate on that token
- label clusters in umap, and map by sim across models
- compare feature-splitting features  on same umap like Towards M
    - use different dataset examples

[https://online.stat.psu.edu/stat505/book/export/html/682](https://online.stat.psu.edu/stat505/book/export/html/682)

---

Misc

- the feature mapping from A to B is the same as B to A bc corr matrix is symmetric

- search by featureID to highlight and zoom in on umap
- claude/gpt4 takes in neuronpedia html and reveng its gui

https://www.alignmentforum.org/posts/fmwk6qxrpW8d4jvbd/saes-usually-transfer-between-base-and-chat-models

- ISSUE: 2L MLP0 sae has many redundant feature neurons that all fire the same!
- find what are the tokens that are 0 in A but nonzero varying in B
    - Model B’s feature appears to fire on more tokens, possibly because it captures more concepts. That is, while these tokens are 0 in model A (1L-21M)’s feature 16251, model B (2L-33M)’s feature 3301 is nonzero for them.

- In 1L, there is no res stream, but in ≥ 2L, can train on other layers than MLP out like res stream

- for labeled umap decoder weights, how do labels change before and after steering?
- label features in mapper plot

Not really feature specific to daughter. Perhaps we can use feature splitting to constrain it to specifically fire for daughter?

- find related story features
    - get sentences just about: she-he-it
    - get sentences just about: princess-dragon-knight

---

[https://www.frontiersin.org/journals/systems-neuroscience/articles/10.3389/neuro.06.004.2008/full](https://www.frontiersin.org/journals/systems-neuroscience/articles/10.3389/neuro.06.004.2008/full)

[https://neuroai.neuromatch.io/tutorials/W1D3_ComparingArtificialAndBiologicalNetworks/student/W1D3_Tutorial1.html#](https://neuroai.neuromatch.io/tutorials/W1D3_ComparingArtificialAndBiologicalNetworks/student/W1D3_Tutorial1.html#)

[https://johnmarktaylor.com/research/](https://johnmarktaylor.com/research/)

https://arxiv.org/abs/2210.16156

https://datumorphism.leima.is/cards/machine-learning/measurement/centered-kernel-alignment/

https://openreview.net/forum?id=8HRvyxc606

https://medium.com/syncedreview/geoffrey-hinton-leads-google-brain-representation-similarity-index-research-aiming-to-understand-b5d14bf77f49

[https://www.youtube.com/watch?v=zZAj8uvr308&ab_channel=IEEESignalProcessingSociety](https://www.youtube.com/watch?v=zZAj8uvr308&ab_channel=IEEESignalProcessingSociety)

[https://www.damtp.cam.ac.uk/research/cia/files/teaching/Optimal_Transport_Notes.pdf](https://www.damtp.cam.ac.uk/research/cia/files/teaching/Optimal_Transport_Notes.pdf)

[https://openreview.net/pdf?id=ByxlnrBeLH](https://openreview.net/pdf?id=ByxlnrBeLH)

- [what's the difference between radius graph and simplicial complex to approximate manifold](https://chatgpt.com/c/895a75e2-9553-41c9-afe0-596ddd733bee)

should we average feature splitting sae instances?

How common are the same analogous patterns for the same dataset? Across datasets? Measure this

- ask chatgpt for help in defining feature manifold. give it overleaf so far

https://chatgpt.com/c/c50f49db-ff6f-4133-83a5-21593d3a2383

Sc manifold

https://youtu.be/wuqTOoKeVWw?si=VnrcVX2h82JH_Slo

Cka

https://youtu.be/uj0uQyJcrxY?si=Rv76ksM2mhzlc9bw

Transfer features 

- read: Not All Language Model Features Are Linear
    
    [https://chatgpt.com/c/d908b8ff-4c84-4002-a198-80956bdd7bd6](https://chatgpt.com/c/d908b8ff-4c84-4002-a198-80956bdd7bd6)
    
    - if the elements in the plot given from the paper are weights, how are the labels like Monday derived?
        
        The labels like "Monday" in the PCA plot are derived from the specific clustering of dictionary elements corresponding to days of the week, as discovered through the use of sparse autoencoders (SAEs) on language model hidden states. Here's a step-by-step explanation of the process:
        
        1. **Sparse Autoencoders (SAEs)**: SAEs are trained to decompose model hidden states into sparse vector sums from an over-complete basis. This means they can identify dictionary elements (features) that are activated by the model.
        2. **Clustering**: The dictionary elements identified by the SAEs are clustered based on their pairwise cosine similarity or Jaccard similarity. This clustering helps in grouping together elements that represent similar concepts or features.
        3. **Multi-dimensional Features**: The clusters that emerge from this process often represent multi-dimensional features, such as the circular patterns observed for days of the week. These clusters are then analyzed to ensure they are not mixtures or separable into lower-dimensional features, making them irreducible multi-dimensional features.
        4. **Interpretation**: Each cluster is interpreted and labeled according to the tokens that predominantly activate the dictionary elements in that cluster. For example, a cluster of dictionary elements that are primarily activated by tokens corresponding to "Monday" will be labeled as such.
        5. **Visualization with PCA**: PCA is used to reduce the dimensionality of these multi-dimensional features for visualization purposes. The resulting plot shows distinct clusters corresponding to the days of the week, which are labeled accordingly.
        
        In summary, the labels like "Monday" are derived by clustering the dictionary elements found by SAEs, which are then analyzed and interpreted based on the tokens that activate them, and visualized using PCA to show the circular representation of the days of the week.
        
    - cite the lines in the paper  that made you derive:
        
        The lines in the paper that support the interpretation and labeling of clusters according to the tokens that predominantly activate the dictionary elements in that cluster are:
        
        1. "This suggests a natural approach to using sparse autoencoders to search for irreducible multi-dimensional features:
            1. Cluster dictionary elements by their pairwise cosine similarity or Jaccard similarity.
            2. For each cluster, run the SAEs on all xi,l ∈ Xi,l and ablate all dictionary elements not in the cluster. This will give the reconstruction of each xi,l restricted to the cluster found in step 1 (if no cluster dictionary elements are non-zero for a given point, we ignore the point).
            3. Examine the resulting reconstructed activation vectors for irreducible multi-dimensional features, especially ensuring that the reconstruction is not separable. This step can be done manually by visually inspecting the PCA projections for known irreducible multi-dimensional structures (e.g. circles, see Fig. 2) or automatically by passing the PCA projections to the tests for Definition 3"【9:0†source】.
        2. "As described in Section 4, given a cluster of dictionary elements S ⊂ {1, . . . ,m}, we run a large set of activations through the SAE, then filter out samples which don’t activate any element in S. For samples which do activate an element of S, reconstruct the activation while setting all SAE features not in S to have a hidden activation of zero. If some collection of SAE features together represent some irreducible feature, we want to remove all other features from the activation vector, and so we only allow SAE features in the collection to participate in reconstructing the input activation"【9:2†source】.
        
        These lines explain the process of clustering dictionary elements based on their similarities and then reconstructing activations to identify and label irreducible multi-dimensional features.
        
    - cite pics
        
        ![Untitled](Project%20Planning%20b4b05f73d85e409f8409b209e44ed692/Untitled%201.png)
        
        ![Untitled](Project%20Planning%20b4b05f73d85e409f8409b209e44ed692/Untitled%202.png)
        

**generalize this procedure to find other structures: ablate by clusters (elements in simplices)**

Observe steering diffs on split features

Steer nonlinear months

Mapping algo: map based on both repr and func sim. May be a diffeomorphism or some other type of deformation mapping?

- toy model 20B token train feas
    
    ![Untitled](Project%20Planning%20b4b05f73d85e409f8409b209e44ed692/Untitled%203.png)
    

Questions

Why decoder weights are dictionary elements, not encoder

---

- to get LLM actvs, stream process LLM actvs on batch at a time, not loading entire dataset and passing into batch. same with SAEs. Do this to obtain feature acts for each batch_seq token.

[https://transformer-circuits.pub/2023/monosemantic-features#discussion-token-in-context](https://transformer-circuits.pub/2023/monosemantic-features#discussion-token-in-context)

this contains unanswered ques about [‘compositional codes’](https://transformer-circuits.pub/2023/superposition-composition/index.html#distributed-compositional)

[https://transformer-circuits.pub/2023/may-update/index.html#feature-manifolds](https://transformer-circuits.pub/2023/may-update/index.html#feature-manifolds)

what is length scale?

[https://transformer-circuits.pub/2024/june-update/index.html#multidimensional-features](https://transformer-circuits.pub/2024/june-update/index.html#multidimensional-features)

how many data pts does plot in Towards Monosem use?

ALgo to check if subspace is similar by matching one feature at a time and checking local score, then merging. Approx manifold using simplex

---

ISSUE: with arch sim. We expect same layer to have same features. That's the sanity check.

The issue is mapping features. Are they arranged in the same way?

https://chatgpt.com/c/8a2f7e89-5938-4dbd-88bb-2f031d88db16

At what point is feature splitting too dissimilar or does it get even more similar in certain subspace or feature groups?

Train sae to map between two models using cka loss. Finds features that both models have.

Ask to brainstorm ideas during meeting

https://youtu.be/TBjdvjdS2KM?si=KWVxjYkaNKmVSeVA

Use sim measures to diagnose healthy vs Wrong nn

Very wide network means all layers similar

We don't expect networks to have same exact features but they do have the same steering vectors and months representations. So something is similar. Can we find mappings?

---

- find tinystories across models with good features
    - map top 5 based on actv sim (corr and/OR cosine sim matrix)
    - manually look at pairs with high corr and use dataset examples to label them
- umap + cca on new saes of tinystories
    - actvs or weights in hinton paper? they’re actvs bc use exampls

- train saes at diff layers for multiple ts models ; then feature actv map & umap cca

---

- neg results: need to improve saes, or try diff layers, or try diff models
    - or could mean saes aren’t universal for certain cases. which cases? impt to know in order to figure out what could generalize
    - generalize: good for transfer learning, and using one model to predict another model’s landscape (eg. if mostly similar, can use one as a ‘map’ to guess impt steerable features of another model instead of needing to find them by trial/error)

⚠️ you can also just use Neuronpedia feature dashboards

- wandb metrics
- compile list of training tips from various resources
    - https://www.lesswrong.com/posts/FSTRedtjuHa4Gfdbr/attention-saes-scale-to-gpt-2-small
        - L0 norm changes at each layer of res stream
- Ask on MI, eluther, ARENA discord + slack for advice or pair prog for training SAEs
    - state have nb (may post it) or just state results
    - did X, etc. can it be even faster?
- ask others about comparing tokens of models with different tokenizers
- VPN

---

Multiple feature circuits

- are those features in a cluster/subgraph involved as a single component in a circuit?

---

### Future work

- **IMPT:** Within-models: also use cca on activations for analogous domains. this shows the abstract structure has “analogous” mappings from one domain to another. Like months and numbers.
    - LEVEL 1: The category is a higher-order structure (circles, simplices, etc)
        - Higher-order structures can just be pair-wise (2-simplex) relation between features (with “analogous” roles). This can be distance, or causal. 3-simplex: “father-mother-daughter”
            - each object is a cluster of points, or the LDA vector est of the cluster
            - Each edge is a vector addition or difference?
        - A simplex approximates a manifold subspace. So categories are subspaces.
    - LEVEL 2: The functor is a mapping between higher-order structures WITHIN-MODEL
        - Not just any triangle. But the idea that “man-woman-child” can be encoded in BOTH “king-queen-princess” and “father-mother-daughter”. Both contain this “man-woman-child” basis, and CCA may map these CVs. This “man-woman-child” is the common abstraction, or functor mapping, between the two categories.
            - The functor IS the analogy
        - If month clusters are arranged circularly, how are numbers mapped with them?
            - each data pt isn’t a month, but a feature weight (not actv)
        - Do circuits compose the functor structure with more specific features?
            - Might require several transformations into a space that cleanly shows this
    - LEVEL 3: The “natural transformation” maps functors (of structures) between models.
        - This shows universality of analogies, and how models converge to them

- cca intuition
    
    https://chatgpt.com/c/e7f60612-f476-4019-825e-d1d6f843748b
    
    CCA finds lin combo of features with highest correlation 
    
    So in cca say features man woman child, and father mother daughter, or king queen princess, are most correlated? Analogous?
    
    In cca can you find which combos map to each other, say if man woman maps to king queen, by coefficients basis
    
    So from cca coefficients can we get mapping of features to features based on their relns
    
    Not just two cv
    

https://chatgpt.com/c/cbecf63f-fe30-4804-a3a2-ae4cee00627d

Sparsity norms

Pretrained SAES: [https://github.com/EleutherAI/sae](https://github.com/EleutherAI/sae)

[https://wandb.ai/eleutherai/sae/runs/k1kn6lst?nw=nwusernorabelrose](https://wandb.ai/eleutherai/sae/runs/k1kn6lst?nw=nwusernorabelrose)

Train

- ask neuronpedia on advice for sae training

https://github.com/jbloomAus/SAELens/issues/191

[https://www.lesswrong.com/posts/5XmxmszdjzBQzqpmz/interpreting-preference-models-w-sparse-autoencoders](https://www.lesswrong.com/posts/5XmxmszdjzBQzqpmz/interpreting-preference-models-w-sparse-autoencoders)

can feasibly train saes on: tinystories (up to 4L), gpt2

[https://www.lesswrong.com/posts/f9EgfLSurAiqRJySD/open-source-sparse-autoencoders-for-all-residual-stream](https://www.lesswrong.com/posts/f9EgfLSurAiqRJySD/open-source-sparse-autoencoders-for-all-residual-stream)

- what's the estimated cost for training effective saes for all layers of gpt-2 medium?
    
    [https://chatgpt.com/c/78867e7f-511e-4a8d-b5fd-c05473c92f99](https://chatgpt.com/c/78867e7f-511e-4a8d-b5fd-c05473c92f99)
    

<<<

Compare

- compare actvs using narrow dataset (eg. only Arabic)

Feature space across models should be more similar than their neuron spaces

we’re not looking for true features based on below’s def, but similar representations that can transfer

[https://www.lesswrong.com/posts/QoR8noAB3Mp2KBA4B/do-sparse-autoencoders-find-true-features](https://www.lesswrong.com/posts/QoR8noAB3Mp2KBA4B/do-sparse-autoencoders-find-true-features)

https://youtu.be/TBjdvjdS2KM?si=moubTttOGY5hvCcK

Sim of nn lecture questions

https://chatgpt.com/c/d8492b87-728f-4abb-8bd5-3e4a9c522ec1

What was the impact of similarities of neural networks by Hinton? If it found models with different archs had same representations, did it allow generalizing features from one model to another? What important things did this paper lead to? How about its relation to mech interp?

Is it impactful to use their methods to compare feature representation spaces of sparse autoencoders trained on activations of different models? Or would the findings already br known from Hintons work?

Issue is next token, not input token. But try ones where both tokenizers use one tokens 

- matrix plot of cca for layer-layer similarity

[https://www.lesswrong.com/posts/FSTRedtjuHa4Gfdbr/attention-saes-scale-to-gpt-2-small](https://www.lesswrong.com/posts/FSTRedtjuHa4Gfdbr/attention-saes-scale-to-gpt-2-small)

This finds feature families. how similar are they across models?

[https://colab.research.google.com/drive/1hZVEM6drJNsopLRd7hKajp_2v6mm_p70?usp=sharing](https://colab.research.google.com/drive/1hZVEM6drJNsopLRd7hKajp_2v6mm_p70?usp=sharing)

This also has automated detection of feature families

[https://chatgpt.com/c/0faedc73-4b92-414b-b1d4-6ade923255df](https://chatgpt.com/c/0faedc73-4b92-414b-b1d4-6ade923255df)

- explain the L0 norm col of the table in:
    
    The "L0 norm" column in the table refers to the number of non-zero coefficients in the sparse autoencoder (SAE) representations. In this context, a lower L0 norm indicates that fewer features are being used to represent the data, which aligns with the goal of sparsity. Sparse representations are desirable as they make the model more interpretable by emphasizing the most important features. The table shows the L0 norm for different layers, indicating how many features are active in each layer after training the SAEs.
    

Don’t just focus on similarities; focus on differences. What parts are common to many, and how much is different?

Mapping clusters or higher-order structures is like mapping the subspaces

We’re also mapping circuits, which is not by geometry. And mapping steering vectors associated with circuits. DO the steering vecs and circuits map togther?

sum of contributions then unembed pca. heart higher-order structures: [https://neuralblog.github.io/logit-prisms/](https://neuralblog.github.io/logit-prisms/)

scaling monose actv plots explained:

[https://www.youtube.com/watch?v=8Nyn3_ZWa_U&t=721s&ab_channel=TheInsideView](https://www.youtube.com/watch?v=8Nyn3_ZWa_U&t=721s&ab_channel=TheInsideView)

<<<

- project proposal: (timestamped, ask fazl first before send to others)
    
    To show: Kiho, Bloom, Conmy, Trenton
    
    only reveal more novel (higher order, mapping, FS, etc) after initial meetings
    
    give expms code so far, and in email for initial meeting say have more novel approaches that can discuss later
    
    - experiments done so far
        - sae training setup (ghost grads, wandb, colab, torrnodes, etc)
            - feature splitting on gpt-tinystories
            - more than 2 models
        - why use CKA, etc.
        - higher-order structures and TDA
        - node mapping (reproduce Anthropic)
    - next steps: in-scope list of (justified) ideas and concrete plan to enact them
        - toy model (diff rand init): many saes
        - edge mapping algorithm (high-lvl; state details not shown here)
    - out-of-scope future work
        - analogous steering

- people to contact:
    
    (towards / scaling anthropic papers)
    
    ask fazl beforehand to ensure timestamp (no work leaks) [he knows who can be trusted as if they have incentive to not steal his work]
    
    8/20, code base distr sys: [https://boards.greenhouse.io/anthropic/jobs/4020305008](https://boards.greenhouse.io/anthropic/jobs/4020305008)
    
    - josh batson
        
        [https://www.youtube.com/watch?v=sQar5NNGbw4&ab_channel=Anthropic](https://www.youtube.com/watch?v=sQar5NNGbw4&ab_channel=Anthropic)
        
    - [https://www.trentonbricken.com/about/](https://www.trentonbricken.com/about/)
        - [https://www.youtube.com/watch?v=UTuuTTnjxMQ&ab_channel=DwarkeshPatel](https://www.youtube.com/watch?v=UTuuTTnjxMQ&ab_channel=DwarkeshPatel)
    - callum

- contact anthropic
    - started in july
    - they cite SVCCA. So they must’ve tried it. once you try your obvious cca approaches, ask them what issues there were with it, and if any issues with yours.
        - compare approaches; give pros/cons each
    - show them the mapping of higher order structures and working with kiho
        - eg) do they both arrange months circular? what other circulars found by algo?
            - can we map the circular structures?
    - toy model feature splitting: give cost estimates of llm and sae training
    - complexity of mapping algorithms

<<<

1. assumps + parameters for sim code for between saes
2. train saes on toy model
    1. get neuronpedia / eleuther to do this
    2. look for feature splitting
3. in another layer, track how a specific set of features (eg. love or cat) changes after steering
- funcsim: are two features across models also connected to analogous features in later layers?
- can you compare ground truth features as the intermediary? no- the "ground truth features" are model specific right, so it wouldn't make sense to see if two diff LLMs are learning the same ground truth feature
- train a model to map between features from two saes

<<<

Run code of “The Geometry of Categorical” on new data related to behavior

- email kiho on interpreting paper and checking if method to measure simplex based on orth relations is right
    - ask about comparing relations across models
    - ask if using TDA to identify simplex works
        - in a space of data point, how do I find which data points belong to an n-simplex, etc, using algorithms?
- brainstorm how to extend hierarchical concepts
    - steer by animal simplex
        - get convex hull that represents “animal” and add it?
            - how do you even add this?
            - estimate vector and convex hull using trained projection (LDA, linear map)- which to recommend?
- put face features thru existing code (geom, circ) on multiple models and look for hierachy (dog face and human face orthon) and other patterns
- find where hierarchy is detected in code nbs
    
    3_Noun_Heatmap.ipynb
    
    animal has cosine 1 with all others concepts bc they are all related to animal. but why 1, the max?
    

---

Steering circuits

- Probes to obtain “analogous steering vectors” across domains- apply these and observe the geometry
    - across models, find feature relation patterns that ‘explain’ analogous steering
    - the higher-order structures you find may be the  steerable “abstraction” common to a domain that you can extract and combine (eg. months with ordinal) from specific examples
    - or save for future paper
- [**Anthropic Beta Steering API**](https://docs.google.com/forms/d/e/1FAIpQLSc9HRcRFOdid4NJ4-Lyo3HdUybbevMqERWscJIbqilLQRuSQA/viewform)
- [The fact that both features contribute to the final output indicates that the model has partially predicted a sentiment from John's statement (the second feature) but will do more downstream processing on the content of his statement (as represented by the first feature) as well.](https://www.notion.so/Scaling-Monosemanticity-Extracting-Interpretable-Features-from-Claude-3-Sonnet-3219b222ee8943ac9ba1a07963f975b0?pvs=21)
    - Can we better formalize these causal relations between features?
- 80Gb instead of 40Gb for A100- vast ai may specify this
- automatically find steering vectors using dataset samples
- [https://www.lesswrong.com/posts/qykrYY6rXXM7EEs8Q/understanding-sae-features-with-the-logit-lens#Characterizing_Features_via_the_Logit_Weight_Distribution](https://www.lesswrong.com/posts/qykrYY6rXXM7EEs8Q/understanding-sae-features-with-the-logit-lens#Characterizing_Features_via_the_Logit_Weight_Distribution)
- [https://discordapp.com/channels/1080558777608183829/1229803194331304047](https://discordapp.com/channels/1080558777608183829/1229803194331304047)
- UNDERSTANDING AND CONTROLLING A MAZESOLVING POLICY NETWORK
    
    [https://arxiv.org/pdf/2310.08043](https://arxiv.org/pdf/2310.08043)
    
    decompose cheese vector
    
- saelens: train sae on gpt2-xl L20 and put steering vector through it, then interpret top features
- [**Scaling Laws for Dictionary Learning**](https://transformer-circuits.pub/2024/april-update/index.html#scaling-laws)
    - [https://transformer-circuits.pub/2024/april-update/index.html](https://transformer-circuits.pub/2024/april-update/index.html)
    - [https://transformer-circuits.pub/2024/april-update/index.html#ablation-exps](https://transformer-circuits.pub/2024/april-update/index.html#ablation-exps)
        - scaling features and observe behavior change
- [**Sparse Interpretable Features in Vision Transformers**](https://www.lesswrong.com/posts/bCtbuWraqYTDtuARg/towards-multimodal-interpretability-learning-sparse-2)
- Copy of HookedSAETransformerDemo.ipynb
    
    [https://colab.research.google.com/drive/1GlrX5K1LlZWrMWhr2EGCttqBIJ1jPrEn](https://colab.research.google.com/drive/1GlrX5K1LlZWrMWhr2EGCttqBIJ1jPrEn)
    
    why priveleged basis: [https://dynalist.io/d/n2ZWtnoYHrU1s4vnFSAQ519J](https://dynalist.io/d/n2ZWtnoYHrU1s4vnFSAQ519J)
    
- Llama2_TL_SAE_training_v1
- where are multiple feature vectors if steering vectors are an avg??

- Method to reduce dead neurons using loss constraints which force learned wright's to have activations be within useful feature range
- Steering is by prompts, not model. CMAP is by model. Compare them.
- [https://apartresearch.com/project/from-sparse-to-dense-refining-the-machiavelli-benchmark-for-real-world-ai-safety](https://apartresearch.com/project/from-sparse-to-dense-refining-the-machiavelli-benchmark-for-real-world-ai-safety)
- Study: https://github.com/nrimsky/CAA
    - is it 3rd last b/c adds end of seq token somehow in some operation? Find this operation
    

instead of deleting file, transfer new code into shared nb by deleting all old cells and pasting new ones from ‘select all’