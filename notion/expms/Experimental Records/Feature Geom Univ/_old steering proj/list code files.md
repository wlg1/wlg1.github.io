# .list code files

Exploratory Tests

- [hierConc_logitLens_llama2.ipynb](https://colab.research.google.com/drive/1Q0wCdowrG-JDLuSx0u-Man4kzncfJLsK)
    
    Prelim tests to look for patterns in hierarchical concepts (this just uses logit lens to unembed activation differences, which is a "brute" approach that one wouldn't expect to get anywhere. The aim is to run more sophisticated approaches that are built on these basics)
    
- [SVD explora tests](../SVD%20explora%20tests%20e685dd8723454c0fbaed4e0d19478fd9.md)
    
    [CAA_actvs_unembSVD_explrTests_v1.ipynb](https://colab.research.google.com/drive/1a0n70XzpTdPr5UMEILzIBrrRhyAFvWJC)
    
    Cleaned up version: [edit_vector_SVD_interp.ipynb](https://colab.research.google.com/drive/17Ja4g84RMSQVxj4DfSdZ7-dJU_esVWBr)
    
    Decomposing model editing/steering vectors with SVD (simplistic way to get features, and only a stepping stone for better approaches we plan to implement later)
    
    The above's last section decomposes the steering vector for sycophancy, but that seems to just predict A or B tokens (for multiple choice prompts) so it's decomposing the A vs B features rather than sycophancy concepts. So we can explore other types of vectors that represent sycophancy better.
    
- [[CAA_SAE_explrTests_v1.ipynb](https://colab.research.google.com/drive/1rv8d3VJBSLxtSbFGq1809VZB1BGPGiZe)](../CAA_SAE_explrTests_v1%20ipynb%20ac477af8bdf54dc5bdf057884cfe0c2b.md)
    
     [CAA_SAE_explrTests_v1.ipynb](https://colab.research.google.com/drive/1rv8d3VJBSLxtSbFGq1809VZB1BGPGiZe)
    
    sparse autoencoder decomp editing
    
    removes exercises: [filt CAA_SAE_explrTests_v1.ipynb](https://colab.research.google.com/drive/1s3h99LmSebc6yiCEfsnRwFHhMts8Do9b)
    
    v1: uses ARENA code
    
    steer_vector_SAE_interp.ipynb
    
    v2: uses [code from here](https://colab.research.google.com/drive/1st56jqGL_QU5i-ACLhFWpI_9dD_HLQdn#scrollTo=UB0OrAXz3sid)