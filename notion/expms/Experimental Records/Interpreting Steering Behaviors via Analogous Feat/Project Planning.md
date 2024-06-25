# Project Planning

[Done](Project%20Planning%20b4b05f73d85e409f8409b209e44ed692/Done%201c002201437341e48b55b8276859a632.md)

---

### Working on

Reproduce SAE decomposition on Llama-2 CAA

- 🐣 training_a_sparse_autoencoder.ipynb
    
    [https://www.alignmentforum.org/posts/f9EgfLSurAiqRJySD/open-source-sparse-autoencoders-for-all-residual-stream](https://www.alignmentforum.org/posts/f9EgfLSurAiqRJySD/open-source-sparse-autoencoders-for-all-residual-stream)
    
    [https://github.com/jbloomAus/SAELens](https://github.com/jbloomAus/SAELens)
    
    training_a_sparse_autoencoder_v1.ipynb: [https://colab.research.google.com/drive/1EUOEuFkIZ6pfYrcCwoNds9ejRQ269Pay](https://colab.research.google.com/drive/1EUOEuFkIZ6pfYrcCwoNds9ejRQ269Pay)
    
- ✅ GPT2_SAE_training_v1.ipynb
    - ✅ Find training data for SAEs
        
        Data cands
        
        - SAE find paper: “All dictionaries were trained on 20M activation vectors obtained by running Pythia-70M over the Pile
        
        - [https://github.com/lyezene/alignment-regularization/blob/main/utils/gpt2_utils.py](https://github.com/lyezene/alignment-regularization/blob/main/utils/gpt2_utils.py)
        
        [https://huggingface.co/datasets/HuggingFaceFW/fineweb](https://huggingface.co/datasets/HuggingFaceFW/fineweb)
        
        - streaming=True
            
            When you use **`streaming=True`**, the dataset is not loaded into memory all at once. Instead, data is fetched and processed on-the-fly as you iterate over it. This means you can start working with the data almost immediately without waiting for the entire dataset to be downloaded and loaded into memory. Streaming is particularly useful when working with very large datasets, such as "The Pile," which are too large to fit entirely in memory.
            
        
        [https://github.com/lyezene/alignment-regularization/blob/main/data/gpt2_dataset.py](https://github.com/lyezene/alignment-regularization/blob/main/data/gpt2_dataset.py)
        
        able to get actvs for gpt2 SMALL by passing all inputs as tokens in one batch with hook fn to save actvs in global list
        
        - [https://huggingface.co/jbloom/GPT2-Small-SAEs](https://huggingface.co/jbloom/GPT2-Small-SAEs)
        
        dataset used to train: [https://huggingface.co/datasets/Skylion007/openwebtext](https://huggingface.co/datasets/Skylion007/openwebtext)
        
        - 🐣 batch train, as computing all h at once runs out of memory
            
            saeWrapper.train()
            
            train_loader contains actvs
            
        - ✅ look at ARENA 1.2 for how to only save actvs from a certain layer using hook
            - issues with storing hook actvs
                
                ```
                    # h_store = pattern  # this won't work b/c replaces entire thing, so won't be stored
                    # h_store.append(1) # if h_store = [], this will work
                    h_store[:] = pattern  # this works b/c changes values, not replaces entire thing
                ```
                
        - ✅ error when training SAE on dataset actvs
            - issue details
                
                RuntimeError: Trying to backward through the graph a second time (or directly access saved tensors after they have already been freed). Saved intermediate values of the graph are freed when you call .backward() or autograd.grad(). Specify retain_graph=True if you need to backward through the graph a second time or if you need to access saved tensors after calling backward.
                
            
            This is not about h size b/c even when using same sizes as when it worked without getting h from dataset, it has same error
            
            **SOLN**: notice your new h has this at the end when calling it, and other prev h didnt’ have this: `grad_fn=<UnsqueezeBackward0>)`
            
    - ✅ code to decompose steering vectors
        
        Look at CAA and Original steering code: [https://colab.research.google.com/drive/1ubDl3dEY7aj3C2iEZOSczRWahAIgiFZJ?usp=sharing](https://colab.research.google.com/drive/1ubDl3dEY7aj3C2iEZOSczRWahAIgiFZJ?usp=sharing)
        
        - ✅ Train with more samples and SAE instances
    - ✅ find features that actv highest for sample X
- 🐣 Scale up to more efficiently use mem for gpt-2-xl with more train data
    
    gpt2-xl is 1.5b. “RLHF interp” used up to pythia-160m. “SAE find” use Pythia-410M
    
    - ✅ ask amir for advice
        
        Hi, I found that deepmind was already doing activation steering by SAE features, and I'm looking to reproduce their work. I was wondering if you have any experience with training SAE models on models like gpt-xl with 1.5B params? I saw in your rlhf paper you work with pythia-160m. I can train gpt2 small with openwebtext, but even with a100 on colab i can only pass in around 100-1000 samples before I get out-of-mem errors.
        
        For details, I'm using hooks to only save activations for the relevant layer, though I'm passing all tokens in at once (I guess I should use mini batches). Do you have any other tips when dealing with memory issues? Also, this is the post I'm looking to reproduce, it may be helpful for sleeping agent feature decomposition too: [https://www.alignmentforum.org/posts/C5KAZQib3bzzpeyrg/progress-update-1-from-the-gdm-mech-interp-team-full-update#Activation_Steering_with_SAEs](https://www.alignmentforum.org/posts/C5KAZQib3bzzpeyrg/progress-update-1-from-the-gdm-mech-interp-team-full-update#Activation_Steering_with_SAEs)
        
- ✅ [JBloom May SAE workshop](SAE%206b08b4ad57a342bf9393d2ef0fa31c6b/JBloom%20May%20SAE%20workshop%20fe2e004ec02742a88a0c5a6ec61d7415.md)
- ✅ [Patching](Patching%20c56dd40648f24f1c9095c38f63d50333.md)
- ✅ Scale up to more efficiently use mem for **gpt-2-xl** with more train data
    - training_a_sparse_autoencoder: (SAElens tutorial) [https://colab.research.google.com/drive/1EUOEuFkIZ6pfYrcCwoNds9ejRQ269Pay](https://colab.research.google.com/drive/1EUOEuFkIZ6pfYrcCwoNds9ejRQ269Pay)
    - GPT2XL_SAElens_training: [https://colab.research.google.com/drive/1PVwCGx4n_HTxMKSjLSbBgxQIR8eas8tS#scrollTo=U4P9POScwSoZ](https://colab.research.google.com/drive/1PVwCGx4n_HTxMKSjLSbBgxQIR8eas8tS#scrollTo=U4P9POScwSoZ)
        
        tutorial code already uses batch training
        
        - ✅ change prompts. see what’s used by: [https://www.alignmentforum.org/posts/C5KAZQib3bzzpeyrg/progress-update-1-from-the-gdm-mech-interp-team-full-update#Activation_Steering_with_SAEs](https://www.alignmentforum.org/posts/C5KAZQib3bzzpeyrg/progress-update-1-from-the-gdm-mech-interp-team-full-update#Activation_Steering_with_SAEs)
        - ✅ L4 is OOM
        - L0, no save or save to wandb: Can train using A100
            
            ```
            total_training_steps = 1000  # probably we should do more
            batch_size = 4096
            ```
            
            total iterations: 4096000 = 1000 * 4096
            
        
        View results at: [https://wandb.ai/wlg100/sae_lens_exploraTest](https://wandb.ai/wlg100/sae_lens_exploraTest)
        
- ⚠️ ISSUE: It can train, saving to wandb, on L0 of gpt-2-xl, but not on L20 ( whether save or not)? even though same dims?
    - ✅ works on L0, L1, L5, but not on L9, L10, L20
- 🐣 [wandb arena 0.3](https://colab.research.google.com/drive/1Nqb3Iw6EjkRP3YUsi2iTopuccJGSZ4pE)
    
    [https://wandb.ai/home](https://wandb.ai/home)
    
    - how models saved on new wandb project?
        
        start new proj: `wandb.init`
        
        **save: `wandb.finish`**
        
    
    ```jsx
    def __init__():
    	wandb.init()
    	wandb.watch()
    def train():	
    	for epoch in epochs:
    		wandb.log()
    	wandb.finish()
    ```
    
- 🐣 vast.ai
    
    [Compute](Compute%20e3182612433a4299b4035d5359548fa4.md) 
    
    - [https://arena3-chapter0-fundamentals.streamlit.app/](https://arena3-chapter0-fundamentals.streamlit.app/)
        
        scroll down to “**System Requirements” and “Virtual Machines”**
        
    
    The GPUs on vast.ai, lambda labs are less powerful than colab pro+
    
- 🐣 sparse feature circuits: find relations between features
    
    [sparse feature circs explora](sparse%20feature%20circs%20explora%2000b39c6ce28e41f991fb17801204ec9d.md) 
    
    - ✅ Run README bash code to get and eval circs: [sparse_feature_circuits_explora.ipynb](https://colab.research.google.com/drive/1lnTXl1-zvrIbGpupijxPO7s52uxNJNaz)
- [feature_trees_public](https://colab.research.google.com/drive/19k5r2lNvO1gzL1Zsek3EzJR1vT7sZO4g)
    
    [Feature clustering](Feature%20clustering%207ca3486abbae499b88169916fd33b8df.md) 
    
- ⚠️ find steering vectors for gpt-2-xl L5 and decompose thru SAE
    - L5 only works up to: 1048576/4096000
    - just hook cache L5. the saelens already does this; in the nb it just used exploratory analysis to cache which is not used in the actual training code, so comment that out
    - saelens used a buffer
- 🐣 gpt2Small_pretrained_steering.ipynb
    - load pretrained SAE. See tutorial nb on saelens github
        - ISSUE: there are no pretrained SAEs on MLP layers, only on res stream output layers
    - train SAE on MLP0 of GPT-2 small using A.2 of successor heads paper
- 🐣 GPT2_SAElens_training_MLP0.ipynb
- ✅ [GPT2_SAE_MLP0_seqcont.ipynb](../Locating%20Shared%20Circuits%2045e3959d9536467ba08a6f99a756df79/Project%20Planning%20(quests)%203798a71e7c5d4a888cad9a7d25a1275c.md)
    - ✅ Train it on integers, then see the highest features that light up on mod-10 tokens ending in 3
        
        NOTE: Most important means highest change in output after ablating. But here, we look for highest activations on these tokens. However, this doesn't mean much because certain features may fire highly for all numbers in general! So use the paper's definition of 'most important’
        

Literature Review on Hierarchical Feature Representations across Models

- ✅ read: [https://www.anthropic.com/research/mapping-mind-language-model](https://www.anthropic.com/research/mapping-mind-language-model)
    
    Catch up to Anthropic research on feature clusters for AI Safety
    
    [**Scaling Monosemanticity- Extracting Interpretable Features from Claude 3 Sonnet**](https://www.notion.so/Scaling-Monosemanticity-Extracting-Interpretable-Features-from-Claude-3-Sonnet-3219b222ee8943ac9ba1a07963f975b0?pvs=21) 
    
    helps our research of building towards finding functionally equivalent features across models to define more universal definitions for features that have an effect on behavior
    
    They DIDN’T edit by “similar clusters” yet
    
    https://www.wired.com/story/anthropic-black-box-ai-research-neurons-features/
    
    Dictionary learning can’t identify anywhere close to all the concepts an LLM considers, he says, because in order to identify a feature you have to be looking for it. 
    
    [https://transformer-circuits.pub/2024/scaling-monosemanticity/umap.html?targetId=34m_31164353](https://transformer-circuits.pub/2024/scaling-monosemanticity/umap.html?targetId=34m_31164353)
    
- 🐣 Study: The Geometry of Categorical and Hierarchical Concepts in Large Language Models
    - paper
        
        [The Geometry of Categorical and Hierarchical Concepts in LLMs](https://www.notion.so/The-Geometry-of-Categorical-and-Hierarchical-Concepts-in-LLMs-87f19f9d714c4a44abe7c02441c7c65b?pvs=21) 
        
        [https://news.ycombinator.com/item?id=40643665](https://news.ycombinator.com/item?id=40643665)
        
        [https://news.ycombinator.com/item?id=40640424](https://news.ycombinator.com/item?id=40640424)
        
        [https://x.com/victorveitch/status/1800221324348125617](https://x.com/victorveitch/status/1800221324348125617)
        
        [https://github.com/KihoPark/LLM_Categorical_Hierarchical_Representations](https://github.com/KihoPark/LLM_Categorical_Hierarchical_Representations)
        
        why do you need to prove thm 4 instead of stating it?
        
        if the simplex of elements is orthogonal to the vector repr of animal, since you can steer by vectors, that means you can steer by simplices. but simplices are more “detailed” and changable than vectors. so more precise. if these vectors are orthogonal, we can steer by them as “monosemantic” features?
        
        [The Linear Representation Hypothesis and](https://www.notion.so/The-Linear-Representation-Hypothesis-and-80d9fdf91ca94c51921e60bb8b0806d6?pvs=21) 
        
    - test code
        
        [https://colab.research.google.com/drive/1Kedm4GCSuf087zLXwC4VLPCBAvgp_gpv#scrollTo=Jyok6K5lZh_X](https://colab.research.google.com/drive/1Kedm4GCSuf087zLXwC4VLPCBAvgp_gpv#scrollTo=Jyok6K5lZh_X)
        
        - login and authorize gemma access: [https://huggingface.co/google/gemma-2b](https://huggingface.co/google/gemma-2b)
        - [https://chatgpt.com/c/d81ffb5b-58ea-4748-855a-8d8b94ec5b22](https://chatgpt.com/c/d81ffb5b-58ea-4748-855a-8d8b94ec5b22)
            - float64 is double, float32 is single (or Float). must match
                - [https://stackoverflow.com/questions/60239051/pytorch-runtimeerror-expected-object-of-scalar-type-double-but-got-scalar-type](https://stackoverflow.com/questions/60239051/pytorch-runtimeerror-expected-object-of-scalar-type-double-but-got-scalar-type)
- ✅ one-pg summary pdf to phil based on edited overleaf copy
    - overleaf paper get rid of white space between title and intro if no authors
        
        [https://www.overleaf.com/project/6672b8361d6a3cad2420bafc](https://www.overleaf.com/project/6672b8361d6a3cad2420bafc)
        
        - [https://tex.stackexchange.com/questions/617824/removing-space-after-title](https://tex.stackexchange.com/questions/617824/removing-space-after-title)
- ✅ [todd hamish meeting](todd%20hamish%20meeting%20817a3cdd501f431796470ff8499988c6.md)
- 🐣 run code of “The Geometry of Categorical” on existing data
    - ✅ `estimated_dir = hrc.estimate_cat_dir(train_lemmas, g, vocab_dict)`
        - will only use code from hrc, not loaded from nb, so get rid of hrc when testing pdb (can’t use pdb by modifying code in downloaded repo)
        - you must put all dependent fns from repo to nb if you use newly defined code in nb, since the original repo code calls within hrc lib, but now it won’t find those fns (eg. `category_to_indices`)
        - ipdb> category_embeddings.dtype
        torch.float32
        - this is actually not just pdb, it’s ALL the code, so your changes with `cov.to(dtype=torch.float64)` didn’t take palce despite the error messages showing that in the code. this is because what’s in the files itself wasn’t what `hrc.estimate_cat_dir()` was, given you already imported hrc using `import hierarchical as hrc` and didn’t run that again after modifying the code! that’s why your error messages were also on the wrong line
        - After
        
        ```
        
            category_embeddings = category_embeddings.to(dtype=torch.float64)
        ```
        
        use 
        
        ```
            train_g = train_g.to(dtype=torch.float64)
            test_g = test_g.to(dtype=torch.float64)
        ```
        
         before b_lda in the nb cell
        
    - ✅ email kiho (main author) about code issues
    - explain train lda code
        
        [https://chatgpt.com/c/99e03fb2-6fd2-4a24-a25e-d4fdfe0ccd8f](https://chatgpt.com/c/99e03fb2-6fd2-4a24-a25e-d4fdfe0ccd8f)
        
        - lemmas
            - "run" "runs" "ran" "running"
            
            The lemma for all these words is "run". When the code processes text, it converts all these inflected forms to their lemma to standardize the data.
            
    - modify 1_Animal_explora.ipynb
        - before pass unembed to 2d_plot: `g = [g.to](http://g.to/)(dtype=torch.float64)`
    - explain 1_Animal_explora and plotting
        
        [https://chatgpt.com/c/5c85cf0c-a1a8-4728-9419-10b5a40b347f](https://chatgpt.com/c/5c85cf0c-a1a8-4728-9419-10b5a40b347f)
        
        - explain: **Orthogonalization:** If `orthogonal` is True, make `dir2` orthogonal to `dir1`.
            
            Subtract this scaled vector from dir2 :
            
            `dir2 - (dir2 @ dir1) * dir1`
            
            This removes the component of `dir2` that is in the direction of `dir1`, leaving a vector that is orthogonal to `dir1`.
            
            ![Untitled](Project%20Planning%20b4b05f73d85e409f8409b209e44ed692/Untitled.png)
            
        - are the unembedding vectors the dots?
            
            No, the unembedding vectors are not the dots. The dots represent the projection of tokens (data points) in the vocabulary onto the 2D subspaces defined by the given directions (e.g., \( \bar{\ell}*{animal} \), \( \bar{\ell}*{mammal} \), etc.). The unembedding vectors are used to project these high-dimensional data points onto the 2D plane.
            
            ### Detailed Explanation:
            
            - **Gray Dots:** These indicate all 256K tokens in the vocabulary, projected onto the 2D plane.
            - **Colored Dots:** These represent specific categories such as "animal", "mammal", "bird", and "plant". Each category is projected onto the 2D plane using the directions defined by the corresponding unembedding vectors.
            - **Vectors:** The blue and red vectors shown in the plots (e.g., \( \bar{\ell}*{animal} \), \( \bar{\ell}*{mammal} \), \( \bar{\ell}*{bird} - \bar{\ell}*{mammal} \)) are the directions used to span the 2D subspaces. These directions are derived from the unembedding vectors.
        - where are the unembedding vecs
            
            The unembedding vectors are not directly visible in the plot as individual dots or points; instead, they are the directions (or axes) used to project the high-dimensional data onto the 2D plane. These vectors are represented by the arrows in the plots.
            
            - In the provided plots, the blue and red arrows represent the directions defined by the unembedding vectors.
            - To make interpretation easier, the directions might be orthogonalized, ensuring that the axes (unembedding vectors) are perpendicular to each other.
        - would orthogonalized change the directions of the unemb vectors? wouldnt that make them inacc?
            
            Orthogonalizing the unembedding vectors does indeed change their directions. However, this is done for a specific reason and doesn't necessarily make them inaccurate. Let's delve into why this is the case and how orthogonalization is used appropriately in these contexts.
            
            ### Understanding Orthogonalization
            
            Orthogonalization is the process of making two or more vectors perpendicular (orthogonal) to each other. In the context of the provided code, this is achieved by modifying `dir2` to ensure it is orthogonal to `dir1`.
            
            ### Why Orthogonalize?
            
            1. **Simplifying Interpretations:**
                - Orthogonal vectors are easier to interpret because they ensure that the directions are independent and there is no overlap between the information they represent.
                - In a 2D plot, having orthogonal axes ensures that the plot is more readable and the projections can be interpreted independently along each axis.
                - For example, in the context of the given plots, having orthogonal directions for "animal" and "mammal" ensures that the plot clearly shows the distinction between these categories without one direction interfering with the interpretation of the other.
            
            ### Impact on Accuracy
            
            1. **Context of Use:**
                - The primary context in the provided code is visualization. The orthogonalization is done to improve the interpretability of the 2D projection, not to directly alter the fundamental properties of the unembedding vectors in the model.
                - The modified vectors still retain the essential properties needed for the specific visualization task.
            2. **Preserving Semantic Relationships:**
                - The orthogonalization process involves adjusting `dir2` to be perpendicular to `dir1`, but the key semantic relationships are preserved.
                - The modified `dir2` (now orthogonal to `dir1`) still captures the relevant semantic information but in a way that ensures independence from `dir1`.
        - what do you mean "the key semantic relationships are preserved" if the dirs change?
            
            When I say "the key semantic relationships are preserved," I mean that the essential distinctions and meanings represented by the unembedding vectors are still maintained even after orthogonalization. Let's clarify this concept further.
            
            ### Semantic Relationships and Directions
            
            1. **Original Directions:**
                - The original unembedding vectors (e.g., \( \bar{\ell}*{animal} \), \( \bar{\ell}*{mammal} \)) represent specific semantic concepts in the high-dimensional space.
                - Each direction captures the relationship of the tokens with respect to a particular category or concept.
            2. **Effect of Orthogonalization:**
                - Orthogonalization involves adjusting one vector to be perpendicular to another while retaining the direction's semantic meaning as much as possible.
                - For example, making \( \bar{\ell}*{mammal} \) orthogonal to \( \bar{\ell}*{animal} \) changes the precise direction of \( \bar{\ell}_{mammal} \) but keeps it within the same semantic plane defined by "mammal" and "animal."
            
            ### Preservation of Semantic Relationships
            
            Even though the vectors' directions change during orthogonalization, their roles in distinguishing between different concepts are maintained. Here’s how:
            
            1. **Maintaining Distinctiveness:**
                - The orthogonalized vectors still point towards the regions in the high-dimensional space that distinguish "animal" from "mammal."
                - Although \( \bar{\ell}*{mammal} \) is adjusted to be perpendicular to \( \bar{\ell}*{animal} \), it continues to highlight the concept of "mammal" in a way that is now independent of "animal."
            2. **Independent Axes for Clarity:**
                - By making the vectors orthogonal, we ensure that the projection onto these axes is independent. This means that when projecting a high-dimensional vector onto these axes, the contribution of "animal" is separated from the contribution of "mammal."
                - This separation helps in visualizing and interpreting the semantic contributions more clearly in the 2D space.
            3. **Practical Visualization:**
                - Consider a high-dimensional token that strongly represents a "mammal." Even after orthogonalization, projecting this token onto the orthogonalized \( \bar{\ell}_{mammal} \) will still result in a high value, indicating its strong association with "mammal."
                - Similarly, a token strongly associated with "animal" will project significantly onto the orthogonalized \( \bar{\ell}_{animal} \).
            
            ### Example
            
            ### Before Orthogonalization:
            
            - **\( \bar{\ell}_{animal} \)**: Represents the "animal" concept.
            - **\( \bar{\ell}_{mammal} \)**: Represents the "mammal" concept, which may have some overlap with "animal."
            
            ### After Orthogonalization:
            
            - **\( \bar{\ell}_{animal} \)**: Still represents the "animal" concept.
            - **Orthogonalized \( \bar{\ell}_{mammal} \)**: Represents the "mammal" concept in a direction that is independent of "animal," emphasizing the distinct features of "mammal."
            
            ### Conclusion
            
            Orthogonalization changes the vectors' directions to make them perpendicular, enhancing clarity and interpretability in visualizations. Despite this change, the vectors continue to represent their respective semantic concepts independently. This way, the essential semantic relationships are preserved because the vectors still distinguish between different categories, albeit in a way that ensures their projections are independent and clear in the 2D space.
            
        - so the Unembedding vectors measure how much each token is for a specific vocab or diff of vocab tokens?
            
            Yes, unembedding vectors can be thought of as measuring how much each token corresponds to specific vocabulary items or differences between vocabulary items.
            
        - fig2: why do all red mammal cluster together and are on tail of mammal vector, but the animal blue points are not and are in a line seemingly perpendicular to the animal vector
            
            The clustering of red "mammal" points at the tail of the "mammal" vector indicates a strong, consistent association with the "mammal" category, leading to their tight grouping. In contrast, the spread of blue "animal" points in a line perpendicular to the "animal" vector reflects the diversity of the "animal" tokens and their weaker association with the specific "mammal" direction, resulting in a broader distribution.
            
        - why are the mammal points on top in left plot, but below in middle plot
            
            The mammal points appear higher in the left plot because they project strongly along the "mammal" vector when compared directly with "animal." In the middle plot, they appear lower because the projection axis
            
            ℓˉbird−ℓˉmammal\bar{\ell}_{bird} - \bar{\ell}_{mammal}
            
            ℓˉbird−ℓˉmammal emphasizes the distinction between birds and mammals, which positions mammal points closer to the origin or lower, reflecting their alignment with the mammal concept and divergence from bird-specific characteristics.
            

Observe how steering affects features downstream

- 🐣 review existing code
    - [gpt2Small_pretrained_steering.ipynb](https://colab.research.google.com/drive/1IUtIe0D6UBAJYlPC4eJl00l8fmpohhKG)
    - [steer_vector_SVD_interp.ipynb](https://colab.research.google.com/drive/1fNOEHkxf1nvah0aC68AcYJgiHqvKP3k9)
    - GPT2_SAE_MLP0_seqcont_explora_v1.ipynb
        - **Find features that actv highest for sample X**
    - [GPT2_SAE_MLP0_seqcont_explora_v2.ipynb](https://colab.research.google.com/drive/1fxFZynvhH0IkvE2WzUWUAqntQY4h7s5G)
- 🐣 use gpt-2 small; regardless of whether steering does anything or features correspind to anything, just observe how it affects feature neurons from layer to layer
    - use existing saes but new contrastive vectors. add vectors then hook the output of features in later layers. get the top changes
    - interpret using dataset examples
- ✅ ask about openai credits
    
    Hi did you see the proposal fazl gave as an example to get openai training credits? I was looking to see if
    
    I may start working with small toy models, so would be hard to estimate the budget for now (to say train saes on interpreting larger models). Looks like it would be helpful to know the dataset size to get the number of tokens needed; i'd look to see if I can estimate how this translates to activations to train saes, and decide if i can get an estimate to send a proposal or not
    
    actually this is only for openai api access, not llama, so you dont need it for saes
    
    only need it if doing auto interp by gpt4
    
    train saes on tvg servers
    

Run code of “The Geometry of Categorical” on new data related to behavior

- ✅ email kiho on project ideas
    
    have been thinking about trying to find other universal patterns across models on how it differentiates related, hierarchical concepts (eg. animal to mammal, as described in your paper).
    
    It seems that there should be composable abstract patterns that these concepts have in common, but it does not appear trivial to locate precisely, and a lot of approaches are transforming activations into monosemantic features, in which an entire neuron represents "golden gate bridge" rather than composing "bridge" with more specific traits (though the sparse feature circuits paper is along the lines of how these features can be composed). Lastly, I am interested to see if these concepts that can be identified by feature relations (similar to the simplices in your paper) can be used for AI safety steering.
    
    As I am planning the feasible scope of this project, I was wondering if you have looked into this before, given that you have studied relations between hierarchical concepts, and if you have found 1) any dead ends I should avoid, or 2) have recommendations on what to look into (that you are not also looking into)?
    
    I am also looking for quick critiques on approaches I am looking to try. For instance, would it make sense to try to use SAEs to find feature circuits that may compose hierarchical concepts? Or would it not be guaranteed that an SAE would find composable features? I hypothesize the model is using relations between features to differentiate concepts, but it is hard to interpret this from activations.
    
    I meant steering by adding and subtracting via hierarchies (would it make sense to say "adding by simplices"?) In addition to activation addition, there is a paper "Successor Heads" that learns linear maps to extract a months_feature from February, and an ordinal_feature_4 from Thursday, then can perform  months_feature +  ordinal_feature_4 to get April. I was wondering if you think this can be generalized?
    
- ✅ msg constantin on succsesor heads
    
    This paper might be relevant to  your work on sequences: [https://arxiv.org/pdf/2312.09230](https://arxiv.org/pdf/2312.09230)
    
    I was looking to find more precise ways of steering by adding abstractions, and this successor heads paper found it could train linear maps to extract a months_feature from February, and an ordinal_feature_4 from Thursday, then can perform months_feature + ordinal_feature_4 to get April.
    
    Might be useful if you want to go over it sometime to critique if it is a good approach to generalize, I'm also reproducing some of its code now as its code is not available
    

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
            3. Patch back in feature ablated in later l
                - Put SAE reconstructions back into model
                    - See: [GPT2_SAE_MLP0_seqcont_explora_v2](https://colab.research.google.com/drive/1fxFZynvhH0IkvE2WzUWUAqntQY4h7s5G#scrollTo=K-wGX_O3xaH9).ipynb
        
        ISSUE: how to identify analogous F1 and F2 across models?
        
    
    [gpt2Small_pretrained_steering.ipynb](https://colab.research.google.com/drive/1IUtIe0D6UBAJYlPC4eJl00l8fmpohhKG)
    
    - NOTE: pretrained use SAELens (which is built on transformerlens), and cache uses transformerlens. Only need to combine saes with tl for step 4
    - 🐣 get contrastive activations for 2 prompts of gpt-2
        - [hierConcepts_logitLens_llama2.ipynb](https://colab.research.google.com/drive/1sUeugm0DLrE_c8NAZy06XETeKdtwizWE#scrollTo=2UdLBhJPkFkf)
            - pass them both in batch, then take actvs of each batch index
    - For third prompt, apply steering vector at layer k
        - hook fn to add? look at prev repos how they did it
        - `activation_additions` (turner et al repo) \ `activation_additions \ hook_utils.py`
            - `hook_fns_from_activation_additions`
        - find also recent papers doing steering to see if they use easier way
            - [https://www.lesswrong.com/posts/ndyngghzFY388Dnew/implementing-activation-steering](https://www.lesswrong.com/posts/ndyngghzFY388Dnew/implementing-activation-steering)
            

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