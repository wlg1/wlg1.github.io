# Brainstorm Corr by Words

- previous dims: (batch, seqlen, model_dim)
    - now, seqlen should be replaced by wordlen, which is total number of words in prompt
    - first, get activations matrix for (batch, seqlen, model_dim)
    - get tokenization of entire prompt
    - get words of each prompt (separated by whitespace)
    - for each word group, group the tokens of the model into word
        - do this by de-tokenizing each token?
            - POSS ISSUE: tokenizing each individual word is different than tokenizing the prompt of words.  so trying to identify which token is in each input is not accurate?
            - non-trivial because a word may be “tree” but the token may be “ree of”?
    - then combine the activations for each token in each group into a new “word” activation
        - output dims are: (batch, wordlen, model_dim)

---

- How to combine tokens: try + and * and mean
    - * has issue bc too low will make product too low
    - mean or sum makes more sense
    - ask chatgpt, claude

---

- alternatives to activation correlation to pair SAE latents
    - only look at single tokens they have in common
    - semantic similarity (top k)
    - common embedding space similarity