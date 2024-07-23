# Brainst- AlgTop Present, draft 1

[https://docs.google.com/presentation/d/1U9gLLkWs_jmkjzg1eMik5WM7f6H69tlO9LFl4R03CtA/edit](https://docs.google.com/presentation/d/1U9gLLkWs_jmkjzg1eMik5WM7f6H69tlO9LFl4R03CtA/edit#slide=id.g2c9ffc13cb8_0_5)

NOTE: this is wrong bc mapper clusters in X, the open cover preimages are just to cluster within each preimage. so each preimage of cover can have multiple clusters

Outline:

Title: Model Behavior Editing via Conceptual Topological Neighborhood Graphs

alt: Model Behavior Editing via Mapper Graphs of Features

- 4 part outline: 1) The AI safety problem, 2) Why Mapper Graphs, 3) Feature Decomp, 4) Editing
- AI safety problem: Why editing by clusters?
    - Concepts (sample types) can be identified by clusters, and edges between clusters indicate that these samples are seen in a “similar way” according to the feature axes they reside in
    - also use these approaches: hierarchical clustering, nearest neighbors
        - but we want to check if we can distinguish data by topological features
    - global properties: relate samples that are far from each other
        - there may be topological invariants in the data
- High level solution using concept cluster editing using mapper graphs and SAE
    - Why is it novel?
        - Mapper Graphs have not been applied to features found by state-of-art mech interp techniques yet; they have been applied to analyze NN activations
        - concept clusters (distinguish from feature vectors)
- Previous work of mapper graphs on activations- why it works
    - [https://arxiv.org/pdf/2011.03209.pdf](https://arxiv.org/pdf/2011.03209.pdf)
        
        5: use cases
        
        The branching order indicates that the deer and horse images are more similar than images from other class categories.
        
    - advantanges
        - [https://www.quantmetry.com/blog/topological-data-analysis-with-mapper/](https://www.quantmetry.com/blog/topological-data-analysis-with-mapper/)
            - 
        - lens preserves high dims
            - so lens projects to low dims, but pullback back preserves dims?
                
                Yes, that's a good way to put it! The "lens" in the Mapper algorithm does project the data into a lower-dimensional representation, but this projection serves more as a way to identify interesting features or regions within the data. This step is critical for understanding the overall structure and identifying which parts of the data should be examined more closely.
                
                After this projection, the critical step that distinguishes Mapper from traditional dimensionality reduction techniques is the "pullback." During the pullback, the lower-dimensional representation guided by the lens is used to organize the data back in the original high-dimensional space. This process doesn't discard the original dimensions of the data; instead, it clusters the data based on the insights gained from the projection but within the context of the original, high-dimensional space. This allows the algorithm to preserve the rich, complex structures and relationships inherent in the data that might be lost in a straightforward dimensionality reduction.
                
                In essence, while the lens function projects the data to a lower-dimensional space to simplify the identification of structures or patterns, the subsequent pullback to the high-dimensional space for clustering ensures that the detailed characteristics and nuances of the data are retained and highlighted. This approach allows Mapper to detect and preserve substructures and relationships that would likely be lost in traditional dimensionality reduction processes, leading to more meaningful and accurate clustering results.
                
            - but the visualized graph is still in 2d
    - What does it add-on to clustering? (a tool that’s an e**nhancement of it)**
        - multi-dim filter function
    - Why can’t clustering do this?
        - Simplicial complex vs graph
        - overlapping clusters rather than non-overlapping- this gives relation between clusters, and thus relations between concepts
    - Why use alg top? — OPTIONAL BUT GOOD, FILL IN ONLY IF FIND GOOD ANS
        - NOTE: if you can’t give a good answer, don’t focus on alg top. Just say the mapper algorithm (an add-on to clustering that looks at relations bewteen them) that has its own advs
            - mapper is not clustering; it uses clustering to output a graph
    
    Mapper graph analyses
    
    - Identified topo neighborhoods (mapper graph’s clusters) as classes / features
    - An edge between a pure and an impure node indicates a transition area where the model's certainty (purity) begins to degrade
        - edges between concept neighborhoods after ablation indicate
- Explain changes to previous work to adapt to mech interp
    
    Novel application of Mapper to mech interp
    
    - Inputs to get points in SAE feature space
    - Filter function
        - Previous works used: PCA, SVD, activation vector norms
        - feature vectors
        - unembedding’s 1st ranked token
    - new neighborhood metric other than purity
    - Identify neighborhoods using GPT-4 auto-labeling of samples, compare to manual

Novel application of Mapper to mech interp

- SAE feature ablation in previous work
    - Look at before and after SAE feature ablation
- Activation/Weight Editing in previous work
- Datasets, Models, Expm Details
    - Resource cost estimates
        - Train SAEs
- Possible Expms
- Other approaches
    - Features of a single input as point cloud
    - Abstract concept hierarchy
    - persistant homology
- Links to Code notebooks
- Next steps
- “How” Details of AlgTop and Feature Decomp