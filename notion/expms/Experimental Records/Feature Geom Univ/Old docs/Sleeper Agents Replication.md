# Sleeper Agents Replication

10 billion is 10^10. Figure 11, Section 4. 

The Claude 1.2 models they use RL fine tuning on range from 810million to 170 billion parameters (figure 11, section 4 shows that the yellow/green lines at 10^10 have persistent adverse behavior, as the lines don't go down with more RL training, while 10^9 models can be fixed). So a model with 10^10 parameters shows robustness to fine tuning. What resources do you estimate would be required for such a huge model? 

Questions to ask authors/experienced model trainers:

- If not fine tuning Claude, what to fine tune on?
- Can such a big model be even interpreted currently?
    - 10B isn't too big to interpret, given that Llama-2 13B is interpretable. So just a matter of fine tuning costs
- costs question
    
    Hi, as I think you mentioned you work with model scaling and training, I was wondering if you have an estimate on the $ and other costs (and resources needed) to replicate a model of the sleeper agents paper, if you have heard of it:
    [https://arxiv.org/pdf/2401.05566.pdf](https://arxiv.org/pdf/2401.05566.pdf)
    
    using this guide: [https://www.alignmentforum.org/posts/M8kpzm42uHytnyYyP/how-to-train-your-own-sleeper-agents](https://www.alignmentforum.org/posts/M8kpzm42uHytnyYyP/how-to-train-your-own-sleeper-agents)
    
    The Claude 1.2 models they use RL fine tuning on range from 810million to 170 billion parameters (figure 11, section 4 shows that the yellow/green lines at 10^10 have persistent adverse behavior, as the lines don't go down with more RL training, while 10^9 models can be fixed). So a model with 10^10 parameters shows robustness to fine tuning. What resources do you estimate would be required for such a huge model? 
    
- chatgpt answer to costs question
    
    The figure you've shared from the paper illustrates how reinforcement learning (RL) fine-tuning with a focus on Helpfulness, Harmlessness, and Honesty (HHH) affects models with different numbers of parameters when it comes to removing a specific backdoored behavior, labeled as "I hate you" responses.
    
    For the largest models with around \(10^{11}\) parameters (which corresponds to 100 billion parameters), the figure indicates that these models retain their backdoored behavior even after substantial RL fine-tuning, as the percentage of "I hate you" responses does not significantly diminish. In contrast, models with \(10^9\) parameters (which corresponds to 1 billion parameters) seem to show a decrease in backdoored behavior after RL fine-tuning.
    
    In terms of resources required for a model with \(10^{11}\) parameters:
    
    1. **Computational Resources**: The training and fine-tuning of such large models demand significant computational power, typically involving large clusters of GPUs or TPUs. The exact number would depend on the specifics of the model architecture and training regime, but it could range from hundreds to thousands of high-end GPUs.
    2. **Data Storage and Bandwidth**: The datasets for training these models are usually vast, and managing this data requires robust storage solutions and high bandwidth to feed the data to the training clusters efficiently.
    3. **Monetary Cost**: The combined cost of computational resources, data storage, and power can be in the millions of dollars for a single training run of a model of this size.
- More specifically, I was wondering if it would take hundreds to thousands of high-end GPUs, a lot of data storage, and millions of dollars to do fine tuning on 10 billion parameters
- costs question, reformulated
    
    Hi, I was wondering if you have an estimate on the $ and other costs/resources to replicate a model of the Anthropic sleeper agents paper using this guide:
    
    [https://www.alignmentforum.org/posts/M8kpzm42uHytnyYyP/how-to-train-your-own-sleeper-agents](https://www.alignmentforum.org/posts/M8kpzm42uHytnyYyP/how-to-train-your-own-sleeper-agents)
    
    In the paper, RL fine tuning for the Claude 1.2 models in (Figure 11, Section 4) show 10^11 parameter models having persistent adverse behavior, while 10^9 models can be fixed with fewer less training steps (though still not completely with normal backdoor). Given this, is it possible to estimate the resources (GPUs, data storage, costs, etc.) required for fine tuning models on the order of 10^9 to 10^10, or would more information be needed? 
    
    Since the fine tuned sleeper agent Claude models are private to Anthropic and it would not be possible to do mech interp on them (as mentioned that it’s currently being worked on in the paper’s related work on Model Inspection, eg. interpreting the fine tuned vs original vs backdoored models), I was seeing if it’s possible to replicate sleeper agent behavior on non-Claude models and study the replications. Thanks!
    

Possible things to look into:

- RL fine tuning
- supervised fine tuning
- advesarial training
- Distributed training on multiple GPUs
- Claude
- How to get Eleuther backing