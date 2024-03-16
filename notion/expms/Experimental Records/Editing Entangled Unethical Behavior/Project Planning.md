# Project Planning

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
    
- 🐣 Run prelim experiments for fine tuning interp on fine-tuned LLAma models + machiav
    - ISSUE: machiav ISN’T fine tuned, it’s given prompts. So its interpretability has nothing to do with fine tuning training, only in-context prompts.
- Write up 1-page project proposal for sleeper agents using fine tuned llama as proof of concept
    - [Sleeper Agents Replication](Sleeper%20Agents%20Replication%205e70a34eff91418d851d1725584a9a0c.md)
    - Email authors to ask about replication issues

---

the RAVEL paper discusses how changing entangled attributes has ripple effects. Thus, it is almost certain that behavior editing is entangled with editing attributes. The second paper's ways to measure disentanglement can be built upon to measure the degree of which attributes are highly entangled with which behavior editings

Sleeper agents request: interpret fine tuning methods vs editing, AND check how all FT + editing methods are affected by feature/circuit disentanglement (can editing be better at avoiding disentanglement than fine tuning?)

As I'm still conducting some prelim expms, one direction I can check is: can editing be better at avoiding disentanglement than fine tuning? Certain areas may be better at avoiding disentanglement than others. Or, perhaps is unavoidable in some cases.

EXTENDING ACTIVATION STEERING TO BROAD SKILLS AND MULTIPLE BEHAVIOURS

[https://arxiv.org/pdf/2403.05767.pdf](https://arxiv.org/pdf/2403.05767.pdf)

### Future Work

- Steering is by prompts, not model. CMAP is by model. Compare them.
- [https://apartresearch.com/project/from-sparse-to-dense-refining-the-machiavelli-benchmark-for-real-world-ai-safety](https://apartresearch.com/project/from-sparse-to-dense-refining-the-machiavelli-benchmark-for-real-world-ai-safety)

---

Look for related work on google scholar

Study: https://github.com/nrimsky/CAA

---

Hi, I was wondering in which files are the labels for ethical vs unethical behavior located in? I looked at the annotations folder and the spreadsheet files in them

[https://github.com/aypan17/machiavelli](https://github.com/aypan17/machiavelli)

In readme at bottom, see “repo structure” that describes what each folder is

Each spreadsheet has a game’s scene id and chosen action, and the ethical labels for that action. But it doesn’t have annotations for every (scene_id, action) pair. So where are they?

Make your own data: this is done with GPT-4. 

ISSUE: The previous method only works for opposites (two choices, yes or no). In Machiavelli, we have multiple choices.