# Project Planning

[Done](Project%20Planning%20b4b05f73d85e409f8409b209e44ed692/Done%201c002201437341e48b55b8276859a632.md)

---

### Working on

Reflect on next direction

- If these actvs are just lin combos of same GTF, that doesn’t seem like “different models”. rather the same model!
    - we need to create 2 different GTF sets that share the same GTF. We should only expect the the shared subset of features to be learned from both- thus, we should apply the metrics to the subset, vs not the subset. This way, we expect the metrics to work well on the subset- if they don’t, they’re bad metrics. We must compare the GTF to each SAE- if it’s high, then we compare the SAEs.
        - this is bc we aim to find what parts of the model are shared. and to determine what relations they share.
- what’s the point of checking these metrics if we already assume they SHOULD be expected to learn the GTF relations? Actually, it’s because we don’t know if they will learn the relations of the GTF too. We use MMCS to see they learn similar features. But that doesn’t mean those features will arrange the same way. So this is not a way to check if those metrics work; they should already work. We’re checking if models learn GTF relations. As such, we don’t need across models, actually- just SAE to GTF.
    - so it’s not even a ‘precursor’ at all- we can directly apply to both real world LLM and synthetic simult. synthetic is ANOTHER expm in parallel to verify if these relations learned are actual ground truth relations, not just spurious across models.
    - more so we need a way to hone in on the subset of features. this is a new method.
    - also to statistically find how well this method works, but this isn’t needed. we can just do this for multiple models.
- how can Jaccard (KNN), RSA and CKA be used if no data to act as instances? I think you have to use them on activations, not weight matrices.
    - so any result you get on weight mats is false
    - just use the orig samples as activations thru these weight matrices to get actvs to compare by instances
        - you dont need training actvs; can use completely new actvs that must be made from same GTF matrix. this way, both models ahve new actvs (as they were trained from diff actvs).
    - we can also match the features by their actvs, but this isn’t 1-1 and can break the metric (and KNN). We need instances.
        - ask Max if we can do this though.

Measure and Match Feature Subspaces

- Brainstorm algorithm steps
    - Get highly correlated features
    - Find nearby features which also have high corr
        - their distance in high dim space. for now, just if they’re in same cluster?
    - Measure repr similarity on subset
- [jaccard_subset_ts_1L_2L.ipynb](https://colab.research.google.com/drive/1LIHrRNnB2rPp197QGLyji7a1IJNeI_g9#scrollTo=nKQgHI_BvyBq)
    - [Check jaccard sim knn if uses indices of matrix](https://chatgpt.com/c/b17bcc9b-c69d-48ac-9e0c-1a778bdda2e2)
        - yes it does
        - Is it illusion for random to always be lower? no
    - It might be bcause the subset matches them? or it stacks them row by row, so that doesn’t make sense. unless it doesn’t stack them by orig index orders
        - examplie pic
            
            ![Untitled](Project%20Planning%20b4b05f73d85e409f8409b209e44ed692/Untitled.png)
            
        - This example shows indices [1309, 16063, 13316], and that the original 13316 is now in the third place of the subset. This is why the two weight matrices could be matched! So jaccard wasn’t an illusion. They ARE moer similar than random because their indices are comparable. They’re both mapped to 0, 1, etc. based on their corresponding match. They aren’t the indices of the original, but are indices of their common matching index.
    - also, if use n_neigh as 11 and only 15 elems, we’d expect them to be close. this is bc it will select the top 11 elements REGARDLESS of if too far away or not- there is no cutoff of ‘within a radius’.
        - [so use lower k when calling jacc](https://colab.research.google.com/drive/1LIHrRNnB2rPp197QGLyji7a1IJNeI_g9#scrollTo=OCtZnRU0J6Rx&line=8&uniqifier=1)
    - it may be the more elems in subset, we expect jacc to be smaller. so relative of your subset to rand subset, not abs jacc vals. this means we can’t just say jacc is low if it’s 0.08, must be rel to rand
        - this is true, as depends on n_neigh.
        - thus these are wrong; try “time” and “she”, they get high jacc
            
            These clusters have to be semantically meaningful **together** though; the three clusters "once", "upon", and "time" form a subspace that has higher jaccard sim than random feature subsets, but if you take clusters which aren't meaningful together like "once", "she", ".", they don't do this. also it's only semantically meaningful feature subspaces; taking the jaccard similarity of the entire feature subspaces is incredily dissimilar
            
        - So while jaccard does match, the example using “if use multiple clusters in same subset” doesn’t hold. IT may be still hold but you need to use some other metrics to prove this.
    - A better comparison than random would be to take modA feats from “once” and modBfeats from “she” and compare them. To make them the same, take whichever has less elems in subset.
        - Yes this is still low in comparison (0.05 to 0.26) for same subset len.
            
            [https://colab.research.google.com/drive/1LIHrRNnB2rPp197QGLyji7a1IJNeI_g9#scrollTo=iVCBF7nmDxAd&line=3&uniqifier=1](https://colab.research.google.com/drive/1LIHrRNnB2rPp197QGLyji7a1IJNeI_g9#scrollTo=iVCBF7nmDxAd&line=3&uniqifier=1)
            
        - This is despite “once” and “she” both having common neighbors. Thus, this rules out “similar because can have common neighbors”.
    - note: the indexing may not be 1-1. check how pytorch does it; can it repeat?
        - example pic
            
            ![Untitled](Project%20Planning%20b4b05f73d85e409f8409b209e44ed692/Untitled%201.png)
            
        - Yes, it can. `weight_matrix_np[[1,1,2], :]` yields the same row. This is why the corr (not 1-1) has same.
    - how many unique elements are in each subset?
        - modA repeats a lot!
    - So bc modA contains repeats, this may be an illusion- though I don’t see how. test on rand reps
        - we need to create an “artificial random mapping” that allows non 1-1 repeats
        - [modify this to make half of the elements select in rand_modA_feats be repeats:](https://chatgpt.com/c/49e501ef-8a8a-4e21-9be1-6167f7d172fa)
            
            ```python
            rand_modA_feats = np.random.randint(low=0, high=weight_matrix_np.shape[0], size=100).tolist()
            rand_modB_feats = np.random.randint(low=0, high=weight_matrix_2.shape[0], size=100).tolist()
            X_subset = weight_matrix_np[rand_modA_feats, :]
            Y_subset = weight_matrix_2[rand_modB_feats, :]
            
            total_scores += jaccard_similarity(X_subset, Y_subset)
            ```
            
        - good; it’s still low.
    - [What if we match based on re-arranging indices of both weight matrices based on highest correlations? This may not be 1-1.](https://colab.research.google.com/drive/1LIHrRNnB2rPp197QGLyji7a1IJNeI_g9#scrollTo=EjWfyiIrMVTo&line=1&uniqifier=1)
        
        `jaccard_similarity(weight_matrix_np[highest_correlations_indices_v1], weight_matrix_2)`
        
        - now they’re highly similar. so it doesn’t matter what combo of clusters you use.
        - `len(list(set(highest_correlations_indices_v1)))` : there are 8097 elem, and 16384 total, so half are repeats. but this doesn’t matter.
- also, it’s obv that once tokens are more similar in dist. so perhaps we should take one repr from “once”, one repr from “time”, etc and ocmpare them across models. no; that’s not knn then, but some other metric.
    
    [https://colab.research.google.com/drive/1LIHrRNnB2rPp197QGLyji7a1IJNeI_g9#scrollTo=FYUuyrMPLl_G&line=1&uniqifier=1](https://colab.research.google.com/drive/1LIHrRNnB2rPp197QGLyji7a1IJNeI_g9#scrollTo=FYUuyrMPLl_G&line=1&uniqifier=1)
    
    - use n_neigh (k) as low if only a few samps, or we need to do this for many representatives as nn being 11 (more like 10, since it includes self at first then cuts it off)

- obviously they would be close to each other in the same space
    - the main question is- are the arrangements also similar? what do we mean by “arrangements”? look at mapper? ask these questions
- but it’s not just arrangements that’s impt- it’s functionality.
- also, the rearrangement of rows to match entire feature subspaces is interesting.

- force 1-1 mappings in corr
- Perhaps match them using knn of tokens instead based on actv
- Stat tests with pval

- quanitfy number of features to how good they are for steering. is there a correlation?
    - which features of the ones that highly actv are good for steering?

---

- Pers hom
- Functional sim of feats by ablate and steer
- ask Max if using subset of correlated subset of features (based on actv values and ablation) works.
    - this is key as it’s your new method to implement; the GTF synth actvs are secondary to this.
    - it’s not ‘just apply old sim metrics’; it’s WHICH subset of features to select to try this!

Train SAEs on synth data for better stats

- change luke’s code-other
    - add tqdm to sae training, but may use something else for synth actv
    - make decorative changes to new synth actv fn
        - use einops on synth data, split into 2 fns
        - must use batch, else too slow. find diff ways to do batch
        - use typing in args
        - data loader?
        - comment on why use `@dataclass`
        - make sure it gets similar results as old fn
    - make synth data (poss sae too) be part of class wrapper (see CAA rimsky)
        - class wrapper contains multiple actvs
    - make sure all get similar results as old nb
- 100mil samps for cluster data (need to speed up batch proc, else takes 5hrs)
- add to overleaf for later expms:
    - some features learned by SAEs aren’t true features (no corr to GTF), though they have high sim to each other- identify these when comparing similarity of feature spaces!
    - plot sim between feature spaces (neigh of discrete features) vs sim of discrete features?
- thurs afternoon: finish refactoring code, send to luke to check, put on github
- make sure lin combos of ground truth features are different enough; if too similar, we get datasets that are too similar. Try diff freqs in each model to get properties specific to each LLM
- Features should be meaningful. Why can't hard code meaningful ones? That's synthetic.
    - can we hard code circles in?
- read more about “-taking-features-out-of-superposition-with-sparse”
    - https://www.lesswrong.com/posts/a4oPE4xJqkYSz6jMS/explaining-taking-features-out-of-superposition-with-sparse
    - https://www.lesswrong.com/posts/DezghAd4bdxivEknM/a-small-update-to-the-sparse-coding-interim-research-report
    - https://www.lesswrong.com/posts/8BEJKhgFekvoNEtHv/research-update-sparse-autoencoder-features-are-bimodal

secondary:

- note which torch structs to pass ‘device’ and ‘dtype’ in to prevent torch incompat
    - dont put in before send code to luke (and dont mention); put in if he suggests

Sim metrics:

- take two sim features, and take their neighboring features. are the spaces similar? this is nearest neighbors.
    - we should only apply this to points that are highly similar, matching them.
    - nearest neighbors can be applied to inputs, but here, we apply it to features based on highly matching features.
    - google: "MUTUAL nearest NEIGHBORS" python
- [https://discordapp.com/channels/729741769192767510/1153431135414669422/1268678877497131028](https://discordapp.com/channels/729741769192767510/1153431135414669422/1268678877497131028)
- [https://discordapp.com/channels/729741769192767510/1153431135414669422/1268681876151730264](https://discordapp.com/channels/729741769192767510/1153431135414669422/1268681876151730264)
    - just treating the SAE encodings a sparse vectors then measuring cos distance. nearest neighbors are both changed from the residual stream space as well as from SAE encodings of adjacent layers.
    - This is an expected result for me given feature splitting. You should be able to measure the cos-sim between individual feature's decoder direction, and also measure their joint jaccard sim (ie input similarity). You should be able to find many features that do point in similar directions but activate on disjoint inputs. The "disjoint inputs"/encoder is what determines your hidden activation.
    - You can have two mutually exclusive directions (ie cos-sim=0) read in from the same datapoint. Suppose we have two read-in vectors basis-aligned in 2D. These activate if a feature goes above some bias threshold (supposed it's >3 for both vectors) Then a datapoint of (100,100) will activate both features even though their encoder directions are mutually exclusive.
    - i'm using mutual-knn as my metric. my thinking was that it was possible that the SAE space was just a strange non-linear warping, but perhaps a consistent one. so in addition to looking at the preservation of NNs from residual stream to SAE space, I also wanted to do a quick check of two different SAE spaces. so i used two subsequent layers of residual space which were known to have high mutual-knn (90%+), then encoded both (with separate trained SAEs) into SAE space. But the high mutual knn also was lost in this scenario.
- umap hover for LLM_A, LLM_B, and ground truth- match A to GT and B, wlog for B.
- [**On a Novel Application of Wasserstein-Procrustes for Unsupervised Cross-Lingual Alignment of Embeddings**](https://arxiv.org/html/2007.09456v2)

- once get first results of non-unif feat space expms working to compare metrics, contact apollo and anthropic

---

SAE training

- see luke’s notes on gpu usage in [aug 5th meeting](Links%20to%20Fellowship%20Shared%20Files%207210eabe5bac45a0adee1dd6f1d92cd9/aug%205th%20meeting%20aa722651ec76486c8027ca9279d95893.md)
    - [https://datacrunch.io/](https://datacrunch.io/)
- use bad gpus torrnodes 1-6 if not train anything impt. how much to train hundreds of saes?
- [openai feature splitting viz for topk](https://openaipublic.blob.core.windows.net/sparse-autoencoder/sae-viewer/index.html#/model/gpt2-small/family/v5_l8_postmlp/num_features/32768/num_active_features/8/feature/0)

https://x.com/ravfogel/status/1814318728491815228?t=lGO6Hq9IbIoRESoMo72Psw&s=19

Steering theory

---

umap inteartcitve

***Figure 4 here (***svelte) contains subplots such that moving on one will move on the others: [https://pair-code.github.io/understanding-umap/](https://pair-code.github.io/understanding-umap/)

---

Ph

- code it and write up

https://youtu.be/5ezFcy9CIWE?si=iXnuCh52RAK3JiqG

https://youtu.be/2PSqWBIrn90?si=9WB9d7GY6mPfFLZg

https://towardsdatascience.com/persistent-homology-with-examples-1974d4b9c3d0

What if 2 struc have same b and d, how are they distinct pts on pers dia?

msg algtop phd/masters students

TDA tuning

- try diff parameters, clustering algo, projection algo (isomap)
- should you normalize data before?
- is edge strength based on num overlapping pts in clusters?

TDA analysis

- map and color corr points in clusters between mapper graphs
- search for features and color clusters across models
- auto find similar subgraphs across models
- label entire subgraphs (like Scaling Monosem)
- What’s the “path distance” from say the “one” community subgraph to the “.” community subgraph across models?

- [place cells: position lays on torus. dont want to end of coord system](https://www.nature.com/articles/s41586-021-04268-7)

[when comparing the similarity of two feature spaces in neural network activations to see if they learn similar feature relations, can we compare the subgraphs of their mapper graphs of their activations or weights?](https://chatgpt.com/c/370df1cc-39da-4416-8d86-15b4caf8d915)

[https://kepler-mapper.scikit-tda.org/en/latest/html-visualization-features.html](https://kepler-mapper.scikit-tda.org/en/latest/html-visualization-features.html)

How come we don't see circular months in umap with number features?

Train on small dataset sith king queen etc to ensure those are captured. Ask gpt etc if this makes sense

[https://dl.acm.org/doi/10.1145/3604433](https://dl.acm.org/doi/10.1145/3604433)

**Visualizing and Interpreting Bias Mitigation Techniques Geometrically for Word Representations**

---

Alt projects

Sim metrics, TDA, and func sim are NOT just for ‘across models’, but for feature splitting WITHIN a model. Map between SAEs. What properties of the manifold / simplicial complex change across feature splitting?

Also, WITHIN an SAE, can map analogous structures (eg. months to days, or king-queen to father-mother). Find similar subspaces within/across layers, mapping how they change over layers or during training.

(future work): These sim metrics / topological properties, once found and studied, may be used in loss functions to optimize the model towards learning certain beneficial topological arrangements

- cross-model feature subspace patching / model stitching

https://www.alignmentforum.org/posts/baJyjpktzmcmRfosq/stitching-saes-of-different-sizes

https://www.reddit.com/r/MachineLearning/s/dJhzCSX93r

Llms hallucinate alike

Train SAEs to learn specific, separate royal family features

- PLAN: our tools (corr, dataset exmps, umap, etc) have been shown to work. now, we need better datasets and models that show fs
    - once get better saes with fs concepts, color code multiple concepts- king queen princess- and check their relations across models
        - train on that specific data, on large sae, to ensure it learns them separately
- is top 5 tokens enough? maybe autolabel multiple. note that gpt4 fails at this. try paid cluade

---

UMAP

- umap plot pretrained gpt2 fs- sanity check, should match neuronpedia
- plot corr actv plots for feature split (or corr features)
- how to detect feature splitting, not just from umaps
    - get top 10 more corr from A to B, vice versa
- take most similar vectors and autolabel how similar their dataset examples are, rather than doing it manually
    - without chatgpt: +1 to score if contains same token in top 5, OR get how many of their top 5 tokens have same tokens
- in actv corr plot, show the dataset examples when hovering that are nonzero
- given corr feature pair, zoom-in on the umap of both
- compare MLP 1
- compare tinystories gpt2 to pretrained gpt2
- 🐣 neuronpedia: you can download the labels for their pretrained to use it yourself

[https://transformer-circuits.pub/2024/scaling-monosemanticity/umap.html](https://transformer-circuits.pub/2024/scaling-monosemanticity/umap.html)

[https://chatgpt.com/c/6b6bce5a-43c5-4b4e-8207-49d259712e4b](https://chatgpt.com/c/6b6bce5a-43c5-4b4e-8207-49d259712e4b)

Repr Sim

- before using cca, filter out features better
- cca on feature actvs
- mutual NN on weights and actvs? no; can only do on inputs (tokens)
    - if pts are features, perhaps we can’t use mnn. only makes sense if we plot the tokens in a projected down feature space.
        - indeed, algtop was applied on input pts, NOT neurons as pts! same with activation atlas!
- can cka be done on unpaired points in space? cca can, but mnn needs points that correspond to same input
    
    [https://claude.ai/chat/ef520765-10d0-4aed-8087-eaab5947af59](https://claude.ai/chat/ef520765-10d0-4aed-8087-eaab5947af59)
    
    [https://chatgpt.com/c/0f959dee-0a79-4333-b14d-8d0b130b658e](https://chatgpt.com/c/0f959dee-0a79-4333-b14d-8d0b130b658e)
    
    chatgpt is WRONG; it says cca needs paired. claude says doesn’t need paired.
    
- ask bloom if it makes sense to use cca on a feature subset
    
    tried it and got high values
    
- ask huh about why use knn over cka

- ISSUE: you’re including that feature as “activating on” that keyword if it contains it. But perhaps the majority of the top 5 (or top 10) should contain it

- plot feature subset
- use multiple keywords, each with different color
- instead of color, put a label box around the points in each plot

- in a box outside plot, display the other model’s pair
- compare subspace scores to random subspace pairs. ask chatgpt for how to better stat tests
- Then, higher-order graphs of keyword subspaces. It’s not enough to just plot the subspace of Dragon to subspace of Dragon; it’s the subspace of {Dragon, Princess}, as that’s relation of Dragon to Princess. Or {he, she}

- [I understand negative correlation between two variables. But what does negative CCA mean between two spaces of datapoints?](https://chatgpt.com/c/00acbbcb-2454-4246-a90c-33a4de7067e4)
    
    Canonical Correlation Analysis (CCA) is a method used to understand the relationship between two sets of multidimensional variables. When we talk about a negative canonical correlation, we're referring to the relationship between linear combinations of these sets of variables. Let's break this down:
    
    1. **CCA Basics**: In CCA, we have two sets of variables (let's call them \(\mathbf{X}\) and \(\mathbf{Y}\)). The goal of CCA is to find linear combinations of \(\mathbf{X}\) and \(\mathbf{Y}\) that are maximally correlated. Specifically, we seek vectors \( \mathbf{a} \) and \( \mathbf{b} \) such that the correlation between \( \mathbf{a}^T \mathbf{X} \) and \( \mathbf{b}^T \mathbf{Y} \) is maximized.
    2. **Canonical Correlation**: The canonical correlation is the correlation coefficient between these linear combinations. This correlation can be positive or negative. A positive canonical correlation indicates that when one set of variables increases, the other set tends to increase as well. Conversely, a negative canonical correlation indicates that when one set of variables increases, the other set tends to decrease.
    3. **Negative Canonical Correlation**:
        - When the canonical correlation is negative, it implies an inverse relationship between the linear combinations of the two sets of variables. In other words, the higher values of the linear combination of one set of variables (\(\mathbf{a}^T \mathbf{X}\)) are associated with lower values of the linear combination of the other set (\(\mathbf{b}^T \mathbf{Y}\)), and vice versa.
        - For example, if \(\mathbf{a}^T \mathbf{X}\) represents a particular weighted sum of the variables in \(\mathbf{X}\) and \(\mathbf{b}^T \mathbf{Y}\) represents a weighted sum of the variables in \(\mathbf{Y}\), a negative canonical correlation would mean that when the weighted sum in \(\mathbf{X}\) increases, the weighted sum in \(\mathbf{Y}\) tends to decrease.
    4. **Interpretation**: In practical terms, a negative canonical correlation suggests that there is an inverse relationship between certain linear features of the two datasets. Understanding this can help in fields such as finance (e.g., where one portfolio might hedge against another), biology (e.g., where certain gene expressions might inversely relate to others), and more.
    
    ### Example
    
    Suppose we have two sets of variables:
    
    - \(\mathbf{X}\): Economic indicators (e.g., interest rates, unemployment rates, GDP growth).
    - \(\mathbf{Y}\): Stock market indicators (e.g., stock prices, market indices, trading volumes).
    
    If we perform CCA and find a negative canonical correlation, it could mean that a particular linear combination of economic indicators (e.g., a scenario where interest rates and unemployment rates are high) is inversely related to a linear combination of stock market indicators (e.g., lower stock prices and trading volumes).
    
    In summary, negative CCA means that there is an inverse relationship between the optimal linear combinations of the two datasets, indicating that as one combination increases, the other tends to decrease. This can provide insights into the underlying structure and relationship between the two sets of variables.
    
- CCA and CKA on this feature subspace compared to other parts
    - the features in fairy tale subspace (is this too big of a subspace?)
    - use examples that are snippets specific to that subset
        - [https://chatgpt.com/c/1ed23e8e-b0a6-47b9-a3b4-1af35af41378](https://chatgpt.com/c/1ed23e8e-b0a6-47b9-a3b4-1af35af41378)
    - compare to random subspaces
    - compare to all of neuron (orignial LLM) space
    - CKA has issues; ask Huh et al if they use KNN over CKA bc over sensitivity of inputs (changing just one input can make repr be 0)
- search for token will highlight all features on both plots that activate on that token
- label clusters in umap, and map by sim across models
- compare feature-splitting features  on same umap like Towards M
    - use different dataset examples

[https://online.stat.psu.edu/stat505/book/export/html/682](https://online.stat.psu.edu/stat505/book/export/html/682)

---

Misc

- the feature mapping from A to B is the same as B to A bc corr matrix is symmetric

- search by featureID to highlight and zoom in on umap
- claude/gpt4 takes in neuronpedia html and reveng its gui

https://www.alignmentforum.org/posts/fmwk6qxrpW8d4jvbd/saes-usually-transfer-between-base-and-chat-models

- ISSUE: 2L MLP0 sae has many redundant feature neurons that all fire the same!
- find what are the tokens that are 0 in A but nonzero varying in B
    - Model B’s feature appears to fire on more tokens, possibly because it captures more concepts. That is, while these tokens are 0 in model A (1L-21M)’s feature 16251, model B (2L-33M)’s feature 3301 is nonzero for them.

- In 1L, there is no res stream, but in ≥ 2L, can train on other layers than MLP out like res stream

- for labeled umap decoder weights, how do labels change before and after steering?
- label features in mapper plot

Not really feature specific to daughter. Perhaps we can use feature splitting to constrain it to specifically fire for daughter?

- find related story features
    - get sentences just about: she-he-it
    - get sentences just about: princess-dragon-knight

---

[https://www.frontiersin.org/journals/systems-neuroscience/articles/10.3389/neuro.06.004.2008/full](https://www.frontiersin.org/journals/systems-neuroscience/articles/10.3389/neuro.06.004.2008/full)

[https://neuroai.neuromatch.io/tutorials/W1D3_ComparingArtificialAndBiologicalNetworks/student/W1D3_Tutorial1.html#](https://neuroai.neuromatch.io/tutorials/W1D3_ComparingArtificialAndBiologicalNetworks/student/W1D3_Tutorial1.html#)

[https://johnmarktaylor.com/research/](https://johnmarktaylor.com/research/)

https://arxiv.org/abs/2210.16156

https://datumorphism.leima.is/cards/machine-learning/measurement/centered-kernel-alignment/

https://openreview.net/forum?id=8HRvyxc606

https://medium.com/syncedreview/geoffrey-hinton-leads-google-brain-representation-similarity-index-research-aiming-to-understand-b5d14bf77f49

[https://www.youtube.com/watch?v=zZAj8uvr308&ab_channel=IEEESignalProcessingSociety](https://www.youtube.com/watch?v=zZAj8uvr308&ab_channel=IEEESignalProcessingSociety)

[https://www.damtp.cam.ac.uk/research/cia/files/teaching/Optimal_Transport_Notes.pdf](https://www.damtp.cam.ac.uk/research/cia/files/teaching/Optimal_Transport_Notes.pdf)

[https://openreview.net/pdf?id=ByxlnrBeLH](https://openreview.net/pdf?id=ByxlnrBeLH)

- [what's the difference between radius graph and simplicial complex to approximate manifold](https://chatgpt.com/c/895a75e2-9553-41c9-afe0-596ddd733bee)

should we average feature splitting sae instances?

How common are the same analogous patterns for the same dataset? Across datasets? Measure this

- ask chatgpt for help in defining feature manifold. give it overleaf so far

https://chatgpt.com/c/c50f49db-ff6f-4133-83a5-21593d3a2383

Sc manifold

https://youtu.be/wuqTOoKeVWw?si=VnrcVX2h82JH_Slo

Cka

https://youtu.be/uj0uQyJcrxY?si=Rv76ksM2mhzlc9bw

Transfer features 

- read: Not All Language Model Features Are Linear
    
    [https://chatgpt.com/c/d908b8ff-4c84-4002-a198-80956bdd7bd6](https://chatgpt.com/c/d908b8ff-4c84-4002-a198-80956bdd7bd6)
    
    - if the elements in the plot given from the paper are weights, how are the labels like Monday derived?
        
        The labels like "Monday" in the PCA plot are derived from the specific clustering of dictionary elements corresponding to days of the week, as discovered through the use of sparse autoencoders (SAEs) on language model hidden states. Here's a step-by-step explanation of the process:
        
        1. **Sparse Autoencoders (SAEs)**: SAEs are trained to decompose model hidden states into sparse vector sums from an over-complete basis. This means they can identify dictionary elements (features) that are activated by the model.
        2. **Clustering**: The dictionary elements identified by the SAEs are clustered based on their pairwise cosine similarity or Jaccard similarity. This clustering helps in grouping together elements that represent similar concepts or features.
        3. **Multi-dimensional Features**: The clusters that emerge from this process often represent multi-dimensional features, such as the circular patterns observed for days of the week. These clusters are then analyzed to ensure they are not mixtures or separable into lower-dimensional features, making them irreducible multi-dimensional features.
        4. **Interpretation**: Each cluster is interpreted and labeled according to the tokens that predominantly activate the dictionary elements in that cluster. For example, a cluster of dictionary elements that are primarily activated by tokens corresponding to "Monday" will be labeled as such.
        5. **Visualization with PCA**: PCA is used to reduce the dimensionality of these multi-dimensional features for visualization purposes. The resulting plot shows distinct clusters corresponding to the days of the week, which are labeled accordingly.
        
        In summary, the labels like "Monday" are derived by clustering the dictionary elements found by SAEs, which are then analyzed and interpreted based on the tokens that activate them, and visualized using PCA to show the circular representation of the days of the week.
        
    - cite the lines in the paper  that made you derive:
        
        The lines in the paper that support the interpretation and labeling of clusters according to the tokens that predominantly activate the dictionary elements in that cluster are:
        
        1. "This suggests a natural approach to using sparse autoencoders to search for irreducible multi-dimensional features:
            1. Cluster dictionary elements by their pairwise cosine similarity or Jaccard similarity.
            2. For each cluster, run the SAEs on all xi,l ∈ Xi,l and ablate all dictionary elements not in the cluster. This will give the reconstruction of each xi,l restricted to the cluster found in step 1 (if no cluster dictionary elements are non-zero for a given point, we ignore the point).
            3. Examine the resulting reconstructed activation vectors for irreducible multi-dimensional features, especially ensuring that the reconstruction is not separable. This step can be done manually by visually inspecting the PCA projections for known irreducible multi-dimensional structures (e.g. circles, see Fig. 2) or automatically by passing the PCA projections to the tests for Definition 3"【9:0†source】.
        2. "As described in Section 4, given a cluster of dictionary elements S ⊂ {1, . . . ,m}, we run a large set of activations through the SAE, then filter out samples which don’t activate any element in S. For samples which do activate an element of S, reconstruct the activation while setting all SAE features not in S to have a hidden activation of zero. If some collection of SAE features together represent some irreducible feature, we want to remove all other features from the activation vector, and so we only allow SAE features in the collection to participate in reconstructing the input activation"【9:2†source】.
        
        These lines explain the process of clustering dictionary elements based on their similarities and then reconstructing activations to identify and label irreducible multi-dimensional features.
        
    - cite pics
        
        ![Untitled](Project%20Planning%20b4b05f73d85e409f8409b209e44ed692/Untitled%202.png)
        
        ![Untitled](Project%20Planning%20b4b05f73d85e409f8409b209e44ed692/Untitled%203.png)
        

**generalize this procedure to find other structures: ablate by clusters (elements in simplices)**

Observe steering diffs on split features

Steer nonlinear months

Mapping algo: map based on both repr and func sim. May be a diffeomorphism or some other type of deformation mapping?

- toy model 20B token train feas
    
    ![Untitled](Project%20Planning%20b4b05f73d85e409f8409b209e44ed692/Untitled%204.png)
    

Questions

Why decoder weights are dictionary elements, not encoder

---

- to get LLM actvs, stream process LLM actvs on batch at a time, not loading entire dataset and passing into batch. same with SAEs. Do this to obtain feature acts for each batch_seq token.

[https://transformer-circuits.pub/2023/monosemantic-features#discussion-token-in-context](https://transformer-circuits.pub/2023/monosemantic-features#discussion-token-in-context)

this contains unanswered ques about [‘compositional codes’](https://transformer-circuits.pub/2023/superposition-composition/index.html#distributed-compositional)

[https://transformer-circuits.pub/2023/may-update/index.html#feature-manifolds](https://transformer-circuits.pub/2023/may-update/index.html#feature-manifolds)

what is length scale?

[https://transformer-circuits.pub/2024/june-update/index.html#multidimensional-features](https://transformer-circuits.pub/2024/june-update/index.html#multidimensional-features)

how many data pts does plot in Towards Monosem use?

if impl succeed (whether neg or pos outcomes), copy todo into here and org into expms:

[Feature actvs on tinystories SAEs](Feature%20actvs%20on%20tinystories%20SAEs%208688850817e34618b8d9347574d66397.md) 

ALgo to check if subspace is similar by matching one feature at a time and checking local score, then merging. Approx manifold using simplex

---

ISSUE: with arch sim. We expect same layer to have same features. That's the sanity check.

The issue is mapping features. Are they arranged in the same way?

https://chatgpt.com/c/8a2f7e89-5938-4dbd-88bb-2f031d88db16

At what point is feature splitting too dissimilar or does it get even more similar in certain subspace or feature groups?

Train sae to map between two models using cka loss. Finds features that both models have.

Ask to brainstorm ideas during meeting

https://youtu.be/TBjdvjdS2KM?si=KWVxjYkaNKmVSeVA

Use sim measures to diagnose healthy vs Wrong nn

Very wide network means all layers similar

We don't expect networks to have same exact features but they do have the same steering vectors and months representations. So something is similar. Can we find mappings?

---

- find tinystories across models with good features
    - map top 5 based on actv sim (corr and/OR cosine sim matrix)
    - manually look at pairs with high corr and use dataset examples to label them
- umap + cca on new saes of tinystories
    - actvs or weights in hinton paper? they’re actvs bc use exampls

- train saes at diff layers for multiple ts models ; then feature actv map & umap cca

---

- neg results: need to improve saes, or try diff layers, or try diff models
    - or could mean saes aren’t universal for certain cases. which cases? impt to know in order to figure out what could generalize
    - generalize: good for transfer learning, and using one model to predict another model’s landscape (eg. if mostly similar, can use one as a ‘map’ to guess impt steerable features of another model instead of needing to find them by trial/error)

⚠️ you can also just use Neuronpedia feature dashboards

- wandb metrics
- compile list of training tips from various resources
    - https://www.lesswrong.com/posts/FSTRedtjuHa4Gfdbr/attention-saes-scale-to-gpt-2-small
        - L0 norm changes at each layer of res stream
- Ask on MI, eluther, ARENA discord + slack for advice or pair prog for training SAEs
    - state have nb (may post it) or just state results
    - did X, etc. can it be even faster?
- ask others about comparing tokens of models with different tokenizers
- VPN

---

Multiple feature circuits

- are those features in a cluster/subgraph involved as a single component in a circuit?

---

### Future work

- **IMPT:** Within-models: also use cca on activations for analogous domains. this shows the abstract structure has “analogous” mappings from one domain to another. Like months and numbers.
    - LEVEL 1: The category is a higher-order structure (circles, simplices, etc)
        - Higher-order structures can just be pair-wise (2-simplex) relation between features (with “analogous” roles). This can be distance, or causal. 3-simplex: “father-mother-daughter”
            - each object is a cluster of points, or the LDA vector est of the cluster
            - Each edge is a vector addition or difference?
        - A simplex approximates a manifold subspace. So categories are subspaces.
    - LEVEL 2: The functor is a mapping between higher-order structures WITHIN-MODEL
        - Not just any triangle. But the idea that “man-woman-child” can be encoded in BOTH “king-queen-princess” and “father-mother-daughter”. Both contain this “man-woman-child” basis, and CCA may map these CVs. This “man-woman-child” is the common abstraction, or functor mapping, between the two categories.
            - The functor IS the analogy
        - If month clusters are arranged circularly, how are numbers mapped with them?
            - each data pt isn’t a month, but a feature weight (not actv)
        - Do circuits compose the functor structure with more specific features?
            - Might require several transformations into a space that cleanly shows this
    - LEVEL 3: The “natural transformation” maps functors (of structures) between models.
        - This shows universality of analogies, and how models converge to them

- cca intuition
    
    https://chatgpt.com/c/e7f60612-f476-4019-825e-d1d6f843748b
    
    CCA finds lin combo of features with highest correlation 
    
    So in cca say features man woman child, and father mother daughter, or king queen princess, are most correlated? Analogous?
    
    In cca can you find which combos map to each other, say if man woman maps to king queen, by coefficients basis
    
    So from cca coefficients can we get mapping of features to features based on their relns
    
    Not just two cv
    

https://chatgpt.com/c/cbecf63f-fe30-4804-a3a2-ae4cee00627d

Sparsity norms

Pretrained SAES: [https://github.com/EleutherAI/sae](https://github.com/EleutherAI/sae)

[https://wandb.ai/eleutherai/sae/runs/k1kn6lst?nw=nwusernorabelrose](https://wandb.ai/eleutherai/sae/runs/k1kn6lst?nw=nwusernorabelrose)

Train

- ask neuronpedia on advice for sae training

https://github.com/jbloomAus/SAELens/issues/191

[https://www.lesswrong.com/posts/5XmxmszdjzBQzqpmz/interpreting-preference-models-w-sparse-autoencoders](https://www.lesswrong.com/posts/5XmxmszdjzBQzqpmz/interpreting-preference-models-w-sparse-autoencoders)

can feasibly train saes on: tinystories (up to 4L), gpt2

[https://www.lesswrong.com/posts/f9EgfLSurAiqRJySD/open-source-sparse-autoencoders-for-all-residual-stream](https://www.lesswrong.com/posts/f9EgfLSurAiqRJySD/open-source-sparse-autoencoders-for-all-residual-stream)

- what's the estimated cost for training effective saes for all layers of gpt-2 medium?
    
    [https://chatgpt.com/c/78867e7f-511e-4a8d-b5fd-c05473c92f99](https://chatgpt.com/c/78867e7f-511e-4a8d-b5fd-c05473c92f99)
    

<<<

Compare

- compare actvs using narrow dataset (eg. only Arabic)

Feature space across models should be more similar than their neuron spaces

we’re not looking for true features based on below’s def, but similar representations that can transfer

[https://www.lesswrong.com/posts/QoR8noAB3Mp2KBA4B/do-sparse-autoencoders-find-true-features](https://www.lesswrong.com/posts/QoR8noAB3Mp2KBA4B/do-sparse-autoencoders-find-true-features)

https://youtu.be/TBjdvjdS2KM?si=moubTttOGY5hvCcK

Sim of nn lecture questions

https://chatgpt.com/c/d8492b87-728f-4abb-8bd5-3e4a9c522ec1

What was the impact of similarities of neural networks by Hinton? If it found models with different archs had same representations, did it allow generalizing features from one model to another? What important things did this paper lead to? How about its relation to mech interp?

Is it impactful to use their methods to compare feature representation spaces of sparse autoencoders trained on activations of different models? Or would the findings already br known from Hintons work?

Issue is next token, not input token. But try ones where both tokenizers use one tokens 

- matrix plot of cca for layer-layer similarity

[https://www.lesswrong.com/posts/FSTRedtjuHa4Gfdbr/attention-saes-scale-to-gpt-2-small](https://www.lesswrong.com/posts/FSTRedtjuHa4Gfdbr/attention-saes-scale-to-gpt-2-small)

This finds feature families. how similar are they across models?

[https://colab.research.google.com/drive/1hZVEM6drJNsopLRd7hKajp_2v6mm_p70?usp=sharing](https://colab.research.google.com/drive/1hZVEM6drJNsopLRd7hKajp_2v6mm_p70?usp=sharing)

This also has automated detection of feature families

[https://chatgpt.com/c/0faedc73-4b92-414b-b1d4-6ade923255df](https://chatgpt.com/c/0faedc73-4b92-414b-b1d4-6ade923255df)

- explain the L0 norm col of the table in:
    
    The "L0 norm" column in the table refers to the number of non-zero coefficients in the sparse autoencoder (SAE) representations. In this context, a lower L0 norm indicates that fewer features are being used to represent the data, which aligns with the goal of sparsity. Sparse representations are desirable as they make the model more interpretable by emphasizing the most important features. The table shows the L0 norm for different layers, indicating how many features are active in each layer after training the SAEs.
    

Don’t just focus on similarities; focus on differences. What parts are common to many, and how much is different?

Mapping clusters or higher-order structures is like mapping the subspaces

We’re also mapping circuits, which is not by geometry. And mapping steering vectors associated with circuits. DO the steering vecs and circuits map togther?

sum of contributions then unembed pca. heart higher-order structures: [https://neuralblog.github.io/logit-prisms/](https://neuralblog.github.io/logit-prisms/)

scaling monose actv plots explained:

[https://www.youtube.com/watch?v=8Nyn3_ZWa_U&t=721s&ab_channel=TheInsideView](https://www.youtube.com/watch?v=8Nyn3_ZWa_U&t=721s&ab_channel=TheInsideView)

<<<

- project proposal: (timestamped, ask fazl first before send to others)
    
    To show: Kiho, Bloom, Conmy, Trenton
    
    only reveal more novel (higher order, mapping, FS, etc) after initial meetings
    
    give expms code so far, and in email for initial meeting say have more novel approaches that can discuss later
    
    - experiments done so far
        - sae training setup (ghost grads, wandb, colab, torrnodes, etc)
            - feature splitting on gpt-tinystories
            - more than 2 models
        - why use CKA, etc.
        - higher-order structures and TDA
        - node mapping (reproduce Anthropic)
    - next steps: in-scope list of (justified) ideas and concrete plan to enact them
        - toy model (diff rand init): many saes
        - edge mapping algorithm (high-lvl; state details not shown here)
    - out-of-scope future work
        - analogous steering

- people to contact:
    
    (towards / scaling anthropic papers)
    
    ask fazl beforehand to ensure timestamp (no work leaks) [he knows who can be trusted as if they have incentive to not steal his work]
    
    8/20, code base distr sys: [https://boards.greenhouse.io/anthropic/jobs/4020305008](https://boards.greenhouse.io/anthropic/jobs/4020305008)
    
    - josh batson
        
        [https://www.youtube.com/watch?v=sQar5NNGbw4&ab_channel=Anthropic](https://www.youtube.com/watch?v=sQar5NNGbw4&ab_channel=Anthropic)
        
    - [https://www.trentonbricken.com/about/](https://www.trentonbricken.com/about/)
        - [https://www.youtube.com/watch?v=UTuuTTnjxMQ&ab_channel=DwarkeshPatel](https://www.youtube.com/watch?v=UTuuTTnjxMQ&ab_channel=DwarkeshPatel)
    - callum

- 8/8: contact anthropic
    - started in july
    - they cite SVCCA. So they must’ve tried it. once you try your obvious cca approaches, ask them what issues there were with it, and if any issues with yours.
        - compare approaches; give pros/cons each
    - show them the mapping of higher order structures and working with kiho
        - eg) do they both arrange months circular? what other circulars found by algo?
            - can we map the circular structures?
    - toy model feature splitting: give cost estimates of llm and sae training
    - complexity of mapping algorithms

<<<

1. assumps + parameters for sim code for between saes
2. train saes on toy model
    1. get neuronpedia / eleuther to do this
    2. look for feature splitting
3. in another layer, track how a specific set of features (eg. love or cat) changes after steering
- funcsim: are two features across models also connected to analogous features in later layers?
- can you compare ground truth features as the intermediary? no- the "ground truth features" are model specific right, so it wouldn't make sense to see if two diff LLMs are learning the same ground truth feature
- train a model to map between features from two saes

<<<

Run code of “The Geometry of Categorical” on new data related to behavior

- email kiho on interpreting paper and checking if method to measure simplex based on orth relations is right
    - ask about comparing relations across models
    - ask if using TDA to identify simplex works
        - in a space of data point, how do I find which data points belong to an n-simplex, etc, using algorithms?
- brainstorm how to extend hierarchical concepts
    - steer by animal simplex
        - get convex hull that represents “animal” and add it?
            - how do you even add this?
            - estimate vector and convex hull using trained projection (LDA, linear map)- which to recommend?
- put face features thru existing code (geom, circ) on multiple models and look for hierachy (dog face and human face orthon) and other patterns
- find where hierarchy is detected in code nbs
    
    3_Noun_Heatmap.ipynb
    
    animal has cosine 1 with all others concepts bc they are all related to animal. but why 1, the max?
    

---

Steering circuits

- Probes to obtain “analogous steering vectors” across domains- apply these and observe the geometry
    - across models, find feature relation patterns that ‘explain’ analogous steering
    - the higher-order structures you find may be the  steerable “abstraction” common to a domain that you can extract and combine (eg. months with ordinal) from specific examples
    - or save for future paper
- [**Anthropic Beta Steering API**](https://docs.google.com/forms/d/e/1FAIpQLSc9HRcRFOdid4NJ4-Lyo3HdUybbevMqERWscJIbqilLQRuSQA/viewform)
- [The fact that both features contribute to the final output indicates that the model has partially predicted a sentiment from John's statement (the second feature) but will do more downstream processing on the content of his statement (as represented by the first feature) as well.](https://www.notion.so/Scaling-Monosemanticity-Extracting-Interpretable-Features-from-Claude-3-Sonnet-3219b222ee8943ac9ba1a07963f975b0?pvs=21)
    - Can we better formalize these causal relations between features?
- 80Gb instead of 40Gb for A100- vast ai may specify this
- automatically find steering vectors using dataset samples
- [https://www.lesswrong.com/posts/qykrYY6rXXM7EEs8Q/understanding-sae-features-with-the-logit-lens#Characterizing_Features_via_the_Logit_Weight_Distribution](https://www.lesswrong.com/posts/qykrYY6rXXM7EEs8Q/understanding-sae-features-with-the-logit-lens#Characterizing_Features_via_the_Logit_Weight_Distribution)
- [https://discordapp.com/channels/1080558777608183829/1229803194331304047](https://discordapp.com/channels/1080558777608183829/1229803194331304047)
- UNDERSTANDING AND CONTROLLING A MAZESOLVING POLICY NETWORK
    
    [https://arxiv.org/pdf/2310.08043](https://arxiv.org/pdf/2310.08043)
    
    decompose cheese vector
    
- saelens: train sae on gpt2-xl L20 and put steering vector through it, then interpret top features
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

- Method to reduce dead neurons using loss constraints which force learned wright's to have activations be within useful feature range
- Steering is by prompts, not model. CMAP is by model. Compare them.
- [https://apartresearch.com/project/from-sparse-to-dense-refining-the-machiavelli-benchmark-for-real-world-ai-safety](https://apartresearch.com/project/from-sparse-to-dense-refining-the-machiavelli-benchmark-for-real-world-ai-safety)
- Study: https://github.com/nrimsky/CAA
    - is it 3rd last b/c adds end of seq token somehow in some operation? Find this operation
    

instead of deleting file, transfer new code into shared nb by deleting all old cells and pasting new ones from ‘select all’