# Analogous Steering Expms

Analogous Structures within SAE or LLM

- 🐣 Brainstorm overall
    - Do similar languages have similar structures?
        - We can use our similarity metrics to test this within a model for two languages
            - Eg) pair uno with one, cato with cat, etc.
                - we’d have to use single tokens
                - just measure by svcca, so don’t require many samples like for jaccard
                - we can use automated pairing
            - rather than just months-days, we can also do
            - this is not necessarily hierarchical as we don’t need the abstract clustering to have some abstract cluster of which months and days both belongs to, but rather, organize things in similar way in different spaces
            - ISSUE: it’s hard to do this for specific features, as it’s not just “one” feature that corresponds to animal, but a cluster. We can take an LDA estimatation of that cluster, or perhaps the mean of that cluster.
        - Then we can test this across models (this is like memes understandable)
            - do different models organize their language concepts in similar way?
- 🐣 Brainstorm expm setup
    - first test on months/numbers/days within GPT-2
        - ISSUE: cannot use nearest neighbors bc too few samples. Try SVCCA or RSA.
        - Pherpas mix in more samples that are non-numbers, but are correctly paired with others. Or use numbers and months all in same.
    - test on Llama-3 SAEs. Ensure it knows different languages
- ✅ Outline expm steps and carry out prelims
- ✅ gpt2 numbers vs months vs Spanish numbers
    
    reprSim_gpt2_nums_months.ipynb
    
    1. load GPT SAE with feature labels
        1. Layer: try resid jb 7 (this is pre 8). if not, try nearby layers, or MLPs.
            1. Based on “not all features are linear” Fig 1
            2. use neuronpedia tutorial
        2. use neuonpedia’s labels, ‘download explanations’ on homepage
    2. find number (etc) features 
        1. [use `jaccard_subset_ts_GPT2_v3.ipynb` : `search modB features with keyword, get modA f pair` ]
        2. first test by searching for “one”
        3. ISSUE: the explanations are general explanations, not highest activating keywords
            1. we can try searching features of “numbers” first, then use the narrowed subset to find which ones are specific for “one”, etc.
            2. NOTE: it is a cluster of features which when ablated, correspond to those concepts (Jan, etc). However, we’ll see if we can also just find many features which actviate for “one” 
                1. activate just for “one” and not others?
        4. try putting in inputs directly, then get actvs of features
            1. fn to get highest actv features. [code](https://colab.research.google.com/drive/1iS1--NuqtBWmU02Qm9C76DglMw4z_hLX#scrollTo=JW5nPgf__4oS&line=5&uniqifier=1)
            2. get gpt2 sae actvs: pretrained_SAE_save_actvs.ipynb
            3. tokenize data: [code](https://colab.research.google.com/drive/1Sfq8SceWuQOMrKi92drfPbgzsiARPG7m#scrollTo=TAPKX8PFH4dj)
        5. get corr of feature weight subsets for those that activate on number vs months
            1. issue- how to pair them?
            2. then match them by activations
            3. ALT: don’t get subset, but match by top corrs
        6. pass just one input in at a time, and check feature overlap
            1. nonzero inds (feat weights) of feature actvs
            2. doesn’t work; many single tokens seem to always activate the same 20 tokens!
                1. it’s the EXACT SAME features with activations over 100!
                    1. even stranger, it’s the EXACT SAME VALUE???
                2. are they position detection- won’t activate for tokens in second pos?
                    1. no; it’s the same thing even when using longer prompts like “My favorite animal is” and “one two three four”!
                    2. how does it even tell anything apart then???
                3. try sequences instead
            3. see if this happens in the LLM. what are the top neurons in the LLMs? they can’t be the same?
                1. obv, every LLM neuron would actv, so nonzero is bogus. 
                2. only neurons for tokens in first pos actv over 100, and same ones
                3. look at the top actv neurons, or those in top 10%.
                4. however, for LLM, neurons are different. all the top 15 are from a glance
            4. SOLN: the top 15 SAE features for the LAST token are also different. this means we shouldn’t just pass in one token through the model; we need to pass in multiple and see the last one for what’s predicted.
                1. Now one and Jan seqcont do have features in common: 
                    1. [https://www.neuronpedia.org/gpt2-small/8-res-jb/636](https://www.neuronpedia.org/gpt2-small/8-res-jb/636)
                    2. [https://www.neuronpedia.org/gpt2-small/8-res-jb/11702](https://www.neuronpedia.org/gpt2-small/8-res-jb/11702)
                    3. [https://www.neuronpedia.org/gpt2-small/8-res-jb/22220](https://www.neuronpedia.org/gpt2-small/8-res-jb/22220)
                2. thus, don’t flatten. only take features from last token, bc the top tokens which include first token are always the same. it IS single token that is an issue.
                    1. `one_top_acts_values, one_top_acts_indices = one_reshaped_activations.topk(feat_k, dim=-1)` will get top features for all the four. but we only care about `one_top_acts_indices[-1, :].` so actually we can just use `one_reshaped_activations[-1,:]` or `one_feature_acts[0, -1, :]`
            5. so if this is the case for sequences, perhaps other similar prompts have features in common? if so, are these impt “abstractions”, while others are more specific?
                1. pass in batches and find the top features they activate on
                2. perhaps can also do this for sequence steering
                3. what if we steer by the common abstraction features?
            6. try “John is big. Mary is” and “…tall..”
                1. [relationships](https://www.neuronpedia.org/gpt2-small/8-res-jb/600)
                2. [compare entities](https://www.neuronpedia.org/gpt2-small/8-res-jb/5903)
                3. [co-occuring words](https://www.neuronpedia.org/gpt2-small/8-res-jb/8399)
                4. [names](https://www.neuronpedia.org/gpt2-small/8-res-jb/22806)
                5. [but none of them are about sizes](https://colab.research.google.com/drive/1HNfItvWhMEWyAWYPPrG6oysLHHKCrlIq#scrollTo=yZCyqPxHXPzG&line=2&uniqifier=1)
            7. note: these features are different than the ones for “size” in neuronpedia
            8. is 600 also in IOI’s “John gave the ball to Mary”?
            9. gpt-2 is really bad at predicting, so we have to move onto a bigger model.
- ✅ try gemma2-2b; gemmascope is for gemma2
    
    reprSim_gemma2_nums_months.ipynb
    
    - [https://deepmind.google/discover/blog/gemma-scope-helping-the-safety-community-shed-light-on-the-inner-workings-of-language-models/](https://deepmind.google/discover/blog/gemma-scope-helping-the-safety-community-shed-light-on-the-inner-workings-of-language-models/)
    - first look for sequential featuers of nums vs months
        - [https://www.neuronpedia.org/gemma-2-2b/20-gemmascope-res-16k/2269](https://www.neuronpedia.org/gemma-2-2b/20-gemmascope-res-16k/2269)
    - it can do spanish, so try that
        - They ALSO have common features related to sequences: [https://colab.research.google.com/drive/1y8DPsPIp99sjGesDm7SP0kqcjarROz6M#scrollTo=c326U4xAjLV4&line=1&uniqifier=1](https://colab.research.google.com/drive/1y8DPsPIp99sjGesDm7SP0kqcjarROz6M#scrollTo=c326U4xAjLV4&line=1&uniqifier=1)
    - ✅ see if the features that don’t have in common with english are related to spanish
        - for top 15, they don’t: [https://colab.research.google.com/drive/1y8DPsPIp99sjGesDm7SP0kqcjarROz6M#scrollTo=OnipbcoJqE5p&line=1&uniqifier=1](https://colab.research.google.com/drive/1y8DPsPIp99sjGesDm7SP0kqcjarROz6M#scrollTo=OnipbcoJqE5p&line=1&uniqifier=1)
        - even top 100 doesn’t
    - ✅ now try numbers vs months
        - only do top 50 bc the rest are 0 (this uses jumprelu not top k)
        - yes, there are differing features that activate for months vs numbers
            - months are calendar/date related
            - numbers seem to be numbers in general not about structured data, like sentiment or shapes
            - but they have features in common that are about structured data
    - ✅ plot top 50 eng vs month features to see if they form different spaces in same UMAP, except for common ones
        - fix umap labeling issue
            - [https://stackoverflow.com/questions/72658105/show-legend-on-umap-plot](https://stackoverflow.com/questions/72658105/show-legend-on-umap-plot)
            - SOLN: use `hover_data` directly in `px.scatter` instead
        - plot fig
            
            ![image.png](Analogous%20Steering%20Expms%207fd323b8e3644ceeb8f6477da6eace78/image.png)
            
        - analyze
            - main takeaway: the common activating features are also associated with spatial (geometric) commonality patterns and semantic commonality patterns
                - previously, it was not shown that similar prompts would have “common abstraction” features; the UMAP only showed semantically similar features were close together
                - now, we show that these similar prompts may have a “common abstraction”
            - are the green (actv on both) the “common abstraction”?
            - is this common abstraction found in feature splitting in smaller SAEs?
                - are they less distinct?
            - is an analogue of the common abstraction found across models?
                - we needed to first find a new sae structure within a model, before finding it across models
                - compare gemma 1 and gemma 2 OR gemma2-2b with gemma2-9b
                - only use sim metric on the subset only, not on entire space (which is likely dissimilar)
                    - instead of random piarings within space, use random subsets
    - NOTE: an issue with the sim metrics is that it requires matching by same token. so we need to claim one and January are aligned, and see which features activate highly on One/Jan, etc.
        - The issue with this is that there are COMMON features that align with each other, making them not “analogous”. It doesn’t make sense to use that sim metric.
        - so we need two which have no features in common. let’s not use sim metric for now
    - NOET: order of loading model and running prompts before using `gather_residual_activations` and before laoding SAE matters somehow; if out of order, get inputs incompat with model.forward
        - SOLN: `sae.cuda()` must be used!
    - what if we ablate/steer the month only features- can we turn them to numbers? instead of predicting May, we predict 5?
        - we only ablate those specific to months, leaving the common features behind. but we don’t activate the number features
        - what if we do this for every layer?
        - what if we ablate the common abstraction?
    - ISSUE with ablate then gen: we use gather_activations on the unablated model, but we should generate after ablation?
    - instead of ablating, just steer months only (increase or patch in specific activations, such as avg actvs from months) to try to change numbers into months
        - try subtracting to get an “activation vector”, then add to new prompt: [https://colab.research.google.com/drive/1y8DPsPIp99sjGesDm7SP0kqcjarROz6M#scrollTo=EABPfVwZFUHP&line=9&uniqifier=1](https://colab.research.google.com/drive/1y8DPsPIp99sjGesDm7SP0kqcjarROz6M#scrollTo=EABPfVwZFUHP&line=9&uniqifier=1)
        - the actvs may be “memorizing” the actv, just like it memorized april as it changes it april when just doing `sae.decode(3*(sae_acts_2 - sae_acts_1))` for input `prompt = "a a a a"`
- 🐣 steering_gemma2_nums_months.ipynb.ipynb
    - use more data for nums vs months
        - umap plot (top 50)
            
            ![image.png](Analogous%20Steering%20Expms%207fd323b8e3644ceeb8f6477da6eace78/image%201.png)
            
        - unfortunately, when using all features from multiple prompts, we don’t see such clusters form
            - but perhaps it’s bc we use top 50, so that counts even small actvs as being in “both”
        - umap plot (top 15)
            
            ![image.png](Analogous%20Steering%20Expms%207fd323b8e3644ceeb8f6477da6eace78/image%202.png)
            
        - 🐣 instead of aggregating batches, what if we use plots for each indiv sample?
    - **fav vs least fav animal (single samp)**
        - no snake feature, just dog feature that activates for both! so not showing clear separation
    - i love V i hate
        
        umap sort of forms clusters
        
    - country capitals (using in-context learning)
        - no distinct “french” or “german”
            - perhaps try even more different / opposing countries
        - america v china DOES have dinstinct features. america has ‘washington’ features (and freedom) nd china has ‘asia’ feature (and its top is corruption)
            - there is an ‘asian’ cluster v ‘usa’ cluster, and though most are in common
            - may show bias? the asian foods cluster is closer to ‘iran’ and ‘corruption’
- ✅ [write up slides](https://docs.google.com/presentation/d/1xyA8SPdcm4TKfH-PaL7TyhsVFKQAGI1gd0eHBSJGeRU/edit#slide=id.g2f72843711f_0_138) for weekly meeting
    - David meeting: present “Univ by Topo, v2” and expm slides
    - before meeting: study on what stat test was used in RSA paper
        - One tail p value over null hyp of 10k rand pair distr
    - [https://huggingface.co/EleutherAI/sae-pythia-70m-32k](https://huggingface.co/EleutherAI/sae-pythia-70m-32k)
        - These SAEs were trained on the outputs of each of the MLPs in [**EleutherAI/pythia-70m**](https://huggingface.co/EleutherAI/pythia-70m).
    - simSAE_two_pythias_70m_160m_MLP2_v2.ipynb: L0 to L2 incl, plot less crowded
    - simLLMs_pythias_70m_160m_OWT_MLP2_v2.ipynb
    - simSAE_pythias_70m_160m_all_layers.ipynb
        - don’t re-use the rand scores for each diff 70m layer bc each compares diff SAE weight matrices
    - simLLM_pythias_70m_160m_all_layers.ipynb

[David K Meeting notes](Analogous%20Steering%20Expms%207fd323b8e3644ceeb8f6477da6eace78/David%20K%20Meeting%20notes%20c715d7931dda4c848f3e6eb29917c407.md)

- ✅ svcca VS procrustes
    - [does svcca measure the similarity of distances in two spaces? for instance, if we measure king-queen in one space, can it measure the similarity of king-queen in another space?](https://claude.ai/chat/faea580c-fa77-4e3a-a9db-c2eb9a8284f1)
    - [https://chatgpt.com/c/f7a87a50-b3c8-478c-a01b-f6e1ac9279cc](https://chatgpt.com/c/f7a87a50-b3c8-478c-a01b-f6e1ac9279cc) (all below use this)
    - try procrustes instead
    - what do you mean similarity of spaces? aren't spaces defined as distances spanned by points?
    - what do you mean correlated patterns? be specific and intuitive
        
        When we talk about "correlated patterns" in the context of analyzing neural networks using techniques like SVCCA, we're primarily focusing on the relationship between activation patterns across different layers or models. Here's a more specific and intuitive explanation:
        
        ### Understanding Activation Patterns
        
        In a neural network, an activation pattern refers to the responses (or outputs) of neurons in a layer when given a set of inputs. Each neuron in a layer responds differently based on its weights and biases, and together, the responses of all neurons in a layer form an "activation pattern." This pattern reflects how the layer is processing and interpreting the input data.
        
        ### Correlation Between Activation Patterns
        
        When comparing two layers, whether within the same network or across different networks, we examine the correlation between their activation patterns to see how similarly they process inputs. Here’s how this works:
        
        1. **Activation Responses**: Consider two layers from different models. When you pass the same input through both models, each layer will generate its own activation pattern.
        2. **Dimensionality Reduction**: With techniques like SVCCA, you often start by using Singular Value Decomposition (SVD) to simplify these activation patterns. This step reduces the complexity by focusing on the most significant features (directions) of the activation patterns, essentially compressing the data while preserving important information.
        3. **Canonical Correlation Analysis (CCA)**: After reduction, CCA is used to find the linear combinations of features from both layers that have the highest correlation. Here, correlation means how well the linear combinations of activation responses from one layer predict the linear combinations from the other layer. If these combinations are highly correlated, it implies that both layers are reacting similarly to the inputs, capturing similar features or patterns even though they may be part of different networks or configurations.
        
        ### Intuitive Example
        
        Imagine two photographers (representing two different neural network layers) taking pictures of the same scene (input data) but using different cameras (model architectures). Each photographer focuses on capturing certain features of the scene:
        
        - **Photographer 1** might focus more on color contrasts.
        - **Photographer 2** might focus on lighting and shadows.
        
        The photos (activation patterns) are then analyzed to see if there are common themes or focuses:
        
        - **Correlated Patterns**: If both photographers consistently emphasize the same aspects of the scenes despite their different techniques and tools, we might conclude that there is a correlation in their focus. This analogy parallels finding correlated patterns in activation responses of different neural network layers, suggesting they are capturing similar information from the input data.
        
        Thus, "correlated patterns" in neural networks are about finding these kinds of relationships—areas where different models or layers are effectively "seeing" or emphasizing the same features in the data, reflecting a similarity in how they process and interpret information. This similarity can help in understanding model behaviors and in transferring knowledge from one model to another.
        
    - so you’re measuring how well combinations of paired instances are correlated?
        
        Yes, exactly! In the context of methods like SVCCA (Singular Vector Canonical Correlation Analysis), the focus is indeed on measuring how well combinations of activation patterns from paired instances (such as layers of neural networks) correlate with each other.
        
        Let's break it down a bit further:
        
        1. **Paired Instances**: These can be different layers within the same network or equivalent layers across different networks. The idea is to compare these pairs to understand how similarly each one processes information.
        2. **Combinations of Activation Patterns**: When using SVCCA, you first reduce the dimensionality of the activation patterns from each layer using Singular Value Decomposition (SVD). This reduction focuses on the most significant features or directions of the data, making the analysis more manageable and focused on the most informative aspects.
        3. **Correlation of Combinations**: After reducing the dimensionality, Canonical Correlation Analysis (CCA) is applied. CCA seeks to find linear combinations of features from each set of reduced data (from each layer or model being compared) that are maximally correlated. This means finding the weights or coefficients that, when applied to the activation patterns of one layer, best match the activation patterns of another layer, thereby indicating a high degree of similarity in how the layers are interpreting the data.
        
        ### Practical Example
        
        Imagine you have two neural networks trained on the same task but with different architectures. You want to compare a specific layer from each network to see if they have learned to process the input in similar ways, despite their architectural differences. You would:
        
        - Extract activation patterns from the chosen layer of each network while processing the same set of inputs.
        - Use SVD to focus on the most significant aspects of these activation patterns.
        - Apply CCA to find how combinations of these reduced patterns correlate across the two networks.
        
        This correlation indicates how functionally similar the layers are, suggesting how one network might have insights or efficiencies that could be leveraged in the other, or confirming that both have converged on a similar strategy to solve the problem, despite their differences.
        
    - using examples, does procrustes measures similar of relations like king-queen across models, while svcca measures if red+dog is simialr across models?
        
        You've touched on an interesting distinction between Procrustes Analysis and SVCCA, and how they might be used to compare features or relations across different models. Let's clarify this with examples to show how each method might be applied in practice.
        
        ### Procrustes Analysis
        
        Procrustes Analysis is ideal for directly comparing specific relationships or configurations between two sets of points (or vectors) in a high-dimensional space, typically used for shape analysis or comparing geometric configurations. In the context of word embeddings or similar features:
        
        - **Example Application**: Suppose you have trained two different word embedding models (like Word2Vec models on different corpora). You want to see if the relationship between "king" and "queen" in one embedding space is similar to that in another.
        - **Procedure**: You would extract the vectors for "king" and "queen" from both models, and then use Procrustes Analysis to optimally rotate, scale, and translate the embeddings from one model to best match the corresponding embeddings in the other model. The analysis would allow you to quantify how similar these relationships are, focusing on the vector differences between "king" and "queen" in each space.
        
        ### SVCCA (Singular Vector Canonical Correlation Analysis)
        
        SVCCA, on the other hand, is used primarily to compare how entire layers or sets of activations in neural networks process information. It’s more about the general similarity in data processing across models rather than specific pairwise relationships.
        
        - **Example Application**: Consider two neural network models trained for image recognition. You want to compare if the way one model processes the concept of "red dog" (as an amalgamation of features like color and animal type) is similar to how another model processes the same concept.
        - **Procedure**: You would pass images labeled or associated with "red dogs" through both models, extract the activation patterns from a particular layer in each model, and then apply SVCCA. This method would tell you how similarly the layers in each model are activating in response to the concept of "red dogs," focusing on the patterns of activation rather than specific semantic or geometric relationships.
        
        ### Key Differences
        
        - **Procrustes Analysis** is about directly measuring how similar specific relationships or vector differences are between models, making it suitable for tasks like comparing semantic relationships in language models.
        - **SVCCA** assesses overall similarity in patterns of activity across large sets of neurons or features, making it more suited for evaluating whether different parts of a model (or different models) extract and process similar types of information from their inputs.
        
        So, in essence, Procrustes is for precise, direct comparisons (like "king" minus "queen"), while SVCCA is for broader, pattern-based comparisons (like how "red dog" activates networks). This makes each technique valuable for different types of analysis in machine learning and data science.
        
    - claude response for procrustes (all below use claude)
        
        Your question touches on an important distinction between different methods for comparing embeddings or representations across models. Let me break this down with examples to clarify the difference between Procrustes analysis and SVCCA.
        
        Procrustes Analysis:
        
        Procrustes analysis is indeed more suited for comparing specific relationships or analogies across different embedding spaces. It tries to find an optimal alignment between two sets of points while preserving their relative positions.
        
        Example with "king-queen":
        Let's say we have two word embedding models, A and B.
        
        In Model A:
        vector("king") - vector("queen") = [0.2, 0.3, -0.1]
        
        In Model B (before alignment):
        vector("king") - vector("queen") = [0.5, -0.4, 0.2]
        
        Procrustes analysis would try to find a rotation and scaling that makes these relationships as similar as possible across the two models. After applying Procrustes, the relationship in Model B might look more like:
        vector("king") - vector("queen") ≈ [0.21, 0.28, -0.11]
        
        This allows us to directly compare relationships like "king-queen" across different models.
        
        SVCCA (Singular Vector Canonical Correlation Analysis):
        
        SVCCA, on the other hand, looks at the overall similarity of the representation spaces, rather than specific relationships. It's more about finding correlated directions in the two spaces.
        
        Example with "red+dog":
        SVCCA wouldn't directly measure if "red+dog" is similar across models. Instead, it would look at how the overall representations of words are correlated between the two models.
        
        Let's say we have two models that represent words in a 3-dimensional space:
        
        Model A:
        "red" = [0.1, 0.2, 0.3]
        "dog" = [0.4, 0.5, 0.6]
        
        Model B:
        "red" = [0.2, 0.3, 0.1]
        "dog" = [0.5, 0.6, 0.4]
        
        SVCCA would try to find linear transformations of these spaces that maximize the correlation between them. It might find that the first dimension in Model A corresponds strongly to the second dimension in Model B, for instance.
        
        The result would be a measure of how similar the overall representation spaces are, rather than a direct comparison of "red+dog" or any other specific combination.
        
        In summary:
        
        - Procrustes is better for comparing specific relationships or analogies (like "king-queen") across models.
        - SVCCA is better for assessing overall similarity of representation spaces, without focusing on specific word relationships.
        
        Your intuition about the difference is correct. Procrustes is more about preserving specific relationships, while SVCCA is about finding overall correlations between representation spaces.
        
    - does svcca need correct pairings?
        
        You've asked an insightful question about SVCCA (Singular Vector Canonical Correlation Analysis). Let me clarify this important point:
        
        SVCCA does indeed require correct pairings or alignments between the two sets of representations being compared. This is a crucial aspect of how SVCCA works:
        
        1. Need for alignment:
            - SVCCA assumes that the data points in both sets of representations correspond to each other.
            - In the context of comparing neural network layers or different models, this typically means having the same input examples for both networks/layers being compared.
        2. Example:
        If you're comparing two different neural networks processing images:
            - You'd need to feed the same set of images through both networks.
            - The representations for each image from Network A would be paired with the representations for the same image from Network B.
        3. Contrast with Procrustes:
            - While Procrustes analysis also typically uses aligned data, it's sometimes possible to use it with partially aligned or even unaligned data in some applications.
            - SVCCA, however, fundamentally relies on the paired nature of the data to compute correlations.
        4. Implications:
            - This requirement means SVCCA is most suitable for comparing representations where you have control over the inputs and can ensure alignment.
            - It's less suitable for comparing representations from disparate sources where direct alignment isn't possible.
        5. Use in practice:
            - When used to compare layers within a single network or across different networks trained on the same task, ensuring this alignment is usually straightforward.
            - It becomes more challenging if you're trying to compare representations from very different models or domains.
        
        So, to directly answer your question: Yes, SVCCA does need correct pairings. It's designed to work with aligned sets of representations, where each data point in one set has a corresponding point in the other set. This alignment is fundamental to how SVCCA computes the correlations between the two representation spaces.
        
    - given matrices of rows, does svcca process each row indpeendently of the others?
        
        Your question touches on an important aspect of how SVCCA (Singular Vector Canonical Correlation Analysis) operates. Let me break this down:
        
        1. SVCCA's input:
        SVCCA typically takes two matrices as input, where each row represents a data point (e.g., an activation vector for a specific input) and each column represents a dimension in the representation space.
        2. Processing of rows:
        SVCCA does not process each row independently. Instead, it considers the entire set of rows collectively to analyze the overall structure of the representation space.
        3. Key steps in SVCCA:
            
            a) Singular Value Decomposition (SVD):
            
            - Applied to each matrix as a whole
            - Considers the relationships between all rows to find principal directions
            
            b) Canonical Correlation Analysis (CCA):
            
            - Operates on the reduced representations from SVD
            - Finds correlations between the two sets of representations, considering all data points together
        4. Importance of the full dataset:
            - The strength of SVCCA lies in its ability to capture the overall structure and relationships in the data.
            - Processing rows independently would lose this holistic view of the representation space.
        5. Example to illustrate:
        Imagine we have two matrices, A and B, each with 1000 rows (data points) and 100 columns (dimensions):
            - SVCCA doesn't compare A[1,:] with B[1,:], then A[2,:] with B[2,:], etc.
            - Instead, it considers all 1000 rows of A together and all 1000 rows of B together to find the most correlated directions across the entire datasets.
        6. Implications:
            - This approach allows SVCCA to capture global patterns and similarities between the two representation spaces.
            - It's particularly useful for understanding how different neural network layers or models represent information in aggregate, rather than for point-by-point comparisons.
        
        In summary, SVCCA does not process each row independently. It operates on the entire set of rows (data points) collectively to analyze and compare the overall structure of the two representation spaces. This global approach is key to its ability to find meaningful correlations between different sets of representations.
        
    - explain intuitively what and how svcca processes "global patterns". i'm stil not sure what global patterns means. can you use an example
        
        Certainly. Let's use a concrete example to illustrate what we mean by "global patterns" in the context of SVCCA. This should help clarify how SVCCA processes data collectively rather than row by row.
        
        Example: Analyzing facial recognition models
        
        Imagine we have two different neural networks trained for facial recognition. We want to compare how they represent faces internally. We'll use SVCCA to compare a particular layer from each network.
        
        Setup:
        
        - We have 1000 face images.
        - For each image, we extract the activations from a specific layer in both networks.
        - Network A gives us 100-dimensional vectors for each face.
        - Network B gives us 80-dimensional vectors for each face.
        
        So we end up with two matrices:
        
        - Matrix A: 1000 rows (faces) x 100 columns (features)
        - Matrix B: 1000 rows (faces) x 80 columns (features)
        
        Now, let's break down what SVCCA does and what we mean by "global patterns":
        
        1. Dimension Reduction (SVD step):
        SVCCA first reduces the dimensionality of both matrices. It finds the most important directions in each representation space.
            
            Global pattern here means: Which directions (combinations of original features) capture the most variance across all faces?
            
            For example, it might find that in Network A:
            
            - The first principal component largely corresponds to face width
            - The second to skin tone
            - The third to eye shape
            
            While in Network B:
            
            - The first principal component might relate to facial hair
            - The second to face length
            - The third to eye color
        2. Correlation Analysis (CCA step):
        SVCCA then finds the correlations between these reduced representations.
            
            Global pattern here means: How do the important features in one network relate to the important features in the other network, considering all faces simultaneously?
            
            It might discover, for instance:
            
            - Network A's "face width" component is highly correlated with a combination of Network B's "face length" and "facial hair" components.
            - Network A's "skin tone" component correlates strongly with Network B's "eye color" component.
        
        What makes this "global":
        
        1. Feature Importance: SVCCA determines which features are most important by looking at how they vary across all 1000 faces, not just one face at a time.
        2. Inter-face Relationships: It considers how different faces relate to each other in the feature space. For example, which faces cluster together? Which are far apart?
        3. Cross-network Mappings: It finds how the representation in one network maps to the representation in the other, considering all faces simultaneously.
        4. Invariance to Individual Differences: Small differences in how individual faces are represented don't matter much; SVCCA focuses on the overall structure of the face space.
        
        In essence, "global patterns" refer to the overarching structure of how faces are represented in each network, considering all faces and all features together, rather than analyzing each face in isolation. This allows SVCCA to capture how the networks organize facial information as a whole, which is much more informative than comparing individual face representations one by one.
        
    - so if in space A, X1 is correlated with Y1 and Z1, and in space B, X2 is correlated with Y2 and Z2, then A and B would have high svcca score?
        
        You're on the right track, but let's clarify this a bit further to ensure we accurately represent how SVCCA works.
        
        Your intuition is partially correct, but SVCCA is a bit more complex than just comparing direct correlations between variables. Let's break it down:
        
        1. SVCCA doesn't directly compare correlations between individual variables (like X1 with Y1 and Z1). Instead, it looks at the overall structure of the spaces.
        2. What SVCCA actually does:
            - It finds the principal directions in each space (using SVD).
            - Then it finds correlations between these principal directions across the two spaces.
        3. A high SVCCA score would indicate that:
            - The main directions of variation in space A can be well-mapped to the main directions of variation in space B.
            - This mapping preserves a significant amount of the structure in both spaces.
        4. Example scenario for a high SVCCA score:
        In space A: The first principal component is a combination of X1, Y1, and Z1.
        In space B: The first principal component is a combination of X2, Y2, and Z2.
            
            If these principal components capture similar patterns of variation in both spaces, even if they're made up of different original variables, SVCCA would show a high correlation.
            
        5. Important distinction:
            - It's not about direct variable-to-variable correlations across spaces.
            - It's about whether the overall patterns of variation are similar, regardless of which specific variables contribute to those patterns.
        6. Hypothetical example:
        Space A: First principal component = 0.7X1 + 0.5Y1 + 0.5Z1
        Space B: First principal component = 0.6X2 + 0.6Y2 + 0.5Z2
            
            If these components describe similar patterns across the data points in both spaces, SVCCA would show a high correlation, even though they're composed of different original variables.
            
        
        So, to refine your statement: If the main patterns of variation in space A (which might involve correlations between X1, Y1, and Z1) are similar to the main patterns of variation in space B (which might involve correlations between X2, Y2, and Z2), then A and B would likely have a high SVCCA score. The key is the similarity of the overall structure, not the direct correlations between individual variables across spaces.
        
    - then why does svcca require correct pairing if it doesn't need direct var to var?
        
        You've asked an excellent question that gets to the heart of how SVCCA works. Let me clarify this apparent contradiction:
        
        1. Need for correct pairing:
        SVCCA requires correct pairing of data points, not direct variable-to-variable mapping across spaces.
        2. What "correct pairing" means:
            - Each row in space A should correspond to the same entity (e.g., input sample, image, word) as the corresponding row in space B.
            - The variables (columns) don't need to directly correspond.
        3. Why pairing is necessary:
            - SVCCA aims to find correlations in how the two spaces represent the same set of items.
            - It needs to compare how each item is positioned relative to others in both spaces.
        4. Example to illustrate:
        Imagine we're comparing word embeddings from two different models:
            
            Space A:  [dog, cat, house, car]  (100-dimensional vectors)
            Space B:  [dog, cat, house, car]  (80-dimensional vectors)
            
            - We need "dog" in Space A to be paired with "dog" in Space B, "cat" with "cat", and so on.
            - The dimensions (variables) in A and B don't directly correspond.
        5. What SVCCA does with this pairing:
            - It looks at how "dog" relates to "cat", "house", and "car" in Space A.
            - It then compares this to how "dog" relates to the others in Space B.
            - It's finding correlations in these relationships, not in the raw variables.
        6. Why unpaired data wouldn't work:
            - If "dog" in Space A was compared to "car" in Space B, the analysis of structural similarities would be meaningless.
            - The method relies on comparing the same semantic entities across spaces to find structural similarities.
        7. Analogy:
        Think of it like comparing two different maps of the same city. You need to ensure you're looking at the same locations on both maps, even if the coordinate systems are different.
        
        In essence, SVCCA needs correct pairing to ensure it's comparing representations of the same things across spaces. It then finds correlations in how these things are structured or related within each space, rather than directly comparing individual variables. The pairing ensures we're making meaningful comparisons of the overall representational structure.
        
    - i see, i was thinking about variables in terms of the rows. since in my case, the rows are feature neurons of a weight matrix.
        
        Ah, I see where the confusion arose. Your specific case is indeed different from the typical use case I was describing, and it's a great opportunity to clarify how SVCCA can be applied in different scenarios. Let's break this down:
        
        1. Your specific case:
            - Rows: Feature neurons (from a weight matrix)
            - Columns: Presumably connections to other neurons or input features
        2. Typical SVCCA use case:
            - Rows: Different input samples or data points
            - Columns: Activation values for different neurons
        3. Implications for your case:
            - You're comparing the structure of weight matrices across different models or layers
            - Each row represents a single neuron's connections
        4. SVCCA application in your case:
            - It would find correlations between how neurons are connected in one layer/model versus another
            - It's looking for similarities in the pattern of connections, not in how specific inputs are processed
        5. Why pairing is still important:
            - If the neurons in both matrices serve similar functions, pairing them correctly allows SVCCA to find meaningful structural similarities
            - However, if the neurons don't have a clear one-to-one correspondence, the pairing becomes more challenging and potentially less meaningful
        6. Potential challenges:
            - Neuron order may not be consistent across different models or training runs
            - The number of neurons might differ between the layers you're comparing
        7. Possible approaches:
            - If you have a way to match neurons functionally (e.g., by their role in the network), use that for pairing
            - If not, you might need to consider techniques like Hungarian matching or other alignment methods before applying SVCCA
        8. Interpretation:
            - A high SVCCA score would suggest that the overall pattern of connections is similar between the two weight matrices
            - This could indicate that the layers have learned similar feature detectors, even if the individual neuron weights differ
        
        Given this context, SVCCA is indeed looking at "global patterns" in the sense of overall connection structures across all neurons, rather than how individual input samples are processed. The requirement for "correct pairing" in your case would ideally mean matching neurons with similar functional roles across the matrices, if possible.
        
        This is a more specialized application of SVCCA, and it's great that you brought this up. It highlights how the method can be adapted to different types of neural network analysis beyond just comparing activations.
        
    - why does pairing neuron to another neuron in another weight matrix measure correlations? it's not connections since it's one layer
        
        I apologize for the confusion in my previous response. You're absolutely right to question this, and I appreciate you pointing it out. Let's clarify this situation more accurately:
        
        1. Your specific case:
            - Rows: Feature neurons from a weight matrix
            - Columns: Likely input features or connections to the previous layer
            - You're comparing weight matrices from different models or training runs
        2. Corrected understanding:
            - Each row represents the weights of a single neuron to all its inputs
            - You're not comparing connections between layers, but rather how each neuron is connected to its inputs
        3. SVCCA in this context:
            - It would analyze the similarity in how neurons are connected to their inputs across different models or training runs
            - It's looking for correlations in the weight patterns, not in neuron-to-neuron connections
        4. Why pairing is still relevant:
            - Ideally, you'd want to compare neurons that serve similar functions across models
            - However, this pairing is often not straightforward in practice
        5. What SVCCA actually measures here:
            - It would find correlated patterns in how weights are distributed across inputs
            - High correlation would suggest that neurons in both matrices tend to emphasize similar input patterns
        6. Challenges in this application:
            - Neurons may not have a clear correspondence across different models or training runs
            - The order of neurons (rows) in the weight matrix is often arbitrary
        7. Interpretation:
            - A high SVCCA score would indicate that the overall pattern of how neurons connect to their inputs is similar across the compared weight matrices
            - This doesn't necessarily mean individual neurons are directly comparable, but rather that the space of weight patterns is similarly structured
        8. Practical considerations:
            - Without a clear neuron-to-neuron correspondence, the results of SVCCA might be less interpretable
            - You might need to consider techniques to align or match neurons across matrices before applying SVCCA, or interpret the results more broadly as a measure of overall weight space similarity
        
        Thank you for this follow-up. It's an important distinction that in your case, we're dealing with weights to inputs for individual neurons, not connections between layers. SVCCA in this context would be measuring similarities in how weights are distributed across inputs, which can give insights into whether different models or training runs are learning similar feature detection patterns.
        
    - so what does svcca actually measure? be intuitive
        
        You're right to push for a more intuitive explanation. Let's break this down to the core of what SVCCA is doing in your case:
        
        Imagine you have two weight matrices from different models or training runs. Each row in these matrices represents how a single neuron "sees" its inputs. SVCCA is essentially trying to answer this question:
        
        "Are the ways neurons look at their inputs similar across these two models?"
        
        To understand this intuitively:
        
        1. Think of each neuron as a spotlight:
            - The weights determine where the spotlight focuses (which inputs it emphasizes).
        2. SVCCA is like comparing spotlight patterns:
            - It's checking if the overall pattern of where neurons tend to shine their spotlights is similar between the two models.
        3. What it's really measuring:
            - The similarity in the "directions" that are important in both weight spaces.
            - These "directions" represent common patterns in how neurons connect to their inputs.
        4. An intuitive example:
            - Say in both models, you often see neurons that focus strongly on the top-left of an image and weakly on the bottom-right.
            - SVCCA would pick up on this as a common "direction" or pattern in both weight spaces.
        5. High SVCCA score means:
            - The important patterns in how neurons connect to inputs in one model can be mapped closely to important patterns in the other model.
            - It suggests both models have learned to emphasize similar aspects of the input.
        6. Low SVCCA score means:
            - The ways neurons typically connect to inputs are quite different between the models.
            - It suggests the models might be focusing on different aspects of the input.
        
        In essence, SVCCA is measuring how similar the "landscape" of neuron-input connections is between your two models. It's not about individual neuron comparisons, but about whether the overall tendencies in how neurons connect to inputs are similar across the models.
        
    - i still dont get what you mean by pattern and global. those are vaguely defined. is it comparing feature space similarity?
        
        I apologize for the continued vagueness. You're right to push for clarity, and I appreciate your persistence. Let me try to explain this more concretely, avoiding vague terms like "pattern" and "global."
        
        Yes, SVCCA is essentially comparing feature space similarity, but in a specific way. Here's a more precise explanation:
        
        1. What SVCCA does:
        It measures the similarity between two sets of features (in your case, two weight matrices) by finding linear transformations that make these feature sets as correlated as possible.
        2. Step-by-step process:
        a) It first reduces the dimensionality of both feature sets using SVD (Singular Value Decomposition).
        b) Then it finds linear combinations of features in one set that correlate maximally with linear combinations of features in the other set.
        3. What it's actually measuring:
            - The degree to which linear combinations of features in one weight matrix can predict linear combinations of features in the other weight matrix.
            - In other words, how well can we reconstruct the important aspects of one feature space using the other feature space?
        4. Concrete example:
        Let's say you have two weight matrices, A and B, each with 100 rows (neurons) and 1000 columns (input connections).
            
            SVCCA might find that:
            
            - A linear combination of rows in A (say, 0.5*row1 + 0.3*row2 - 0.2*row3) correlates strongly with a different linear combination of rows in B (say, 0.4*row5 + 0.6*row8 - 0.1*row12).
            - It finds multiple such correlating combinations.
        5. The SVCCA score:
            - Is based on how strong these correlations are.
            - A high score means we can find many strongly correlated linear combinations between the two matrices.
            - A low score means even the best linear combinations we can find aren't very correlated.
        6. Interpretation:
            - High similarity: The two weight matrices represent similar feature spaces, just potentially rotated or scaled differently.
            - Low similarity: The feature spaces are fundamentally different; linear transformations can't make them match well.
        
        So, in essence, SVCCA is measuring feature space similarity by assessing how well linear transformations of one feature set can predict linear transformations of the other feature set. It's not about comparing individual features, but about comparing the spaces spanned by these features.
        
    - what does strong corr lin combo have to do with similar feature spaces just rotated or scaled diff
        
        You're absolutely right to question this connection. Let me break this down more precisely to show the relationship between correlated linear combinations and similarity of feature spaces:
        
        1. What correlated linear combinations mean:
        When we find strongly correlated linear combinations between two sets of features, it indicates that we can express important variations in one set using combinations from the other set.
        2. Rotation and scaling in feature spaces:
            - Rotation: Different bases (combinations of original features) represent the same information.
            - Scaling: The magnitude of variations might differ, but the relationships are preserved.
        3. Connection to feature space similarity:
        If we can find linear combinations in space A that correlate strongly with linear combinations in space B, it suggests that:
            - The essential information captured by the features in A can be expressed using features in B, and vice versa.
            - This is equivalent to saying the spaces are similar, just potentially rotated or scaled differently.
        4. Concrete example:
        Imagine two 2D spaces:
        Space A: x-axis is "size", y-axis is "brightness"
        Space B: 45° rotated from A, with x'-axis capturing a combo of size and brightness
            - A linear combination in A (e.g., 0.7*size + 0.7*brightness) would strongly correlate with a different combination in B (e.g., 1.0*x').
            - This strong correlation indicates that both spaces capture the same fundamental information, just represented differently.
        5. Why this indicates similar feature spaces:
            - If we can find such correlations for multiple important dimensions, it means both spaces are capturing the same underlying factors, just expressing them differently.
            - The ability to "translate" between the spaces via linear combinations indicates their fundamental similarity.
        6. Relation to rotation/scaling:
            - Rotation: Different linear combinations in each space correlate strongly, indicating a rotated view of the same information.
            - Scaling: The strength of correlations might differ, indicating scaled differences in how strongly each space captures certain variations.
        
        In essence, when SVCCA finds strong correlations between linear combinations, it's demonstrating that both feature spaces are capturing the same underlying factors or dimensions of variation in the data. The fact that we need different combinations in each space to show this correlation is what indicates the spaces might be rotated or scaled versions of each other, rather than identical representations.
        
    - intuitively how does procrustes work
        
        Certainly! Let's explain Procrustes analysis intuitively:
        
        Imagine you have two sets of points representing the same objects in different coordinate systems. Procrustes analysis is like trying to overlay these two sets of points as closely as possible using only simple transformations. Here's a step-by-step intuitive explanation:
        
        1. Starting point:
        You have two shapes (sets of points) that look similar but don't quite match up.
        2. Goal:
        Make one shape fit over the other as closely as possible.
        3. Allowed transformations:
            - Translation: Move the entire shape up/down or left/right.
            - Scaling: Make the shape bigger or smaller.
            - Rotation: Spin the shape around its center.
            - (Sometimes) Reflection: Flip the shape like a mirror image.
        4. Process:
            - Center both shapes: Move them so their "average points" are at the origin.
            - Scale one shape: Make it roughly the same size as the other.
            - Rotate one shape: Spin it to align it as best as possible with the other shape.
        5. Measuring fit:
        Calculate how well the points match up after these transformations.
        6. Result:
            - A measure of how similar the shapes are (how well they match after transformation).
            - The transformations needed to achieve the best fit.
        
        Real-world analogy:
        Imagine you have two paper cutouts of the same country, but they're different sizes and orientations. Procrustes analysis is like:
        
        1. Placing both on a table.
        2. Moving one cutout over the other.
        3. Stretching or shrinking one to match the size of the other.
        4. Rotating one until it lines up as well as possible with the other.
        5. Seeing how well they overlap after these adjustments.
        
        Key points:
        
        - It preserves the relative positions of points within each shape.
        - It finds the best overall fit, not perfect point-to-point matching.
        - It tells you both how similar the shapes are and how to transform one to best match the other.
        
        This approach is useful in comparing data sets that might represent the same underlying structure but are expressed in different coordinate systems or scales.
        
    - how procrustes difffers from svcca
        
        Great question! Procrustes analysis and SVCCA (Singular Vector Canonical Correlation Analysis) are both methods for comparing datasets, but they differ in their approach and what they measure. Let's break down the key differences:
        
        1. Basic Approach:
            
            Procrustes:
            
            - Directly transforms one set of points to match another set.
            - Uses rigid transformations (translation, rotation, scaling).
            
            SVCCA:
            
            - Finds correlations between linear combinations of features in both datasets.
            - Doesn't physically transform the data.
        2. What They Preserve:
            
            Procrustes:
            
            - Maintains the relative positions of points within each dataset.
            
            SVCCA:
            
            - Focuses on preserving the directions of maximum variance.
        3. Flexibility:
            
            Procrustes:
            
            - More restrictive, limited to rigid transformations.
            - Assumes a direct correspondence between points.
            
            SVCCA:
            
            - More flexible, can find relationships between different numbers of dimensions.
            - Doesn't require direct point-to-point correspondence.
        4. Dimensionality:
            
            Procrustes:
            
            - Typically works with datasets of the same dimensionality.
            
            SVCCA:
            
            - Can compare datasets with different numbers of dimensions.
        5. Output:
            
            Procrustes:
            
            - Produces a transformed version of one dataset to match the other.
            - Gives a measure of similarity based on the residual differences after transformation.
            
            SVCCA:
            
            - Provides correlations between the most important directions in each dataset.
            - Doesn't produce a transformed dataset.
        6. Interpretation:
            
            Procrustes:
            
            - Easier to visualize, especially in 2D or 3D.
            - Useful when you expect datasets to be similar up to rotation, scaling, and translation.
            
            SVCCA:
            
            - More abstract, deals with correlations in feature space.
            - Useful for comparing complex, high-dimensional representations.
        7. Use Cases:
            
            Procrustes:
            
            - Often used in shape analysis, comparing physical structures.
            - Good for aligning datasets with clear correspondences.
            
            SVCCA:
            
            - Commonly used in comparing neural network representations.
            - Useful when dealing with abstract feature spaces where direct alignment isn't possible.
        
        In essence, Procrustes is about finding the best physical alignment between two sets of points, while SVCCA is about finding the best correlations between linear combinations of features in two datasets. Procrustes is more intuitive and directly interpretable, especially in lower dimensions, while SVCCA is more flexible and better suited for comparing complex, high-dimensional representations where direct alignment might not be possible or meaningful.
        
    - why does svcca need pairing if lin combo doesnt require that? pairing neuron to neuron is required. so two weight matrices have rows of neurons, and each row is paired with its most correlated neuron in terms of mean activation correlation
        
        I apologize for the confusion in my previous explanations. You've made an excellent point that highlights a crucial aspect of SVCCA that I didn't articulate clearly before. Let me clarify:
        
        You're absolutely correct that SVCCA, in its core mathematical operation of finding correlations between linear combinations, doesn't inherently require pairing. The linear combinations are flexible and can work across unpaired data.
        
        However, the pairing requirement comes from a different aspect of the SVCCA process, specifically in how it's typically applied to neural networks:
        
        1. Why pairing is often used:
            - In neural network analysis, we often want to compare corresponding layers or neurons across models.
            - Pairing ensures we're comparing analogous parts of the networks.
        2. Your specific case:
            - You're comparing weight matrices where each row represents a neuron.
            - You're pairing neurons based on mean activation correlation.
        3. Role of pairing in this context:
            - It's not for the mathematical operation of SVCCA itself.
            - It's to ensure we're comparing semantically meaningful units (neurons with similar functions) across models.
        4. What pairing provides:
            - A way to align the rows of the weight matrices before applying SVCCA.
            - This alignment helps in interpreting the results in terms of neuron function.
        5. SVCCA without pairing:
            - Mathematically, SVCCA could be applied to unpaired weight matrices.
            - But the interpretation of results would be less clear in terms of neuron-to-neuron comparisons.
        6. Benefit of your approach:
            - By pairing neurons based on activation correlation, you're ensuring that SVCCA compares weights of functionally similar neurons.
            - This makes the results more interpretable in terms of how similar neurons behave across models.
        
        So, to summarize:
        
        - You're right that the core SVCCA computation doesn't require pairing.
        - The pairing in your case is a pre-processing step to make the SVCCA results more meaningful and interpretable in the context of comparing neural network structures.
        - This pairing ensures that when SVCCA finds correlations between linear combinations, these combinations are based on weights from neurons that are functionally similar across the models.
        
        Thank you for pushing for clarity on this point. It's an important distinction that the pairing is more about setting up a meaningful comparison rather than being a mathematical requirement of SVCCA itself.
        
    - why doesnt this svcca work where neurons aren't paired across weight matrices correctly in terms of mean actv corr
        
        You've asked a crucial question that gets to the heart of applying SVCCA to neural network weight matrices. Let's break this down:
        
        1. SVCCA's core operation:
        SVCCA finds correlations between linear combinations of features (in this case, weight vectors) across two datasets.
        2. Why pairing matters:
            - SVCCA doesn't inherently require pairing for its mathematical operation.
            - However, for meaningful interpretation in the context of neural networks, we typically want to compare functionally similar components.
        3. What happens without proper pairing:
            - SVCCA will still compute correlations between linear combinations of weight vectors.
            - But these correlations may not be meaningful in terms of comparing similar neural functions across networks.
        4. The impact on results:
            - Without proper pairing, SVCCA might find spurious correlations between unrelated neurons.
            - This could lead to overestimating the similarity between the networks.
            - Or, it might miss important similarities if corresponding neurons are misaligned.
        5. Interpretation challenges:
            - If neurons aren't paired correctly, it's harder to interpret what the SVCCA results mean in terms of network function.
            - You might be comparing apples to oranges, so to speak.
        6. Why mean activation correlation matters:
            - Pairing by mean activation correlation helps ensure you're comparing neurons with similar roles across networks.
            - This makes the SVCCA results more interpretable in terms of how functionally similar parts of the networks relate to each other.
        7. SVCCA still "works" mathematically:
            - The algorithm will run and produce results even without proper pairing.
            - But these results may not be meaningful or useful for understanding network similarities.
        
        In essence, SVCCA without proper neuron pairing is like comparing two sentences by randomly matching words from each - you might find some correlations, but they won't tell you much about the actual similarity of the sentences' meanings.
        
        This is why your approach of pairing neurons based on mean activation correlation before applying SVCCA is valuable. It ensures that when SVCCA finds correlations, they're between weights of neurons that are likely playing similar roles in their respective networks, making the results more meaningful and interpretable.
        
    - why does svcca only compare spaces with diff rotation but not permutation
        
        You've touched on a crucial point about SVCCA's properties and limitations. Let's break this down:
        
        1. SVCCA's core operation:
        SVCCA finds correlations between linear combinations of features in two spaces.
        2. Handling rotations:
            - SVCCA can handle rotations because it works with linear combinations.
            - A rotated space can be expressed as linear combinations of the original space.
        3. Why permutations are different:
            - Permutations reorder the features (in your case, neurons) rather than combining them linearly.
            - SVCCA doesn't inherently account for arbitrary reorderings of features.
        4. Mathematical perspective:
            - Rotations preserve the subspace structure, which SVCCA captures.
            - Permutations change the ordering of basis vectors, which SVCCA isn't designed to detect.
        5. Why this matters for neural networks:
            - Neurons in different networks might develop in a different order.
            - Their functional roles might be similar, but their position in the weight matrix could be different.
        6. Limitation of SVCCA:
            - It assumes a consistent ordering of features across the spaces being compared.
            - It doesn't automatically find the best permutation of features to maximize correlation.
        7. Your pairing approach:
            - By pairing neurons based on mean activation correlation before applying SVCCA, you're essentially addressing this limitation.
            - You're creating a consistent ordering across the weight matrices based on functional similarity.
        8. Alternative approaches:
            - Some variations of CCA (like DCCA - Deep Canonical Correlation Analysis) can handle permutations better.
            - Other techniques like optimal transport or graph matching might be used to find the best permutation before applying SVCCA.
        
        In essence, SVCCA is designed to handle linear transformations (like rotations and scalings) but not non-linear transformations like permutations. This is why pairing or aligning neurons based on their function (as you're doing with mean activation correlation) is crucial when applying SVCCA to compare neural network weights. Your approach helps overcome this limitation by ensuring that functionally similar neurons are compared, regardless of their original order in the weight matrices.
        
    - i still dont get the above. explain in detail and how it does this
- ✅ steer using batches to see if “April” is stll present, or some other month
    
    [steering_gemma2_nums_months.ipynb](https://colab.research.google.com/drive/1gsl1OCstEh31pbbGWC4DRAp7H9fDbxsU#scrollTo=Qple37K-DDJ2)
    
    - pair each num prompt with its months analogue, and subtract
    - take mean of all differences
        - try both mean of LLMs and mean of SAEs
    - tests ensure not illusion (anecdotal, etc):
        - steer nw prompts that were not used to construct the steering vector
        - steer ‘aaaa’ random prompts with diff multipliers
            - perhaps the steering isn’t specific to the prompt, but the steering vector just overrides the old prompt?
    - **instead of sequences, just use numbers:** we can take mean sae of 10 NUMERALS and add to nw and months and (some) days of the week (but not letters) depending on steering multiplier used
        - it also works for counting down; "four three two”
        - works for this word problem: "This month is July, next month is”
        - doesn’t work for work problem:  "Today is Monday, tomorrow is”
        - DOES work for work problem:  "Today is Wednesday, tomorrow is”
        - can we do this for LLMs? what if decompose, ablate, recon?
        - try adding to mod 10
            - ISSUE: gemma-2 can’t do mod10 SEQUENCES (cyclic)
- ✅ steering_gemma2_nums_months_v2.ipynb: get rid of other input tasks and umaps and common features, only focus on steering expms to check how many cases get desired answer by steering vec
    - ✅ organize tests into fns / cells
    - ✅ compare to LLM steer vec
    - ✅ **Decompose the LLM steering vec**
        - interpret the features of the steering vector and ablate non-numeric ones
    - ✅ instead of reconstructing the ablated LLM vector, add it directly into SAE space of new actv then recon
    - ✅ **Ablate directly from SAE steering vec**
    - ✅ “list of tests”
        - steer number words (len 3 seqs)
        - steer months (len 4 seqs, non-cyclic)
        - steer days of the week
        - steer word problems (months)
        - steer word problems (days)
        - steer spanish number words
        - steer spanish months
    - ✅ list of steering vectors to compare
        - SAE sv (nums 1 to 9)
        - LLM sv
        - LLM decomposed and ablated; add to LLM space
        - LLM decomposed and ablated; add to SAE space
        - SAE sv ablated
- ✅ steering_gemma2_nums_months_v3.ipynb: turn tests to fns with scores; plot and tables
    - ✅ make “list of tests” into a fn
        - get list of correct answer (manual bc so few)
        - compare output of each prompt with corr ans
        - get % right acc score
- ✅ figures for docs
    - ✅ create a table of right/wrong prompts for **one** test and one sv (best one)
        - rows: prompt
        - cols: unsteered ans, steer ans
    - ✅ obtain a plot of acc values (bar? line?)
        - use bar as line is for continuum on x-axis, which we don’t have when x-axis is sv. two options:
        - do this for a **single** task (eg. months to indices)
            - each x-axis tick is a bar of an sv type
            - y-val are acc scores
        - do this for a few tasks (not all as overcrowded)
            - x-tick is a test, and within each x-tick are multiple diff color bars for each sv
    - ✅ plot of avg scores over all tasks (take max)
    - ✅ OPT (this is same bar 2nd bar plot)- create a table comparing ALL acc results (max only)
        - rows: sv
        - cols: acc score for each test
        - actually no need to do this; is redundant and takes up space
- ✅ submit general appl
- ✅ finish writing neel’s appl
- ✅ finish writeup
    - ✅ Table contents of appl
        - steer
            - compare to steering by just changing or patching vector values
            
            tests ensure not illusion (anecdotal, etc):
            
            - only steer by last token
            - steer random prompts with diff multipliers
                - perhaps the steering isn’t specific to the prompt, but the steering vector just overrides the old prompt?
                - eg)  ‘aaaa’ ; get results on batch of random prompts
            - steer nw prompts that were not used to construct the steering vector
            - steer prompts with random vectors
        - analysis: likely findings, unlikely findings
            - what tests to ensure not illusion- to do in future?
            - do it multiple times to ensure not random chance it happened to be right answer for a prompt
        - follow-up
            - what could be done better
        - appendix: other tests
            - Common top features
                - 3 types: america v china, number words v months, love v hate
            - UMAP
            - ablate then gen (similar to decompose steering vecs)
    - ✅ intro
    - ✅ methods
    - ✅ expm setup
        - check that it’s this specific vector with this ability. ensure not just any nudges would have this effect?
            - add random vector or another steering vector
                - of course this wouldn’t work; in sae space, when we use months vector, it just nudges it to ‘ ‘ space char, not a number char. so no need to do rand vecs (put in appdx)
            - amplify existing actvs to see what happens
                - same reason don’t need to do this as above
    - ✅ expm results
    - ✅ discussion
    - ✅ followup work
        - auto-ablate certain features: a model (one on the level of gpt-4; either the same one or another) can look at the feature labels and choose which features to ablate / steer. this is a general research question.
        - measure the cosine similarity of these steering vectors (SAE and recon LLM)
        - measure effect on model output logits. which one increases correct answer more?
        - what if we manipulate certain features specifically? which ones have the highest change in output (logit diff) after ablation?
        - Try using 0 when constructing steering vecs
        - we can add the LLM recon of the SAE sv (directly constructed from SAE actvs), but given that adding in LLM space seems worse, I did not do this as it may be redundant
    - ✅ possible flaws in expms to test later
        - hard to rigorously tell by just looking at UMAP due to “clustering illusions”
        - (end of writeup) impact: this was just an investigative project out of curiosity, and is not motivated by a research question that would have impact or publications. if i am in MATS, I will focus on actual research questions with impact.
    - ✅ link to appendix: update appendix after submit appl to have a link to new code after appl
- ✅ clean up nb: steering_gemma2_nums_months_v4.ipynb
- ✅ steering_gemma2_nums_months_v5: get actvs using transformerlens rather than gemma2’s tutorial and see if there’s a diff after ablating
- ✅ submit neel’s appl : steering_gemma2_ordinalSeqs.ipynb