# Networking

Emails and DMs

[email- why algtop needed](Networking%205eb6990dfeee475b920112de369de0ab/email-%20why%20algtop%20needed%2090a8057d0f47426f848c74b01f797949.md)

[AlgTop Msgs- 29 July week](Networking%205eb6990dfeee475b920112de369de0ab/AlgTop%20Msgs-%2029%20July%20week%20d2b50240185b49348930508f4d21ebba.md)

[NN sim Msgs- 29 July week](Networking%205eb6990dfeee475b920112de369de0ab/NN%20sim%20Msgs-%2029%20July%20week%20a18f20b6f1b040c8b4e61b294ec2e4e5.md)

[SAE Msgs- 29 July week](Networking%205eb6990dfeee475b920112de369de0ab/SAE%20Msgs-%2029%20July%20week%205a060dd8f5ef46f28004052c2ca0a701.md)

Twitter

---

### **List of people contacted**

NN Geometry

Email

- [beren@millidge.name](mailto:beren@millidge.name)
    - Questions from University of Oxford intern about synthetic activations sampling
        
        Hi, I’m currently a research intern at the University of Oxford working on a research project involving synthetic activations based on this approach that you worked on: [https://www.alignmentforum.org/posts/z6QQJbtpkEAX3Aojj/interim-research-report-taking-features-out-of-superposition](https://www.alignmentforum.org/posts/z6QQJbtpkEAX3Aojj/interim-research-report-taking-features-out-of-superposition)
        
        I’m looking to modify the setup to train SAEs on multiple sets of activations, each simulating a different LLM, that are combinations of ground truth features sampled from a space where the features form interesting arrangements with one another, such clusters or circles. I was wondering how sound these modifications are:
        
        1. Would it be sound to sample ground truth features from a Gaussian Mixture Model (using make_blobs in scikitlearn) instead? Not sure if the uniform distribution is necessary to say, allow the cosine sim to be low and not always/mostly be high (due to skewness).
        2. To simulate multiple LLMs (where we know the ground truth features), I’m looking to use different sets of activations that are sparse linear combinations of the same matrix of ground truth features. Would I have to use different ways to get frequencies of feature activations to simulate different LLMs, to make sure they differ enough? Not sure what I’d need to do to achieve this yet, so I am open to advice.
        3. Would it be sound to use hard coded ground truth features, say using the encoder weights of an SAE trained on an actual llm? I think that has issues, eg) the features found may have biases from the specific llm training mixed in and wouldn't be good to generate other simulated llms from it.
        
        I can explain more about what the project actually is if you are interested, but I was looking to first keep my questions as short as possible. Thanks!
        
- [danbraun15@gmail.com](mailto:danbraun15@gmail.com)
    
    Questions from University of Oxford intern about synthetic activations sampling
    

Discord

- park
    - msg to kiho on feature familities co-oc matrix
        
        Yes (section 4.2). Do you think their the co-occurence matrix on features to find  feature families (having an edge between high to low density features, or general to specific concepts) is related to your approach with the cosine sim matrix between child-parent vectors? 
        
- hamish

AlignmentForum

- [Robert_AIZI](https://www.lesswrong.com/users/robert_aizi)
    - ground truth features from non-unif
        
        Hi, I’m working on a research project involving synthetic activations based on this approach that you wrote a well-written explainer on: [https://www.alignmentforum.org/posts/z6QQJbtpkEAX3Aojj/interim-research-report-taking-features-out-of-superposition](https://www.alignmentforum.org/posts/z6QQJbtpkEAX3Aojj/interim-research-report-taking-features-out-of-superposition)
        
        I’m looking to modify the setup to train SAEs on multiple activations that are combinations of ground truth features sampled from a space where the features form interesting arrangements with one another, such clusters or circles. I was wondering how sound these modifications are:
        
        1. Would it be sound to sample ground truth features from a Gaussian Mixture Model (using make_blobs in scikitlearn) instead? Not sure if the uniform distribution is necessary to say, allow the cosine sim to be low and not always/mostly be high (due to skewness).
        2. Would it be sound to use hard coded ground truth features, say using the encoder weights of an SAE trained on an actual llm? I think that has issues, eg) the features found may have biases from the specific llm training mixed in and wouldn't be good to generate other simulated llms from it.
        
        Thanks!
        
    - his reply
        
        That sounds like a cool project! I'm not aware of much continued research on purely synthetic features after everyone started playing with LLMs, so I'd be excited to see your work on this. The easy answer is to say "you should try all those things and see which ones work", and thinking it through.
        
        Just to make sure I follow what you're describing, this is what I understand you to be proposing:
        
        1. Make a "ground truth dictionary" which is a matrix M of size (d_embed, n_features), whose rows are the ground truth features you hope the SAE to find. For Sharkey et al, these rows were randomly sampled points from an n-ball, but you're proposing using (1) points from a Gaussian Mixture Model or (2) an encoder matrix from a separate SAE.
        2. To generate a single datapoint to train the SAE, you make a sparse vector x of size (n_features, 1), and then compute M*x, which results in a vector of size (d_embed, 1).
        3. Then train an SAE on the set of datapoints generated by this process, and measure if it rediscovers (parts of) the original matrix M.
        
        To your questions:
        
        1. I think using not-uniformly-sampled synthetic data from a GMM is a good thing to try. As you suggested, you'll want to ensure that your metric (cosine similarity or similar) is sensitive enough to pick out features in the blobs. A few options spring to mind to help with that:
            1. Center the set of features, so that the average feature is at the origin. This should be enough to ensure that a point in blob A has low cosine similarity with a point in blob B.
            2. Use the other points as a "baseline". If your SAE learns feature f which is cosine-similar to ground truth feature x, then also check for the ground truth feature y which is the most cosine-similar to x (besides x itself). If CS(f,x)<CS(y,x) then I'd say the SAE isn't "really" finding a feature for x.
            3. Check if the same SAE feature is used as indicator for multiple ground truth features. For instance, if x and y are ground truth feature, then the SAE might learn f=average(x,y) as a feature, and this would have high CS with both x and y (and would pass the test I described in the previous part). But f would be the indicator for *both* x and y, and that would be suspicious.
        2. Using encoder weights from an existing LLM is interesting. It is possible they are "essentially random" and an SAE would learn them as well as truly-randomly-generated points. Some tests you could run to identify this:
            1. Is the average SAE feature near 0? [On random data: Yes]
            2. Do the SAE features have high cosine similarity with any other SAE feature? [On random data: No]
            3. Do the SAE features have roughly equal norm? [On random data produced by Sharkey et al: yes, norms which are exactly equal.]
        
        Let me know if that answered your questions! If you'd like, I can also send you some code I have for training an SAE to help you get spun up faster.
        
    - his reply 2
        
        If you're using the exact same data generator just with a different random seed, I think you're likely to end up with similar SAEs at the end of the process. I think your best bet to similate multiple LLMs is to change the feature covariance matrix.
        
        For the Gaussian Mixture Model, I'd be especially interested in changing the covariance matrix to change the relative co-occurrence of features from the same blob. For instance, what happens if blob A always has exactly 1 feature active? Exactly 2 features active? A random number between 1 and 3 features? I could imagine the SAE behaving very differently in terms of learning a single feature for "that blob" vs a bunch of features for the individual points in that blob.
        

<<<

**SAE training**

Slack

- jbloom
    - umap on actvs question
    - umap issue
    - [auxk issue](Project%20Planning%20b4b05f73d85e409f8409b209e44ed692.md)
    - feature univ project ques on opinions
        
        I was also looking for feedback on this direction: One of the sub-topics I’m looking into is feature universality relations, particularly in SAE space. I’ve been running prelim expms to compare SAEs across similar LLMs (same tokenizer and training dataset), such as comparing cluster relations in UMAPs and in other graphs like Mapper. Given “clustering illusions”, I’m looking into more rigorous methods using representation space + functional similarity metrics. 
        
        One hypothesis is that we don't expect feature spaces to look exactly the same, but hypothesize some patches of their subspaces to be similar. This is based on the idea that certain relations may be hidden in a low-dimensional manifold within "reality" already that different datasets are capturing (huh2024platonic), and that models are modeling this low-dimensional manifold. Also, some SAE decoder weights may model ground truth features (sharkey2022interim). 
        
        For instance, several LLMs may find similar, optimal ways to partition the concepts of "happy" and "not happy" in feature space. If we extend this case to many concepts, it is possible that there are some arrangements of multiple concepts that are analogous across feature spaces (eg. “months” circles). We do not always expect the concept of "dog" to always be "above" "animal"; however, it may be possible there are some connectivity relations of this feature subspace that can be topologically mapped.
        
        I was wondering if you have any thoughts of this topic as you’ve worked with SAE features, and if you have any ideas of how it can be feasibly approached?
        
    - feature families hierachies viz
        
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
        
- luke marks

Alignment Forum

- https://www.alignmentforum.org/users/connor-kissane?from=post_header
    - ask about sae training tinystories
        
        Hi, I started working on a paper that involves SAE training on tinystories models to compare feature splitting by feature geometries. I saw you have been doing SAE training, and as I’m still learning the practices for it, I was wondering if I can talk or meet with you about ways to tune SAE training to select more monosemantic and truer features in the dataset, such as a feature that is monosemantic for “king”? I can share the runs I have tried. I am also interested in finding collaborators if you are also interested. 
        
- https://www.alignmentforum.org/users/robertzk?from=post_header

<<<

**Sim metrics**

- [max.klabunde@uni-passau.de](mailto:max.klabunde@uni-passau.de)
    - email to max 8/5
        
        Thanks! The second point makes sense when comparing different models. Right now I'm using 2 sets of synthetic activations that use the same ground truth features, but with different linear combinations of them (and perhaps at different frequencies, to model properties specific to each LLM). This week I'll also try using MMCS before and after using Orthogonal Procrustes to find an alignment first. I just started reading your new paper so I'll get back to you once I finish it. Will the repo in the paper's link be public soon?
        
        Also, since I’m looking to use metrics that compare how well the SAEs for different LLMs capture the feature space (comparing how well they detect distinct clusters + shapes), I was looking to use features that form interesting arrangements with one another. I was wondering if you can check if you think this is a correct interpretation (overall, I have 2 questions):
        
        In the [“Taking features out of…” post](https://www.alignmentforum.org/posts/z6QQJbtpkEAX3Aojj/interim-research-report-taking-features-out-of-superposition), ground truth features are sampled from a uniform distribution, and they’re only made correlated when put into linear combinations, as the coefficients of the activation vectors are selected based on the feature frequencies. So the ground truth features would still form a uniform distribution, and the SAE encoder or decoder weights would also form a uniform distribution, meaning their UMAP plots wouldn’t show semantic clusters like those seen in “Scaling Monosemanticity”.**Q1:** Thus, would it make sense to modify the synthetic activations generation so that ground truth features are not from a uniform distribution but from a feature space with clusters and other shapes? I've tried sampling from a gaussian mixture model; so far this has trained bad SAEs with very high loss (think I just need more samples or tuning, I'll see).
        
        **Q2:** I was also wondering if it would make sense to somehow get already hard coded features from some decomposition? Say if we just use encoder weights, from a sparse feature space of another SAE trained on an actual llm, as ground truth features. But I think that has issues, such as the features found may have biases from the specific llm training mixed in and wouldn't be good to generate other simulated llms from it. Possibly also breaks other assumptions.
        
- austin

<<<

**AlgTop**

- beiwang@[sci.utah.edu](http://sci.utah.edu/)
    - archit@arathore.com
- [vidit](https://people.maths.ox.ac.uk/nanda/)
    - email 1
        
        I am a research intern working in the Torr Vision Group at the University of Oxford from July to Sept, and as part of a paper I am writing, I have been applying TDA to a new field of transformer interpretability research. Specifically, I am conducting research in a field that has been using a technique to extract highly interpretable features from language model neuron activations, and I have been applying Mapper to this new feature space, motivated by the feature manifold hypothesis which claims there are may be “higher-order feature subspaces” universal across models.
        
        Along with preliminary experiments, I have a write-up of the overall project and main research questions. However, I have only started to use TDA, and would like to consult with experts in the field to: 1) Manifest new ideas by exchanging ideas between TDA and AI interpretability, and to 2) Ensure TDA methods like persistent homology are correctly applied. There may be TDA techniques other than Mapper that can be applied, and I am eager to learn about them.
        
        I was wondering if you would be interested to meet and talk about a possible collaboration in the field? I can discuss the main research questions and experiments. Alternatively, if you know anyone else in the field (such as Masters/PhD students) who may be interested in talking, I would be happy to meet with them too. If you or your students are not looking to collaborate, I am also looking to just consult with experts in the field, and can include them in the paper’s Acknowledgements. I am free any time next week (Aug 5th) or later, except at 12-1pm Mondays (BST) and at 2-3pm Fridays (BST). I am located at the Information Engineering Building. Thank you!
        

---

### Not contacted yet

NOTE: not all coauthors are in the subject, so look up which ones did it

NN geom

- “not all features are linear”
- ask bloom for tips on better interactive umap viz

Sim metrics

- cca people (hinton group)

Algtop

- List of algtop + nn people to contact
    - zhou325@sci.utah.edu
    - [**Emilie Purvine**](https://scholar.google.com/citations?user=_i4Kv1wAAAAJ&hl=en)
    - Alexandria Volkening
    - [https://www.danieltolosa.com/](https://www.danieltolosa.com/)
- contact these authors
    
    [https://dl.acm.org/doi/10.1145/3604433](https://dl.acm.org/doi/10.1145/3604433)
    
    [https://dblp.org/pid/250/3875.html](https://dblp.org/pid/250/3875.html)
    
- List of algtop people to contact
    - vidit
    - [spalande@danforthcenter.org](mailto:spalande@danforthcenter.org)

[https://x.com/patrickshafto](https://x.com/patrickshafto)

- interesting papers
    - [https://arxiv.org/pdf/2407.04854](https://arxiv.org/pdf/2407.04854)
        
        Statistical investigations into the geometry and homology of
        random programs
        
    - Integral Betti signature confirms the hyperbolic geometry of brain, climate,
    and financial networks
    - Wasserstein convergence of Cech persistence diagrams for ˇ
    samplings of submanifolds

<<<

---

- old proj
    - Feb 24th MI #general post
        
        Just got back to looking at the sleeper agents paper from the reading group a few weeks ago, I was wondering if anyone has tried replicating it yet for non-Anthropic models as per this post: [https://www.alignmentforum.org/posts/M8kpzm42uHytnyYyP/how-to-train-your-own-sleeper-agents](https://www.alignmentforum.org/posts/M8kpzm42uHytnyYyP/how-to-train-your-own-sleeper-agents)
        I assume the backdoored Anthropic models are not available to the public
        
    - Alice Rigg DM
        
        Hi, I was interested in your talk about the future direction of MI, and was wondering about how the research in interpreting the effects of fine tuning are going. I saw in the server that there are papers in that area (Fine-Tuning Enhances Existing Mechanisms, [https://openreview.net/forum?id=8sKcAWOf2D](https://openreview.net/forum?id=8sKcAWOf2D) and Editing Models with Task Arithmetic), and I was wondering what you think about pursuing a direction that studies and compares the internals of different fine tuning approaches? Do you know of any other research in this area, and is it feasible/fruitful at this time? Thanks!
        
        I think in the paper, "ok-enough" sleeper agenty properties emerge at the ~10b parameter scale that are robust to RL or SFT approaches, and don't just immediately collapse
        i think this could definitely be an eleuther-backed project, if you got enough momentum going for it
        
        ah, i see. in general, i was looking to study models related to deceptive behavior, trying to find some i can study without a lot of compute
        makes sense, was looking to start small scale first for prelim expms