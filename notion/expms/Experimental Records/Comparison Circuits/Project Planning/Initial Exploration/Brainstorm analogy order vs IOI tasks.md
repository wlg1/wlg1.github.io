# Brainstorm analogy order vs IOI tasks

- Understand IOI circuit and use that to guide new, similar non-IOI inputs
    
    [https://colab.research.google.com/drive/1n4Wgulv5ev5rgRUL7ypOw0odga9LEWHA?usp=sharing](https://colab.research.google.com/drive/1n4Wgulv5ev5rgRUL7ypOw0odga9LEWHA?usp=sharing)
    IOI Notebook
    
    **Hypotheize** that the "pet is" input has heads identifying subject, then heads determining order. This is based on idea that there are identifying-subjects heads, inhibition heads, ordering heads. Find similar heads using 'head attn' and actv patching
    
    Mary, Fido, Fido. Pebbles, Rachel -> Pebbles
    **Hypothesis**: Thus, Rachel, Mary, Fido are all inhibited
    
    Is there an algorithm for "pet is", like IO?
    	Mary is X. John is Y. Z is Mary.
    	- Identify who is first
    	- remove all that's not the first? (inhibit)
    	- just output the first one
    What if this is changed up to have more than 2? can it reocgnize the changed pattern?
    	try on -xl if -large does bad
    
    Can we inhibit certain heads so it doesn’t output the first, but the one associated with second instead? or ADD/EDIT it to not assume Z = Y (based on position) but on certain traits such “Y has animal, X doesn’t have animal”. 
    More elaborate analogies may have heads that identify traits, eg) what is the relation of the MC to the mentor, to identify who is not the MC (inhibit), check if MC has sword (as freq that hero has sword is large in many examples of hero's journey)
    

---

- Using functions/classes, find a way to repeat the same things we often need to test, but with diff conds/inputs. Put in collapsable or new page that’s searchable/filterable in custom views.
    
    [create tables of useful results]
    
    Focus on analogy order and sequences for combos consisting of:
    
    - different inputs types.
        - Eg) finding ‘cat’ is type of ‘pet’ over ‘human’ failed. what about other subclasses? say teacher, house, color, etc.
        - try providnig the trait in the input. Eg) Mary has paws. John has no paws. The animal is
    - various models
    - various ablations of heads (zero, mean)
    - various corruptions (switch order, add noise to input embeddings)
    
    Things to test correlations for: (use blocking, stat tests, etc)
    
    - using external info?
    - try using more traits
    - ordering: names, traits, sentences
    - stronger markers/boundaries to define separations to model (eg. that is part of source, not target, system)
    - use more examples of the pattern in the source
    - just test on more samples (how similar?)
    
    No need to test every combination; guess when to not test for untested certain combos or to stop testing new examples of already-tested combos,  due to the results of similarly tested combos.
    

---

Create new nb to test simple analogies (before, tested sequences and just the one type of analogy of “the pet is…”)

simple_analogies_circuits, pt2.ipynb

[https://colab.research.google.com/drive/1aOEeY4roW8oWqkZ0MuuZRJXmJGDRNcbr](https://colab.research.google.com/drive/1aOEeY4roW8oWqkZ0MuuZRJXmJGDRNcbr)

- 1) Test on gpt2-large. Provide a source system and then a target system. Use as little external information as possible
    
    Mary has X. John has Y. Z is John. Ashley has X. Ben has Y. Z is
    
    As before, change the order. But don't switch the names order; switch which names have which properties (y, x). This corruption's correct answer is now 'Ashley'.
    
    RESULT: Failure, Ashley is in 5th
    
    Could it be using external information, such as Ben being a man and John being a man? Let's test this.
    
    RESULT: The model doesn't seem to be using external info as it correctly guesses "Ashley". It seems to think the correct analogies is by the "second name of the system".
    
    Note that it does predict Ashley with far less probability than it did when the answer was Ben, but given that these are only 2 examples, we are unsure if this is just a coincidence or a correlation of using gender as external info.
    
    Another thing we can test is to put all of system 1 in one sentence, and all of system 2 in one sentence, and see if that helps it understand the 'boundary' better that we have 2 separate systems.
    
    RESULT: This attempt at a 'system separator' actually makes the probability of the correct answer go down.
    
    Thus, we will not proceed with using "stronger separators" or trying to control for "external gender information" for the next set of expms.
    
    Let's try adding more properties to see if it gets the picture.
    
    RESULT: Interestingly, Ashley goes up in rank. But how often does this happen; was this just a coincidence? 
    
    Try adding more properties.
    
    RESULT: Unlike before, Ashley goes down. So that 'going up in rank' may not have been correlated with 'adding more traits'; it may have been a coincidence. Let's try again, but using actual words instead of variable letters.
    
    In summary, based on these few tests, we have evidence that:
    
    - Changing the order of names doesn’t allow it to get the new correct output as it guesses the same output (which was correct before but isn’t now)
        - This is different from how the paper on IOI corrupted the input, in which changing the names allowed it to get a new corrupt output
    - The gpt-2-large model, to calculate the analogous output, doesn’t: 1) use external info about gender, 2) get affected by separators of source and target systems, 3) improve its guess on the correct output by taking more information about traits into account
    
    **Using actual words instead of variable letters**
    
    This is because it is a LANGUAGE model, so it may respond better to actual words instead of just variables it often doesn't associate with other words.
    
    Switch which names have which properties (y, x)
    
    RESULT: Like in the 'variable letters' case, this approach doesn't get the correct answer when the names are switched with the traits.
    
    ---
    
    Given that gpt-2-large does badly on all these properties that are used in making analogies (identifying based on similar traits b/w source and target, using external info about similar traits, etc), it does not seem like there will be many, or complex enough, analogous inputs it will get the correct output on. 
    
    We want to study a model that does well on analogy-making, to some extent, as we want to study the circuits that allow it to do so, then corrupt inputs and mechanisms to test for which parts of inputs and mechanisms are important for analogy-making. Thus, we decide not to study gpt-2-large, but -xl, which should have improved overall performance on several tasks.
    
    This requires colab pro due to -xl needing high RAM
    
- 2) Test on gpt2-xl
    
    Mary has X. John has Y. Z is John. Ashley has X. Ben has Y. Z is
    
    We find that gpt-2-xl does worse than gpt2-large at the uncorrupted input
    
    "Mary has X. John has Y. Z is John. Ashley has Y. Ben has X. Z is”
    
    gpt-2-xl still doesn’t get the right answer
    
    **Using actual words instead of variable letters**
    
    "Mary has a hat. John has no hat. The student is John. Ashley has no hat. Ben has a hat. The student is”
    
    It still fails at this. it outputs Ben instead of Ashley
    
    Try more/different traits with actual words (we didn't try this for -large either)
    
    try not using ‘no [obj]’ as a trait
    
    Test this on keep trait description order, but switching the order of names.
    
    xl still fails and believes the answer is Ben; it even has MORE confidence that the answer is Ben!
    
    Use more examples of the pattern in the source. First, give it a second example (with answer) where:
    
    - the order is switched
    - use one trait per person
        
        It fails at this too; it still thinks the answer is Ben, by a lot.
        
    
    Check if the second example is just because it’s the most recent (or most frequent type of name-trait ordering) one, or if it’s inferring a pattern from it.
    
    Check if it’s just detecting based on duplicate names, or if it’s detecting based on multiple similar traits.
    
- 3) The simple analogies aren’t being corrected answered so far. Think back to why IOI worked
    
    In this task, NEW names are given (Ben, Ashley) [in the target]; in IOI, it uses the same names. It had heads which “moved” these names and just outputted the same names.
    
    Actually, in this case, it’s still outputting a same name (Ben, Ashley). It just has to recognize the pattern from a source now, instead of having a “built-in” algorithm to recognize the IOI pattern.
    
- 4) Test sentence completions from previous papers using -xl (using diff libs than transformer lens)
    
    This test is done b/c the -xl we’re using may not be the -xl that successfully got outputs from previous papers
    
- 5) Try loading bigger models than -xl (1.5b)
    
    Have 25.5 GB RAM for T4, V100
    
    Have 83 GB system RAM (40gb gpu ram) for A100. but it uses 10x more compute units than T4
    
    [https://neelnanda-io.github.io/TransformerLens/model_properties_table.html](https://neelnanda-io.github.io/TransformerLens/model_properties_table.html)
    
    - gpt-j-6B
        - Your session crashed after using all available RAM. (25gb)
    - gpt-neo-2.7B
        - T4: CUDA out of memory. Tried to allocate 26.00 MiB (GPU 0; 14.75 GiB total capacity; 14.07 GiB already allocated; 14.81 MiB free; 14.09 GiB reserved in total by PyTorch)
        - A100: is able to use this, using 20gb system ram
    - gpt-neo (6b)
    - othello
    - llama (7b)
- 6) gpt-neo-2.7B is able to load using A100. Test it on previous prompts
    
    This fails previous inputs (perhaps not specific enough on what the pattern in the source is) until it gets to this one, which seems to be “specific enough” on what the source pattern is by providing enough traits (but with only 1 example as a source/previous case):
    
    ```python
    "Mary has a hat. John has a cane. John has a vest. The student is John. Ashley has a cane. Ashley has a vest. Ben has a hat. The student is"
    example_answer = " Ashley"
    # Top 0th token. Logit: 15.71 Prob: 36.55% Token: | Ashley|
    # Top 1th token. Logit: 15.62 Prob: 33.67% Token: | Ben|
    ```
    
    But just barely; it is 36% for ashley and 33% for Ben
    
    Use more examples of the pattern in the source. The student is the one with the cane, and it shouldn’t matter what order the cane appears in.
    
    Now it fails and thinks the answer is Ben. Perhaps the example before was just a coincidence, not a correlation.
    
- 7) Note that the model must recognize “has”, associating the name with the trait. Perhaps test if it can do this in the first place before trying to chain it into systems of traits:
    
    `"Mary has a hat. John does not have a hat. The person who has the hat is”`
    
    Yes, it identifies Mary has the hat.
    
    - `"John has a cane. Mary has a hat. The person who has the hat is”`
        
        **`Rank: 14       Logit: 10.71 Prob:  0.81% Token: | Mary|`**
        
        ```
        Top 0th token. Logit: 13.18 Prob:  9.53% Token: | the|
        Top 1th token. Logit: 12.35 Prob:  4.14% Token: | going|
        Top 2th token. Logit: 12.34 Prob:  4.11% Token: | a|
        Top 3th token. Logit: 12.29 Prob:  3.91% Token: | not|
        Top 4th token. Logit: 12.23 Prob:  3.68% Token: | John|
        Top 5th token. Logit: 11.98 Prob:  2.88% Token: | more|
        Top 6th token. Logit: 11.87 Prob:  2.57% Token: | in|
        Top 7th token. Logit: 11.78 Prob:  2.35% Token: | always|
        Top 8th token. Logit: 11.56 Prob:  1.89% Token: | called|
        Top 9th token. Logit: 11.55 Prob:  1.86% Token: | wearing|
        ```
        
        This is an issue 
        
    - "John is tall. Mary is red. The person who is red is”
        
        **`Rank: 6        Logit: 12.22 Prob:  2.99% Token: | Mary|`**
        
        ```
        Top 0th token. Logit: 14.14 Prob: 20.37% Token: | John|
        Top 1th token. Logit: 13.04 Prob:  6.74% Token: | tall|
        Top 2th token. Logit: 12.84 Prob:  5.52% Token: | the|
        Top 3th token. Logit: 12.75 Prob:  5.06% Token: | taller|
        Top 4th token. Logit: 12.64 Prob:  4.51% Token: | not|
        Top 5th token. Logit: 12.32 Prob:  3.29% Token: | a|
        Top 6th token. Logit: 12.22 Prob:  2.99% Token: | Mary|
        Top 7th token. Logit: 11.75 Prob:  1.86% Token: | also|
        Top 8th token. Logit: 11.51 Prob:  1.46% Token: | short|
        Top 9th token. Logit: 11.43 Prob:  1.35% Token: | shorter|
        ```
        
        This is also an issue.
        
- 8) Run attention patterns on inputs anyways just to see if that can explain its top outputs (use -xl)
    
    -xl gets the following, which is clean (no switched order), correct:
    
    ```
    example_prompt = "Mary is a human. Fido is a dog. The pet of this family is Fido. Rachel is a human. Pebbles is a cat. The pet of this family is"
    example_answer = " Peb"
    ```
    
    Top 0th token. Logit: 18.54 Prob: 92.88% Token: | Peb|
    Top 1th token. Logit: 14.16 Prob:  1.17% Token: | a|
    
    **Attention Patterns + Logit Difference Analysis**
    
    We see that "is", the last token, strongly attends to "Peb" for the top 3 positive attention heads at the (is, L), where L is near the "almost" last layers (37 out of 45, 31 out of 45, etc.)
    
    Strangely, the 2nd and 3rd negative attention heads do attend to Peb. But the strongest negative attention head attends to Rachel; perhaps that cancels the other two out?
    
    How does was the attention gradually accumulated in the residual stream all the way to "is"? That is, at what points was it crucial that it started to attend to "peb"? Look at the previous plots.
    
    If we look at the logit difference, it's around layer 30 where the accumulation starts to pick up to separate "Peb" far above "Rachel".
    
    Another thing to notice is that the "of" (prepositions) and "is" (linking verbs) are where attending occurs. So right after the subject, these seem to attend to a subject a few positions back (the last sentence's of or is attends to Pebbles, though that is the most "recent" subject positio-wise), or right before (Rachel is).
    
    So with this, we can see that it’s probably attending to the “most recent subject”. See if this checks out with the other examples.
    
- 9) Reflect why, and post…
    
    The attention patterns for these “simple analogies” seem to output the subject that’s the most recent subject from before, and seems to inhibit more those that aren’t recent. So it’s not actually understanding the analogy but is just finding what’s the most recent subject because “is” attends to the most recent subject from before. 
    
    The structure of “John is….” then asking “The person is…” appears to be a bad structure due to the inverse of where the subject and property are. Though in other notebooks, I’ve used the same subject in the previous sentences and the “to output” sentence and it still doesn’t show improvement in correct output.
    
    But this doesn’t explain why it doesn’t get the correct output for “who has X?” Run attn pats on those and check.
    
- 10) Try “Other Analogy Prompts” using just -large
    
    `John is big. Mary is small. John is tall. Mary is`
    
    Yes, GPT-2-large is able to say “short”!
    
    Top 0th token. Logit: 17.18 Prob: 57.68% Token: | short|
    Top 1th token. Logit: 14.84 Prob:  5.54% Token: | small|
    
    ---
    
    These examples suggest that the model is better at making analogies of TRAITS using external knowledge, than finding the right subject to put in. Before, we tried to make it output the right subject, but it failed when we switched orders; it appeared to just output “the most recent subject”. Now, we’re making it output the right trait, which it is doing better on more of the time.
    

11) We can also analyze the circuits of how the model is able to recognize who “has” a trait. This is a stepping stone to testing analogies. See if -small can do this.

[https://colab.research.google.com/drive/1aOEeY4roW8oWqkZ0MuuZRJXmJGDRNcbr#scrollTo=RsNcYPZJUaCx](https://colab.research.google.com/drive/1aOEeY4roW8oWqkZ0MuuZRJXmJGDRNcbr#scrollTo=RsNcYPZJUaCx)

- simple_analogies_circuits, pt3.ipynb
    
    [https://colab.research.google.com/drive/1GQo_RSEY40ncByvwy81kxwSKGPHlbxSx](https://colab.research.google.com/drive/1GQo_RSEY40ncByvwy81kxwSKGPHlbxSx)
    

Revisit nbs/papers analyzing these types of plots (direct logit lens, attn heads, actv path) to see what other similar analysis you can do on the ones for the new case

- Will adding a source system prevent the model from even considering tall over short within its layers?
    
    No source system:
    
    ![Untitled](../../../Experimental%20Results%208545f5a36448499c934d8659ba08d2c1/EB-%20Analysis%20on%20Inputs%20for%20Tall%20vs%20Short%20370cf22d285243ec9dd1f4ad9e25efe8/Untitled.png)
    
    With source system:
    
    ![Untitled](../../../Experimental%20Results%208545f5a36448499c934d8659ba08d2c1/EB-%20Analysis%20on%20Inputs%20for%20Tall%20vs%20Short%20370cf22d285243ec9dd1f4ad9e25efe8/Untitled%202.png)
    
    There's still a dip. But compare it to before. Before there were two dips, and they were deeper. Also, the end logit diff is bigger now. Could the source sentence be making it "more sure" of "short", through in-context learning and induction heads? Try more examples of "no source" vs "source".
    
    First check the last layer logit diffs in 'test prompts'. Then compare how their layers logit diff changes; is "with source sys" more sure throughout the layers? The (inductive based) hypothesis is that it will be, given this one example.
    
- Try adjective-to-subject identification
    
    John is red. Mary is blue. Connor is green. Mary is
    Connor is green. John is red. Mary is blue. Mary is
    
    name_descrp_circuits.ipynb:
    [https://colab.research.google.com/drive/1QN2Pj1Yjbh7N326HqZBEQ2q_hcFiQVRB#scrollTo=pQpu5-pi4Yu2](https://colab.research.google.com/drive/1QN2Pj1Yjbh7N326HqZBEQ2q_hcFiQVRB#scrollTo=pQpu5-pi4Yu2)
    It fails to give the correct adjective. The model strangely seems to have a circuit that wants to output opposites given this structure, though. So it probably needs a head that attends to the "adjective" then another head that "finds" its opposite.
    After these further tries, stick with analysis of the opposite (size diff, color, etc) circuits.
    
    we hypothesize that all the important heads will be at the end token (for query) and attend to the adjective (key). the opposite heads may do something with the value, or the MLP.
    the value is what's done. writing, copying, etc
    

[Ask online for help](Brainstorm%20analogy%20order%20vs%20IOI%20tasks%208977518d2819431a97dd743c23b94810/Ask%20online%20for%20help%20f26e1b9c13a9477ead2f972ddbc04581.md)

To do next:

- For now, stick with seeing how it identifies the subject to output based on position of subject

---

**To Do:**