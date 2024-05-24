# Done

[ArXiV Draft v1](Done%20b715c92198314529880806d9f206803d/ArXiV%20Draft%20v1%2035c75a5f1929460fb199edd5fce9a6fe.md)

[NAACL Draft v1](Done%20b715c92198314529880806d9f206803d/NAACL%20Draft%20v1%20cff04ab3612d474cbca60c48f2967762.md)

Interval Sequences on Larger Models - Explora tests (incr num)

Run Llama-2 on same data by March 22nd: [https://aclrollingreview.org/dates](https://aclrollingreview.org/dates)

March 24th - 27th is Author Response for ACL

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
                
                ![Untitled](Done%20b715c92198314529880806d9f206803d/Untitled.png)
                
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
            
            ![Untitled](Done%20b715c92198314529880806d9f206803d/Untitled%201.png)
            
            Either:
            
            1. It’s predicting using the empty space as the prompt (not likely bc/ then all prompts would be the same prediction, but this isn’t happening)
            2. Or, it uses the prompt as input but will predict empty space
        
    - ✅ [Give space in prompt end](https://colab.research.google.com/drive/1mx0zSN7X5u5SBHZR5MrMEVFS-fSD4s36#scrollTo=lAmonB77JUrG&line=1&uniqifier=1) for utils
        
        ![Untitled](Done%20b715c92198314529880806d9f206803d/Untitled%202.png)
        
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
        
        ![Untitled](Done%20b715c92198314529880806d9f206803d/Untitled%203.png)
        
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
        
        ![Untitled](Done%20b715c92198314529880806d9f206803d/Untitled%204.png)
        
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

- ✅ [Fibonacci plan](../Fibonacci%20plan%202e0e51805bee4b44ba09fe671e89ab19.md)
- 🐣 [[Llama2_fibonacci.ipynb](https://colab.research.google.com/drive/1oFGRQxRdqcXb9NDP6Mp-3t6M3LouvWe-#scrollTo=vKYgaZ9JjihZ)](../Expm%20Results-%20Llama%202%20bc7eb66db28f4bbda27403862beea6ec/Llama2_fibonacci%20ipynb%20b59d5b5e54564c2f86a90f04761c6dec.md)
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
        
        ![Untitled](Done%20b715c92198314529880806d9f206803d/Untitled%205.png)
        
    - ✅ Ask DQ on slack
        
        Hi, I was looking to see what's the best way to get the logits for an answer that is split into two tokens? I'm looking to get logits_original = model(dataset.toks) to measure logit diff between clean and corrupted for say "13", but llama-2 splits that into two tokens (as in the image attached). Was thinking of doing "1 2 3 5 8 1" to predict "3" but that seems to be giving too much info to the model. Was also thinking about a way to feed the 1 back into the model and measuring its output logit value of "3", not sure if that is a good approach.
        
    - ✅ David Quarrel response
        
        By definition, p(x,y) = p(x|y)p(y). So, I would measure the probability of "1 2 3 5 8" -> 1 and "1 2 3 5 8 1" -> 3, and then multiply
        
        so yeah, two forward passes
        
        Wait, I'm silly. If you give it "1 2 3 5 8 1", then the output is of shape `(1,6,vocab_size)` . The last entry represents the distribution P( . | 1 2 3 5 8 1), and the second to last represents P( . | 1 2 3 5 8 )
        So, you can extract both out, and then multiply (though it's better to work with log probabilities and add for numerical stability
        You may also want to look into the `logsumexp` function provided by torch, also for numerical stability purposes
        
- ✅ test if tokenizer really is char level, or just for double digits
    
    ![Untitled](Done%20b715c92198314529880806d9f206803d/Untitled%206.png)
    
    It’s not; just for double digits