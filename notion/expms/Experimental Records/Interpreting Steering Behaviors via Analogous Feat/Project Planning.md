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
        

Catch up to Anthropic research on feature clusters for AI Safety

- ✅ read: [https://www.anthropic.com/research/mapping-mind-language-model](https://www.anthropic.com/research/mapping-mind-language-model)
    
    [**Scaling Monosemanticity- Extracting Interpretable Features from Claude 3 Sonnet**](https://www.notion.so/Scaling-Monosemanticity-Extracting-Interpretable-Features-from-Claude-3-Sonnet-3219b222ee8943ac9ba1a07963f975b0?pvs=21) 
    
    helps our research of building towards finding functionally equivalent features across models to define more universal definitions for features that have an effect on behavior
    
    They DIDN’T edit by “similar clusters” yet
    
    https://www.wired.com/story/anthropic-black-box-ai-research-neurons-features/
    
    Dictionary learning can’t identify anywhere close to all the concepts an LLM considers, he says, because in order to identify a feature you have to be looking for it. 
    
    [https://transformer-circuits.pub/2024/scaling-monosemanticity/umap.html?targetId=34m_31164353](https://transformer-circuits.pub/2024/scaling-monosemanticity/umap.html?targetId=34m_31164353)
    

- impt papers measuring analogous features
    - platonic repr hypothesis
    - similarity survey (2023)
    - successor heads
    - func eqv features

[Similarity measurements](Project%20Planning%20b4b05f73d85e409f8409b209e44ed692/Similarity%20measurements%2059d99860501849cfb9960f028265819b.md)

Steer by feature relations of distance or causal. This is true steering by concepts. Concepts are captured by a network of features, not a single feature. A bridge vs golden gate Bridge. In that case, it's not saes. 

Kernel is distance between samples, not features

Structure preserving feature relations

Feature must be at some threshold 

Sim measure within model between hierarchical analogous concepts

Trace backwards single token inputs or two contrasting differing by single input. Measure the feature dim for traits along each. Do this for both neurons, sae features, components. Then measure distances between these features. Is there a pattern?

Ask gpt4 to critique and refine this

Issue is hard to isolate commonality. What if more than one commonality? Even for vision models. For text, there's position. But sample at many pos, many contexts and they have commonality. If use synonymous tokens or of Same class.

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