# Project Planning

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
        
- ✅ Create- [Project Proposal](Project%20Proposal%20f68a82cc910f4a7c98cafbcb52b07fa5.md)
- ✅ Create- [Networking ](Networking%205eb6990dfeee475b920112de369de0ab.md)
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
            
    
    LM is language model, DRRN is RL model
    
    But the lm_agent.py file doesn’t have them as an option; it only loads gpt models using openai_helpers.py
    
- Compare 2 single prompts (with one difference, say multiple choice) in GPT2 or Pythia or Llama-2’s activations. Compare on multiple dimensions- eg. change from “Save the baby” to “Save the adult”, see what activations change. Create a method to summarize what’s different in these activations.
    - Ask multiple people theoretically why this wouldn’t work, but still try it yourself
        - But it DOES work b/c that’s what model steering already does!
        - ask callum about issues with this approach
            
            Hi, I was thinking about the pros/cons of simple "brute" approach to looking at activations. For instance, inputting two prompts with only a small change between them and just subtracting their activations by components (similar to how steering vecs are found by activation steering). Or doing this via two datasets with only a small change between them and looking at means/the distribution per component. Then, one can see which components have the biggest differences, then applying patching on them to get stronger and causal evidence. Was thinking about this vs individually patching and running each component as in ACDC. I assume early papers must've tried this and thought of cons, which is why more sophisticated techniques had to be used instead. I was wondering what kind of pros/cons you know for this, and what papers have done things like this (as the papers I see mostly use patching)? Thanks!
            
    - Save the cache and just subtract the outputs for each component (cache key).

<<<

Associated Concepts Network- Plan

- 

Associated Concepts Network Brainstorm

There are patterns among the concepts. Not just find the circuit; there is a PATTERN for each concept, that is analogous across models. This is what interpretability is missing. No one will uncover this but you.

- a new method to look at activation differences, similar to activation steering, of related concepts to try to find a relational network of analogous representations at diff layers across models
    
    ask callum about issues with this approach
    
- Concepts related to bad vs good. Can it make stereotypes by these associations? How do they change across layers- are there layers where it decides this?
- If it knows X is related to Y, and Y_2 is a type of Y, it should know X is related to Y_2. How is this reasoning performed within the model?

### Future Work

- Steering is by prompts, not model. CMAP is by model. Compare them.
- [https://apartresearch.com/project/from-sparse-to-dense-refining-the-machiavelli-benchmark-for-real-world-ai-safety](https://apartresearch.com/project/from-sparse-to-dense-refining-the-machiavelli-benchmark-for-real-world-ai-safety)

---

Exploratory tests to try model editing:

- Edit associations
    - Gather concepts that are “similar” to the abstract behavior
        - Similar on what component activations?
    - Does adding things about “money” change behavior on “greed”? Indirect changes to behavior based on other concepts, such as removing money.

<<<
Look for related work on google scholar

Study: https://github.com/nrimsky/CAA

---

Hi, I was wondering in which files are the labels for ethical vs unethical behavior located in? I looked at the annotations folder and the spreadsheet files in them

[https://github.com/aypan17/machiavelli](https://github.com/aypan17/machiavelli)

In readme at bottom, see “repo structure” that describes what each folder is

Each spreadsheet has a game’s scene id and chosen action, and the ethical labels for that action. But it doesn’t have annotations for every (scene_id, action) pair. So where are they?

Make your own data: this is done with GPT-4. 

ISSUE: The previous method only works for opposites (two choices, yes or no). In Machiavelli, we have multiple choices.