# Find Research Topics + Prelim Expms

Meandering to find research topics

- ✅ Compare the inputs of Function Vector’s ICL prompts vs Machiavelli Benchmark prompts.
    
    [https://arena3-chapter1-transformer-interp.streamlit.app/[1.5]_Function_Vectors_&_Model_Steering](https://arena3-chapter1-transformer-interp.streamlit.app/%5B1.5%5D_Function_Vectors_&_Model_Steering)
    
    [https://colab.research.google.com/drive/1yuPIBfz2MO2bHLuIkJETCemJU8TRKZLT#scrollTo=2724827c](https://colab.research.google.com/drive/1yuPIBfz2MO2bHLuIkJETCemJU8TRKZLT#scrollTo=2724827c)
    
    - How are function vectors extracted?
        
        You need a “good” set of prompts eg) antonym pair prompts would beget antonym FV. For Machiavelli, this would be “ethical” prompts.
        
    - How similar are they?
    - Can function vectors be extracted from a forward pass of machiavelli prompts?
        
        The ethical prompts would have in-context examples of ethical decisions. They have an observation with actions. So ethical prompts just have the ethical action.
        
- ✅ Literature review on machiavelli to avoid repeating work:
    
    [https://scholar.google.com/scholar?cites=4697205417656837392&as_sdt=5,31&sciodt=0,31&hl=en](https://scholar.google.com/scholar?cites=4697205417656837392&as_sdt=5,31&sciodt=0,31&hl=en)
    
- ✅ [model_edit_deception_draft.ipynb](https://colab.research.google.com/drive/1AgTC7ebuZGVJTdh5b4FG9Yu-M0RxdKB0)
- ✅ Read [Sleeper Agents](https://www.notion.so/Sleeper-Agents-247200c8dddf4fecbdee86e8a611bed2?pvs=21)
- 🐣 How did previous papers generate data?
- ✅ machiavelli pip install reqs issue: [https://github.com/aypan17/machiavelli/issues/14](https://github.com/aypan17/machiavelli/issues/14)
    
    occurs with both python 3.8 and 3.12, miniconda and conda
    
    - not avail on windows
        
        The error you're encountering during the installation process is due to the **`sh`** library trying to import the **`fcntl`** module, which is not available on Windows. The **`fcntl`** module is specific to Unix-like systems (Linux, macOS, etc.) and provides an interface to file control operations. The **`sh`** library is primarily designed for Unix-like systems, hence the issue when trying to run it on Windows.
        
- ✅ Create- [Project Proposal](../../Project%20Proposal%20f68a82cc910f4a7c98cafbcb52b07fa5.md)
- ✅ Create- [Networking ](../../Networking%205eb6990dfeee475b920112de369de0ab.md)
- ✅ Run machiavelli in colab: [https://colab.research.google.com/drive/1hqzY4HGVOfzcHsUZczabSOpwiBXVlkkJ#scrollTo=QtsZfKsVFyDY](https://colab.research.google.com/drive/1hqzY4HGVOfzcHsUZczabSOpwiBXVlkkJ#scrollTo=QtsZfKsVFyDY)
    
    The most simple way to upload a folder onto Google Colab is to **create a .** **zip file of the folder on our local machines and then upload it as a file on Colab**.
    
- ✅ Find where the agent data is located in Machiav repo
    
    [demo.py](http://demo.py) → from machiavelli.agent.load_agent import load_agent → lm_agents.py
    The models are just gpt3 or gpt4 with instruction prompts. So not interpretable like llama
    
    ```python
    if model in ['davinci', 'text-davinci-002', 'text-davinci-003']:
                self.is_chat_model = False
    elif model in ['gpt-3.5-turbo', 'gpt-4']:
    ```
    
- ✅ Can we use Llama for Machiavalli instead? Yes; Appendix K shows llama-2 finetuned was used in Machiavelli (but lm_agents.py doesn’t have llama as an option?)
    - fine tuning llama2 resources
        
        Can fine tuning llama 2 be done using an A100 on colab? If not, how to do it using other resources an individual can buy? Research: [https://github.com/tatsu-lab/stanford_alpaca#fine-tuning](https://github.com/tatsu-lab/stanford_alpaca#fine-tuning)
        
        - chatgpt answer
            
            Fine-tuning LLaMA 2 using an A100 on Colab may not be directly feasible due to limitations in hardware resources provided by Colab, which typically offers T4 GPUs with 16 GB of VRAM. This amount of VRAM is barely enough to store the weights of smaller LLaMA models, making full fine-tuning challenging without resorting to parameter-efficient techniques like LoRA or QLoRA. These techniques allow for fine-tuning by adding a small number of trainable parameters to a largely frozen, pre-trained model, thus reducing the VRAM and computational requirements【5†source】【6†source】.
            
            To fine-tune LLaMA 2 models using more accessible resources, you can follow a detailed guide that involves several steps, including setting up your environment with necessary libraries (like `accelerate`, `peft`, `bitsandbytes`, and `transformers`), loading the model and tokenizer from Hugging Face, preparing your dataset, and applying 4-bit quantization via QLoRA for efficient fine-tuning on consumer hardware. This approach dramatically reduces the VRAM requirements and makes it possible to fine-tune large language models on machines with limited resources【5†source】.
            
            For individuals looking to fine-tune LLaMA 2 models using their own resources, it's advisable to invest in hardware that can support the computational and memory requirements of large language models. An NVIDIA A100 GPU is indeed a powerful choice for such tasks, offering substantial improvements in memory and compute capacity compared to the GPUs available on Colab. When using an A100 or similar high-end GPU, you can follow fine-tuning tutorials that leverage datasets like the Databricks Dolly 15k dataset, which is designed for fine-tuning large language models. This process involves loading and preprocessing the dataset, applying parameter-efficient fine-tuning techniques, and training the model with a focus on efficiency and minimizing computational overhead【6†source】.
            
            For those unable to use Colab's A100 for direct fine-tuning, cloud-based AI platforms or dedicated GPU servers rented from cloud providers could be viable alternatives. These platforms often offer a range of GPU options, including the A100, and are capable of handling the demands of fine-tuning large models like LLaMA 2. When opting for these services, you'll benefit from the scalability and flexibility they offer, allowing for efficient resource management and potentially reducing the cost associated with fine-tuning large language models.
            
        - So an A100 can work?
            
            Yes. Using an A100 for fine-tuning involves leveraging its advanced capabilities, such as high-bandwidth memory (HBM2), which can significantly speed up data transfer rates and processing times, and its support for mixed-precision training, which can further enhance performance and efficiency by allowing computations to be performed in both 32-bit (float32) and 16-bit (float16) precision. This is particularly useful for training large models as it can reduce memory consumption and accelerate training times without a significant loss in model accuracy or performance.
            
    - ask authors in email
        
        
    
    LM is language model, DRRN is RL model
    
    But the lm_agent.py file doesn’t have them as an option; it only loads gpt models using openai_helpers.py
    
- 🐣 Run prelim experiments for fine tuning interp on fine-tuned LLAma models + machiav
    - ISSUE: machiav ISN’T fine tuned, it’s given prompts. So its interpretability has nothing to do with fine tuning training, only in-context prompts.
- ⚠️ Write up 1-page proposal for sleeper agents using fine tuned llama as proof of concept
    - [Sleeper Agents Replication](../../Old%20docs%201a3cbae85bf64adf94fee4aade63548b/Sleeper%20Agents%20Replication%205e70a34eff91418d851d1725584a9a0c.md)
    - Email authors to ask about replication issues
    - ISSUE: the paper states they are already working on interpreting sleeper agents
- ✅ [Brainstorm- related behavior](../../Brainstorm-%20related%20behavior%20588d73c1315d48e3bb7db26038712fd8.md)
    - Check the novelty. Do existing behavior/concept papers not talk about hierarchical concepts/related behavior? Look at what cites papers of this topic and their related work.
    - Find datasets on behavior and check if interp done on those datasets before
        - Machiavelli
        - CAA
- ✅ Update overleaf with new plan
    
    [https://www.overleaf.com/project/6595bd526fe1eee6f40a8e4c](https://www.overleaf.com/project/6595bd526fe1eee6f40a8e4c)
    
- ⚠️ Code to steer activations from Machiav and CAA ethical datasets
    - [Editing Machiavelli Prelims](../../Old%20docs%201a3cbae85bf64adf94fee4aade63548b/Editing%20Machiavelli%20Prelims%20a0708db298d544b388375641494a755f.md)
    - Copy + paste ONE prompt from Machiavelli with TWO choices into CAA nnsight (bc storage)
        
        CAA repl: [Project Planning](../../../ARENA%20notes%201a8ff2624cff486e9d91b13139420026/CAA%20Replication%20c7062646b89f46b2b623d72f722a7902/Project%20Planning%207fb9304394ea4a728098c812a60d7034.md) 
        
    - machiavelli.ipynb
    - ⚠️ steer_machiav_draft.ipynb
        - ISSUE: nnsight model gen
        - ask question to server and caden
            
            ![Untitled](Find%20Research%20Topics%20+%20Prelim%20Expms%20cb0481999aa04ff6a92e5859837c3508/Untitled.png)
            
        - nnsight server soln
            
            ![Untitled](Find%20Research%20Topics%20+%20Prelim%20Expms%20cb0481999aa04ff6a92e5859837c3508/Untitled%201.png)
            
        - ISSUE: **ValueError: You have to specify either input_ids or inputs_embeds!**
            
            [https://github.com/huggingface/transformers/issues/3626](https://github.com/huggingface/transformers/issues/3626)
            
- ✅ Get CAA activations using original code and decompose into features
    
    CAA has been updated. Look at new repo’s `generate_vectors`
    
    [CAA_get_actvs_explrTests_v1.ipynb](https://colab.research.google.com/drive/1a0n70XzpTdPr5UMEILzIBrrRhyAFvWJC)
    
    `model.model.model.layers[15].activations`
    
    - ✅ logit lens
        - first check final logits are unembed corr before unembed intr feats
        - check its shape is corr
        - try layer norm before unembed
    - ✅ SVD on actvs, then unembed singular vectors
        - [https://github.com/BerenMillidge/svd_directions](https://github.com/BerenMillidge/svd_directions)
        - We are mixing code from svd_directions and CAA. Not transformelns
            - find other papers that directly apply pca/svd on actvs, such as gpt-2 gt
            - check llama 2 unembedding in assoc concepts
    - ✅ decompose steering vector
    - [SVD explora tests](../../SVD%20explora%20tests%20e685dd8723454c0fbaed4e0d19478fd9.md)
    - ✅ double check nb code and understand why for most of it
- ✅ send progress of nbs
    
    make new public sharing folder with new nbs. call it _revised
    
    - activation differences (using transformerlens cache)
    - SVD logit lens unembedding
    - steering using nnsight (solves memory issues)
        - CAA and function steering
        
- 🐣 [[CAA_SAE_explrTests_v1.ipynb](https://colab.research.google.com/drive/1rv8d3VJBSLxtSbFGq1809VZB1BGPGiZe)](../../CAA_SAE_explrTests_v1%20ipynb%20ac477af8bdf54dc5bdf057884cfe0c2b.md)
    - SAE_template
- ✅ read “sparse feature circuits”
    
    it is good to know that something similar to the high level idea I have has a feasible implementation. Given that one can modify behavior by modifying its feature circuits (shown in the paper), one can study these feature-behavior relations in more detail and study how modifying one behavior modifies another behavior (entangled behavior) and how to de-tangle them
    
- cont: 🐣 [[CAA_SAE_explrTests_v1.ipynb](https://colab.research.google.com/drive/1rv8d3VJBSLxtSbFGq1809VZB1BGPGiZe)](../../CAA_SAE_explrTests_v1%20ipynb%20ac477af8bdf54dc5bdf057884cfe0c2b.md)
- ✅ create: [Brainstorm- AlgTop Actvs ](../../Brainstorm-%20AlgTop%20Actvs%20f2894d4bd51247a88c0de5251754dc31.md)
    - ✅ Read papers + lectures on Mapper
    - ✅ Hatcher Ch0
    - ✅ [email- why algtop needed](../../Networking%205eb6990dfeee475b920112de369de0ab/email-%20why%20algtop%20needed%2090a8057d0f47426f848c74b01f797949.md)
- 🐣 [Brainst- AlgTop Present, draft 1](../../Brainst-%20AlgTop%20Present,%20draft%201%206e9000b30efc4c09ad0dd28f05dbfba7.md)
    - Outline: Why Mapper solves interp/editing issue
        - Take solns from sim papers + guess how they can be used for MI
        - Read more papers on TDA that use the edges
            - Find papers that use mapper which utilize the edges in their analysis
                
                I found some interesting papers that utilize the Mapper algorithm and incorporate edge analysis in their studies:
                
                1. **Topological Data Analysis for COVID-19**: A study applies the Mapper algorithm to visualize and analyze the spread of COVID-19 in the U.S. The paper discusses the utility of Mapper graphs in understanding the pandemic across time and space, highlighting the importance of connected components and branches within these graphs. These components and branches help identify COVID-19 hotspots and their development over time. This application of the Mapper algorithm does not solely rely on statistical methods but focuses on the geometry and topology of the data, providing a novel perspective on epidemiological data analysis【5†source】.
                2. **TDAview**: This tool offers an online visualization for topological data analysis, allowing users to define edge color or infer it from node color, and to display labels showing the number of common points between two linked nodes. It supports exporting Mapper graphs to various formats, facilitating the analysis of the topological structures formed by data points【6†source】.
                3. **Learning a Cover in the Mapper Construction**: A paper introduces an approach to optimizing the cover of a Mapper graph by focusing on the selection of the cover parameter. The study demonstrates the Mapper algorithm's application to a toy dataset, showing how the construction process involves choosing a lens function, cover, and clustering algorithm to generate a graph that accurately reflects the structure of the dataset. This process highlights the importance of edge connections in understanding the dataset's topological features【7†source】.
                
                These papers demonstrate diverse applications of the Mapper algorithm, emphasizing the analysis of edges in the resulting graphs to understand complex datasets better. They cover areas from epidemiology to optimizing the algorithm's parameters for more accurate data representation, showing the versatility and depth of analysis possible with this approach.
                
- 🐣 [Brainst- Proj Present 1](../../Brainst-%20Proj%20Present%201%202383a603b271491c84199a41da57b600.md)
- 🐣 GPT2_TL_SAE_training_v1
    
    [[CAA_SAE_explrTests_v1.ipynb](https://colab.research.google.com/drive/1rv8d3VJBSLxtSbFGq1809VZB1BGPGiZe)](../../CAA_SAE_explrTests_v1%20ipynb%20ac477af8bdf54dc5bdf057884cfe0c2b.md) 
    
    - ✅ Modify `n_input_ae` and `n_hidden_ae` to use gpt2 dims
    - ✅ Modify training data to use GPT-2’s activations, then train
    - 🐣 Train with more batches and SAE instances
- ✅ [Brainstorm- extend sv to eqv classes](../../Brainstorm-%20extend%20sv%20to%20eqv%20classes%20e8e8d62ec04a43e78d6df5b52ab6020d.md)
- ✅ finish slides
- ✅ learn about concurrent work
    
    [https://www.alignmentforum.org/posts/HpAr8k74mW4ivCvCu/progress-update-from-the-gdm-mech-interp-team-summary](https://www.alignmentforum.org/posts/HpAr8k74mW4ivCvCu/progress-update-from-the-gdm-mech-interp-team-summary)
    
    [https://www.alignmentforum.org/posts/C5KAZQib3bzzpeyrg/progress-update-1-from-the-gdm-mech-interp-team-full-update#3__Improving_the__Anger__Steering_Vector](https://www.alignmentforum.org/posts/C5KAZQib3bzzpeyrg/progress-update-1-from-the-gdm-mech-interp-team-full-update#3__Improving_the__Anger__Steering_Vector)
    
    Interpreting steering vectors using SAEs is very interseting work! I had just wrote a proposal to start this, but looks like it's already been done. I'll see if there's anything I can build on
    
    Thanks for the heads up! Just to ensure I don't pursue something with too much overlap, would your future work be related to circuits? If so I will probably decide upon another direction in this area.
    I just read the blog post and it was very helpful for finding evidence that there is some "features vs noise" within steering vectors, which I'd only hypothesized on last week after reading how CAA improved on actadd with larger/more varied datasets, and was going to try, so now it's good that there's some validation!
    
    I just learned that Google Deepmind (Neel Nanda, etc.) had already tackled the work I was going to do for my project, steering vector interpretability via SAE features and finding how to improve steering vectors using interpretability. It's already happened that several times I'm working on something and then I realize a bigger group had already done it, but I guess there's pros/cons to this.
    The cons is that this work has now been done before, but the pros is that it works, plus there are other approaches I can think of that were not done before. So the new direction is to build upon that existing work using the new approaches, though this would prob take longer as these as less low hanging fruit than just interpreting steering with saes. I would be interested in talking to anyone who is also interested in this direction.
    
    From the blog post:
    We find a single SAE feature for anger which is a Pareto-improvement over the anger steering vector from existing work. We have more mixed results with wedding steering vectors: we can partially interpret the vectors, but the SAE reconstruction is a slightly worse steering vector, and just taking the obvious features produces a notably worse vector. We can produce a better steering vector by removing SAE features which are irrelevant
    One of my main aims was improving the anger vector by removing certain SAE features, and they did the exact same thing; I wasn't sure if my approach would've worked but now I have evidence it does! Neel said there's still a lot of work not done yet that they'll work on. I was thinking of interpreting how steering vectors affect feature circuits, which may improve selecting features- note their blog post states the wedding vector was not improved upon, so perhaps this can be done. So if anyone is also thinking of talking/working on that, let me know. Hopefully this work won't be also done by Deepmind too
    

**EXPM**: Reproduce SAE decomposition on Llama-2 CAA & Successor Heads

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
        
- ✅ [JBloom May SAE workshop](../../SAE%206b08b4ad57a342bf9393d2ef0fa31c6b/Training%20tips%2097054f2568c04b06910600e546c60b99/JBloom%20May%20SAE%20workshop%20fe2e004ec02742a88a0c5a6ec61d7415.md)
- ✅ [Patching](../../Patching%20c56dd40648f24f1c9095c38f63d50333.md)
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
    
    [Compute](../../Compute%20e3182612433a4299b4035d5359548fa4.md) 
    
    - [https://arena3-chapter0-fundamentals.streamlit.app/](https://arena3-chapter0-fundamentals.streamlit.app/)
        
        scroll down to “**System Requirements” and “Virtual Machines”**
        
    
    The GPUs on vast.ai, lambda labs are less powerful than colab pro+
    
- 🐣 sparse feature circuits: find relations between features
    
    [sparse feature circs explora](../../sparse%20feature%20circs%20explora%2000b39c6ce28e41f991fb17801204ec9d.md) 
    
    - ✅ Run README bash code to get and eval circs: [sparse_feature_circuits_explora.ipynb](https://colab.research.google.com/drive/1lnTXl1-zvrIbGpupijxPO7s52uxNJNaz)
- [feature_trees_public](https://colab.research.google.com/drive/19k5r2lNvO1gzL1Zsek3EzJR1vT7sZO4g)
    
    [Feature clustering](../../Feature%20clustering%207ca3486abbae499b88169916fd33b8df.md) 
    
- ⚠️ find steering vectors for gpt-2-xl L5 and decompose thru SAE
    - L5 only works up to: 1048576/4096000
    - just hook cache L5. the saelens already does this; in the nb it just used exploratory analysis to cache which is not used in the actual training code, so comment that out
    - saelens used a buffer
- 🐣 gpt2Small_pretrained_steering.ipynb
    - load pretrained SAE. See tutorial nb on saelens github
        - ISSUE: there are no pretrained SAEs on MLP layers, only on res stream output layers
    - train SAE on MLP0 of GPT-2 small using A.2 of successor heads paper
- 🐣 GPT2_SAElens_training_MLP0.ipynb
- ✅ [GPT2_SAE_MLP0_seqcont.ipynb](../../../Locating%20Shared%20Circuits%2045e3959d9536467ba08a6f99a756df79/Project%20Planning%20(quests)%203798a71e7c5d4a888cad9a7d25a1275c.md)
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
- ✅ [todd hamish meeting](../../todd%20hamish%20meeting%20817a3cdd501f431796470ff8499988c6.md)
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
            
            ![Untitled](Find%20Research%20Topics%20+%20Prelim%20Expms%20cb0481999aa04ff6a92e5859837c3508/Untitled%202.png)
            
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

- ✅ understand `store_matrices.py`
    
    In “Linear Repr Hyp” paper, gamma (umembedding into output space) is transformed into g using the causal inner product by “unifying” it with the input (embedding) space prompt. This g is calculated by equation 3.8, and is the g of this code.
    
    In `1_Animal`, this g is used to obtain the condition in equation 4.1- g(relevant item in category) has similarity with the linear repr of the concept in category, but is orthogonal to irrelevant concepts
    
    `animals_g` is a dict of concept:tensor that takes a slice from  `g`, which is a tensor of shape `[256000, 2048])` , and puts it in in the concept. So g must have first index be vocab,  animals_g['mammal'].shape is `([194, 2048])`, it’s possible that’s 194 different animals? It’s different from animals_g['bird'].shape, which is`([115, 2048])`. So this first number is specific to each key in animals. 
    
    But g is just direction, not a vector with magniutde. So we need to use `estimate_cat_dir`
    
    `animals_token.keys()` : `dict_keys(['mammal', 'bird', 'reptile', 'fish', 'amphibian', 'insect'])`
    
    So there are only 6 categories of animals, and indeed, the first idnex of animals_g are types of those animals: `animals_token['mammal'][0:5]` is `['▁beaver', '▁Beaver', '▁panther', '▁Panthers', '▁Panther']`
    
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
    
- brainstorm why this approach can be useful
    
    Questions about research to pass- if not, weaker justification for doing it
    
    - ✅ msg andy zou and 1st author of ref vec on why steering is useful
        
        Hi, I read your paper on Representation Engineering and had questions about how model steering would be used in practice, as I'm working in a summer research internship with the TVG group at University of Oxford now and am looking to do work in model steering. However, I am trying to justify in a proposal why it would be useful in practice.
        
        In practice, say we want a model to refuse user behavior. We can use the steering vector during inference time for certain inputs, or all inputs. But can we just detect the user input + model output (not shown to the user yet) using another model or algorithm, and just not go through with the request?
        
        I think for other behaviors such as sycophancy it might make more sense though. But I was wondering why use the refusal vector over just not going through with a request that can be detected as harmful through other means? Thank you.
        
        My guesses for why to use steering would be:
        
        1) It may not be possible to perfectly detect what are bad / good outputs every time, so steering is an extra safety net
        
        2) We may still want the model to output something, so not throw everything out that’s good just because there’s some bad
        
        For comparing steering vs fine tuning, I think of 3 reasons: it’s cheaper, more interpretable, and more precise (less side effects, more predictable). 
        
    - Do steering communities care about steering specifics (which can be done by composing)? Justify its use in AI safety
        
        
    - why feature decomposition can’t just be found via model splitting?
    - do features across layers, like a circuit, influence behavior?
    - When steering is used, the steering vector may be used for every user input. But why not just detect the input beforehand (using another model or algorithm to measure output) and not have the model output anything?
    - Preserve invariant structure while changing style is useful for img2img, but what about text?
    - The points about steering’s flaws from (Relational Composition) seem speculative.
    - If care about specifics, why not just not steer on certain specific inputs? What about multiple steering vectors?
    - How is steering even used in deployment? Is it just used on all inputs?
- ✅ ask neel for updates on steering vec decomp
    
    Hi, it's been a while since I last thought about this topic as I was working on other research projects, but without giving out details, I was wondering if it's possible to say if decomposing steering vectors has since led to any promising results, or if it hasn't really been continued? New papers such as Refusal Vector seem to do really well with just difference-of-means and I'm guessing decomposition may have been tried on the refusal vector too. Just asking to see if this is a good avenue to pursue still or not
    
- ✅ **Editing Model Behavior, Proposal Brainstorm v1**
    
    [https://www.overleaf.com/project/6672b8361d6a3cad2420bafc](https://www.overleaf.com/project/6672b8361d6a3cad2420bafc)
    
- ✅ make slides
    
    [https://docs.google.com/presentation/d/1-FK73_RLgU6X3TkWdJmvPo-omlMVQ2bi532wXapvrC8/edit#slide=id.g2153ba3b593_0_372](https://docs.google.com/presentation/d/1-FK73_RLgU6X3TkWdJmvPo-omlMVQ2bi532wXapvrC8/edit#slide=id.g2153ba3b593_0_372)
    
    [https://chatgpt.com/c/391f2a1f-ed25-4997-b2d3-aa457dabf2c9](https://chatgpt.com/c/391f2a1f-ed25-4997-b2d3-aa457dabf2c9)
    
    [https://lucid.app/](https://lucid.app/)