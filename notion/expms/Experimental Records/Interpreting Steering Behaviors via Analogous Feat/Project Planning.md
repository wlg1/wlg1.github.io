# Project Planning

[Done](Project%20Planning%20b4b05f73d85e409f8409b209e44ed692/Done%201c002201437341e48b55b8276859a632.md)

---

### Working on

Meandering to find research topics

- ✅ send progress of nbs
    
    make new public sharing folder with new nbs. call it _revised
    
    - activation differences (using transformerlens cache)
    - SVD logit lens unembedding
    - steering using nnsight (solves memory issues)
        - CAA and function steering
        
- 🐣 [[CAA_SAE_explrTests_v1.ipynb](https://colab.research.google.com/drive/1rv8d3VJBSLxtSbFGq1809VZB1BGPGiZe)](CAA_SAE_explrTests_v1%20ipynb%20ac477af8bdf54dc5bdf057884cfe0c2b.md)
    - SAE_template
- ✅ read “sparse feature circuits”
    
    it is good to know that something similar to the high level idea I have has a feasible implementation. Given that one can modify behavior by modifying its feature circuits (shown in the paper), one can study these feature-behavior relations in more detail and study how modifying one behavior modifies another behavior (entangled behavior) and how to de-tangle them
    
- cont: 🐣 [[CAA_SAE_explrTests_v1.ipynb](https://colab.research.google.com/drive/1rv8d3VJBSLxtSbFGq1809VZB1BGPGiZe)](CAA_SAE_explrTests_v1%20ipynb%20ac477af8bdf54dc5bdf057884cfe0c2b.md)
- ✅ create: [Brainstorm- AlgTop Actvs ](Brainstorm-%20AlgTop%20Actvs%20f2894d4bd51247a88c0de5251754dc31.md)
    - ✅ Read papers + lectures on Mapper
    - ✅ Hatcher Ch0
    - ✅ [email- why algtop needed](Networking%205eb6990dfeee475b920112de369de0ab/email-%20why%20algtop%20needed%2090a8057d0f47426f848c74b01f797949.md)
- 🐣 [Brainst- AlgTop Present, draft 1](Brainst-%20AlgTop%20Present,%20draft%201%206e9000b30efc4c09ad0dd28f05dbfba7.md)
    - Outline: Why Mapper solves interp/editing issue
        - Take solns from sim papers + guess how they can be used for MI
        - Read more papers on TDA that use the edges
            - Find papers that use mapper which utilize the edges in their analysis
                
                I found some interesting papers that utilize the Mapper algorithm and incorporate edge analysis in their studies:
                
                1. **Topological Data Analysis for COVID-19**: A study applies the Mapper algorithm to visualize and analyze the spread of COVID-19 in the U.S. The paper discusses the utility of Mapper graphs in understanding the pandemic across time and space, highlighting the importance of connected components and branches within these graphs. These components and branches help identify COVID-19 hotspots and their development over time. This application of the Mapper algorithm does not solely rely on statistical methods but focuses on the geometry and topology of the data, providing a novel perspective on epidemiological data analysis【5†source】.
                2. **TDAview**: This tool offers an online visualization for topological data analysis, allowing users to define edge color or infer it from node color, and to display labels showing the number of common points between two linked nodes. It supports exporting Mapper graphs to various formats, facilitating the analysis of the topological structures formed by data points【6†source】.
                3. **Learning a Cover in the Mapper Construction**: A paper introduces an approach to optimizing the cover of a Mapper graph by focusing on the selection of the cover parameter. The study demonstrates the Mapper algorithm's application to a toy dataset, showing how the construction process involves choosing a lens function, cover, and clustering algorithm to generate a graph that accurately reflects the structure of the dataset. This process highlights the importance of edge connections in understanding the dataset's topological features【7†source】.
                
                These papers demonstrate diverse applications of the Mapper algorithm, emphasizing the analysis of edges in the resulting graphs to understand complex datasets better. They cover areas from epidemiology to optimizing the algorithm's parameters for more accurate data representation, showing the versatility and depth of analysis possible with this approach.
                
- 🐣 [Brainst- Proj Present 1](Brainst-%20Proj%20Present%201%202383a603b271491c84199a41da57b600.md)
- 🐣 GPT2_TL_SAE_training_v1
    
    [[CAA_SAE_explrTests_v1.ipynb](https://colab.research.google.com/drive/1rv8d3VJBSLxtSbFGq1809VZB1BGPGiZe)](CAA_SAE_explrTests_v1%20ipynb%20ac477af8bdf54dc5bdf057884cfe0c2b.md) 
    
    - ✅ Modify `n_input_ae` and `n_hidden_ae` to use gpt2 dims
    - ✅ Modify training data to use GPT-2’s activations, then train
    - 🐣 Train with more batches and SAE instances
- ✅ [Brainstorm- extend sv to eqv classes](Brainstorm-%20extend%20sv%20to%20eqv%20classes%20e8e8d62ec04a43e78d6df5b52ab6020d.md)
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
    

---

### Future Work

- Llama2_TL_SAE_training_v1
- Code “train SAE to decompose steering vectors”
    - where are multiple vectors if steering vectors are an avg?

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