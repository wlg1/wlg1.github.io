# Dot Product Similarity for Size Comparison Inputs

- REFS:
    
    [1]: [https://www.notion.so/Congruence-1585ccca1ae94a0ca7dc6ad88ff9e808](https://www.notion.so/Congruence-1585ccca1ae94a0ca7dc6ad88ff9e808?pvs=21)
    
- Type Labels
    
    Type T1: The following experiments all use:
    
    - gpt-2-large
    

---

EXPM: Take dot product of inputs after first embedding

DESC: due to the difficulty of representing multi-token words as vectors, we only use single token words

RESULTS: 

- semantically similar inputs seem to have high similarity
- tokens with spaces in front seem to have lower similarity with each other than tokens without spaces in front

TYPES: [T1]

REFS: [1]

[https://colab.research.google.com/drive/1rch6VaG9O1YFJT1wPjjbXyDgXizGT7WV#scrollTo=dDRC2P8Vpk-T&line=1&uniqifier=1](https://colab.research.google.com/drive/1rch6VaG9O1YFJT1wPjjbXyDgXizGT7WV#scrollTo=dDRC2P8Vpk-T&line=1&uniqifier=1)

<<<

EXPM: try to compare multi-token words by dot product by taking mean

RESULT: does not work

REFS: [1]

<<<

EXPM: take dot product of congruence between two tokens (after the first embedding)

DESC: congruence of a token is its dot product with all neurons. We are taking the dot product of two congreuences. for multiple randomly genereated words, we plot a distribution. We call this value C_pair

RESULT: on average, the distribution shows random tokens have an average C_pair of around 800, while semantically similar tokens have higher C_pair similarity

REFS: [1]

<<<
EXPM: Compute dot products for "tall" and "large", and compare the similarities (eg. which are in the top) AND identify their common top neurons

RESULT: The top neurons are in layer 35 (last one for -large)

ANALYSIS: What is important about layer 35? Perhaps it’s trivial and not meaningful (eg. last layer is always like this)- if so, exclude it to see next top neurons.