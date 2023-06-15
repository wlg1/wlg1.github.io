# Test feasibility of simpler inputs by mapping to previous workflows

Try mapping new inputs from workflow of [“An” neuron](../Learn%20a%20workflow%20of%20transformer%20interpretability%20e%2055b5218ed69840b4b15da2070c413538/%E2%80%9CAn%E2%80%9D%20neuron%2092888cb0c37548b7949c1d9c3c9d260d.md); keep seeing what can be applied until the analogy breaks down

---

******************************************************Brainstorm new simple inputs (that fit this workflow)******************************************************

I will give you chunks of a research paper. Only reply "yes" until I say otherwise

- Summary
    
    In summary, the article discusses a method of using activation patching on a neuron level to find neurons that are important for predicting specific tokens in a language model like GPT-2. The authors found that the activation of a particular neuron, which they call the "an" neuron, is highly correlated with the prediction of the token "an" in general. They also found that this neuron has a high congruence with the "an" token, meaning that its output weights have a high dot product with the embedding for the "an" token, and that it has a higher congruence with this token than any other token. They further applied a search method to find neuron-token pairs that are mutually exclusive in their congruence and found that the top 5 pairs had a strong correlation between the neuron activation and the prediction of their respective tokens. However, the authors note that there could be other factors at play, such as other neurons or attention heads contributing to a token's prediction, and caution against overinterpreting the results.
    
    - "its output weights have a high dot product with the embedding for the "an" token"
    are the weights vector and the embedding token vector in the same vector space with the same basis?
        
        Yes, the weights vector and the embedding token vector are in the same vector space with the same basis. In GPT-2, the embedding and output weight matrices are learned jointly during training, so they are both represented in the same vector space. The dot product between the neuron's output weights and the embedding for the "an" token is simply a measure of how similar these vectors are in this shared vector space.
        
        - What basis represents them?
            
            The basis used to represent the weights vector and the embedding token vector depends on the architecture and implementation of the model. In the case of GPT-2, the model uses a learned embedding matrix to convert each input token to a continuous vector representation, and the weights of each neuron in the network are learned during training using backpropagation. Both the embedding matrix and the weight vectors are typically represented in the same vector space, and their dimensions are determined by the hyperparameters of the model. However, the specific basis vectors used to represent these vectors are not explicitly specified or known, as they are learned during training through the optimization process.
            

Suggest other tasks that are similar to this research and can be conducted using the methods provided. For example, tasks that look for when to use word X over Y, where x and y are variables for words other than "an" and "a”

- chatgpt answer
    
    There are many possible tasks that could be explored using the methods presented in this research. Here are a few examples:
    
    1. Finding neurons associated with other determiners: Instead of focusing on the "an" vs "a" distinction, we could look for neurons that are specifically associated with other determiners, such as "the", "this", "that", "these", and "those". By using the same approach of searching for neurons with high congruence with specific tokens, we could potentially identify neurons that are responsible for determining when to use each of these determiners.
    2. Exploring other syntactic or semantic categories: We could also use this approach to investigate other aspects of language use, such as verb tense, prepositions, or adjectives. For example, we could search for neurons that are associated with past tense verbs or with specific types of prepositions, such as "in", "on", or "at".
    3. Examining differences between dialects or languages: Another possible application of this method would be to explore differences between different dialects or languages. By analyzing the activations of specific neurons across different datasets or language models, we could identify differences in the way that different languages or dialects use specific words or grammatical constructions.
    4. Investigating language acquisition: Finally, we could use this method to explore how language is acquired by neural networks. By training a language model on a simplified language with specific rules for word usage, we could identify which neurons are responsible for following these rules and learn more about how neural networks learn to use language.
- Generalize why “an” vs “a” was chosen in the previous work
    
    > The choice depends on whether the word that comes after starts with a vowel or not, but GPT-2 can only output one word at a time.
    > 
    
    It seems the authors are wondering why the model can choose “an” or “a” article based on the word after the article, even though it doesn’t “directly see ahead”.
    
    To generalize, think of instances that, given previous tokens A, require choosing token B1 or B2 based on token C.
    
    can we generalize more abstractly? [tbc]
    
- Brainstorm other ideas based on this generalization
    
    He / She
    
    Here are some more examples:
    
    1. Choosing between different verb tenses based on the subject of the sentence. For example, the sentence "He ___ (eat) dinner every night" requires the verb tense to match the third person singular subject "he", resulting in the choice between "eats" or "ate" depending on whether the action is in the present or past.
    2. Choosing between different pronouns based on the gender of the antecedent. For example, in the sentence "Samantha went to the store. ___ (She/He) bought some groceries", the choice between "she" and "he" depends on the gender of Samantha.
    3. Choosing between different punctuation marks based on the structure of the sentence. For example, the sentence "I went to the store, ___ (.) it was closed" requires the use of a comma before the conjunction "it was closed", rather than a period which would result in two separate sentences.
        1. Not good b/c we want just TOKEN C, not requiring more than one token
    4. Choosing between different adjectives based on the noun they modify. For example, in the sentence "The ___ (big/small) dog chased the cat", the choice between "big" or "small" depends on the size of the dog.
    5. Choosing between different prepositions based on the verb used in the sentence. For example, in the sentence "She apologized ___ (for/to) being late", the choice between "for" or "to" depends on the verb "apologized".
- Generalize even further; just try simple patterns
    
    https://docs.google.com/spreadsheets/d/1oOdrQ80jDK-aGn-EVdDt3dg65GhmzrvBWzJ6MUZB8n4/edit#gid=0
    
    [https://www.alignmentforum.org/s/yivyHaCAmMJ3CqSyj/p/XNjRwEX9kxbpzWFWd](https://www.alignmentforum.org/s/yivyHaCAmMJ3CqSyj/p/XNjRwEX9kxbpzWFWd)
    
    Continuing sequences that are common in natural language (E.g, "1 2 3 4" -> "5", "Monday\nTuesday\n" -> "Wednesday”
    
    Find neuron: Look for a SPECIFIC TOKEN (eg. picked an, picked a)
    
    Find circuit: Look for a PATTERN (eg. John and Mary went to a store, John gave Mary; John and Tom went to a store, John gave Tom)
    
- Arbitrarily choose one of these ideas and test if it has the right conditions to apply the first step of the previous workload on it
    
    **First step of workload: Choosing the prompt**
    
    [https://colab.research.google.com/drive/11gsCLfBaC9cpA8S18TUqLTvcnx3ceBbP#scrollTo=x-hNAqAk5KMX](https://colab.research.google.com/drive/11gsCLfBaC9cpA8S18TUqLTvcnx3ceBbP#scrollTo=x-hNAqAk5KMX)
    
    Try “1 2 3 4” - this finds a circuit, not a specific neuron
    
- The “an neuron” prompt seemed to be “completing an analogy.” Theorize again if using analogous inputs is a good fit for these previous workflows
    
    On second thought, the “an neuron” workflow looks for a specific neuron. This may be too restrictive as there may not be a neuron which activates for a certain pattern. Perhaps “interp in the wild” is better as it just looks for more general patterns, in both attn and mlp. There may be no reason to make the input so simple.
    
    Go back to the analogies goal. The models were “bad at consistently outputting correct analogies” but that was when we analyzed it based on its sampled output, instead of just the highest logit. If we look at the logits of gpt2-xl, does it consistently get a good analogy?
    
    This prompt from “an neuron” seems to be “completing an analogy”:
    
    > “I climbed up the pear tree and picked a pear. I climbed up the apple tree and picked”
    > 
    
    Try analogies that don’t require a lot of background knowledge but can be derived based on the input (eg. star wars vs lotr is not a good prompt).
    
    Prompt ideas: 
    
    Try to make something like this, but shorter: *In a family: John is a human. Mary is a human. Fido is a dog. The pet of this family is Fido. In another family, Adam is a human. Rachel is a human. Pebbles is a cat. The pet of this family is*
    
    Mary is a human. Fido is a dog. The pet of this family is Fido. Rachel is a human. Pebbles is a cat. The pet of this family is
    
    This is a different task than “an neuron” because the output is not always “a” or “an”, but depends on the input (Mary, Fido, etc). This is more similar to the IOI task. Even “1 2 3 4” is more similar to the IOI task. This is where the analogy breaks down.
    

---

Because we decided to try number sequence inputs, we are looking for semantic patterns rather than specific tokens. The IOI experiments also looked for semantic patterns. Thus, we hypothesize the number seq experiments to also discover attention head circuits, rather discover neurons corresponding to tokens, as in the “An neuron” expms. We alter course to map this new task to [**Exploratory Analysis Demo**](https://www.notion.so/Exploratory-Analysis-Demo-c61288d8f11b45d993c796ec28a62132) instead.

number_seq_circuit_expms.ipynb:

[https://colab.research.google.com/drive/1LW2JYRnaL3ZqALK_calYdF9e5PP2U4gE#scrollTo=mnon1yrWOeMN](https://colab.research.google.com/drive/1LW2JYRnaL3ZqALK_calYdF9e5PP2U4gE#scrollTo=mnon1yrWOeMN)

1) Test prompts to look at top 10 tokens with highest logits

gpt-2-small does badly on “2 4”. The more info is given (eg. 3 tokens instead of 2), the better it can get a correct pattern.

2) Get logit diffs b/w correct and incorrect answer (s?)

- Debug this
    - input code
        
        ```python
        prompts = [
            "1 2 3 4",
        ]
        # List of answers, in the format (correct, incorrect)
        answers = [
            (" 5", " 4"),
        ]
        # answer_tokens: Convert answer strings to tokens (ints)
        answer_tokens = []
        for i in range(len(answers)):
            for j in range(2):
                answer_tokens.append(
                    (
                        model.to_single_token(answers[-1][0]),
                        model.to_single_token(answers[-1][1]),
                    )
                )
        answer_tokens = torch.tensor(answer_tokens).cuda()
        
        tokens = model.to_tokens(prompts, prepend_bos=True)
        tokens = tokens.cuda() # Move the tokens to the GPU
        original_logits, cache = model.run_with_cache(tokens) # Run the model and cache all activations
        
        def logits_to_ave_logit_diff(logits, answer_tokens, per_prompt=False):
            # Only the final logits are relevant for the answer
            final_logits = logits[:, -1, :]
            answer_logits = final_logits.gather(dim=-1, index=answer_tokens)
            answer_logit_diff = answer_logits[:, 0] - answer_logits[:, 1]
            if per_prompt:
                return answer_logit_diff
            else:
                return answer_logit_diff.mean()
        
        print("Per prompt logit difference:", logits_to_ave_logit_diff(original_logits, answer_tokens, per_prompt=True))
        original_average_logit_diff = logits_to_ave_logit_diff(original_logits, answer_tokens)
        print("Average logit difference:", logits_to_ave_logit_diff(original_logits, answer_tokens).item())
        ```
        
    
    SOLN: There is an issue with the `answer_tokens` list construction. The `i` index of the loop is not used, and instead, the last element of the `answers` list is used twice. This means that `answer_tokens` will contain duplicate entries.
    
    Here is the corrected code for constructing `answer_tokens`:
    
    ```
    # answer_tokens: Convert answer strings to tokens (ints)
    answer_tokens = []
    for answer in answers:
        correct_token = model.to_single_token(answer[0])
        incorrect_token = model.to_single_token(answer[1])
        answer_tokens.append((correct_token, incorrect_token))
    answer_tokens = torch.tensor(answer_tokens).cuda()
    
    ```
    
    This code creates a tuple of the correct and incorrect tokens for each answer in the `answers` list and adds it to the `answer_tokens` list.
    
    With this correction, the code should run without issues.
    
    ---
    
    The reason the loop code is wrong is b/c the original in Expl An had a combination of every prompt with every name (hence the double loop). Here, we are not creating such combinations, but merely directly getting answer tokens for every answer.
    

The previous expms had one very likely incorrect answer, which could rise to the top rank if the prompt is “corrupted”. Do we have the same thing here (or does the analogy break down and we have to modify the procedure)?

3) Look at the logit lens (contribution of each accumulated residual stream to the logit diff)

This graph changes based on what is considered the “incorrect token”. You need something defined as the incorrect token to get logit diffs.

gpt-2-small gives a linear logit lens graph. Try gpt-2-large instead.

- 4) Redo previous steps on gpt-2-large
    
    The model still doesn’t do well on inputs like “2 4 6”
    
    Try a different type of input: Mary is a human. Fido is a dog. The pet of this family is Fido. Pebbles is a cat. Rachel is a human. The pet of this family is
    
    If we change the order, it doesn’t predict “Peb”, but Rachel, by 74% prob. So it’s not looking at semantics, but order. Why?
    
    Try changing Mary and John in IOI
    
    4.1) Debug why "an neuron" and "IOI" logit lens plots have diff shapes
    
- 5) Attention head on gpt-2-large
    - TypeError: plotly.express._imshow.imshow() got multiple values for keyword argument 'labels’
        
        The error message you're seeing indicates that there's a problem with the arguments you're passing to the `imshow` function. Specifically, it looks like you're passing the `labels` argument more than once.
        
        Looking at the code, it appears that you're passing `labels` as a dictionary of axis labels to the `imshow` function, which is correct. However, the error message suggests that there might be another `labels` argument being passed somewhere else in the code.
        
        One possible explanation for this error is that the `imshow` function you're using is actually a wrapper around the Plotly `imshow` function, and that the wrapper function is passing an extra `labels` argument to the underlying `imshow` function.
        
        To fix this error, you can try removing the `labels` argument from the `imshow` function call and instead pass it directly to the underlying `imshow` function using the `imshow_kwargs` argument. Here's an example of how to do this:
        
        ```
        import plotly.express as px
        
        # ...
        
        per_head_logit_diffs = einops.rearrange(per_head_logit_diffs, "(layer head_index) -> layer head_index", layer=model.cfg.n_layers, head_index=model.cfg.n_heads)
        fig = px.imshow(per_head_logit_diffs, color_continuous_scale='RdBu_r', title="Logit Difference From Each Head", x=['Head'], y=['Layer'], imshow_kwargs={'labels': {'x': 'Head', 'y': 'Layer'}})
        fig.show()
        
        ```
        
        In this code, we use `px.imshow` instead of `imshow` to create the plot. We pass `per_head_logit_diffs` as the data, and use `color_continuous_scale` to specify the color scheme for the plot.
        
        We also pass the `title` argument directly to `px.imshow`, and use `imshow_kwargs` to pass the `labels` argument as a dictionary to the underlying `imshow` function. This should prevent any conflicts with other `labels` arguments that might be present in the code.
        
        SOLN:
        
        `imshow(per_head_logit_diffs, title="Logit Difference From Each Head")`
        
    
    Inspecting the setup, it seems the code is slightly different from that of "exploratory analysis demo". It came from "Main Demo (TransformerLens)" b/c that's where the original code to get attn patterns was from.
    
    To preserve the debugging history of this notebook, make a copy of this notebook and replace the setup with the "EA demo". Then redo the expms, starting from gpt-2 small (since the reason we switched to -large was b/c the logit lens plot was y=2x)
    

6) New notebook with right setup code

[simple_analogies_circuits.ipynb](../../../Code%20Notebooks%20432b45bb746f43eabf4172f69d384f8a/simple_analogies_circuits%20ipynb%20766fb391cad246da9150bcd5d98248a4.md) 

[https://colab.research.google.com/drive/1mhcgx2SU3GrDq3pMZp_-JPtE_fO-7kGg](https://colab.research.google.com/drive/1mhcgx2SU3GrDq3pMZp_-JPtE_fO-7kGg)

The logit lens plot for -small is now not y=2x

- 7) Attention analysis on analogous input “The pet is…”
    
    Found very little attending to previous tokens.
    
    One thing to keep in mind when looking at attending is that it’s ACCUMULATIVE. It’s not just say “this”, alone, attends to“family”. It means all prev tokens in the input, “Mary is … Rachel. The pet of this”, ALL attend to “family”.
    
    - check with chatgpt
        
        Yes, that is generally true about attention in transformers.
        
        When we talk about attention in transformers, we usually mean multi-head attention, which is a mechanism that allows the model to selectively attend to different parts of the input sequence when generating an output. In multi-head attention, the input sequence is first transformed into three vectors: the query vector, the key vector, and the value vector.
        
        The query vector is used to compute a similarity score between each position in the input sequence and every other position, based on the dot product of the query vector and the key vector at each position. The similarity scores are then used to compute a weighted sum of the value vectors at each position, where the weights are given by a softmax function applied to the similarity scores.
        
        The resulting weighted sum is the attended representation of the input sequence at the current position. This attended representation is then used as input to the next layer of the transformer.
        
        Importantly, the attention mechanism is accumulative in the sense that each position in the input sequence contributes to the attended representation of every other position. That is, when computing the similarity scores between the query vector and the key vectors at each position, the contribution of each position is weighted by its relevance to the query vector, as determined by the dot product. Therefore, even if the query vector corresponds to a single word in the input sequence, the attended representation of that word will be influenced by the context in which it appears, because the context will affect the relevance weights assigned to the other words in the sequence.
        
        So, to answer your question: yes, when we say that "the pet of this attends to family", we mean that the attended representation of "the pet of this" takes into account the context of "family" in the input sequence, because the attention mechanism is accumulative and considers all positions in the sequence when computing the weights for the weighted sum.
        
    
    This is the power of the residual stream.
    
    Thus, “this” as a token doesn’t always attend to certain tokens, as it depends on the previous tokens that give it context.
    
    Pet has no attention to dog or cat. This is gpt-small but shouldn’t that be a basic association it learns from its training data? What was its training data?
    
    Try this for -large
    
- 8) Let’s move on to activation patching.
    
    The corruption in our new case is swapping the order of the Pebbles and Rachel sentences. 
    
    Actually, no- that’s not how corruption was used. In the previous cases, the corruption is meant to give a different output. This swapping of sentence order corruption gives the SAME output, but it’s the wrong output for that swapped-order output. 
    
    Thus, to keep the analogy intact, we should find a corruption that gives a DIFFERENT output, then use causal tracing to restore the original output. IT doesn’t matter what’s wrong or right- we just need to find that part of the model whose activations give that specific original output. We can perform this corruption either by noise (mean ablation; note zero ablation causes too much output wreckage), or by using a different sentence meant to give a different output. 
    
    For example, make it so the output becomes Rachel instead of Pebbles.
    
    "The human is Mary. The dog is Fido. The pet is Fido. The dog is Pebbles. The human is Rachel. The pet is”
    
    "The human is Mary. The dog is Fido. The pet is Fido. The dog is Rachel. The human is Pebbles. The pet is” (Corrupt by switching words)
    
    But does this really associate the pattern? It seems to associate the specific word
    
    This is a bad input b/c "Rachel is a cat. Pebbles is a human. The pet of this family is" yields Pebbles as the top result even though it should be Rachel.
    
    **What was original vs corrupted, and answer tokens, in expl analysis demo (that this is based on)?**
    
    Go back to domain of analogy (explr analysis) and think about why its corruption choice worked for its case.
    
    logits_to_ave_logit_diff() gets the logits for the specified answer tokens, then subtracts first ind and second ind of answer token tuple. So corrupted should be negative because it should have the second ind be higher than first, regardless of what second is.
    
    Thus, corrupted input’s result just has to place second ind answer_token[i][1] higher than first ind answer_token[i][0]; exact ranking doesn't matter. 
    
    This will cause corrupted logit diff to be neg, while clean is pos
    
    Test prompt the corrupted’s logit rankings before using it in actv patching
    
    For now, it also doesn’t matter how you corrupt it as long as this goal is achieved (later we will refine it; eg. zero ablation is too drastic)
    

9) Try corrupting number or other sequences that don’t involve too much external knowledge about its token’s traits (eg. knowing a dog or cat is usually the pet). 

1 2 3 4 → 1 2 3 5 ; answer_token = (5, 6)

ALL the layers outputting to residual stream attend highly to the last token. That's obvious because the last token was the one that was changed. This is such a short sequence that we don't expect early sites like in the more elaborate sentences.

The activation patches we obtain for this aren’t that interesting. Try going back to simple analogous inputs, which are more similar to IOI (due to requiring to identify subjects, inhibit certain subjects, identify syntax/grammar, etc), as sequences may SEEM to be simpler but they also seem to be too different from IOI. We want a task which may involve similar heads + circuits as IOI.