# EMNLP prepa

### Main

Fundamental LLM concepts

- backprop
- [LoRA](https://www.notion.so/LoRA-beac52c3b5cc4053a29c71e4419e9490?pvs=21)
- BERT
    
    https://www.datacamp.com/blog/what-is-bert-an-intro-to-bert-models
    
    - roberta: duplicating training data and masking it 10 times, each time with a different mask strategy

Fundamental interp concepts

- ✅ saliency maps
    
    compute partial deriv gradient of output to input pixel 
    
    computes using fwd pass
    
- GRADcam
    
    compute partial deriv gradient of output to latent
    
- LIME
    - compu expensive
- SHAP
- interpretable vs black box models
    - interpretable : decision trees, logistic regression

Mech interp concepts

[Patch](EMNLP%20prepa%20139afed922dc80d48c1be70146462e0e/Patch%2013dafed922dc8063af51d46d7209ec05.md)

### Optional

Fundamental stats concepts

- maximum-likelihood problem
    - https://python.quantecon.org/mle.html
    - https://www.aptech.com/blog/beginners-guide-to-maximum-likelihood-estimation-in-gauss/
- precision and recall
    - precision: how many selected are positive over WHAT MODEL PREdicts
    - recall: how many selected are positive over TOTAL ACtual POSITIVE
    
    ![image.png](EMNLP%20prepa%20139afed922dc80d48c1be70146462e0e/image.png)
    
- F1 score
    
    The two metrics (p, r) contribute equally to the score, ensuring that the F1 metric correctly indicates the reliability of a model.
    
- roc score
- hierarchical clustering

---

Look for concepts to briefly study (read summaries) in a sample set of papers from various tracks of EMNLP 

Select 1 paper from impt/closely relevant tracks, and 5 papers from interp:

Interp

- ✅ [Interpreting Arithmetic Mechanism in Large Language Models through Comparative Neuron Analysis](https://arxiv.org/pdf/2409.14144)
    - Claim: 2D perf decreases upon head patching bc uses 1D memorization. however, this is not tested. It may be tested by trying to observe if 2D results do follow pattern of destroying some specific 1D memorized observation?
        - 1D memorization: only need memorize two 1D operations for each col
    - is a.h memorizes specific operation, was this found by finding that changing these heads didn’t change outputs for some general pattern (eg. all operations involving carry 1), but only specific memorized operations?
    - Sec5: lora is used here to represent weight matrices as 2 smaller matrices, so that interp is done on the 2 smaller matrices?
        - [how is lora used in this paper? why is it used to mech interp?](https://chatgpt.com/c/67314d67-2b68-800c-b412-bac2e1c23832)
            - LoRA adjusts the attention layer outputs, which propagate through the residual stream and modify the inputs to the FFN layers.
- ✅ On the Similarity of Circuits across Languages: a Case Study on the Subject-verb Agreement Task
- [Understanding Higher-Order Correlations Among Semantic Components in Embeddings](https://arxiv.org/pdf/2409.19919)
    - pca
    - ica

BlackboxNLP

- 

---

Employers

- [https://www.bloomberg.com/company/values/tech-at-bloomberg/artificial-intelligence-ai/](https://www.bloomberg.com/company/values/tech-at-bloomberg/artificial-intelligence-ai/)

workshop:

[https://underline.io/events/470/reception](https://underline.io/events/470/reception)

tutorials:

[https://underline.io/events/471/reception](https://underline.io/events/471/reception)