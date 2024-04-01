# Initial Exploration

As stated in the IOI interview, finding the prompt is difficult, so expect to spend some time (1-2) weeks on this before choosing a more concrete research topic with evidence that it’s feasible

---

### Working on

N/A

### DONE

**Choosing a research topic (input pattern’s circuits to study)**

- Choose an initial goal and assess its implementation feasibility relative to prev work
    - **MAIN AIM:** Find similarities in circuits of analogous inputs (the common patterns between any items). Compare runs w/ abstraction and specifics.
    - Freeform brainstorm about initial goal
        
        analogy expms: use analogous "pattern" as input and see which attn heads attnend to certain query-> key relations.
        Eg) ordering of yoda, car vs lion vs horse collections
        
        What analogies can GPT-2-xl make? Are there heads whose role is to recognize the analogy?
        
        Star Wars vs Zelda vs Mario: Luke is MC. Link is MC. Leia is Princess. Zelda is Princess. Mario and princess peach.
        
        Can it write a story based on this simple structure?
        
        Which component (head, MLP, neuron, etc) of stream contains the “mammal” class? Is it built up in a “memory” subset of the stream?
        
        Attention heads: move information by matching patterns
        
        Types: duplicate, induction, inhibition, backup, translation
        
        MLP: store facts, “make information more semantic (?)”
        
- Test what GPT2 is capable of outputting
    
    First, define “analogous inputs”. Instead of complex analogies (defined using structure preserving maps, or graph homomorphisms), start simple by just seeing if the model can output a “next item” based on the common patterns from previous items. Now test both small and -xl:
    
    [test_gpt2.ipynb](https://colab.research.google.com/drive/1-pUjv-gdcdClslXRI5eFBs8KM8pN8pjD)
    
    This shows gpt-small isn’t good at predicting correct outputs that involve “identifying common patterns”. For instance:
    
    - **Super vs Subclasses**
        
        GPT2-small fails at identifying mammals most of the time (it includes “sea lizards”)
        
        GPT2-xl is able to identify mammals
        
        What is “common to” mammals? — this task is not about sentence structure
        
    
    For other sentence completion, see if GPT2-xl can correctly identify the analogy.
    
    Try more complex paragraphs:
    
    In a family: John is a human. Mary is a human. Fido is a dog. The pet of this family is Fido. In another family, Adam is a human. Rachel is a human. Pebbles is a cat. The pet of this family is
    
    This correctly says “Pebbles” in all 3 outputs
    
    Try changing the order to see if it's making the analogy based on semantics, rather than only on order:
    
    In a family: John is a human. Mary is a human. Fido is a dog. The pet of this family is Fido. In another family, Adam is a human. Pebbles is a cat. Rachel is a human. The pet of this family is
    
    This is incorrect now; it says Rachel in all 3 outputs!
    
    Thus, find the circuit which algorithmically identifies this “ordering” pattern. Later, compare it to a model that correctly idenfities the semantics, and see what’s missing [postponed]
    
    ---
    
- QUES: GPT-2 small doesn’t always output “mary” for "When Mary and John went to the store, John gave a drink to” ?
    
    [https://colab.research.google.com/drive/1-pUjv-gdcdClslXRI5eFBs8KM8pN8pjD#scrollTo=rWTyNUm5wj0U&line=1&uniqifier=1](https://colab.research.google.com/drive/1-pUjv-gdcdClslXRI5eFBs8KM8pN8pjD#scrollTo=rWTyNUm5wj0U&line=1&uniqifier=1)
    
    This colab block shows this issue
    
    V TRY: Read paper to see if they address this
    
    NOTE: Figure 8 and Appendix L discuss probability on multiple different inputs, not about the random outputs of one input
    
    V TRY 2: get 100 outputs and get the % times answer is correct
    
    Around 50% of the time
    
    SOLN: [[link](https://www.notion.so/GPT-mechanisms-108c635e0f0849ac8e556c91c892dec2?pvs=21)]
    
    - GPT chooses, by a form of sampling, a random next token from the top-k highest probabilities instead of just the token with the highest probability. However, when we analyze what’s predicted, we don’t look at what’s actually chosen, but just the token with the highest probability. The calculation of these probabilities (and before softmax, the logits) is deterministic.
- Revise initial goal due to feasibility issues
    
    GPT-2 is not great at completing analogies. Also, some analogous inputs often require long sentences (to establish the pattern such as “a hero’s journey”). So try a simpler goal first, then re-visit this once you are more familiar with the techniques.
    
    - **NEW AIM:** Modify experiments that involve investigating circuits associated with input patterns, but use a different input pattern
    - Brainstorm simple syntax patterns other than IOI. Ask ChatGPT too
        
        [https://www.grammarly.com/grammar](https://www.grammarly.com/grammar)
        
        ---
        
        Indirect object identification aims to see if a model can, Given the sentence:
        “When Mary and John went to the store, John gave a drink to”,
        of the two names in the sentence, predict the name that isn’t the subject of the last clause. So it should be completed with “Mary”.
        Brainstorm other simple linguistic tasks
        
        1. Part of speech tagging: Identifying the part of speech (noun, verb, adjective, etc.) of each word in a sentence.
        2. Named entity recognition: Identifying named entities such as people, places, organizations, and dates in a sentence.
        3. Sentiment analysis: Determining the sentiment (positive, negative, or neutral) expressed in a sentence.
        4. Text classification: Classifying a text into predefined categories such as spam or non-spam, news or sports articles, etc.
        5. Language identification: Identifying the language in which a text is written.
        6. Question answering: Answering questions based on a given text.
        7. Machine translation: Translating a text from one language to another.
        8. Text summarization: Summarizing a long text into a shorter version.
        9. Pronoun resolution: Identifying the antecedent of a pronoun in a sentence.
        10. Coreference resolution: Identifying all the words in a sentence that refer to the same entity.
    - Other tasks based on sentence structure
        
        Indirect object identification aims to see if a model can, Given the sentence:
        “When Mary and John went to the store, John gave a drink to”,
        of the two names in the sentence, predict the name that isn’t the subject of the last clause. So it should be completed with “Mary”.
        Brainstorm other simple linguistic tasks based on sentence input structure
        
        1. Subject-verb agreement: Given a sentence, identify if the subject and verb agree in number (singular or plural).
        
        Example: The cat jumps over the fence. (Subject and verb agree in number)
        
        1. Identifying parts of speech: Given a sentence, identify the parts of speech for each word in the sentence.
        
        Example: The quick brown fox jumps over the lazy dog. (The - determiner, quick - adjective, brown - adjective, fox - noun, jumps - verb, over - preposition, the - determiner, lazy - adjective, dog - noun)
        
        1. Identifying the main verb: Given a sentence, identify the main verb that conveys the main action or state of being.
        
        Example: She is singing a song. (The main verb is "singing")
        
        1. Identifying the subject of a sentence: Given a sentence, identify the noun or pronoun that is performing the action or being described in the sentence.
        
        Example: The dog chased the cat. (The subject is "dog")
        
        1. Identifying the direct object: Given a sentence, identify the noun or pronoun that is receiving the action of the verb.
        
        Example: The teacher gave the students homework. (The direct object is "homework")
        
    - For simpler input ideas, see [“An” neuron](https://www.notion.so/An-neuron-92888cb0c37548b7949c1d9c3c9d260d?pvs=21)
        - We choose this workflow b/c the input is VERY simple and the “how it was done” part of the project is well-documented and short
        - Thus, try a NEW simpler output using “An neuron” experiments workflow

[Test feasibility of simpler inputs by mapping to previous workflows](Initial%20Exploration%2006eb3b02c5684ef88cb6f64881f8a44f/Test%20feasibility%20of%20simpler%20inputs%20by%20mapping%20to%20p%20e13b76d3448c42af8d8b2e5b7a1858ba.md)

- Revise goal to be more similar to initial goal, but with better defined conditions
    
    Thus, instead of finding simple inputs other than analogies, we are deciding now to go back to the initial goal of the project (examining simple analogies). This time, we re-frame it so the analogy input conditions are better defined:
    
    - There is a source description and a target description. The aim is to predict a target word that analogously fits the pattern given by the source.
        - “analogous” is defined more formally using structure preservation: If A→ B, then h(A) →h(B). This is similar to the definition of graph homomorphism.
    - Most of the information should be given to the input, so the model doesn’t rely that much on external information. We should check how much external info (not from input, but from its learned knowledge) it uses.
    
    This is similar to giving examples to chatGPT so it can generalize these input examples to make new ones. We will see to what extent less powerful models can do this.
    

[Brainstorm analogy order vs IOI tasks](Initial%20Exploration%2006eb3b02c5684ef88cb6f64881f8a44f/Brainstorm%20analogy%20order%20vs%20IOI%20tasks%208977518d2819431a97dd743c23b94810.md)

- Analyze projects from [https://apartresearch.com/jam](https://apartresearch.com/jam)
    
    **Find feature neurons:**
    
    [https://clementneo.itch.io/we-discovered-an-neuron](https://clementneo.itch.io/we-discovered-an-neuron)
    
    uses both actv patching + neuroscope. not automated yet.
    
    [https://www.alignmentforum.org/posts/btasQF7wiCYPsr5qw/200-cop-in-mi-techniques-tooling-and-automation](https://www.alignmentforum.org/posts/btasQF7wiCYPsr5qw/200-cop-in-mi-techniques-tooling-and-automation)
    
    [https://alexfoote.itch.io/investigating-neuron-behaviour-via-dataset-example-pruning-and-local-search](https://alexfoote.itch.io/investigating-neuron-behaviour-via-dataset-example-pruning-and-local-search)
    
    [https://lomichelle42.itch.io/automated-identification-of-potential-feature-neurons](https://lomichelle42.itch.io/automated-identification-of-potential-feature-neurons)
    
    last two just used neuroscope perturbations
    
    **Circuits:**
    
    [https://satojk.itch.io/backup-transformer-heads-are-robust](https://satojk.itch.io/backup-transformer-heads-are-robust)
    
    [https://cmathw.itch.io/identifying-a-preliminary-circuit-for-predicting-gendered-pronouns-in-gpt-2-smal](https://cmathw.itch.io/identifying-a-preliminary-circuit-for-predicting-gendered-pronouns-in-gpt-2-smal)
    
    [Automated Circuit Discovery](https://www.notion.so/Automated-Circuit-Discovery-78c36eb7aa084d7db89fa74016e83d3e?pvs=21) 
    
    Towards Automated Circuit Discovery for Mechanistic Interpretability + hackathon posts
    
    WHY did those analyses work? copy code and interpret results
    
    Try to run ACDC on trial inputs
    
    **Model editing:**
    
    [https://jas-ho.itch.io/model-editing-hazards-at-the-example-of-rome](https://jas-ho.itch.io/model-editing-hazards-at-the-example-of-rome)
    

[Tall Short Neuron Exploration](Initial%20Exploration%2006eb3b02c5684ef88cb6f64881f8a44f/Tall%20Short%20Neuron%20Exploration%20f68842d97ef64f3cabbc2ffad0d9e06f.md)

- NEW GOAL: Just find evidence those heads change output values for those tokens, and affect those other heads (via circuit connections). That’s it; that’s the finish line for this.
    - Summary
        
        Test prompts: (table)
        
        - Mary has X. John has Y. Z is. → John (failure on all models)
        
        Write up in Expms: We already found, by attn head patterns, the heads for 
        
        - “[subject] is X. The pet is”
        - “John is Tall. Mary is”
        
        [ TBC ]
        
- **SELECTED RESEARCH TOPIC**: “Comparison” circuits for sizes, opposites, and more. Further explore where name movers are found (see if there also exists adjective and verb movers)
    - Rename project from “Interpret Attention Head Circuits of Analogous Inputs” to “Interpret Attention Head Circuits of Comparison Inputs”

TO DO NEXT: **Conduct Experiments on Research Topic**

(copy+paste relevant ones from exploration before)

### (Potential) Future Work

- Create a table comparing initial findings of simple analogies
- Look at attention patterns of analogous inputs.
    
    Hypothesis: Analogous inputs have similar attention patterns. Eg) Zelda should attend to Link in a similar way that Peach attends to Mario.
    
    [https://colab.research.google.com/drive/1nD6tfM33StbAqXG5HnYPlC40hKSj8mzD#scrollTo=1p2zyJ_6IAif](https://colab.research.google.com/drive/1nD6tfM33StbAqXG5HnYPlC40hKSj8mzD#scrollTo=1p2zyJ_6IAif)
    
    see “Direct logit attr- Attention Analysis” and “**Visualizing Attention Patterns”**
    
    [https://colab.research.google.com/drive/1Jte9lTR05cfwToO-OyoP83R7o2qNQ1UJ#scrollTo=HouujxF94YvN](https://colab.research.google.com/drive/1Jte9lTR05cfwToO-OyoP83R7o2qNQ1UJ#scrollTo=HouujxF94YvN)
    
    see “**Caching all Activations”**
    
    modify TransformerLens demo:
    
    [https://colab.research.google.com/drive/1Syd-StXzmpMuJ-Hqfw692lzJyX7MOszX](https://colab.research.google.com/drive/1Syd-StXzmpMuJ-Hqfw692lzJyX7MOszX)
    
    Get attention patterns for:
    
    John is a human. Mary is a human. Fido is a dog. The pet of this family is Fido. In another family, Adam is a human. Rachel is a human. Pebbles is a cat. The pet of this family is
    
    VS
    
    John is a human. Mary is a human. Fido is a dog. The pet of this family is Fido. In another family, Adam is a human. Pebbles is a cat. Rachel is a human. The pet of this family is
    
    How to compare the 2 patterns?
    
    Activation patching (see TransformerLens: **Hooks: Intervening on Activations)**
    
    Hypothesis: patching certain heads will lead to decrease in logit of correct answer. For this input, the correct answer is “Pebbles”.
    
    Try even simpler inputs
    
    what to do after getting attention pattern?
    attn pattern says which word attends to which prev word. to find this by calculation, compare logit diffs. how? see explor analysis 'direct logit attr'
    
    How to compare logit diffs:
    
    1. code that calculates the logit difference directions by subtracting the residual direction corresponding to the incorrect answer from the residual direction corresponding to the correct answer. 
        - logit_diff_directions = answer_residual_directions[:, 0] - answer_residual_directions[:, 1]
    2. 
    
- Causal patch to look for it (map from previous code)
    
    [https://colab.research.google.com/drive/1nD6tfM33StbAqXG5HnYPlC40hKSj8mzD#scrollTo=xJXsNJMMIAiV](https://colab.research.google.com/drive/1nD6tfM33StbAqXG5HnYPlC40hKSj8mzD#scrollTo=xJXsNJMMIAiV)
    
    [https://colab.research.google.com/drive/1Jte9lTR05cfwToO-OyoP83R7o2qNQ1UJ#scrollTo=HouujxF94YvN](https://colab.research.google.com/drive/1Jte9lTR05cfwToO-OyoP83R7o2qNQ1UJ#scrollTo=HouujxF94YvN)
    
    Modify “exploratory analysis” logit differences
    
    Mod “transformerlens demo” attention patterns
    
    attention patterns for transformerlens demo uses cv.attention.attention_patterns()
    
    in the demo, looks at layer 0
    
    for exploratory analysis uses visualize_attention_patterns(), written in pysvelte
    
    this splits attention heads into types and ranks (eg. top 3 name movers). in this nb, looks at layers 9 and 10
    
    No_Position_Experiment uses imshow and numpy
    
- Map from [Main Demo notebook (TransformerLens)](https://www.notion.so/Main-Demo-notebook-TransformerLens-daaafedc55154a56b549f832a01b119a?pvs=21)
    
    ### Introduction
    
    HOOKS:
    
    def head_ablation_hook() : returns losses after ablating head in a layer
    
    Old: ablate each head
    
    New: ablate each head and run analogous inputs through
    
    ACTIVATION PATCHING:
    
    Finds the (token, layer) that is important for correct output
    
    New: Finds the (token, layer) that is important for correct pattern
    
    What layer is associated with the pattern?
    
    Eg) Both “pig” and “cow” have common associations of ‘farm, mammal, etc’. 
    
    [ TBC ]
    
- Understand more indepth how attention heads in IOI algorithmically work together to identify the indirect object to be outputted
- Alter superclass and see effect on subclass
- What allows gpt-xl to correctly make analogies based on previous ordering patterns in a prompt?
    
    Try more complex paragraphs:
    
    In a family: John is a human. Mary is a human. Fido is a dog. The pet of this family is Fido. In another family, Adam is a human. Rachel is a human. Pebbles is a cat. The pet of this family is
    
    This correctly says “Pebbles” in all 3 outputs
    
    Try changing the order to see if it's making the analogy based on semantics, rather than only on order:
    
    In a family: John is a human. Mary is a human. Fido is a dog. The pet of this family is Fido. In another family, Adam is a human. Pebbles is a cat. Rachel is a human. The pet of this family is
    
    This is incorrect now; it says Rachel in all 3 outputs!
    
    Thus, find the circuit which algorithmically identifies this “ordering” pattern. Later, compare it to a model that correctly idenfities the semantics, and see what’s missing
    

[Map old experiments code to new task](Initial%20Exploration%2006eb3b02c5684ef88cb6f64881f8a44f/Map%20old%20experiments%20code%20to%20new%20task%20f7794839baeb489c9d976ac663df947d.md)