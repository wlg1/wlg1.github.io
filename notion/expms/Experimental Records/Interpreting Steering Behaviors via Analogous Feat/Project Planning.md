# Project Planning

[Done](Project%20Planning%20b4b05f73d85e409f8409b209e44ed692/Done%201c002201437341e48b55b8276859a632.md)

---

### Working on

Plan project by summarizing notes so far

- 🐣 project summary
    
    [https://docs.google.com/document/d/1sEoX0fw3JXorOaa5KtN3T-l8aG7aSWZhPmprL7-HDfo/edit](https://docs.google.com/document/d/1sEoX0fw3JXorOaa5KtN3T-l8aG7aSWZhPmprL7-HDfo/edit)
    
- 🐣 plan benchmark
    - [https://chatgpt.com/c/e4f12e4e-9c3e-40fb-bf1f-4334a021399f](https://chatgpt.com/c/e4f12e4e-9c3e-40fb-bf1f-4334a021399f)
        
        Creating a benchmark to measure the effectiveness of steering vectors for large language models (LLMs) involves several key steps. Here’s a general outline of how you might approach this, along with some recommended papers and resources to help you learn more about creating benchmarks:
        
        ### Steps to Create a Benchmark
        
        1. **Define the Objective:**
            - Clearly articulate what you want to measure with the benchmark. For steering vectors, this could include accuracy, robustness, bias reduction, and effectiveness in guiding model responses toward desired outcomes.
        2. **Select or Create Tasks:**
            - Choose a set of tasks that reflect the scenarios where steering vectors will be used. This could include question-answering, summarization, translation, dialogue systems, etc.
        3. **Collect or Generate Data:**
            - Gather or create datasets that represent the tasks. Ensure diversity in topics, difficulty levels, and linguistic variations to comprehensively evaluate the steering vectors.
        4. **Establish Metrics:**
            - Define the metrics to evaluate performance. Common metrics include accuracy, F1 score, BLEU score (for translation), ROUGE score (for summarization), and specific metrics for evaluating bias or ethical alignment.
        5. **Baseline Models:**
            - Include performance of baseline models (without steering vectors) to compare and measure the improvement brought by the steering vectors.
        6. **Experimental Setup:**
            - Design the experimental framework, including how to apply steering vectors, and how to measure their impact on model performance.
        7. **Evaluation and Analysis:**
            - Conduct experiments and analyze the results to determine the effectiveness of the steering vectors. Consider statistical significance and robustness of the results.
        
        ### Recommended Papers and Resources
        
        Here are some papers and resources that can help you learn more about creating benchmarks and measuring the effectiveness of steering vectors:
        
        1. **Benchmarking and Evaluation of Language Models:**
            - "GLUE: A Multi-Task Benchmark and Analysis Platform for Natural Language Understanding" by Alex Wang et al.
            - "SuperGLUE: A Stickier Benchmark for General-Purpose Language Understanding Systems" by Alex Wang et al.
            - "The GEM Benchmark: Natural Language Generation, its Evaluation and Metrics" by Sebastian Gehrmann et al.
        2. **Steering and Control of Language Models:**
            - "Steering GPT-3 to be more specific: Controlling Content Generation with Prompt Engineering" by Various Authors (explore relevant blog posts and articles on OpenAI’s blog).
            - "Plug and Play Language Models: A Simple Approach to Controlled Text Generation" by Angela Fan et al.
            - "Language Models are Few-Shot Learners" by Tom B. Brown et al.
        3. **Evaluation Metrics and Bias Analysis:**
            - "On the Dangers of Stochastic Parrots: Can Language Models Be Too Big?" by Emily Bender et al.
            - "Fairness and Abstraction in Sociotechnical Systems" by Selbst et al. (for understanding fairness and bias considerations).
        
        ### Determining the Size of the Benchmark
        
        The size of the benchmark depends on the following factors:
        
        - **Diversity of Tasks:** Include a wide range of tasks to ensure comprehensive evaluation.
        - **Data Size:** Ensure the datasets are large enough to provide statistically significant results but manageable within computational constraints.
        - **Complexity:** Balance between simple and complex tasks to cover different aspects of model performance.
        
        For example, the GLUE benchmark includes 9 tasks with varying data sizes, while the SuperGLUE benchmark includes 10 more challenging tasks. Aim for a benchmark that includes at least 5-10 different tasks with adequate data points for each to ensure robust evaluation.
        
        ### Conclusion
        
        Creating a benchmark to measure the effectiveness of steering vectors for LLMs is a multifaceted task that requires careful planning and consideration of objectives, tasks, metrics, and experimental design. By leveraging existing research and frameworks, you can build a comprehensive benchmark that provides meaningful insights into the performance of steering vectors in LLMs.
        
- ✅ advice from others on project
    - Minseon
        
        For the pros, she said that model steering seems to be promising field of research, such as a recent paper she learned of “Refusal in Language Models Is Mediated by a Single Direction” that showed the effectiveness of the refusal vector.
        
        For the cons, she said the statement in the summary, "explaining why activation steering works so effectively” is vague, so that I should explain why it’s effective. She said to make my hypothesis more direct and clearer.
        
        We also discussed other points but there were too many to list in a message.
        
        Choose to either make new benchmark or improve method but not both, as that would disqualify previous measurements. 
        
        Overall, from the conversation we decided my project can be restated as: interpreting how steering would affect multiple features in multiple layers, and aiming to develop better techniques to both find and target only intended features and not others. 
        
        It seems like a more concrete project plan statement because it is similar to the concrete experiments done by Neel Nanda cited in the project proposal. However, it is also general enough, as being too specific on a hypothesized approach that may be wrong would lead to dead ends, so I can re-adjust the specifics when needed. 
        
    - clement advice
        
        case study on previous behavior that failed with current techniques (like sleeper agents), or benchmark. with those, effectiveness of steering can be evaluated
        
        use cases of what people use activation steering for production / user experience - easier way, actv steering is more transparent
        
        ‘precise’ is hard to argue. methodlogy doesn’t matter. 
        
        I also just talked to Clement and got good advice about showing how my new approach to steering may be able to allow us to control model behavior more specifically using safety related vectors, such as not just allowing the model to refuse in general, but refuse specific things, such as refusing to answer chemistry. This could have applications to modifying models for more nuanced tasks to avoid generalizing in unintended ways, and improve alignment to specific human goals. I will write up a 1pg draft of this for tomorrow
        
- ✅ read workshop papers and revise project proposal
    
    Thanks for highlighting parts that should be clarified! I’m going to finish revising a clearer version of the project summary during Tuesday. Meanwhile I’ll elaborate more on the first 2 questions (and address the others later, since it’s already long) based on the previous works. I’ve attached this as a pdf since it’s lengthy, and here’s the link to the google docs:
    
    [https://docs.google.com/document/d/1yZ63OpguH7RjFxxUe53wRPg1Rno2Wmulmh3bAG4OrJA/edit?usp=sharing](https://docs.google.com/document/d/1yZ63OpguH7RjFxxUe53wRPg1Rno2Wmulmh3bAG4OrJA/edit?usp=sharing)
    
    1) The statement “explain why adding… works so well” is from the last line of the paper “Activation Addition” (Turner et al 2023) where they discuss future work. I agree this is a vague statement, even in the original paper. It seems, however, it can be implied from the paper that they mean to tie this to a statement from earlier in their paper: “Adding values to imprecisely targeted intermediate memory locations would not yield sensible results in most programs. Why expect this from Transformers?” The authors then go on to say, “Our hypothesis… is that neural networks represent features…. with a linear representation.” So they believe that if features are linear directions, you can just use their simple contrastive subtraction method to obtain a steering vector for most features.
    
    2) That explains what “why adding works” means; but now I believe I have a better way to phrase my topic than that statement. This better way is to address the limitations (A, B, C) stated below. Even if all features can be represented linearly and be obtained by a factor of a “difference-in-means” direction, there may still be many questions about its limitations, such as: A) how to find them (more optimally while minimizing noise) [see: [https://www.alignmentforum.org/posts/C5KAZQib3bzzpeyrg/full-post-progress-update-1-from-the-gdm-mech-interp-team](https://www.alignmentforum.org/posts/C5KAZQib3bzzpeyrg/full-post-progress-update-1-from-the-gdm-mech-interp-team) ], B) how to steer them while minimizing interference (mentioned in the paper discussed in the next point), and
    
    C) In the ICML MI Workshop (Spotlight) paper, “Relational Composition in Neural Networks” (Wattenberg and Viégas), the authors “argue that this success [of the linear rep hypothesis] is incomplete without an understanding of relational composition: how (or whether) neural nets combine these internal representations to represent more complicated relationships.” They give an example of this limitation: “A scene where a duck is perched on a capybara and one where the capybara is perched on the duck would have the same representation.” If “duck on capybara” is “good” while “capybara on duck” is a “threat”, we should steer the model to recognize the former as good and not the other way around- to accomplish this, we would require more targeted steering that looks at mechanisms other than just feature addition. Would we obtain specific features of “duck on capybara” vs “capybara on duck”? This seems inefficient due to the many combinations of concepts. Instead, we can obtain building blocks of concepts and find how they’re composed in the representation space, and alter these composition operations. This is ambitious, but perhaps we can build towards this in small but significant steps. 
    
    Pretraining and fine-tuning can do this, but the aim of editing/steering is to be more interpretable and less of a black box with uncertain outcomes that could possibly result in deceptive agents. With interpretability, it’s like we can use a MRI on deceptive agents to locate “problematic structures” in the geometry of representation space, and then perform surgery to fix them.
    
    Now, I have many ideas for approaches about finding how the model composes concepts in representation space. One of them builds on the ICML MI Workshop (Oral) paper, “The Geometry of Categorical and Hierarchical Concepts”, which assumes the linear representation hypothesis as true and extends it to find that “hierarchically related concepts are orthogonal… complex concepts are represented as polytopes constructed from direct sums of simplices.” This may mean we can manipulate composable concepts as a “hierarchy”, composing feature “knobs” from parent (animal) to child (mammal) to grandchild (cat). Perhaps, instead of finding features separate for each animal, we find a more abstract “animal feature” that all of them share, and then we find more specific animals by performing operations onto this animal feature. This is similar to inheritence in object-oriented programming, which promotes efficient code re-use (if used for the right scenarios). 
    
    I communicated via a few emails with the main author of that paper (who is also the main author of “The Linear Representation Hypothesis" that David mentioned) and he was interested in this idea of steering with more decomposed concepts, and I’m planning to meet with him this Thursday to better refine this plan. By then I would have a better plan written down, likely with some prelim steering expms (though not directly related to the hierarchical concepts code). I think in ~2 weeks, after running more steering experiments, I can talk to others like Nina Rimsky to discuss the steering aspects of this project better.
    
    Also, here are some other possible limitations of steering:
    
    i) I mentioned there may be questions such as “how to find features?” We can take two very large datasets where the only difference is one contains a concept and the other doesn’t, but there’s still a lot of uncertainty in how well this works, such as how do we get rid of a concept in the other dataset- do we just get replace it, or not mention it? But what if that concept isn’t a word, but a long description of a pattern (eg. the duck-capybara example)? Is it position dependent? How much does the dataset structure choice affect the vector you obtain? In addition to diff-of-means, we can use SAEs. But will SAEs always find features we want to change? Large enough SAEs may do this due to “feature splitting”, but we have to experiment with this further and compare across models.
    
    ii) The linear representation hypothesis also isn’t enough to describe the downstream effects of steering (eg. how one feature affects another then affects the output, like a circuit); this is a question I’m investigating in prelim experiments
    
    iii) While several papers have been written with evidence justifying the linear representation hypothesis, this hypothesis still has to go through more tests. Papers such as “Not All Language Model Features Are Linear” (Engels et al 2024) argue that not all features are linear; they present evidence of circular features (eg. months). If the linear representation hypothesis does not hold, then steering using just features as directions is not enough, which is a big limitation of steering we can tackle. 
    
    Overall, I think “extending activation steering to do more targeted output changes” is a better topic statement than “explaining why activation addition works so well”. The latter statement was an older, high-level placeholder, and now with a more thorough literature review I can hone in on a less vague topic. I’ll write all of this up much clearer on Tuesday.
    
- brainstorm why this approach can be useful
    
    Questions about research to pass- if not, weaker justification for doing it
    
    - ✅ msg andy zou and 1st author of ref vec on why steering is useful
        
        Hi, I read your paper on Representation Engineering and had questions about how model steering would be used in practice, as I'm working in a summer research internship with the TVG group at University of Oxford now and am looking to do work in model steering. However, I am trying to justify in a proposal why it would be useful in practice.
        
        In practice, say we want a model to refuse user behavior. We can use the steering vector during inference time for certain inputs, or all inputs. But can we just detect the user input + model output (not shown to the user yet) using another model or algorithm, and just not go through with the request?
        
        I think for other behaviors such as sycophancy it might make more sense though. But I was wondering why use the refusal vector over just not going through with a request that can be detected as harmful through other means? Thank you.
        
        My guesses for why to use steering would be:
        
        1) It may not be possible to perfectly detect what are bad / good outputs every time, so steering is an extra safety net
        
        2) We may still want the model to output something, so not throw everything out that’s good just because there’s some bad
        
        For comparing steering vs fine tuning, I think of 3 reasons: it’s cheaper, more interpretable, and more precise (less side effects, more predictable). 
        
    - Do steering communities care about steering specifics (which can be done by composing)? Justify its use in AI safety
        
        
    - why feature decomposition can’t just be found via model splitting?
    - do features across layers, like a circuit, influence behavior?
    - When steering is used, the steering vector may be used for every user input. But why not just detect the input beforehand (using another model or algorithm to measure output) and not have the model output anything?
    - Preserve invariant structure while changing style is useful for img2img, but what about text?
    - The points about steering’s flaws from (Relational Composition) seem speculative.
    - If care about specifics, why not just not steer on certain specific inputs? What about multiple steering vectors?
    - How is steering even used in deployment? Is it just used on all inputs?
- ✅ ask neel for updates on steering vec decomp
    
    Hi, it's been a while since I last thought about this topic as I was working on other research projects, but without giving out details, I was wondering if it's possible to say if decomposing steering vectors has since led to any promising results, or if it hasn't really been continued? New papers such as Refusal Vector seem to do really well with just difference-of-means and I'm guessing decomposition may have been tried on the refusal vector too. Just asking to see if this is a good avenue to pursue still or not
    
- ✅ **Editing Model Behavior, Proposal Brainstorm v1**
    
    [https://www.overleaf.com/project/6672b8361d6a3cad2420bafc](https://www.overleaf.com/project/6672b8361d6a3cad2420bafc)
    
- ✅ make slides
    
    [https://docs.google.com/presentation/d/1-FK73_RLgU6X3TkWdJmvPo-omlMVQ2bi532wXapvrC8/edit#slide=id.g2153ba3b593_0_372](https://docs.google.com/presentation/d/1-FK73_RLgU6X3TkWdJmvPo-omlMVQ2bi532wXapvrC8/edit#slide=id.g2153ba3b593_0_372)
    
    [https://chatgpt.com/c/391f2a1f-ed25-4997-b2d3-aa457dabf2c9](https://chatgpt.com/c/391f2a1f-ed25-4997-b2d3-aa457dabf2c9)
    
    [https://lucid.app/](https://lucid.app/)
    

Observe how steering affects features downstream

- implement ‘see what steering at a layer affect other features’
    
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
                
                
    - STEP 5: Observe differences, before and after steering, for features from layer k to last layer
        - pass their differences too
- d**ecompose love-hate vector into features**

feature inds or batch_seq inds may not be right because sae flattens them but saelens doesn’t give them as batch_seq. double check if you’re computing the right ones

make shared github

---

- plan
    
    circuits plan:
    
    1. first find features for love-hate in gpt2
    2. then find for safety vectors in larger models
    
    composable geometry plan:
    
    1. first find simplices for animal
    2. then try to find for safety behaviors 
    3. animal steering (cat to dog) and safety behavior simplex steering
    4. see if concepts are also recombined in circuits
    
    First paper (ICLR) may just be about this technique in smaller models, such as love-hate or finding animal composability relations. (eg. this would still be a paper with impt findings, like how the IOI-SAE feature paper did this just for iOI). If have time, can extend to safety behaviors in larger models, but this may be for later paper
    
    geom paper may be separate if only find relns for animal, but can combine with steering vecs circuits if find geom relns for love-hate
    
    starting steering vecs (behavior interp circuits): love-hate (small), anger (xl)
    
    first find this in smaller models as a proof of concept, then consult with more experts by showing proof-of-concept to extend this to larger models
    

- add plan to slides: (add this to outline at start of slides)
    
    add expms done so far and findings, and why findings don’t mean doesn’t work- it may mean these features are impt
    
    ablate those features to see if they’re really impt, not just have highest actvs for prompt
    

---

ablate all the impt L6 features after steering

ablate and patch

compare features before + after steering 

VS before + after random additions

post vs pre

a * mammal + b*bird 

First compare multiple steering vectors at diff layers

Decompose them

Perhaps downstream features not precise enough. Find them and steer only certain ones

Algo to sel

This is primary. Second is more specific fns

if steer, do we get different feature coeffs from pass in unsteered actvs vs steered actvs?

it’s okay if steering vector is done at post bc you cache the pre at later layers too, so just put them thru the pretrained saes

it could be possible that they’re more interpretable? we get a higher percentage of nonzero feature coefficients after steering.

resid pre vs resid post

What is a change in feature considered impt? Traceback? All features should change. Some drastic changes. Perhaps steer feature and ablate another feature. But why not just ablate that feature?

Can we distrust person type X but trust person type Y?

first compare interpreting features without relation to steering vector. what do we find?

then decompose steering vectors at each layer. compare their features. 

plot these features before and after steering. what happens to their simplex relations?

decompose sae into features

but also steer features in later layers too, and the upstream ones that affect the steering vector

claim: in IOI, they had stronger effect by steering features at multiple sites. another paper also argues that multiple vector steering is effective

why not just get steering vectors for multiple layers? yes, but then we decompose them. and we also see what they affect. 

an algorithm to select which multiple featuers across layers for steering is effective. develop it with chatgpt

In slides list assumptions of hypothesis and state how will test them. And if doesn't hold true how project still successful

If rind too compelx for safety vehavioes, then something in between ioi and deception or sycopjancu

Do you need this? Useful?

Task-specific SAEs vs s. Full-distribution SAEs

“SAEs trained on either the IOI dataset (task-specific SAEs) or the LLM’s pre-training dataset (fulldistribution SAEs)”

“task-specific SAEs allow us to edit attributes by changing fewer features compared to full-distribution SAEs.”

why find circuit instead of just using steering vectors?

because steering circuit is “better”?

“(2) the features can be used to edit capability-relevant information in internal model representations”

so you first need supervised dictionaries? so circuits act as supervision?

[https://arxiv.org/pdf/2405.08366](https://arxiv.org/pdf/2405.08366)

aim of original paper: 

“we cannot directly evaluate the usefulness of features learned by an SAE, as we do
not know the hypothetical ‘true’ features to begin with”

- simple supervised methods can be used as a principled way to compute high-quality
feature dictionaries in a task-specific context;

• these dictionaries can be used as ‘skylines’ to evaluate and contextualize the performance of unsupervised methods, such as SAEs.

---

Run code of “The Geometry of Categorical” on new data related to behavior

- brainstorm how to extend hierarchical concepts
    - steer by animal simplex
        - get convex hull that represents “animal” and add it?
            - how do you even add this?
            - estimate vector and convex hull using trained projection (LDA, linear map)- which to recommend?
- put face features thru existing code (geom, circ) on multiple models and look for hierachy (dog face and human face orthon) and other patterns
- find where hierarchy is detected in code nbs
    
    3_Noun_Heatmap.ipynb
    
    animal has cosine 1 with all others concepts bc they are all related to animal. but why 1, the max?
    
- understand `store_matrices.py`
    
    In “Linear Repr Hyp” paper, gamma (umembedding into output space) is transformed into g using the causal inner product by “unifying” it with the input (embedding) space prompt. This g is calculated by equation 3.8, and is the g of this code.
    
    In `1_Animal`, this g is used to obtain the condition in equation 4.1- g(relevant item in category) has similarity with the linear repr of the concept in category, but is orthogonal to irrelevant concepts
    
    `animals_g` is a dict of concept:tensor that takes a slice from  `g`, which is a tensor of shape `[256000, 2048])` , and puts it in in the concept. So g must have first index be vocab,  animals_g['mammal'].shape is `([194, 2048])`, it’s possible that’s 194 different animals? It’s different from animals_g['bird'].shape, which is`([115, 2048])`. So this first number is specific to each key in animals. 
    
    But g is just direction, not a vector with magniutde. So we need to use `estimate_cat_dir`
    
    `animals_token.keys()` : `dict_keys(['mammal', 'bird', 'reptile', 'fish', 'amphibian', 'insect'])`
    
    So there are only 6 categories of animals, and indeed, the first idnex of animals_g are types of those animals: `animals_token['mammal'][0:5]` is `['▁beaver', '▁Beaver', '▁panther', '▁Panthers', '▁Panther']`
    

to go over with kiho and other authors:

1. propose steering project using hier concepts
- ask about papers
    1. Why do we need to unify input and output space? How does this help with steering?
        1. is it that a concept in one space is “the same” as the concept in the other?
        2. Author response: sec 3 of lin repr paper, the inner product is not interpr, the prob distr is preserved. the inner product in each space is arbitrary. what’s the right notion of inner product? 
    2. animal may not be binary, but is it “not animal”? so would there be a vector for each polytope categorical concept? but dog isn’t a binary concept either, yet it’s a vector. and animal does have a vector representation l_animal that says animal is a binary feature. this is orthogonal to the simplex. but shouldn’t they be the same, as they’re both animal- so parallel, not orthogonal?
        1. The animal dir is calculated here: `dirs.update({'animal': estimate_cat_dir(all_animals_tokens, g, vocab_dict)})`
        2. or, is this simplex NOT the same as animal, but is the difference between each concept that’s NOT animal? in other words, it’s all the things that make each concept different from animal?
        - Author response:
            1. conditional prob: animal - dog is (dog | animal), so not really steering concept
            2. embeddings space is probability distribtuion and is hard to find vector rep with dir and magn with 0 and 1. but only want to change target concept without changing other concepts. this may not be the right direction decomposition
            3. if some value is subordinate to another value, should not affect the subvalued conditioned on the upper value. simplex ; position of trianlge (perpendicular line o fit) is parallel to animal. projection onto direction. 
            4. this fig 3 spce is not the same as activation space. fig 3 is unembed space. so varying along fig 3 gives different probability in output. 3d subspace of vocab space
            - gamma is original unemb vector, within weight matrix of unembed matrix. g is tranformed to causal inner product by centering and whitening ( uncorrelated and each have variance 1). unified means lambda bar w and gamma bar w are the same. they map to the same thing in causal inner product space.
                1. dirs for animal bird etc, when add these to embedding, the intervention did work. but not sure if this is the real embedding from some context. so maybe intervening is out of space.
                2. embd space means final layer hidden states of last hidden tokens. so both are after final layer. this paper computes what the model ends up with and if those representions have similiaries
                3. intermediate layers are more complicated with logit lens. kiho says they’re not linear; after final layer, the last step is layer norm (which is not linear), but not concrete
                4. contrastive sentences: if concept is sentiment, on movie reviews, is easy. but if we add this difference to news or other things, it will not give it. out of distribution. may be open problem. so train must match test. test out if train on news and add to movie. so that’s why we want a more general direction. what if used a very big dataset that contained those, perhaps is better. but test set should out of distribution. 
                - do polytopes exist in intermediate space? the umbed should be at point of simplex.
                    1. simplex not found in intermediate space yet but not that meaningful. decomposition
                    2. steer by simplex: korean chinese english, their categorical concepts means
                    3. direct sum in fig1a means thm 6 d and e means animal-plant dir is ortho to mammal-animl so subspace spanned by these diffs are orth to animal, so this simplex is orth to this dir. 
                    4. define concept carefully. now, it’s actv after final layer so it’s for next word prediction. so intermediate feature is hard to define.
                    5. polytope of clusters- try to find, may be a simplex
                    6. ablate the simplex of (mammal bird reptile)- would that leave you with animal? then you could isolate a concept. so simplex are the differences. span(animal- mammal, animal-bird, etc). simplex can be more than 3 things. 
                    7. animal is repr as binary vector. animal has no counterfactual definition. binary feature is animal and not animal, but not same as counterfactual
                    8. an animal vector, the simplex polytope is not animal category, is the differences. 
            1. adj mat in fig 5: if feature is conn by a subset relation, so 0 means no relation and 1 means they’re subset
1. ask about code

Analogous reasoning: finds missing structure and infers from it, just like knowing the first ind of tensor is batch, so we can understand that’s batch too. This structure must be represented somewhere. Especially for induction. How does it remember a pattern? 

[https://arxiv.org/pdf/2302.07384](https://arxiv.org/pdf/2302.07384)

The Geometry of Neural Nets’ Parameter Spaces Under Reparametrization

---

Start from existing features and find supporting features and backup features when ablated

This will help us find the exact side effects too

Subtract and decompose the patch

My guess is if we don't find this others will find this soon

yarin- STTEERING oxford

The Geometry of Neural Nets’ Parameter Spaces Under Reparametrization

Is it measuring similarity in some other space?

why certain layers? perhaps it’s because those layers contain that feature. but it is also because those features have important interactions with downstream layers, like in a feature circuit? then if we modify the feature circuit, perhaps we can 1) improve the steering vector (see above measurements) or 2) obtain steering on more specific types of behaviors.

multiple layers; multiple vectors may make it more specific

don’t make activation addition be another black box; decompose and interpret it even further (like bio to chem to physics)

Use differences to find features

Why not just find features? Bc sv may not be found from saes. Can steering vector be found from saes?

Not just feature interactions, but component. Then find features in components 

Use diff of means to find vevs ghen decompose to find features and connect th9se features

[https://www.lesswrong.com/posts/DtdzGwFh9dCfsekZZ/sparse-autoencoders-work-on-attention-layer-outputs](https://www.lesswrong.com/posts/DtdzGwFh9dCfsekZZ/sparse-autoencoders-work-on-attention-layer-outputs)

https://transformer-circuits.pub/2021/framework/index.html

read/write residual streams, so edges between components

[https://medium.com/@zepingyu/123-cb62513f5d50](https://medium.com/@zepingyu/123-cb62513f5d50)

ask austin about doing benchmarks

reply to andys

what if subtraction makes actvs go to negative? where do existing prompts fall in measurement of love-hate? can we measure this via projection? 

---

[https://academia.stackexchange.com/questions/82582/oral-vs-poster-vs-workshop-which-is-the-most-prestigious-in-the-context-of-comp](https://academia.stackexchange.com/questions/82582/oral-vs-poster-vs-workshop-which-is-the-most-prestigious-in-the-context-of-comp)

[https://openreview.net/group?id=ICML.cc/2024/Workshop/MI#tab-accept-oral](https://openreview.net/group?id=ICML.cc/2024/Workshop/MI#tab-accept-oral)

[https://www.reddit.com/r/LocalLLaMA/comments/1dipzxs/full_paper_is_out_refusal_in_language_models_is/](https://www.reddit.com/r/LocalLLaMA/comments/1dipzxs/full_paper_is_out_refusal_in_language_models_is/)

[https://openreview.net/pdf?id=zzCEiUIPk9](https://openreview.net/pdf?id=zzCEiUIPk9)

[https://openreview.net/forum?id=bcV7rhBEcM](https://openreview.net/forum?id=bcV7rhBEcM)

dict end to end

[https://openreview.net/forum?id=DwhvppIZsD](https://openreview.net/forum?id=DwhvppIZsD)

clip

[https://openreview.net/forum?id=akCsMk4dDL](https://openreview.net/forum?id=akCsMk4dDL)

steering vectors

[https://openreview.net/forum?id=3eBdq2n848](https://openreview.net/forum?id=3eBdq2n848)

**Controlling Large Language Model Agents with Entropic Activation Steering**

[https://openreview.net/pdf?id=kUGkpykJdh](https://openreview.net/pdf?id=kUGkpykJdh)

face

[https://arxiv.org/abs/2306.03819](https://arxiv.org/abs/2306.03819)

leace

[https://chatgpt.com/c/9501c7d4-24df-4814-8ffd-0a2f0dc36393](https://chatgpt.com/c/9501c7d4-24df-4814-8ffd-0a2f0dc36393)

explain this in layman's terms. does it mean all features can be obtained by difference of means?: [https://blog.eleuther.ai/diff-in-means/](https://blog.eleuther.ai/diff-in-means/)

[https://blog.kuzudb.com/post/wcoj/](https://blog.kuzudb.com/post/wcoj/)

https://blog.kuzudb.com/post/wcoj/#a-thank-you--an-anecdote-about-knuths-reaction-to-the-term-worst-case-optimal

[https://arxiv.org/pdf/2310.07837](https://arxiv.org/pdf/2310.07837)

Measuring Feature Sparsity in Language Models

[https://www.alignmentforum.org/posts/zj3GKWAnhPgTARByB/saes-discover-meaningful-features-in-the-ioi-task](https://www.alignmentforum.org/posts/zj3GKWAnhPgTARByB/saes-discover-meaningful-features-in-the-ioi-task)

[https://arxiv.org/pdf/2405.08366](https://arxiv.org/pdf/2405.08366)

[https://openreview.net/pdf?id=JdrVuEQih5](https://openreview.net/pdf?id=JdrVuEQih5)

A Systematic Comparison of Sparse Autoencoder Variants for Model Steering on the IOI Task

---

- impt papers measuring analogous features
    - the geometry of categorical and hierarchical
        
        questions to ask authors
        
        - did they do this for predictions?
        
        things to try
        
        - add simplices to steer different hierarchies
        - do this for predictions
        - how do steering vectors
    - linear repr hypothesis
    - platonic repr hypothesis
    - circuit complexity vs geometry
    - similarity survey (2023)
    - successor heads- extracting addable abstractions (similar to activations vectors)
        - try to break it (when does it not work?)
    - func eqv features
    - Transformer visualization via dictionary learning: contextualized embedding as a linear superposition of transformer factors
- impt papers on steering feature relations
    - sparse feature circuits
    - ripple effects
    - scaling monosemanticity
    - Automatic Discovery of Visual Circuits
        - [https://openreview.net/pdf/0fafa04c83370f95d637dc509e78e7d77ea3c9da.pdf](https://openreview.net/pdf/0fafa04c83370f95d637dc509e78e7d77ea3c9da.pdf)

**Main topic**: Measure what groups of feature RELATIONS are affected by steering vectors (or other vector representations) across models to pinpoint that targetting them will improve steering vector by reducing noise

- Steer by feature relations?
- Sparse features can STILL have relations to one another in geometric space! AND we can decompose these vectors- bc they’re vectors.

scaling monosem:

Feature splitting 

Features as Computational Intermediates

[https://transformer-circuits.pub/2023/monosemantic-features/index.html#phenomenology-feature-splitting](https://transformer-circuits.pub/2023/monosemantic-features/index.html#phenomenology-feature-splitting)

- san fran feature splits
    
    We also find evidence of [feature splitting](https://transformer-circuits.pub/2023/monosemantic-features/index.html#phenomenology-feature-splitting) [8] , a phenomenon in which features in smaller SAEs **“split” into multiple features in a larger SAE, which are geometrically close and semantically related to the original feature, but represent more specific concepts**. For instance, a “San Francisco” feature in the 1M SAE splits into two features in the 4M SAE and eleven fine-grained features in the 34M SAE.
    
    similar features have small angles between their dictionary vectors.
    
- idealized features
    
    We conjecture that there is some idealized set of features that dictionary learning would return if we provided it with an unlimited dictionary size. Often, these "true features" are clustered into sets of similar features, which the model puts in very tight superposition. Because the number of features is restricted, dictionary learning instead returns features which cover approximately the same territory as the idealized features, at the cost of being somewhat less specific.
    
    In this picture, the reason the dictionary vectors of conceptually similar features are similar is that they are likely to produce similar behaviors in the model, and so should be responsible for similar effects in the neuron activations. For instance, it would be natural for a feature that fires on periods to predict tokens with a leading space followed by a capital letter
    

if the sae is better, then we can steer by features. so will a very big sae decompose into many composable specific features? red dog → red, dog

if so then we can steer by “analogous” hierarchical, wacky specific compositions

does feature splitting occur earlier for sae from 12mil to 18mil, then take approach

"feature relations" aren't as intuitive to humans for language as they are for vision (eg. we identify a face via relations between noses, eyes, etc but it's not as intuitive to phrase this for language concepts, though the anthropic papers do mention feature relations in the umap plots)

Also I've thought about the "universal patterns" and I think that would be too ambitious for a project, given that identify some taxonomy of model representations would require a lot of models and careful descriptions of them, it would take a while, so I think I will pivot from that to something similar but less ambitious

better interpret later layer features- sae paper doesn’t seem to do this? compared to ICA etc which is faster but less interprateable

are there features that sae can’t isolate? feature splitting may do this, so try this

use ACDC to locate the impt layers or components then train saes on the impt components of those layers

would you get same sae features from unablated vs ablated unimpt components? this might get smaller sae with more precision

if you have really good sae, you can just steer with those features, so don’t need steering vector?

you still are interested in how steering those features affects other features? and can bthey be deocmposed

are certain features only expressed in multiple layers?

look at MI server #sparse-coding (logan riggs) says did try multiple layers but disentanglement using MLP, so expresses features in a diff language, so have to get something invariant to this translation

2 layers, hypothesize MLP is destroying entanglement. can we stitch together two layers, extend sae architecture to include linear layer between or train a translator?

platonci repr hypothesis paper

certain steering vectors are composed of multiple layers?

if i add together which features from sae base, can we reconstruct how the model is building a steering vector?

basis of svd not guaranteed to be same basis as sae; energise of eigenvec are impts

Just start by running prev relevant paper code on new data of your problem and look for patterns across them. Then modify them slightly to fit stepping stone questions of your problem you want to uncover

Find an inscope subproblem that will help advance this field:

** face relation, eyes nose mouth: dogs and humans

find sae + lin probe features across models

unify sae and lin probe? is there a way to compare them using cosine sim?

ways to measure feature relns:

1. cosine sim
2. causal patching
3. sim metrics across models
4. clustering
5. mapper, topo invariants (betti)
6. func eqv patching cross-models (nikhil, cat the)
7. jaccard (bau, gurnee)

ask todd for linalg advice; pair prog on lin alg proj code on steering feature vectors and seeing effects on features in next layers

[https://chatgpt.com/c/d5e58a44-0435-4126-9ec7-599afb64c2b0](https://chatgpt.com/c/d5e58a44-0435-4126-9ec7-599afb64c2b0)

- how does it differ from regular linalg, looks like its just geom transf
    
    Projective Geometric Algebra (PGA) differs from regular linear algebra in several key ways, although it builds on linear algebra concepts. Here are the main differences:
    
    1. **Homogeneous Coordinates**:
        - **Linear Algebra**: Typically deals with vectors in Euclidean space using Cartesian coordinates.
        - **PGA**: Uses homogeneous coordinates to represent points, lines, and planes in projective space. This allows for the representation of points at infinity and more flexibility in handling geometric transformations.
    2. **Geometric Interpretations**:
        - **Linear Algebra**: Primarily concerned with vector spaces, linear transformations, and solving systems of linear equations.
        - **PGA**: Extends these concepts to include geometric objects and their relationships. It is particularly well-suited for representing and manipulating geometric transformations such as rotations, translations, and scaling in a unified framework.
    3. **Multivectors and Operations**:
        - **Linear Algebra**: Focuses on operations involving vectors and matrices, such as dot products and matrix multiplication.
        - **PGA**: Introduces multivectors (combinations of scalars, vectors, bivectors, etc.) and operations such as the geometric product, outer product, and inner product. These operations are designed to work naturally with geometric entities and transformations.
    4. **Transformations**:
        - **Linear Algebra**: Uses matrices to represent linear transformations. Transformations are typically applied to vectors.
        - **PGA**: Uses the geometric algebra framework to represent and apply transformations directly to geometric objects (points, lines, planes) in a more intuitive and algebraically consistent manner.
    5. **Unification of Geometric Concepts**:
        - **Linear Algebra**: Requires different tools and methods to handle various geometric transformations and concepts (e.g., separate methods for translation, rotation, scaling).
        - **PGA**: Provides a unified algebraic system that can handle a wide range of geometric transformations and relationships seamlessly. For example, a single framework can represent both rotations and translations, which are treated separately in traditional linear algebra.
    6. **Higher-Dimensional Extensions**:
        - **Linear Algebra**: Extends to higher dimensions but often with increasing complexity in handling geometric interpretations.
        - **PGA**: Naturally extends to higher dimensions while maintaining consistent geometric interpretations and operations. This makes it powerful for applications in computer graphics, robotics, and physics.
    
    In summary, while PGA builds on the foundation of linear algebra, it extends and enhances it to provide a more comprehensive and unified approach to handling geometric transformations and relationships. This makes it particularly useful in fields that require sophisticated geometric reasoning and manipulation.
    
- why study multivectors ? what applications this has to nueral network latent spaces
    
    Studying multivectors and understanding their applications can offer several advantages, particularly in fields like computer graphics, robotics, physics, and even neural networks. Here’s an exploration of why multivectors are studied and their potential applications in neural network latent spaces:
    
    ### Why Study Multivectors?
    
    1. **Unified Framework for Geometric Transformations**:
        - Multivectors provide a unified framework to represent and manipulate geometric transformations such as rotations, translations, and scaling. This is particularly useful in 3D graphics and robotics where complex transformations are common.
    2. **Efficiency and Compactness**:
        - Using multivectors can lead to more efficient algorithms and compact representations of geometric data. This can improve computational efficiency and reduce storage requirements.
    3. **Intuitive Understanding of Geometric Relationships**:
        - Multivectors offer a more intuitive way to understand and work with geometric relationships. They make it easier to reason about the interactions between different geometric entities (points, lines, planes).
    4. **Extensibility to Higher Dimensions**:
        - The framework of multivectors extends naturally to higher dimensions, providing a consistent way to handle complex geometric and algebraic problems in higher-dimensional spaces.
    
    ### Applications in Neural Network Latent Spaces
    
    1. **Enhanced Feature Representation**:
        - In neural networks, particularly in deep learning, latent spaces represent compressed versions of input data. Using geometric algebra and multivectors, it may be possible to encode richer geometric relationships in these latent spaces, potentially leading to better feature representations.
    2. **Improved Geometric Transformations**:
        - Neural networks, especially convolutional neural networks (CNNs) used in image processing, can benefit from the robust and unified transformation capabilities of multivectors. For example, representing transformations in latent spaces more accurately could improve tasks like image recognition and object detection.
    3. **Equivariance and Invariance**:
        - Geometric algebra can help in designing neural network architectures that are equivariant or invariant to certain transformations. This means the network’s output can change predictably (or remain unchanged) when the input undergoes specific transformations, which is valuable in applications like computer vision and reinforcement learning.
    4. **Learning Geometric Relationships**:
        - Multivectors could enable neural networks to learn and encode geometric relationships directly. This is beneficial in tasks where spatial relationships are crucial, such as in 3D object recognition, scene understanding, and robotics.
    5. **Regularization and Constraints**:
        - Incorporating multivector representations can help impose geometric constraints and regularization in neural networks. This can lead to more robust and generalizable models by embedding prior geometric knowledge into the learning process.
    
    ### Example Use Cases
    
    1. **3D Computer Vision**:
        - In 3D computer vision, using multivectors can improve the network’s ability to understand and process 3D shapes, perform object detection, and recognize objects from different viewpoints.
    2. **Robotics**:
        - For robotic manipulation and navigation, multivectors can help neural networks better understand and manipulate spatial relationships, leading to more accurate and efficient robot control.
    3. **Physics Simulations**:
        - In physics-based simulations, representing physical entities and their interactions using multivectors can lead to more accurate models that neural networks can learn from and predict.
    4. **Generative Models**:
        - In generative models like Variational Autoencoders (VAEs) and Generative Adversarial Networks (GANs), multivectors can improve the representation of latent spaces, leading to better generation of complex structures such as human faces, natural scenes, and 3D objects.
    
    In summary, studying multivectors and applying them in neural network latent spaces can lead to more powerful, efficient, and geometrically aware models. This can enhance performance in various applications, from computer vision and robotics to generative modeling and beyond.
    
- what relation do multivector have with simplicial complexes and hierarchical concepts in latent space
    
    Multivectors, simplicial complexes, and hierarchical concepts in latent spaces can interrelate in meaningful ways, particularly in the context of geometric and topological data analysis, and machine learning. Here's how they connect:
    
    ### Multivectors and Simplicial Complexes
    
    **Multivectors**:
    
    - Multivectors are elements of geometric algebra that can represent various geometric objects (scalars, vectors, bivectors, trivectors, etc.).
    - They provide a compact and algebraically rich framework to describe geometric transformations and relationships.
    
    **Simplicial Complexes**:
    
    - Simplicial complexes are a combinatorial structure made up of simplices (points, line segments, triangles, and their higher-dimensional counterparts).
    - They are used in computational topology to study the shape of data, particularly in persistent homology, which is a method in topological data analysis.
    
    **Relation**:
    
    - Multivectors can represent the oriented volumes of simplices in a geometric algebra framework. For instance, a bivector can represent an oriented area (a 2-simplex), and a trivector can represent an oriented volume (a 3-simplex).
    - In computational topology, geometric algebra can be employed to perform operations on these simplices more efficiently and intuitively, leveraging the algebraic structure provided by multivectors.
    
    ### Hierarchical Concepts in Latent Space
    
    **Hierarchical Latent Spaces**:
    
    - In machine learning, particularly in neural networks, latent spaces are representations where data is encoded into a lower-dimensional space.
    - Hierarchical latent spaces involve multiple levels of abstraction, where higher levels capture more abstract features and lower levels capture more concrete features.
    
    **Relation to Simplicial Complexes and Multivectors**:
    
    - **Simplicial Complexes**: These can be used to model hierarchical relationships within the data. For example, different layers of simplices can represent different levels of abstraction in the latent space, capturing hierarchical structures within the data.
    - **Multivectors**: By leveraging the rich algebraic properties of multivectors, one can efficiently encode and manipulate these hierarchical structures. For example, a multivector can represent complex hierarchical relationships within the latent space, capturing interactions between different levels of features.
    
    ### Applications
    
    1. **Topological Data Analysis (TDA)**:
        - **Using Simplicial Complexes**: TDA involves using simplicial complexes to study the topological features of data. Persistent homology, a TDA technique, can identify and analyze features at multiple scales, providing insights into the hierarchical structure of data.
        - **Multivectors**: In TDA, multivectors can represent simplices in a way that facilitates geometric computations, making it easier to analyze and manipulate topological features.
    2. **Neural Network Latent Spaces**:
        - **Hierarchical Representations**: In neural networks, especially deep learning models, hierarchical latent spaces can be used to capture complex, multi-scale features of the input data.
        - **Geometric and Topological Insights**: By representing these hierarchical features using simplicial complexes and multivectors, one can gain deeper geometric and topological insights into the latent space, potentially leading to better understanding and improvements in model architecture and performance.
    3. **Geometric Deep Learning**:
        - **Combining Concepts**: Geometric deep learning aims to extend deep learning techniques to non-Euclidean spaces (graphs, manifolds). Using multivectors and simplicial complexes can provide a framework for such extensions, allowing the models to capture more complex geometric and topological structures within the data.
    
    ### Summary
    
    - **Multivectors** provide a powerful algebraic tool to represent and manipulate geometric objects and transformations, which can be applied to simplicial complexes in computational topology.
    - **Simplicial Complexes** are crucial for understanding the topological structure of data, especially in hierarchical and multi-scale contexts.
    - **Hierarchical Latent Spaces** in neural networks benefit from these concepts by allowing for richer, multi-level representations of features, leading to potentially more robust and insightful models.
    
    By integrating these concepts, one can create more sophisticated models that leverage geometric and topological properties of data, leading to advancements in fields such as data analysis, machine learning, and beyond.
    

- run sparse feature circuits code

repr eng: bias term from cojntrastive to steerm ; combine multiplying featuers ; inefficient transformation 

Phi models toy models

Eun kim

is it same truth vector of PCA for all true-false contrastive statements? universal

DOLA: DECODING BY CONTRASTING LAYERS IMPROVES
FACTUALITY IN LARGE LANGUAGE MODELS

https://arxiv.org/abs/2402.09090

[Multimodal interp notes](Project%20Planning%20b4b05f73d85e409f8409b209e44ed692/Multimodal%20interp%20notes%2046f2ab3a3b3642d2b1d09e8c1c9608bc.md)

[https://www.simplexaisafety.com/](https://www.simplexaisafety.com/)

[https://www.lesswrong.com/posts/gTZ2SxesbHckJ3CkF/transformers-represent-belief-state-geometry-in-their](https://www.lesswrong.com/posts/gTZ2SxesbHckJ3CkF/transformers-represent-belief-state-geometry-in-their)

[https://www.lesswrong.com/posts/mBw7nc4ipdyeeEpWs/why-would-belief-states-have-a-fractal-structure-and-why](https://www.lesswrong.com/posts/mBw7nc4ipdyeeEpWs/why-would-belief-states-have-a-fractal-structure-and-why)

https://youtu.be/5dggwz76Qys?si=k-Ef1u0WDpaoAZiR

Compu mechanics wolfram

https://people.maths.ox.ac.uk/nanda/

can we use sae as filter function in mapper to construct a simplicial complex? the clustering is based on the sae feature space?

[https://x.com/viditnanda/status/1778540829998805094](https://x.com/viditnanda/status/1778540829998805094)

[https://x.com/viditnanda/status/1778540829998805094](https://x.com/viditnanda/status/1778540829998805094)

venhoff00@gmail.com

features correspond to syntactic aspects. syntax becomes one single semantic aspect

multiple polysemantic features together act as monosemantic 

find circuit for function vector

is it solving higher lvl task

**Discovering Latent Knowledge in Language Models Without Supervision**

[https://imtiazhumayun.github.io/grokking/](https://imtiazhumayun.github.io/grokking/)

obsidian graph tool

https://x.com/dashstander/status/1802501901209960638?t=-IkIBrku8L07piuMukRbMw&s=19

https://x.com/chanindav/status/1802933505367953430?t=sQxME-k8gzgJRopimlS9IA&s=19

https://youtu.be/jSAT_RuJ_Cg?si=WVPy2CwFiKIXVMA4

Arc challenge

14m dreamcoder

Filter local during training to grok

Filter local in early layers to global analogies (contact logit lens Thang)

Find evidence of simplices in more than just animals first then contact vidit

Contact kiho on ideas

ask minseon on opinions of adv exmps by topoact; grok

---

Researchers so far;

Phil fazl

Austin

Possible:

Clement louis luke amir

Todd

Vidit

Kiho Victor

bei wang- Utah algtop

Konstantin

Euan

Conmy

Multicellular (future work)

---

[Similarity measurements](Project%20Planning%20b4b05f73d85e409f8409b209e44ed692/Similarity%20measurements%2059d99860501849cfb9960f028265819b.md)

Steer by feature relations of distance or causal. This is true steering by concepts. Concepts are captured by a network of features, not a single feature. A bridge vs golden gate Bridge. In that case, it's not saes. 

Kernel is distance between samples, not features

Structure preserving feature relations

Feature must be at some threshold 

Sim measure within model between hierarchical analogous concepts

measure common subspace

Relation in terms of containment, and replacement mapping, not just distance. Locked in to map multiple chains of connecting relns

Trace backwards single token inputs or two contrasting differing by single input. Measure the feature dim for traits along each. Do this for both neurons, sae features, components. Then measure distances between these features. Is there a pattern?

Ask gpt4 to critique and refine this

Issue is hard to isolate commonality. What if more than one commonality? Even for vision models. For text, there's position. But sample at many pos, many contexts and they have commonality. If use synonymous tokens or of Same class.

https://youtu.be/zBnkO8p32w0?si=sDj_TTxkAYy5HdgY

But sep features, like blue dog and red dog, can be two sae features. Analogous steering

Topological

Make sep shared team notion without all the info

Alignment of steering vectors across models via features

Nonlinear features

No steering benchmark

If bias exists in frozen embedding,  doctor closer to man in woman, is there inherent bias in clip output?

Used to br frozen text and frozen img then just train Bridge. But now is training end to end, not separate img and txt models. Chameleon meta

after sae transformation, we align two models by a cross-model sae. then, apply alignment-based measures

slides: explain in a line how past/curr work in overlapping + diverging circuits (for seqcont) can help with studying overlapping + diverging feature circuit calculation for this project

---

kmeans cluster to find inputs that activate the same features

Steer models with similar features from same or related cluster- what's the difference? Is there a correlation between feature similarity and output effect?

[https://transformer-circuits.pub/2024/april-update/index.html#ablation-exps](https://transformer-circuits.pub/2024/april-update/index.html#ablation-exps)

dampen and ablation have simialr effect, much bigger than doubling

steering is both subtracting and adding. feature steering in successor heads is abalting then adding

any corruption of actv patching with ordered seqs finds successor heads

bloom trained gpt2-small saes, so just use pretrained there. A6000 has 80Gb for [vast.ai](http://vast.ai) for tinystories and pythia 160m. even this takes 8hrs

to choose threshold, relative effect: how steering changes circuit relative to non-steering

attribution patching is less precise but more efficient

ablate and scale pre-existing gpt-2 small circuits from marks

error terms of saes to circuits

if run model without this, not accurate. but 

if they could ablate features in feature circuits for small, may also be able to steer with small. steer grammar rules

https://arxiv.org/abs/2405.07987

[https://twitter.com/phillip_isola/status/1790488966308769951](https://twitter.com/phillip_isola/status/1790488966308769951)

https://github.com/minyoungg/platonic-rep

- remarks
    
    What they actually show is that 1) affine maps do a pretty good job of translating between the representation spaces of different NNs across, and 2) as models get stronger, they tend to have representation spaces that align more closely with each other. There are a lot of other hypothesis that explain these results so I think they jump the gun a little by dedicating >half the paper to analysis
    
    1. One could be that neural networks are predisposed to learning spaces that can easily be mapped between with affine transformations. Another is that we might see a plateau in representation alignment once the models have eaten up all the low-hanging fruit on lossless abstractions
    2. ***May 16, 2024 4:21 PM (EDT)*May 16, 2024 4:21 PM (EDT)*May 16, 2024 4:21 PM (EDT)***
        
        One thing to consider in their graphs that plot models on axes of language capability vs alignment with vision models is that it seems linear but if you switch out the language capabilities with the compute cost of training, you'll see what might end up being an asymptote
        

https://www.reddit.com/r/MachineLearning/s/ElJYeGM9JX

[https://twitter.com/hamandcheese/status/1707158049834639663](https://twitter.com/hamandcheese/status/1707158049834639663)

[https://twitter.com/mattecapu](https://twitter.com/mattecapu)

[https://twitter.com/bgavran3](https://twitter.com/bgavran3)

---

### Future Work

- [The fact that both features contribute to the final output indicates that the model has partially predicted a sentiment from John's statement (the second feature) but will do more downstream processing on the content of his statement (as represented by the first feature) as well.](https://www.notion.so/Scaling-Monosemanticity-Extracting-Interpretable-Features-from-Claude-3-Sonnet-3219b222ee8943ac9ba1a07963f975b0?pvs=21)
    - Can we better formalize these causal relations between features?
- success heads: change form numerals to ranks
- 80Gb instead of 40Gb for A100- vast ai may specify this
- automatically find steering vectors using dataset samples
- [https://www.lesswrong.com/posts/qykrYY6rXXM7EEs8Q/understanding-sae-features-with-the-logit-lens#Characterizing_Features_via_the_Logit_Weight_Distribution](https://www.lesswrong.com/posts/qykrYY6rXXM7EEs8Q/understanding-sae-features-with-the-logit-lens#Characterizing_Features_via_the_Logit_Weight_Distribution)
- [https://discordapp.com/channels/1080558777608183829/1229803194331304047](https://discordapp.com/channels/1080558777608183829/1229803194331304047)
- UNDERSTANDING AND CONTROLLING A MAZESOLVING POLICY NETWORK
    
    [https://arxiv.org/pdf/2310.08043](https://arxiv.org/pdf/2310.08043)
    
    decompose cheese vector
    
- saelens: train sae on gpt2-xl L20 and put steering vector through it, then interpret top features\
- mapper
- Feature complexity paper
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

instead of deleting file, transfer new code into shared nb by deleting all old cells and pasting new ones from ‘select all’

---

- store their steering vectors
- add by features of decomposed steering vectors (which are just mean diffs of sample sets)
- auto-label dataset examples of a feature
- cluster by features
- cluster by samples

---

- is it 3rd last b/c adds end of seq token somehow in some operation? Find this operation
- clean up nbs and update repo
- Method to reduce dead neurons using loss constraints which force learned wright's to have activations be within useful feature range
- Code to decompose CAA activations + steered actvs
    - then do Machiav activations
- Steering is by prompts, not model. CMAP is by model. Compare them.
- [https://apartresearch.com/project/from-sparse-to-dense-refining-the-machiavelli-benchmark-for-real-world-ai-safety](https://apartresearch.com/project/from-sparse-to-dense-refining-the-machiavelli-benchmark-for-real-world-ai-safety)
- Study: https://github.com/nrimsky/CAA