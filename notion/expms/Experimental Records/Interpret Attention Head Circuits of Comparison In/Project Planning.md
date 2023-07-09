# Project Planning

### Working on

- S-inhibition heads using Explr nb

### Ongoing Issues

- 

### Done

✅ 1) **Learn Existing Techniques and Workflows**

[✅ Learn a workflow of transformer interpretability expms](Project%20Planning%20821fd0c71f4d4a44b5f7b240725c5547/%E2%9C%85%20Learn%20a%20workflow%20of%20transformer%20interpretability%2055b5218ed69840b4b15da2070c413538.md)

✅ 2) **************************************************Choosing a research topic (input pattern’s circuits to study)**************************************************

[Initial Exploration and Brainstorm](Project%20Planning%20821fd0c71f4d4a44b5f7b240725c5547/Initial%20Exploration%20and%20Brainstorm%2006eb3b02c5684ef88cb6f64881f8a44f.md)

3) **Conduct Experiments on Research Topic**

- ✅ Now that we know some expms that can be run based on existing technqiues, begin [Outline Writeup Draft](Outline%20Writeup%20Draft%2096f5c9785c684e359a76ecb09d264875.md) : list secs, figs, tables based on expms to run
    - Use this to guide what to do next
- ✅ Run prelim expms for size comparison: logits lens, actv patching, atten heads, dot product semantic similarity . See: [PLAN- Size Comparison Circuits and Neurons](PLAN-%20Size%20Comparison%20Circuits%20and%20Neurons%201111d95ef57b4131b259ef88363f3010.md)
- ✅ See that similar inputs for size comparison (John is tall. Mary is [short]) also work for the more general case of antonyms, so run same prelim expms for antonyms. See: [Antonym Circuits and Neurons ](Antonym%20Circuits%20and%20Neurons%20824f0d162ce84a8fb09c27f4e4931194.md)
- ✅ Understand how to implement OV matrix “scores” (eg. copy) for custom data
    - This is more impt than path patching b/c it tells the function of the head better
    - Antonym heads: instead of copy scores (same token appears in top logits), check if opposite token appears in top logits
    
    Thus, do these sub-tasks: (in tall_short_circuit.ipynb)
    
    - Candidate heads: check and auto put sigf heads into ‘copy score’ and ‘path patch’
        - Add “Get sigf attention heads” section (from “simple_analogies_circuits, pt3.ipynb”) before path patching
            - ISSUE: library conflict, as explr analysis code uses newer version
                - SOLN: Run code in 2 separate notebooks, transfering data from one to other
    - 1. Understand how to modify datasets to use those techniques
        
        [Custom Dataset for Circuit Discovery](https://www.notion.so/Custom-Dataset-for-Circuit-Discovery-44e775a363e34cc8ad1acfc01383bb6a?pvs=21) 
        
        - one issue may be that not enough examples, because in IOI, it was a different subject each time, and one could create many examples using many subjects. Here, we are predicting adjectives, adn there’s not a lot of adjectives to predict- one can only create one template from this. This template may exchange subjects, but the different subjects don’t matter in this case, because the subject isn’t being predicted.
        - The corruption in this case is just one example (since it should be the same length) that uses antonym adjective
    - 2. Understand how to modify code to use those techniques: [Modify copy circuits code](Modify%20copy%20circuits%20code%20004c16a403b04ddbb7c09b62cad532d7.md)
    - 3. Understand how to analyze the outputs of techniques
- **[POSTPONED]** Move info into more fitting pages from [Antonym Circuits and Neurons ](Antonym%20Circuits%20and%20Neurons%20824f0d162ce84a8fb09c27f4e4931194.md), [PLAN- Size Comparison Circuits and Neurons](PLAN-%20Size%20Comparison%20Circuits%20and%20Neurons%201111d95ef57b4131b259ef88363f3010.md) and [Most Recent S Name Movers](Most%20Recent%20S%20Name%20Movers%20a72ccc6fdccc4e4baa78251399fdd2d7.md)
    - ✅ “Find Antonym” and “Size Comparison” both discuss copy circuits, but it wasn’t modified until “most_recent_S_name movers”. Move their content about copy circuits into a “modify copy circuits page”, and record a rough guess of the order this content was found in “planning”
- ✅ Work on modifying attn head output vs token logit plot
    1. ✅ DONE- Look at IOI notebook for the code. In the copy, create new section analyzing code within the plot function
        
        [IOI notebook code](https://www.notion.so/IOI-notebook-code-fde870610bf0467ca455bcfc8a526f37?pvs=21) 
        
    2. ✅ Modify this code for new “most recent S” dataset
        
        [Most Recent S Name Movers](Most%20Recent%20S%20Name%20Movers%20a72ccc6fdccc4e4baa78251399fdd2d7.md) 
        
        2.1. ✅ put in “end” key in self.word.idx of dataset
        
    3. ✅ Generate more prompts for “most recent S” dataset so more pts on plot
    4. ✅ Doesn't work w/ S1 due to bug about space in front, so fix that in scatter_plot
    5. ✅ Make other changes to scatter_plot to convert its focus on IO and S to S1, S2, etc.
    
- ✅ Move info into more fitting pages from [Antonym Circuits and Neurons ](Antonym%20Circuits%20and%20Neurons%20824f0d162ce84a8fb09c27f4e4931194.md), [PLAN- Size Comparison Circuits and Neurons](PLAN-%20Size%20Comparison%20Circuits%20and%20Neurons%201111d95ef57b4131b259ef88363f3010.md) and [Most Recent S Name Movers](Most%20Recent%20S%20Name%20Movers%20a72ccc6fdccc4e4baa78251399fdd2d7.md)
    - ✅ Create new nb to separate adj identification from most recent name movers
- ✅ [Size Comparison Congruence](PLAN-%20Size%20Comparison%20Circuits%20and%20Neurons%201111d95ef57b4131b259ef88363f3010/Size%20Comparison%20Congruence%20e94368b6a22a4e9e9d0d444b3c5972e5.md) : review and continue
    - ✅ # Dot products of input after first MLP layer: Use this for congruence: z_0 = model.blocks[1].attn.ln1(cache["blocks.0.hook_resid_post"])
    - ✅ Divide results for -large and -small in same notebook
        - [dotprod_size_tokens_GPTsmall.ipynb](../Code%20Notebooks%20432b45bb746f43eabf4172f69d384f8a/dotprod_size_tokens_GPTsmall%20ipynb%2048e2ade011e7429aa6721e08a4666242.md)
    - ✅ ISSUE: the “intermediate output dot product code” used an older version of the library (IOI notebook) to get the model, so it doesn’t work using the setup code from “an neuron” notebook. Move IOI notebook’s setup to GPTsmall dot products and see if it can be run again
        - It runs with no errors
    
- ✅ More diverse examples that output “most recent subject”. [test_prompt_most_recent_S.ipynb](../Code%20Notebooks%20432b45bb746f43eabf4172f69d384f8a/test_prompt_most_recent_S%20ipynb%20a51ecffd653d4d6c995692f0920be200.md)
- [**POSTP**] Writeup activation head patching, scatter plot, and copy scores for subject movers. [Most Recent S Name Movers](Most%20Recent%20S%20Name%20Movers%20a72ccc6fdccc4e4baa78251399fdd2d7.md) into [Draft- Subject Choice Circuits](../Paper%20Drafts%20c8403ec170204b3aa40fd28465a5635d/Paper%20Draft-%20Comparison%20Circuits%20852d577eb555460e87ae511a1750ef50/Draft-%20Subject%20Choice%20Circuits%20293b34dee6104b619beee9b28e7392a7.md)
    - Re-read IOI paper, explor an nb for ideas on which findings to select
        1. Activation Patching for Most Recent Name Movers
        - ✅ Was logit diff commented on? If so, how?
        - Find average logit difference X over N examples (before, only used over 1 example. Try 50 then 500 now, similar to IOI paper)
            - most_recent_S_attn_pat.ipynb : get dataset of more examples.
                
                We just need input prompts and (right, wrong) outputs
                
                We also need a list of descriptions, and a list of single token names. Then make a template that uses placeholders for them, and fill in the template.
                
                - ✅ Try using promptgen from [most_recent_S_name_movers_DRAFT.ipynb](../Code%20Notebooks%20432b45bb746f43eabf4172f69d384f8a/most_recent_S_name_movers_DRAFT%20ipynb%20ee6f1afdee0b4f369cf505ae00aaed4d.md). Note that uses an older library, so see if code is compatible with logit diff
                - ✅ change logit_diff() to not use len(dataset), but dataset.N
                - Edit promptgen code to fit logit diff code
                    - ✅ ISSUE: AttributeError: 'Dataset' object has no attribute 'io_tokenIDs’
                        
                        This means we must further edit dataset
                        
                        However, we can also just use logit diff from Explorartory Analysis notebook. To do so, just generate input prompts and (right, wrong) outputs 
                        
                    
        
        [POSTPONED]
        
        later:
        
        - Generate new descriptions in template
    
    later;
    
    - How was activation head patching described?
        
        
- ✅ Try more variations with different number of names, varying in source and target (eg. s-3 t-3, or s-2 t-3, etc). Continue in [test_prompt_most_recent_S.ipynb](../Code%20Notebooks%20432b45bb746f43eabf4172f69d384f8a/test_prompt_most_recent_S%20ipynb%20a51ecffd653d4d6c995692f0920be200.md) [[LINK](../Code%20Notebooks%20432b45bb746f43eabf4172f69d384f8a/test_prompt_most_recent_S%20ipynb%20a51ecffd653d4d6c995692f0920be200.md)]
- ✅ Writeup activation head patching, scatter plot, for subject movers. [Most Recent S Name Movers](Most%20Recent%20S%20Name%20Movers%20a72ccc6fdccc4e4baa78251399fdd2d7.md) into [Draft- Subject Choice Circuits](../Paper%20Drafts%20c8403ec170204b3aa40fd28465a5635d/Paper%20Draft-%20Comparison%20Circuits%20852d577eb555460e87ae511a1750ef50/Draft-%20Subject%20Choice%20Circuits%20293b34dee6104b619beee9b28e7392a7.md)
    
    [NOTE: Head attribution is different than activation head patching!!!](https://www.notion.so/Exploratory-Analysis-Demo-c61288d8f11b45d993c796ec28a62132?pvs=21)
    
    - ✅ How were “logit diff head attribution” and “activation head patching” results described in previous papers/notebooks?
    - ✅ What do the axes of the scatter plot mean? Check the code.
    - ✅ Interpret new scatter plot results. Use previous writings to map to new results. (NOTE: WHY were this considered sigf enough to write in? If sigf not applicable to current results, avoid writing. Same for ‘not sigf’; include it if it’s a diff case than before)
    
- ✅ **make_latestS_prompts():** Makes new “latest S” dataset by just changing subjects (obtains 4 rand sampled subjs from list of names); don’t change descriptions for now
    
    In most_recent_S_name_movers_DRAFT.ipynb: **Generate more prompts for dataset**
    
    I**n** most_recent_S_attn_pat.ipynb: Try N=10 
    
- ✅ Use **make_latestS_prompts() on avg logit diff [in most_recent_S_attn_pat.ipynb]**
- ✅ [most_recent_S_attn_pat.ipynb] make_latestS_prompts() on actv patch by corrupting
- ✅ run N=10 with GPU (T4)
    
    remember to change tensor, tok code to use .cuda() when running model
    
    T4 takes 11sec to do actv patch on res (CPU takes >5m)
    
- ✅ change N=10 section into N=50
    
    actv patch on res takes 46s
    
    actv patch on layers takes 1m36s
    
    actv patch on heads takes 19s
    
- ✅ analyze and writeup logit lens & actv patch results for multiple prompts
    - ✅ Average logit diff
    - ✅ Activation patching to find impt (layer, tokens)
    - ✅ Impt heads in both logit diff and actv patch heatmaps
    
- ✅ Move some logit diff and actv patch sentences to overleaf draft as placeholders to get a sense of what to carve down or add in
- ✅ Write up copy scores draft; take sentence from prev and apply it to new
- [**POSTP**] Attention patterns (QK) analysis for latest S. [3. Figuring out Head Functionality for Most Recent Name Movers](../Paper%20Drafts%20c8403ec170204b3aa40fd28465a5635d/Paper%20Draft-%20Comparison%20Circuits%20852d577eb555460e87ae511a1750ef50/Draft-%20Subject%20Choice%20Circuits%20293b34dee6104b619beee9b28e7392a7/3%20Figuring%20out%20Head%20Functionality%20for%20Most%20Recent%20%20d35d8e08cfc649d7838236eb03e6bf22.md)
- ✅ Put a table of a few results for “latest S input prompts” in overleaf
- ✅ For GPT-small, describe some dot product results we had so far and put them into ‘expm blocks’ or [Draft- Adjectives Congruence](../Paper%20Drafts%20c8403ec170204b3aa40fd28465a5635d/Paper%20Draft-%20Comparison%20Circuits%20852d577eb555460e87ae511a1750ef50/Draft-%20Adjectives%20Congruence%20f95dc5b0f41c4b10ac6e5a96bde7e8c6.md) .
    
    Just put a sentence or two in for now
    
    - ✅ Get outline from TOC of colab.
    - ✅ Copy analysis from colab + [Size Comparison Congruence](PLAN-%20Size%20Comparison%20Circuits%20and%20Neurons%201111d95ef57b4131b259ef88363f3010/Size%20Comparison%20Congruence%20e94368b6a22a4e9e9d0d444b3c5972e5.md) to draft.
        - ✅ ISSUE: postpone this to fix histogram to prevent “same token” dotprods
        SOLN: This is a triangular format that skips diagonals (since grid is symmetric):
            
            `for i in range(num_tokens):
                 for j in range(i + 1, num_tokens):`
            
- [POSTP] Find if there are S-inhibition heads. See [S-Inhibition for Latest S heads](S-Inhibition%20for%20Latest%20S%20heads%2094ec995d650f408eac783a06732a7f4f.md)
    - TRY: modify new obj Dataset to be used in path_patching (reqs correct methods/vars)
        
        [https://colab.research.google.com/drive/1NCBOLPx038FxwEacmHDsCesWIAW1z8kU#scrollTo=PB3jRKuennZ3&line=3&uniqifier=1](https://colab.research.google.com/drive/1NCBOLPx038FxwEacmHDsCesWIAW1z8kU#scrollTo=PB3jRKuennZ3&line=3&uniqifier=1)
        
        - ✅ Change RELEVANT_TOKENS by downloading old file “blob/main/easy_transformer/ioi_circuit_extraction.py” after downloading repo in setup
            
            ISSUE: the old lib was used via ‘pip install’, which doesn’t get the files on colab
            
            SOLN: fork the repo instead and pip install the forked repo
            
        
        - ✅ In RELEVANT_TOKENS, comment all out except `RELEVANT_TOKENS[head] = ["end"]` . Then commit ioi_circuit_extraction.py and try `do_circuit_extraction()` again
        - Debug: `'Dataset' object has no attribute 'groups'`
- ✅ correlation value in scatterplot
    
    [https://www.notion.so/wlg1/3-Figuring-out-Head-Functionality-for-Most-Recent-Name-Movers-d35d8e08cfc649d7838236eb03e6bf22?pvs=4#46884b3c68fc4d2ab5b1529b1f690869](../Paper%20Drafts%20c8403ec170204b3aa40fd28465a5635d/Paper%20Draft-%20Comparison%20Circuits%20852d577eb555460e87ae511a1750ef50/Draft-%20Subject%20Choice%20Circuits%20293b34dee6104b619beee9b28e7392a7/3%20Figuring%20out%20Head%20Functionality%20for%20Most%20Recent%20%20d35d8e08cfc649d7838236eb03e6bf22.md)
    
    - make new notebook to keep outputs of bugs in prev. **latest_S_name_movers_DRAFT_v2.ipynb** cleans up bugs, runs from start w/o errors
    
    [https://www.notion.so/wlg1/3-Figuring-out-Head-Functionality-for-Most-Recent-Name-Movers-d35d8e08cfc649d7838236eb03e6bf22?pvs=4#c2ccb59d9c30446ca5b7f403795910cd](../Paper%20Drafts%20c8403ec170204b3aa40fd28465a5635d/Paper%20Draft-%20Comparison%20Circuits%20852d577eb555460e87ae511a1750ef50/Draft-%20Subject%20Choice%20Circuits%20293b34dee6104b619beee9b28e7392a7/3%20Figuring%20out%20Head%20Functionality%20for%20Most%20Recent%20%20d35d8e08cfc649d7838236eb03e6bf22.md)
    
- ✅ Neuron Dir: Try [Random Linear Updates on “Language Models Implement .. Vector Arithmetic”](../Expms%20on%20other%E2%80%99s%20work%2020fe4166597c45ed844fbdff1d2bb956/Random%20Linear%20Updates%20on%20%E2%80%9CLanguage%20Models%20Implemen%202d2e575a175b4a7a8ee0228fa87ee998.md)

### Future Work Ideas / Postponed

**Next in line to do**

Activation Patching to find Circuits

Find if there are S-inhibition heads. See [S-Inhibition for Latest S heads](S-Inhibition%20for%20Latest%20S%20heads%2094ec995d650f408eac783a06732a7f4f.md) 

Exploratory analysis nb says just to guess mid layers are doing this, using actv patching on logit outputs; no need for head outputs

[Activation patching on head outputs instead of logits](Project%20Planning%20821fd0c71f4d4a44b5f7b240725c5547/Activation%20patching%20on%20head%20outputs%20instead%20of%20log%20647ee177f3414718b97953d2ccbf8a22.md)

Brainstorm alternative ways to get S-inhibition

- Try new ACDC notebook

[https://colab.research.google.com/github/ArthurConmy/Automatic-Circuit-Discovery/blob/main/notebooks/colabs/ACDC_Editing_Edges_Demo.ipynb](https://colab.research.google.com/github/ArthurConmy/Automatic-Circuit-Discovery/blob/main/notebooks/colabs/ACDC_Editing_Edges_Demo.ipynb)

Heads Functioanlity

- large negative copy score
- **Copy Scores for multiple prompts**
    
    [https://colab.research.google.com/drive/1NCBOLPx038FxwEacmHDsCesWIAW1z8kU#scrollTo=0MBbP2Agg-iR](https://colab.research.google.com/drive/1NCBOLPx038FxwEacmHDsCesWIAW1z8kU#scrollTo=0MBbP2Agg-iR)
    

Congruence

- Neuroscope + Automated by fasttext
- [https://colab.research.google.com/github/neelnanda-io/TransformerLens/blob/main/demos/Interactive_Neuroscope.ipynb](https://colab.research.google.com/github/neelnanda-io/TransformerLens/blob/main/demos/Interactive_Neuroscope.ipynb)
- [https://colab.research.google.com/drive/1lZQkZ5u2mQxsYyiGaUKbW-XjdHP0GJpA#scrollTo=ykzEQtT65KMZ](https://colab.research.google.com/drive/1lZQkZ5u2mQxsYyiGaUKbW-XjdHP0GJpA#scrollTo=ykzEQtT65KMZ)
    
    ~~NOTE: maybe the difference is so small in actv patching bc that neuron 4413 has both tall and short, so the corruption should actually be on a different token? unless tall and short have big logit diff too~~
    
    try patching in all neurons for output that restore ‘decline’ prediction (use in-context) and see if 4413 sticks out
    

Related Work

- **More in-depth literature review**

<<<<<<<<<

**For much later (after finishing items above)**

- make more varied dataset by changing descs, not just subjs
- Figure out the dims for z in copy_scores to see how skipping QK matrix “fully attends to the name tokens”
    
    [https://www.notion.so/wlg1/Modify-copy-circuits-code-004c16a403b04ddbb7c09b62cad532d7?pvs=4#03d0a172e5264aea8c9d28f557a52fe6](Modify%20copy%20circuits%20code%20004c16a403b04ddbb7c09b62cad532d7.md)
    
    - look at IOI copy nbs or [Most Recent S Name Movers](Most%20Recent%20S%20Name%20Movers%20a72ccc6fdccc4e4baa78251399fdd2d7.md)
    - [https://www.notion.so/wlg1/Query-Key-Value-Matrices-fe92464f6ee24068b6aaa56bb85e903e](https://www.notion.so/Query-Key-Value-Output-Matrices-fe92464f6ee24068b6aaa56bb85e903e?pvs=21)
    - what about v?
    
    Work on modifying attn head output vs token logit plot
    
    1. modify template so it’s not source vs target, just a bunch of descriptions about names. show that it just selects most recent name. also repeat names in templates.

<<<

Techniques to Try

- Figure out how updated ACDC takes in custom datasets
    - Check if transformerLens has updated code, or if ACDC has it
- actv patching: understand decomposing heads (value vector vs QK?)
    
    [**Exploratory Analysis Demo**](https://www.notion.so/Exploratory-Analysis-Demo-c61288d8f11b45d993c796ec28a62132?pvs=21) 
    
- Perform actual hypothesis testing to get p-value for congruence histogram (of dot product)? See [Draft- Adjectives Congruence](../Paper%20Drafts%20c8403ec170204b3aa40fd28465a5635d/Paper%20Draft-%20Comparison%20Circuits%20852d577eb555460e87ae511a1750ef50/Draft-%20Adjectives%20Congruence%20f95dc5b0f41c4b10ac6e5a96bde7e8c6.md)
    
    

<<<<<<<<<

Optional

- Why use activation patching on layers vs res stream?
- Patch the layers that show sharp curve changes in layer analysis (both accumulate and sep by attn and MLP). Patch the heads that have big values in head analysis.
- In order to identify what’s a subject, the attention head weights may be “aligned” geometrically (in similar, closer to parallel than orthogonal, direction) to some “space” of subjects. What linear combination of neurons/features spans to make up this space?
- Write program (by chatgpt) to generate prompts of a certain pattern
- “is” seems to be a factual association, but it’s also a relation, so are attention heads involved? Also, “opposites” is an association but it’s a TYPE of association; how does the model differ it from other types of association like “is”?
- Try many prompts about mammals to see which heads are active