# Done

[Find Research Topics + Prelim Expms](Done%201c002201437341e48b55b8276859a632/Find%20Research%20Topics%20+%20Prelim%20Expms%20cb0481999aa04ff6a92e5859837c3508.md)

**EXPM**: Observe how steering affects features downstream

- ✅ implement ‘see what steering at a layer affect other features’
    
    [https://docs.google.com/presentation/d/1uvM4LbpBnPav2dD-t55jDpedaIfhJbgpbV3GhJ_UyC8/edit#slide=id.g2ce4bd20f45_0_722](https://docs.google.com/presentation/d/1uvM4LbpBnPav2dD-t55jDpedaIfhJbgpbV3GhJ_UyC8/edit#slide=id.g2ce4bd20f45_0_722)
    
    **TODO:** change these features and measure how the steering vector performs in output and on benchmarks (latter may be noted as next steps when presenting)
    
    - plan detailed steps
        1. Difference of 2 contrastive prompts actvs at layer k of GPT-2
            1. do contrastive sets later
        2. For third prompt, apply steering vector at layer k
        3. Cache activations from layer k to last layer L for unst & steered runs
        4. Pass both those activations through their respective pre-trained SAEs
        5. Observe differences, before and after steering, for features from layer k to last layer L
            1. Obtain features via SAE, SVD, etc.
        - Later work
            1. Interpret features using dataset example labeling, unembedding methods (eg. logit lens), patching (for causal relations)
                1. Eg) Does the anger vector alter features related to anger?
            2. Generalize universal patterns across models and different classes of steering vectors (eg. vectors representing parent-child relations)
                1. Eg) The anger vector always alters F1 and F2, where F1 = P*F2, F1 activates on “fearful” and F2 activates on “threat”
            3. Patch back in feature ablated in later layers
                - Put SAE reconstructions back into model
                    - See: [GPT2_SAE_MLP0_seqcont_explora_v2](https://colab.research.google.com/drive/1fxFZynvhH0IkvE2WzUWUAqntQY4h7s5G#scrollTo=K-wGX_O3xaH9).ipynb
        
        ISSUE: how to identify analogous F1 and F2 across models?
        
    
    [gpt2Small_pretrained_steering.ipynb](https://colab.research.google.com/drive/1IUtIe0D6UBAJYlPC4eJl00l8fmpohhKG)
    
    This implementation simplifies away the wrappers that hide the fns to make it easier to understand the basics of the steering algorithms
    
    - ✅ STEP 1: get contrastive activations for 2 prompts of gpt-2
        - [hierConcepts_logitLens_llama2.ipynb](https://colab.research.google.com/drive/1sUeugm0DLrE_c8NAZy06XETeKdtwizWE#scrollTo=2UdLBhJPkFkf)
            - pass them both in batch, then take actvs of each batch index
    - ✅ STEP 2: For third prompt, apply steering vector at layer k
        - ✅ hook fn to add? look at prev repos how they did it
            - `activation_additions` (turner et al repo) \ `activation_additions \ hook_utils.py`
                - `hook_fns_from_activation_additions`
        - ✅ find also recent papers/blogs doing steering to see if they use easier way
            - [https://www.lesswrong.com/posts/ndyngghzFY388Dnew/implementing-activation-steering](https://www.lesswrong.com/posts/ndyngghzFY388Dnew/implementing-activation-steering)
            - ✅ ⚠️ TL ISSUE: `TypeError: act_add.<locals>.hook() got an unexpected keyword argument 'hook'`
                - Wrapper (using HF) ISSUE : `AttributeError: 'GPT2LMHeadModel' object has no attribute 'layers’`
                - `TL :`Try `run_with_hooks` instead of `add_hook`
                    - runwithhooks: GPT2_SAE_MLP0_seqcont_explora_v2.ipynb
                        
                        [https://colab.research.google.com/drive/1fxFZynvhH0IkvE2WzUWUAqntQY4h7s5G#scrollTo=tNWEV_Mn9z31&line=5&uniqifier=1](https://colab.research.google.com/drive/1fxFZynvhH0IkvE2WzUWUAqntQY4h7s5G#scrollTo=tNWEV_Mn9z31&line=5&uniqifier=1)
                        
                    - no; b/c can’t use runwithhooks with generate
            - ✅ `act_add.<locals>.hook()` issue isn’t due to adding steering vec, it’s the wrong way to add hook.
                - ✅ SOLN: try adding hook like this instead: auto_prompt_test_simple_arithm_v2.ipynb
                    
                    [https://colab.research.google.com/drive/13OodYS3_MB7mHGP-4r0zhVNF1nvhZJTk#scrollTo=dg3XuWScAVvG&line=11&uniqifier=1](https://colab.research.google.com/drive/13OodYS3_MB7mHGP-4r0zhVNF1nvhZJTk#scrollTo=dg3XuWScAVvG&line=11&uniqifier=1)
                    
                    - instead of doing this
                        
                        ```jsx
                        def act_add(steering_vec):
                            def hook(activation):
                                # return activation + steering_vec
                                return activation
                            return hook
                        
                        test_sentence = "I think cats are "
                        model.add_hook(name=cache_name, hook=act_add(steering_vec))
                        print(model.generate(test_sentence, max_new_tokens=10))
                        ```
                        
                    - do this
                        
                        ```jsx
                        from functools import partial
                        
                        def act_add(
                            activation,
                            hook,
                            steering_vec 
                        ):
                            # return activation + steering_vec
                            return activation
                        
                        hook_fn = partial(
                                act_add,
                                steering_vec=steering_vec
                            )
                        
                        cache_name = 'blocks.5.hook_resid_post'
                        model.reset_hooks(including_permanent=True)
                        model.add_hook(cache_name, hook_fn)
                        print(model.generate(test_sentence, max_new_tokens=10))
                        ```
                        
                - ✅ ISSUE: but when using steering_vec with hook, get : `RuntimeError: The size of tensor a (6) must match the size of tensor b (2) at non-singleton dimension 1`
                    - ✅ SOLN: unlike in the lesswrong post, you just take the LAST position, as seen here: [https://github.com/annahdo/implementing_activation_steering/blob/main/pytorch_hooks.ipynb](https://github.com/annahdo/implementing_activation_steering/blob/main/pytorch_hooks.ipynb)
                        - In repeng, it’s added to every tok pos?
                        - in caa blog post, rimsky states for generated, it’s added to every token pos after generation, but in initial prompt, it’s only added to last token pos
                    - ✅ though this works, in each gen it only modifies the NEW last token pos, not all of them after the initial prompt’s end
                        
                        ```jsx
                        steering_vec = steering_vec.unsqueeze(0)
                        
                        def act_add(
                            # z: Float[Tensor, "batch seq head d_head"],
                            # hook: HookPoint,
                            activation,
                            hook,
                            steering_vec 
                        ):
                            # print(activation[:, -1, :].shape)
                            # print(steering_vec[:, -1, :].shape)
                            activation[:, -1, :] += steering_vec[:, -1, :]
                            return activation
                        ```
                        
                    - ✅ SOLN: this seems to change every pos after initial end
                        
                        ```jsx
                        from functools import partial
                        
                        def act_add(
                            activation,
                            hook,
                            steering_vec,
                            initPromptLen
                        ):
                            activation[:, initPromptLen:, :] += steering_vec[:, -1, :]
                            return activation
                        
                        hook_fn = partial(
                                act_add,
                                steering_vec=steering_vec,
                                initPromptLen=initPromptLen
                            )
                        
                        test_sentence = "I think cats are "
                        initPromptLen = len(model.tokenizer.encode("I think cats are "))
                        cache_name = 'blocks.5.hook_resid_post'
                        model.reset_hooks(including_permanent=True)
                        model.add_hook(cache_name, hook_fn)
                        print(model.generate(test_sentence, max_new_tokens=10))
                        ```
                        
                    - ✅ you should use a multiplier to change hate cats to love cats
                        
                        `activation[:, initPromptLen:, :] += steering_vec[:, -1, :] * 10`
                        
        - ✅ if rollouts are random, for a prompt, how many rollouts should we use? just set the generation to deterministic (see `Llama2_spanish_months.ipynb, test prompts)`
    - ✅⚠️STEP 3: Cache activations from layer k to last layer L for unst & steered runs
        - ⚠️ ISSUE: for multiple generated tokens, which activations do we store? it’s not just the “next” one. then we need to pass all of them thru SAEs. perhaps we can track ALL the activations of every pos? but it’s not really comparable.
            - ✅ for now, just work with the immediate next generation  (for next token)
    - ✅ STEP 4: Pass both those activations through their respective pre-trained SAEs
        
        NOTE: pretrained use SAELens (which is built on transformerlens), and cache uses transformerlens. Only need to combine saes with tl for step 4
        
        - ✅ see saelens tutorial, [basic_loading_and_analysing](https://colab.research.google.com/drive/1KpWSKZ8PlUVzT8tjcttWU62qNRfoRgzN).ipynb
            - once get `feature_acts`, ignore the rest of that nb and use `GPT2_SAE_MLP0_seqcont_explora_v1.ipynb` and `GPT2_SAE_MLP0_seqcont_explora_v2.ipynb` to find most impt features from `feature_acts`
        - ✅ find feature inds with highest values
        - ✅ for each feature, find its highest actv tokens on pretrained sae’s dataset
            - ✅ need to flatten (batch,seq) into batch*seq first because it's ANY batch_seq, even if in same batch or same pos
            - ✅ top_acts_indices should be also be 1D. Then convert the indices into (batch, seq)
            - ✅ broadcast steering vec to actv samps
                
                [https://chatgpt.com/c/609ca94e-8db3-4d52-8b8b-b28d5a644018](https://chatgpt.com/c/609ca94e-8db3-4d52-8b8b-b28d5a644018)
                
                activation[:, -1, :] += steering_vec[:, -1, :] * 3
                if activation is
                torch.Size([32, 128, 768])
                
                and steering_vec is [1, 128, 768), will pytorch broadcast steering_vec to every batch samp in first dim?
                
            - ✅ we’re finding top features AFTER steering? they’re not going to be found before steering since it’s not obvious they’d activate? so dataset examples should only activate after steering on batch_tokens
                
                
    - ✅ STEP 5: Differences, before and after steering, for features from layer k to last layer
        - pass their differences too
        - feature inds or batch_seq inds may not be right because sae flattens them but saelens doesn’t give them as batch_seq. double check if you’re computing the right ones
            
            [https://chatgpt.com/c/d7e78853-306c-4763-8798-684d48c7bcb4](https://chatgpt.com/c/d7e78853-306c-4763-8798-684d48c7bcb4)
            
- ✅ figure out why saelens only trained resid_pre, not resid_post. in pytorch huggingface transformers, is resid post 5 the same as resid pre 6?
    
    In the context of the Hugging Face Transformers library and the architecture of Transformer models (like GPT), "resid post 5" and "resid pre 6" refer to the residual connections at different stages of the transformer layers.
    
    1. **resid post 5**: This typically refers to the output after the 5th transformer layer, including its residual connection.
    2. **resid pre 6**: This typically refers to the input to the 6th transformer layer, before any operations (like self-attention or feed-forward) are applied in that layer.
    
    In the architecture of a Transformer model, the output of one layer (including its residual connection) is the input to the next layer. Hence, the output of the 5th layer (which includes the residual connection, i.e., "resid post 5") is indeed the input to the 6th layer (i.e., "resid pre 6").
    
    Therefore, **"resid post 5" is the same as "resid pre 6"**. They are different terms for the same data tensor within the model architecture, just viewed from the perspective of different layers.
    
- ✅ Why are dataset examples for 5_resid_post and 6_resid_pre different for the same features?
    - This code outputs 1, showing they’re the exact same thing
        
        ```jsx
        comparison_result = (unst_cache['blocks.6.hook_resid_pre'] == unst_cache['blocks.5.hook_resid_post'])
        num_true = torch.sum(comparison_result).item()
        total_elements = comparison_result.numel()
        num_true / total_elements
        ```
        
    - ✅ SOLN: they’re the same, but each time you run dataset examples, you get different results
        
        The code exhibits randomness due to the use of `activation_store.get_batch_tokens()`, which is likely fetching a random batch of tokens from a dataset each time it is called. This introduces variability in the examples displayed each run.
        
    - ✅ [https://jbloomaus.github.io/SAELens/api/#sae_lens.ActivationsStore](https://jbloomaus.github.io/SAELens/api/#sae_lens.ActivationsStore)
    - ✅ `get_batch_tokens` doesn’t take num samples as arg, prob bc outdated vers but only old vers works for code in nb
        - you can replace fn but this still misses args
            
            ```
            def get_batch_tokens(self, batch_size: int | None = None):
                """
                Streams a batch of tokens from a dataset.
                """
                if not batch_size:
                    batch_size = self.store_batch_size_prompts
                sequences = []
                # the sequences iterator yields fully formed tokens of size context_size, so we just need to cat these into a batch
                for _ in range(batch_size):
                    sequences.append(next(self.iterable_sequences))
                return torch.stack(sequences, dim=0).to(self.model.W_E.device)
            
            activation_store.get_batch_tokens = get_batch_tokens
            ```
            
        - stream from openwebtext from hugf
            
            cannot use 32 x 1024, or else out of memory
            
        - Using 128, we find 5 post and 6 pre are the same. Also, later layers have closer features. Why doesn’t it change later layers if it changes output signif?
    - ✅ try samples from openwebtext that contain ‘love’ or ‘hate’ in them
        - how do i modify it so that half of the samples have the word love or hate in them?
            
            [https://chatgpt.com/c/b739a774-7574-4d8d-a72c-269c04e42588](https://chatgpt.com/c/b739a774-7574-4d8d-a72c-269c04e42588)
            
    - NOTE: in dataset examples, when the activation of a (samp, feat) is 0 (so feature doesn’t activate on anything else), it will default to batch 0 and a seq in it, but that doesn’t mean anything
- ✅ d**ecompose love-hate vector into features**
    
    [https://colab.research.google.com/drive/1IUtIe0D6UBAJYlPC4eJl00l8fmpohhKG#scrollTo=MBII3m57QCMZ](https://colab.research.google.com/drive/1IUtIe0D6UBAJYlPC4eJl00l8fmpohhKG#scrollTo=MBII3m57QCMZ)
    
    - Hi, got a question from the blog post. It was stated:
        
        [https://www.alignmentforum.org/posts/C5KAZQib3bzzpeyrg/full-post-progress-update-1-from-the-gdm-mech-interp-team](https://www.alignmentforum.org/posts/C5KAZQib3bzzpeyrg/full-post-progress-update-1-from-the-gdm-mech-interp-team)
        
        “look at the active features on the “ger” token of the “|BOS|An|ger|'' input.”
        
        Which dataset was used for this, and how many samples? For a certain steering vector in GPT2 small, I’m looking at the pretrained SAEs of SAELens and thinking about using the samples from activationstore (the activationstore of its pretrained sae gpt2 models uses Skylion007/openwebtext), though not sure if this is a good approach. 
        
    - what if we just steer this feature?
        
        ![Untitled](Done%201c002201437341e48b55b8276859a632/Untitled.png)
        
- just use neuronpedia to get max actv examples for top features
    
    I think I understand better now you find the top features and look up the top activating examples on neuronpedia; that's what the "Feature dashboard:" board is (I had used other code to get max actv examples)
    
    - you can also just directly search up features on neuronpedia
        - actually i could've just search up keywords using explanations on neuronpedia, i just found the same neuron on it that way
    - neuronpedia also already has clusters via umap
- ✅ dog vs cat vs mammal vs animal
    - search up on neuronpedia
        - sae set: residual-JB (joseph bloom)
        - dog: L6, F3986
            - belongs to cluster 548, which is about animals
            - cat also
        - dog: L9, F12435, F3163
        - just make a list on Neuronpedia’s site
            - [https://www.neuronpedia.org/list/cly36o0ui003v4y1gs5e9mza7](https://www.neuronpedia.org/list/cly36o0ui003v4y1gs5e9mza7)
            - how come top pos logits aren’t related to dogs, but top actv inputs are?
    - steer those features while ablating others
- ✅ [https://www.neuronpedia.org/steer/gemma-2b](https://www.neuronpedia.org/steer/gemma-2b)
    
    you can steer combinations of features already on neuronpedia
    
- ✅ [Neuronpedia steering results](../Neuronpedia%20steering%20results%20cef112a3d4444447ba4877a6da196737.md)

Organize notes and contact people

- ✅ msg bloom
    - dyn paper for multiple steering
        
        [https://opensourcemechanistic.slack.com/archives/C06R43HV2CR/p1719852417968129](https://opensourcemechanistic.slack.com/archives/C06R43HV2CR/p1719852417968129)
        
    - ask proj ideas
        
        [https://opensourcemechanistic.slack.com/archives/D07ACHVNR1C/p1719854597705039](https://opensourcemechanistic.slack.com/archives/D07ACHVNR1C/p1719854597705039)
        
- ✅ msg conmy
    
    [https://opensourcemechanistic.slack.com/archives/D070QED11RP/p1719862027211289](https://opensourcemechanistic.slack.com/archives/D070QED11RP/p1719862027211289)
    
    Thanks for the links! I was wondering if you have any findings about how steering specific parts of "component roles" in a circuit might have a specific effect on the input? For instance, ablating/patching/steering at subject inhibitors might affect which subjects are inhibited. I saw Makelov's research does do name steering at specific components of the IOI circuit, but I think the paper's focus was more about studying supervised vs sae features. If you have done work similar to this I'm interested in generalizing this to other behaviors
    
- ✅ msg luke
    
    Thanks for mentioning issues about the side effect speculation today, I was wondering if you can write it down again in a msg so I can be more aware of what to address? I think it was said "the reason the steering vector may work at layer L and not earlier layers is because layer L and after would not have side effects, while earlier layers may". Or may be something else
    
    - Sorry, forgot to reply to your earlier message. The person working with Alex is called Jacob. I don't recall his last name but his initials are GW.
    - Your description of what I said earlier is pretty accurate, but my question was a bit more general, and was more like "why think there is a meaningful explanation for side effects at all?", and then an example I gave is that side effects may differ massively based on the activations of the layer(s) you modify
    
    Thanks for the reply! I didn't get to the second part of my project talk yet, but it has something to do with comparing saes across models. I think your project is about finding better sae features for a model using a method you call alignment regularization; it's not directly related to what I'm thinking of, but I think you have some useful insights into how saes can better learn true features. Given that you have experience comparing saes I think I may have several questions to ask later if you have time in a few weeks. I'm running prelim geom experiments now so it'd be easier to explain once I finish them
    
    And by comparing sae features across models I mean a continuation of this: [https://transformer-circuits.pub/2023/monosemantic-features#phenomenology-universality](https://transformer-circuits.pub/2023/monosemantic-features#phenomenology-universality)
    
- [Geometry project ideas](../Geometry%20project%20ideas%20eb549c97d93548fc97e75e83fcba87a8.md)
- [SAE circuits brainstorm](../SAE%20circuits%20brainstorm%20bbdf5ded4da24855b11d0e706f19f097.md)
- [Feature Geometry- Lit Review](../Feature%20Geometry-%20Lit%20Review%20384f2f70a32245a7a9aa5b1481cd85ab.md)
- [Steering when ablate or patch](../SAE%20circuits%20brainstorm%20bbdf5ded4da24855b11d0e706f19f097/Steering%20when%20ablate%20or%20patch%205a04e0db28a34e44965e7b6fbe79a925.md)

Geometry of Activations: First steps

- ✅ browse feature plotting code
    - platonic repr
        
        [https://phillipi.github.io/prh/](https://phillipi.github.io/prh/)
        
        [https://github.com/minyoungg/platonic-rep](https://github.com/minyoungg/platonic-rep)
        
    - LLM categorical
        - linear repr repo
    - toy models superpos ARENA
        - [https://colab.research.google.com/drive/1hoD36nsHp6K0E-YeFgPzxazlstb7HPyh#scrollTo=DRQ9j4ftyHXf](https://colab.research.google.com/drive/1hoD36nsHp6K0E-YeFgPzxazlstb7HPyh#scrollTo=DRQ9j4ftyHXf)
        - [https://github.com/callummcdougall/ARENA_3.0/blob/main/chapter1_transformer_interp/exercises/part4_superposition_and_saes/utils.py](https://github.com/callummcdougall/ARENA_3.0/blob/main/chapter1_transformer_interp/exercises/part4_superposition_and_saes/utils.py)
    - neuronpedia umap (ask joseph)
- ✅ study categ geom paper thms
    
    [https://chatgpt.com/c/daf9bf12-e7dd-472b-a765-00bb6857ce37](https://chatgpt.com/c/daf9bf12-e7dd-472b-a765-00bb6857ce37)
    
    thm 8
    
    There is no perpendicular direction (in 1D space) to adjust one point without affecting the others. In higher dimensions, if vectors are not collinear, you have the freedom to move perpendicularly to affect one variable without altering the relative positions of others. 
    
    - what's the probability of w2? is that a different point on the line?
        
        Let's break it down intuitively using the concept of collinear points and probabilities.
        
        When we talk about the vectors \(\bar{\ell}*{w_0}, \bar{\ell}*{w_1}, \bar{\ell}_{w_2}\) being on a line, we are essentially saying that the positions of these points can be described using a single dimension. In this case:
        
        1. **Probabilities along a Line**: If these vectors are collinear, any change in the probability of one attribute (e.g., \(w_2\)) will necessarily influence the relative probabilities of the other attributes (\(w_0\) and \(w_1\)) because all movements are constrained to the line they form.
        2. **Probability of \(w_2\)**: The probability of \(w_2\) can be seen as a point along the line formed by \(\bar{\ell}*{w_0}, \bar{\ell}*{w_1}, \bar{\ell}_{w_2}\). To change the probability of \(w_2\), you have to move along this line. This movement will also affect the relative probabilities of \(w_0\) and \(w_1\).
        3. **Impact of Collinearity**: Since there is no direction in the line that allows you to move independently to change the probability of \(w_2\) without also affecting \(w_0\) and \(w_1\), you can't adjust one without influencing the others.
        
        To visualize this, think of the line as a tightrope. If you are walking along the tightrope (the line), every step forward or backward changes your position relative to all points on the tightrope. There's no way to step to the side (no perpendicular movement), so every move affects your relative position to all other points on the line.
        
        In summary, the probability of \(w_2\) is represented by a point on this line. To change this probability (i.e., move this point), you must move along the line, inherently affecting the relative probabilities of \(w_0\) and \(w_1\) as well.
        
- ✅ review UMAP
- ✅ find how actvs and weights plotted in
    
    [**Towards Monosemanticity**](https://www.notion.so/Towards-Monosemanticity-66d08a43363640ff9444550db9ca4151?pvs=21) 
    
    [https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html](https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html)
    
- ✅ plan feature geom sim measurement proj
    
    [Feature Geometry- Lit Review](../Feature%20Geometry-%20Lit%20Review%20384f2f70a32245a7a9aa5b1481cd85ab.md) 
    
    [Geometry project ideas](../Geometry%20project%20ideas%20eb549c97d93548fc97e75e83fcba87a8.md) 
    
- ✅ **EXPM**: plot pretrained sae features
    - plot feature weights 2D
        - ✅ [feature_weights_pca](https://colab.research.google.com/drive/1stczggQZRSRW7OU2mwoJ2XxDxhdfyqH5#scrollTo=MNk7IylTv610).ipynb
            - ✅ use updated `basic_loading_and_analysing`.ipynb [https://colab.research.google.com/github/jbloomAus/SAELens/blob/main/tutorials/basic_loading_and_analysing.ipynb#scrollTo=XoMx3VZpv611](https://colab.research.google.com/github/jbloomAus/SAELens/blob/main/tutorials/basic_loading_and_analysing.ipynb#scrollTo=XoMx3VZpv611)
            - ✅ [ask chatgpt to plot weights in pca and umap](https://chatgpt.com/c/68ebe2fd-6d96-4ba8-8bc1-574775aa47b9)
                - ✅ pca works but usign A100 is faster
                - ✅ debug umap
                    
                    ERROR: `AttributeError: module 'numpy.linalg._umath_linalg' has no attribute '_ilp64'`
                    
                    - [https://umap-learn.readthedocs.io/en/latest/](https://umap-learn.readthedocs.io/en/latest/)
                    - [https://umap-learn.readthedocs.io/en/latest/faq.html#is-there-gpu-or-multicore-cpu-support](https://umap-learn.readthedocs.io/en/latest/faq.html#is-there-gpu-or-multicore-cpu-support)
                    - transformerlens or saelens incompat w/ latest numpy? or gpu/cpu incompat
        - ✅ [feature_weights_umap](https://colab.research.google.com/drive/1Nxw9hntiIAwu8iYpQWQyarRY9MuS4JR8#scrollTo=s7GJCvWj2yBE).ipynb: try saving pickled sae feature weights in nb that installs saelens, then plot in umap in separte nb
            - cpu works
        - analyze results
            - [for the feature weight encoder matrix of a sparse autoencoder, torch.Size([768, 24576]), trained on activations of layer 8 of gpt-2 small, what does this plot mean? why don't I see clusters?](https://chatgpt.com/c/5a819a8f-6731-457c-88e5-74c09d9d70dd)
            - make sure you’re plotting by the cols? for decoder?
                
                Yes, it does matter whether you plot by columns or rows of the weight matrix because it changes the meaning of the points in the UMAP plot.
                
                ### Plotting Rows vs. Columns
                
                1. **Plotting Rows of the Weight Matrix:**
                    - Each row represents a different feature (in your case, 768 features).
                    - The UMAP plot will show the relationships between these features in a lower-dimensional space.
                    - This is useful if you want to understand how the features are related or clustered based on the autoencoder's weight matrix.
                2. **Plotting Columns of the Weight Matrix:**
                    - Each column represents a different input dimension (in your case, 24576 dimensions).
                    - The UMAP plot will show the relationships between the input dimensions in a lower-dimensional space.
                    - This is useful if you want to understand how the input dimensions are represented or clustered based on the autoencoder's weight matrix.
                
                ### Example: Plotting Rows
                
                If you want to visualize the relationships between the features, you should plot the rows of the weight matrix.
                
                ```python
                import umap
                import matplotlib.pyplot as plt
                
                # Assuming weight_matrix is your original matrix of size [768, 24576]
                
                # Initialize UMAP
                reducer = umap.UMAP(n_neighbors=15, min_dist=0.1, metric='euclidean')
                
                # Fit and transform the data by rows
                embedding = reducer.fit_transform(weight_matrix)
                
                # Plot the UMAP result
                plt.figure(figsize=(10, 8))
                plt.scatter(embedding[:, 0], embedding[:, 1], s=5, cmap='Spectral')
                plt.title('UMAP of Weight Matrix by Rows (Features)')
                plt.xlabel('UMAP Component 1')
                plt.ylabel('UMAP Component 2')
                plt.show()
                
                ```
                
                ### Example: Plotting Columns
                
                If you want to visualize the relationships between the input dimensions, you should transpose the weight matrix and plot the columns.
                
                ```python
                # Transpose the weight matrix to get dimensions [24576, 768]
                transposed_weight_matrix = weight_matrix.T
                
                # Initialize UMAP
                reducer = umap.UMAP(n_neighbors=15, min_dist=0.1, metric='euclidean')
                
                # Fit and transform the data by columns
                embedding = reducer.fit_transform(transposed_weight_matrix)
                
                # Plot the UMAP result
                plt.figure(figsize=(10, 8))
                plt.scatter(embedding[:, 0], embedding[:, 1], s=5, cmap='Spectral')
                plt.title('UMAP of Weight Matrix by Columns (Input Dimensions)')
                plt.xlabel('UMAP Component 1')
                plt.ylabel('UMAP Component 2')
                plt.show()
                
                ```
                
                ### Choosing Rows or Columns
                
                - **Choose Rows** if you are interested in the feature relationships.
                - **Choose Columns** if you are interested in the input dimension relationships.
                
                Based on your previous context, if you want to see how the features encoded by the sparse autoencoder cluster, you should plot the rows of the weight matrix. If your interest lies in understanding how the original input dimensions (activations of layer 8 of GPT-2 small) cluster, then you should plot the columns.
                
            - how to compare two umap set of points to see if similar
                
                
            - compare to neuronpedia
                - ask slack / jb
                    
                    I was also wondering if I can ask this question on the [#neuronpedia](https://opensourcemechanistic.slack.com/archives/C06R43HV2CR) channel: I'm looking to understand the umap plots on neuronpedia better so I've been taking the feature weight matrix from saelens (sae.W_enc) and just plotting them in umap to see if I get similar plots/clusters. I was wondering if there's a paper or blog post about what Umap parameters (num_neigh, etc) were used?
                    
                    Were they similar to the parameters in Towards Monosemanticity (attached paragraph)? Also I suppose to use decoder rather than encoder weights
                    
    - plot feature actvs 2D
        - ✅ plot feature actvs in pca
            
            same nb as weights
            
        - plot feature actvs in umap
            - ✅ either umap wasn’t compat with GPU, OR umap lib wasn’t compatible with saelens lib (diff vers of numpy, etc).
                - loading umap w/ saelens doesn’t work.
                    - so we needed to save feature_acts from a separate nb that loaded saelens
                - so test if umap compat with gpu. yes; it works with gpu
                    - So when saving feature_acts from pca, can save as gpu. Note a cpu run cannot load a tensor that was saved from a gpu; must use `.cpu` before saving it
            - there are clusters, but what are they?
                
                ![Untitled](Done%201c002201437341e48b55b8276859a632/Untitled%201.png)
                
    - interpret feature actvs
        
        
    - scale up using Torr node
- ✅ msg luke on universal features converging across models
    
    comparing saes across models. I think your project is about finding better sae features for a model using a method you call alignment regularization; it's not directly related to what I'm thinking of, but I think you have some useful insights into how saes can better learn true features. Given that you have experience comparing saes I think I may have several questions to ask later if you have time in a few weeks. I'm running prelim geom experiments now so it'd be easier to explain once I finish them
    
    And by comparing sae features across models I mean a continuation of this: [https://transformer-circuits.pub/2023/monosemantic-features#phenomenology-universality](https://transformer-circuits.pub/2023/monosemantic-features#phenomenology-universality)
    
    To phrase it better, I was thinking about how your method would approximate the true features better in one LLM. For two LLMs that are initialized differently, the saes trained on each of them for a layer would likely not find many analogous features. But if you train better saes, say with your method using the aggregates of multiple saes, I was wondering how much they would "converge' to find universally similar features, esp when features splitting occurs as saes get bigger. Similar to the platonic rep hypothesis. Do you think they would converge?
    
- ✅ chatgpt on ‘hier geom’ causal inner product reasons
    
    [https://chatgpt.com/c/fbfde9a6-76fd-4c88-a2bd-267312a4d3df](https://chatgpt.com/c/fbfde9a6-76fd-4c88-a2bd-267312a4d3df)
    
    - Why do we need to use the causal inner product? Why couldn't the authors have just looked for simplex orthogonality relations directly in the embedding space (last token, last layer) or unembedding space separately?
        1. **Unification of Embedding and Unembedding Spaces**:
        The causal inner product allows for the unification of the context embedding space (Λ) and the token unembedding space (Γ) into a single representation space. This unification is essential because it ensures that concepts represented in these distinct spaces can be compared and analyzed under a common framework. The transformation using an invertible matrix \( A \) and a constant vector \( \gamma_0 \) aligns these spaces such that the Euclidean inner product in the transformed space respects the semantics of language【6:2†source】.
        2. **Simplicity and Structure**:
        The causal inner product allows for the representation of categorical and hierarchical concepts as simple geometric structures, such as simplices. This geometric representation is more interpretable and aligns with the hierarchical nature of semantic concepts. By ensuring orthogonality and maintaining a unified representation space, the causal inner product supports the formation of these geometric structures, facilitating easier manipulation and understanding of the concepts【6:12†source】【6:14†source】.
        3. **Empirical Validation**:
        The theoretical results are empirically validated using a large language model (Gemma-2B). The transformation to a canonical representation space via the causal inner product allows for the alignment of the embedding and unembedding representations, enabling the observation and measurement of the predicted geometric structures in practice. This empirical validation strengthens the theoretical foundation laid out by the authors【6:12†source】.
        
        Directly looking for simplex orthogonality relations in either the embedding space or the unembedding space separately would not ensure the alignment of these spaces or respect the hierarchical and causal relationships between concepts. The causal inner product provides a rigorous mathematical framework that ensures these properties are maintained, enabling a more accurate and interpretable representation of semantic structures in language models.
        
    - Was LDA used to get a vector in the causal inner product's space? If we just look at individual activation spaces of a layer, do we need LDA or can we just look at the activation vector directly?
        1. **Separate Classes**: The primary role of LDA is to find a projection that maximizes the separation between different classes (e.g., words belonging to different concepts) while minimizing the variance within each class. This helps in creating a clear distinction between concepts in the representation space.
        2. **Minimize Variance**: By minimizing the within-class variance, LDA ensures that the projection of the unembedding vectors for tokens associated with a specific concept (e.g., "mammal") is consistent, which aligns with the requirement that concepts should have well-defined vector representations with minimal variance around a central value.
        3. **Align with Theoretical Results**: The LDA-based estimation of vector representations aligns with the theoretical framework provided by the causal inner product, ensuring that the geometric properties such as orthogonality and simplex structures are preserved and observable in the empirical results.
        
        ### Looking at Individual Activation Spaces
        
        If we were to look at the activation vectors directly within an individual layer without transforming them via the causal inner product, there are some key considerations:
        
        1. **Representation Alignment**: Without the transformation provided by the causal inner product, the embeddings and unembeddings might not be aligned in a way that respects the semantic relationships between concepts. This misalignment can obscure the geometric structures (such as orthogonality and simplices) that are crucial for understanding the hierarchical relationships.
        2. **Need for LDA**: In the individual activation spaces, LDA can still be beneficial because it helps in finding directions that separate different classes of concepts. However, if the goal is to directly observe activation vectors, LDA might not be strictly necessary if the vectors already exhibit clear separations. Yet, typically, raw activation vectors might not be as well-separated without some form of dimensionality reduction or projection technique like LDA.
        3. **Empirical Consistency**: The empirical validation of theoretical results often requires transformations like LDA to ensure consistency with the theoretical framework. Direct observation of raw activation vectors might miss subtle relationships that are more apparent after applying LDA or similar techniques.
        
        ### 
        
    - actually LDA is used to get a vector for an attribute, which is a collection of tokens, using those tokens?
        
        Yes, you're correct. LDA (Linear Discriminant Analysis) is indeed used to get a vector representation for an attribute, which is essentially a collection of tokens. Here's a detailed explanation of how LDA is utilized in this context:
        
        ### Purpose of LDA in the Study
        
        LDA is employed to estimate the vector representations of attributes by utilizing the tokens associated with those attributes. Here's how this works:
        
        1. **Attribute and Token Relationship**: Each attribute (e.g., "mammal") is associated with a set of tokens (e.g., "dog," "cat," "elephant"). The goal is to find a vector that represents this attribute based on the embeddings of these tokens.
        2. **Class Separation**: LDA helps in finding a projection that maximizes the separation between the tokens associated with the attribute and those that are not. This ensures that the vector representation of the attribute captures the distinguishing features of the tokens that belong to it.
        3. **Minimizing Within-Class Variance**: LDA also minimizes the variance within the tokens of the same attribute. This means that the tokens associated with the attribute should have similar projections onto the resulting vector, making the representation consistent.
        
        ### Process of Using LDA
        
        Here's a step-by-step process of how LDA is used in this study:
        
        1. **Collect Tokens**: Gather the tokens that belong to the attribute (e.g., all tokens that can be considered "mammals").
        2. **Compute Unembedding Vectors**: For each token, compute its unembedding vector in the representation space.
        3. **Estimate the Vector Representation**: Use LDA to find the direction that best separates the tokens associated with the attribute from those that are not. This involves:
            - Calculating the mean vector for the tokens of the attribute.
            - Calculating the covariance matrix of these tokens.
            - Finding the direction that maximizes the between-class variance and minimizes the within-class variance.
        
        ### Equation for LDA-based Vector Estimation
        
        The LDA-based estimation of the vector representation for an attribute \( w \) is given by:
        \[ \ell_w = \frac{\text{Cov}(g_w)^{-1} \mathbb{E}(g_w)}{\|\text{Cov}(g_w)^{-1} \mathbb{E}(g_w)\|_2} \]
        where \( g_w \) represents the unembedding vectors of the tokens associated with the attribute \( w \), and \(\text{Cov}(g_w)\) is the covariance matrix of these vectors.
        
        ### Empirical Validation
        
        Using LDA in this manner ensures that the resulting vector representation of the attribute aligns with the theoretical expectations, such as the orthogonality of hierarchically related concepts and the simplex structure of categorical concepts. This process helps in empirically validating the theoretical results by showing that the estimated vectors exhibit the expected geometric properties.
        
        ### Conclusion
        
        LDA is indeed used to get a vector for an attribute by utilizing the tokens associated with that attribute. This approach ensures that the resulting vector representation accurately captures the distinguishing features of the attribute and aligns with the theoretical framework provided by the causal inner product.
        
    - i dont see here how multiple tokens aer used? it says g_w is just a word sampled
        
        The confusion arises from the notation and the explanation in the text. Let's clarify how multiple tokens are used to estimate the vector representation for an attribute using LDA:
        
        ### Explanation of the Equation
        
        1. **Tokens Associated with Attribute \( w \)**:
            - \( Y(w) \) represents the set of tokens associated with the attribute \( w \). For example, if \( w \) is "mammal," \( Y(w) \) might include tokens like "dog," "cat," "elephant," etc.
        2. **Unembedding Vectors**:
            - \( g_w \) represents the unembedding vector of a word sampled uniformly from \( Y(w) \). This means that for the calculation, each word in \( Y(w) \) has an unembedding vector \( g \), and \( g_w \) is the set of these vectors for all tokens in \( Y(w) \).
        3. **Covariance Matrix**:
            - The covariance matrix \( \text{Cov}(g_w) \) is computed using the unembedding vectors of all tokens in \( Y(w) \). This involves taking all the tokens associated with \( w \) and calculating the covariance of their unembedding vectors.
        4. **LDA Estimation**:
            - The vector \( \ell_w \) for the attribute \( w \) is estimated using these unembedding vectors. Specifically, the estimation involves calculating the mean vector \( \mathbb{E}(g_w) \) and the covariance matrix \( \text{Cov}(g_w) \) for the set of tokens.
        
        ### Detailed Steps
        
        1. **Collect Tokens**:
            - Gather all tokens that are associated with the attribute \( w \). This forms the set \( Y(w) \).
        2. **Compute Unembedding Vectors**:
            - For each token in \( Y(w) \), compute its unembedding vector. Let's denote the set of these vectors as \( \{ g_{w1}, g_{w2}, ..., g_{wn} \} \).
        3. **Calculate Covariance Matrix**:
            - Calculate the covariance matrix \( \text{Cov}(g_w) \) using the unembedding vectors of all tokens in \( Y(w) \). This matrix captures the variance and correlations of the vectors within the set.
        4. **Estimate Vector Representation**:
            - Use LDA to find a projection that separates the tokens associated with \( w \) from those not associated with it. The LDA process maximizes the separation between classes (tokens associated with \( w \) vs. those that are not) while minimizing the within-class variance.
        5. **Compute the Vector**:
            - The vector \( \ell_w \) is computed using the pseudo-inverse of the covariance matrix and the mean vector of the unembedding vectors. The formula provided in the text is:
            \[
            \ell_w = \left( \tilde{g}_w^T \mathbb{E}(g_w) \right) \tilde{g}_w, \quad \text{with} \quad \tilde{g}_w = \frac{\text{Cov}(g_w)^\dagger \mathbb{E}(g_w)}{\| \text{Cov}(g_w)^\dagger \mathbb{E}(g_w) \|_2}
            \]
            - Here, \( \mathbb{E}(g_w) \) is the mean of the unembedding vectors of tokens in \( Y(w) \), and \( \text{Cov}(g_w)^\dagger \) is the pseudo-inverse of the covariance matrix.
        
        ### Summary
        
        While the text may seem to suggest using a single token, it actually involves using the set of tokens associated with the attribute to compute the mean and covariance matrix. These are then used in the LDA process to estimate the attribute's vector representation. Thus, multiple tokens are indeed used to derive the vector \( \ell_w \) for the attribute \( w \).
        
    - why were these attribute vectors such as “L_bird” used, rather than individual tokens such as “bird”?
        
        The attribute vectors (e.g., \( \ell_{\text{bird}} \)) are used rather than individual token vectors (e.g., "bird") for several key reasons:
        
        ### 1. Capturing Generality and Abstraction
        
        - **Attribute vectors** represent the general concept or category that encompasses all tokens associated with that attribute. For example, the attribute vector \( \ell_{\text{bird}} \) captures the essence of the concept "bird" which includes all specific instances of birds (like "sparrow," "eagle," "parrot").
        - **Individual token vectors** represent specific words, which may only capture particular instances or narrower aspects of the attribute. The vector for "bird" might only reflect the specific usage of the word "bird" in the training data, rather than the entire category.
        
        ### 2. Reducing Variability and Noise
        
        - **Attribute vectors** are calculated by aggregating information from multiple tokens, reducing the variability and noise inherent in individual word usage. This aggregation results in a more robust and stable representation of the concept.
        - **Individual token vectors** can vary significantly depending on context and usage frequency, leading to less reliable representations if used in isolation.
        
        ### 3. Semantic Coherence
        
        - **Attribute vectors** ensure that the semantic properties of the entire category are captured. For instance, the vector \( \ell_{\text{bird}} \) is derived from multiple bird-related tokens, ensuring that the representation is semantically coherent and representative of the entire class.
        - **Individual token vectors** might not fully capture the hierarchical or categorical relationships within the data, missing out on the broader semantic context.
        
        ### 4. Facilitating Geometric Interpretations
        
        - **Attribute vectors** allow for the application of geometric interpretations such as orthogonality and simplex structures. These interpretations are crucial for understanding relationships between different concepts and categories in the representation space.
        - **Individual token vectors** do not provide a straightforward way to apply these geometric interpretations, as they are tied to specific instances rather than abstract categories.
        
        ### 5. Enabling Hierarchical and Categorical Analysis
        
        - **Attribute vectors** support the analysis of hierarchical and categorical relationships, which is essential for understanding the structure of semantic representations in language models. For example, \( \ell_{\text{mammal}} \) and \( \ell_{\text{animal}} \) can be used to study the hierarchical relationship between mammals and animals.
        - **Individual token vectors** do not easily facilitate this kind of analysis, as they do not inherently represent the broader categories or hierarchical levels.
        
        ### Practical Implementation
        
        As detailed in the provided document, the authors used LDA to derive these attribute vectors from the unembedding vectors of multiple tokens associated with each attribute. This method ensures that the resulting vectors are representative of the entire category rather than just individual instances.
        
        ### Conclusion
        
        Using attribute vectors such as \( \ell_{\text{bird}} \) instead of individual tokens like "bird" allows for more general, stable, and semantically coherent representations. These vectors facilitate the analysis of hierarchical and categorical structures in the representation space of language models, which is essential for understanding and interpreting the underlying semantic relationships.
        
    
    It seems like the statement “"the simplex of fish,mammal, bird is orthogonal to the vector representation of animal" is interpreted as span{¯ℓmammal,¯ℓbird,¯ℓfish} is orthogonal to L_animal. If so,  what does it mean that a * mammal + b*bird + c*fish is orthogonal to L_animal?
    
    - Semantically what does a * mammal + b*bird + c*fish mean? How can a specific vector be a combination of those?
        
        **Example**: Interpolating between "mammal" and "bird" might create a vector that captures semantic similarities or shared characteristics, such as being warm-blooded.
        
    - do the vectors in span{¯ℓmammal,¯ℓbird,¯ℓfish} represent specific animals?
        
        The vectors in \(\text{span}\{\ell_{\text{mammal}}, \ell_{\text{bird}}, \ell_{\text{fish}}\}\) do not necessarily represent specific animals directly. Instead, they represent combinations of the attributes associated with mammals, birds, and fish. Here’s a more detailed explanation:
        
        ### Understanding the Span
        
        1. **Span of Vectors**:
            - The span of \(\{\ell_{\text{mammal}}, \ell_{\text{bird}}, \ell_{\text{fish}}\}\) consists of all possible linear combinations of these vectors. Mathematically, this means any vector \( v \) in this span can be expressed as:
            \[
            v = a \cdot \ell_{\text{mammal}} + b \cdot \ell_{\text{bird}} + c \cdot \ell_{\text{fish}}
            \]
            - Here, \(a\), \(b\), and \(c\) are scalar coefficients.
        
        ### Semantic Interpretation
        
        1. **Attribute Combinations**:
            - The vectors within this span represent different mixtures or combinations of the semantic attributes associated with mammals, birds, and fish. They do not correspond to specific animals but rather to abstract concepts that blend these attributes.
        2. **Conceptual Space**:
            - For example, a vector in this span might represent a general concept that has some mammalian traits, some avian traits, and some piscine traits. This is more about capturing the shared and overlapping characteristics rather than pinpointing specific animals.
        3. **Abstract Entities**:
            - Such combinations could be used to model abstract or hypothetical entities. For instance, in a hypothetical or fantasy context, a vector in this span could represent a creature with a mix of traits from mammals, birds, and fish.
        
        ### Specific Animals and Attribute Vectors
        
        1. **Representing Specific Animals**:
            - Specific animals like "dog," "sparrow," or "salmon" would typically be represented by their own unique vectors, derived from their particular contexts and usage in the training data.
            - These specific animal vectors would be located in the broader semantic space, which might be influenced by the attribute vectors \(\ell_{\text{mammal}}, \ell_{\text{bird}}, \ell_{\text{fish}}\), but not confined to their span.
        2. **Hierarchical and Categorical Representation**:
            - The span of these attribute vectors provides a subspace that helps in understanding and organizing the broader semantic space. It’s useful for analyzing relationships and hierarchies but doesn’t directly map to specific instances.
        
        ### Practical Example
        
        - **Combining Attributes**: If you have \(\ell_{\text{mammal}}\), \(\ell_{\text{bird}}\), and \(\ell_{\text{fish}}\), a vector \(0.5 \cdot \ell_{\text{mammal}} + 0.3 \cdot \ell_{\text{bird}} + 0.2 \cdot \ell_{\text{fish}}\) might represent an abstract concept that combines features of these three classes. This vector is not a direct representation of a specific animal but rather an abstract blend.
        
        ### Conclusion
        
        The vectors in \(\text{span}\{\ell_{\text{mammal}}, \ell_{\text{bird}}, \ell_{\text{fish}}\}\) represent abstract combinations of the attributes associated with mammals, birds, and fish. They do not correspond directly to specific animals but provide a useful subspace for exploring the relationships and characteristics of these broader categories. Specific animals are represented by their own unique vectors within the broader semantic space of the model.
        
- ✅ How does whitening matrix "make" variables uncorrelated? Shouldn't the correlation be how the variables truly are? Or is it transforming the data into a perspective such that when look at it from that basis, the data is uncorrelated on that basis?
    
    [https://chatgpt.com/c/3091fef0-4b87-41f9-8df3-c4c4ef37db3f](https://chatgpt.com/c/3091fef0-4b87-41f9-8df3-c4c4ef37db3f)
    
    The concept of whitening a matrix is indeed to transform the data into a new basis where the variables are uncorrelated and standardized. This transformation doesn't change the true relationships between the variables but provides a different perspective or basis where the correlations between the transformed variables are zero, and their variances are equal to one. Here’s how it works and why it’s useful:
    
    ### How Whitening Works
    
    1. **Centering the Data**: The first step is to center the data by subtracting the mean of each variable, making the dataset have a mean of zero for each variable.
    2. **Covariance Matrix**: Compute the covariance matrix \( \Sigma \) of the centered data. This matrix contains the variances along the diagonal and the covariances off-diagonal, representing the relationships between the original variables.
    3. **Eigenvalue Decomposition**: Perform eigenvalue decomposition on the covariance matrix:
    \[
    \Sigma = V \Lambda V^T
    \]
    where \( V \) is a matrix of eigenvectors, and \( \Lambda \) is a diagonal matrix of eigenvalues.
    4. **Whitening Transformation**: The whitening matrix \( W \) is constructed using the eigenvectors and the inverse square root of the eigenvalues:
    \[
    W = \Lambda^{-\frac{1}{2}} V^T
    \]
    The whitened data \( X_{\text{whitened}} \) is obtained by multiplying the centered data \( X \) by the whitening matrix:
    \[
    X_{\text{whitened}} = X W
    \]
    
    ### Why Whitening Makes Variables Uncorrelated
    
    The multiplication by the whitening matrix \( W \) transforms the original data into a new space where:
    
    - **Uncorrelated Variables**: The covariance matrix of \( X_{\text{whitened}} \) becomes the identity matrix \( I \), meaning the variables are uncorrelated. This is because the whitening transformation diagonalizes the covariance matrix and rescales the eigenvalues to one.
    - **Unit Variance**: Each variable in the whitened data has a variance of one.
    
    ### Interpretation and Utility
    
    - **Perspective Transformation**: Whitening provides a new basis in which the data is analyzed. It doesn't alter the inherent relationships in the data but represents it in a way that is often more useful for certain algorithms and analyses (e.g., principal component analysis, independent component analysis).
    - **Standardization**: Whitening standardizes the data, which can be particularly beneficial for machine learning algorithms that are sensitive to the scale and correlation of the data (e.g., gradient-based optimization algorithms).
    
    ### Summary
    
    Whitening transforms the data such that, in the new basis, the variables are uncorrelated and have unit variance. This transformation is a mathematical tool to facilitate certain analyses and algorithms, not a reflection of the "true" state of the variables in their original form. The true correlations remain in the original data, but in the transformed space, the data is easier to work with for various applications.
    
- ✅ email kiho on project idea
    
    Hi, I was wondering if you have some advice on adjusting this project plan:
    
    I was thinking about how to detect simplex structures in intermediate layers. A starting point would be to just look at the embedded activation vectors of individual tokens, and to use LDA to calculate vectors for the attribution sets they belong to. Then we can calculate the orthogonality relations of these attribute vectors. I have a few questions about how to extend the “Hierarchical concepts” paper to intermediate layers:
    
    1) The paper looks for the structure in a canonical representation space with the causal inner product, not just in the embedding space. Would we have to “unify” an intermediate layer embedding with the unembedding space, if this is possible right now? Or would it make sense to look for orthogonality relations of attribute vectors constructed directly by LDA from activation vectors of individual tokens?
    
    2) In Figure 5, my understanding is the adjacency matrix doesn’t depend on the vectors, but is already there from Wordnet, and we want to check if it appears in the cosine sim matrix (fig 5b) but not for child-parent (fig 5c). Can we do this for intemediate space experiments? Also, would fig 5c show there’s a “nested” hierarchy where (animal - mammal) may be manipulated separately from (mammal-elephant)?
    
    3) Experimentally, should we show this for polytopes of say span{4 members or more} and not just span{3 members}?
    
    (The question below is less important for planning, so not needed to answer now):
    
    A) Why were these attribute vectors such as “L_bird” used, rather than individual tokens such as “bird”? I’m guessing we’re not trying to study individual tokens, but a general “subspace” of an attribute; a set of tokens in an attribute set form a “cluster” and we want to obtain the vector that represents that cluster over other clusters (so LDA maximizes between-class variance). Then L_bird estimates this “subspace” better. But what’s a good response if someone questions why we don’t just use “bird”?
    
    B) It seems like the statement "the simplex of fish,mammal, bird is orthogonal to the vector representation of animal" is interpreted as span{¯ℓmammal,¯ℓbird,¯ℓfish} is orthogonal to L_animal. If (a * mammal - b*bird + c*fish) is a member of the span, what does that mean semantically (I think we pass in an input that contains “traits” of all three?) and does it mean that semantically speaking, those specific traits are orthogonal to L_animal?
    
- ✅ writeup geom plan (org notes just on it) and slides
    
    [https://docs.google.com/presentation/d/1AHuy77JmlQ0xzLxSiwVxaNS-5U3BLWn-z9HMoM2R-Rs/edit#slide=id.g2e9f646b02d_0_13](https://docs.google.com/presentation/d/1AHuy77JmlQ0xzLxSiwVxaNS-5U3BLWn-z9HMoM2R-Rs/edit#slide=id.g2e9f646b02d_0_13)
    
    - Universality by Geometry, v2
        
        [https://docs.google.com/presentation/d/1QQ9cnGzRH7MCkRF1RlQ_28M9gJ1j9ra3umWy96v5slc/edit#slide=id.g2ea1a29255c_0_71](https://docs.google.com/presentation/d/1QQ9cnGzRH7MCkRF1RlQ_28M9gJ1j9ra3umWy96v5slc/edit#slide=id.g2ea1a29255c_0_71)
        
    - how ph paper finds the “right” layer across 2 models to compare?
    - understand mutual nearest neighbors. kernel alignment metric computes a score based on datapoints passed thru metrics.
    - model stitching
- ✅ **EXPM**: plot feature acts, and compare before vs after steering/ablating/patching
    - in another layer, track how a specific set of features (eg. love or cat) changes after steering
        - [save_actvs_afterSteer](https://colab.research.google.com/drive/1Kvb-MJUdSyolrmXTON2432l8UIAHQmwq#scrollTo=SRZ1lgrSBVBE).ipynb
        - [feature_actvs_afterSteer_umap](https://colab.research.google.com/drive/1brV9lxVX9uR_GHtWprUqSFEWqgriB0ZX#scrollTo=4vuh4LF02nKs).ipynb
            - get CCA scores, but it’s slow
                
                Canonical Correlation Analysis (CCA) can indeed be computationally intensive, especially for large datasets or high-dimensional feature spaces. If you’re finding CCA to be very slow, there are several approaches and alternative methods you can consider to make the comparison more efficient and effective.
                
                Here’s a comprehensive guide to faster and more efficient ways to compare UMAP embeddings, including methods to speed up CCA and other alternatives:
                
                ### 1. **Optimizing CCA Performance**
                
                If you still want to use CCA, here are some strategies to optimize its performance:
                
                ### **a. Reduce Dimensionality Before CCA**
                
                Reducing the dimensionality of your feature space before applying CCA can significantly speed up the computation. You can use PCA (Principal Component Analysis) or any other dimensionality reduction technique for this purpose.
                
                ```python
                from sklearn.decomposition import PCA
                from sklearn.cross_decomposition import CCA
                
                # Reduce dimensionality with PCA before CCA
                pca1 = PCA(n_components=50)  # Adjust the number of components as needed
                pca2 = PCA(n_components=50)
                data1_reduced = pca1.fit_transform(embedding1)
                data2_reduced = pca2.fit_transform(embedding2)
                
                # Apply CCA
                cca = CCA(n_components=10)
                cca.fit(data1_reduced, data2_reduced)
                
                # Transform the data
                data1_c, data2_c = cca.transform(data1_reduced, data2_reduced)
                
                ```
                
                ### **b. Use Approximate CCA Algorithms**
                
                Consider using libraries or implementations optimized for large datasets. For instance, you can use the `sklearn` implementation of CCA, but there are also other libraries and frameworks designed for efficiency in large-scale computations.
                
                ### 2. **Alternative Methods for Comparing UMAP Embeddings**
                
                Here are several alternative methods for comparing UMAP embeddings that are generally faster and may provide useful insights:
                
                ### *a. **Procrustes Analysis**
                
                Procrustes analysis is a method for comparing the shapes of two datasets and can be done quickly with the `scipy` library.
                
                ```python
                from scipy.spatial import procrustes
                
                # Perform Procrustes analysis
                mtx1, mtx2, disparity = procrustes(embedding1, embedding2)
                
                print(f"Procrustes Disparity: {disparity}")
                
                ```
                
                ### *b. **k-Nearest Neighbors (k-NN) Consistency**
                
                Comparing the k-NN consistency measures how well the neighborhood structure is preserved across the two datasets.
                
                ```python
                from sklearn.neighbors import NearestNeighbors
                
                def knn_consistency(embedding1, embedding2, n_neighbors=5):
                    nbrs1 = NearestNeighbors(n_neighbors=n_neighbors).fit(embedding1)
                    nbrs2 = NearestNeighbors(n_neighbors=n_neighbors).fit(embedding2)
                    indices1 = nbrs1.kneighbors(return_distance=False)
                    indices2 = nbrs2.kneighbors(return_distance=False)
                    consistency = np.mean([len(np.intersect1d(indices1[i], indices2[i])) / n_neighbors for i in range(len(embedding1))])
                    return consistency
                
                knn_consistency_score = knn_consistency(embedding1, embedding2)
                print(f"k-NN Consistency: {knn_consistency_score}")
                
                ```
                
                ### *c. **Distance Correlation**
                
                Distance correlation measures both linear and non-linear relationships and is generally computationally efficient.
                
                ```python
                from scipy.spatial.distance import pdist, squareform
                from scipy.stats import pearsonr
                
                def distance_correlation(X, Y):
                    X_dist = squareform(pdist(X, 'euclidean'))
                    Y_dist = squareform(pdist(Y, 'euclidean'))
                    corr, _ = pearsonr(X_dist.ravel(), Y_dist.ravel())
                    return corr
                
                dist_corr = distance_correlation(embedding1, embedding2)
                print(f"Distance Correlation: {dist_corr}")
                
                ```
                
                ### *d. **Mutual Nearest Neighbors (MNN) Analysis**
                
                Mutual nearest neighbors can also be used to compare embeddings, though it may be less common.
                
                ```python
                from sklearn.neighbors import NearestNeighbors
                
                def mutual_nearest_neighbors(embedding1, embedding2, n_neighbors=5):
                    nbrs1 = NearestNeighbors(n_neighbors=n_neighbors).fit(embedding1)
                    nbrs2 = NearestNeighbors(n_neighbors=n_neighbors).fit(embedding2)
                    indices1 = nbrs1.kneighbors(return_distance=False)
                    indices2 = nbrs2.kneighbors(return_distance=False)
                    mnn_count = 0
                    for i in range(len(embedding1)):
                        mnn_count += len(set(indices1[i]).intersection(indices2[i]))
                    mnn_ratio = mnn_count / len(embedding1)
                    return mnn_ratio
                
                mnn_score = mutual_nearest_neighbors(embedding1, embedding2)
                print(f"Mutual Nearest Neighbors Ratio: {mnn_score}")
                
                ```
                
                ### 3. **Visualization for Initial Comparison**
                
                Sometimes, visual inspection of the UMAP embeddings can provide useful insights, and it is a quick first step:
                
                ```python
                import matplotlib.pyplot as plt
                
                # Plot the UMAP results
                fig, axes = plt.subplots(1, 2, figsize=(12, 6))
                axes[0].scatter(embedding1[:, 0], embedding1[:, 1], c='blue', label='Dataset 1')
                axes[0].set_title('UMAP Projection of Dataset 1')
                axes[0].legend()
                
                axes[1].scatter(embedding2[:, 0], embedding2[:, 1], c='green', label='Dataset 2')
                axes[1].set_title('UMAP Projection of Dataset 2')
                axes[1].legend()
                
                plt.show()
                
                ```
                
                ### 4. **Using UMAP’s `transform` for Different Seeds**
                
                To ensure consistent results across different seeds, you can set a fixed seed value for reproducibility in UMAP, but it's important to note that it does not eliminate the inherent randomness completely.
                
                ```python
                import umap
                
                # UMAP with a fixed seed for reproducibility
                reducer = umap.UMAP(random_state=42)
                embedding1 = reducer.fit_transform(data1)
                embedding2 = reducer.fit_transform(data2)
                
                ```
                
                ### 5. **Comparing UMAP Embeddings with Other Dimensionality Reduction Techniques**
                
                You might also want to compare UMAP embeddings using other dimensionality reduction techniques like t-SNE or PCA.
                
                ```python
                from sklearn.manifold import TSNE
                from sklearn.decomposition import PCA
                
                # t-SNE
                tsne = TSNE(n_components=2, random_state=42)
                embedding1_tsne = tsne.fit_transform(data1)
                embedding2_tsne = tsne.fit_transform(data2)
                
                # PCA
                pca = PCA(n_components=2)
                embedding1_pca = pca.fit_transform(data1)
                embedding2_pca = pca.fit_transform(data2)
                
                ```
                
                ### Summary Table of Methods and Performance
                
                | Method | Pros | Cons | Speed |
                | --- | --- | --- | --- |
                | CCA | Detailed canonical correlation analysis | Computationally intensive for large datasets | Slow |
                | PCA + CCA | Reduces dimensionality before CCA | Requires setting PCA components properly | Moderate |
                | Procrustes Analysis | Fast, effective for shape comparison | Measures only shape similarity | Fast |
                | k-NN Consistency | Simple, measures neighborhood structure | May not capture all relationships | Fast |
                | Distance Correlation | Captures both linear and non-linear relationships | Measures overall similarity | Fast |
                | Mutual Nearest Neighbors | Measures neighborhood consistency | Less common, may be less intuitive | Fast |
                | Visualization | Provides intuitive visual insights | Not a quantitative measure | Fast |
                | Other Dimensionality Reduction (t-SNE, PCA) | Useful for comparison, can be faster | t-SNE can be slow for large datasets | Moderate |
                
                ### Conclusion
                
                While CCA can be slow, there are several alternative methods for comparing UMAP embeddings that are computationally more efficient. By reducing dimensionality, using alternative comparison methods, or employing effective visualization techniques, you can achieve meaningful comparisons without extensive computation times.
                
                You can choose the approach based on the size of your dataset, the specific aspects you are interested in comparing, and the computational resources available to you.
                
                ### Example Code with Optimizations and Alternatives
                
                Here’s a comprehensive example incorporating PCA for dimensionality reduction, along with Procrustes Analysis, Distance Correlation, and k-NN Consistency:
                
                ```python
                import numpy as np
                import umap
                import cupy as cp
                from sklearn.decomposition import PCA
                from sklearn.neighbors import NearestNeighbors
                from scipy.spatial import procrustes
                from scipy.spatial.distance import pdist, squareform
                from scipy.stats import pearsonr
                from sklearn.datasets import make_blobs
                from time import time
                import matplotlib.pyplot as plt
                
                # Generate or load data
                data1 = np.random.rand(10000, 50)  # Synthetic data
                data2 = np.random.rand(10000, 50)  # Another synthetic dataset
                
                # Apply UMAP with a fixed random state
                reducer = umap.UMAP(random_state=42)
                embedding1 = reducer.fit_transform(data1)
                embedding2 = reducer.fit_transform(data2)
                
                # Reduce dimensionality with PCA before CCA
                pca1 = PCA(n_components=50)
                pca2 = PCA(n_components=50)
                data1_reduced = pca1.fit_transform(embedding1)
                data2_reduced = pca2.fit_transform(embedding2)
                
                # Apply CCA
                cca = CCA(n_components=
                ```
                
            - can i use cca on umap?
                
                Yes, you can use Canonical Correlation Analysis (CCA) on UMAP embeddings to compare the embeddings of two different datasets. The idea is to first reduce the dimensionality of both datasets using UMAP, and then use CCA to find the linear combinations of the UMAP embeddings that are maximally correlated.
                
                ### Step-by-Step Guide
                
                Here is a step-by-step guide to apply CCA on UMAP embeddings:
                
                1. **Install the Required Libraries**:
                Ensure you have `umap-learn`, `numpy`, `scikit-learn`, and `matplotlib` installed.
                    
                    ```python
                    !pip install umap-learn numpy scikit-learn matplotlib
                    
                    ```
                    
                2. **Import Libraries**:
                Import the necessary libraries for UMAP, CCA, and data manipulation.
                    
                    ```python
                    import numpy as np
                    import umap
                    from sklearn.cross_decomposition import CCA
                    import matplotlib.pyplot as plt
                    
                    ```
                    
                3. **Generate or Load Data**:
                For demonstration purposes, let's create some synthetic data.
                    
                    ```python
                    # Generate synthetic data for demonstration
                    data1 = np.random.rand(100, 50)  # 100 samples with 50 features
                    data2 = np.random.rand(100, 50)  # Another dataset with the same dimensions
                    
                    ```
                    
                4. **Apply UMAP**:
                Use UMAP to reduce the dimensionality of both datasets.
                    
                    ```python
                    # Apply UMAP to both datasets
                    reducer = umap.UMAP(n_components=10, random_state=42)
                    embedding1 = reducer.fit_transform(data1)
                    embedding2 = reducer.fit_transform(data2)
                    
                    ```
                    
                5. **Apply CCA**:
                Use CCA to find the linear combinations of the UMAP embeddings that are maximally correlated.
                    
                    ```python
                    # Apply CCA on UMAP embeddings
                    cca = CCA(n_components=2)  # Number of components to extract
                    cca.fit(embedding1, embedding2)
                    
                    # Transform the data using CCA
                    cca_embedding1, cca_embedding2 = cca.transform(embedding1, embedding2)
                    
                    # Optional: To see the correlation coefficients
                    corrs = [np.corrcoef(cca_embedding1[:, i], cca_embedding2[:, i])[0, 1] for i in range(cca_embedding1.shape[1])]
                    print("Canonical Correlation Coefficients:", corrs)
                    
                    ```
                    
                6. **Visualize the Results**:
                Plot the first two canonical variables to visually inspect the correlation.
                    
                    ```python
                    # Plot the first two canonical variables
                    plt.figure(figsize=(12, 6))
                    
                    plt.subplot(1, 2, 1)
                    plt.scatter(cca_embedding1[:, 0], cca_embedding1[:, 1], c='blue', label='UMAP Dataset 1')
                    plt.title('Canonical Variables of UMAP Dataset 1')
                    plt.xlabel('Canonical Variable 1')
                    plt.ylabel('Canonical Variable 2')
                    plt.legend()
                    
                    plt.subplot(1, 2, 2)
                    plt.scatter(cca_embedding2[:, 0], cca_embedding2[:, 1], c='green', label='UMAP Dataset 2')
                    plt.title('Canonical Variables of UMAP Dataset 2')
                    plt.xlabel('Canonical Variable 1')
                    plt.ylabel('Canonical Variable 2')
                    plt.legend()
                    
                    plt.show()
                    
                    ```
                    
                
                ### Complete Example Code
                
                Here's the complete code for applying CCA on UMAP embeddings and visualizing the results:
                
                ```python
                # Install the required libraries
                !pip install umap-learn numpy scikit-learn matplotlib
                
                # Import libraries
                import numpy as np
                import umap
                from sklearn.cross_decomposition import CCA
                import matplotlib.pyplot as plt
                
                # Generate synthetic data for demonstration
                data1 = np.random.rand(100, 50)  # 100 samples with 50 features
                data2 = np.random.rand(100, 50)  # Another dataset with the same dimensions
                
                # Apply UMAP to both datasets
                reducer = umap.UMAP(n_components=10, random_state=42)
                embedding1 = reducer.fit_transform(data1)
                embedding2 = reducer.fit_transform(data2)
                
                # Apply CCA on UMAP embeddings
                cca = CCA(n_components=2)  # Number of components to extract
                cca.fit(embedding1, embedding2)
                
                # Transform the data using CCA
                cca_embedding1, cca_embedding2 = cca.transform(embedding1, embedding2)
                
                # Optional: To see the correlation coefficients
                corrs = [np.corrcoef(cca_embedding1[:, i], cca_embedding2[:, i])[0, 1] for i in range(cca_embedding1.shape[1])]
                print("Canonical Correlation Coefficients:", corrs)
                
                # Plot the first two canonical variables
                plt.figure(figsize=(12, 6))
                
                plt.subplot(1, 2, 1)
                plt.scatter(cca_embedding1[:, 0], cca_embedding1[:, 1], c='blue', label='UMAP Dataset 1')
                plt.title('Canonical Variables of UMAP Dataset 1')
                plt.xlabel('Canonical Variable 1')
                plt.ylabel('Canonical Variable 2')
                plt.legend()
                
                plt.subplot(1, 2, 2)
                plt.scatter(cca_embedding2[:, 0], cca_embedding2[:, 1], c='green', label='UMAP Dataset 2')
                plt.title('Canonical Variables of UMAP Dataset 2')
                plt.xlabel('Canonical Variable 1')
                plt.ylabel('Canonical Variable 2')
                plt.legend()
                
                plt.show()
                
                ```
                
                ### Explanation
                
                1. **UMAP**: Reduces the dimensionality of the datasets to a more manageable number of components (10 in this case).
                2. **CCA**: Finds the linear combinations of the UMAP embeddings that are maximally correlated.
                3. **Visualization**: Plots the first two canonical variables for both datasets to inspect the correlation visually.
                
                By following this approach, you can effectively use CCA on UMAP embeddings to compare the relationships between two datasets.
                
            - how to itnerpret this: Canonical Correlations: -0.23755626716455025
                
                Interpreting the results from Canonical Correlation Analysis (CCA) involves understanding both the canonical correlations and the correlation coefficients:
                
                ### Canonical Correlations
                
                The canonical correlations indicate the overall relationship between the sets of canonical variables. These values represent the strength of the linear relationships between the two sets of UMAP embeddings.
                
                - **Canonical Correlations**: These are the correlations between the first pair of canonical variables, the second pair, and so on. In your case, the canonical correlation values were found to be:
                    - 0.23755626716455025
                
                The negative value here might indicate an inverse relationship for the first canonical variable pair. Canonical correlations close to 1 or -1 indicate strong linear relationships, while those close to 0 indicate weak relationships.
                
                ### Correlation Coefficients
                
                The correlation coefficients between the transformed UMAP embeddings (canonical variables) represent how well the corresponding pairs of canonical variables correlate with each other.
                
                - **Correlation Coefficients**: These values show the correlation between the pairs of canonical variables. In your case, the coefficients are:
                    - [0.49006658992455354, 0.26686220794459087]
                
                Here's what these coefficients mean:
                
                1. **First Canonical Variable Pair**:
                    - Correlation Coefficient: 0.49006658992455354
                    - This indicates a moderate positive linear relationship between the first pair of canonical variables derived from the UMAP embeddings of the two datasets.
                2. **Second Canonical Variable Pair**:
                    - Correlation Coefficient: 0.26686220794459087
                    - This indicates a weaker positive linear relationship between the second pair of canonical variables.
                
                ### Interpretation Summary
                
                - The first canonical correlation is negative, suggesting an inverse relationship for the first pair of canonical variables.
                - The correlation coefficient for the first canonical variable pair is around 0.49, indicating a moderate positive relationship. This suggests that the first pair of canonical variables derived from the UMAP embeddings have a moderate positive linear association.
                - The correlation coefficient for the second canonical variable pair is around 0.27, indicating a weak positive relationship.
                
                These results suggest that while there is some degree of linear association between the canonical variables derived from the UMAP embeddings of your datasets, the relationships are not very strong. This implies that the structures captured by the UMAP embeddings of the two datasets have moderate to weak linear relationships when examined through the lens of CCA.
                
                ### Improving Interpretability
                
                To further interpret and validate these results, you might consider:
                
                1. **Visual Inspection**:
                    - Plot the pairs of canonical variables to visually inspect their relationships. This can help you understand the nature of the relationships better.
                    
                    ```python
                    plt.figure(figsize=(12, 6))
                    
                    plt.subplot(1, 2, 1)
                    plt.scatter(cca_embedding1[:, 0], cca_embedding2[:, 0], c='blue', label='First Canonical Variable Pair')
                    plt.title('First Canonical Variable Pair')
                    plt.xlabel('First Canonical Variable (Dataset 1)')
                    plt.ylabel('First Canonical Variable (Dataset 2)')
                    plt.legend()
                    
                    plt.subplot(1, 2, 2)
                    plt.scatter(cca_embedding1[:, 1], cca_embedding2[:, 1], c='green', label='Second Canonical Variable Pair')
                    plt.title('Second Canonical Variable Pair')
                    plt.xlabel('Second Canonical Variable (Dataset 1)')
                    plt.ylabel('Second Canonical Variable (Dataset 2)')
                    plt.legend()
                    
                    plt.show()
                    
                    ```
                    
                2. **Dimensionality Reduction Before CCA**:
                    - If the datasets are very high-dimensional, consider using PCA to reduce the dimensionality before applying UMAP and CCA. This can sometimes enhance the interpretability of the canonical variables.
                3. **Investigating Other Relationships**:
                    - If the linear relationships are weak, you might consider investigating non-linear relationships using other methods such as kernel CCA or distance correlation.
                
                By examining these additional aspects, you can gain deeper insights into the relationships between your datasets as captured by UMAP and analyzed by CCA.
                
- ✅ is there an issue with comparing umap due to randomness? how to better quantitatively compare them?
    
    [https://chatgpt.com/c/ca134e95-ac2c-4290-b9c7-107dbeba93fe](https://chatgpt.com/c/ca134e95-ac2c-4290-b9c7-107dbeba93fe)
    
    - umap is NOT random on projection (cosine sim) but becomes random after uniform nearest neighbor
- ✅ [UMAP](../UMAP%206019e8cd74ca4abebc143f9f13760055.md)

Compare SAEs of Different (Small) Models

- ✅ ask #sparse-autoencoders OpenMI slack for prev work (chatgpt doesnt find anything)
    
    Hi, I'm looking to run experiments similar to this section:
    
    [https://transformer-circuits.pub/2023/monosemantic-features#phenomenology-universality](https://transformer-circuits.pub/2023/monosemantic-features#phenomenology-universality)
    
    which involves comparing "different dictionary learning runs trained on different activations from a different transformer with different random seeds but otherwise identical hyperparameters." I was wondering if anyone has also done anything similar to this before (say a blog post / repo) and if they found any additional insights not mentioned by the Towards Monosemanticity paper? Would add to my lit review too
    
    I may not have the resources to train on 100 billion tokens from the pile like Anthropic did, so looking to scale it down or do something similar with toy models, hoping the saes on these toy models would still find "true enough" features that could be compared
    
- ⚠️ **EXPM**: train saes on toy model
    
    Models to Reproduce
    
    [https://colab.research.google.com/drive/1elITv-IptxH-J8aeDDvjXLNsu7p5JbxL#scrollTo=Gh3FW5X2BrsM](https://colab.research.google.com/drive/1elITv-IptxH-J8aeDDvjXLNsu7p5JbxL#scrollTo=Gh3FW5X2BrsM)
    
    - [https://www.lesswrong.com/posts/z6QQJbtpkEAX3Aojj/interim-research-report-taking-features-out-of-superposition](https://www.lesswrong.com/posts/z6QQJbtpkEAX3Aojj/interim-research-report-taking-features-out-of-superposition)
    - [https://www.lesswrong.com/posts/a5wwqza2cY3W7L9cj/sparse-autoencoders-find-composed-features-in-small-toy](https://www.lesswrong.com/posts/a5wwqza2cY3W7L9cj/sparse-autoencoders-find-composed-features-in-small-toy)
    - [https://transformer-circuits.pub/2023/monosemantic-features#problem-setup](https://transformer-circuits.pub/2023/monosemantic-features#problem-setup)
        - NOTE: these are not toy models, just 1L models, because trained on 100 billion tokens, so may not be reproducible. Try toy models.
        - ✅ Model Dataset and Sizes
            
            ![Untitled](Done%201c002201437341e48b55b8276859a632/Untitled%202.png)
            
        - ✅ training feasibility how-to
            - [https://chatgpt.com/c/13d7b189-1900-439f-ba71-a2a478416f7e](https://chatgpt.com/c/13d7b189-1900-439f-ba71-a2a478416f7e)
            - [https://transformer-circuits.pub/2023/monosemantic-features#setup-transformer](https://transformer-circuits.pub/2023/monosemantic-features#setup-transformer)
            - [https://transformer-circuits.pub/2023/monosemantic-features#appendix-transformer](https://transformer-circuits.pub/2023/monosemantic-features#appendix-transformer)
        - ✅ tokenizer
            
            BPE tokenizer: **Byte-Pair Encoding tokenization**
            
            [https://arxiv.org/pdf/2101.00027](https://arxiv.org/pdf/2101.00027)
            
            We analyze the distribution of document lengths, as well as the number of bytes-per-token using the GPT-2 tokenizer
            
        - ISSUE: on `train_loader`, FileNotFoundError: [https://the-eye.eu/public/AI/pile/train/00.jsonl.zst](https://the-eye.eu/public/AI/pile/train/00.jsonl.zst)
    - No_Position_Experiment.ipynb: [https://colab.research.google.com/github/TransformerLensOrg/TransformerLens/blob/main/demos/No_Position_Experiment.ipynb#scrollTo=seo_rX_d1uO6](https://colab.research.google.com/github/TransformerLensOrg/TransformerLens/blob/main/demos/No_Position_Experiment.ipynb#scrollTo=seo_rX_d1uO6)
    - ARENA 1.4: Training Toy Model with Superposition
        
        [https://colab.research.google.com/drive/1mHKZpkhYAr0WWAQo2Y6pXL08yNfJHOVx?usp=sharing#scrollTo=MtjKlA3D5DS0](https://colab.research.google.com/drive/1mHKZpkhYAr0WWAQo2Y6pXL08yNfJHOVx?usp=sharing#scrollTo=MtjKlA3D5DS0)
        
    - nanda tutorail: [https://colab.research.google.com/drive/1u8larhpxy8w4mMsJiSBddNOzFGj7_RTn?usp=sharing](https://colab.research.google.com/drive/1u8larhpxy8w4mMsJiSBddNOzFGj7_RTn?usp=sharing)
- ✅ [Ashkan meeting notes](../Ashkan%20meeting%20notes%20cf47680d80a04812ac616fd4597e9e09.md)
- ✅ summary to fazl
    
    Hi, as a quick summary of last week, I was running experiments and researching for a new project topic I can discuss with you next meeting. After some discussions with the other interns and lab members such as Ashkan, I decided this new project was more novel and impactful. The topic is about improving the understanding of SAE feature universality via geometric metrics such as canonical correlation analysis. Essentially, it is an extension of this Anthropic work: [https://transformer-circuits.pub/2023/monosemantic-features#phenomenology-universality](https://transformer-circuits.pub/2023/monosemantic-features#phenomenology-universality)
    
    My approach, which has not been tried yet on SAE feature space, uses geometric measurement techniques similar to (Kornblith et al, 2019),  “Similarity of Neural Network Representations Revisited” (of which Geoffrey Hinton is a coauthor). My project’s aim is also similar to that paper.
    
    I talked with other interns who offered good advice for the next experimental steps. I also presented the project to Ashkan, who gave a lot of other good advice in our meeting and found the proposed approach to be viable and interesting. 
    
- ✅ [Sim of NN revisted](../Repr%20sim%20papers%20f1e073e6e4124d3ba7b6929d92cee13d/Sim%20of%20NN%20revisted%2074743e14a51b4f7593e67ad7b2e92162.md)
- ✅ [**Sholto Douglas & Trenton Bricken - How to Build & Understand GPT-7's Mind**](https://www.youtube.com/watch?v=UTuuTTnjxMQ&ab_channel=DwarkeshPatel)
    - deception circuit
    - universality
    - doing research part-time into residency
- ✅ **EXPM**: CCA on pretrained SAEs (across models)
    
    [CM_pretrained_SAE_save_actvs](https://colab.research.google.com/drive/1hzWwIq0iULPvZt-GFnY8TPNvqZiDgsen#scrollTo=V5O39_ub_e0_)
    
    - ✅ load two SAEs : gpt2, gemma-2b
        - latest loading nb: https://github.com/jbloomAus/SAELens
        - [https://jbloomaus.github.io/SAELens/sae_table/](https://jbloomaus.github.io/SAELens/sae_table/)
            - [https://chatgpt.com/c/56aeb74d-8e2d-4673-a087-bdef0e1e37f6](https://chatgpt.com/c/56aeb74d-8e2d-4673-a087-bdef0e1e37f6)
            - [https://www.lesswrong.com/posts/f9EgfLSurAiqRJySD/open-source-sparse-autoencoders-for-all-residual-stream](https://www.lesswrong.com/posts/f9EgfLSurAiqRJySD/open-source-sparse-autoencoders-for-all-residual-stream)
    - ✅ get LLM then SAE actvs and save to drive
    
    [CM_pretrained_SAE_UMAP_CCA.ipynb](https://colab.research.google.com/drive/1lDWBYXwKSxOiwJzILvedjMCxNCkT0xsG#scrollTo=kUYRF57KNxrL)
    
    - ✅ for every pair of their middle layers, run UMAP then CCA
        - make sure you use UMAP correctly
        - [https://chatgpt.com/c/ca93999b-8aab-40e7-b5cf-fbacbb639bc6](https://chatgpt.com/c/ca93999b-8aab-40e7-b5cf-fbacbb639bc6)
- ⚠️ **EXPM**: Find features with high actv corr in pretrained SAEs (across models)
    
    [actv_corr_mat.ipynb](https://colab.research.google.com/drive/1iM4Ta6NLR9Ka4sG6q9YUzpla-Rezm0bx#scrollTo=qdOPsIx9vHIH)
    
    - ✅ "For each feature in run A/1, we find the closest feature by activation similarity in run B/1," what's an efficient algorithm to do this?
        
        [https://chatgpt.com/c/38c634db-f342-480d-bbf7-3371938dca51](https://chatgpt.com/c/38c634db-f342-480d-bbf7-3371938dca51)
        
    - ✅ BRUTE FORCE: for each input sample, get actvs for all features. a batch sample of N has N x F activations. So there are F vectors of size N. In the second SAE, ther are F_2 vectors of size N. We can take the cosine sim of every F vector with every F_2 vector to get a cosine sim, and find the highest
        - ✅ load saved actvs
        - cosine sim mat: [https://chatgpt.com/c/100362a0-be1e-4bc1-97ca-a97fed673706](https://chatgpt.com/c/100362a0-be1e-4bc1-97ca-a97fed673706)
            
            [https://claude.ai/chat/ca272816-0223-49f4-9660-bbf6cb726061](https://claude.ai/chat/ca272816-0223-49f4-9660-bbf6cb726061)
            
            - NOTE: this is not 1-1 mapping, but each feature has a ranking
        - ✅ given cosine_sim_matrix , for each feature in A, find the top 3 features in B, and vice versa. make this into a function.
        - function that finds the top 5 pairs with the highest sim
            - compare these on neuronpedia
                - jump to feature: [https://www.neuronpedia.org/gpt2-small](https://www.neuronpedia.org/gpt2-small)
                - ISSUE: can’t jump to feature for L12 of gemma-2b, only L6
                - Save gemma L6 feat actvs
    - ⚠️ Reproduce Anthropic’s A vs B actvs plot
        - ✅ take a slice of last dim of (batch*seq, features) for each A and B
        - ✅ is this nonzero actvs? most tokens should be 0 for one feature
            
            no; plot says most actvs are around 0, if you look at the long line of pts at each axis’s 0 that represents how those pts are 0 at A but zero or nonzero at B, etc.
            
        - what data pts do they use? every (btach, seq) of a sample?
            - two features would be similar in this sense if they take similar values over a diverse set of data.
                - they cite SVCCA. So they must’ve tried it. once you try your obvious cca approaches, ask them what issues there were with it, and if any issues with yours.
        - ✅ how come get nans in corrcoeff
            
            If you're getting NaN values in the correlation coefficient calculation, it's usually due to one of these reasons:
            
            1. Constant values: If all values in one or both of the tensors are the same (i.e., the tensor has zero variance), the correlation coefficient will be undefined (NaN).
            2. Presence of NaN or infinity values: If your tensors contain NaN or infinity values, these will propagate through the correlation calculation.
            3. All zero values: If one or both tensors contain all zeros, this can also lead to NaN in the correlation calculation.
            
            To diagnose and fix this issue, you can try the following:
            
            1. Check for constant values:
            
            ```python
            print("A constant?:", torch.all(tensor_A == tensor_A[0]))
            print("B constant?:", torch.all(tensor_B == tensor_B[0]))
            
            ```
            
            1. Check for NaN or infinity values:
            
            ```python
            print("A has NaN:", torch.isnan(tensor_A).any())
            print("B has NaN:", torch.isnan(tensor_B).any())
            print("A has inf:", torch.isinf(tensor_A).any())
            print("B has inf:", torch.isinf(tensor_B).any())
            
            ```
            
            1. Check for all zero values:
            
            ```python
            print("A all zeros?:", torch.all(tensor_A == 0))
            print("B all zeros?:", torch.all(tensor_B == 0))
            
            ```
            
            1. If you're still getting NaNs, you can try to calculate the correlation manually:
            
            ```python
            def manual_correlation(x, y):
                x_mean = x.mean()
                y_mean = y.mean()
                x_std = x.std()
                y_std = y.std()
            
                if x_std == 0 or y_std == 0:
                    return 0  # or you might want to return NaN here
            
                return ((x - x_mean) * (y - y_mean)).mean() / (x_std * y_std)
            
            corr = manual_correlation(tensor_A, tensor_B)
            print("Manual correlation:", corr)
            
            ```
            
            1. If you're dealing with very small numbers, numerical precision issues could arise. In this case, you might want to scale your data:
            
            ```python
            tensor_A_scaled = (tensor_A - tensor_A.mean()) / tensor_A.std()
            tensor_B_scaled = (tensor_B - tensor_B.mean()) / tensor_B.std()
            correlation = np.corrcoef(tensor_A_scaled.numpy(), tensor_B_scaled.numpy())[0, 1]
            
            ```
            
            After applying these checks and potential fixes, you should be able to identify the cause of the NaN values and address it appropriately. If you're still having issues, you might want to examine a small subset of your data to see if there are any unexpected patterns or values.
            
        - if A is first feature vector and so is B (For two models), is this is the same as their corrcoef: cosine_sim_matrix[0][0]
            
            You're on the right track, but there's an important distinction to make between correlation coefficients and cosine similarity. While they're related, they're not exactly the same. Let's break this down:
            
            1. Correlation coefficient (Pearson's r):
                - Measures the linear relationship between two variables
                - Ranges from -1 to 1
                - Is invariant to scaling and shifting of the variables
            2. Cosine similarity:
                - Measures the cosine of the angle between two vectors in a multi-dimensional space
                - Ranges from -1 to 1 for real numbers (1 for identical orientation, 0 for orthogonal, -1 for opposite orientation)
                - Is invariant to scaling but not to shifting (direction)
            
            In many cases, especially when dealing with centered data (mean = 0), the cosine similarity and the Pearson correlation coefficient will be very close or even identical. However, they can differ significantly if the data is not centered.
            
            Given your context:
            
            - If `A` is the first feature vector from one model and `B` is the first feature vector from another model
            - And `cosine_sim_matrix[0][0]` represents the cosine similarity between these two vectors
            
            Then `cosine_sim_matrix[0][0]` would indeed give you the cosine similarity between the first feature vectors of the two models. This is often a good measure of how similar the features are across models.
            
            To compare this with the correlation coefficient:
            
            ```python
            import numpy as np
            from scipy.spatial.distance import cosine
            
            # Assuming A and B are your feature vectors (as numpy arrays or torch tensors)
            A = ...  # Your first feature vector from model A
            B = ...  # Your first feature vector from model B
            
            # Convert to numpy if they're torch tensors
            if torch.is_tensor(A):
                A = A.numpy()
            if torch.is_tensor(B):
                B = B.numpy()
            
            # Cosine similarity
            cosine_sim = 1 - cosine(A, B)  # cosine() returns distance, so we subtract from 1
            
            # Correlation coefficient
            correlation = np.corrcoef(A, B)[0, 1]
            
            print(f"Cosine similarity: {cosine_sim}")
            print(f"Correlation coefficient: {correlation}")
            
            ```
            
            If your data is centered (mean subtracted), these values should be very close. If not, they might differ. The choice between cosine similarity and correlation coefficient depends on your specific needs:
            
            - Use cosine similarity if you're interested in the angle between the vectors regardless of their magnitudes or if you want to ignore constant offsets.
            - Use correlation coefficient if you're specifically interested in linear relationships and want to account for both the angle and the spread of the data.
            
            In the context of comparing feature activations across models, cosine similarity is often preferred because it focuses on the direction of the feature vectors rather than their exact magnitudes.
            
        - is "not invariant shifting" meaning will have diff values if translate vectors say diff origin, but not direction?
            
            You've got it exactly right. Let me break this down to clarify:
            
            1. "Not invariant to shifting" means that if you translate the vectors (i.e., add a constant to all elements), the cosine similarity can change.
            2. This is in contrast to the direction of the vectors, which remains unchanged by translation.
            
            Here's a simple example to illustrate:
            
            Let's say we have two vectors:
            A = [1, 2, 3]
            B = [2, 3, 4]
            
            The cosine similarity between A and B will be some value, let's call it X.
            
            Now, if we shift both vectors by adding 10 to each element:
            A' = [11, 12, 13]
            B' = [12, 13, 14]
            
            The cosine similarity between A' and B' will be different from X.
            
            However, the direction of the vectors in space remains the same. If you were to plot these vectors, A and A' would point in the same direction, as would B and B'.
            
            This property is why cosine similarity is often used in text analysis and recommendation systems where the magnitude of the vectors might not be as important as their direction.
            
            In contrast, correlation coefficient is invariant to both scaling and shifting. If you add a constant to all elements of both vectors, the correlation coefficient will remain the same.
            
            This difference can be important depending on your specific application and what aspect of the data you're most interested in comparing.
            
        - give equation for corr coeff
            
            Certainly! The equation for the correlation coefficient, specifically Pearson's correlation coefficient, is as follows:
            
            r = Σ((x_i - x̄)(y_i - ȳ)) / (√Σ(x_i - x̄)² * √Σ(y_i - ȳ)²)
            
            Where:
            
            - r is the Pearson correlation coefficient
            - x_i and y_i are individual sample pairs
            - x̄ is the mean of all x values
            - ȳ is the mean of all y values
            - Σ represents the sum over all samples
            
            This can also be written as:
            
            r = cov(X,Y) / (σ_X * σ_Y)
            
            Where:
            
            - cov(X,Y) is the covariance of X and Y
            - σ_X is the standard deviation of X
            - σ_Y is the standard deviation of Y
            
            In computational terms, you might see it implemented like this:
            
            r = Σ((x_i - x̄)(y_i - ȳ)) / (n * σ_X * σ_Y)
            
            Where n is the number of samples.
            
            This formula calculates the normalized measure of the covariance between two variables X and Y, giving a value between -1 and 1, where:
            
            - 1 indicates a perfect positive linear correlation
            - 0 indicates no linear correlation
            - 1 indicates a perfect negative linear correlation
            
            The correlation coefficient measures both the strength and direction of the linear relationship between two variables.
            
    - ⚠️ reproduce their plot of finding highest mapping for each feature
        
        ![Untitled](Done%201c002201437341e48b55b8276859a632/Untitled%203.png)
        
    - ✅ ask #neuronpedia for pretrained SAEs
        
        I saw in sae_table that there’s SAEs for the GPT2 small, Gemma-2B, and Mistrial-7B models. I also see several pretrained SAEs on other models (Llama-3, PMs, etc). I was wondering if there’s a list of links to uploaded pretrained SAEs in general (eg. GeLU-1L, tinystories, GPT2-medium)? 
        
        I’m guessing people may have filled out the form to upload them to Neuronpedia too and they’re currently being processed. Also, as seen in sae_table, we can load gemma-2b-res-jb layer 12 post, but not search/steer it on Neuronpedia. I was wondering why? Also, were there only SAEs for L0, L6 and L12 due to cost?
        
        - reply
            
            Those wouldn't be hard to train with SAE Lens :slightly_smiling_face: and if you do, happy to support them. We're a little busy right now but in general we'd be willing to train SAEs for researchers 
            
        
        Thanks again! I'm planning this week to train saes on gpt2 style models (was looking into training toy model llms with only different initializations, but thought to first train saes without needing to train llms) on nodes in my lab. When you say willing to train saes do you mean to help with resources?
        
    - ✅ ask callum for lit review and saes
        
        Hi, to follow up on my project to compare feature geometries across models, I'm looking to run experiments similar to this section:[https://transformer-circuits.pub/2023/monosemantic-features#phenomenology-universality](https://transformer-circuits.pub/2023/monosemantic-features#phenomenology-universality)which involves comparing "different dictionary learning runs trained on different activations from a different transformer with different random seeds but otherwise identical hyperparameters." I was wondering if anyone has also done anything similar to this before (say a blog post / repo) and if they found any additional insights not mentioned by the Towards Monosemanticity paper? Would add to my lit review tooAlso, aside from the saelens list of pretrained models, GPT2 small, Gemma-2B, and Mistrial-7B models, I also see several pretrained SAEs on other models (Llama-3, PMs, etc). I was wondering if there’s a list of links to uploaded pretrained SAEs in general (eg. GeLU-1L, tinystories, GPT2-medium)? Hopefully with for models with the same tokenizers like gpt2 small and medium. Thanks!
        
        I was listening to a podcast with Trenton Bricken and he mentioned he's still doing work with universality, I assume he's looked into techniques like cca or cka though I have some other ideas with finding and comparing higher order structures
        
    - ⚠️ ISSUE: different tokenizers
        - ✅ do gpt2 and gemma-2b use diffrent tokenizer
            
            [https://chatgpt.com/c/7e74ddc0-0694-46da-9b4a-447ee68093c2](https://chatgpt.com/c/7e74ddc0-0694-46da-9b4a-447ee68093c2)
            
        - ✅ Did they plot by tokens or samples? It looks like by tokens of samples
            - Universality is NOT just one section of the paper, but within each feature in ‘feature-analysis’
                - [https://transformer-circuits.pub/2023/monosemantic-features#feature-arabic](https://transformer-circuits.pub/2023/monosemantic-features#feature-arabic)
                - We give each token an "Arabic script" score
            - thus, umap plotting the batch*seq is right?
        - ✅ can you use canonical corerlation analysis on two matrices with all diff dims
            
            Canonical Correlation Analysis (CCA) is a statistical method used to understand the relationship between two sets of variables. It finds linear combinations of the variables in each set such that the correlation between these combinations is maximized. However, for CCA to be applicable, the two matrices must meet certain requirements regarding their dimensions:
            
            1. **Number of Samples (Rows):** Both matrices must have the same number of samples (rows). CCA requires that each row corresponds to a paired observation across the two matrices.
            2. **Number of Features (Columns):** The number of features (columns) can differ between the two matrices. That is, one matrix can have more features than the other.
            
            For example, if you have two matrices \( X \) and \( Y \):
            
            - \( X \) is of shape \( (n, p) \)
            - \( Y \) is of shape \( (n, q) \)
            
            Here, \( n \) is the number of samples (which must be the same for both matrices), while \( p \) and \( q \) are the number of features in matrices \( X \) and \( Y \) respectively (which can be different).
            
            In summary, as long as the two matrices have the same number of rows (samples), CCA can be applied, even if the number of columns (features) in each matrix is different.
            
        - ✅ [Perhaps just use last token of each sample](https://colab.research.google.com/drive/1iM4Ta6NLR9Ka4sG6q9YUzpla-Rezm0bx#scrollTo=5HHD5vQixRfk&line=1&uniqifier=1)
            - this still has issue bc not always the same token
        
        what if two LLMs use different tokenizer? then how do you compare if they have the same tokens? for now, try to compare LLMs with same tokenizer.
        
- ✅ ssh access into [Torr nodes](../Compute%20e3182612433a4299b4035d5359548fa4/Torr%20nodes%203b93e6da492c4d519d6343510fc46f14.md)
- ✅ **EXPM**: first train gpt2-style saes in colab (before torrnodes)
    - ✅ ask amir for advice
        
        hi, as part of my project, I'm looking to extend the results of
        [https://transformer-circuits.pub/2023/monosemantic-features#phenomenology-universality](https://transformer-circuits.pub/2023/monosemantic-features#phenomenology-universality)
        
        in which they compare sae feature activations (of a dataset) for two 1-layer LLMs trained on The Pile with 100 billion tokens. Given that's infeasible for me, I'm looking to train 2 toy model LLMs and compare their saes with CCA, etc. The pretrained SAElens models are too different to compare (eg. gpt2, gemma, mistrial use diff tokenizers). I was wondering if you have any advice for picking the params for the toy models and their saes, and est time + costs? thanks!
        
    - amir reply
        
        For the toy models, it depends on the tasks. For stuff like 6 digit addition, I've seen two layer transformers do really well. (Apparently going from 1 layer to 2 or 3 works better.)
        
        For the SAE's, the most important parameters are the regularization loss and the hidden state size of the autoencoder. For a "toy" model, I wouldn't expect you'd need very high hidden dimension, since its lower complexity than a full LLM. Something like 1/2 to 1x of the MLP dimension should be more than enough. For the regularization l1 loss, you might need to play with that parameter more since its more sensitive. But I'd guess somewhere in the 0.01 to 0.1 range should be plenty.
        
    - ✅ tinystories: just uses saelens tutorial code!
        - already trained an sae in the saelens tutorial
            
            [training_a_sparse_autoencoder.ipynb](https://colab.research.google.com/github/jbloomAus/SAELens/blob/main/tutorials/training_a_sparse_autoencoder.ipynb#scrollTo=hFz6JUMuOVHv)
            
        
        [**TinyStories: The Smallest GPT with Coherent English (by Microsoft)**](https://www.reddit.com/r/LocalLLaMA/s/y2XYlDJkxX)
        
        [https://huggingface.co/calum/tinystories-gpt2-3M](https://huggingface.co/calum/tinystories-gpt2-3M)
        
    - ✅ compile tips: [https://www.lesswrong.com/posts/f9EgfLSurAiqRJySD/open-source-sparse-autoencoders-for-all-residual-stream](https://www.lesswrong.com/posts/f9EgfLSurAiqRJySD/open-source-sparse-autoencoders-for-all-residual-stream)
    
    [Train GPT-Tinystories SAEs](../Train%20GPT-Tinystories%20SAEs%20abef355b40764a00a733b84513bda85b.md) 
    
    - ✅ [`torch.save`](http://torch.save) into drive as `tiny-stories-1L-21M_sae_v1.pth`
    - ✅ train saes for `tiny-stories-1M` and `tiny-stories-3M`  [(also many others)](https://transformerlensorg.github.io/TransformerLens/generated/model_properties_table.html)
        - just change model name in traiing cell of saelen’s tuotiral! A100.
        - choose models
            - tiny-stories-instruct-1M vs tiny-stories-1M
                
                The "Tiny Stories" datasets are collections of small, narrative texts designed to aid in language modeling and understanding for AI systems. These datasets are part of the growing field of AI and machine learning, which seeks to develop and improve upon models that can generate, understand, and interact with human-like text.
                
                ### Tiny Stories Instruct 1M
                
                **Purpose:**
                
                - The Tiny Stories Instruct 1M dataset is tailored for instructional and guiding purposes, often designed to train models to follow specific instructions or perform certain tasks.
                
                **Features:**
                
                - **Instructional Content:** Contains text that gives specific instructions, examples, or tasks for the model to perform. This can include question-answer pairs, directive text, or educational content.
                - **Task-Oriented:** Aimed at improving the model's ability to follow human-like instructions and complete predefined tasks accurately.
                - **Structure:** The dataset is likely organized in a format where instructions and responses are clearly delineated, providing a structured learning environment for the model.
                
                **Use Cases:**
                
                - Ideal for training models that need to perform tasks based on specific instructions.
                - Useful for creating AI systems that assist with educational tools, customer service bots, or any application requiring precise task completion.
                
                ### Tiny Stories 1M
                
                **Purpose:**
                
                - The Tiny Stories 1M dataset focuses on general narrative text, designed to enhance a model's ability to generate coherent and creative stories.
                
                **Features:**
                
                - **Narrative Content:** Comprises a vast array of short, self-contained stories. These stories are typically rich in narrative structure and elements such as characters, plot, and setting.
                - **Creativity and Coherence:** Aims to improve the model's capability in storytelling, enhancing its ability to generate human-like, engaging, and coherent narratives.
                - **Variety:** Likely includes a wide range of genres, themes, and styles to provide a broad training ground for creative text generation.
                
                **Use Cases:**
                
                - Suitable for training models intended for creative writing, content generation, and entertainment.
                - Useful in applications such as story generation tools, interactive fiction, and creative content platforms.
                
                ### Key Differences
                
                1. **Content Focus:**
                    - **Instruct 1M:** Instructional and task-oriented text.
                    - **1M:** General narrative and storytelling text.
                2. **Purpose:**
                    - **Instruct 1M:** Train models for following instructions and completing tasks.
                    - **1M:** Train models for creative writing and generating coherent narratives.
                3. **Structure:**
                    - **Instruct 1M:** Structured around instructions and responses.
                    - **1M:** More fluid and varied narrative structures.
                4. **Use Cases:**
                    - **Instruct 1M:** Educational tools, customer service, task automation.
                    - **1M:** Creative writing, story generation, interactive fiction.
                
                By understanding these distinctions, developers and researchers can select the appropriate dataset based on their specific needs and goals in the field of AI and language modeling.
                
            - which of these models are gpt2 style and use the same tokenizer:
            [https://transformerlensorg.github.io/TransformerLens/generated/model_properties_table.html](https://transformerlensorg.github.io/TransformerLens/generated/model_properties_table.html)
                
                [https://chatgpt.com/c/9980e4f9-b69e-4119-8b15-523671d470bc](https://chatgpt.com/c/9980e4f9-b69e-4119-8b15-523671d470bc)
                
                this HALLUCINATES tinystories-gpt2-small
                
        - choose gpus
            
            1L-21M: Way too slow on T4
            
            epochs is batchsize * train_steps. Only gets to 33% in an hr. 
            
            - is M3 max faster than T4 or A100
                
                When comparing the Apple M3 Max, NVIDIA A100, and NVIDIA Tesla T4 in terms of performance, each GPU excels in different areas, which makes them suited for different types of workloads.
                
                1. **Apple M3 Max**:
                    - The M3 Max, with its 40-core GPU, is designed for high-performance computing in laptops, particularly in graphics and machine learning applications. It is built on a 5nm process technology, which allows for greater efficiency and lower power consumption compared to its competitors. However, detailed benchmarks comparing it directly to the A100 and T4 are scarce due to the different application focus (laptop vs. workstation GPUs)【5†source】【6†source】.
                2. **NVIDIA A100**:
                    - The A100 is a powerhouse for deep learning and AI workloads. It boasts 19.5 TFLOPS of FP32 performance and 312 TFLOPS of FP16 Tensor Core performance, making it significantly faster in terms of raw computational power compared to the M3 Max and T4. It is built on a 7nm process and designed for data centers, offering substantial improvements in training and inference tasks due to its advanced tensor cores and large memory bandwidth【6†source】.
                3. **NVIDIA Tesla T4**:
                    - The T4, while not as powerful as the A100, provides a good balance between performance and power efficiency. It has lower power consumption (75W compared to the A100's 400W) and is more cost-effective. It is suitable for inferencing tasks and provides decent performance in deep learning workloads, albeit not at the same level as the A100【7†source】【8†source】.
                
                **Performance Comparison**:
                
                - **Deep Learning**: The A100 outperforms both the M3 Max and T4 significantly in deep learning tasks due to its superior tensor core performance and higher memory bandwidth.
                - **Power Efficiency**: The T4 is the most power-efficient, making it suitable for environments where power consumption is a critical factor.
                - **General Computing**: The M3 Max offers strong performance for general computing and graphics tasks, particularly in a mobile form factor.
                
                In conclusion, if you are looking for the highest performance in deep learning, the A100 is the best choice. For a balance between cost, power consumption, and performance, especially for inferencing tasks, the T4 is suitable. For high performance in a mobile form factor, the M3 Max is a strong contender.
                
        - `tiny-stories-1M`
            
            [train_gpt2_tinsto_sae_v2.ipynb](https://colab.research.google.com/drive/14xzZkdf_4H4kZu184XhfpBLSAG3x5mlR#scrollTo=PJuT3FEn_ku3)
            
            `save_path = 'tiny-stories-1M_MLP0_sae.pth’`
            
            no need load model; just change:
            
            1. `model_name` and 
            2. `wandb_project` in `cfg = LanguageModelSAERunnerConfig. wandb_project` to `tiny-stories-1M_MLP0_sae`. 
            3. Look at d_model col of [https://transformerlensorg.github.io/TransformerLens/generated/model_properties_table.html](https://transformerlensorg.github.io/TransformerLens/generated/model_properties_table.html) OR model.cfg.`d_model`  (if loaded model) to change `d_in`. 
            4. Change `save_path` filename too
        - tiny-stories-3M
            
            train_tiny-stories-3M_sae.ipynb
            
- ✅ ⚠️ **EXPM**: feature mapping actvs on tinystories
    
    [tinystories_get_featActvs_v1.ipynb](https://colab.research.google.com/drive/1WzN6JDecF6M5Z8VCJmzlSo6nIGq4Up8G#scrollTo=qaB5T9asFU6j) 
    
    - ✅ load saes in new nb
        
        To get feature actvs, use sae_lens class method. To do this, you must load the sae as the sae class (wrapper over torch model).
        
        - [https://github.com/jbloomAus/SAELens/blob/main/sae_lens/sae.py](https://github.com/jbloomAus/SAELens/blob/main/sae_lens/sae.py)
            - see how to load in: `def load_from_pretrained(`)
            - need to load cfg dict (from json) into sae wrapper
                - When viewing`cfg_dict` (see `basic_loading_and_analysing.ipynb`), it’s a dict, and not the same as `cfg=LanguageModelSAERunnerConfig` used as input to training the SAE
                - **SOLN**: `cfg.to_dict()`
            - ISSUE: TypeError: SAEConfig.**init**() missing 1 required positional argument: 'finetuning_scaling_factor'
                
                ```jsx
                cfg_dict = cfg.to_dict()
                sae_cfg = SAEConfig.from_dict(cfg_dict)
                ```
                
                See SAEconfig: [https://github.com/jbloomAus/SAELens/blob/main/sae_lens/sae.py#L31](https://github.com/jbloomAus/SAELens/blob/main/sae_lens/sae.py#L31)
                
                POSS SOLN: If you add `cfg_dict['finetuning_scaling_factor'] = 0` then you can pass it to SAEconfig, but this might have issues.
                
    - actually, sae_lens ALREADY has a `sae.save_model`
        - `save_model()` shows you just use `cfg.to_dict()` to turn `LanguageModelSAERunnerConfig`  into json
        - Gives it a path in colab files, and it makes a folder with cfg json and saves model using `from safetensors.torch import save_file`. Then copy folder to drive.
    - 🐣 can also download saes from wandb and put on hf
        
        [https://colab.research.google.com/github/jbloomAus/SAELens/blob/main/tutorials/training_a_sparse_autoencoder.ipynb#scrollTo=er3H1TDoOVHw](https://colab.research.google.com/github/jbloomAus/SAELens/blob/main/tutorials/training_a_sparse_autoencoder.ipynb#scrollTo=er3H1TDoOVHw)
        
        - You can download the resulting sparse autoencoder / sparsity estimate from wandb and upload them to huggingface if you want to share your SAE with other.
            - cfg.json (training config)
            - sae_weight.safetensors (model weights)
            - sparsity.safetensors (sparsity estimate)
    - interpret features using dataset examples
        - ✅ see interp code: [gpt2Small_pretrained_steering_v1](https://colab.research.google.com/drive/1IUtIe0D6UBAJYlPC4eJl00l8fmpohhKG#scrollTo=V0VeMKEJAQTf).ipynb
            - No, this uses new vers: [CM_pretrained_SAE_save_actvs.ipynb](https://colab.research.google.com/drive/1hzWwIq0iULPvZt-GFnY8TPNvqZiDgsen#scrollTo=EMHpFpBz2gri)
        - ✅ load tinystories dataset of certain samples
            - ✅ Load and transform to right format: [https://huggingface.co/datasets/apollo-research/roneneldan-TinyStories-tokenizer-gpt2](https://huggingface.co/datasets/apollo-research/roneneldan-TinyStories-tokenizer-gpt2)
                - This is just token ids, not the dataset examples. We can turn them into text but no need to do that when they already exist in [https://huggingface.co/datasets/roneneldan/TinyStories](https://huggingface.co/datasets/roneneldan/TinyStories)
                - But we should get them as token ids.
                    - Look at TL’s `tokenize_and_concatenate`. That fn works on a hf dataset TEXT as input, and requires not loading it as streaming
                    - ALT: how to take a list of token_ids and turn them into a pytorch tensor. then stack a bunch in a loop over a dataset of lsit of token_ids
                        
                        [https://chatgpt.com/c/24409ae6-1238-4070-950e-45dfb889709c](https://chatgpt.com/c/24409ae6-1238-4070-950e-45dfb889709c)
                        
                - get them as a batch using `token_dataset[:32]["tokens"]`
        - ✅ run tokens through LLM, hook actvs, THEN sae feature actvs
        - ✅ dataset examples on top 5 highest sae feature actvs
            - prev code used older saelens so update
        - ⚠️ you can also just use Neuronpedia feature dashboards
            
            [https://colab.research.google.com/github/jbloomAus/SAELens/blob/main/tutorials/basic_loading_and_analysing.ipynb#scrollTo=BxluyNRBv612](https://colab.research.google.com/github/jbloomAus/SAELens/blob/main/tutorials/basic_loading_and_analysing.ipynb#scrollTo=BxluyNRBv612)
            
- ✅ ISSUE: MLP_0_out has 0.39% nonzero features, so train on diff layer!
    - ✅ 1L-21M was fine tuend to get good features in tutorial already, so use that one as one model
        
        frist check how many nonzero features it has to ensure it actually is good
        
        tinystories_get_featActvs_21M_1L.ipynb
        
        for 32 samples, 13% nonzeroes, so okay
        
        But most are boring, highly activating on “a” or “the”
        
        in your batch, get ones that activate on others
        
    - ✅ were tiny-stories-1L-21M and tiny-stories-instruct-1L-21M initialzied differently? how different are they? or is one fine tuned from the other?
        
        Yes, that’s correct. TinyStories-Instruct-1L-21M was not initialized differently in terms of its base weights. It was fine-tuned from the pre-trained TinyStories-1L-21M model. The fine-tuning process involves taking the pre-trained TinyStories-1L-21M model and further training it on an instructional dataset to enhance its ability to understand and follow instructions. Therefore, TinyStories-Instruct-1L-21M retains the base model's initialization and capabilities but gains additional skills through the fine-tuning process.
        
    - ✅ [train_tiny-stories-2L-33M.ipynb](https://colab.research.google.com/drive/1Oyz0uoP7LgB4fBcYE40RJh02J5GfsHIh#scrollTo=trabeLxABN6o)
        
        train_tiny-stories-2L-33M_MLP1.ipynb
        
        train on both its MLPs
        
        remember to change `hook_layer=0`  in cfg!
        
        NOTE: put mount drive in START of nb bc if you mount after training but your browsr isn’t open, the run will auto shut off (mount failed) and you won’t save model
        
        NOTE: before leaving it to run, also put in wandb api key when run train cell (only need to do once per colab run)
        
- ✅ [kiho meeting 2](../Kiho%20e23ba8681d5d4f0688740c8974f03758/kiho%20meeting%202%203900465d2b7f45639e8dd1e48d97706e.md)
- ✅ Reorder slides ‘expms done’ to show most relevant, not by-date (eg. ‘found features active in tinystories’ is first, then issues with pretrained tokenizers to think about, then love-hate decomposition, etc). Add hinton’s paper
- ✅ ISSUE: this line `top_acts_values, top_acts_indices = feature_acts_2.topk(feat_k, dim=-1)` doesn’t make sense and neither does `for feature_idx in top_acts_indices[0, -1, :]`, because those take the top features for each (batch, seq), then we loop over only the top features for the first sample and last pos. That made sense for a single sample, but not here.
    - TRY: in `tinystories_actv_save.ipynb`, run interpret features on top features in matching pair with model B, vice versa
- ✅ get top N highest matching feature pairs, and interpret each feature using dataset examples
    
    `tinystories_actv_save`
    
    `tinystories_actv_corr_mat_v1.ipynb`
    
    In a separate nb, get dataset examples (can’t run cos sim and TL tokenizer fn in same nb)
    
    - ISSUE: [how can you have cosine sim greater than 1 using: from sklearn.metrics.pairwise import cosine_similarity](https://chatgpt.com/c/44134f77-f4b0-4dc6-8e37-e11a35b28d1c)
        - can two vectors with mostly 0s cause issues with cosine sim or correlation
            
            Yes, two vectors with mostly zeros can cause issues with both cosine similarity and correlation calculations. Here’s a detailed explanation of how and why:
            
            ### Cosine Similarity
            
            Cosine similarity measures the cosine of the angle between two non-zero vectors. When vectors contain mostly zeros, the following issues can arise:
            
            1. **Zero Vectors**: If one or both of the vectors are zero vectors (i.e., all elements are zero), the cosine similarity is undefined because the denominator (the product of the magnitudes) becomes zero.
            2. **Sparse Vectors**: For sparse vectors (with mostly zero elements), the cosine similarity might still be defined, but the similarity score might be misleading if the non-zero elements are not aligned in a meaningful way. Even small differences in non-zero positions can drastically affect the similarity score.
            
            ### Pearson Correlation
            
            Pearson correlation measures the linear relationship between two vectors. Sparse vectors can also cause issues with this metric:
            
            1. **Variance and Mean**: Pearson correlation depends on the mean and variance of the vectors. If the vectors have mostly zeros, the variance might be very low, and any slight change in the non-zero elements can result in a large change in the correlation coefficient.
            2. **Spurious Correlation**: Sparse data can sometimes show high correlation due to a few non-zero elements coinciding by chance, which might not reflect a true underlying relationship.
            
            ### Example and Demonstration
            
            Here’s a practical demonstration with code:
            
            ```python
            import numpy as np
            from sklearn.metrics.pairwise import cosine_similarity
            from scipy.stats import pearsonr
            
            # Sparse vectors
            vector_a = np.array([0, 0, 0, 0, 0, 1, 0, 0, 0, 0])
            vector_b = np.array([0, 0, 0, 0, 0, 0, 0, 1, 0, 0])
            
            # Cosine similarity
            cos_sim = cosine_similarity(vector_a.reshape(1, -1), vector_b.reshape(1, -1))
            print("Cosine Similarity:", cos_sim[0][0])
            
            # Pearson correlation
            correlation, _ = pearsonr(vector_a, vector_b)
            print("Pearson Correlation:", correlation)
            
            # Another pair of sparse vectors with mostly zero but non-zero in the same positions
            vector_c = np.array([0, 0, 0, 0, 0, 1, 0, 0, 0, 0])
            vector_d = np.array([0, 0, 0, 0, 0, 2, 0, 0, 0, 0])
            
            # Cosine similarity
            cos_sim_cd = cosine_similarity(vector_c.reshape(1, -1), vector_d.reshape(1, -1))
            print("Cosine Similarity (C and D):", cos_sim_cd[0][0])
            
            # Pearson correlation
            correlation_cd, _ = pearsonr(vector_c, vector_d)
            print("Pearson Correlation (C and D):", correlation_cd)
            
            ```
            
            ### Explanation:
            
            1. **Vector A and B**:
                - `vector_a` and `vector_b` have mostly zeros and a single non-zero element in different positions.
                - The cosine similarity is zero, as the vectors are orthogonal.
                - The Pearson correlation might be undefined or very low, indicating no linear relationship.
            2. **Vector C and D**:
                - `vector_c` and `vector_d` have mostly zeros but non-zero elements in the same position.
                - The cosine similarity is 1 because they are perfectly aligned, ignoring magnitude differences.
                - The Pearson correlation is also 1, indicating a perfect linear relationship.
            
            ### Key Points:
            
            - **Cosine Similarity**: Sensitive to the positions of non-zero elements; zero vectors result in undefined similarity.
            - **Pearson Correlation**: Sensitive to the variance and mean; sparse vectors can result in misleading high correlations if non-zero elements align by chance.
            
            ### Recommendations:
            
            1. **Normalization**: Normalize the vectors before computing similarity or correlation.
            2. **Sparsity Handling**: Use techniques specifically designed for sparse data, like the Jaccard similarity for binary vectors.
            3. **Thresholding**: Ignore vectors with very high sparsity when computing similarity or correlation to avoid misleading results.
            
            By understanding these nuances, you can better interpret the similarity and correlation metrics for sparse vectors and ensure more accurate analysis.
            
    - ✅ ISSUE: the interpretations for many features just fire on the EOS token at the start
        - `tokenize_and_concatenate` has `add_bos_token=sae.cfg.prepend_bos,` which is True. True it with False; perhaps tinystories has no padding? try loading with no padding
            - It doesn’t fire on BOS in front, but now actvs for the “highly siimlar” features are 0.
        - ✅ for 100 samples with no BOS prepend, save these actvs and run again but use correlation not cosine sim
            - fActs_ts_1L_21M_noBOS.pkl
            - in python, how do I find a correlation matrix of two matrices (with same row size)?
            
            Still has bad correlations
            
- ✅ NOTE: “most similarly” firing features across models doesn’t mean those features fire high- it could be that most are 0, and only a few fire high, which is why they’re most similar (trivially)! You need to eliminate these trivial pairs. Filter out only “meaningful” features
    - read Towards M, Scaling M, and Not all for how to auto find features
    - Read this. How do they find important features automatically?
- ✅ get samples for a concept both models should represent (eg. pronouns “she” or “her”, fire, etc) and see what features both fire on.
    
    [tinystories_actv_save_v2](https://colab.research.google.com/drive/1yB4-mBBpUIRwVCWCl9QoIPQbbAuTg4NT#scrollTo=GFApm9B6afEP&line=1&uniqifier=1).ipynb
    
    fActs_ts_1L_21M_sheHer.pkl
    
    This finds interpretable features!
    
    [tinystories_actv_corr_mat_v3](https://colab.research.google.com/drive/1F1-fHJJYNywejQg4EzO1_NCTdwoss13K).ipynb
    
    - ✅ given two torch.Size([24960, 16384]) matrices, get a col from one matrix and find the correlation with all other cols of the other matrix. get the cols from matrix B with highest correlation
    - ✅ manually look at top N feature pairs, not just top 5 (which could be trivial)
    - ✅ save the data used to get activations too!
- ✅ feature top_ind_from_B(1786) is “years”, while its analogues in A are “time, summer, morning, day, once” so not EXACT but similar.
    - [The plot is somewhat correlated](https://colab.research.google.com/drive/1F1-fHJJYNywejQg4EzO1_NCTdwoss13K#scrollTo=K1G8Cs1VnoD7&line=5&uniqifier=1)
        - the value is 0.49385567883754433
    - [load_actvs_interpret_features](https://colab.research.google.com/drive/1qUNgjrK8l1JNbSde9PLT6tnm9vgwv-HL#scrollTo=NsN8cKw5mfuj).ipynb: after obtaining correlated features, load tinystories F actvs again and interpret with dataset examples
    - top_ind_from_B(3103)
        
        [14923 16251 13152 13166 10373 16144  7364 15399  9425  5912]
        [0.55415695 0.48495889 0.45813565 0.44274656 0.44002068 0.43836193
        0.43768772 0.43551364 0.43548672 0.43543239]
        
    - ✅ improve plot
        
        ![Untitled](Done%201c002201437341e48b55b8276859a632/Untitled%204.png)
        
    
    Model B’s feature appears to fire on more tokens, possibly because it captures more concepts. That is, while these tokens are 0 in model A (1L-21M)’s feature 16251, model B (2L-33M)’s feature 3301 is nonzero for them.
    
- ✅ fazl meet: [7 12](../Fazl%20meeintg%20fb1fec5aea894f4aa13ec302d8c6a66f/7%2012%2077b28515af034c5f9ff61902f4c8b81a.md)

Feature Manifold Expm Planning

- ✅ [Will meet](../Will%20meet%20c258bd9c464d453a90a6c7110cece677.md)
- ✅ [read actv atlas](../Feature%20manifold%20papers%20722de0b743c34f82b13a975f7c6b143e.md) (more focus on this when analyzing data; for now, focus on setup expms)
- ✅ issues with topoact results- why demo not same as paper/lecture pres?
    
    [https://tdavislab.github.io/TopoAct/single-layer-view.html](https://tdavislab.github.io/TopoAct/single-layer-view.html)
    
    this is polysemantic
    
- ✅ look into topology mapper in python
    - ✅ topoact github is just html code, no algtop algos
    - https://github.com/tdavislab/TopoBERT/blob/master/backend/server/graph_generator.py
    - tell chatgpt to read Towards and Topoact, then: “Given those two papers, how would you design experiments and code to apply mapper to feature activations? Given setup details”
        
        [https://chatgpt.com/c/42f8db48-047d-44d9-8283-95a81e980ba7](https://chatgpt.com/c/42f8db48-047d-44d9-8283-95a81e980ba7)
        
        - how do i adopt mapper to be used on the feature activations of a sparse autoencoder, in which the features are a pytorch tensor of (batch, seqlen, featuredim), obtained by the code: feature_acts = sae.encode(h_store) ? Refer to the attached python code for how to get sae features.
            
            `tinystories_actv_save_v2.ipynb as .py`
            
        - explain all the code from 3. Mapper Construction onwards in detail and intuitively, using analogies when needed for non trivial concepts
            
            ### 3. Mapper Construction
            
            ### Create Cover
            
            We start by dividing the data into overlapping regions (cover sets), which helps us understand local structures and how they connect globally.
            
            ### Code Explanation
            
            ```python
            def create_cover(filtered, intervals, overlap):
                min_val, max_val = np.min(filtered, axis=0), np.max(filtered, axis=0)
                steps = (max_val - min_val) / (intervals - 1) * (1 + overlap)
                cover = []
                for i in range(intervals):
                    for j in range(intervals):
                        cover.append(((min_val[0] + i * steps[0], min_val[0] + (i + 1) * steps[0]),
                                      (min_val[1] + j * steps[1], min_val[1] + (j + 1) * steps[1])))
                return cover
            
            ```
            
            - **Filtered**: The reduced-dimension data (e.g., from PCA).
            - **Intervals**: Number of intervals to divide each dimension into.
            - **Overlap**: Degree of overlap between intervals.
            - **Steps**: Calculated based on the range of data values and overlap.
            
            We create a grid of intervals in the lower-dimensional space and store these as pairs of ranges.
            
            ### Intuition
            
            Imagine spreading a mesh net over a terrain (our data). The intervals define the mesh's squares, and overlap ensures the squares cover the terrain more smoothly.
            
            ### Cluster Within Cover Sets
            
            For each cover set, cluster the data points that fall within it. This helps in identifying local groupings of data.
            
            ### Code Explanation
            
            ```python
            def cluster_cover(cover, filtered, activations):
                clusters = []
                for (x_range, y_range) in cover:
                    indices = np.where((filtered[:, 0] >= x_range[0]) & (filtered[:, 0] < x_range[1]) &
                                       (filtered[:, 1] >= y_range[0]) & (filtered[:, 1] < y_range[1]))[0]
                    if len(indices) > 0:
                        clustering = DBSCAN().fit(activations[indices])
                        clusters.append((indices, clustering.labels_))
                return clusters
            
            ```
            
            - **DBSCAN**: A clustering algorithm that groups points closely packed together, marking outliers.
            - **Indices**: Points falling within the cover set.
            - **Clusters**: Each cover set’s clustered points.
            
            ### Intuition
            
            Think of the mesh net's squares as neighborhoods. We examine each neighborhood to find clusters of houses (data points) that are close together, ignoring outliers.
            
            ### 4. Topological Summary
            
            ### Construct Mapper Graph
            
            We build a graph representing the clusters and their connections.
            
            ### Code Explanation
            
            ```python
            import networkx as nx
            
            def construct_mapper_graph(clusters):
                G = nx.Graph()
                for idx, (indices, labels) in enumerate(clusters):
                    for label in np.unique(labels):
                        if label != -1:
                            cluster_indices = indices[labels == label]
                            G.add_node((idx, label), members=cluster_indices)
                for i, (indices1, labels1) in enumerate(clusters):
                    for j, (indices2, labels2) in enumerate(clusters):
                        if i < j:
                            common_indices = np.intersect1d(indices1, indices2)
                            if len(common_indices) > 0:
                                for label1 in np.unique(labels1):
                                    if label1 != -1:
                                        members1 = indices1[labels1 == label1]
                                        for label2 in np.unique(labels2):
                                            if label2 != -1:
                                                members2 = indices2[labels2 == label2]
                                                if len(np.intersect1d(members1, members2)) > 0:
                                                    G.add_edge((i, label1), (j, label2))
                return G
            
            mapper_graph = construct_mapper_graph(clusters)
            
            ```
            
            - **Nodes**: Represent clusters in each cover set.
            - **Edges**: Connect clusters sharing data points across different cover sets.
            
            ### Intuition
            
            Imagine a social network where each node is a group of friends (clusters), and an edge represents shared friends (common data points) between groups.
            
            ### 5. Visualization
            
            ### Visualizing the Graph
            
            Use a spring layout to visualize the constructed graph.
            
            ### Code Explanation
            
            ```python
            import matplotlib.pyplot as plt
            
            pos = nx.spring_layout(mapper_graph)
            nx.draw(mapper_graph, pos, with_labels=True, node_size=50, node_color="blue")
            plt.show()
            
            ```
            
            - **Spring Layout**: Positions nodes based on simulated physical forces to enhance visualization clarity.
            - **Draw**: Visualizes the graph with nodes and edges.
            
            ### Intuition
            
            Visualize the network as a map of cities (clusters) connected by roads (edges). The spring layout helps position cities so that the map is clear and roads are easy to follow.
            
            ### Conclusion
            
            This process creates a simplified representation of high-dimensional data using the Mapper algorithm, providing insights into the structure and relationships within the data. Each step, from cover creation to graph visualization, helps in understanding complex data in a more intuitive way.
            
    - mapper_fAct_explora.ipynb
        - compare to random data
        - is empty plot always a bug? where did the pts go? do you expect random data to all be noise and thus have empty plot?
            
            When applying the Mapper algorithm to random data, it is not necessarily expected that all data will be classified as noise, resulting in an empty plot. However, it is common because random data lacks structure. Here are some points to consider:
            
            ### Expectation for Random Data
            
            1. **Lack of Structure**:
                - Random data often does not have the dense regions necessary for clustering algorithms like DBSCAN to form clusters.
                - This can result in many points being labeled as noise (`1`).
            2. **Parameter Sensitivity**:
                - The clustering parameters (`eps` and `min_samples` in DBSCAN) might not be suitable for the random data.
                - Random data might require different settings to form clusters, though meaningful clusters may still not be found.
            3. **Real-World Data vs. Random Data**:
                - Real-world data typically has inherent patterns and structures, making it more likely to form meaningful clusters.
                - Random data lacks such patterns, leading to more points being identified as noise.
            
            ### Practical Steps
            
            - **Verify Data Distribution**: Check the distribution of your random data.
                
                ```python
                plt.scatter(filtered_random_data[:, 0], filtered_random_data[:, 1], alpha=0.5)
                plt.title("Filtered Random Data Points")
                plt.xlabel("PCA Component 1")
                plt.ylabel("PCA Component 2")
                plt.show()
                
                ```
                
            - **Adjust Clustering Parameters**:
                
                ```python
                random_clusters = cluster_cover(random_cover, filtered_random_data, reshaped_random_data, eps=0.3, min_samples=3)
                
                ```
                
            - **Check Clusters**:
                
                ```python
                for idx, (indices, labels) in enumerate(random_clusters):
                    print(f"Cluster {idx}: {len(indices)} points, labels: {np.unique(labels)}")
                
                ```
                
            
            ### Example
            
            If you still encounter an empty plot after adjustments, it suggests that the random data does not form clusters under the given parameters. This is typical and highlights the contrast between structured real-world data and random noise, validating the effectiveness of the Mapper algorithm in capturing meaningful structures in real data.
            
            By experimenting with different parameters and visualizing the data, you can better understand the behavior of random data in comparison to real data and the appropriateness of clustering algorithms like DBSCAN.
            
        - i got this for feature activations. are activations usually in a circle? if not what could this mean
            
            Activations typically are not expected to form a perfect circle. If your feature activations form a circular pattern, it could indicate several things:
            
            1. **Dimensionality Reduction Artifact**: If you used PCA or another dimensionality reduction technique, the circular pattern might result from how the algorithm projected the data into a lower-dimensional space.
            2. **Periodic Structure in Data**: The underlying data might have periodicity or cyclical patterns that are being captured in the activations.
            3. **Model Regularity**: The model might have learned a regular, cyclical pattern from the training data, which is reflected in the activations.
            
            ### Steps to Investigate Further
            
            1. **Verify Dimensionality Reduction**:
                - Check the explained variance ratio of the PCA components to ensure that the circle is not an artifact of the reduction process.
                
                ```python
                print(pca.explained_variance_ratio_)
                
                ```
                
            2. **Analyze the Source Data**:
                - Investigate the input data to see if there are any inherent periodic or cyclic patterns.
                
                ```python
                plt.plot(h_store[0].detach().numpy())  # Example for the first sequence
                plt.title("Input Data Sample")
                plt.show()
                
                ```
                
            3. **Check Model Training**:
                - Ensure that the model training process did not introduce regularities that might cause this pattern.
                - Check for overfitting or regularization artifacts.
            4. **Compare with Random Data**:
                - Generate random data and pass it through the model to see if a similar circular pattern appears.
                
                ```python
                random_data = np.random.randn(*h_store.shape)
                random_activations = sae.encode(torch.from_numpy(random_data).float())
                filtered_random_data = pca.transform(random_activations.view(-1, featuredim).detach().numpy())
                plt.scatter(filtered_random_data[:, 0], filtered_random_data[:, 1], alpha=0.5)
                plt.title("Filtered Random Data Points")
                plt.show()
                
                ```
                
            
            ### Conclusion
            
            While a circular pattern in activations is unusual, it's essential to analyze the steps leading to this result and verify if it's due to the model, the data, or the dimensionality reduction technique. By performing these checks, you can better understand the cause and take appropriate steps to address any issues.
            
        - how do i plot the pca before mapper
        - what do the indices on this plot mean?
            
            The indices on this plot likely represent the clusters and their labels as identified by the Mapper algorithm. In the format `(x, y)`, each pair can be interpreted as follows:
            
            1. **Cluster Index (`x`)**: This is the index of the cover set in which the cluster was found. Cover sets are created during the Mapper construction process by dividing the data space into overlapping regions.
            2. **Cluster Label (`y`)**: This is the label assigned by the clustering algorithm (e.g., DBSCAN) within that cover set. Each unique label represents a distinct cluster, and `1` typically indicates noise or outliers.
            
            Given the circular arrangement, this pattern likely results from how the data was reduced and clustered, with each node representing a cluster from a specific cover set and showing how they connect.
            
            In summary, the indices `(x, y)` indicate which cover set (region of the data space) a cluster belongs to (`x`) and the cluster label within that cover set (`y`). This representation helps in understanding the topological relationships between different clusters in the data.
            
        - the feature actvs were of shape torch.Size([195, 128, 16384]). why are they so few pts in mapper plot? also, why isn't the mapper plot a graph with edges?
            
            Given your feature activations are of shape `torch.Size([195, 128, 16384])`, there are a few reasons why you might see only a few points and no edges in the Mapper plot:
            
            ### 1. Dimensionality Reduction Impact
            
            The high dimensionality of the feature activations (16384 dimensions) is drastically reduced to 2 dimensions using PCA. This could result in loss of significant structural information, leading to fewer meaningful clusters.
            
            ### 2. Clustering Parameters
            
            The DBSCAN parameters (`eps` and `min_samples`) might not be optimal for the reduced data, causing many points to be labeled as noise (`-1`). Adjusting these parameters could help.
            
            ### 3. Overlapping Cover Sets
            
            The choice of cover intervals and overlap affects how many points fall into multiple cover sets, influencing the number of clusters formed.
            
            ### 4. Graph Construction
            
            For edges to appear, there must be shared points between clusters across cover sets. If no such shared points exist, no edges will be drawn.
            
            ### Detailed Steps to Address These Issues
            
            ### 1. Verify Dimensionality Reduction
            
            Ensure that the PCA retains enough variance:
            
            ```python
            from sklearn.decomposition import PCA
            
            # Perform PCA and check explained variance ratio
            pca = PCA(n_components=2)
            pca_acts = pca.fit_transform(reshaped_acts)
            print(pca.explained_variance_ratio_)
            
            ```
            
            Ensure enough variance is captured, or consider increasing the number of components and then using t-SNE or UMAP for 2D visualization.
            
            ### 2. Adjust DBSCAN Parameters
            
            Experiment with different `eps` and `min_samples`:
            
            ```python
            from sklearn.cluster import DBSCAN
            
            def cluster_cover(cover, filtered, activations, eps=0.5, min_samples=5):
                clusters = []
                for idx, (x_range, y_range) in enumerate(cover):
                    indices = np.where((filtered[:, 0] >= x_range[0]) & (filtered[:, 0] < x_range[1]) &
                                       (filtered[:, 1] >= y_range[0]) & (filtered[:, 1] < y_range[1]))[0]
                    if len(indices) > 0:
                        clustering = DBSCAN(eps=eps, min_samples=min_samples).fit(activations[indices])
                        clusters.append((idx, clustering.labels_))
                return clusters
            
            # Adjust eps and min_samples
            random_clusters = cluster_cover(random_cover, filtered_acts, reshaped_acts, eps=0.3, min_samples=3)
            
            ```
            
            ### 3. Visualize PCA Before Applying Mapper
            
            ```python
            import matplotlib.pyplot as plt
            
            plt.scatter(pca_acts[:, 0], pca_acts[:, 1], alpha=0.5)
            plt.title("PCA of Feature Activations")
            plt.xlabel("Principal Component 1")
            plt.ylabel("Principal Component 2")
            plt.show()
            
            ```
            
            ### 4. Verify Mapper Graph Construction
            
            Check if nodes and edges are being added correctly:
            
            ```python
            import networkx as nx
            
            def construct_mapper_graph(clusters):
                G = nx.Graph()
                for idx, (indices, labels) in enumerate(clusters):
                    for label in np.unique(labels):
                        if label != -1:
                            cluster_indices = indices[labels == label]
                            G.add_node((idx, label), members=cluster_indices)
                for i, (indices1, labels1) in enumerate(clusters):
                    for j, (indices2, labels2) in enumerate(clusters):
                        if i < j:
                            common_indices = np.intersect1d(indices1, indices2)
                            if len(common_indices) > 0:
                                for label1 in np.unique(labels1):
                                    if label1 != -1:
                                        members1 = indices1[labels1 == label1]
                                        for label2 in np.unique(labels2):
                                            if label2 != -1:
                                                members2 = indices2[labels2 == label2]
                                                if len(np.intersect1d(members1, members2)) > 0:
                                                    G.add_edge((i, label1), (j, label2))
                return G
            
            random_mapper_graph = construct_mapper_graph(random_clusters)
            print(nx.info(random_mapper_graph))
            
            # Visualize the Mapper graph
            pos = nx.spring_layout(random_mapper_graph)
            nx.draw(random_mapper_graph, pos, with_labels=True, node_size=50, node_color="blue")
            plt.title("Mapper Graph")
            plt.show()
            
            ```
            
            ### Conclusion
            
            The fewer points and lack of edges indicate that most points are considered noise or not shared between clusters. Adjusting parameters and ensuring proper data preprocessing can help in obtaining a more meaningful Mapper graph.
            

Feature Splitting Expms

- ⚠️ [Arabic script feature splitting](../Arabic%20script%20feature%20splitting%20776f6c550d954080824fcc18a0fcac16.md)
    - [https://www.neuronpedia.org/gpt2-small/?sourceSet=res_fs768-jb&selectedLayers=[]&sortIndexes=[]&ignoreBos=true&q=arabic](https://www.neuronpedia.org/gpt2-small/?sourceSet=res_fs768-jb&selectedLayers=%5B%5D&sortIndexes=%5B%5D&ignoreBos=true&q=arabic%0A)
        
        The pull down menu has the SAE for each feature split
        
        - How to find arabic script? Just type in the search terms used in Towards?
    - ask neuronpeia slack
    [](https://www.neuronpedia.org/gpt2-small/?sourceSet=res_fs768-jb&selectedLayers=%5B%5D&sortIndexes=%5B%5D&ignoreBos=true&q=arabic%0A)
        
        Hi, I was looking for recs on how to use Neuronpedia to search for languages such as Arabic, and have a few questions:
        
        1) Should I just try a variety of examples such as ال or phrases such as **كيف حالك ?**
        
        2) Is there a way to search by explanation like “Arabic”, not just by dataset examples?
        
        3) The “towards mono” paper mentions characters like ث are tokenized into `\xd8` `\xab`. Would it make more sense to search for the script characters or their utf-8 encodings? (guessing the former since I see japanese characters in the dataset examples)
        
        4) I’ve been trying to find Arabic script features in GPT-2 small L8 SAEs (and its feature splitting variants). Would the model unlikely have Arabic (due to its training dataset); if so, has anyone found Arabic features in publically available models, or believe there could be? Haven’t found this in Gemma-2 either.training 
        
        Lastly, are there separate channels/chats for asking questions about the neuronpedia interface VS asking specific research questions that use neuronpedia?
        

Following are in: [TS Feature Split Expms](../TS%20Feature%20Split%20Expms%2047b1224c6561451ca1ddd9fd26293517.md) 

- ✅**EXPM:** train sae feature split on tinystories
    - ✅ figure out fs factors
        - In Towards, 4096/512 = 8, 16384/4096 = 4, so not constant factor
        - in [saetable](https://jbloomaus.github.io/SAELens/sae_table/#gpt2-small-res-jb-feature-splitting), they just keep doubling
    - train_ts_sae_1L-21M uses 1024 * 16, so just use 1024 * 32, 1024 * 8, etc. These are extremes so need for finer unless find feature splitting with those; if not, refine params before fs
        - ✅ train_ts_sae_1L-21M_df-8192.ipynb
        - ✅ train_ts_sae_1L-21M_df-16384.ipynb
        - ✅ train_ts_sae_2L-33M_MLP0_df-8192.ipynb
        - train_ts_sae_2L-33M_MLP0_df-16384.ipynb
- 🐣 [SAE training skills to learn](../SAE%206b08b4ad57a342bf9393d2ef0fa31c6b.md)
- 🐣 **EXPM:** save actvs for two fs models: df-8192
    - [ts_actv_save_MLP0_df-8192.ipynb](https://colab.research.google.com/drive/1v9ohVNqrCpMgVpIN-NCsMozQ2YAqhYV9)

Feature Relation Mapping Expms

- ✅ **EXPM:** map feature relns in 1L to 2L (dfeat = **16384**) - UMAP
    
    [ts_actv_save_1L_2L_featRelns.ipynb](https://colab.research.google.com/drive/1yxw5HJn2h9v4OpAkSdpHvKeAvR3CIpHE)
    
    - ✅ loop through entire dataset is too long; just choose a very max batch size
        - we want each word to not be overrepresented but there’s a disproportionate amount
            
            ![Untitled](Done%201c002201437341e48b55b8276859a632/Untitled%205.png)
            
        - instead of saying just one word means accept sample, loop through each sample and find samples until the max num for that word is reached
            - it’s okay if king appears in these other words’ samples, as long as there’s enough of the other words. no need to same num
        - save as: fActs_ts_1L_21M_featrelns_v1.pkl
    - ⚠️ get sentences just about: king-queen-princess ***and*** father-mother-daughter
        
        ![Untitled](Done%201c002201437341e48b55b8276859a632/Untitled%206.png)
        
        Not really feature specific to daughter. Perhaps we can use feature splitting to constrain it to specifically fire for daughter?
        
        - issue: top actv features fire on unrelated words like ‘and’, and are often repetitive
    - ✅ instead of find ‘top actv features’ (meaningless), use a search fn that finds features which activate for specific dataset tokens.
        - ⚠️ One way is: don’t use entire batch tokens, but only snippets that have ‘princess’ in it
            
            This is bc too many words
            
            - ISSUE: to create this dataset, you’d be loop through windows of each sample. that takes a long time; the second method below is easier to code
        - ✅ One way is: get top 5 snippets for ALL features, then search to display only features that have the search keywords in their top 5 snippets
            - ✅ search function for features actv on keyword
                - ✅ for each feature, store their top 5 snippets in a list.
                    
                    we can also only store ‘keyword relevant’ snips, but this is inefficient if we want to search through ANY keyword
                    
                - ✅ brute search thru every feature and every list to see if keyword appears
                    - ✅ it’s not just enough for the keyword to appear; it has to be highlighted
            - ⚠️ ask chatgpt to improve this with better algo
            - ⚠️ [https://docs.neuronpedia.org/search](https://docs.neuronpedia.org/search)
    - ⚠️ ISSUE: there’s not a monosemantic princess feature. rather, it’s mixed with a bunch of other related concepts
        
        We should probably look for he/male to king, and she/female to queen, etc. that are MORE separated
        
        There’s princess features that are more related to fairy tales, and other more related to pronouns, and others related to family
        
        we can’t get a clean princess feature, BUT we can still compare subspaces of fairy tales, and say they’re more CCA similar to each other than other subspaces
        
    - ✅ to find how separated semantic clusters are, we should plot a umap then label the features using GPT-4 data analysis (direct input of rows). then we can find similar clusters across models to get subspaces to compare.
        
        [ts_1L_2L_UMAP](https://colab.research.google.com/drive/1Cl7nohl7hyaKz17bHbrkDgkADf-0DPqZ#scrollTo=kUYRF57KNxrL).ipynb
        
        - ✅ plot umap of decoder weights first as closer to anthropic
            
            [https://transformer-circuits.pub/2023/monosemantic-features#appendix-umap](https://transformer-circuits.pub/2023/monosemantic-features#appendix-umap)
            
            - ✅ save decoder weights in [ts_actv_save_1L_2L_featRelns](https://colab.research.google.com/drive/1yxw5HJn2h9v4OpAkSdpHvKeAvR3CIpHE#scrollTo=PXCAAVFcup6L&line=1&uniqifier=1).ipynb
            - ✅ whats the diff between these two code, do they both use 2 components? are the components the axis displayed?
                
                [https://chatgpt.com/c/046b8a82-8582-4083-8519-fa159a6e4bb0](https://chatgpt.com/c/046b8a82-8582-4083-8519-fa159a6e4bb0)
                
                In both snippets, UMAP reduces the data to 2 components.
                
            - ✅ decoder weight matrix umap has much more structure than the encoder W
            - ✅ the decoder matrix has dims (features_sae, features_LLM). Does the umap have a point for each feature_sae row?
                
                Yes, in the context of UMAP applied to the decoder matrix with dimensions (features_sae, features_LLM), each row corresponds to a feature from the sparse autoencoder (SAE). Therefore, the UMAP would generate a point for each row (feature_sae), representing how each SAE feature is embedded in the reduced 2-dimensional space.
                
                Given that the decoder matrix maps SAE features to LLM features, the UMAP visualization shows the relationship and distribution of these SAE features in a lower-dimensional space, highlighting patterns and clusters among the features learned by the autoencoders.
                
        - ⚠️ try cca
            - -0.99
                
                Canonical correlation measures the relationship between two sets of variables. The value ranges from -1 to 1, where:
                
                - A value of 1 indicates a perfect positive correlation.
                - A value of -1 indicates a perfect negative correlation.
                - A value of 0 indicates no correlation.
                
                Given the canonical correlation value of -0.9918, this indicates a very strong negative correlation between the two sets of variables. This means that as values in one set increase, values in the other set decrease almost perfectly in a linear fashion.
                
                Therefore, this is not a "low" correlation; it is actually very high in magnitude, just negative. This indicates a very strong linear relationship between the two sets of variables, but in opposite directions.
                
            - what does that mean for the umap of two decoder weights of a sparse autoencoder? read what saes are here before answering: [https://transformer-circuits.pub/2023/monosemantic-features#](https://transformer-circuits.pub/2023/monosemantic-features#)
                
                A sparse autoencoder (SAE) aims to extract interpretable features from a neural network by decomposing the activation space into more components than neurons, helping understand the model's behavior. When using UMAP to visualize two decoder weight matrices from such an SAE, a strong negative canonical correlation (like -0.9918) suggests the two weight matrices are almost perfect opposites. This implies that the features learned by the autoencoder are highly distinct in their contributions to the network, emphasizing the SAE's ability to separate features effectively.
                
                For more detailed context, visit [Transformer Circuits](https://transformer-circuits.pub/2023/monosemantic-features).
                
            - does that mean the features are not similar across the two models? these are decoder weights on two saes from two separate models trained on the same dataset
                
                A canonical correlation of -0.9918 between the UMAP embeddings of decoder weights from two sparse autoencoders trained on the same dataset indicates that the features are highly dissimilar across the two models. This strong negative correlation means that when one model assigns a high value to a feature, the other model assigns a correspondingly low value, suggesting that the features learned by each model capture different aspects or perspectives of the same data.
                
                For more information on sparse autoencoders and their applications, refer to the [Transformer Circuits](https://transformer-circuits.pub/2023/monosemantic-features) article.
                
        - ✅ given a list of size features_sae with strings, create an interactive umap plot such that hovering over a point will display the feature id and string (from the list) in a box above the plot, and another code such that hovering over a point will display the same thing in a box next to the cursor
        - ✅ output stored dataset examples into a file, then input to gpt-4 for labeling
            
            [ts_actv_save_1L_2L_featRelns](https://colab.research.google.com/drive/1yxw5HJn2h9v4OpAkSdpHvKeAvR3CIpHE#scrollTo=PXCAAVFcup6L&line=1&uniqifier=1).ipynb: [https://colab.research.google.com/drive/1yxw5HJn2h9v4OpAkSdpHvKeAvR3CIpHE#scrollTo=n1_YKW1I10YZ&line=1&uniqifier=1](https://colab.research.google.com/drive/1yxw5HJn2h9v4OpAkSdpHvKeAvR3CIpHE#scrollTo=n1_YKW1I10YZ&line=1&uniqifier=1)
            
            - ✅ use 500 any samples (not specific keywords), max len 128
                - 1000 x 512 gets OOM on A100
            - ✅ in python, given a dict of "feature int : list of 5 strings", what's the best format to save it in as an output to give to gpt-4 to give a short description that summarizes the 5 strings? there are 16300 features. give code
                
                [https://chatgpt.com/c/b273493b-8db6-4ce0-9c91-c1dba50bb1b6](https://chatgpt.com/c/b273493b-8db6-4ce0-9c91-c1dba50bb1b6)
                
            - ⚠️ This is a json file containing dictionaries of “feature id” and “strings”. For each feature id, give a short description (less than a sentence; the shorter the better) that summarizes the 5 strings in the list in “strings”. Focus especially on the token within “[bold u dark_orange]{new_str_token}[/]”. Output the “feature_id” with your short description summary of it in a format you find best for loading into python, such as json. Don't display what you output, save it all to a json file and just give me the file
                
                
                - the entire 16000 features file is too big, so try splitting into segments of ~5000
            - ✅ if gpt4 can’t handle labeling that many, just show dataset examples for now
                - just get highlighted token for top 5 samples
        - ✅ label features on umap
            - ✅ to create two side by side plots such that hovering over any pt in a plot will bring up the hovered label
        - ✅ do this across models to look for similarities
    - it appears that while the actual arrangement of points in UMAP are different each run due to randomness, the relative clusterings and topologically distances apart remain the same
- 🐣 **EXPM:** for correlated features, side by side umaps such that hovering over one feature will locate the highest corr feature in the other plot and both of their labels
    - ✅ first try cosine on weights (this probably doesn’t make any sense)
        
        Histogram: We see weights have VERY low correlations, so try activations now
        
    - ✅ now get actvs on anySamps for both models
        
        ts_actv_save_1L_2L_anySamps.ipynb
        
        - fActs_ts_1L_21M_anySamps_v1.pkl
    - ✅ [get actv correlations](https://colab.research.google.com/drive/1Cl7nohl7hyaKz17bHbrkDgkADf-0DPqZ#scrollTo=fRJdgEFbD_c7&line=1&uniqifier=1)
        - ✅ [is there any way to speed this up for 64000 x 16384 matrices:](https://chatgpt.com/c/b9d1b869-2d27-48b8-ab1f-b3db82f750f0)
            
            To speed up your function for handling 64000 x 16384 matrices, you can utilize the power of PyTorch for vectorized operations and GPU acceleration. This way, you can avoid looping over the columns and instead perform the operations in parallel. Here's a refactored version of your function:
            
            ```python
            import torch
            import numpy as np
            
            def top_ind_from_B(ind, reshaped_activations_A, reshaped_activations_B):
                # Select a column from matrix B (e.g., the first column)
                column_A = reshaped_activations_B[:, ind]
            
                # Ensure tensors are on GPU
                if torch.cuda.is_available():
                    reshaped_activations_A = reshaped_activations_A.to('cuda')
                    reshaped_activations_B = reshaped_activations_B.to('cuda')
                    column_A = column_A.to('cuda')
            
                # Calculate means and standard deviations
                mean_A = column_A.mean()
                std_A = column_A.std()
            
                # Mask columns with zero standard deviation
                std_B = reshaped_activations_A.std(dim=0)
                valid_columns_mask = std_B != 0
            
                # Compute correlations for valid columns
                valid_reshaped_activations_A = reshaped_activations_A[:, valid_columns_mask]
                mean_B = valid_reshaped_activations_A.mean(dim=0)
                std_B = valid_reshaped_activations_A.std(dim=0)
            
                covariance = ((valid_reshaped_activations_A - mean_B) * (column_A - mean_A).unsqueeze(1)).mean(dim=0)
                correlations = covariance / (std_A * std_B)
            
                # Fill correlations with -inf where columns were invalid
                all_correlations = torch.full((reshaped_activations_A.shape[1],), float('-inf')).to(correlations.device)
                all_correlations[valid_columns_mask] = correlations
            
                # Get the indices of the top 10 columns in B with the highest correlations
                top_10_indices = torch.topk(all_correlations, 10).indices.cpu().numpy()
                top_10_correlations = all_correlations[top_10_indices].cpu().numpy()
            
                return top_10_indices, top_10_correlations
            
            # Example usage
            reshaped_activations_A = torch.randn(64000, 16384)
            reshaped_activations_B = torch.randn(64000, 16384)
            
            top_10_indices, top_10_correlations = top_ind_from_B(0, reshaped_activations_A, reshaped_activations_B)
            print(f'Top 10 indices: {top_10_indices}')
            print(f'Top 10 correlations: {top_10_correlations}')
            
            ```
            
            ### Key Optimizations:
            
            1. **Vectorization**: We avoid explicit Python loops by using PyTorch's broadcasting and vectorized operations.
            2. **GPU Acceleration**: The function checks for the availability of a CUDA-compatible GPU and transfers tensors to the GPU for computation.
            3. **Masking Invalid Columns**: We handle zero standard deviation columns by creating a mask and filling invalid correlations with `inf`.
            
            This approach should significantly speed up your computation by leveraging PyTorch's efficient tensor operations and, if available, GPU acceleration.
            
        - ✅ use this sped up code to find the highest correlated feature from A to B for every of the 16384 features
            - ✅ this is still slow. can you speed it up say with matrix multp for all features at once?
            - ✅ ISSUE: same indices, and values are nan
        - ✅ save dataset to drive, then load in umap nb to do ds interpret after corr pairs
            - ISSUE: needs model.tokenizer to convert token to str
                
                `AttributeError: module 'pyarrow.lib' has no attribute 'ListViewType’`
                
                Importing Transformelens is incompatible with umap lib!
                
            - ✅ TRY: load hf’s tokenizer and use decode
                
                [https://chatgpt.com/c/c334dba9-cf63-4e76-8f4c-1475c1284a44](https://chatgpt.com/c/c334dba9-cf63-4e76-8f4c-1475c1284a44)
                
    - 🐣 given a dictionary that maps every point number from the first plot to a point number in the second plot, make a side by side interative plot like above but where hovering over a point in one plot will also bring up the hovered label in the second plot. also, when a point is hovered over, it turns yellow and its point partner also turns yellow
        - [https://chatgpt.com/c/a6434589-5715-49ff-9c2f-dfa11065ef73](https://chatgpt.com/c/a6434589-5715-49ff-9c2f-dfa11065ef73)
            - that doesn't work. I mean this: here's a dictionary mapping the two features_list and features_list_2: feat_map = {3:40, 60:5, ...} as an example only. take this as input. now, when you hover over element 3 in the left plot, then that not only brings up a hovered label for element 3 in the left, but brings up a hovered label for element 40 on the right. and so forth. ALSO you didn't make the points yellow when they're hovered over!
        - [https://claude.ai/chat/32d6c56e-9a46-4505-8ae1-3b358129b832](https://claude.ai/chat/32d6c56e-9a46-4505-8ae1-3b358129b832)
            - it has to work in colab. if not possible to do in colab, what are the steps to do this somewhere else for free
                
                I apologize for the confusion. You're right to point out that some of the more advanced interactive features might not work directly in Colab due to limitations in how it handles JavaScript callbacks. Let's explore a few options:
                
                1. Simplified Colab Version:
                We can create a simpler version that works in Colab but with limited interactivity. This won't have the cross-plot highlighting, but it will still show hover information.
                2. Using Plotly Dash (can be done for free):
                This is a more robust solution that allows for full interactivity, but it requires setting up a small web application.
                
                Let's start with the simplified Colab version, and then I'll explain how to set up the fully interactive version using Plotly Dash.
                
                Simplified Colab Version:
                
                ```python
                import umap
                import pandas as pd
                import plotly.graph_objects as go
                from plotly.subplots import make_subplots
                import numpy as np
                
                # Assume weight_matrix_np, weight_matrix_2, fList_model_A, and fList_model_B are already defined
                
                # Initialize UMAP
                reducer = umap.UMAP(n_neighbors=15, min_dist=0.01, metric='euclidean')
                
                # Fit and transform the data by rows
                embedding1 = reducer.fit_transform(weight_matrix_np)
                embedding2 = reducer.fit_transform(weight_matrix_2)
                
                # Create DataFrames for Plotly
                df1 = pd.DataFrame(embedding1, columns=['UMAP Component 1', 'UMAP Component 2'])
                df1['Feature ID'] = range(len(embedding1))
                df1['Feature Description'] = fList_model_A[:len(embedding1)]
                
                df2 = pd.DataFrame(embedding2, columns=['UMAP Component 1', 'UMAP Component 2'])
                df2['Feature ID'] = range(len(embedding2))
                df2['Feature Description'] = fList_model_B[:len(embedding2)]
                
                # Create side by side plots using Plotly subplots
                fig = make_subplots(rows=1, cols=2, subplot_titles=('UMAP Projection of Dataset 1', 'UMAP Projection of Dataset 2'))
                
                # Add first scatter plot
                fig.add_trace(
                    go.Scatter(
                        x=df1['UMAP Component 1'], y=df1['UMAP Component 2'],
                        mode='markers', marker=dict(color='blue', size=8),
                        text=df1['Feature ID'], customdata=np.array(df1[['Feature Description']]),
                        hovertemplate='<b>Feature ID:</b> %{text}<br><b>Description:</b> %{customdata[0]}'
                    ),
                    row=1, col=1
                )
                
                # Add second scatter plot
                fig.add_trace(
                    go.Scatter(
                        x=df2['UMAP Component 1'], y=df2['UMAP Component 2'],
                        mode='markers', marker=dict(color='green', size=8),
                        text=df2['Feature ID'], customdata=np.array(df2[['Feature Description']]),
                        hovertemplate='<b>Feature ID:</b> %{text}<br><b>Description:</b> %{customdata[0]}'
                    ),
                    row=1, col=2
                )
                
                # Update layout
                fig.update_layout(
                    title_text='UMAP Projections of Datasets',
                    showlegend=False,
                    hovermode='closest'
                )
                
                fig.update_xaxes(title_text='UMAP Component 1', row=1, col=1)
                fig.update_xaxes(title_text='UMAP Component 1', row=1, col=2)
                fig.update_yaxes(title_text='UMAP Component 2', row=1, col=1)
                fig.update_yaxes(title_text='UMAP Component 2', row=1, col=2)
                
                fig.show()
                
                ```
                
                This version will work in Colab and provide basic interactivity (hovering to see point information), but it won't have the cross-plot highlighting feature.
                
                For the fully interactive version with cross-plot highlighting, you'll need to use Plotly Dash. Here are the steps to set this up for free:
                
                1. Set up a free Heroku account ([https://www.heroku.com/](https://www.heroku.com/)).
                2. Install the Heroku CLI on your local machine.
                3. Create a new Python file (e.g., `app.py`) with the Dash application code.
                4. Create a `requirements.txt` file listing the required Python packages.
                5. Create a `Procfile` for Heroku deployment.
                6. Initialize a Git repository, commit your files, and push to Heroku.
                
                Here's a basic structure for the `app.py` file:
                
                ```python
                import dash
                from dash import dcc, html
                from dash.dependencies import Input, Output
                import plotly.graph_objects as go
                from plotly.subplots import make_subplots
                import pandas as pd
                import numpy as np
                import umap
                
                # Initialize your data and UMAP embeddings here
                # (You'll need to load your data or compute it on the fly)
                
                app = dash.Dash(__name__)
                server = app.server  # Needed for Heroku deployment
                
                app.layout = html.Div([
                    dcc.Graph(id='umap-plots')
                ])
                
                @app.callback(
                    Output('umap-plots', 'figure'),
                    Input('umap-plots', 'hoverData')
                )
                def update_graph(hoverData):
                    # Create your figure here, similar to the Colab version
                    # Use hoverData to implement the cross-plot highlighting
                
                    return fig
                
                if __name__ == '__main__':
                    app.run_server(debug=True)
                
                ```
                
                This is a basic structure and would need to be filled out with your specific data and plot creation code.
                
                The main advantage of using Dash is that it allows for more complex interactivity and updating of the plots based on user input, which is necessary for the cross-plot highlighting feature you requested.
                
                Would you like me to provide more details on any part of this process?
                
            - can it work in colab? why wouldn't it?
                
                I apologize for any confusion in my previous responses. You're right to question this, and I appreciate the opportunity to clarify.
                
                Upon further consideration, it is indeed possible to create an interactive plot with cross-plot highlighting in Google Colab. My initial hesitation was unwarranted, as Colab does support Plotly's JavaScript callbacks when properly implemented.
                
                Here's a version that should work in Colab with the cross-plot highlighting feature:
                
                ```python
                import umap
                import pandas as pd
                import plotly.graph_objects as go
                from plotly.subplots import make_subplots
                import numpy as np
                from IPython.display import display, HTML
                
                # Assume weight_matrix_np, weight_matrix_2, fList_model_A, and fList_model_B are already defined
                
                # Initialize UMAP
                reducer = umap.UMAP(n_neighbors=15, min_dist=0.01, metric='euclidean')
                
                # Fit and transform the data by rows
                embedding1 = reducer.fit_transform(weight_matrix_np)
                embedding2 = reducer.fit_transform(weight_matrix_2)
                
                # Create DataFrames for Plotly
                df1 = pd.DataFrame(embedding1, columns=['UMAP Component 1', 'UMAP Component 2'])
                df1['Feature ID'] = range(len(embedding1))
                df1['Feature Description'] = fList_model_A[:len(embedding1)]
                
                df2 = pd.DataFrame(embedding2, columns=['UMAP Component 1', 'UMAP Component 2'])
                df2['Feature ID'] = range(len(embedding2))
                df2['Feature Description'] = fList_model_B[:len(embedding2)]
                
                # Create side by side plots using Plotly subplots
                fig = make_subplots(rows=1, cols=2, subplot_titles=('UMAP Projection of Dataset 1', 'UMAP Projection of Dataset 2'))
                
                # Add first scatter plot
                trace1 = go.Scatter(
                    x=df1['UMAP Component 1'], y=df1['UMAP Component 1'],
                    mode='markers', marker=dict(color='blue', size=8),
                    text=df1['Feature ID'], customdata=np.array(df1[['Feature Description']]),
                    hovertemplate='<b>Feature ID:</b> %{text}<br><b>Description:</b> %{customdata[0]}',
                    name='Dataset 1'
                )
                fig.add_trace(trace1, row=1, col=1)
                
                # Add second scatter plot
                trace2 = go.Scatter(
                    x=df2['UMAP Component 1'], y=df2['UMAP Component 1'],
                    mode='markers', marker=dict(color='green', size=8),
                    text=df2['Feature ID'], customdata=np.array(df2[['Feature Description']]),
                    hovertemplate='<b>Feature ID:</b> %{text}<br><b>Description:</b> %{customdata[0]}',
                    name='Dataset 2'
                )
                fig.add_trace(trace2, row=1, col=2)
                
                # Update layout
                fig.update_layout(
                    title_text='UMAP Projections of Datasets',
                    showlegend=False,
                    hovermode='closest'
                )
                
                fig.update_xaxes(title_text='UMAP Component 1', row=1, col=1)
                fig.update_xaxes(title_text='UMAP Component 1', row=1, col=2)
                fig.update_yaxes(title_text='UMAP Component 2', row=1, col=1)
                fig.update_yaxes(title_text='UMAP Component 2', row=1, col=2)
                
                # Create a dictionary to map points from plot 1 to plot 2 (replace this with your actual mapping)
                point_mapping = {i: i for i in range(len(embedding1))}  # Example: one-to-one mapping
                
                # Add JavaScript code for interactivity
                js_code = """
                <script>
                var originalColors = {
                    'Dataset 1': 'blue',
                    'Dataset 2': 'green'
                };
                
                function resetColors(gd, trace) {
                    var update = {
                        'marker.color': [originalColors[trace.name]]
                    };
                    Plotly.restyle(gd, update, [trace.index]);
                }
                
                function highlightPoint(gd, trace, ptNumber) {
                    var update = {
                        'marker.color': trace.marker.color.map((_, i) => i === ptNumber ? 'yellow' : originalColors[trace.name])
                    };
                    Plotly.restyle(gd, update, [trace.index]);
                }
                
                var point_mapping = %s;
                
                gd = document.getElementById('%s')
                gd.on('plotly_hover', function(data) {
                    var trace = data.points[0].data;
                    var ptNumber = data.points[0].pointNumber;
                
                    highlightPoint(gd, trace, ptNumber);
                
                    if (trace.name === 'Dataset 1' && point_mapping.hasOwnProperty(ptNumber)) {
                        var otherTrace = gd.data[1];
                        highlightPoint(gd, otherTrace, point_mapping[ptNumber]);
                    } else if (trace.name === 'Dataset 2') {
                        var otherTrace = gd.data[0];
                        var matchingPoint = Object.keys(point_mapping).find(key => point_mapping[key] === ptNumber);
                        if (matchingPoint !== undefined) {
                            highlightPoint(gd, otherTrace, parseInt(matchingPoint));
                        }
                    }
                });
                
                gd.on('plotly_unhover', function(data) {
                    resetColors(gd, gd.data[0]);
                    resetColors(gd, gd.data[1]);
                });
                </script>
                """
                
                # Generate a unique ID for the graph div
                import random
                import string
                graph_id = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
                
                # Update the layout to include the graph ID
                fig.update_layout(
                    autosize=False,
                    width=1000,
                    height=500,
                )
                
                # Show the plot
                fig.show()
                
                # Display the JavaScript code
                display(HTML(js_code % (point_mapping, graph_id)))
                
                ```
                
                This code should work in Colab and provide the cross-plot highlighting feature you requested. Here's why it works:
                
                1. We create the Plotly figure as before.
                2. We generate a unique ID for the graph div to ensure we can target it with our JavaScript.
                3. We create a JavaScript code block that includes the functions for highlighting and resetting colors, as well as the event listeners for hover and unhover events.
                4. We use the `display(HTML())` function to inject this JavaScript code into the notebook after the plot is displayed.
                
                The reason this approach works in Colab is that we're not relying on Plotly's built-in JavaScript callback system (which can be more limited in notebook environments). Instead, we're manually injecting our JavaScript code into the notebook, which allows us to add custom interactivity.
                
                I apologize again for my earlier confusion. This solution should provide the interactive features you're looking for while working within the Colab environment. Let me know if you need any clarification or have any questions about this implementation!
                
        - [try giving these instructions from scratch without preexisting code](https://chatgpt.com/c/cf944c0e-1b61-4282-8964-479c87456b40)
            
            
        - [try gpt4 instead of 4o](https://chatgpt.com/c/2fd82b53-8ea9-4f77-9f35-ca84047b9d61)
        - [https://stackoverflow.com/questions/70944316/plotly-highlight-data-point-and-nearest-three-points-on-hover](https://stackoverflow.com/questions/70944316/plotly-highlight-data-point-and-nearest-three-points-on-hover)
        - [what's an easy alternative way to do this if i'm not confined to running in colab, and what clear steps to do this?](https://chatgpt.com/c/2fd82b53-8ea9-4f77-9f35-ca84047b9d61)  (ctlr+f this phrase in chat)
            
            For a scenario where you're not confined to running in Colab and can use a broader range of tools, creating an interactive web application using JavaScript directly alongside Python could be an excellent way to handle interactive, linked UMAP visualizations. Using a combination of a Python backend (Flask or FastAPI) to serve the data and a frontend using libraries like Plotly.js or D3.js can give you much more control and flexibility over the interactive elements.
            
            ### Step-by-Step Guide to Setting Up an Interactive Visualization with Flask and Plotly.js:
            
            ### Step 1: Setup Your Environment
            
            Ensure Python is installed and set up a new virtual environment:
            
            ```bash
            python -m venv venv
            source venv/bin/activate  # On Windows use `venv\\Scripts\\activate`
            pip install flask umap-learn numpy sklearn
            
            ```
            
            ### Step 2: Prepare Your Python Script (Backend)
            
            Create a Flask app to serve UMAP data and the HTML for the frontend:
            
            1. **Flask App Setup**:
            
            ```python
            from flask import Flask, jsonify, render_template
            import umap
            from sklearn.datasets import make_blobs
            
            app = Flask(__name__)
            
            # Generate sample data
            data1, _ = make_blobs(n_samples=100, centers=3, n_features=5, random_state=42)
            data2, _ = make_blobs(n_samples=100, centers=3, n_features=5, random_state=84)
            
            # Perform UMAP
            reducer1 = umap.UMAP()
            embedding1 = reducer1.fit_transform(data1)
            reducer2 = umap.UMAP()
            embedding2 = reducer2.fit_transform(data2)
            
            # Map indices
            feat_map = {i: (99-i) for i in range(100)}
            
            @app.route('/')
            def index():
                return render_template('index.html')
            
            @app.route('/data')
            def data():
                return jsonify({
                    'embedding1': embedding1.tolist(),
                    'embedding2': embedding2.tolist(),
                    'map': feat_map
                })
            
            if __name__ == '__main__':
                app.run(debug=True)
            
            ```
            
            1. **HTML and JavaScript (Frontend)**:
            Create a file `templates/index.html` in the same directory as your Flask app:
            
            ```html
            <!DOCTYPE html>
            <html>
            <head>
                <title>UMAP Visualizations</title>
                <script src="<https://cdn.plot.ly/plotly-latest.min.js>"></script>
            </head>
            <body>
                <div id="plot1" style="width:600px; height:500px;"></div>
                <div id="plot2" style="width:600px; height:500px;"></div>
            
                <script>
                    fetch('/data')
                        .then(response => response.json())
                        .then(data => {
                            const trace1 = {
                                x: data.embedding1.map(d => d[0]),
                                y: data.embedding1.map(d => d[1]),
                                mode: 'markers',
                                type: 'scatter',
                                text: Object.keys(data.map),
                                hoverinfo: 'text'
                            };
            
                            const trace2 = {
                                x: data.embedding2.map(d => d[0]),
                                y: data.embedding2.map(d => d[1]),
                                mode: 'markers',
                                type: 'scatter',
                                text: Object.values(data.map),
                                hoverinfo: 'text'
                            };
            
                            const layout = { hovermode: 'closest' };
            
                            Plotly.newPlot('plot1', [trace1], layout);
                            Plotly.newPlot('plot2', [trace2], layout);
            
                            const plots = [document.getElementById('plot1'), document.getElementById('plot2')];
            
                            plots.forEach((plot, index) => {
                                plot.on('plotly_hover', function(data) {
                                    let ptNumber = data.points[0].pointNumber;
                                    let mapIndex = index === 0 ? data.map[ptNumber] : Object.keys(data.map).find(key => data.map[key] === ptNumber);
                                    Plotly.Fx.hover(index === 0 ? 'plot2' : 'plot1', [{curveNumber: 0, pointNumber: mapIndex}], 'xy');
                                });
                            });
                        });
                </script>
            </body>
            </html>
            
            ```
            
            ### Step 3: Run Your Application
            
            Run the Flask app by executing `python <filename>.py`. Visit `localhost:5000` in your web browser to view the interactive UMAP plots.
            
            ### Summary:
            
            This setup allows for a high degree of interactivity by directly manipulating data on the client side with JavaScript. You can hover over points in one plot to highlight corresponding points in another plot, using Plotly.js for visualization and Flask for serving the data and the webpage. This method leverages the full capabilities of modern web technologies for interactive data visualization.
            
        - can i save umap embeddings in colab and use them for this flask app

[Overleaf Draft](https://www.overleaf.com/project/6697d06e15b57400bac20e26/detacher)

- ✅ send to fazl
    
    Hi, I have created an overleaf draft for the project that includes:
    
    1) An abstract + 1 sentence summary + main contributions outline,
    
    2) Some background info and motivation (will expand upon this soon),
    
    3) Progress of some experiments run so far + notable results
    
    4) Concrete next steps from now to the end of the projectThis is the link to the overleaf:
    
    [https://www.overleaf.com/project/6697d06e15b57400bac20e26/detacher](https://www.overleaf.com/project/6697d06e15b57400bac20e26/detacher)
    
    I have also attached a pdf of it (I will make more improvements after I finish the experiments I'm running today and tomorrow, so this pdf will be updated later)
    
- ✅ fazl reply
    - Which specific LLM architectures do you plan to compare in this study? How many different architectures will be included, and what are their key differences?
    - What criteria will you use to determine the similarity of feature spaces across different LLM architectures? How do you plan to quantify and compare these similarities?
    - What specific evidence do you expect to find supporting the existence of Feature Manifolds? How might this evidence compare to or extend previous findings?
    - What are your hypotheses regarding the generalizability of your potential findings? Do you expect similar results across all types of LLM architectures, or do you anticipate limitations to the universality you might observe?
    - If your study yields positive results, what implications do you foresee for the transferability of interpretability methods across different LLM architectures? How might this impact future research in mech interp?
    - Can you elaborate on how your potential findings might be applied practically in areas like feature steering or transfer learning?