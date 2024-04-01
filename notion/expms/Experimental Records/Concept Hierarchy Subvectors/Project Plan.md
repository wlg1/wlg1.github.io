# Project Plan

Simple Approach- Activation Differences

- ⚠️ Compare 2 single prompts (with one difference, say multiple choice) in GPT2 or Pythia or Llama-2’s activations. Compare on multiple dimensions- eg. change from “Save the baby” to “Save the adult”, see what activations change. Create a method to summarize what’s different in these activations.
    
    [[assoc_concepts_explTests.ipynb](https://colab.research.google.com/drive/1AP-JZjCLgYRaicTf2xTaYxju9q9pZbZc)](assoc_concepts_explTests%20ipynb%208d0ff697c8bc43e9ac6df4ea5a332329.md) 
    
    - Ask multiple people theoretically why this wouldn’t work, but still try it yourself
        - ask callum about issues with this approach
            
            Hi, I was thinking about the pros/cons of simple "brute" approach to looking at activations. For instance, inputting two prompts with only a small change between them and just subtracting their activations by components (similar to how steering vecs are found by activation steering). Or doing this via two datasets with only a small change between them and looking at means/the distribution per component. Then, one can see which components have the biggest differences, then applying patching on them to get stronger and causal evidence. Was thinking about this vs individually patching and running each component as in ACDC. I assume early papers must've tried this and thought of cons, which is why more sophisticated techniques had to be used instead. I was wondering what kind of pros/cons you know for this, and what papers have done things like this (as the papers I see mostly use patching)? Thanks!
            
    - Save the cache and just subtract the outputs for each component (cache key).
        - ✅ lion vs red lion
            
            This is hard to directly compare due to tokenization; lion is broken into "l" and "ion", while "red lion" is broken into "red" and " lion". So try hierarchical concepts that aren't broken into multiple tokens.
            
        - color vs red
            - ✅ unembed diffs on resid post
            - ✅ unembed non-diffs
            
            This is NEXT TOKEN prediction. So putting “color” through the NN doesn’t really predict “color”. We need to direct the input to try to output “color” vs “red”. 
            
        - ⚠️ question on lion vs red lion tokenization
            
            if I pass in "lion" and "red lion" as 2 prompts in a batch to gpt2-small, the resid post tensor shape is [2, 3, 768]. Lion is 1 token, so why is seq len 3? Is the last token in the first prompt "lion" padding? Is the first token padding? If both the first and last token are padding, why are 
            
- ✅ ⚠️ assoc_concepts_explTests_llama2.ipynb
    
    [https://colab.research.google.com/drive/1Gpz305GhYswEkYtUBSgPJeqFJKvXGxFt#scrollTo=osj9DKA6MxbE](https://colab.research.google.com/drive/1Gpz305GhYswEkYtUBSgPJeqFJKvXGxFt#scrollTo=osj9DKA6MxbE)
    
    - debug why prompts return twice, and don’t match with answer token, and have same token (father)
        - ✅ Ask #questions in ARENA slack
            
            Does anyone know why using this TransformerLens function on Llama2 return two rankings? It only returns one for GPT2.
            
            ![Untitled](Project%20Plan%2069cd4099a97748dcb58439d3036f1a6d/Untitled.png)
            
        - ✅ Wait for answers
            
            It looks like it's because the thing you passed in got tokenized into 2 separate tokens (weirdly the first one seems like just the empty string, idk why)
            
            I'm guessing `utils.test_prompt` under the hood does something like tokenize the answer then iterate over each token in the answer and apply this to each of them
            
            So the thing I'd recommend is look under the hood and see if you can find & fix the part of the code that tokenizes the answer as `["", "short"]` (assuming you passed in just the string `"short"`)
            
        - ✅ Ask chatgpt with attached screenshot
            
            why using this TransformerLens function on Llama2 return two rankings? It only returns one for GPT2. search up this repo's file for an answer: [https://github.com/neelnanda-io/TransformerLens/blob/main/transformer_lens/utils.py](https://github.com/neelnanda-io/TransformerLens/blob/main/transformer_lens/utils.py)
            
            The function `utils.test_prompt` from the TransformerLens repository seems to generate two rankings when used with LLaMA-2 models due to differences in how the models are implemented and possibly due to additional features or configurations within the LLaMA-2 models compared to GPT-2.
            
            For instance, the implementation of LLaMA-2 models could have variations in how the logits are processed or how the probabilities are calculated and displayed. LLaMA-2 models might also incorporate additional layers or components, which could affect the output of such utility functions. Another aspect could be the different architectural choices or hyperparameters used in LLaMA-2 models that might result in varied outputs from utility functions like `utils.test_prompt`.
            
            TransformerLens has been updated to support LLaMA-2 models, which might have introduced changes to the way model outputs are handled, including the ranking of logit scores【6†source】【7†source】【8†source】. To find the specific reason why `utils.test_prompt` is returning two rankings for LLaMA-2, one would likely need to examine the pull requests and issues on the GitHub repository, particularly those related to the support and implementation of LLaMA-2 models. This might provide insights into any changes made to the function or model handling that could result in multiple rankings being returned.
            
            [https://github.com/neelnanda-io/TransformerLens/issues/353](https://github.com/neelnanda-io/TransformerLens/issues/353)
            
            [https://github.com/neelnanda-io/TransformerLens/pull/234](https://github.com/neelnanda-io/TransformerLens/pull/234)
            
            [https://github.com/neelnanda-io/TransformerLens/releases](https://github.com/neelnanda-io/TransformerLens/releases)
            
        - look at: [https://github.com/neelnanda-io/TransformerLens/blob/main/transformer_lens/utils.py](https://github.com/neelnanda-io/TransformerLens/blob/main/transformer_lens/utils.py)
            - `prepend_bos=True` is required for it to work correctly. Changing it to False doesn’t fix it.
                
                see [test_prompts_llama2_7b](https://colab.research.google.com/drive/1zFWHdQkE8vpRe6PcQwoOVz1qAdNBwtdY#scrollTo=o_DBP8Geq07r).ipynb
                
                Note that GPT uses `['<|endoftext|>'`, but llama uses `['<s>'` . 
                
            - It’s split by `answer_str_tokens = model.to_str_tokens(answer, prepend_bos=False)` in `test_prompt()`. It will split it even if use ‘8’ without space in front and using prepend_bos=True.
                - `to_str_tokens`: [https://github.com/neelnanda-io/TransformerLens/blob/main/transformer_lens/HookedTransformer.py#L812](https://github.com/neelnanda-io/TransformerLens/blob/main/transformer_lens/HookedTransformer.py#L812)
                    
                    uses `to_tokens`, which uses:
                    
                
                ```jsx
                tokens = self.tokenizer(
                            input,
                            return_tensors="pt",
                            padding=True,
                            truncation=truncate,
                            max_length=self.cfg.n_ctx if truncate else None,
                        )["input_ids"]
                ```
                
        - ✅ ask on #questions in MI server
            
            Has anyone used transformerlens on llama-2 using the hf LlamaTokenizer before? Looking to do logit lens on it, and got a bunch of questions on why the tokenizer seems to split strings into having the empty space ' ' token sometimes (which it puts after the endoftext token). Eg)
            
            > model.tokenizer('short') tokenizers into <s> and short token, but model.tokenizer('8') tokenizes into <s> '' and 8 tokens. Using model.generate with max_new_tokens=1 on "opposite of tall is" will predict short, but using it on "5 6 7" will predict " ". But utils.test_prompt() in transformerlens will always split the answer, even short, into '' and 'short', regardless of prepend_bos or not using a space in the answer argument to test_prompt
            > 
            
            There's a lot to type, would be cleaner if anyone has time to call, rather than take up space pasting it on this channel
            
        - wait for answer
    - ✅ debug why unembedding last layer of llama is inconsistent with predicted token
        - ✅ if the tokenizer splits the answer, then the predicted token is the space? check the shape of the logits for a single prompt
            
            it’s just the next token, not two tokens
            
        - ✅ `tl_model.generate("The opposite of left is right. The opposite of tall is", max_new_tokens=1, **generate_kwargs)`
            
            This gives the next token as “short”, but not “ “.
            
            model.tokenizer('short') tokenizers into <s> and short token, but model.tokenizer('8') tokenizes into <s> '' and 8 tokens. Using model.generate with max_new_tokens=1 on "opposite of tall is" will predict short, but using it on "5 6 7" will predict " ". 
            
        - ✅ SOLN: Try this code
            
            ```
            last_token_logits = original_logits[:, -1, :]
            values, indices = torch.topk(last_token_logits, 5, dim = -1)
            for token_id in indices[0]:
                print(model.tokenizer.decode(token_id.item()))
            ```
            
            This gives this result:
            
            ```jsx
            short
            small
            short
            Short
            ...
            ```
            
            Before, you tried this code:
            
            ```jsx
            resid_post_0 = cache['ln_final.hook_normalized']
            resid_post_0_diffs = resid_post_0[1][1]
            resid_post_0_diffs_batchPos = resid_post_0_diffs.unsqueeze(0).unsqueeze(0)
            resid_post_0_diffs_logits = model.unembed(resid_post_0_diffs_batchPos)
            resid_post_0_diffs_logits_squeezed = resid_post_0_diffs_logits.squeeze()
            
            top_token_ids = torch.topk(resid_post_0_diffs_logits_squeezed, k=5).indices
            for id in top_token_ids:
                print(model.tokenizer.decode(id))
            ```
            
            and got this:
            
            ```jsx
            
            in
            (
            I
            following
            ```
            
            But: ln_final suggests a layer normalization layer, it's more likely that you're dealing with normalized features or activations rather than logits. Logits specifically refer to the outputs of a model that are then passed to a softmax function (in the context of classification) to obtain probabilities. 
            
            ALSO:
            
            `resid_post_0[1][1]` is not correct! This gets the second token pos of the prompt! This worked before when there was a ONE TOKEN PROMPT b/c the ‘1’ was the “second token” given the split of ‘’ and input_token, but now there’s moer than one token. So update it to be:
            
            ```jsx
            last_token_actvs = resid_post_0[:, -1, :]
            last_token_actvs = last_token_actvs.unsqueeze(0)
            unembed_last_token_actvs = model.unembed(last_token_actvs)
            unembed_last_token_actvs = unembed_last_token_actvs.squeeze()
            values, indices = torch.topk(unembed_last_token_actvs, 5, dim = -1)
            for token_id in indices[0]:
                print(model.tokenizer.decode(token_id.item()))
            ```
            
    - ✅ Try adding a space at the end of prompt. Now, “The word for a male parent is” works (before, opposites already worked)
    - ✅ ISSUE: GPU RAM 39.5 / 40.0 GB ; how to clear? gc and del dont make it go down. trying to cache transformer activations
        
        [https://chat.openai.com/c/ae6c8058-0931-4511-81d0-34207178318a](https://chat.openai.com/c/ae6c8058-0931-4511-81d0-34207178318a)
        
        **Ensure Variables are Actually Deleted**: Sometimes, merely calling **`del`** on a variable doesn't free up memory if there are other references to the object it points to. Make sure the object you're deleting doesn't have other references pointing to it.
        
        don’t use model = tl_model, it makes a copy!
        
- 🐣 [List of papers- concept repr](List%20of%20papers-%20concept%20repr%202da9545e277847e2bbac3fa05df46be3.md)
- 🐣 [Brainstorm- concept repr](Brainstorm-%20concept%20repr%205cdd49ded4d04473a8823d72367f83fe.md)
- ✅ Unembed father-mother and opposite actvs
    
    [assoc_concepts_explTests_llama2_v2.ipynb](https://colab.research.google.com/drive/1JZijP3F8SoTGigleW6BuCQPElEMJaMXT)
    
    This cleans up explr test results from v1
    
    IMPT: `unembed()` requires a 3D tensor, so either use unsqueeze twice (if one sample) or once (if a batch) because you sliced the position dim, which makes a 1D or 2D tensor
    
    Also, `indices` doesn’t need [0] if just a single sample. Indices has first dim of size N for N samples, so [0] gets the first sample’s top tokens!
    
    ```jsx
    last_token_actvs = cache['ln_final.hook_normalized'][1, -1, :]
    last_token_actvs = last_token_actvs.unsqueeze(0).unsqueeze(0)
    unembed_last_token_actvs = model.unembed(last_token_actvs)
    unembed_last_token_actvs = unembed_last_token_actvs.squeeze()
    values, indices = torch.topk(unembed_last_token_actvs, 5, dim = -1)
    for token_id in indices:
        print(model.tokenizer.decode(token_id.item()))
    ```
    
- ✅ Unembed their activation differences
    
    This gives “masculine” direction
    
    ```jsx
    for layer in range(32):
        last_token_actvs = cache[f'blocks.{layer}.hook_resid_post'][:, -1, :]
        last_token_actvs = cache[f'blocks.{layer}.hook_resid_post'][0, -1, :] - cache[f'blocks.{layer}.hook_resid_post'][1, -1, :]
        last_token_actvs = last_token_actvs.unsqueeze(0).unsqueeze(0)
        unembed_last_token_actvs = model.unembed(last_token_actvs)
        unembed_last_token_actvs = unembed_last_token_actvs.squeeze()
        values, indices = torch.topk(unembed_last_token_actvs, 1, dim = -1)
        for token_id in indices:
            print('layer', layer, model.tokenizer.decode(token_id.item()))
    ```
    
    if you switch the two sample’s subtraction, you get the “feminine” direction
    
- ✅ Try abstract class vs specific class vectors
    
    We reproduced the activation steering results in a way. Now, we try this to find abstract vs specific directions. OR, we subtract abstract from each type of specific.
    
    Ideas to try
    
    - animal - lion , animal - tiger, lion - tiger
    - animal - (lion, tiger) , animal - (wolf, coyote), (lion, tiger) - (wolf, coyote)
    - NOTE: we can’t just repeat “animal” because that’d activate a copying mechanism, rather than the “semantic” reasoning mechanism in the activations?
    - Try inputting definition and asking what animal it is
        - ISSUE: Doesn’t work: A large cat of the genus Panthera, native to Africa and India; what type of animal is this?
        - This works, but “lion” has two tokens: A large feline animal is called a
        - Use this instead: A canine animal is called a
        - ISSUE:
            
            ```jsx
            prompts = ["A fern is a plant. A rat is an ",
                       "A feline animal is called a "]
            ```
            
            This doesn’t add padding? Cat isn’t predicted; 0 is instead. This is b/c first prompt is 13, second is 9. But when we pass same len prompts, cat is predicted.
            
        - SOLN: just make all prompts have same length
        
        ```jsx
        prompts = ["Fern is plant. Rat is an ",
                   "A feline animal is called a ",
                   "A canine animal is called a "]
        ```
        

Findings:

Dog - cat (and dog - animal) just gives dog instead of anything meaningful. This means they’re mostly unrelated, so the cat direction has no impact on dog. This is the same with animal - cat or animal - dog, or cat - . In contrast, father - mother is a vector that unembeds as male. 

Therefore, we didn’t find that subtraction yields insights into how the model views dog as a “type” of animal. This sort of knowledge may be stored somewhere in an MLP, rather than be a general latent space relation. So general-specific relation is not as trivial as an activation vector. This is good, as it is not easy for concurrent work to find how this is represented.

So, what hypotheses are there about how this is represented? 

1. As MLP fact recall (animal-dog as a “triplet”)
2. As circuits (recognize animal, recognize dog, then relate them)

~~Separately run animal vs cat/dog then compare their activations~~

seems like unembed uses softmax on activations to turn them into logits. when we already have logits, we don’t need unembed

Turn above findings into doc pgs

Export notion and place notes + code in repos (site + paper_drafts ‘notes folder’ repos)

- [Brainstorm- anything](Brainstorm-%20anything%20d5fe68be1dae4787b718e7011b2f588e.md)

### Future Work

Interpret Abstract Reasoning

LLaMA can complete abstract reasoning. Find the components used in an abstract group.

- distance of animal-cat to animal-dog
- multiply, divide, and other strange vector operations / algorithms. ask chatgpt for ideas
    - aside from vector addition in latent space like king-queen, what other multiply, divide, and other strange vector operations / algorithms can we try?
        
        ### 1. Vector Multiplication and Division
        
        While less common due to the non-linear nature of latent spaces, these operations can be experimented with. For instance, attempting to multiply vectors to amplify or diminish certain features, or using division as a form of feature attenuation or extraction. These operations are not standard and can have unpredictable outcomes due to the lack of a direct mathematical foundation in the context of latent spaces.
        
        ### 2. Analogical Reasoning
        
        Beyond simple arithmetic, exploring complex analogical reasoning tasks where relationships are encoded as operations in latent space. For example, finding analogies across different domains (art styles, music genres) by manipulating vectors to reflect these relationships.
        
        ### 3. Interpolation and Extrapolation
        
        Interpolating between vectors in latent space can reveal smooth transitions that capture underlying data generative factors. Conversely, extrapolating beyond known data points can generate novel, sometimes outlandish, outputs. These techniques are particularly popular in generative models for creating smooth animations or exploring variations of generated entities.
        
        ### 4. Clustering and Dimensionality Reduction
        
        Using algorithms like t-SNE or UMAP to visualize high-dimensional latent spaces can reveal clusters and relationships not evident in the original high-dimensional space. These reduced spaces can then be manipulated or explored further to understand the structure of the data.
        
        ### 5. Regularization and Normalization Techniques
        
        Applying different forms of vector normalization (e.g., L2 normalization) or regularization techniques can enforce constraints on the vectors, leading to different behaviors or representations in latent space. This can be useful in controlling the magnitude of vectors, preventing overly dominant features, and improving the interpretability of latent representations.
        
        ### 6. Neural Arithmetic Logic Units (NALU)
        
        Developing models that explicitly aim to perform arithmetic operations within neural networks, NALUs are designed to learn and execute a range of arithmetic tasks (addition, subtraction, multiplication, division) directly within the model's architecture. While not a latent space operation per se, it represents an approach to embed arithmetic reasoning within neural models.
        
        ### 7. Eigen Decomposition and Spectral Methods
        
        Applying spectral methods, such as eigen decomposition, to latent representations can reveal principal directions of variance, akin to principal component analysis (PCA) in traditional statistics. Manipulating vectors along these principal directions can offer insights into the most significant modes of variation within the data.
        
        ### 8. Complex and Hypercomplex Operations
        
        Exploring operations within complex or hypercomplex spaces (e.g., quaternions) for certain types of data, especially where relationships might be more naturally represented in these spaces, such as rotations in 3D space or relationships between entities that require a richer mathematical framework than real-valued vectors can provide.
        
        Each of these approaches requires careful experimentation and validation, as the non-linear and high-dimensional nature of latent spaces can lead to unexpected results. The effectiveness and interpretability of these operations can vary greatly depending on the specific application and the characteristics of the latent space.
        
- Are “same output” activations and their difference vectors different based on the prompt used? Clearly, repetition won’t work.
- is father - mother same vector as king - queen ?
- behavior - concept
- (analogous abstraction) - (specific)
    - person sad vs glass breaking ; how to find what’s common between them?
- “throw things in blender for fun”- try out other strange differences when have time
- Can circuit of neural network components be turned into geometric latent space representations, just like neurons are vectors in latent space?
    
    Yes, circuits of neural network components can be turned into geometric latent space representations, similar to how individual neurons are often conceptualized as vectors in a latent space. This process involves mapping the functional or structural properties of a neural circuit—a collection of interconnected neurons or components—into a multidimensional geometric space. This representation can help in understanding the complex interactions within the circuit and between different circuits within the network.
    
    ### How It Works
    
    1. **Vector Representation**: Each neuron or component in the circuit can be represented as a vector in a high-dimensional space based on its properties, such as its activation patterns, connections, or the weights of its connections. This is akin to how words are represented in natural language processing (NLP) tasks using techniques like word embeddings.
    2. **Circuit as a Geometric Object**: The circuit, being a collection of these neurons/components, can be represented as a geometric object in this space. This object's shape, orientation, and location within the latent space can provide insights into the circuit's functionality and its role within the larger network.
    3. **Dimensionality Reduction and Visualization**: High-dimensional data is often hard to interpret directly. Techniques like PCA (Principal Component Analysis), t-SNE (t-distributed Stochastic Neighbor Embedding), or UMAP (Uniform Manifold Approximation and Projection) can be used to reduce the dimensions of the latent space to a more manageable number (often 2D or 3D) for visualization and analysis. This process helps in understanding the relationships and dynamics within the circuit.
    4. **Analysis of Circuit Dynamics**: By studying the geometric latent space representations, researchers can identify patterns, clusters, or trajectories that signify different operational modes, behaviors, or states of the neural circuit. This can lead to insights into how neural networks process information and adapt to new inputs.
    
    ### Applications
    
    - **Understanding Neural Network Behavior**: This approach helps in deciphering how complex neural networks, such as those in deep learning, accomplish specific tasks, by breaking down the network into interpretable components.
    - **Network Pruning and Optimization**: By identifying redundant or less significant components within a circuit, it's possible to streamline the network for efficiency without significant loss of performance.
    - **Neuroscience Research**: In biological contexts, mapping neural circuits to geometric spaces can aid in understanding the brain's structural and functional architecture.
    
    This geometric representation of neural circuits complements traditional analysis techniques by providing a visual and conceptual framework to study the collective behavior of groups of neurons or components within neural networks.
    
- What object is the circuit then? is it a vector?
    
    When we talk about representing a neural network circuit as an object in a geometric latent space, it's not just as a single vector but rather as a more complex geometric structure that could encompass multiple dimensions and embody the relationships and interactions between its components (neurons or layers). Here's how we can conceptualize it:
    
    1. **Vectors for Individual Components**: Individual neurons or components within the circuit can indeed be represented as vectors in the latent space, where each vector's direction and magnitude could encode properties such as activation levels, connection patterns, or other relevant characteristics.
    2. **Circuit as a Composite Structure**: The circuit as a whole, however, becomes a composite structure made up of these vectors. This structure can be thought of in several ways, depending on the level of abstraction and the properties you're focusing on:
        - **Point Cloud**: If each neuron/component is a vector, the entire circuit could be visualized as a point cloud in the latent space, where each point represents a neuron or component, and the spatial relationships between points reflect their interactions.
        - **Subspace or Manifold**: In more abstract terms, the circuit could form a subspace or a manifold within the larger latent space. This means the circuit's overall behavior and properties could be represented by the geometric relationships within this subspace—such as distances between points (vectors), angles, or curvature.
        - **Graph Structure**: Considering the connectivity and flow of information, the circuit can also be represented as a graph embedded in the latent space, where nodes (vertices) are the vectors representing neurons, and edges indicate connections or interactions between them.
    3. **Beyond Simple Vectors**: While individual components might be vectors, the circuit itself, when considered as a whole, transcends the simple vector representation. It embodies the complex interplay and dynamics of its components, and understanding it requires analyzing the geometric or topological properties of the structure it forms in the latent space.
    4. **Analysis Tools**: Tools and techniques like dimensionality reduction (PCA, t-SNE, UMAP), clustering, and network analysis can be used to study this complex structure. They help in identifying patterns, clusters, components, or pathways within the circuit that are crucial for its function.
    
    Thus, in a geometric latent space, a neural network circuit is represented as a complex geometric object or structure that reflects the interactions, functions, and dynamics of its components, rather than as a single vector. This approach offers a richer and more nuanced understanding of neural circuits, facilitating insights into their operational principles and behaviors.
    
- [https://discordapp.com/channels/1042030674388979713/1211743151136579667/1217770018066923550](https://discordapp.com/channels/1042030674388979713/1211743151136579667/1217770018066923550)

Vision

- Compare text vectors to image vectors across models
- logit lens for image models: unembed CNNs instead of feature viz
- edit text-to-image models. does image affect behavior?
- [https://gabgoh.github.io/ThoughtVectors/](https://gabgoh.github.io/ThoughtVectors/)

LLM

- Are there “analogous memories” (templates like tortoise vs hare) in text models?
- Can a llm learn a fable and extrapolate from it?

---

Why pursue this topic:

This work is highly novel, and I think it would make for high impact citations if any future work involving text vs image models and abstract vectors is done, as they’d have to cite this.

How does editing abstract concepts affect behavior? Compare activation vectors of concepts vs that of behavior. Surely, there are similarities between “danger” vector and “dangerous behavior”? Can we cluster them?

Hopefully others are more focused on implementation and theoretical details such as scaling to do the same interpretations for abstract and analogous activation comparisons. 

Also, hopefully they did try something similar but not the same and were not able to solve it. People can tackle the same problem but solve it in different ways; they may not find the same insights or even be able to solve it.

How to approach problems

Worrying about every detail is infeasible. Only double check things that lead to generalizable, impt findings about ‘laws’.

---

Papers and resources

- Analyzing Transformers in Embedding Space (Dar, Geva, et al 2022)
    - [https://github.com/guyd1995/embedding-space](https://github.com/guyd1995/embedding-space)
        - Parameter-alignment.ipynb aligns the two models!
        
        [https://colab.research.google.com/drive/1TO7LzabzLvpiIfJ3mZylEwZF9Llhou6H#scrollTo=7ff967e6-9737-410f-9ade-52af976bdbc9](https://colab.research.google.com/drive/1TO7LzabzLvpiIfJ3mZylEwZF9Llhou6H#scrollTo=7ff967e6-9737-410f-9ade-52af976bdbc9)
        

[https://www.lesswrong.com/posts/kobJymvvcvhbjWFKe/laying-the-foundations-for-vision-and-multimodal-mechanistic](https://www.lesswrong.com/posts/kobJymvvcvhbjWFKe/laying-the-foundations-for-vision-and-multimodal-mechanistic)

Tools:

[https://github.com/openai/transformer-debugger](https://github.com/openai/transformer-debugger)