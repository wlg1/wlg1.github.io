# Project Planning (quests)

[Done](Project%20Planning%20(quests)%203798a71e7c5d4a888cad9a7d25a1275c/Done%20b715c92198314529880806d9f206803d.md)

---

### Working on

Clean up code

- ✅ make new copy of code folder and delete old explora files
    - ✅ clean up word probs into: llama2_word_problems.ipynb
    - ✅ clean up llama2 expms nbs into their own folders in repo’s notebooks
    - ✅ clean up llama 2 iter note pruning nbs
    - ✅ clean up llama2 attnpats and ovscores nbs
- ✅ [lllama2_plus1and2_logit_lens](https://colab.research.google.com/drive/1bZ7RUOI9iGqCEIf6qKYybP0ORxuq9wr1#scrollTo=53hE6w62EDLv): are there succsesor MLPs? Somewhat at MLP 20, but [ablation doesn’t show it as hugely impt. it is pretty impt though](https://colab.research.google.com/drive/1Z4SBtG5ZN_Jji7Z9fmhqNlKUqTovpDDW#scrollTo=I9SR5ETh6BWw)
- ✅ practice poster story + potential Q&A you think of when looking at poster
    - sufficient: if you’re just looking at output instead of logit difference, and you knock everything out and keep just the circuit to obtain the same answer, what if there are other circuits? this doesn’t prove those components are important for the task. but this is good for in-depth analysis of comparing performance scores by tweaking parts of the circuit and seeing what happens
    - necessary: this is easier to just see if output changes
    - both are helpful, but we only tried knocking out the circuit for intervaled seqs as it was faster/easier, and this was one of the last tasks we did as the deadline was approaching

[EMNLP prepa](Project%20Planning%20(quests)%203798a71e7c5d4a888cad9a7d25a1275c/EMNLP%20prepa%20139afed922dc80d48c1be70146462e0e.md)

---

---

### Future Work

- clean up code within nbs
    - llama2 ablation
    - llama 2 iter note pruning
    - llama2 attnpats and ovscores

<<<

[monotonic repr paper](https://aclanthology.org/2024.acl-short.18.pdf)

[https://transformer-circuits.pub/2024/jan-update/index.html#](https://transformer-circuits.pub/2024/jan-update/index.html#)

[**Multilingual Features in Large Models**](https://transformer-circuits.pub/2024/jan-update/index.html#dict-learning-scaling)

Words meaning “two”

More tests

- use same 50 runs of rand 4 heads for all
- add seqcont sparse feature circs and circular to related works
- run more tests on 7.11: try rand order vs in-order seq prompts
- for NLP prompts, instead of “destroying  circuit”, try “ablating all but the circuit”

seq ablation

- top 40 seqcont, arithm
- gpt-2 multiple prompts for seqcont
- for random, for 1 prompt, get individual scores and make sure they’re close in distribution, with none of them being outliers
- improve speed of eval prompts by using MM
- ablate top X heads of circuit sets
- *optional*
    - *opt:* for arithm and seqcont, get logit diff scores
    - auto score Spanish prompts
        - multiple random ablation for spanish counting
    - ✅ (Abortrd) measure rankings and what tokens are in the other rankings
        
        an issue with just “seeing the result” from generation is that the prediction of them may be very low, and too close to the others
        
        This is too much info for readers tho, logit diff is enough
        
    - just using correct logit, likewise, doesn’t show differences in rankings. so try logit diff. we can use any arbitrary incorrect token logit- no, this won’t work if the incorrect is just as low always (meaning corruption won’t make it go higher)
        - if both last seq mem and answer are same num of (eg. two) digits, we can get correct and incorrect logit diff by assuming the incorrect is the last sequence member.
            - one digit last member to two digit correct answer is less common so can be ignored (or separated), or just choose ‘8 ‘, where second member is space
            - we found that using logit diff for multi-tok was better than adding correct toks logits
            - check if we can do multitok by giving “a digit first”; compare the “10…. 1” circuit with “1…4” to see if similar (they should be). if more similar than using multitok sum correct logits, we prob can.
    - ablate mlps

interval-k func components

- attn pat figures comparisons (use more data); don’t need all attn pats

*OPT*:

- analyze intersection of intervaled circs and main 3 tasks
    - 6.11 is very impt in +2, +3 giveFirstDigit
        
        Llama2_intervals_giveFirstDigit_attnpats.ipynb
        
        not much different from not giving first digit, same pattern
        
- get most impt MLPs and logit lens
- OV scores of impt heads
- *OPT:* look for multiTok circs (MLPs, mean ablate)

word problems 

- *OPT:* use gpt4 to evaluate word prompt completions, using ‘yes’ or ‘no’
    - see svd hackathon proj
    - No api calls. Output a json file of its generated answers and have gpt4o give a score for each prompt
        - have llama-2 output
    - Do this for both unablated to see what is correct, and of those correct, do this for ablated
    - Manually inspect a sample of 100 of 1000 prompts
    - First try for a few prompts one at a time, then MM

https://arena-uk.slack.com/archives/C057L9GPK19/p1718810195173909?thread_ts=1718810195.173909&cid=C057L9GPK19

Ioi multitoken names

---

### Optional

[To put in writing](Project%20Planning%20(quests)%203798a71e7c5d4a888cad9a7d25a1275c/To%20put%20in%20writing%20cc3ead9e8f8148068a2cd6d2aff95a3d.md)

- three digit addition using “be concise”
- test ablating these circs on IOI and other type of prompts
- corr logit ratios are MUCH higher than for logit diff; that’s why the 80% doesn’t work for corr logit, it needs to be much stricter (keep if 95%?)
- test gpt2 arithmetic
- read circs of: A Mechanistic Interpretation of Arithmetic Reasoning in Language Models
    - models used
        
        ![Untitled](Project%20Planning%20(quests)%203798a71e7c5d4a888cad9a7d25a1275c/Untitled.png)
        
    
    D:\Documents\_library\__articles\llm interp\math behavior
    
    Shared circuits show a connection between seq cont, greater-than, and arithmetic. Unites these three papers.
    
    [https://github.com/alestolfo/lm-arithmetic](https://github.com/alestolfo/lm-arithmetic)
    
    [https://scholar.google.com/scholar?cites=13180253809186561554&as_sdt=5,31&sciodt=0,31&hl=en](https://scholar.google.com/scholar?cites=13180253809186561554&as_sdt=5,31&sciodt=0,31&hl=en)
    
    [https://aclanthology.org/2023.emnlp-main.435/](https://aclanthology.org/2023.emnlp-main.435/)
    
- mean ablate generation
- WHEN does it diverge from addition, multp, to plus 2? Needs instruction though. Try this by ablating circs and generating; this narrows the search to circ subsets instead of all 1024.

To Debug

- ⚠️ why did sinlge tok fibo and 036 fail by having ablation cause “too much incr” (allowing most heads to be removed?) is it bc single prompt?
- ablate by specific pos to check which pos the component attends to
    - Only need do this for word prompts or arithmetic operands

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
- check if the error is with the code by running the code of Llama2_multitok on single prompt 1234
    - Llama_2_multiTok_1234

- +2 interval circuit (multikTok)
    - 1 3 5
    - 3 5 7
    - 11 13 15
- (once have multitok) find llama2 circuits:
    - +2, +3 intervals, +100, multiply, fibonacci
        
        dataset size: 20 prompts, len 4 seqs (except fibon)
        
    - multiTok: spanish nw, months circs
    - ov scores, logit lens, attn pats

---

Optional small improvements:

- we only look at attn pats of what’s considered impt, but what about all else? even if those have similar seq det attn pats, they aren’t used in computation, so can ignore
- “threshold” in iterative node pruning backws is too confusing.
    - # eg. new_perc is still 30, thres is 20, so "too close to 100”
    - But we should have 80 be threshold, not 20, so we have `(new_perc) > threshold` instead of `(100 - new_perc) < threshold` to decide removal. Easier to reason with when coding and debugging.
        - however, then must change every nb and code in repo showcase
- threshold is inaccurate because if an impt component was removed before so that now perf is just above threshold, then a very unimportant component that just reduces by -1 would NOT be removed. but if a diff order- where the unimp component was first- then the unimpt component WOULD be removed. so order and threshold matter a lot.
    - that’s why random is an option- but we cannot just take intersection or most freq then eval perf from that to check if still destroys perf, as that’s not dependent on connectivity?
- multi tok logit score: what if high on first tok, low on second tok pred? does it matter? What if first tok high messes it up bc it still gets that usually right even after ablation?
- new measure of next score: don’t measure top 5, just get the first ranked output
- Instead of taking in the entire corrupted sequence anew each generation, instead add a SINGLE new position to the new corrupted generated position. This allows the clean and corrupted to stay consistent. This is because the tokenizer would have tokens of different lengths for different strings, even if the strings are just “adding onto” previous strings. So the clean and corrupted could have different lengths!
- If just measuring and not logit diff - stop at next space or until corr tok?
- in main, mention appendix has expms for ablating new tokens by 0 or mean?
- ~~clean up “ablate then generate” by re-tokenizing, which should use 0 ablation on the words that have been tokenized as now corrupted won’t correspond to previous words~~

optional, longer implementations:

- ONLY ablate CERTAIN tokens in initial prompt
- whittle down to find all paths for sequence continuation: ablate circuit, and see if it works. If it does, keep on searching for backups to ablate until it doesn’t work anymore.
    - Could it may be distributed throughout the entire thing? If so, we should ablate PART of everything. Possibly using activations differences at every layer.
- circuit for word prompts such as What are the months in a year?
- measure how much sequences generate is corr after it CONTINUES beyond the next member. [Notice sometimes it gets the next correct, but not the othres if it continues.](https://colab.research.google.com/drive/1LPw0da125JQy1qm7nGOFbGwwdO_Fz62M#scrollTo=uemHL8P9uLGk&line=3&uniqifier=1)
    - perf score for multiple tokens: just add up.
- run edge ablation on sub-circuit

double checks:

- for an input where the growing string is diff for each tokenization, (uno cuatro cuatro), compare generating using retokenization vs concat tokens, and compare which one is the same as  `model.generate`.
- zero ablate?
    - how to find what tokens word gets tokenized into in newly concatenated prompt?
    - actually, if we concat tokens, this won’t change what we pass in. So we can still mean ablate. If not, just zero ablate.

---

---

### Future Papers

You can allocate some of these tasks to others who can decide by themselves if they have the ability/interest to tackle them.

[Circuit func mapping](Project%20Planning%20(quests)%203798a71e7c5d4a888cad9a7d25a1275c/Circuit%20func%20mapping%20c0805c4b41df47bea39344d637644b00.md)

[Steering](Project%20Planning%20(quests)%203798a71e7c5d4a888cad9a7d25a1275c/Steering%20234ffb7bcb1646309755764449cbe151.md)

[Circular features](Project%20Planning%20(quests)%203798a71e7c5d4a888cad9a7d25a1275c/Circular%20features%2064fe86bffa3648aa808b1b3e991c7275.md)

- Test prompts in a conversation. As the convo goes on, how does the ablated model handle reasoning? What if you TELL it the answer, even after it’s corrupted? Can you correct its wrong knowledge of the sequence order?
    - Can we change the sequence order by telling or editing/steering?
- can ablating circs destroy performance after fine tuning? diffs of before and after fine tuning for circs?: [https://ar5iv.labs.arxiv.org/html/2403.04706](https://ar5iv.labs.arxiv.org/html/2403.04706)
- Future work: difference in alphabet, if there are any mappigns between letters
- Scale this up from letters to concepts?

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
    

---

### To do: Code Improvements

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

---

## Less Impactful Things to Try

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
    - set actvs similar to `hook_fn_mask_mlp_out` but NOT as means, but as cache from one entirely different run! make sure same sizes. then, see what preds are.

Toy model

More complex sequences with in-context (eg. a1, a3, a2- alternating, etc. See if it can generalize)

both random words + semantically meaningful sequences at unequal intervals

random words at same intervals allows display as attn pat visual; but ablation doesn’t require equal intervals

Eg) He had 1 pencil. Then he had 2 pencils. Afterwards, he got

Ask chatgpt to generate several templates from code

### Future Work Ideas / Postponed

- Circuit Connectivity- better iterative algos for all tasks
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
    
- Circuit Connectivity
    - Ablate neurons, and res stream outputs
    - Feature ablation:
        
        `!pip install git+`
        
        - [https://www.lesswrong.com/posts/LnHowHgmrMbWtpkxx/intro-to-superposition-and-sparse-autoencoders-colab](https://www.lesswrong.com/posts/LnHowHgmrMbWtpkxx/intro-to-superposition-and-sparse-autoencoders-colab)
        
        [https://transformer-circuits.pub/2023/monosemantic-features#phenomenology-feature-splitting](https://transformer-circuits.pub/2023/monosemantic-features#phenomenology-feature-splitting)
        
        [https://transformer-circuits.pub/2023/may-update/index.html#simple-factorization](https://transformer-circuits.pub/2023/may-update/index.html#simple-factorization)
        
        [https://drive.google.com/drive/u/0/folders/1GgF91n2YNLXJD2KHhHe1WUhXe4zRrqQe](https://drive.google.com/drive/u/0/folders/1GgF91n2YNLXJD2KHhHe1WUhXe4zRrqQe)
        
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
- Circuit Functionality
    - is less-than a subcircuit of decreasing seq?
        - Use incontext learning to get less than
    - [Information movement using corruption on diff tokens/positions](https://www.lesswrong.com/posts/u6KXXmKFbXfWzoAXn/a-circuit-for-python-docstrings-in-a-4-layer-attention-only#Patching_experiments)
        
        When clean patched with corrupted, red means “it got worse”? When corrupted patched with clean, blue means “It got better”???
        
        - [https://colab.research.google.com/drive/1swp35sxN_1zNuIW4i4JyhWeY-YUlmUkk#scrollTo=YzmdOdeJIAiY&line=20&uniqifier=1](https://colab.research.google.com/drive/1swp35sxN_1zNuIW4i4JyhWeY-YUlmUkk#scrollTo=YzmdOdeJIAiY&line=20&uniqifier=1)
        - Corrupt “Adam is 1…” mean ablation using repeated seqs
    - The corruption type used in auto ablation and path patching tells the functionality
        
        eg) If a head influences an induction head (find this via path patching / iterative pruning via ablation), that head may be a prev token head (induction requires prev token head)
        
        - Swap at different positions
        - Or random num at a pos
    - Find attnpat + OV scores of heads found from [manual adding and checking perf](Expm%20Results-%20NAACL%208de8fe5b943641ec92c4496843189d36/Early%20Head%20Analysis%20b73c8162b7334655ad1ff91fb236b69e.md)
        - [https://colab.research.google.com/drive/16b8SwFckyC7Gv3RPUX8mme_Y8dfw0o1g](https://colab.research.google.com/drive/16b8SwFckyC7Gv3RPUX8mme_Y8dfw0o1g)
    - record how induction is used differently in each circuit
        
        How induction circuits work differently as sub-circuits in not just similar but dissimilar tasks, and what non-shared components differentiate these circuits from one another; IOI and many others already have induction inherently as a sub-circuit.
        
    - the induction patterns are irregular; attneds n-3, then n-7 instead of n-6
        - Try to reproduce ioi results on early
    - loop through the output of OV unembeddings (just like SVD) and use GPT-4 to classify each (instead of just finding if copying or not). more than just top 5 tokens
    - attn pat on months/words (put in appendix; state in main they had similar patterns)
    - how to tell if a head is inh or boost another? name movers caused pos logit diff, while s inh caused neg logit diff
        - so dont just measure change in logit diff, but pos or neg on heatmap. Read IOI
    - check which heads’ copy scores are specific for numbers, not just “any type”. use multiple input types to those heads. Note that 7.10, 7.11 and 8.11 aren’t “name mover heads”, though 8.10 was a “s-inh” head
        - IOI small circuit (not found by ACDC) only got 87% score of original logit diff in ‘faithfulness’
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