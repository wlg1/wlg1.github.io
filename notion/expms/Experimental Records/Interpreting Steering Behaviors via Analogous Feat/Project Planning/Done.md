# Done

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
        
- ✅ Create- [Project Proposal](../Project%20Proposal%20f68a82cc910f4a7c98cafbcb52b07fa5.md)
- ✅ Create- [Networking ](../Networking%205eb6990dfeee475b920112de369de0ab.md)
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
    - [Sleeper Agents Replication](../Sleeper%20Agents%20Replication%205e70a34eff91418d851d1725584a9a0c.md)
    - Email authors to ask about replication issues
    - ISSUE: the paper states they are already working on interpreting sleeper agents
- ✅ [Brainstorm- related behavior](../Brainstorm-%20related%20behavior%20588d73c1315d48e3bb7db26038712fd8.md)
    - Check the novelty. Do existing behavior/concept papers not talk about hierarchical concepts/related behavior? Look at what cites papers of this topic and their related work.
    - Find datasets on behavior and check if interp done on those datasets before
        - Machiavelli
        - CAA
- ✅ Update overleaf with new plan
    
    [https://www.overleaf.com/project/6595bd526fe1eee6f40a8e4c](https://www.overleaf.com/project/6595bd526fe1eee6f40a8e4c)
    
- ⚠️ Code to steer activations from Machiav and CAA ethical datasets
    - [Editing Machiavelli Prelims](../Editing%20Machiavelli%20Prelims%20a0708db298d544b388375641494a755f.md)
    - Copy + paste ONE prompt from Machiavelli with TWO choices into CAA nnsight (bc storage)
        
        CAA repl: [Project Planning](../../ARENA%20notes%201a8ff2624cff486e9d91b13139420026/CAA%20Replication%20c7062646b89f46b2b623d72f722a7902/Project%20Planning%207fb9304394ea4a728098c812a60d7034.md) 
        
    - machiavelli.ipynb
    - ⚠️ steer_machiav_draft.ipynb
        - ISSUE: nnsight model gen
        - ask question to server and caden
            
            ![Untitled](Done%201c002201437341e48b55b8276859a632/Untitled.png)
            
        - nnsight server soln
            
            ![Untitled](Done%201c002201437341e48b55b8276859a632/Untitled%201.png)
            
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
    - [SVD explora tests](../SVD%20explora%20tests%20e685dd8723454c0fbaed4e0d19478fd9.md)
    - ✅ double check nb code and understand why for most of it
- ✅ send progress of nbs
    
    make new public sharing folder with new nbs. call it _revised
    
    - activation differences (using transformerlens cache)
    - SVD logit lens unembedding
    - steering using nnsight (solves memory issues)
        - CAA and function steering
        
- 🐣 [[CAA_SAE_explrTests_v1.ipynb](https://colab.research.google.com/drive/1rv8d3VJBSLxtSbFGq1809VZB1BGPGiZe)](../CAA_SAE_explrTests_v1%20ipynb%20ac477af8bdf54dc5bdf057884cfe0c2b.md)
    - SAE_template
- ✅ read “sparse feature circuits”
    
    it is good to know that something similar to the high level idea I have has a feasible implementation. Given that one can modify behavior by modifying its feature circuits (shown in the paper), one can study these feature-behavior relations in more detail and study how modifying one behavior modifies another behavior (entangled behavior) and how to de-tangle them
    
- cont: 🐣 [[CAA_SAE_explrTests_v1.ipynb](https://colab.research.google.com/drive/1rv8d3VJBSLxtSbFGq1809VZB1BGPGiZe)](../CAA_SAE_explrTests_v1%20ipynb%20ac477af8bdf54dc5bdf057884cfe0c2b.md)
- ✅ create: [Brainstorm- AlgTop Actvs ](../Brainstorm-%20AlgTop%20Actvs%20f2894d4bd51247a88c0de5251754dc31.md)
    - ✅ Read papers + lectures on Mapper
    - ✅ Hatcher Ch0
    - ✅ [email- why algtop needed](../Networking%205eb6990dfeee475b920112de369de0ab/email-%20why%20algtop%20needed%2090a8057d0f47426f848c74b01f797949.md)
- 🐣 [Brainst- AlgTop Present, draft 1](../Brainst-%20AlgTop%20Present,%20draft%201%206e9000b30efc4c09ad0dd28f05dbfba7.md)
    - Outline: Why Mapper solves interp/editing issue
        - Take solns from sim papers + guess how they can be used for MI
        - Read more papers on TDA that use the edges
            - Find papers that use mapper which utilize the edges in their analysis
                
                I found some interesting papers that utilize the Mapper algorithm and incorporate edge analysis in their studies:
                
                1. **Topological Data Analysis for COVID-19**: A study applies the Mapper algorithm to visualize and analyze the spread of COVID-19 in the U.S. The paper discusses the utility of Mapper graphs in understanding the pandemic across time and space, highlighting the importance of connected components and branches within these graphs. These components and branches help identify COVID-19 hotspots and their development over time. This application of the Mapper algorithm does not solely rely on statistical methods but focuses on the geometry and topology of the data, providing a novel perspective on epidemiological data analysis【5†source】.
                2. **TDAview**: This tool offers an online visualization for topological data analysis, allowing users to define edge color or infer it from node color, and to display labels showing the number of common points between two linked nodes. It supports exporting Mapper graphs to various formats, facilitating the analysis of the topological structures formed by data points【6†source】.
                3. **Learning a Cover in the Mapper Construction**: A paper introduces an approach to optimizing the cover of a Mapper graph by focusing on the selection of the cover parameter. The study demonstrates the Mapper algorithm's application to a toy dataset, showing how the construction process involves choosing a lens function, cover, and clustering algorithm to generate a graph that accurately reflects the structure of the dataset. This process highlights the importance of edge connections in understanding the dataset's topological features【7†source】.
                
                These papers demonstrate diverse applications of the Mapper algorithm, emphasizing the analysis of edges in the resulting graphs to understand complex datasets better. They cover areas from epidemiology to optimizing the algorithm's parameters for more accurate data representation, showing the versatility and depth of analysis possible with this approach.
                
- 🐣 [Brainst- Proj Present 1](../Brainst-%20Proj%20Present%201%202383a603b271491c84199a41da57b600.md)
- 🐣 GPT2_TL_SAE_training_v1
    
    [[CAA_SAE_explrTests_v1.ipynb](https://colab.research.google.com/drive/1rv8d3VJBSLxtSbFGq1809VZB1BGPGiZe)](../CAA_SAE_explrTests_v1%20ipynb%20ac477af8bdf54dc5bdf057884cfe0c2b.md) 
    
    - ✅ Modify `n_input_ae` and `n_hidden_ae` to use gpt2 dims
    - ✅ Modify training data to use GPT-2’s activations, then train
    - 🐣 Train with more batches and SAE instances
- ✅ [Brainstorm- extend sv to eqv classes](../Brainstorm-%20extend%20sv%20to%20eqv%20classes%20e8e8d62ec04a43e78d6df5b52ab6020d.md)
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