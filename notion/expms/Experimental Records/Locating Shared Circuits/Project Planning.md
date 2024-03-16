# Project Planning

[Done](Project%20Planning%203798a71e7c5d4a888cad9a7d25a1275c/Done%20b715c92198314529880806d9f206803d.md)

---

### Working on

Get some results by March 22nd: [https://aclrollingreview.org/dates](https://aclrollingreview.org/dates)

March 24th - 27th is Author Response for ACL

You only need to apply this to more tasks on Llama, Pythia. 

Interval Sequences on Larger Models - Explora tests (incr num)

- ⚠️ In new drive folder, test prompts on Llama-2. See if can do 2, 4, 6 and Fibonacci
    
    [test_prompts_llama2_7b.ipynb](https://colab.research.google.com/drive/1zFWHdQkE8vpRe6PcQwoOVz1qAdNBwtdY#scrollTo=DcZG9rm2IAiA)
    
    - issue: why two ranking lists? first is for empty string.
- ✅ [Llama2_num_runModel_explrTests_v1.ipynb](https://colab.research.google.com/drive/143roK4-FGgqqxtoM1ohDRe95enEdcVW6#scrollTo=vKYgaZ9JjihZ)
    - ✅ try get unablated (orig) logit diff score
        - ✅ ISSUE: freezes when tokenizing dataset for `dataset = Dataset(prompts_list, pos_dict, model.tokenizer)` because of long list of `Keyword arguments {'add_special_tokens': False} not recognized.`
            - search this repo for why Keyword arguments {'add_special_tokens': False} not recognized. occurs when llama 2 uses model.tokenizer: [https://github.com/neelnanda-io/TransformerLens](https://github.com/neelnanda-io/TransformerLens)
                
                The issue you're experiencing with the `{'add_special_tokens': False}` keyword argument not being recognized appears to be related to how different tokenizers handle the addition of special tokens (such as beginning-of-string tokens) to inputs. Specifically, in the context of the TransformerLens project, there have been discussions and fixes regarding how the OPT and LLaMA models' tokenizers prepend tokens to the inputs.
                
                For the Facebook OPT tokenizer, it was observed that it automatically prepends a `</s>` token to OPT prompts unless the tokenizer call explicitly sets `add_special_tokens=False`. This behavior was not affecting the GPT tokenizer. A solution proposed was to conditionally set `add_special_tokens=False` based on the model type, specifically for OPT models, to prevent this automatic prepending from happening【5†source】.
                
                Further discussion on this topic suggested that handling of the `add_special_tokens` parameter might need to be more nuanced, potentially involving checks against the model's tokenizer name or the model architecture to ensure compatibility across different models without introducing unexpected bugs【5†source】【6†source】.
                
                Another related issue was reported for LLaMA models, where the beginning-of-string (bos) token was always prepended for strings processed by the `HookedTransformer` methods, which use the `.to_tokens()` function. This was due to the `add_special_tokens=False` setting not being applied to LLaMA models, although LLaMA's tokenizer, similar to OPT's, adds a bos token by default. A fix was proposed to automatically infer the `add_special_tokens` parameter for the tokenizer, addressing the issue where an extra bos token was being added unintentionally【7†source】.
                
                These discussions and fixes illustrate the importance of carefully managing tokenizer settings and the `add_special_tokens` parameter when working with different models within the TransformerLens project or similar frameworks. The goal is to ensure that tokenization behavior aligns with the expectations for each specific model type, preventing issues like unwanted token prepending.
                
            
            SOLN: For now, just use dataset of 12 samples %%capture
            
        - ✅ ISSUE: orig score is 0
            - ✅ Check corr logits and incorr logits are diff
                
                They’re the same ids
                
            - Check prompts dict for what was in corr and incorr
                
                ![Untitled](Project%20Planning%203798a71e7c5d4a888cad9a7d25a1275c/Untitled.png)
                
                The logit diff isn’t measured by the 1st rank token minus incorr token. It’s what’s marked as the correct token, regardless of if correct token is 1st ranked or not. This means it doesn’t matter what 
                
                SOLN: In dataset, just take `self.tokenizer.encode(prompt["corr"])[-1]` instead of `0` because `model.tokenizer.decode(29945)` is 5
                
    - ✅ ISSUE: out of mem even for 12 samps
        
        decide to try diff route
        
    - ✅ Try pure seq instead for 12 samps
        - ISSUE: the incorr token logits are higher than corr token logits (neg diff score)
            - Check token ids of prompts and corr, incorr.
                
                Notice we use up to 14. The padding for llama’s tokenzier on numbers after 10 seeems to split them up, meaning there is more padding on “1 2 3 4” earlier prompts. Does this make a difference? Yes; putting it in with extra padding messes it up, not predicting “5”. 
                
- ✅ if you add padding to the end of a prompt, will transformers treat the padding as different than if there was no padding, and predict for the padding as the last token instead?
    
    Yes, when you add padding to the end of a prompt for a transformer model, it can affect the model's predictions, but perhaps not in the way you might initially think. Padding tokens are a special kind of token used to bring sequences of words or tokens to a uniform length, enabling batch processing of input data by the model. These padding tokens are typically ignored by the model during predictions due to the use of attention masks.
    
    In the context of natural language processing (NLP) and transformer models, an attention mask is applied to specifically ignore these padding tokens during the attention calculations. The attention mechanism is a core component of transformer models, allowing them to focus on relevant parts of the input data when making predictions. By using an attention mask, the model can differentiate between actual input data and padding, effectively treating the padding as non-existent for the purposes of prediction.
    
    So, while the presence of padding alters the input sequence, the model is designed to predict ignoring these padding tokens as if they were not part of the input. This means that the model will not "predict for the padding as the last token" because, from the model's perspective, the padding tokens are masked out and do not influence the prediction of actual content tokens.
    
    However, the addition of padding can still have indirect effects on model performance, especially if the padded sequences are significantly longer than the original content, potentially impacting computational efficiency. But as far as predictions go, transformer models are designed to handle padding gracefully and predict as if the padding were not there, thanks to attention masking.
    
- ✅ Try for only 1 sample to avoid inconsistent padding issues
    
    [Llama2_num_runModel_explrTests_v2.ipynb](https://colab.research.google.com/drive/1mx0zSN7X5u5SBHZR5MrMEVFS-fSD4s36)
    
    - ✅ ISSUE: orig score still neg, same values for first prompt, despite `utils.test_prompt` now correctly predicting 5 (example prompt has no padding at end)
        
        So padding wasn’t the issue
        
        - Look at highest tokens to see what it’s predicting then
            
            SOLN:
            
            ![Untitled](Project%20Planning%203798a71e7c5d4a888cad9a7d25a1275c/Untitled%201.png)
            
            Either:
            
            1. It’s predicting using the empty space as the prompt (not likely bc/ then all prompts would be the same prediction, but this isn’t happening)
            2. Or, it uses the prompt as input but will predict empty space
        
    - ✅ [Give space in prompt end](https://colab.research.google.com/drive/1mx0zSN7X5u5SBHZR5MrMEVFS-fSD4s36#scrollTo=lAmonB77JUrG&line=1&uniqifier=1) for utils
        
        ![Untitled](Project%20Planning%203798a71e7c5d4a888cad9a7d25a1275c/Untitled%202.png)
        
    - ✅ Give space in prompt end to get logits
        
        It works
        
- ✅ post on ARENA slack your findings
    
    It seems that when I tried a prompt like "1 2 3 4", the llama model in transformerlens, the tokens with the highest logit would be the "" empty space, and the top 5 wouldn't have "5" either. But using "1 2 3 4 " with a space at the end allowed 5 to be the token with the highest logit. Still looking for a better work around as this seems gimmicky. Also, seem to be running of memory easily with A100 for llama-2 so may switch to nnsight as I did before.
    
- ✅ run ‘ablate each attention head’ on 1 samp of llama-2
    
    Llama-2 has 32 heads per layer
    
    - ✅ ISSUE: S0 lookup issue because pos_dict starts using S1 hard-coded, so change to S0 to S3 instead in both prompts_lsit and Pos_dict and prompst_list_2
    - ✅ ISSUE: Now the loop tries to find S4, saying it’s not found. So look in code to see why it’s looking for S4 when neither prompts_list nor pos_dict have it as a key.
        
        ```python
            SEQ_POS_TO_KEEP = {}
            for i in range(len(model.tokenizer.tokenize(dataset_2.prompts[0]['text']))):
                CIRCUIT['S'+str(i)] = lst
                if i == len(model.tokenizer.tokenize(dataset_2.prompts[0]['text'])) - 1:
                    SEQ_POS_TO_KEEP['S'+str(i)] = 'end'
                else:
                    SEQ_POS_TO_KEEP['S'+str(i)] = 'S'+str(i)
        ```
        
        SOLN: Running this in colab, we find there’s 8 positions because the random prompt using integers greater than 10, which breaks down into tokens of more than 1.
        
    - ISSUE: it’s NOT the integer, it’s tokenizer the empty space as a token!
        
        ![Untitled](Project%20Planning%203798a71e7c5d4a888cad9a7d25a1275c/Untitled%203.png)
        
        Seems like the llama tokenizer.tokenize works differently than the tokenizer for GPT-2, which would break ‘1 4 4 3’ into just four tokens for each integer instead of making each space be a token
        
- ⚠️ pos_dict all pos (even spaces)
    
    [Llama2_num_runModel_explrTests_v3.ipynb](https://colab.research.google.com/drive/1w49rGrjH55D2pBwqtH_qS7kd10xzuT52#scrollTo=vKYgaZ9JjihZ)
    
    This deletes previous explora tests and cleans up code. Don’t hard code pos dict but make key for every tokenized token
    
    - ⚠️ ISSUE: why are the scores all negative (meaning removal makes incorr be higher than corr for any of these components, so they’re essential?)
- ✅ try fix tokenizer using slack suggestion
    
    [Llama2_num_runModel_explrTests_v4.ipynb](https://colab.research.google.com/drive/1W-w3CqxNKN08VUwJblLy6g1vvOeG7Lva)
    
    `tokenizer = LlamaTokenizer.from_pretrained(LLAMA_2_7B_CHAT_PATH, use_fast= False, add_prefix_space= False)` 
    
    > using `'use_fast'= False, 'add_prefix_space'= False` when defining the tokenizer makes the problem go away (though you have to add spaces manually. it's a bit messy
    > 
    
    This doesn’t fix test prompt. Getting rid of space at end also makes it predict ‘ ‘ instead of corr token.
    
- ✅ respond to slack about persisting issue
    
    I added them using tokenizer = LlamaTokenizer.from_pretrained(LLAMA_2_7B_CHAT_PATH, use_fast= False, add_prefix_space= False) and it fixes encode and decode (encode('5') encodes it into padding <s> and 5 IDs without the ' ') but it seems test_prompt still has two rankings for ' ' and 5 (it's not directly used in ablation so it doesn't need to be correct) and logits_original = model(dataset.toks) still predicts empty space ' ' as the top token unless the space is added to the end of the input prompt (I suppose this is what you meant by add spaces manually)? 
    
- ✅ Llama2_num_runModel_explrTests_v3: fix why are the scores all negative
    
    SOLN:  You changd the wrong line of code of what to ablate. 
    
    ```
    circ = [(layer, head) for layer in range(32) for head in range(29, 31)]
    to_loop = circ.copy()
    ```
    
    `circ` should ALWAYS start off as the full circuit, while to_loop should contain which heads to remove from circ one by one but independent of one another (this isn’t acdc yet)!
    
    Try going from 20 to 30 first, as most likely that’s what’s impt
    
- ⚠️ run on 1…12 pure num samps
    
    [Llama2_num_runModel_explrTests_v5.ipynb](https://colab.research.google.com/drive/11Nmwec2lwDDakMskq-ENo0HtjDXliOyx#scrollTo=vKYgaZ9JjihZ)
    
    Before, was only on 1 samp
    
    - ISSUE: tokenizer breaks up digits into individual tokens
        
        ![Untitled](Project%20Planning%203798a71e7c5d4a888cad9a7d25a1275c/Untitled%204.png)
        
        It appears to be a **Character-Level Tokenization, even though this says it’s BPE:**
        
        [https://huggingface.co/docs/transformers/en/model_doc/llama2](https://huggingface.co/docs/transformers/en/model_doc/llama2)
        
- ✅ run on  1…9 pure num samps (5 total)
    
    [Llama2_num_runModel_explrTests_v6](https://colab.research.google.com/drive/1_X-FGghmCEAQzbKIagMOCuiVl7Ew_Rl4#scrollTo=DcZG9rm2IAiA)
    
- ✅ [Llama2_numerals_amongItems_AttnPats.ipynb](https://colab.research.google.com/drive/1iiTVFV7bw-FQBmt22W_4sz6epni36BE3)
    
    uses transformerlens because saves the cache
    
    Llama-2 NEEDS A100 high-ram just to load; V100 won’t work
    
    - why A100 has more memory than V100
        
        The NVIDIA A100 and V100 are both high-performance GPUs designed for data center use, catering to different demands in computation, AI, and deep learning tasks. The A100, being a more recent addition to NVIDIA's lineup, boasts more memory than the V100 due to several factors:
        
        1. **Technological Advancements**: Since the A100 is newer, it benefits from advancements in semiconductor and memory technologies, allowing for higher memory capacities within the same physical space constraints.
        2. **Increased Data Demands**: Modern AI and machine learning workloads have grown in complexity and size, necessitating GPUs with more memory to efficiently process and analyze large datasets.
        3. **Architecture Improvements**: The A100 utilizes the NVIDIA Ampere architecture, which offers significant improvements over the previous Volta architecture used in the V100. These improvements include better memory management and higher efficiency, making it feasible to include more memory.
        4. **Market Expectations**: As the industry progresses, there's a continuous push for more powerful computing resources. NVIDIA designed the A100 to meet these growing demands, ensuring it remains competitive by including more memory to handle larger and more complex workloads.
        5. **Use Case Flexibility**: With more memory, the A100 can cater to a wider range of applications, from AI training and inference to high-performance computing (HPC) tasks. This flexibility makes it a more versatile and attractive option for data centers that handle diverse workloads.
        
        The A100 doesn't just have more memory; it also includes several architectural enhancements over the V100 that improve its overall performance and efficiency, further justifying its place as the successor in NVIDIA's GPU lineup.
        
    
    Use attn heads from here: [https://colab.research.google.com/drive/1_X-FGghmCEAQzbKIagMOCuiVl7Ew_Rl4#scrollTo=susSZdqpqVzd&line=7&uniqifier=1](https://colab.research.google.com/drive/1_X-FGghmCEAQzbKIagMOCuiVl7Ew_Rl4#scrollTo=susSZdqpqVzd&line=7&uniqifier=1)
    
    Found seq detection heads: (3, 24), (5, 25)
    
    analogue to 7.11: (16, 0)
    
    and successor heads: (20, 17) - same one from succ head paper? The paper doesn’t mention what specific one from llama-2 it found, just it found multiple
    
    > In the rest of this work, we perform a case study on the attention head (L12H0) with the maximal successor score in Pythia-1.4B.
    > 

Interval Sequences on Larger Models - Fibonacci

- ✅ [Fibonacci plan](Fibonacci%20plan%202e0e51805bee4b44ba09fe671e89ab19.md)
- [[Llama2_fibonacci.ipynb](https://colab.research.google.com/drive/1oFGRQxRdqcXb9NDP6Mp-3t6M3LouvWe-#scrollTo=vKYgaZ9JjihZ)](Expm%20Results-%20Llama%202%20bc7eb66db28f4bbda27403862beea6ec/Llama2_fibonacci%20ipynb%20b59d5b5e54564c2f86a90f04761c6dec.md)
    - ✅ ISSUE: fibo reqs above 10, but tokenizer breaks double digits into single chars
        
        SOLN: make pos_dict INSIDE Dataset(), after creating `self.toks` because that uses padding=True, which makes all prompts in the tensor have the same length using padding:
        
        ```
        pos_dict = {}
          for i in range(len(self.toks)):
              pos_dict['S'+str(i)] = i
        ```
        
    - ⚠️ ISSUE: must still have same keys for all prompts due to patching requiring specific keys in clean needing the corresponding key from corrupted (?)
        
        ```jsx
             70         for (mlp_type, layer_list) in circuit.items():
             71             seq_pos = seq_pos_to_keep[mlp_type]
        ---> 72             indices = means_dataset.word_idx[seq_pos]
        ```
        
        TRY: start from double digits, don’t go into triple digits
        
        ISSUE: fibonacci quickly becomes triple digits
        
        TRY: clean prompts are double digits at most, corrupted prompts ONLY use double digits
        
        ISSUE: the predicted token, if double digit, may only be a single token! (eg. 89 is 8)
        
        ![Untitled](Project%20Planning%203798a71e7c5d4a888cad9a7d25a1275c/Untitled%205.png)
        
    - Ask DQ on slack
        
        Hi, I was looking to see what's the best way to get the logits for an answer that is split into two tokens? I'm looking to get logits_original = model(dataset.toks) to measure logit diff between clean and corrupted for say "13", but llama-2 splits that into two tokens (as in the image attached). Was thinking of doing "1 2 3 5 8 1" to predict "3" but that seems to be giving too much info to the model. Was also thinking about a way to feed the 1 back into the model and measuring its output logit value of "3", not sure if that is a good approach.
        
    
- test if tokenizer really is char level, or just for double digits
    
    ![Untitled](Project%20Planning%203798a71e7c5d4a888cad9a7d25a1275c/Untitled%206.png)
    
    It’s not; just for double digits
    

Future Work

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