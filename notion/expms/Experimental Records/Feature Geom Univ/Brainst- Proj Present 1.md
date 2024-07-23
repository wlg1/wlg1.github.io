# Brainst- Proj Present 1

- Drafts
    
    v2: [https://docs.google.com/presentation/d/1PZlOrnk-e4ZxCr48NJPOK_OKcf8g6Jnqt5EE0cRhcVs/edit#slide=id.p](https://docs.google.com/presentation/d/1PZlOrnk-e4ZxCr48NJPOK_OKcf8g6Jnqt5EE0cRhcVs/edit#slide=id.p)
    

[https://docs.google.com/presentation/d/13376Sc70cuR89SFa5IW71_uB_yYQAhjeR3ESIFUosj8/edit#slide=id.p](https://docs.google.com/presentation/d/13376Sc70cuR89SFa5IW71_uB_yYQAhjeR3ESIFUosj8/edit#slide=id.p)

Editing Model Behaviors by Analogous Features

Outline

- ~~Originally started with a different approach, but I decided it was a riskier research direction so opted for this one instead~~
    - or, put this at end of outline as “viz using mapper graphs”
- Editing should be clean and the feature vectors should be sparse (made up of a few neurons)
    - papers show linear directions contain features
- Activation Steering takes sets of samples, averaging neuron activations, and subtracts them. A clear next step is to average feature activations to obtain directions. Or decompose steering vectors.
    - Primary aim: add by features
    - Secondary aim: can we pinpoint the minimal criteria for finding steering vectors for behaviors?
        - why: minimal criteria shows what’s unnecessary, preventing researchers from unnecessary data gathering
            - this makes steering vectors more interpretable
                - we can also put steering vectors thru the SAE
        - steer using disentangled features
    - Tertiary aim: can we find better directions using features?
    - adding by feature vectors can be done, as shown by the successor heads paper. however, they only study the most important feature for mod10 addition
        - figure
            
            ![Untitled](Brainst-%20Proj%20Present%201%202383a603b271491c84199a41da57b600/Untitled.png)
            
        - we see that a mod-10 feature found
            - i also did concurrent work for this that showed analogous tasks also shared sub-circuits. and was planning to do something similar to this editing but the successor heads paper did it before i did.
        - we want to extend this to behavior. can features used for behavior A be used to modify behavior B in an analogous way? can we “transform” features to be used analogously?
            - cross task?
                - merullo
            - transforming one feature to be used for another behavior
- Novel contributions
    1. Analogous features across behaviors: 
        - SAE paper equation of feature ablation
        - Can one feature vector that modifies behavior I be used for another behavior II?
        - Can we transform feature vector for behavior I to an analogous feature vector that can to be used for behavior II?
            - Possible transformations: multiple additions, steering vectors
    - msg others and rsch cited to check if these have been done before
        - actually I think something like this was done in the successor heads paper. to clarify, adding the mean difference between only some features of type A and B prompts (and leaving other feature neurons in the steering vec unchanged). successor heads paper adds/subtracts a mean feature value of a mod-10 class, tho not diffs
        - ask amir and callum
            
            Hi, I've been looking into some research topics, and I was thinking people must've thought of activation steering by SAE features (similar to how "SAE find highly..." do feature ablation) in a similar way to how activation steering is done by mean difference in residual stream activations. However I'm not entirely up to date on what approaches with SAE people have done recently. Do you know of any works that do this? Thanks!
            
    1. Hierarchical features: what’s the relation between them? What if we added a feature that corresponds to a cousin or parent attribute- how does behavior change?
        - SAE and other approaches (DBM, DAS) performs disentanglement
            - measure using RAVEL
        - Equivalence classes of features similar to mod 10? Found by common features among samples of a class
        - eqv classes partition under an eqv reln like mod 10. what eqv classes can be made from non-number concepts, such as in terms of behavior or animals?
            
            ### Behavior
            
            1. **Response to Stimuli**: Animals can be classified based on their response to a specific stimulus. For example, animals that are attracted to light (phototactic) vs. those that avoid light (negative phototactic). Each class consists of animals sharing the same behavior towards light.
            2. **Social Behavior**: Animals or humans can be grouped based on their social behaviors, such as those that display altruistic behavior vs. those that do not. For example, species known for cooperative breeding or those that engage in reciprocal altruism can form one equivalence class, while those that don’t can form another.
            3. **Feeding Habits**: Organisms can be classified based on their feeding habits. Herbivores, carnivores, and omnivores each form their own equivalence class based on what they eat.
            
            ### Animals
            
            1. **Habitat**: Animals can be grouped by their preferred habitat, creating equivalence classes such as aquatic animals, terrestrial animals, and aerial animals.
            2. **Reproductive Methods**: Animals that reproduce in similar ways can form equivalence classes. For instance, animals that lay eggs (oviparous) vs. those that give birth to live young (viviparous).
            3. **Taxonomy**: Taxonomic classifications inherently create equivalence classes, such as species, genus, family, etc. Each level of classification groups organisms that share common characteristics and evolutionary history.
            4. **Thermoregulation**: Animals can be divided based on how they regulate their body temperature. Endotherms, animals that regulate their body temperature internally, form one class, while ectotherms, which rely on external sources, form another.
            
            These examples demonstrate the versatility of the concept of equivalence relations and equivalence classes. They can be used to categorize and understand a wide range of phenomena, not limited to numbers or mathematics, by grouping entities that share a specific, defined relation.
            
    2. investigate better sets or a pruned set of samples to subtract, to understand which are impt or not. Averaging out the entire batch works but info is lost on what in batch matters
        - SAE paper performs ACDC to select a feature subset to intervene on
            - can we improve on this?
        - we can do this iteratively or train a model to learn which samples that are used to obtain a steering vector are correlated a lot with behavior changes
    3. Viz using mapper graphs, possible editing by clusters (?)
        - previous papers appraoch to viz
            
            pca proj: [https://www.lesswrong.com/posts/PDDG4uuCLpPsuKepY/comparing-representation-vectors-between-llama-2-base-and](https://www.lesswrong.com/posts/PDDG4uuCLpPsuKepY/comparing-representation-vectors-between-llama-2-base-and)
            
            2018, tsne actv proj:
            
            [https://arxiv.org/pdf/2311.09433.pdf](https://arxiv.org/pdf/2311.09433.pdf)
            
        - CAA also visualizes activations by PCA and clustering. We can do this with mapper graphs
        - dont mention this, since we ARE using mapper graphs
            - (moved here) last few slides: originally, spent some time thinking on using mapper graphs and clustering (auto-labeling samples), using co-optimal transport to measure mapper graph similarity. but realized this did not contribute to improving editing. however, can still be a future project related to interpretabiilty by comparing mapper graphs before and after ablation.
            - if we have time, we can still use this for interpretability, but not guaranteed can contribute to editing
            - this can be figures in a paper to shed light on what’s happening during editing, but may not contribute directly to better editing?
- How to identify features with attrbs
    - Identify features using auto-labeling via GPT-4 of dataset examples that highly activate those features. Tie them to attributes.
    - Identify features impt to behavior by show their ablation causes big behavior change
    - label behavior outputs similar to CAA paper
        - CAA paper measured this by a single token given multiple choice options, so we can do similar
- Steering Comparison Experiments
    - Compare their feature disentanglement scores
        - RAVEL: compare approaches for disentanglement to find monosem feats
            - tests how well do they on feature patching
- Next steps

---

Papers

Sae

Succ

Caa

- there are papers on multiple behavior editing

---

[https://drive.google.com/drive/folders/1BV-QUGDLg5GRb7ejuif4yc_hSHQTm-Eg](https://drive.google.com/drive/folders/1BV-QUGDLg5GRb7ejuif4yc_hSHQTm-Eg)

caa code

---

[https://scholar.google.com/scholar?oi=bibs&hl=en&cites=12785422939412301773&as_sdt=5](https://scholar.google.com/scholar?oi=bibs&hl=en&cites=12785422939412301773&as_sdt=5)

Extending Activation Steering to Broad Skills and Multiple Behaviours

[https://arxiv.org/pdf/2403.05767.pdf](https://arxiv.org/pdf/2403.05767.pdf)

Activation Steering for Robust Type Prediction in CodeLLMs

[https://arxiv.org/pdf/2404.01903.pdf](https://arxiv.org/pdf/2404.01903.pdf)