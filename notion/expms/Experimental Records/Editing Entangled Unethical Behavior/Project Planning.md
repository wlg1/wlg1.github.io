# Project Planning

[Done](Project%20Planning%20b4b05f73d85e409f8409b209e44ed692/Done%201c002201437341e48b55b8276859a632.md)

---

### Working on

Meandering to find research topics

- 🐣 Run prelim experiments for fine tuning interp on fine-tuned LLAma models + machiav
    - ISSUE: machiav ISN’T fine tuned, it’s given prompts. So its interpretability has nothing to do with fine tuning training, only in-context prompts.
- ⚠️ Write up 1-page proposal for sleeper agents using fine tuned llama as proof of concept
    - [Sleeper Agents Replication](Sleeper%20Agents%20Replication%205e70a34eff91418d851d1725584a9a0c.md)
    - Email authors to ask about replication issues
    - ISSUE: the paper states they are already working on interpreting sleeper agents
- ✅ [Brainstorm- related behavior](Brainstorm-%20related%20behavior%20588d73c1315d48e3bb7db26038712fd8.md)
    - Check the novelty. Do existing behavior/concept papers not talk about hierarchical concepts/related behavior? Look at what cites papers of this topic and their related work.
    - Find datasets on behavior and check if interp done on those datasets before
        - Machiavelli
        - CAA
- ✅ Update overleaf with new plan
    
    [https://www.overleaf.com/project/6595bd526fe1eee6f40a8e4c](https://www.overleaf.com/project/6595bd526fe1eee6f40a8e4c)
    
- ⚠️ Code to steer activations from Machiav and CAA ethical datasets
    - [Editing Machiavelli Prelims](Editing%20Machiavelli%20Prelims%20a0708db298d544b388375641494a755f.md)
    - Copy + paste ONE prompt from Machiavelli with TWO choices into CAA nnsight (bc storage)
        
        CAA repl: [Project Planning](../ARENA%20notes%201a8ff2624cff486e9d91b13139420026/CAA%20Replication%20c7062646b89f46b2b623d72f722a7902/Project%20Planning%207fb9304394ea4a728098c812a60d7034.md) 
        
    - machiavelli.ipynb
    - ⚠️ steer_machiav_draft.ipynb
        - ISSUE: nnsight model gen
        - ask question to server and caden
            
            ![Untitled](Project%20Planning%20b4b05f73d85e409f8409b209e44ed692/Untitled.png)
            
        - nnsight server soln
            
            ![Untitled](Project%20Planning%20b4b05f73d85e409f8409b209e44ed692/Untitled%201.png)
            
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
    - [SVD explora tests](SVD%20explora%20tests%20e685dd8723454c0fbaed4e0d19478fd9.md)
    - ✅ double check nb code and understand why for most of it
- ✅ send progress of nbs
    
    make new public sharing folder with new nbs. call it _revised
    
    - activation differences (using transformerlens cache)
    - SVD logit lens unembedding
    - steering using nnsight (solves memory issues)
        - CAA and function steering
        
- 🐣 [[CAA_SAE_explrTests_v1.ipynb](https://colab.research.google.com/drive/1rv8d3VJBSLxtSbFGq1809VZB1BGPGiZe)](CAA_SAE_explrTests_v1%20ipynb%20ac477af8bdf54dc5bdf057884cfe0c2b.md)
    - SAE_template
- read “sparse feature circuits”
    
    it is good to know that something similar to the high level idea I have has a feasible implementation. Given that one can modify behavior by modifying its feature circuits (shown in the paper), one can study these feature-behavior relations in more detail and study how modifying one behavior modifies another behavior (entangled behavior) and how to de-tangle them
    
- cont: 🐣 [[CAA_SAE_explrTests_v1.ipynb](https://colab.research.google.com/drive/1rv8d3VJBSLxtSbFGq1809VZB1BGPGiZe)](CAA_SAE_explrTests_v1%20ipynb%20ac477af8bdf54dc5bdf057884cfe0c2b.md)

---

### Future Work

- is it 3rd last b/c adds end of seq token somehow in some operation? Find this operation
- clean up nbs and update repo
- Method to reduce dead neurons using loss constraints which force learned wright's to have activations be within useful feature range
- Code to decompose CAA activations + steered actvs
    - then do Machiav activations
- Steering is by prompts, not model. CMAP is by model. Compare them.
- [https://apartresearch.com/project/from-sparse-to-dense-refining-the-machiavelli-benchmark-for-real-world-ai-safety](https://apartresearch.com/project/from-sparse-to-dense-refining-the-machiavelli-benchmark-for-real-world-ai-safety)
- Study: https://github.com/nrimsky/CAA