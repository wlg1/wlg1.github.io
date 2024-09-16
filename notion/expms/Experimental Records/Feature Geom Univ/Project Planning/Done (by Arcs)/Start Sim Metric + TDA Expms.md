# Start Sim Metric + TDA Expms

Write-Up Background + Plan for Networking Pitches

- ✅ contact plan this week
    
    This week, contact algtop, saetrain ppl not in big mechinterp company/org ppl (do that next week)
    
    Expect ~1 week response to setup meetings to gather feedback on proj. Then, next week expect ~1 week response from big MI comp/org to setup meetings to get further MI-specific feedback
    
    Take the 1 week to org notes, code, and do more expms
    
    Ask for poss collab. See if they want to add resources/teams to your project. This elicits more likely response than just asking for feedback/ideas (with no credit given to them).
    
    Email at least 10 people in each of the 3 fields. Expect 30% to reply
    
    ---
    
    **AIM**: You already have spent time finding novel research topics. But that’s your secret- not your pitch. The aim here is not to recruit or convince people to “hire” you onto a team; it’s just to get ideas and feedback. Don’t aim to impress them. 
    
    You have many ideas. Look at diff opinions on what people say on those ideas to filter them out. Get new ideas from them too.
    
    You spent 4 weeks running experiments and getting familiar with this work to be able to develop opinions on your own AND contribute to convos with these rschers instead of just blindly saying “I’ll try that”. You also show that you have prelim expms. This is enough. The aim is to contribute to the convo with them (to better THEIR ideas, NOT to impress them), and you can do that now. 
    
- ✅ [AlgTop Notes](../../AlgTop%20Notes%209dda4810e41c4eaf91002696758eb4a3.md) : study mapper, PH theory
    - put essential questions from notes (notion, chatgpt) into overleaf
        - essential: why use this over others? each expm choice should have reason
- ✅ NN sim
    - [why do we need cca, cka, mnn? why not just cosine sim?](https://chatgpt.com/c/4e010143-72eb-4278-b7f2-e89601dc1592)
        
        The need for Canonical Correlation Analysis (CCA), Centered Kernel Alignment (CKA), and Maximum Mean Discrepancy (MMD) over simpler methods like cosine similarity arises from the complexities and nuances of comparing high-dimensional data and neural network representations. Here are the key reasons:
        
        ### 1. **Canonical Correlation Analysis (CCA)**
        
        ### Purpose:
        
        CCA is used to understand the relationship between two sets of variables by finding linear combinations of the variables that are maximally correlated.
        
        ### Why Not Just Cosine Similarity:
        
        - **Dimensionality and Alignment**: Cosine similarity measures the angle between two vectors but does not account for the relationships between sets of variables. CCA, on the other hand, considers multiple dimensions and finds a projection where the correlations are maximized.
        - **Inter-set Relationships**: CCA is specifically designed to find the relationships between two sets of variables, not just individual vectors, making it more suitable for tasks like understanding the similarity between two datasets or neural network layer representations.
        
        ### 2. **Centered Kernel Alignment (CKA)**
        
        ### Purpose:
        
        CKA is used to compare the similarity between representations learned by different neural networks or different layers within a network, considering both linear and non-linear relationships.
        
        ### Why Not Just Cosine Similarity:
        
        - **Non-linear Relationships**: CKA uses kernels to capture non-linear relationships between representations, which cosine similarity cannot.
        - **Alignment and Centering**: CKA aligns and centers the data to remove the influence of mean differences, providing a more robust comparison across different representations.
        - **Invariant to Isometric Transformations**: CKA is invariant to orthogonal transformations and isotropic scaling, making it more reliable when comparing neural network representations.
        
        ### 3. **Maximum Mean Discrepancy (MMD)**
        
        ### Purpose:
        
        MMD is used to measure the difference between two distributions, often used in the context of generative models to compare generated data to real data.
        
        ### Why Not Just Cosine Similarity:
        
        - **Distribution Comparison**: Cosine similarity is designed to compare individual vectors, not distributions. MMD, on the other hand, compares distributions, making it suitable for tasks like evaluating the quality of generative models.
        - **Kernel Trick**: MMD leverages kernels to capture complex, non-linear discrepancies between distributions, offering a more nuanced comparison than cosine similarity can provide.
        
        ### Summary
        
        While cosine similarity is a straightforward and useful measure for comparing individual vectors, it falls short in the following scenarios:
        
        1. **Relationships Between Sets of Variables**: CCA is better for understanding complex relationships between sets of variables.
        2. **Non-linear Representations**: CKA and MMD use kernels to capture non-linear relationships and differences between distributions.
        3. **Distribution Comparisons**: MMD is specifically designed for comparing distributions, a task for which cosine similarity is not suitable.
        
        Each of these methods offers advantages that make them more appropriate for specific tasks in machine learning and data analysis, addressing the limitations of simpler measures like cosine similarity.
        
    - mnn
        
        Mutual Nearest Neighbors (MNN) is another technique used to compare feature activations or embeddings, particularly in the context of aligning or matching different datasets or representations. It focuses on finding nearest neighbors in a mutual manner, often used in scenarios such as data integration or unsupervised alignment of features. Here’s why MNN might be preferred over simpler metrics like cosine similarity:
        
        ### Why Use MNN Instead of Cosine Similarity
        
        ### Purpose of MNN:
        
        MNN aims to find corresponding features or data points across different datasets by identifying pairs that are mutual nearest neighbors. This method is particularly useful for aligning datasets or embeddings when direct feature comparison is difficult.
        
        ### Advantages of MNN:
        
        1. **Robustness to Noise and Outliers**:
            - **Cosine Similarity**: Measures the similarity between two vectors based solely on the angle between them, which can be sensitive to noise and outliers.
            - **MNN**: By focusing on mutual nearest neighbors, MNN is more robust to noise and outliers, as it relies on mutual agreement between neighbors rather than a single measure of similarity.
        2. **Handling of Complex Alignments**:
            - **Cosine Similarity**: Works well for direct, pairwise comparison of vectors but does not account for more complex alignments or relationships between datasets.
            - **MNN**: Captures complex alignments by identifying mutual nearest neighbors, making it suitable for tasks like batch effect correction in single-cell RNA sequencing or aligning embeddings from different models.
        3. **Contextual Relationships**:
            - **Cosine Similarity**: Ignores the broader context of where a vector lies relative to the rest of the data.
            - **MNN**: Considers the local neighborhood of each point, providing a more contextually aware method for comparing data points.
        4. **Cross-dataset Comparisons**:
            - **Cosine Similarity**: Limited when directly comparing different datasets, as it does not inherently handle differences in scale, distribution, or feature space.
            - **MNN**: Specifically designed to align datasets, even when they come from different conditions or have different distributions.
        
        ### Application Contexts for MNN:
        
        1. **Batch Effect Correction**:
            - In single-cell RNA sequencing, MNN is used to align cells from different batches by finding mutual nearest neighbors, correcting for batch effects.
        2. **Unsupervised Embedding Alignment**:
            - When aligning embeddings from different neural networks or different layers within a network, MNN can find corresponding features without requiring labeled data.
        3. **Data Integration**:
            - Integrating datasets from different sources, especially in bioinformatics or computer vision, where direct feature comparison is challenging due to varying scales and distributions.
        
        ### Summary:
        
        MNN provides a more robust and contextually aware method for comparing and aligning feature activations or embeddings, addressing several limitations of cosine similarity:
        
        1. **Noise and Outlier Sensitivity**: MNN is less sensitive to noise and outliers due to its reliance on mutual agreement between neighbors.
        2. **Complex Alignments**: MNN can handle more complex alignments between datasets, making it suitable for tasks that require integrating or aligning different data sources.
        3. **Contextual Awareness**: By considering the local neighborhood, MNN captures more contextual information than cosine similarity.
        4. **Cross-dataset Applicability**: MNN is specifically designed for comparing and aligning different datasets, overcoming limitations related to scale, distribution, and feature space differences.
        
        Overall, while cosine similarity is a useful tool for simple, direct comparisons, MNN and other techniques like CCA, CKA, and MMD offer more sophisticated methods for comparing high-dimensional data and neural network representations, addressing various complexities and nuances in these tasks.
        
    - MSID
        
        [https://chatgpt.com/c/571ca3bd-a0db-40df-bfbd-1124481f65df](https://chatgpt.com/c/571ca3bd-a0db-40df-bfbd-1124481f65df)
        
        [https://github.com/xgfs/imd](https://github.com/xgfs/imd)
        
- ✅ learn about SAE training
    - look at metrics in papers
        - sae find highly (cunning)
            - KL div as downstream loss
        - Improving Dictionary Learning with Gated Sparse Autoencoders
            - L0
            - defines Loss Recovered
        - scaling and eval (openai)
            - we evaluate autoencoders on sparsity L0, and reconstruction meansquared
            error (MSE). We report a normalized version of all MSE numbers, where we divide by a baseline reconstruction error of always predicting the mean activations.
            - 
        - [https://www.lesswrong.com/posts/fifPCos6ddsmJYahD/my-best-guess-at-the-important-tricks-for-training-1l-saes](https://www.lesswrong.com/posts/fifPCos6ddsmJYahD/my-best-guess-at-the-important-tricks-for-training-1l-saes)
            - What does "affine rescaling" mean here
                
                Loss recovered: "Affine rescaling" in this context refers to adjusting the average test loss using a linear transformation that includes both scaling and shifting. Essentially, it's a way to normalize the loss values such that:
                
                - 0% loss recovered corresponds to the scenario where the loss is at its highest (equivalent to zero ablating the MLP).
                - 100% loss recovered corresponds to the model's test loss without any modifications.
                
                This transformation makes it easier to compare and interpret the effectiveness of the SAE outputs in recovering the original model's performance.
                
            - is "Affine rescaling" just another way to say "normalized”
                
                "Affine rescaling" specifically refers to a linear transformation involving both scaling (multiplying by a constant) and shifting (adding a constant), whereas "normalized" typically refers to adjusting values to fit within a standard range, often [0, 1], without necessarily involving both scaling and shifting. In the context provided, "affine rescaling" means mapping the loss values to a range where 0% represents the worst-case loss and 100% represents the best-case loss, explicitly using both scaling and shifting.
                
    - wandb metrics to check and tune until good
        - [compare to jbloom tutorial results](https://wandb.ai/jbloom/sae_lens_tutorial/runs/x44akxec?nw=nwuserjbloom)
        - [ask chatgpt](https://chatgpt.com/c/93b2a800-f73a-43e5-a47b-2600ecf31574)
            - compare ce to mse loss. why have both in wandb?
                
                ### CE Loss vs. MSE Loss:
                
                **Cross-Entropy (CE) Loss:**
                
                - **Purpose:** Primarily used for classification tasks.
                - **Function:** Measures the difference between two probability distributions – the true distribution and the predicted distribution.
                - **Strength:** Penalizes confident but wrong predictions more heavily, which is crucial for improving classification accuracy.
                
                **Mean Squared Error (MSE) Loss:**
                
                - **Purpose:** Commonly used for regression tasks.
                - **Function:** Calculates the average squared difference between the actual and predicted values.
                - **Strength:** Suitable for tasks where the output is continuous and focuses on reducing overall prediction error.
                
                ### Why Use Both in WandB:
                
                - **Versatility:** Having both losses allows for monitoring and fine-tuning models for different types of tasks (classification and regression).
                - **Comprehensive Analysis:** Provides a broader view of model performance, especially in cases where the model might need to balance between classification accuracy and prediction precision.
        - is the MSE loss stable and low?
        - is the L0
        - num training steps needed
    - impt sae feature metrics
        - number of dead features
    - model properties
        - context length
            
            see n_ctx (it’s seq len in input matrix): [https://transformerlensorg.github.io/TransformerLens/generated/model_properties_table.html](https://transformerlensorg.github.io/TransformerLens/generated/model_properties_table.html)
            
            - tinystories context len
                
                [https://github.com/TransformerLensOrg/TransformerLens/issues/492](https://github.com/TransformerLensOrg/TransformerLens/issues/492)
                
                Tinystories-1L-21M and Tinystories-2L-33M. These models have a context length of 2048 tokens per sample. But while the models can technically handle up to 2048 tokens, their training and optimal performance are tailored for sequences up to 512 tokens.
                
- ✅ train_tiny-stories-2L-33M_topk_100k_trainSteps.ipynb
    - ✅ HfHubHTTPError: 500 Server Error: Internal Server Error for url: [https://huggingface.co/api/datasets/roneneldan/TinyStories](https://huggingface.co/api/datasets/roneneldan/TinyStories) (Request ID: Root=1-66a54356-2eb3fb182d4fa0f76db78300;7c1532d0-33bd-483b-a47f-743b8f7391f7)
    [https://x.com/winglian/status/1817238956376801394](https://x.com/winglian/status/1817238956376801394) (fixed)
    - ✅ strange grad error (just went away?)
        
        ```
        Estimating norm scaling factor: 100%|██████████| 1000/1000 [01:12<00:00, 13.84it/s]
        
        ```
        
        ```
        ---------------------------------------------------------------------------
        
        ```
        
        ```
        RuntimeError                              Traceback (most recent call last)
        
        ```
        
        ```
        <ipython-input-18-570336b14fb4> in <cell line: 64>()
             62 )
             63 # look at the next cell to see some instruction for what to do while this is running.
        ---> 64 sparse_autoencoder = SAETrainingRunner(cfg).run()
        
        ```
        
        ---
        
        6 frames
        
        ---
        
        ```
        /usr/local/lib/python3.10/dist-packages/sae_lens/sae_training_runner.py in run(self)
            104    105         self._compile_if_needed()
        --> 106         sae = self.run_trainer_with_interruption_handling(trainer)
            107    108         if self.cfg.log_to_wandb:
        
        ```
        
        ```
        /usr/local/lib/python3.10/dist-packages/sae_lens/sae_training_runner.py in run_trainer_with_interruption_handling(self, trainer)
            147    148             # train SAE
        --> 149             sae = trainer.fit()
            150    151         except (KeyboardInterrupt, InterruptedException):
        
        ```
        
        ```
        /usr/local/lib/python3.10/dist-packages/sae_lens/training/sae_trainer.py in fit(self)
            170             self.n_training_tokens += self.cfg.train_batch_size_tokens
            171
        --> 172             step_output = self._train_step(sae=self.sae, sae_in=layer_acts)
            173    174             if self.cfg.log_to_wandb:
        
        ```
        
        ```
        /usr/local/lib/python3.10/dist-packages/sae_lens/training/sae_trainer.py in _train_step(self, sae, sae_in)
            248         self.scaler.scale(
            249             train_step_output.loss
        --> 250         ).backward()  # loss.backward() if not autocasting
            251         self.scaler.unscale_(self.optimizer)  # needed to clip correctly
            252         # TODO: Work out if grad norm clipping should be in config / how to test it.
        
        ```
        
        ```
        /usr/local/lib/python3.10/dist-packages/torch/_tensor.py in backward(self, gradient, retain_graph, create_graph, inputs)
            523                 inputs=inputs,
            524             )
        --> 525         torch.autograd.backward(
            526             self, gradient, retain_graph, create_graph, inputs=inputs
            527         )
        
        ```
        
        ```
        /usr/local/lib/python3.10/dist-packages/torch/autograd/__init__.py in backward(tensors, grad_tensors, retain_graph, create_graph, grad_variables, inputs)
            265     # some Python versions print out the first line of a multi-line function
            266     # calls in the traceback and some print out the last line
        --> 267     _engine_run_backward(
            268         tensors,
            269         grad_tensors_,
        
        ```
        
        ```
        /usr/local/lib/python3.10/dist-packages/torch/autograd/graph.py in _engine_run_backward(t_outputs, *args, **kwargs)
            742         unregister_hooks = _register_logging_hooks_on_whole_graph(t_outputs)
            743     try:
        --> 744         return Variable._execution_engine.run_backward(  # Calls into the C++ engine to run the backward pass
            745             t_outputs, *args, **kwargs
            746         )  # Calls into the C++ engine to run the backward pass
        
        ```
        
        ```
        RuntimeError: element 0 of tensors does not require grad and does not have a grad_fn
        ```
        
    - ✅ https://github.com/jbloomAus/SAELens/pull/201
        - https://github.com/jbloomAus/SAELens/blob/main/sae_lens/sae.py
        - IMPT: You need to pass in cfg, which uses `LanguageModelSAERunnerConfig`. But this does NOT contain `activation_fn_str` in its `# SAE Parameters` , but `activation_fn`. Find this by ctrl+f. However, it does have `activation_fn_kwargs`
            - https://github.com/jbloomAus/SAELens/blob/main/sae_lens/config.py
            - the args should be on top of the class, not within a fn! don’t just ctrl+f to find it in a class, look at the actual args to see if something like it is there under a similar name
    - ✅ for top k, what value of k do you usually first try when training (relative to llm dmodel?) I see k=8 to 512 (in Figure 6 of openai's sae paper, num active latents L0).
        
        For language models 8-64. Use k =32
        
    - ✅ compare topk metrics to relu. what improves/doesn’t? what does paper say should be diff?
        - ✅ get actvs for 1L, 2L for 8k and 16k widths
        - [fs_UMAP_v1](https://colab.research.google.com/drive/1Ubxrtvycgo0NWr6svNQj93AKt2ZNT7ap).ipynb: topk 32, 100k epochs
            - ISSUE: unlike ReLU, too many dead features!
                - topK has 12000 dead features, while ReLU has 2
                    - [https://wandb.ai/wlg100/sae_tiny-stories-1L-21M_MLP0_df16384_steps100k_topK?nw=nwuserwlg1](https://wandb.ai/wlg100/sae_tiny-stories-1L-21M_MLP0_df16384_steps100k_topK?nw=nwuserwlg1)
                        
                        ![Untitled](Start%20Sim%20Metric%20+%20TDA%20Expms%20b27936470f68400dba996b4f43a4e1c6/Untitled.png)
                        
                    - [https://wandb.ai/wlg100/sae_tiny-stories-1L-21M_df16384_steps30K_relu?nw=nwuserwlg1](https://wandb.ai/wlg100/sae_tiny-stories-1L-21M_df16384_steps30K_relu?nw=nwuserwlg1)
                        
                        ![Untitled](Start%20Sim%20Metric%20+%20TDA%20Expms%20b27936470f68400dba996b4f43a4e1c6/Untitled%201.png)
                        
                    - [https://wandb.ai/jbloom/sae_lens_tutorial/runs/x44akxec?nw=nwuserjbloom](https://wandb.ai/jbloom/sae_lens_tutorial/runs/x44akxec?nw=nwuserjbloom)
            - Try looking into AuxK (open ai paper)- need to use this prevent dead latents. Ask bloom if implemented
        - mapper
    - ✅ why not use topk for feature split (clement comments)
        
        feature spliting shouldnt use topk. 3 features. just one more feature
        
        L0 alllows sae to use more features when it needs to, and less when it doesn’t need to
        
        if a feature needs to be split into 2, then it should be when width is big
        
        topk breaks a lot of intuitions of feature splitting. introduce a prior.
        
        have ppl studied feature splitting with topk?
        
- ✅ [AlgTop Msgs- 29 July week](../../Networking%205eb6990dfeee475b920112de369de0ab/AlgTop%20Msgs-%2029%20July%20week%20d2b50240185b49348930508f4d21ebba.md)
- ✅ [NN sim Msgs- 29 July week](../../Networking%205eb6990dfeee475b920112de369de0ab/NN%20sim%20Msgs-%2029%20July%20week%20a18f20b6f1b040c8b4e61b294ec2e4e5.md)
- ✅ [SAE Msgs- 29 July week](../../Networking%205eb6990dfeee475b920112de369de0ab/SAE%20Msgs-%2029%20July%20week%205a060dd8f5ef46f28004052c2ca0a701.md)
    - ask how many training steps recommended
- ✅ [July 29 meeting](../../Links%20to%20Fellowship%20Shared%20Files%207210eabe5bac45a0adee1dd6f1d92cd9/July%2029%20meeting%20b59cf5f6b99541609c9d1c5c19c71d21.md)
- ✅ [umap html](https://colab.research.google.com/drive/1bW9USPbYUeGX3Gg5rqM3rsX2ox7wPJjb#scrollTo=ovXKp_SriDtZ&line=1&uniqifier=1)
    - the two “once” clusters (red) and the “upon” cluster (right in 1, bottom right in 2) seem to form a triangle
        
        However, this can be a superficial coincidence. We need to find more of these examples to show it’s not.
        
        ![Untitled](Start%20Sim%20Metric%20+%20TDA%20Expms%20b27936470f68400dba996b4f43a4e1c6/Untitled%202.png)
        
    - try to plot hover side by side. ask hamish todd, jay ram and kevin peterson (areana slack)
        
        Hi, I was wondering if you have time for some advice? I've been trying to modify this plot (attached the html) such that hovering over a point in one scatterplot will create a hover box over another point in a second hover box, based on a list "highest_correlations_indices" in which indices are point ids in scatter plot 2 and the values are the mapped indices in scatter plot 1. I've tried several ways but it hasn't worked. Do you have ideas on how to do this? It uses plotly but I don't think that's the way to do it. I've also attached the code with comments on the input args, and a zip of saved input files. Thanks!
        
- ✅ auxk not in saelens ; ask jbloom
    - openai paper, sec A.2
        
        ![Untitled](Start%20Sim%20Metric%20+%20TDA%20Expms%20b27936470f68400dba996b4f43a4e1c6/Untitled%203.png)
        
    
    [https://github.com/jbloomAus/SAELens/pull/201](https://github.com/jbloomAus/SAELens/pull/201)
    
    **Missing**: I didn't reimplement the auxiliary loss which prevents neuron death in top-k SAEs so even though you could train SAEs in this library, it might be inefficient to do so at present.
    
    - msg to jbloom
        
        Hi, I slightly modified the colab code “Training an SAE” to use `activation_fn_str = "topk"` and
        `activation_fn_kwargs = {"k":32}` to train an SAE on tinystories-1L-21M, but it got 12k dead features out of the 16k features (whereas the original ReLU code had only ~20). I was wondering if this has to do with auxiliary loss; was it implemented? I saw issue #201 may not have it. 
        
        One of the things I’m doing is looking for feature splitting on this 1L tinystories model, but while havling/doubling the 16k params and plotting the weights on the same umap shows weights activating on similar tokens next to one another, I don’t really see feature splitting. The weights are activating on tokens like “upon” or punctuation; they combine concepts like “dragon, princess, king” to one feature and don’t seperate them. Do you think topK (L0=32) would help with this, or would it not? I also tried 100k training steps; would more steps help? Looking for general advice to get feature splitting. The tutorial already seems to get good sparsity and loss recovered.
        
    - response
        
        We didn't implement that yet. If you'd like to I'd accept a demonstrably working PR for the auxilliary loss for top k. This should fix dead features . idk how tuning k with top k as Ive not trained with top k myself.
        

Prepare Sim metrics meeting questions

- ✅ read [Towards Measuring Representational Similarity of Large Language Models](https://openreview.net/pdf?id=gG5UGgUzDR)
    - [**NeurIPS 2023 Workshop UniReps Submissions**](https://openreview.net/submissions?page=2&venue=NeurIPS.cc%2F2023%2FWorkshop%2FUniReps)
        - [**Universality of intrinsic dimension of latent representations across models**](https://openreview.net/forum?id=AxRD2FF7aD)
        - [**Comparing Representational and Functional Similarity in Small Transformer Language Models**](https://openreview.net/pdf?id=uKWqDnLI3o)
        - [**On the Direct Alignment of Latent Spaces**](https://openreview.net/forum?id=nro8tEfIfw)
        - [Estimating shape distances on neural representations with limited samples](https://openreview.net/pdf?id=iEnGqvuI8W)
        - [Grokking as Compression](https://openreview.net/pdf?id=uviLSCIsvt)
    - the orthogonal and scaling transforms requires 2 assumptions: 1) repr of inputs is determ (so token “dog” depends on entire sample, not just the token itself), 2) all rows (samples) of repr between models should corr to same input.
        - Thus, we only study models with same tokenizers, for same samples, allowing studying not just last layer
        - The paper uses diff assumption, and only studies last token, last layer to avoid issue of tokenization. Like us, they also use fixed input prompts.
- ✅ [ask bloom on opinoins of feature reln univ](../../Networking%205eb6990dfeee475b920112de369de0ab.md)
- ✅ umap details
    - ✅ update overleaf with umap params & num samples for labels
    - ✅ write up how umap works
        - [https://umap-learn.readthedocs.io/en/latest/how_umap_works.html](https://umap-learn.readthedocs.io/en/latest/how_umap_works.html)
        - [https://pair-code.github.io/understanding-umap/](https://pair-code.github.io/understanding-umap/)
        - [**UMAP Dimension Reduction, Main Ideas!!!**](https://www.youtube.com/watch?v=eN0wFzBA4Sc&ab_channel=StatQuestwithJoshStarmer)
        - [https://www.youtube.com/watch?v=iPV7mLaFWyE&t=1229s&ab_channel=DeepFindr](https://www.youtube.com/watch?v=iPV7mLaFWyE&t=1229s&ab_channel=DeepFindr)
        - [https://topos.site/blog/2024-04-05-understanding-umap/](https://topos.site/blog/2024-04-05-understanding-umap/)
    - ✅ send umap (color once and upon) to luke
        
        I attached a umap of sae feature decoder weights for 16k width SAEs trained on MLP0 of tinystories 1L-21M and 2L-33M. It uses n_neighbors=15, metric="cosine", and min_dist=0.01. The plots are simple for now, where hovering over a point gives the top 5 highest activating tokens from 500 samples of the tinystories dataset (will scale this up to more soon). I’m also working on making it so that hovering over a point in one umap will create a hover box over another point in a second hover box umap. Don’t think can be done in plotly, I’m looking into svelte. Secondly, there are 16k points, but some features like those that capture “princess” are few so hard to see, so it would be better to have a function that zooms into both plots when searching up this keyword.
        
        A few caveats on the “projection/clustering illusions”; in UMAP, distances between clusters are likely to be meaningless due to using local distances when constructing the graph. UMAP runs are also stochastic at certain steps. Lastly, I’m looking to train SAEs that capture ground-truth features better (and more monosemantic), but I’m not seeing feature splitting occurring when I try to replicate the feature splitting plots from Towards Monosemanticity. 
        
        Next, as you mentioned, I’m probably going to look into seeing how similar SAEs on different toy models with synthetic features are (would it be feasible to train dozens of toy models?); these could be a test bed for various more quantitative measures I’m testing (MNN, MSID, etc) than just looking at UMAP/Mapper (not rigorous).
        
- 🐣 Try Mutual Nearest Neighbors code
    - [is Mutual Nearest Neighbors the same as knn](https://chatgpt.com/c/2095e7e3-2e1b-4210-87a5-7558ec19df55)
        
        Mutual Nearest Neighbors (MNN) and k-Nearest Neighbors (kNN) are related concepts in machine learning and data analysis but they are not the same.
        
        ### k-Nearest Neighbors (kNN)
        
        kNN is a classification and regression algorithm that operates by finding the k closest training examples in the feature space to a given query point. The "closeness" is typically measured using a distance metric like Euclidean distance. In the case of classification, the query point is assigned the label most common among its k nearest neighbors. For regression, the query point is assigned the average value of its k nearest neighbors.
        
        **Key points:**
        
        - Finds the k closest points in the feature space.
        - Used for both classification and regression tasks.
        - Distance metrics (e.g., Euclidean, Manhattan) are used to determine closeness.
        
        ### Mutual Nearest Neighbors (MNN)
        
        MNN, on the other hand, is a concept often used in the context of data integration, especially in single-cell RNA sequencing data analysis. It identifies pairs of points that are mutual nearest neighbors between two datasets. This means that point A from dataset 1 is one of the k nearest neighbors of point B in dataset 2, and vice versa.
        
        **Key points:**
        
        - Used primarily for aligning and integrating datasets.
        - Focuses on finding pairs of points that are nearest neighbors of each other across two datasets.
        - Helps in removing batch effects and aligning data from different conditions or experiments.
        
        ### Summary
        
        - **kNN** finds the k nearest neighbors of a query point within a single dataset and is used for classification and regression.
        - **MNN** identifies pairs of points that are mutual nearest neighbors between two datasets, commonly used for data integration tasks.
        
        Thus, while both concepts involve the idea of "nearest neighbors," their purposes and implementations are quite different.
        
    
    [ts_1L_2L_mnn.ipynb](https://colab.research.google.com/drive/10vLXIEWhqhjtOKffTY39ZKAXidGkJMdH#scrollTo=ccDMnuHGg8hC&line=3&uniqifier=1)
    
    - given two weight matrices each of size torch.Size([16384, 1024]), how do mnn of them in python
    - what does result mean given two weight matrices each of size torch.Size([16384, 1024]),: Found 27 mutual nearest neighbors.
- ✅ email algtop ppl again
    - msg torr
        
        As I have been applying Mapper (a topological data analysis [TDA] technique, similar to that used in the toroidal representation paper you linked) to model feature spaces, I was also looking to consult with people who work with TDA. There are some TDA people I am looking to contact, and I was also wondering if you are familiar with people who work in this field (who may also be looking to collaborate, but not necessary)? I am guessing the field is quite niche so it may be hard to connect to people there.
        
    - [email vidit to meet next week](../../Networking%205eb6990dfeee475b920112de369de0ab.md)
        
        
    - email wang, rathore again to meet thurs or later
        
        I hope this message finds you well, I wanted to follow up on the email I sent on Saturday, as it may have been missed due to being sent on a weekend. As detailed in the original email above, I am sending an inquiry about a potential collaboration or meeting for questions regarding research combining TDA and transformer interpretability.
        
        Please let me know if you need any additional information or have any questions. I appreciate your time and look forward to your response.
        
- **✅ Sim metrics meeting questions**
    
    Main
    
    - look for metrics other than clustering in high dim space- may be illusions of closeness due to many ways to get projections?
    - want to get advice on which methods to look into before spending a lot of time looking into them
    - first assmp: if give same sentence, token always gets same sentence. but stochastic repr for var autoen. but in llm things are determ
    - second assmp: just use same tokenizer
    
    Secondary:
    
    - what do you think of distance metrics in sae space? given its sparsity, two vectors might not have any dimensions in common, so would "distance" be roughly the manhattan distance? would it be better to use mutual nearest neighbors instead of euclidean distance to measure feature vector distance then?
    - CKA issues
    - platonic repr hyp paper: if mnn is kenenl-alignment metric, what’s the kernel in both spaces? is it nearest neighbors? then the metric between kernels is set intersection?
    - actv sim is not the only way to compare saes; cosine sim also works. thus, can compare across models with diff tokenizers?
    
    [https://github.com/mklabunde/llm_repsim](https://github.com/mklabunde/llm_repsim)
    
- ✅ meeting notes
    
    CKA: can manip scores. differne and add to loss, but paint any pic you want using lay by layer heatmaps. models still work but repr sims between diff layers are arbitrary. potential problem. models arent realistic. what extent transfer to real models. 
    
    bnechmark for sim metrics. rank metrics. cka most popular, but if test variants, cka is good but not great. orig paper still valid, just didnt test enough. L2 finds L2 is supposed to most sim- thats a big assumption.
    
    1) not develop a method but use existing methods and assume that they work well, and just measure similarity scores of spaces and subspaces.
    
    indiv axis of LLM arent meaningful (not priv)
    
    sae dims- each axis is aligned with meaning. use sim measure thats not invar to rotations, use soft matching 
    
    mutual nearest neighbors
    
    rank 23 metrics: layer test, JSD corr, etc. avg of tests. 
    
    test in same framework
    
    models from hf auto collect actvs
    
    sim metrics invar to rotations: dont use cca bc assumes linear transf from one model to another for efatures, but arb lin combo of features make them not interp (oppo). best metrics: permutation procrustes, instead of orth matrix just use perm matrix to match repr. scipy lienar sum assignment problem. soft matching is imprv of this- tries to match features, but can also match featues in distrb manner. feat is 80% of B1 and 20% of B2. this is more flexible and still only invar to permutations. order of features doesnt matter, but doesnt destroy meaning of directions. convert orig features in new space in cca and diff dims dontt have particular monosemantic feature.
    
    methods- just say holds, these sim metrics are stronger if can extract repr that intuitiely for some other easons. apply sim metrics to ground truth synethic data to see if metrics hold. if so, then can use metrics on models where we dont know groudn turth features.
    
    feature subspaces- can also just take subset and use metrics. model merging. 
    
    topo distances: invariance to rotation but not sure. sometimes can ignore theory and it just works. main problem: geometry score and MSID are pretty slow. high dim may be quadratic. need a lot of samples.  didnt use geom score on benchmark. try it on small toy model with low dims.
    
    sae benchmark: can do it without benchmark bc empirically many papers pass peer review dont use benchmark. create good test. see if results are intersting before get good test. for instance, soft matching dist, stochastic matrix . use probs/scores for features across models to find consistently match features. alignment matrix that maps features to other features is a graph and do clustering.
    
    no guar will find anythin intersting- so risky. dont need to compare techniques to baseline. sae throughout training LLM. see emergence of specific features.
    
    try both perm proc and soft match. first is strict 1-1, other is 1 to multiple. great for clustering. 
    
    last layer, last token- both vers of papers do that. others reverse tokenization and go backwards. get avg of word repr. valid to also just use same tokenizer. BUT if use diff tokenizers,
    
    decoder uses last repr- so all info is already theree. so last token is very impt. only applies to last layer. if go to diff layers, check which words get same tokenization. maybe works out. otherwise, makes sense to aggregate tokens per word. to be agnostic to tokenizer (future papers)
    
    repr space metrics: an aggre measure of relations beween such pts- some are (jaccard, mnn)
    
    some arent- cka
    
    since can use stitching layers to transform repr of one layer to another layer, there needs to some partial correspondance between models. one assmp is bc can match things, there is some reoccurence of features.
    
    RSA have control over invariant bc pariwise dist, dep on how you do that, would have diff invar. may work. sae best use perm based stuff.
    
    getting aligned with repr alignment (on human brains and anns) survey
    
- ✅ meeting reply
    
    For Permutation Procrustes (One-to-One Matching Distance) and Soft-Matching Distance, you can take a look at [http://arxiv.org/abs/2311.09466](http://arxiv.org/abs/2311.09466)
    
    I don’t have code for the soft version, but I have computed Permutation Procrustes with
    
    `PR, PRp = scipy.optimize.linear_sum_assignment(R.T @ Rp, maximize=True)  # returns column assignments`
    
    `distance = float(np.linalg.norm(R[:, PR] - Rp[:, PRp], ord="fro"))`
    
    where R and Rp are collections of representations with shape num_samples x num_dimensions.
    
    Like I mentioned, my coauthor and I are aiming to push an updated version of our survey to arxiv very soon. Our follow-up work that proposes a benchmark for similarity measures should reach arxiv just before that. I will contact you once it is available.
    
- ✅ read: [https://www.alignmentforum.org/posts/z6QQJbtpkEAX3Aojj/interim-research-report-taking-features-out-of-superposition](https://www.alignmentforum.org/posts/z6QQJbtpkEAX3Aojj/interim-research-report-taking-features-out-of-superposition)
    - ISSUE: note that this trains SAEs on synthetic activations, not on toy LLMs. These are activations which simulate one LLM’s activations already. So either use these approaches:
        - train LLM on synthetic data in a similar way. not sure hwo to even approach this as the previous post use synthetic activations, not synthetic text, so it doesn’t even work.
        - use two synthetic activations which share features but combine them in different ways. This simulates two different LLMs
    - ask max on MMCSq
        
        This is the approach I'm experimenting with right now- they create a set of synthetic activations to simulate one LLM, then use MMCS, mean max cosine similarity, between the learned dictionary D and the ground truth features F to measure how well the learned dictionary recovered the ground truth features:
        
        https://www.alignmentforum.org/posts/z6QQJbtpkEAX3Aojj/interim-research-report-taking-features-out-of-superposition
        
        What do you think about using MMCS to compare two SAE feature decoder weights? I think the metrics depend on measuring weights or feature activations; I'm looking to experiment with both cases.
        
    - notes
        - After defining the ground truth features, we then constructed sparse ground truth feature coefficients by (1) sampling from a G-dimensional binary random variable that takes 0 with high probability and 1 with low probability such that on average 5 out of G ground truth features are active at a time, and (2) scaling those sparse binary vectors by multiplying them with a G-dimensional vector where each element is sampled from a uniform distribution between 0 and 1 to obtain an ‘activation’ for that feature.
        - stickiness means y-axis value is constant across an interval on x-axis (plateau)
        - **One of the main things we’d like to identify are the properties of the language model activations that cause the differences from the toy model**
        - If we continue this line of research, we’ll probably also explore better metrics for ground truth feature recovery than mean max cosine similarity. Currently, MMCS only accounts for the maximally similar dictionary element for each ground truth element. But dictionaries may have learned redundant copies of ground truth features, which MMCS fails to account for. An improved metric may be especially important if we explore variable levels of feature correlation and more variable differences between features’ probabilities (i.e. feature probability decay). MMCS also relies on cosine similarity, which will scale poorly as the sizes of our dictionaries increase for realistic models.
        - It would be nice to know if the difference we’re seeing between the toy data and the langauge model results are due to there simply being too many features being in superposition in the langauge model or if it’s due to something about MLP activations in transformers. One way we could address this in future experiments is to train a transformer on a simpler, algorithmic task, rather than natural language. Algorithmic tasks can have fewer features than in natural language, so we might see less superposition as well as be able to precisely quantify probable ranges of feature sparsity.
        - In their current formulation, SAEs leave a few important problems unaddressed, including:
            - SAEs probably don't learn the most functionally relevant features. They find directions in the activations that are separable, but that doesn't *necessarily* reflect the network's ontology. The features learned by SAEs are probably too granular.
            - SAEs don't automatically provide a way to summarize the interactions between features (i.e. there is a gap between features and circuits).
    - [https://chatgpt.com/c/e9a4090b-e560-40d7-aad0-a64c00cf0995](https://chatgpt.com/c/e9a4090b-e560-40d7-aad0-a64c00cf0995)
        - exlain the reasons for using each of these choices: we created a random covariance matrix for a multivariate normal distribution with zero mean. We took a single sample from a correlated multivariate normal distribution and, for each dimension of that sample, found where that sample lay on the standard normal cumulative distribution function.
            1. **Random Covariance Matrix for a Multivariate Normal Distribution with Zero Mean**:
                - **Reason**: The covariance matrix defines the relationships between features. A multivariate normal distribution with zero mean is a standard choice because it is well-understood and mathematically convenient. The zero mean simplifies calculations without loss of generality.
            2. **Single Sample from a Correlated Multivariate Normal Distribution**:
                - **Reason**: By sampling from this distribution, we generate a set of values that inherently follow the correlation structure defined by the covariance matrix. This mimics the real-world scenario where certain features tend to occur together.
            3. **Mapping Sample Values to the Standard Normal Cumulative Distribution Function (CDF)**:
                - **Reason**: The CDF transforms the values into a uniform range (0, 1), preserving the correlations. This step ensures that the resulting binary variables (features being active or not) have the desired correlation structure. This transformation is key to converting continuous values into probabilities that reflect the original correlations.
            
            In summary, these choices allow the researchers to create a realistic model of feature correlations using well-established mathematical tools.
            
        - the probability of the G-dimensional random variable exponentially decayed with the feature’s index. why Exponential Decay?
            
            **Exponential Decay Reasoning**:
            
            1. **Realistic Feature Distribution**: In real-world data, certain features are inherently more common than others. Exponential decay mirrors this natural skewness by making some features appear much more frequently.
            2. **Controlled Variability**: The decay parameter (\(\lambda\)) allows fine-tuning of how quickly feature frequencies drop. This creates a more nuanced distribution, where a few features dominate while others become progressively rarer.
            3. **Mathematical Convenience**: Exponential functions are mathematically well-understood and computationally efficient, making them a practical choice for modeling such distributions.
            
            In summary, exponential decay provides a realistic, adjustable, and mathematically convenient way to simulate feature frequencies.
            
        - 
            
            
- ✅ plan next expm steps
    - Studying existing representational similarity metrics to find which ones would fit the assumptions for SAE feature spaces (have privileged basis so rotation invariant, etc)
    - use multiple synthetic activatiosn to simuate multp toy mods
        
        To verify how accurate each metric is for measuring SAE feature space similarity, we first test each metric on SAEs trained on synthetic activations that simulate toy model activations and are combinations of known ground truth features. These activations are constructed using the approach of \cite{sharkey2022interim}. \textcolor{blue}{An important note is that these experiments do use not toy toy models trained on synthetic text data, but directly use activations which are sparse linear combinations of known ground truth feature directions.} Thus, no toy models are trained; only SAEs are trained. The reason we start with synthetic activation experiments instead of with activations on larger LLMs is because we don’t know the ground truth features that these LLMs learn, and thus don’t know which features should be similar.
        
        \cite{sharkey2022interim} only use one set of synthetic activations to simulate the activations of one toy model; however, since we are comparing SAEs from across multiple models, we use multiple sets of synthetic activations. For the following experiments, we use two synthetic activations which share ground truth features, but linearly combine them into activations in different ways. This simulates two different toy models.
        
        Our experiments record which ground truth features each SAE learns to ensure they’re similar, and use multiple, theoretically valid, metrics to assess their similarity, looking at which metrics correctly find that they’re similar. We compare these results to non-similar SAEs trained on LLMs with different features to ensure they also say those SAEs are not similar.
        
- ✅ overleaf- sim methods & expm plan: sim metrics on toy models with synthetic data
    - [https://chatgpt.com/c/7dbc7fa2-4e28-49e6-90b5-dc16a88bd9f1](https://chatgpt.com/c/7dbc7fa2-4e28-49e6-90b5-dc16a88bd9f1)
- ✅ ask Luke, Clement, beren, etc. to verify if your approach works.
    
    I was wondering if you can assess the validity of this paragraph? It’s one part of a longer experimental setup writeup (I can send that later if requested):
    
    \cite{sharkey2022interim} only use one set of synthetic activations to simulate the activations of one toy model; however, since we are comparing SAEs from across multiple models, we use multiple sets of synthetic activations. For the following experiments, we use N sets of synthetic activations which linearly combine shared ground truth features into activations in different ways. This simulates N different toy models.
    

EXPMS- Sim metrics on ground truth features

- 🐣 explora: toy models from luke’s code
    
    [synthData_explora.ipynb](https://colab.research.google.com/drive/1lHOtRa8KHIZuqbetilKkZFypfHDnSz2M#scrollTo=PLIDVkYupqYY)
    
    - ✅ `from tqdm import tqdm  # must do this to call to fn, not tqdm module from "import tqdm", for batch_start in tqdm()`
    - ✅ can’t use saelens as that is trained on a model in its cfg, not synth actvs
    - ✅ luke’s code uses class `SparseAutoencoder` as the self.model in `SAETrainer`. `SparseAutoencoder` has an `nn.ModuleList` of encoders
        - ✅ Each SAE uses a params from `parameter_grid` (this does hyperparam sweep?). This finds dicts that are combos of the values in `parameter_grid`
            
            ```
            combinations_generator = find_combinations(parameter_grid)
            one_combination = next(combinations_generator)
            ```
            
        - ✅ the model is locally defined within `train_synthetic_sae`, and not returned, so we need to find one globally in order to extract its weights to use UMAP + our own metrics on it
        - ✅ as seen in `trainer.train,` the SAEs are located in `trainer.model.encoders.` We can obtain the hxJ matrix using `trainer.model.encoders[0].weight.detach().t()`
            - the name suggests these are encoder weights. But are they?
                
                The encoder is followed by a learned dictionary of features, D, which is a h×J decoder matrix (with no bias) whose columns (the learned features)
                
                J = G x 2. So are `trainer.model.encoders`. So those may be decoders.
                
                But luke’s paper has W (encoder) be hxJ
                
                SOLN: `trainer.model.encoders[0].weight.detach().shape` is Gxh because `.t()` is transpose. So in paper, encoder is hxG, but in code (luke’s and saelen’s), encoder is Gxh. So don’t take transpose when doing umap
                
                - Regardless of which they are, we can still plot any weights in UMAP as long as the feature weights (the cols) are the rows (just take transpose). And we can still use MMCS and other metrics on these cols.
                    
                    [the reason encoder weights may have failed before is bc you didnt plot the feature weights on rows, while decoder weights uses feature weights as rows {thou thye should be cols} in saelens]
                    
    - 🐣 get rid of the mutual reg loss, if it’s there
- ✅ UMAP plot ground truth feats matrix + SAE enc_weights trained on synthetic actvs to see if they form clusters. they shouldn’t bc they’re uniform; or would they, bc they’re correlated?
    
    
- ✅ where in the code does it take corr ground truth features into lin combos of saes?
    
    `X` (batches) are the activations of toy model, while `Fe` are the ground truth features. SAE is trained on train_loader, which uses X.
    
    ```
    train_dataset = TensorDataset(X)
    torch.save(train_dataset, 'synthetic_dataset.pth')
    train_loader = DataLoader(train_dataset, batch_size=2048, shuffle=True)
    ```
    
- ✅ after making the features correlated, would the features still be in uniform distribution? would it have distinct clusters or shapes in data?
    
    After making the features correlated, the distribution of features would no longer be uniform. Instead, the data would likely show patterns reflecting these correlations, meaning certain features are more likely to appear together.
    
    ### Key Changes in Distribution:
    
    1. **Loss of Uniformity**: Originally uniform feature distributions are transformed to reflect the defined correlations, leading to non-uniform distributions.
    2. **Clusters and Patterns**: The correlated features might form distinct clusters or exhibit specific shapes in the data, depending on how strong the correlations are and how the exponential decay affects feature frequencies.
    
    ### Detailed Effects:
    
    - **Clusters**: Features that are strongly correlated might cluster together in the data, meaning instances where one feature is present will likely include others.
    - **Shapes**: Depending on the correlation structure and decay parameters, the data could form more complex shapes, reflecting high-dimensional correlations and variable feature frequencies.
    
    Thus, the process introduces more structure and pattern into the feature space, departing from a simple uniform distribution.
    
- ✅ It doesn’t matter about the actvs, bc the code should make ground truth features be corr, not when they’re put into actvs X. Find the code that does this.
    
    `generate_synthetic_data` does this in `group_probs`. 
    
- ✅ However, Luke’s code does not modify the `true_features` correlations; only modifies them when choosing coeffs for the activation vectors.
- ✅ QUES: Modify so capture feature relns. Does it make sense if all come from unif distr?
    - perhaps yes, since it’s features that come from unif distr, not the correlated activations
        - but we want to capture FEATURE relations. this is still poss valid- they make correlated FEATURES (not actvs)
        - Actually, not valid- only makes corr when sel coeffs for actvs, NOT changing orig feat distr!
- 🐣 msg to luke about non-unif:
    
    Also, as I’m looking to use metrics that compare how well the SAEs for different LLMs capture the feature space (comparing how well they detect distinct clusters + shapes), I was looking to use features that form interesting arrangements with one another. I was wondering if this is a correct interpretation and what you think of it:
    
    In the “Taking features out of…” post, ground truth features are from sampled from a uniform distribution, and they’re only made correlated when put into linear combinations, as the coefficients of the activation vectors are selected based on the feature frequencies.
    
    So the ground truth features would still form a uniform distribution, and the SAE encoder or decoder weights would also form a uniform distribution. Meaning their UMAP plots wouldn’t show semantic clusters like those seen in “Scaling Monosemanticity”, and wouldn’t be that interesting.
    
    Thus, would it make sense to modify the synthetic activations generation so that ground truth features are not from a uniform distribution, but from a feature space with clusters and other shapes?
    
- 🐣 [msg to chatgpt- does this procedure allow for meaningful feature relns](https://chatgpt.com/c/e9a4090b-e560-40d7-aad0-a64c00cf0995)
    - same msg to chatgpt
        
        Your interpretation is correct, and it makes sense to modify the synthetic activations generation to create a more interesting feature space. Here's a detailed explanation
        
        ### Current Interpretation:
        
        - **Uniform Ground Truth Features**: In the original setup, ground truth features are sampled from a uniform distribution.
        - **Correlations in Linear Combinations**: Features are made correlated when combined into activation vectors, but individually they remain uniformly distributed.
        - **Resulting Distributions**: This leads to uniform distributions in both ground truth features and SAE weights, resulting in less interesting UMAP plots without clear semantic clusters.
        
        ### Modifying the Synthetic Activations:
        
        To generate more interesting feature arrangements:
        
        1. **Non-Uniform Ground Truth Features**: Sample ground truth features from a distribution that naturally forms clusters or other shapes. This can be done by:
            - Introducing correlations directly among features during sampling.
            - Using a known non-uniform distribution with cluster-forming properties (e.g., Gaussian mixtures).
        2. **Generating Synthetic Activations**:
            - Ensure that the activation vectors reflect these non-uniformly distributed features.
            - Maintain or enhance the correlations between features in a way that highlights distinct clusters and patterns.
        
        ### Benefits:
        
        - **Interesting Arrangements**: The modified feature space will likely form distinct clusters and shapes, making it easier to visualize and analyze using techniques like UMAP.
        - **Comparative Metrics**: This setup allows for better comparison of how different SAEs capture and represent complex feature spaces, providing more insight into their effectiveness.
        
        In summary, modifying the synthetic activations to create a more structured feature space with inherent clusters and shapes will make your analysis more meaningful and visually informative.
        
    - Devise a procedure of synthetic activation generation that allows for meaningful feature relations like clusters and circles in ground truth feature space to be captured by SAEs, using metrics like mutual nearest neighbors and soft matching distance to compare how similar the feature arrangements are of SAEs trained on two different toy model simulations
        
        ### Procedure for Generating Synthetic Activations with Meaningful Feature Relations
        
        1. **Define Ground Truth Features**:
            - Create clusters and shapes like circles within the feature space.
            - Use a mixture of Gaussians for clusters and parametric equations for shapes (e.g., circles).
        2. **Introduce Correlations**:
            - Use a covariance matrix to introduce correlations within and between clusters.
            - Ensure features within the same cluster have higher correlations.
        3. **Sample Features**:
            - Sample from the defined distributions to create the ground truth feature vectors.
            - Ensure the sampling maintains the designed structures.
        4. **Transform to Binary/Activation Values**:
            - Apply a transformation (e.g., thresholding or sigmoid function) to convert continuous values to binary activations.
        5. **Generate Activation Vectors**:
            - Combine features linearly, using coefficients that reflect feature frequencies and correlations.
            - Introduce noise to simulate real-world scenarios.
        6. **Train Sparse Autoencoders (SAEs)**:
            - Train SAEs on the generated activation vectors from different toy model simulations.
            - Ensure consistent hyperparameters for comparability.
        
        ### Evaluation Metrics
        
        1. **Mutual Nearest Neighbors (MNN)**:
            - Compute MNN between the encoded feature spaces of the two SAEs.
            - High MNN indicates similar feature arrangements.
        2. **Soft Matching Distance (SMD)**:
            - Measure the distance between distributions of features in the encoded spaces.
            - Lower SMD indicates closer resemblance in feature arrangement.
        
        ### Steps for Comparison
        
        1. **Generate Synthetic Data**:
            - Follow the above procedure to generate synthetic activation data for two different toy models.
        2. **Train SAEs**:
            - Train one SAE on each set of synthetic data.
        3. **Extract Encodings**:
            - Obtain the encoded feature representations from both SAEs.
        4. **Apply Metrics**:
            - Use MNN and SMD to compare the similarity of the encoded feature spaces.
        5. **Analyze Results**:
            - Interpret the results to understand how well each SAE captures the designed feature relations.
        
        This procedure ensures that the synthetic data contains meaningful relationships, allowing for a robust comparison of how well different SAEs capture and represent these relationships.
        
    - Explain more "Use a mixture of Gaussians for clusters " intuitively and detail procedure wise why ti works
        
        ### Mixture of Gaussians Intuitively Explained
        
        A **Mixture of Gaussians** (MoG) is a statistical model used to represent data as a collection of clusters, where each cluster follows a Gaussian (normal) distribution. Intuitively, think of it as multiple "blobs" of data points, each blob representing a different cluster with its own mean (center) and variance (spread).
        
        ### Why It Works
        
        - **Natural Clustering**: Many real-world data sets have cluster structures. A MoG can naturally model these clusters.
        - **Flexibility**: By adjusting the parameters (means and variances) of each Gaussian, we can create diverse shapes and densities, capturing complex relationships in the data.
        - **Mathematical Tractability**: Gaussian distributions are well-studied and have desirable mathematical properties, making them easy to work with.
        
        ### Procedure to Create Synthetic Activations Using MoG
        
        1. **Define Clusters**:
            - Choose the number of clusters \( K \).
            - For each cluster, define the mean vector \( \mu_k \) and covariance matrix \( \Sigma_k \). The mean vector sets the center, and the covariance matrix defines the shape and spread.
        2. **Sample Data Points**:
            - For each cluster \( k \):
                - Determine the number of points \( n_k \) to sample (proportional to the cluster’s weight).
                - Sample \( n_k \) points from a multivariate normal distribution \( \mathcal{N}(\mu_k, \Sigma_k) \).
        3. **Combine Clusters**:
            - Combine the sampled points from all clusters into a single data set. This results in a synthetic data set with distinct clusters.
        4. **Generate Activation Vectors**:
            - Use the sampled points as ground truth features.
            - Create activation vectors by combining these features linearly, preserving the cluster structure.
        
        ### Example
        
        Let's create a synthetic data set with three clusters:
        
        1. **Define Parameters**:
            - Cluster 1: \( \mu_1 = [1, 1] \), \( \Sigma_1 = [[0.1, 0], [0, 0.1]] \)
            - Cluster 2: \( \mu_2 = [5, 5] \), \( \Sigma_2 = [[0.2, 0.1], [0.1, 0.2]] \)
            - Cluster 3: \( \mu_3 = [8, 1] \), \( \Sigma_3 = [[0.3, 0], [0, 0.3]] \)
        2. **Sample Points**:
            - From \( \mathcal{N}(\mu_1, \Sigma_1) \), sample 100 points.
            - From \( \mathcal{N}(\mu_2, \Sigma_2) \), sample 100 points.
            - From \( \mathcal{N}(\mu_3, \Sigma_3) \), sample 100 points.
        3. **Combine and Visualize**:
            - Combine the 300 points and plot them. The plot will show three distinct clusters.
        4. **Generate Activation Vectors**:
            - Use these 300 points as features and create activation vectors by combining them linearly.
        
        ### Metrics for Comparison
        
        1. **Mutual Nearest Neighbors (MNN)**:
            - For each feature in one SAE, find its nearest neighbors in the other SAE’s feature space.
            - Calculate the proportion of mutual nearest neighbors.
        2. **Soft Matching Distance (SMD)**:
            - Measure the distance between the distributions of features in the two SAEs’ encoded spaces.
            - Use a metric like the Earth Mover’s Distance to compute this.
        
        This procedure ensures that the synthetic data contains meaningful relationships, allowing for a robust comparison of how well different SAEs capture and represent these relationships.
        
    - write python code to generate the grund truth features and synthetic activations in this new way
        
        Here is the Python code to generate ground truth features using a mixture of Gaussians and synthetic activations with meaningful feature relations like clusters:
        
        ```python
        import numpy as np
        import matplotlib.pyplot as plt
        from sklearn.preprocessing import normalize
        
        def generate_gaussian_mixture(n_samples, means, covariances):
            """
            Generate a mixture of Gaussians.
        
            Parameters:
            - n_samples: list of number of samples for each Gaussian component.
            - means: list of means for each Gaussian component.
            - covariances: list of covariance matrices for each Gaussian component.
        
            Returns:
            - X: Generated samples.
            """
            X = []
            for i, (mean, cov, n) in enumerate(zip(means, covariances, n_samples)):
                samples = np.random.multivariate_normal(mean, cov, n)
                X.append(samples)
            return np.vstack(X)
        
        def create_activation_vectors(features, n_activations):
            """
            Create synthetic activation vectors by combining features linearly.
        
            Parameters:
            - features: Ground truth features.
            - n_activations: Number of activation vectors to generate.
        
            Returns:
            - activations: Synthetic activation vectors.
            """
            n_features = features.shape[1]
            activations = np.dot(np.random.randn(n_activations, n_features), features.T)
            activations = normalize(activations, norm='l2', axis=1)
            return activations
        
        # Parameters for Gaussian mixture
        n_samples = [100, 100, 100]
        means = [[1, 1], [5, 5], [8, 1]]
        covariances = [[[0.1, 0], [0, 0.1]], [[0.2, 0.1], [0.1, 0.2]], [[0.3, 0], [0, 0.3]]]
        
        # Generate ground truth features
        features = generate_gaussian_mixture(n_samples, means, covariances)
        
        # Generate synthetic activation vectors
        n_activations = 300
        activations = create_activation_vectors(features, n_activations)
        
        # Plot ground truth features
        plt.figure(figsize=(8, 6))
        plt.scatter(features[:, 0], features[:, 1], alpha=0.6)
        plt.title("Ground Truth Features")
        plt.xlabel("Feature 1")
        plt.ylabel("Feature 2")
        plt.grid(True)
        plt.show()
        
        # Plot synthetic activations (for visualization, using first two dimensions)
        plt.figure(figsize=(8, 6))
        plt.scatter(activations[:, 0], activations[:, 1], alpha=0.6)
        plt.title("Synthetic Activation Vectors")
        plt.xlabel("Activation 1")
        plt.ylabel("Activation 2")
        plt.grid(True)
        plt.show()
        
        ```
        
        ### Explanation
        
        1. **Gaussian Mixture Generation**:
            - **Parameters**: Define the number of samples, means, and covariances for each Gaussian cluster.
            - **Function**: `generate_gaussian_mixture()` generates samples from a mixture of Gaussians.
        2. **Synthetic Activation Vectors**:
            - **Parameters**: Specify the number of activation vectors.
            - **Function**: `create_activation_vectors()` combines the ground truth features linearly to create activation vectors.
        3. **Visualization**:
            - **Plots**: Visualize the ground truth features and synthetic activation vectors to see the clusters and relationships.
        
        This code creates a meaningful feature space with clusters, generating synthetic activations that reflect these structures. You can then use these synthetic activations to train SAEs and compare their performance using metrics like mutual nearest neighbors and soft matching distance.
        
    - what other approaches can be used to simulate interesting feature spaces? don't need distinct clusters
        
        Here are several approaches to simulate interesting feature spaces without creating distinct clusters:
        
        ### 1. **Manifold Learning**
        
        - **Description**: Generate data that lies on or near a low-dimensional manifold within a higher-dimensional space.
        - **Approach**: Use techniques like t-SNE, Isomap, or locally linear embedding (LLE) to create complex, nonlinear structures.
        - **Example**: Generate points on a Swiss roll or an S-curve.
        
        ### 2. **Fractal Patterns**
        
        - **Description**: Create features based on fractal patterns which have self-similarity and intricate structures.
        - **Approach**: Use mathematical formulas like the Mandelbrot set or Julia set to generate data points.
        - **Example**: Generate points from a fractal formula and add noise for variation.
        
        ### 3. **Periodic Functions**
        
        - **Description**: Use periodic functions (sine, cosine) to create wave-like structures.
        - **Approach**: Combine multiple sine and cosine functions with different frequencies and amplitudes.
        - **Example**: Create data that forms a wave pattern in multiple dimensions.
        
        ### 4. **Latent Variable Models**
        
        - **Description**: Generate data from a model where observed variables are influenced by unobserved latent variables.
        - **Approach**: Use models like Gaussian Mixture Models (GMMs), Hidden Markov Models (HMMs), or Variational Autoencoders (VAEs).
        - **Example**: Generate data points influenced by a few latent factors that create interesting dependencies.
        
        ### 5. **Complex Geometric Shapes**
        
        - **Description**: Generate data based on complex geometric shapes.
        - **Approach**: Use mathematical definitions of shapes like tori, hypercubes, or spheres.
        - **Example**: Points distributed on the surface of a torus or inside a hypercube.
        
        ### 6. **Noise-Infused Patterns**
        
        - **Description**: Create data with inherent patterns but infused with various types of noise.
        - **Approach**: Define an underlying pattern (linear, quadratic) and add Gaussian, Poisson, or uniform noise.
        - **Example**: Linear trend with Gaussian noise to simulate noisy observations.
        
        ### 7. **Simulated Physical Systems**
        
        - **Description**: Model data based on physical systems or processes.
        - **Approach**: Use simulations of physical phenomena like fluid dynamics, weather patterns, or particle systems.
        - **Example**: Data points representing the movement of particles in a fluid.
        
        ### 8. **Graph-based Features**
        
        - **Description**: Generate data that represents nodes and edges in a graph.
        - **Approach**: Use graph generation algorithms like Erdos-Renyi, Barabasi-Albert, or Watts-Strogatz.
        - **Example**: Nodes representing people in a social network with edges indicating relationships.
        
        ### Example Code for Generating Data on a Swiss Roll:
        
        ```python
        import numpy as np
        import matplotlib.pyplot as plt
        from sklearn.datasets import make_swiss_roll
        
        # Generate Swiss Roll Data
        n_samples = 1000
        noise = 0.1
        X, _ = make_swiss_roll(n_samples, noise)
        
        # Plot Swiss Roll Data
        fig = plt.figure(figsize=(8, 6))
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=X[:, 0], cmap='Spectral', s=5)
        ax.set_title("Swiss Roll Data")
        plt.show()
        
        ```
        
        This code generates and visualizes data points on a Swiss roll, creating an interesting nonlinear structure in 3D space.
        
    - what's good resources for Mixture of Gaussians specific to what you used
        
        
    - these talk about clustering, not distribution sampling from an artificial distr of data. why is that?
        
        When you look for resources about Mixture of Gaussians (MoG) in the context of clustering, it's because MoG is frequently used for clustering applications. However, the same principles apply to distribution sampling, as the underlying mechanism involves modeling data with a mixture of Gaussian distributions. Here’s a more focused approach for generating synthetic data:
        
        ### Sampling from a Mixture of Gaussians
        
        1. **Understanding the Model**:
            - **Gaussian Components**: Each Gaussian component represents a cluster.
            - **Weights**: Each component has a weight (probability) indicating its prevalence.
        2. **Generating Samples**:
            - **Step-by-Step**:
                1. **Define Parameters**:
                    - Means, covariances, and weights for each Gaussian.
                2. **Component Selection**:
                    - Randomly choose a Gaussian component based on weights.
                3. **Sampling**:
                    - Sample from the chosen Gaussian distribution.
        
        ### Detailed Procedure
        
        1. **Define Parameters**:
            
            ```python
            import numpy as np
            import matplotlib.pyplot as plt
            
            # Parameters for the Gaussians
            means = [np.array([1, 1]), np.array([5, 5]), np.array([8, 1])]
            covariances = [np.array([[0.1, 0], [0, 0.1]]),
                           np.array([[0.2, 0.1], [0.1, 0.2]]),
                           np.array([[0.3, 0], [0, 0.3]])]
            weights = [0.3, 0.4, 0.3]  # Sum should be 1
            
            ```
            
        2. **Component Selection and Sampling**:
            
            ```python
            def sample_from_mog(n_samples, means, covariances, weights):
                n_components = len(weights)
                samples = []
            
                for _ in range(n_samples):
                    component = np.random.choice(n_components, p=weights)
                    sample = np.random.multivariate_normal(means[component], covariances[component])
                    samples.append(sample)
            
                return np.array(samples)
            
            # Generate samples
            n_samples = 300
            samples = sample_from_mog(n_samples, means, covariances, weights)
            
            # Plot the samples
            plt.figure(figsize=(8, 6))
            plt.scatter(samples[:, 0], samples[:, 1], alpha=0.6)
            plt.title("Samples from Mixture of Gaussians")
            plt.xlabel("Feature 1")
            plt.ylabel("Feature 2")
            plt.grid(True)
            plt.show()
            
            ```
            
        
        ### Explanation
        
        - **Parameters**: Define the means, covariances, and weights for each Gaussian component.
        - **Component Selection**: Randomly choose which Gaussian to sample from based on the weights.
        - **Sampling**: Draw a sample from the chosen Gaussian distribution.
        
        ### Additional Resources
        
        - **Scikit-learn Documentation**: Although primarily about clustering, [scikit-learn’s Gaussian Mixture](https://scikit-learn.org/stable/modules/mixture.html) provides functions that can be adapted for sampling.
        - **Statistical Textbooks**: Books like "Pattern Recognition and Machine Learning" by Christopher Bishop cover MoG in detail, including sampling.
        
        This approach allows you to create synthetic data with complex structures without predefined clusters, making it suitable for various simulations and analyses.
        
    - would umap of make_blobs or make_circles data look uniform?
        
        The UMAP (Uniform Manifold Approximation and Projection) visualization of data generated using `make_blobs` or `make_circles` would not look uniform. Here's why:
        
        ### `make_blobs`:
        
        - **Clusters**: This function generates data in distinct clusters.
        - **UMAP Visualization**: The UMAP plot would show separate clusters, each representing a blob. The data points within each cluster would be close together, but distinct clusters would be spread out.
        
        ### `make_circles`:
        
        - **Circular Patterns**: This function generates data in concentric circles.
        - **UMAP Visualization**: The UMAP plot would show circular patterns, with data points forming distinct rings. The inner and outer circles would be evident, showing non-uniform distribution.
        
        ### Example Code
        
        ### `make_blobs`
        
        ```python
        from sklearn.datasets import make_blobs
        import matplotlib.pyplot as plt
        import umap
        
        # Generate data
        X, y = make_blobs(n_samples=300, centers=3, random_state=42)
        
        # Fit and transform using UMAP
        umap_model = umap.UMAP()
        X_umap = umap_model.fit_transform(X)
        
        # Plot
        plt.scatter(X_umap[:, 0], X_umap[:, 1], c=y, cmap='viridis')
        plt.title("UMAP of make_blobs data")
        plt.xlabel("UMAP1")
        plt.ylabel("UMAP2")
        plt.show()
        
        ```
        
        ### `make_circles`
        
        ```python
        from sklearn.datasets import make_circles
        import matplotlib.pyplot as plt
        import umap
        
        # Generate data
        X, y = make_circles(n_samples=300, factor=0.5, noise=0.05)
        
        # Fit and transform using UMAP
        umap_model = umap.UMAP()
        X_umap = umap_model.fit_transform(X)
        
        # Plot
        plt.scatter(X_umap[:, 0], X_umap[:, 1], c=y, cmap='viridis')
        plt.title("UMAP of make_circles data")
        plt.xlabel("UMAP1")
        plt.ylabel("UMAP2")
        plt.show()
        
        ```
        
        ### Conclusion
        
        UMAP visualizations of `make_blobs` and `make_circles` data will highlight their inherent structures—clusters and concentric circles, respectively—demonstrating non-uniform distributions.
        
    - [https://chatgpt.com/c/c7aa4b39-5f80-4bdb-8a33-a42c67d1d1fb](https://chatgpt.com/c/c7aa4b39-5f80-4bdb-8a33-a42c67d1d1fb)
- 🐣 learn more on mixture gaussians
    - [https://builtin.com/articles/gaussian-mixture-model#](https://builtin.com/articles/gaussian-mixture-model#)
        - One important characteristic of K-means is that it’s a hard clustering method, which means that it will associate each point to one and only one cluster. A limitation to this approach is that there is no uncertainty measure or probability that tells us how much a data point is associated with a specific cluster. So what about using a soft clustering instead of a hard one?
        - A Gaussian mixture is a function that is composed of several Gaussians,
    - [https://medium.com/@juanc.olamendy/understanding-gaussian-mixture-models-a-comprehensive-guide-df30af59ced7](https://medium.com/@juanc.olamendy/understanding-gaussian-mixture-models-a-comprehensive-guide-df30af59ced7#:~:text=At%20its%20core%2C%20a%20GMM,its%20components%2C%20each%20weighted%20accordingly)
    - [https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html)
- ✅ get approval on collabs from fazl and phil
- ✅ read “feature familiies”
    - to bloom
        
        I just saw someone post in [#sparse-autoencoders](https://opensourcemechanistic.slack.com/archives/C06RB35HBDE) a new paper about "feature families", [https://arxiv.org/abs/2408.00657](https://arxiv.org/abs/2408.00657)
        
        They also have a web app: [https://huggingface.co/spaces/charlieoneill/saerch.ai](https://huggingface.co/spaces/charlieoneill/saerch.ai)
        
        Think it might be interesting to add to neuronpedia if more about feature families are investigated. Would also be interested in your thoughts on the paper in general if you've read it
        Seems relevant to what I'm doing now, they state in App E.2
        
        > Visualizing the resulting principal components confirms that the feature families we find do not represent manifolds or irreducible multi-dimensional structures. We can instead think of feature families as linear subspaces
        > 
        
        So the feature families they find (across 2 dataset embeddings too) appear to be linear subspaces, though I don't think that means all interesting structures would be linear subspaces. They also find feature families across dataset embeddings (app D). Overall I think there's a lot more to explore with linear subspace structures even if manifold strucs aren't found
        
    - bloom reply
        
        don't have a super detailed understanding of the paper (but have skimmed it) I've been thinking about related stuff for a while and have unpublished results on co-occurence and hierarchical clustering of features separately.Neuronpedia is likely to have the following in the near future:
        
        - Top-K features by cosine similarity (in dashboards)
        - Some form of graph data structure mapping features to each other
        
        However, I don't want to jump quickly on deploying particular methods published in papers (for a few reasons) so I can't say that the methods from this particular work be used. In general, our advisors seem to be fine with me using my discretion here so if I am convinced something will become a standard method we can deploy it.
        
    - msg to kiho on feature familities co-oc matrix
        
        Yes (section 4.2). Do you think their the co-occurence matrix on features to find  feature families (having an edge between high to low density features, or general to specific concepts) is related to your approach with the cosine sim matrix between child-parent vectors? 
        
    - [https://huggingface.co/charlieoneill/embedding-saes](https://huggingface.co/charlieoneill/embedding-saes)
    - [https://huggingface.co/spaces/charlieoneill/saerch.ai](https://huggingface.co/spaces/charlieoneill/saerch.ai)
- ✅ get non-unif feat distrb for ground truth features
    - ✅ [pca](https://chatgpt.com/c/aa7a414c-068b-4eae-a801-99705aec0f61)
        - **PCA and t-SNE on True Features**: These plots provide a visual representation of the high-dimensional true features in a reduced 2D space.
        - **PCA and t-SNE on Sample Data Points**: These plots give insights into how the generated data points are distributed in the reduced 2D space.
    - ✅ the pca and umap on 10000 data points made from `blobs` actually works to create clusters! Perhaps 10 mil data pts before was too many to “zoom out” so it looked uniform, but with 10k we see the clusters look diff from uniform.
- ✅ use MMCS to compare SAEs across diff synth actvs
    - ✅ [rewrite luke’s fns](https://chatgpt.com/c/345651c0-8cc8-4971-98a7-acc8f96ac128) using einops
    - ✅ need to use the SAME ground truth features! so 2 sepr fns!
    - ✅ plot umap of saes across diff synth actvs
    - ✅ MMCS for 2 diff SAEs encoder weights
        - we want low loss scores during training, and high MMCS scores
            - we find that they’re low
- ✅ https://stats.stackexchange.com/questions/534543/what-is-the-meaning-of-isotropic-gaussian-blobs-which-are-generated-by-sklearn
    
    A Gaussian mixture model is not Gaussian unless there is only one cluster, which is why your plots don't look Gaussian, but rather a combination of Gaussians.
    
- ✅ msg others about non-unif ideas using gaussian mixture models
    - reply to luke about idea to use non-unif ground truth feature space
        
        Makes sense, to design clusters in ground truth feature space I'm looking to sample from a gaussian mixture model. I was also wondering if it would make sense to somehow get already hard coded features from some decomposition. If we just use encoder weights, from a sparse feature space of another sae trained on an actual llm, as ground truth features, but I think that breaks some assumptions in that the features found may have biases from the specific llm training mixed in and wouldn't be good to generate other simulated llms from it. Not entirely sure though
        
    - email to max
        
        Thanks! The second point makes sense when comparing different models. Right now I'm using 2 sets of synthetic activations that use the same ground truth features, but with different linear combinations of them (and perhaps at different frequencies, to model properties specific to each LLM). This week I'll also try using MMCS before and after using Orthogonal Procrustes to find an alignment first. I just started reading your new paper so I'll get back to you once I finish it. Will the repo in the paper's link be public soon?
        
        Also, since I’m looking to use metrics that compare how well the SAEs for different LLMs capture the feature space (comparing how well they detect distinct clusters + shapes), I was looking to use features that form interesting arrangements with one another. I was wondering if you can check if you think this is a correct interpretation (overall, I have 2 questions):
        
        In the [“Taking features out of…” post](https://www.alignmentforum.org/posts/z6QQJbtpkEAX3Aojj/interim-research-report-taking-features-out-of-superposition), ground truth features are sampled from a uniform distribution, and they’re only made correlated when put into linear combinations, as the coefficients of the activation vectors are selected based on the feature frequencies. So the ground truth features would still form a uniform distribution, and the SAE encoder or decoder weights would also form a uniform distribution, meaning their UMAP plots wouldn’t show semantic clusters like those seen in “Scaling Monosemanticity”.
        
        **Q1:** Thus, would it make sense to modify the synthetic activations generation so that ground truth features are not from a uniform distribution but from a feature space with clusters and other shapes? I've tried sampling from a gaussian mixture model; so far this has trained bad SAEs with very high loss (think I just need more samples or tuning, I'll see).
        
        **Q2:** I was also wondering if it would make sense to somehow get already hard coded features from some decomposition? Say if we just use encoder weights, from a sparse feature space of another SAE trained on an actual llm, as ground truth features. But I think that has issues, such as the features found may have biases from the specific llm training mixed in and wouldn't be good to generate other simulated llms from it. Possibly also breaks other assumptions.
        
- ✅ [short intro overleaf](https://www.overleaf.com/project/66b09d88a32e42d4dd92d6bd)
- ✅ debug why high loss when sampling from gaussian mixture model
    - ✅ try on unif gft for 10k samps (try first bc faster)
        - the loss, while still 10x when using 10mil samples, is MUCH lower- it’s 12 compared to 1000 (for both loss and L2)
        - but calculate_MMCS(enc_weights_a, enc_weights_b) is 0.13
        - ✅ found that encoder weight is Gxh instead of hxG- so new synth actvs fn had error! Was it lack of transpose? hard to tell.
            - SOLN: no, it’s because before use `trainer.model.encoders[0].weight.detach().t().shape`, and now don’t use `.t()`
            - so we should use `calculate_MMCS(encoder.weight.detach().t(), self.Fe, self.device)` instead of not using .t() for both of them!
            - calculate_MMCS(enc_weights_a.t(), enc_weights_b.t(), device)
                - This is now 0.19 instead of 0.13; still low
            - `calculate_MMCS(enc_weights_a.t(), grTrue_feats, device)`
                - this is 0.18. it should be high; we prob don’t have enough samples this means
    - ✅ use old synth code on unif gft for 10k samp
        - loss is STILL 13
        - umap looks more spherical instead of ellipsoid
        - calculate_MMCS(enc_weights_a, enc_weights_b) is STILL 0.19
        - this same result suggests new synth fn is corr
    - ✅ more actv samps for unif
        - ✅ SOLN: now loss is ~1. This fixes it. So perhaps non-unif needs even MORE samps than 10mil
        - ✅ ISSUE: MMCS of encoder weights and gtf is still 0.18, even though it’s higher in luke’s original code (should be 0.9)
        - ✅ TRY: `true_features` was run again in the `get_synth_actvs` that uses luke’s code. so try running everything again, from 10k to 10mil samps.
            - 10k is still 0.18 MMCS between encoder and gtf
            - **SOLN:** But 10mil is 0.9 MMCS, low L2 and low AR; same as last time!
        - ✅ Now MMCS of A and B is 0.9. This is across 2 diff actv sets- are the actv sets not different enough?
    - ✅ try 5 gtf clus, more actv samps (10mil)
        - ✅ [i don't see this downloading. could it be too big?:](https://chatgpt.com/c/5e1f9417-b1e1-4511-a4c8-b111c57a0d25)
            
            yes; it downloaded another file but not this one. have to save to drive then download
            
        - ✅ what's the equivalent of this for make_blobs, given  we defined a set of ground truth features by uniformly sampling G=512 independent samples from a h-dimensional sphere. This creates a h×G matrix of ground truth features: `torch.randn(h, G, device=device, dtype=torch.float16)`
            
            [https://chatgpt.com/c/eb9bfcee-f4d5-41db-bb02-48c8a148d015](https://chatgpt.com/c/eb9bfcee-f4d5-41db-bb02-48c8a148d015)
            
            SOLN: before, chatgpt mixed up h and G bc we didn’t specify what true_features etc meant in luke’s code. now we specify what h and G are, so more accurate
            
            - i dont want to get exactly like standard normal distribution, I want a gaussian mixture model. just wanted to know where to put h and G correctly ffrom before
        - loss is MCUH better (17 loss, 7 L2) and 0.5 MMCS. Still not as good as MMCS tho.
        - ✅ MMCS between SAEs is VERY low 0.2- which is almost same as random. So we’re not finding commonalities or the common feature subspace.
- 🐣 use other metrics to compare SAEs on diff synth actvs (of non-unif)
    - [https://github.com/mklabunde/llm_repsim](https://github.com/mklabunde/llm_repsim)
    - [what's an orthogonal_procrustes of 3.3 mean](https://chatgpt.com/c/668babf2-e00f-451f-b027-588062c0452f)
        - what's the scale 3.3 falls on? for instance cosine sim is 0 to 1
    - what does jaccard similarity of 0.15 mean
        
        A value of 0.15 indicates that only 15% of the total elements (considering both sets) are common to both sets.
        
- ✅ compare diff metrics (of unif)
    - jaccard is higher (0.69) and orth procr is low (1.1 instead of 3)
- ✅ reflect (so far)
    
    on the plus side, for MMCS and jaccard, we get similar uniform distrb. but the saes seem to not be similar for non-unif distrb. this may be due to the saes not finding the ground truth features well enough.
    
    This means when MMCS (indiv feature matching) is high, the feature relations (jaccard) are also high?
    
- ✅ [If MMCS is high and jaccard both correlate in being high, does that mean if individual discrete features match (MMCS), then feature relations (jaccard) also correlate?](https://chatgpt.com/c/543e4ecc-bca1-4f88-b5de-0531044ad649)
    
    Yes, if both the Mean Max Cosine Similarity (MMCS) and the Jaccard index are high, it implies that there is a correlation between the presence of individual discrete features (MMCS) and the relationships between these features (Jaccard index). In other words, when discrete features match closely, the relationships or overlaps between these features also tend to be strong. This indicates that features identified by sparse autoencoders, which minimize the reconstruction loss and maximize sparsity, capture both individual feature similarities and their relational structure effectively.
    
- ✅ contact dan/beren/Robert_AIZI on clusters mnn
    - Questions from University of Oxford intern about synthetic activations sampling
        
        Hi, I’m currently a research intern at the University of Oxford working on a research project involving synthetic activations based on this approach that you worked on: [https://www.alignmentforum.org/posts/z6QQJbtpkEAX3Aojj/interim-research-report-taking-features-out-of-superposition](https://www.alignmentforum.org/posts/z6QQJbtpkEAX3Aojj/interim-research-report-taking-features-out-of-superposition)
        
        I’m looking to modify the setup to train SAEs on multiple sets of activations, each simulating a different LLM, that are combinations of ground truth features sampled from a space where the features form interesting arrangements with one another, such clusters or circles. I was wondering how sound these modifications are:
        
        1. Would it be sound to sample ground truth features from a Gaussian Mixture Model (using make_blobs in scikitlearn) instead? Not sure if the uniform distribution is necessary to say, allow the cosine sim to be low and not always/mostly be high (due to skewness).
        2. To simulate multiple LLMs (where we know the ground truth features), I’m looking to use different sets of activations that are sparse linear combinations of the same matrix of ground truth features. Would I have to use different ways to get frequencies of feature activations to simulate different LLMs, to make sure they differ enough? Not sure what I’d need to do to achieve this yet, so I am open to advice.
        3. Would it be sound to use hard coded ground truth features, say using the encoder weights of an SAE trained on an actual llm? I think that has issues, eg) the features found may have biases from the specific llm training mixed in and wouldn't be good to generate other simulated llms from it.
        
        I can explain more about what the project actually is if you are interested, but I was looking to first keep my questions as short as possible. Thanks!
        
- ✅ change luke’s code to be different enough: synth data
    
    [synthData_explora_v2.ipynb](https://colab.research.google.com/drive/1S9GlHc60Y_SD3EN4D27GBLSpGPPhrR-l#scrollTo=Tdr-XiFEGDgR)
    
    - ✅ [https://chatgpt.com/c/7936706a-1c66-4a43-9dbb-9b8fa32b225a](https://chatgpt.com/c/7936706a-1c66-4a43-9dbb-9b8fa32b225a)
        - explain what every line of code in here does with comments
            
            ```python
            def get_synth_actvs(synth_features, total_data_points, num_features, num_true_features, device):
                # Define constants for the synthetic activations generation process
                num_active_features_per_point = 32
                decay_rate = 0.99
                num_feature_groups = 12
                batch_size = 1000
            
                # Calculate the size of each feature group and create groups of feature indices
                group_size = num_true_features // num_feature_groups
                feature_groups = [torch.arange(i * group_size, (i + 1) * group_size, device=device) for i in range(num_feature_groups)]
            
                # Create probability distributions for each group based on the decay rate
                group_probs = [torch.pow(decay_rate, torch.arange(group_size, device=device, dtype=torch.float16)) / (1 - decay_rate) for _ in range(num_feature_groups)]
            
                # Initialize a list to store batches of synthetic activations
                batches = []
            
                # Loop over the data points in chunks of 'batch_size'
                for batch_start in tqdm(range(0, total_data_points, batch_size), desc="Generating Batches"):
                    # Adjust the batch size for the last batch if necessary
                    batch_size = min(batch_size, total_data_points - batch_start)
            
                    # Initialize a tensor to store the coefficients for the features
                    coeffs = torch.zeros(batch_size, num_true_features, device=device, dtype=torch.float16)
            
                    # Randomly select a feature group for each data point in the batch
                    selected_groups = torch.randint(num_feature_groups, (batch_size,), device=device)
            
                    # Loop over each feature group and its corresponding probabilities
                    for i, (group, probs) in enumerate(zip(feature_groups, group_probs)):
                        # Create a mask to identify which data points belong to the current group
                        mask = selected_groups == i
                        if mask.any():
                            # Randomly select feature indices from the current group based on the probabilities
                            indices = group[torch.multinomial(probs, num_active_features_per_point, replacement=False)]
                            # Assign random coefficients to the selected features for the masked data points
                            coeffs[mask.nonzero(as_tuple=True)[0].unsqueeze(1), indices] = torch.rand(mask.sum(), num_active_features_per_point, device=device, dtype=torch.float16)
            
                    # Multiply the coefficients by the transpose of the true features to get the synthetic activations
                    batch_data = torch.mm(coeffs, true_features.T)
                    
                    # Append the batch data to the list after moving it to the CPU
                    batches.append(batch_data.cpu())
            
                    # Clean up the GPU memory by deleting unnecessary tensors and emptying the cache
                    del coeffs, batch_data
                    torch.cuda.empty_cache()
            
                # Concatenate all batches into a single tensor and return it
                return torch.cat(batches)
            
            ```
            
        - relate that code to the procedure in the paper linked that discusses "To better simulate the expected statistical properties of features in real neural data". cite the code and the quoted lines it matches to
            
            The code provided can be related to specific procedures and concepts discussed in the paper "Taking features out of superposition with sparse autoencoders" to simulate the statistical properties of features in real neural data. Here's how the code aligns with the methodology described in the paper:
            
            ### Setting Up the Feature Groups
            
            - **Code**:**Paper**:
                
                ```python
                num_feature_groups = 12
                group_size = num_true_features // num_feature_groups
                feature_groups = [torch.arange(i * group_size, (i + 1) * group_size, device=device) for i in range(num_feature_groups)]
                
                ```
                
                > "To simulate the expected statistical properties of features, we divide the features into several groups, each representing a distinct statistical distribution."
                > 
            
            ### Probability Distribution and Decay Rate
            
            - **Code**:**Paper**:
                
                ```python
                decay_rate = 0.99
                group_probs = [torch.pow(decay_rate, torch.arange(group_size, device=device, dtype=torch.float16)) / (1 - decay_rate) for _ in range(num_feature_groups)]
                
                ```
                
                > "We assign probabilities to features within each group using a decay rate, ensuring that some features are more likely to be active, reflecting their statistical distribution in real data."
                > 
            
            ### Generating Batches of Data
            
            - **Code**:**Paper**:
                
                ```python
                for batch_start in tqdm(range(0, total_data_points, batch_size), desc="Generating Batches"):
                    batch_size = min(batch_size, total_data_points - batch_start)
                    coeffs = torch.zeros(batch_size, num_true_features, device=device, dtype=torch.float16)
                    selected_groups = torch.randint(num_feature_groups, (batch_size,), device=device)
                
                ```
                
                > "To manage computational resources, we generate synthetic activations in batches, ensuring each batch is processed efficiently."
                > 
            
            ### Random Selection of Features
            
            - **Code**:**Paper**:
                
                ```python
                for i, (group, probs) in enumerate(zip(feature_groups, group_probs)):
                    mask = selected_groups == i
                    if mask.any():
                        indices = group[torch.multinomial(probs, num_active_features_per_point, replacement=False)]
                        coeffs[mask.nonzero(as_tuple=True)[0].unsqueeze(1), indices] = torch.rand(mask.sum(), num_active_features_per_point, device=device, dtype=torch.float16)
                
                ```
                
                > "Within each batch, features are selected randomly from their respective groups based on predefined probabilities, simulating the feature activation patterns observed in neural networks."
                > 
            
            ### Combining Coefficients and Features
            
            - **Code**:**Paper**:
                
                ```python
                batch_data = torch.mm(coeffs, true_features.T)
                batches.append(batch_data.cpu())
                del coeffs, batch_data
                torch.cuda.empty_cache()
                
                ```
                
                > "The coefficients are multiplied by the transpose of the true features matrix to generate the final synthetic activations, which are then concatenated across batches."
                > 
            
            By following these steps, the code effectively implements the methodology outlined in the paper to simulate the statistical properties of features in real neural data. You can find more details in the full report [here](https://www.alignmentforum.org/posts/z6QQJbtpkEAX3Aojj/interim-research-report-taking-features-out-of-superposition).
            
        - did the original post use feature groups when making some features have more prob than others? cite the line it says this
            - you hallucinated that
        - does the code make correlations using a random covariance matrix for a multivariate normal distribution with zero mean?
            
            The code provided does not directly create correlations using a random covariance matrix for a multivariate normal distribution with zero mean. Instead, it appears to create synthetic activations through a sparse combination of features with certain probabilities assigned to each feature within groups. Let's break down the relevant parts of the code to illustrate this.
            
            ### Key Parts of the Code
            
            1. **Feature Groups Creation**:
                
                ```python
                num_feature_groups = 12
                group_size = num_true_features // num_feature_groups
                feature_groups = [torch.arange(i * group_size, (i + 1) * group_size, device=device) for i in range(num_feature_groups)]
                
                ```
                
            2. **Assigning Probabilities with a Decay Rate**:
                
                ```python
                decay_rate = 0.99
                group_probs = [torch.pow(decay_rate, torch.arange(group_size, device=device, dtype=torch.float16)) / (1 - decay_rate) for _ in range(num_feature_groups)]
                
                ```
                
            3. **Generating Coefficients and Activations**:
                
                ```python
                coeffs = torch.zeros(batch_size, num_true_features, device=device, dtype=torch.float16)
                selected_groups = torch.randint(num_feature_groups, (batch_size,), device=device)
                
                for i, (group, probs) in enumerate(zip(feature_groups, group_probs)):
                    mask = selected_groups == i
                    if mask.any():
                        indices = group[torch.multinomial(probs, num_active_features_per_point, replacement=False)]
                        coeffs[mask.nonzero(as_tuple=True)[0].unsqueeze(1), indices] = torch.rand(mask.sum(), num_active_features_per_point, device=device, dtype=torch.float16)
                
                batch_data = torch.mm(coeffs, true_features.T)
                
                ```
                
            
            ### Explanation
            
            - **Feature Groups and Probabilities**: The code divides features into groups and assigns probabilities to each feature within a group using a decay rate. This does not explicitly involve a covariance matrix or multivariate normal distribution.
            - **Sparse Coefficients**: It generates coefficients for features, ensuring sparsity by selecting a subset of features for each data point and assigning random values to them.
            - **Matrix Multiplication**: Finally, it multiplies these coefficients with the true features to generate synthetic activations.
            
            ### What the Code Does Not Do
            
            - **Random Covariance Matrix**: The code does not generate or use a random covariance matrix.
            - **Multivariate Normal Distribution**: There is no use of a multivariate normal distribution with zero mean.
            
            ### Conclusion
            
            The code simulates synthetic activations through a structured process of feature grouping and probability assignment, but it does not create correlations via a random covariance matrix for a multivariate normal distribution. Instead, it focuses on sparse combinations of features, influenced by predefined probabilities.
            
            For further context on using covariance matrices and multivariate normal distributions in generating correlated data, additional resources on statistical methods and machine learning practices would be helpful.
            
    - ✅ 🐣 luke’s **synth fn explora and relate to origpost and luke’s paper**
        - don’t use feature groups, as that’s luke’s mod. understand orig way to corr feats
        - understand luke’s corr algo
            - in paper
                
                ![Untitled](Start%20Sim%20Metric%20+%20TDA%20Expms%20b27936470f68400dba996b4f43a4e1c6/Untitled%204.png)
                
            - [By selecting a subset of features based on the decaying probability distribution, the code ensures that certain features within a group are more likely to be activated together.](https://chatgpt.com/c/674974e8-3ed8-4c2b-a8f8-61e82334b00d)
                
                The code you provided introduces correlations between features through several mechanisms embedded within the process of generating synthetic activations. Let's break down these mechanisms step by step:
                
                ### 1. Feature Grouping
                
                The code divides the true features into groups:
                
                ```python
                group_size = num_true_features // num_feature_groups
                feature_groups = [torch.arange(i * group_size, (i + 1) * group_size, device=device) for i in range(num_feature_groups)]
                
                ```
                
                Here, the total number of true features (`num_true_features`) is divided into several groups (`num_feature_groups`). Each group contains a subset of features. This initial grouping step is crucial for introducing correlations because features within the same group are treated together in subsequent steps.
                
                ### 2. Group Probability Distribution
                
                Each feature group is assigned a probability distribution that decays exponentially:
                
                ```python
                group_probs = [torch.pow(decay_rate, torch.arange(group_size, device=device, dtype=torch.float16)) / (1 - decay_rate) for _ in range(num_feature_groups)]
                ```
                
                This creates a bias towards selecting certain features within each group more frequently than others. The decay rate (`decay_rate = 0.99`) ensures that the first features in each group have higher probabilities, thus making these features more likely to be selected together.
                
                ### 3. Batch Processing and Group Selection
                
                For each batch of data points, a group is randomly selected for each data point:
                
                ```python
                selected_groups = torch.randint(num_feature_groups, (batch_size,), device=device)
                
                ```
                
                Each data point (within a batch) will have its active features selected from the same group, further enforcing the correlation between features within the same group.
                
                ### 4. Feature Selection Within Groups
                
                Within each selected group, a fixed number of features (`num_active_features_per_point`) are chosen based on the pre-defined probability distribution:
                
                ```python
                indices = group[torch.multinomial(probs, num_active_features_per_point, replacement=False)]
                
                ```
                
                By selecting a subset of features based on the decaying probability distribution, the code ensures that certain features within a group are more likely to be activated together. This reinforces the correlation among these features.
                
                ### 5. Coefficient Assignment
                
                The selected features for each data point are assigned random coefficients:
                
                ```python
                coeffs[mask.nonzero(as_tuple=True)[0].unsqueeze(1), indices] = torch.rand(mask.sum(), num_active_features_per_point, device=device, dtype=torch.float16)
                
                ```
                
                This step assigns non-zero values to the selected features, effectively "activating" them for each data point.
                
                ### 6. Synthesis of Feature Activations
                
                Finally, the synthetic feature activations are generated through a matrix multiplication:
                
                ```python
                batch_data = torch.mm(coeffs, synth_features.T)
                
                ```
                
                The `coeffs` matrix, which contains the selected and activated features for each data point, is multiplied with the transpose of the `synth_features` matrix. This process generates the final synthetic activations where features within the same group exhibit correlated activations due to the way they were selected and assigned coefficients together.
                
                ### Summary
                
                Correlations between features are introduced primarily through:
                
                1. **Grouping of features**: Features are divided into groups, and each group is treated as a unit.
                2. **Decaying probability distribution within groups**: Certain features within a group are more likely to be selected together.
                3. **Consistent group selection for each data point**: All active features for a data point come from the same group, enforcing intra-group correlations.
                4. **Coefficient assignment and activation**: Selected features are assigned coefficients, creating correlated activations.
                
                Overall, this systematic approach ensures that specific sets of features are more likely to be active together, thus introducing correlations into the synthetic dataset.
                
        - The orig post’s correlations use a cov matrix between features not within a group, while luke’s uses groups that act as ‘preset corrs’ such that featuers within a group are all corr.
    - ✅ [understand orig post to corr features](https://chatgpt.com/c/3a32e07a-515b-4c3e-b91e-cd37d59156d3)
        - i dont get why using that cov matrix, sampling from corr multinorm dist, then finding where it lies on standard normal cumulative distribution function, makes correlation bewteen features
            
            To understand the process of creating correlations between features using the method described, let's break it down step by step:
            
            1. **Creating a Random Covariance Matrix**:
                - A random covariance matrix for a multivariate normal distribution with zero mean is created. This matrix defines how the different dimensions (features) are correlated.
            2. **Sampling from a Correlated Multivariate Normal Distribution**:
                - Using the random covariance matrix, a single sample is drawn from this multivariate normal distribution. This sample represents a point in a high-dimensional space where each dimension corresponds to a feature.
            3. **Transforming to Standard Normal Cumulative Distribution**:
                - For each dimension of the sample, the corresponding value is transformed using the standard normal cumulative distribution function (CDF). This transformation maps the values to a range between 0 and 1.
            
            Here’s why this process creates correlations between features:
            
            ### Why it Works:
            
            - **Correlated Multivariate Normal Distribution**: When you sample from a multivariate normal distribution with a specified covariance matrix, the resulting sample will inherently have the correlation structure defined by the covariance matrix. If two features are positively correlated in the covariance matrix, they are more likely to have values that move together (both high or both low) in the sample.
            - **Transformation Using CDF**: Applying the standard normal CDF to each dimension of the sample maintains the correlation structure. The CDF transformation is a monotonic function, which means it preserves the order of values. Therefore, the relative positioning (and hence the correlation) between values in different dimensions remains intact.
            
            ### Example:
            
            1. **Covariance Matrix**: Suppose you have a covariance matrix that defines a positive correlation between feature A and feature B.
            2. **Sample**: Drawing a sample might give you a point where both the values for A and B are high.
            3. **CDF Transformation**: Applying the CDF will map these high values to a range between 0 and 1, but since the transformation is order-preserving, both A and B will still be relatively high compared to other features, maintaining their correlation.
            
            ### Summary:
            
            The key idea is that the correlation structure imposed by the covariance matrix on the multivariate normal distribution is preserved through the sampling and transformation steps. The resulting vector (with values between 0 and 1) has the same correlation pattern as defined by the original covariance matrix, which translates to correlated feature activations.
            
            This procedure effectively creates a binary random vector where some features are more likely to be active together, reflecting the correlations specified in the covariance matrix.
            
        - how is this done in detail: Using the random covariance matrix, a single sample is drawn from this multivariate normal distribution.
        - so the correlated multivariate normal distribution uses the random covariance matrix for a multivariate normal distribution with zero mean?
        - intuitively explain why this is done: for each dimension of that sample, found where that sample lay on the standard normal cumulative distribution function.
            
            To intuitively explain why we find where each dimension of the sample lays on the standard normal cumulative distribution function (CDF), let’s break down the process and its purpose:
            
            ### Context
            
            The goal is to create a vector where features (dimensions) have certain correlations and are more likely to be active together. This process involves generating samples that respect the correlation structure defined by a covariance matrix and transforming them into a specific range, typically between 0 and 1.
            
            ### Key Steps
            
            1. **Generate Correlated Samples**:
                - We start with a sample from a multivariate normal distribution that has the desired correlation structure defined by the covariance matrix. This sample reflects how features are correlated in a continuous space.
            2. **Map to a Uniform Distribution**:
                - The next step is to transform these continuous, normally distributed values into a uniform distribution in the range [0, 1]. This transformation is achieved using the standard normal cumulative distribution function (CDF).
            
            ### Why Use the Standard Normal CDF?
            
            ### Intuition Behind the CDF Transformation
            
            - **Standard Normal Distribution**: The standard normal distribution is a bell-shaped curve where values closer to the mean (0) are more probable, and values further from the mean are less probable.
            - **Cumulative Distribution Function (CDF)**: The CDF of the standard normal distribution tells us the probability that a random variable from this distribution is less than or equal to a given value. It maps values from the normal distribution to a uniform distribution between 0 and 1.
            
            ### Preserving Correlation Structure
            
            - **Order-Preserving Transformation**: The CDF is a monotonically increasing function. This means if one value is larger than another in the normal distribution, it remains larger after the CDF transformation. Thus, the relative order (and thereby the correlation structure) of the features is preserved.
            - **Uniform Distribution**: After applying the CDF, the values are transformed into a uniform distribution. This makes it easier to handle these values in subsequent steps, as they are now bounded between 0 and 1.
            
            ### Example
            
            Imagine we have two correlated features, A and B:
            
            1. **Correlated Normal Samples**: From the multivariate normal distribution, we might get samples where both A and B are high due to their positive correlation.
            2. **Applying CDF**: By applying the CDF to each of these samples, we transform high values into values close to 1 and low values into values close to 0. Importantly, if A is higher than B in the original sample, it will still be higher after the transformation.
            
            ### Summary
            
            The process of mapping each dimension of the sample to the standard normal CDF:
            
            - **Transforms the distribution**: Converts normally distributed samples to uniformly distributed samples between 0 and 1.
            - **Maintains correlations**: Keeps the relative relationships between dimensions, thus preserving the correlation structure defined by the covariance matrix.
            - **Standardizes values**: Puts values in a common range [0, 1], facilitating subsequent analyses or transformations.
            
            This approach ensures that we maintain the desired correlation structure while transforming the values into a form that is more manageable and standardized for further processing.
            
    - ✅ [orig procedure code](https://chatgpt.com/c/8fc2dce5-adc0-4f8c-b300-58156d37dc81)
        - don't use feature groups, use your original code. quote from the original post from below (which comes from the link) to explain each part of the code. add in thigns that weren't there. the aim is to get an torch tensor output of synth actvs of size numsamps x modelDims given (synth_features, total_data_points, num_features, num_true_features) in a function. synth_features is hxG, where h is modelDim and G is feature dim.
        - synth_features is a torch tensor that may be on gpu made by:
        `device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        synth_features = torch.randn(model_dims, feature_dims, device=device, dtype=torch.float16)`
        modify the above fn you made to use torch tensor based on device, not np array
        - what's the slower parts of the batch loop? how much slower?
        - would it be possible and faster to do sampling and transformations outside of batch loop, and just do matmul inside batch loop? or not?
        - why this? is it to change samples into probs? what was samples before?:
        `samples = np.random.multivariate_normal(mean, cov_matrix, batch_size_current) 
            uniform_samples = norm.cdf(samples)  # (batchNumSamps, G) in (0,1) range`
        - `decay_factors = decay_rate ** indices  #
        decayed_probs = uniform_samples * decay_factors`
        is this the same as taking each prob in uniform_samples and raising to the power of (ind * lambda)?
    - ✅ code new synth actv fn
        - ✅ synth actvs needs to be in `numsamps x modelDims` since it’s the model actvs, not features
        - ✅ use 1000000 isntead of 10000000 bc batch gen is slower with orig method
            - but this gets high loss (~50) and low cosine sim (0.2)
            - 10000000 same loss and low sim ; takes 33mins per group to run this; 1mil is 3m. for a100
        - ✅ debug by starting only from first step and seeing if SAE can recover
            - ISSUE: `binary_sparse_coeffs` has 45% ones! This depends on `rescaled_probs_tensor,` which multiplies the decay probs by a scaling factor `avg_active_feats / mean_prob`, which is 75. So that’s very big
                - The “ratio of the number of ground truth features that are active at a time (5
                out ofGin this case) to the mean probability”- this ratio is not 5, but 5 out of G. chatgpt got that wrong.
                - Also, use `torch.bernoulli(rescaled_probs_tensor)` instead of `(torch.rand(total_data_points, G, device=device, dtype=dtype) < rescaled_probs_tensor).float()`
                - Finally, this gives a tensor with sum of ones being 0.06, which is the same as the ratio 32/512
            - explain intuitively why each step in the attached image is used. for instance, why the ratio? why multiply by this ratio? how, codewise, to parameterize a vector of Bernoulli random variables?
            - SOLN: This changes 1mil sample score from 0.2 to 0.4 to 0.7, and with 28 loss (half the loss of 70). Perhaps try 10mil samps now
        - ✅ comment well, quoting orig post
        - ✅ make sure it gets similar MMCS results as old fn
            - 1mil samps: for some reason, sae1 in both datasets has worse perf, and lower sim (as it doesnt recover ground truth as well)
            - 10mil samps: both saes have VERY high cosine sim with GTF (0.97, 0.98) for SAE A, higher than for Luke’s synth actvs
                - not only that, but SAE A1 and SAE B1 have high cosine sim with each other!
                - however, these SAEs take a while to train
    - ✅ clean up and send to Robert Huben to check: [test_synthActvs.ipynb](https://colab.research.google.com/drive/16HzLfM-3OG_5AkPlkAz63fSltx85zRnB)
    - ✅ Add in overleaf about synth actvs not sharing same ground truth feats
        
        These experiments are only used to verify which methods. Real LLMs are not expected to share the exact same ground truth features; however, in these experiments, the synthetic activations are allow to share them because we are testing ideal cases for measuring how well metrics are for capturing the same ground truth features. We also vary these experiments to measure synthetic activations that share only a percentage of ground truth features in their linear combinations; for instance, given sets of features A, B and C, synthetic activation $S_1$ is a linear combination of features A and B, and synthetic activation $S_2$ is a linear combination of features A and C.
        
    - ✅ undestand correlation matrix sampling: [https://numpy.org/doc/stable/reference/random/generated/numpy.random.multivariate_normal.html](https://numpy.org/doc/stable/reference/random/generated/numpy.random.multivariate_normal.html)
        - The multivariate normal, multinormal or Gaussian distribution is a generalization of the one-dimensional normal distribution to higher dimensions. Such a distribution is specified by its mean and covariance matrix.
        - the output dim is (num samps, cov mat dim). cov mat is square, so it’s the first dim of it. numsamps can be multiple dims; in our case, we only use 1D for numsamps.
        - [why cov should be pos semidef](https://chatgpt.com/c/f989835e-4d44-4ac6-98a7-164674896a45)
            
            Variance, by definition, cannot be negative. 
            
            the eigenvalues of the covariance matrix represent the variances along the principal components of the data. Negative eigenvalues would imply imaginary variances, which are not meaningful in real-valued data.
            
    - ✅ try new synth actv code for gmms
        - for some reason, synth actvs when using samples from gmm is faster (~15m for 10mil samps)
        - OOM error so restart when doing this; also in batch, del the batch and clear cache after saving it to batches list
            - continues; save actvs for each LLM and run sae, then delete actvs before making new actvs for new LLM
            - even this isn’t enough. you have to save to drive, disconn, then run for X_b.
        - ISSUE: matmul error
            - SOLN: bc shouldn’t transpose before returning makeblobs samples. Now when get actvs, is around same as unif (~33m)
        - RESULT: 0.5 sim between A and B, and for each with GTF
    - ✅ try new synth actv code for jaccard and other metrics
        
        0.5 jaccard for clust data
        
- change luke’s code- SAEs and MMCS
    
    [synthData_explora_v3](https://colab.research.google.com/drive/1g44mZQNDMx7RiUvvIeZkeSYmN1srD53U).ipynb
    
    - ✅ first run using luke’s saes without AR loss
        
        Note that AR uses MMCS, as it’s specific to luke’s paper
        
        However, the prev runs sets its as false in params. so we expect it didn’t use
        
        - same results as last time
    - use sae class from arena in synth actv code
        - ✅ both saelens and eleuther tutorials dont show how to use actvs from custom models, just existing ones. so look at their sae code for your own saes
        - compare to luke’s code
            - ✅ no need for param search for now; use same params for just 2 saes
            - ✅ Both uses `torch.optim.Adam(list(self.parameters()), lr=lr)`, and don’t change this lr from the start (so it’s constant)
                - luke puts lr in params, which stores in config in Trainer, while ARENA only puts lr in when training by calling `.optimize`
            - ✅ luke’s train uses 1 epcoh (in params) but batch size of 2048 from train loader, meaning it goes thru all samples once but in batches
            - minibatch fwd on data
                - WRONG STM: ARENA doesn’t do minibatch proc on actvs (`h`), just entire batch. luke uses train loader to do batch proc.
                    - no, you delete this code from orig nb bc you used saes on small data:
                        
                        ```python
                         # Get a batch of hidden activations from the model (for the training step & the neuron resampling)
                        with t.inference_mode():
                            features = model.generate_batch(batch_size)
                            h = einops.einsum(features, model.W, "batch instances feats, instances hidden feats -> batch instances hidden")
                        ```
                        
                        you replaced it with: `h = self.model_h`
                        
                - however, ARENA uses `generate_btach`, which takes a rand btach of data. So each step is an epoch. We don’t want this for synth actvs; we want to go thru entire batch. That’s why we should use `for X_batch, in train_loader:`
                - both luke and eleuther uses `from torch.utils.data import DataLoader, Dataset`
                    - instead of passing in `h` for ARENA’s `autoencoder = AutoEncoder(ae_cfg, h)`, pass in `DataLoader` obj. Luke first turns the tensor into `TensorDataset`from torch.utils.data . Eleuther uses `Dataset`
                - `X_batch`  is the same as `h?`
                    - no; `h` is 3 dims because it contains the num of saes being broadcast. It’s `batch_size n_instances n_input_ae`, whereas dataloader batch is is `batch_size, n_input_ae`. Aside from einsum you must change `W_enc` to be 2dim, not 3dim. Same with `b_enc`
                - Luke uses `self.model(X_batch)`, which calls `forward` on top actvs to get `encoded` and passes encoded through linear
                    - [https://chatgpt.com/c/2beea028-78ba-4358-9fb5-fc405df48302](https://chatgpt.com/c/2beea028-78ba-4358-9fb5-fc405df48302)
                        - what is the output of model(X_batch) when model = SparseAutoencoder(params)? does forward pass do one encoder matrix multiply, or does encoder matrix on X_batch then decoder?
                        - if it doesn't do decoding how does this work when output = model(X_batch):
                        l2_loss: torch.Tensor = sum(self.criterion(output, X_batch) for output in outputs)
                            
                            
                            Even though the current implementation doesn’t explicitly include a decoder, the final linear transformation with normalized weights acts as a form of reconstruction, transforming the encoded sparse representation back to a space that can be compared to the input `X_batch`
                            
                    - I figured out that `self._topk_activation(encoder(x))` does the encoder operation because it contains `encoder(x).` This is the same as ARENA’s `acts`. THEN top K is done. This is because TOPK replaces ReLU, which is done after encoder mutlp.
                    - like openai, luke uses tied weights, repr decoder as `normalized_weights.t())`
            - delete the dead neurons code; won’t need it when doing topK?
        - first run on small actv samps to make sure enc is G x h, so that `.t()` is hxG
            - in luke’s why is
            
            ```
            self.encoders: nn.ModuleList = nn.ModuleList([
                        nn.Linear(self.config["input_size"], self.config["hidden_size"] * (i + 1))
                        for i in range(self.config.get("num_saes", 1))
                    ])
            ```
            
            but `trainer.model.encoders[0].weight.detach().t().shape` is hxG, the opposite?
            
            - `enc = nn.ModuleList([            nn.Linear(256, 512)            for i in range(1)        ])
            enc[0].weight.shape`
            why is this 512x256 instead of 256x512
                
                [https://chatgpt.com/c/fe761a2a-475e-456a-aa71-038bdb439e35](https://chatgpt.com/c/fe761a2a-475e-456a-aa71-038bdb439e35)
                
                In PyTorch, the `nn.Linear` layer's `weight` matrix has the shape `(out_features, in_features)`. This means that if you create a `nn.Linear` layer with 256 input features and 512 output features, the weight matrix will be of shape `(512, 256)`.
                
            - this means it’s ok that ARENAs is hxG, just transpose it when taking cosine sim. ARENA’s is actually wrong though, it should be Gxh instead of hxG. It’s just that einsum will automatically fix this when mm. In math notation, we use Wx. But arena uses xW to demonstrate einsum’s ability to disregard this.
        - make sure it gets similar results as old fn
    - new MMCS code
    - use top k from eleuther

Reflect on next direction

- ✅ If these actvs are just lin combos of same GTF, that doesn’t seem like “different models”. rather the same model!
    - we need to create 2 different GTF sets that share the same GTF. We should only expect the the shared subset of features to be learned from both- thus, we should apply the metrics to the subset, vs not the subset. This way, we expect the metrics to work well on the subset- if they don’t, they’re bad metrics. We must compare the GTF to each SAE- if it’s high, then we compare the SAEs.
        - this is bc we aim to find what parts of the model are shared. and to determine what relations they share.
- ✅ what’s the point of checking these metrics if we already assume they SHOULD be expected to learn the GTF relations? Actually, it’s because we don’t know if they will learn the relations of the GTF too. We use MMCS to see they learn similar features. But that doesn’t mean those features will arrange the same way. So this is not a way to check if those metrics work; they should already work. We’re checking if models learn GTF relations. As such, we don’t need across models, actually- just SAE to GTF.
    - so it’s not even a ‘precursor’ at all- we can directly apply to both real world LLM and synthetic simult. synthetic is ANOTHER expm in parallel to verify if these relations learned are actual ground truth relations, not just spurious across models.
    - more so we need a way to hone in on the subset of features. this is a new method.
    - also to statistically find how well this method works, but this isn’t needed. we can just do this for multiple models.
- ✅ how can Jaccard (KNN), RSA and CKA be used if no data to act as instances? I think you have to use them on activations, not weight matrices.
    - so any result you get on weight mats is false
    - just use the orig samples as activations thru these weight matrices to get actvs to compare by instances
        - you dont need training actvs; can use completely new actvs that must be made from same GTF matrix. this way, both models ahve new actvs (as they were trained from diff actvs).
    - we can also match the features by their actvs, but this isn’t 1-1 and can break the metric (and KNN). We need instances.
        - ask Max if we can do this though.

Measure and Match Feature Subspaces

- ✅ Brainstorm algorithm steps
    - Get highly correlated features
    - Find nearby features which also have high corr
        - their distance in high dim space. for now, just if they’re in same cluster?
    - Measure repr similarity on subset
- ✅ [jaccard_subset_ts_1L_2L.ipynb](https://colab.research.google.com/drive/1LIHrRNnB2rPp197QGLyji7a1IJNeI_g9#scrollTo=nKQgHI_BvyBq)
    - [Check jaccard sim knn if uses indices of matrix](https://chatgpt.com/c/b17bcc9b-c69d-48ac-9e0c-1a778bdda2e2)
        - yes it does
        - Is it illusion for random to always be lower? no
    - It might be bcause the subset matches them? or it stacks them row by row, so that doesn’t make sense. unless it doesn’t stack them by orig index orders
        - examplie pic
            
            ![Untitled](Start%20Sim%20Metric%20+%20TDA%20Expms%20b27936470f68400dba996b4f43a4e1c6/Untitled%205.png)
            
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
            
            ![Untitled](Start%20Sim%20Metric%20+%20TDA%20Expms%20b27936470f68400dba996b4f43a4e1c6/Untitled%206.png)
            
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
- ✅ also, it’s obv that once tokens are more similar in dist. so perhaps we should take one repr from “once”, one repr from “time”, etc and ocmpare them across models. no; that’s not knn then, but some other metric.
    
    [https://colab.research.google.com/drive/1LIHrRNnB2rPp197QGLyji7a1IJNeI_g9#scrollTo=FYUuyrMPLl_G&line=1&uniqifier=1](https://colab.research.google.com/drive/1LIHrRNnB2rPp197QGLyji7a1IJNeI_g9#scrollTo=FYUuyrMPLl_G&line=1&uniqifier=1)
    
    - use n_neigh (k) as low if only a few samps, or we need to do this for many representatives as nn being 11 (more like 10, since it includes self at first then cuts it off)
- ✅  [actually see WHAT are the nearest neighbors.](https://colab.research.google.com/drive/1LIHrRNnB2rPp197QGLyji7a1IJNeI_g9#scrollTo=GxkwjaSub0S4&line=1&uniqifier=1)
    - “he” seems to be in common with all feats from A, and once seems to be common in both
- ✅ actually see WHAT COMMON neighs the two spaces have
    - [if we take intersection, “once” is the most common. that’s obvious- all things should be connected to once, given how common it is to start a story](https://colab.research.google.com/drive/1LIHrRNnB2rPp197QGLyji7a1IJNeI_g9#scrollTo=eA0lEjgkbJwc&line=2&uniqifier=1)
- ✅ [only take NN of 1-1 features; get rid of features in B that map to features in A that were already mapped to](https://colab.research.google.com/drive/1LIHrRNnB2rPp197QGLyji7a1IJNeI_g9#scrollTo=lKWc6tiaLGmg&line=1&uniqifier=1)
    - RESULT: even without repeats in feats_A, the jaccard sim of “she” features is higher than random of same size. There are 247 “she” features
- ✅ [match them using knn of tokens based on actv instead of weights](https://colab.research.google.com/drive/1LIHrRNnB2rPp197QGLyji7a1IJNeI_g9#scrollTo=wL6kOGPiKuob&line=1&uniqifier=1)
    - ✅ it’s not jaccard of inds that’s slow; it’s KNN of each feature set
        - we can start with just a 10k subset of the 64k flattened token actvs
        - RESULT: 0.41 sim
    - ✅ Compare this to a shuffled subset (tokens don’t match) of actvs B
        - `jaccard_similarity(reshaped_activations_A[:10000, :], reshaped_activations_B[10000:20000, :])`
        - this is like compare jaccard of 2 LLMs on 2 diff feature actvs
        - RESULT: 0.001 sim
    - ✅ now instead of taking rand subset of features, compare actvs A to a random matrix of same size
        - RESULT: 0.0005 sim

Reflect

- ✅ double check synth actvs gen procedure
    - perhaps the decay procedure isn't the same as I do it on a batch of samples, rather than all 512, I should probably either carry decay to the next batch or increase the decay as it works on a smaller set
        - no; this is a misunderstanding, the decay is for each FEATURE. It’s the same for every sample; so it’s broadcast to all of them. You can put it out of the loop!
        - So this is not needed: decay_rate = 0.99 * batch_ind * batch_size
- ✅ respond to Dan’s email about actv sets being the same
    
    Hi Dan,
    
    Thanks for the helpful feedback! I can explain the project:
    
    **Project Overview**
    
    In short, I’m looking to measure the extent of SAE feature subspaces with similar feature relations (arrangements) learned across similar LLMs (say, trained on the same dataset with similar architectures). 
    
    Taxonimizing by different parameters (eg. SAE widths, comparing both representational and functionality similarity of feature splitting of families like in [https://arxiv.org/abs/2408.00657](https://arxiv.org/abs/2408.00657) ), I hypothesize entire spaces to have low similarity for different metrics (namely ones that work for  privileged basis), but “patches” of them may be similar (Eg. like how both months and days of the week were found to be arranged circularly across models; perhaps also the relation between months + days may be learned analogously across models). It would also be interesting to see how superposition plays a role in how “difficult” it is for SAEs to decompose features, as it affects how features are arranged in LLM latent space; we may vary sparsity in toy LLMs and observe this.
    
    **Response to advice**
    
    For point #2, I agree with you strongly about using different ground truth feature matrices to “simulate” multiple LLMs. After I sent the email I realized that if we just train SAEs on two different sets of activations, that could still just simulate training SAEs on different activation samples from the **same** LLM. So now I’m thinking that to compare if 2 SAEs learn similar feature relations across LLMs, perhaps to use two sets of ground truth features that share at least a subset of features, but not all.
    
    And I was thinking of using different frequencies of which features are active in different synthetic activations would “simulate” how certain LLMs would tend to learn some features more than others. So not just varying the mean number of active features, but have different simulated LLMs prefer to use certain features (such as the shared ones) more than others. They’d draw from distributions with different covariance matrices too.
    
    **Why synthetic activation experiments?**
    
    The synthetic activation work is a part of a larger project, though I may be postponing these synthetic activation experiments to prioritize another task regarding feature subspace matching. There are several purposes for doing them:
    
    1. To check the extent of ground truth feature (GTF) relations learned by SAEs (this is “**Approach 3” of** [https://www.lesswrong.com/posts/MFBTjb2qf3ziWmzz6/sae-feature-geometry-is-outside-the-superposition-hypothesis](https://www.lesswrong.com/posts/MFBTjb2qf3ziWmzz6/sae-feature-geometry-is-outside-the-superposition-hypothesis) )
    2. To check how different the GTF relations learned by SAEs are when trained on different LLMs
    3. To measure which metrics work well for accurately scoring the SAEs- they should have high scores when they learn actual similar GTF relations, and low scores otherwise. We use synthetic activations as in LLMs, we don’t know the GTFs. Thus, we first find metrics that work well on activations constructed by known GTF, and then apply the metrics that work well on SAEs trained on LLMs.
    
    I’m working with Fazl Barez in the Torr Vision Group. We are still finishing preliminary experiments and are looking to share these with possible collaborators once we get results rooted in stronger experimental setups. Lastly, I was reproducing the synthetic activation code (using GMM sampling for GTFs); there may be errors I’m looking for help to check, but here is the link to it so far if you want to look at it (also attached as a file): [https://colab.research.google.com/drive/1y8pdbnCACls3C1IyGceTTdOQ0bVqs57T](https://colab.research.google.com/drive/1y8pdbnCACls3C1IyGceTTdOQ0bVqs57T)
    
- 🐣 re-read to see which strucs to look for: [https://www.lesswrong.com/posts/MFBTjb2qf3ziWmzz6/sae-feature-geometry-is-outside-the-superposition-hypothesis#fnref7909cqttr07](https://www.lesswrong.com/posts/MFBTjb2qf3ziWmzz6/sae-feature-geometry-is-outside-the-superposition-hypothesis#fnref7909cqttr07)
    - ctrl + f: “Here are the clusters that I thought might have interesting structure:”
        - Most clusters however don't seem obviously interesting…. it could just be that our methods are limited, or the LLMs and/or SAEs we used weren't large enough, or that there is interesting geometry but it's not obvious to us from PCA plots like the above.
        - I know that for myself, even when considering basic 4D geometry like a tesseract, if data clusters were around corners of the shape I'd only spot a small number of the possible 2D slices, and in at least one of those cases might think what I was looking at was a circle instead of a tesseract:
    - ctrl + f: “Each neuron is responsible for one small rectangle under the curve.”
    - GPT-2-small uses a cosine/sine spiral for its learned positional embeddings
    - One plausible possibility here might be that sets of feature vectors that are semantically related to each other in interesting ways (ways that favor certain forms of computation) tend to form (approximate) sub-spaces, of various types and dimensionalities facilitating those computations — which we could then learn a taxonomy of common types of.
    - the features on one layer are thought of as relevant combinations of simpler features from the previous layer
        
        For example, you can certainly build a simplicial complex in the following way: let the features for the first layer be the 0-simplices be the first layer. For a feature F on the n-th layer, compute the n most likely features from the previous layer to fire on a sample highly related to F, and produce an (n-1)-simplex on these (by most likely, I mean either by sampling or there may be a purely mathematical way of doing this from the feature vectors). This simplicial complex is a pretty basic object recording the relationship between features (on the same layer, or between layers). I can't really say whether it would be particularly easy to actually compute with, but it might have some interesting topological features (e.g. how easy is it to disconnect the simplex by removing simplices, equivalently clamping features to zero).
        
- train sae relu on 100k steps
    - wandb: [https://wandb.ai/wlg100/sae_tiny-stories-1L-21M_MLP0_df16384_steps100k?nw=nwuserwlg1](https://wandb.ai/wlg100/sae_tiny-stories-1L-21M_MLP0_df16384_steps100k?nw=nwuserwlg1)
        - L1 loss only goes from 160 down to 30
        - L2 loss (reconstruct actvs) seems to improve
        - CE loss (downstream once replace) seems to improve
        - num dead neuron stays around 1

TDA revisited

- 🐣 [Pers Hom Code Explora](../../Pers%20Hom%20Code%20Explora%20b1cd6485f6a74fc1903d80c10f78a4bd.md)
- **Gunnar Carlsson: "Topological Modeling of Complex Data"**
    
    [Mapper](../../Mapper%20c4be8be4e15e4ff7b70908fd3512434b.md) 
    
    [https://www.notion.so/wlg1/Mapper-Code-Explora-880f6e49fb09483f94155492009bd222](../../Mapper%20Code%20Explora%20880f6e49fb09483f94155492009bd222.md)
    
- find how to specify lens fn in kepler:  fit_transform(..,`projection`
    - [https://kepler-mapper.scikit-tda.org/en/latest/examples.html](https://kepler-mapper.scikit-tda.org/en/latest/examples.html)
    - [https://kepler-mapper.scikit-tda.org/en/latest/applications.html](https://kepler-mapper.scikit-tda.org/en/latest/applications.html)
    - isomap lens projects down to 100 dim space
- [interpret the colors based on gunnar’s talk. colors are any function of interest, not just the lens](https://chatgpt.com/c/948cd911-e000-43d0-8803-cfd9c9e92498)
- 3 Mapper variations using diff lens & color fns (same clustering and cover)
    
    SAE_DW_mapper_explora_v1.ipynb
    
    - Use PCA as lens
        - n_comp should be small, not like 100. That’s why it did Isomap 100 then UMAP to 2 before.
    - Use norm as lens (same as bei)
        - [https://kepler-mapper.scikit-tda.org/en/latest/notebooks/Cancer-demo.html](https://kepler-mapper.scikit-tda.org/en/latest/notebooks/Cancer-demo.html)