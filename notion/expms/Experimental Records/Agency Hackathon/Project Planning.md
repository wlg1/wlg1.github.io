# Project Planning

### Working on

- ✅ brainstorm agency concepts
    
    Directions to look for:
    
    - agents
    - emotions/states of being: content, hungry, tired, happy, angry, sad, enjoying, hating, trust
    - facts vs opinions, arguments, opposing views, cultural differences
    
    Prefrontal cortex in devision making and planning. Is the same part that predicts in nns used
    
    Not just the next word, but simple planning q n a.
    
    They think it, fact vs opinion
    
    John did not make it on time. What emotion is John feeling?
    
    John is smiling. What emotion is John feeling?
    
    Corruption- John is frowning.
    
    See if lateness and sadness have some correlation a
    
    John has a knife. What is John? An enemy. John has a cake.
    Corrupt enemy to friend
    Is knife correlated with enemy? Cosine sim and also sim after an output
    
    - Prompt gpt4 for a list of subject types vs object types
        - [https://chat.openai.com/c/6eb6b0ab-76b4-461b-a466-19b2fab1fca8](https://chat.openai.com/c/6eb6b0ab-76b4-461b-a466-19b2fab1fca8)
        
- ✅ Autolabel heads and MLPs to search for “agency concepts”
    - ✅ may just do MLPs b/c too many heads, too costly
    - ✅ run autolabel using saved repo data, not new data
    - double check results by manual check ‘yes’ and check if a few samples are right
    - first check agents, then check emotions, then check cultures/beliefs
        - may just run this on SVD trace if too costly
- SVD trace to find “agency concepts”. loop over all heads (second search method)
- Edit to remove agency

### Done

- [https://www.alignmentforum.org/s/yivyHaCAmMJ3CqSyj/p/eqvvDM25MXLGqumnf](https://www.alignmentforum.org/s/yivyHaCAmMJ3CqSyj/p/eqvvDM25MXLGqumnf)
- [Brainstorm](Brainstorm%20ebb2cabfaf5f48c59323a38a8f2802cf.md)
- ⚠️ [Object vs agent tokens](Object%20vs%20agent%20tokens%2028486adc69aa4c31b6f1dce1d931d860.md)
- [Clustering by layer](Clustering%20by%20layer%2077c19fec1e6b4450b701492d98d935e2.md)
- [SVD- subjs and objs](SVD-%20subjs%20and%20objs%20279d402ddd9d4a0a84f64fe1cca2f116.md) start
- ✅ Call GPT-4 to interpret one direction of a head matrix
- ✅ Call GPT-4 to interpret 3 head matrix directions
- ✅ Call GPT-4 to recognize subjects
- ✅ Save GPT-labeled singular vector data in new folder

### Future Work

- Theory of Mind Prompts; give theory of mind writings to gpt4 and have it brainstorm test prompts for gpt2 to gpt4
- Ask GPT4 to label each “agency” direction with a word
- Plot, colored by head or MLP, directions with GPT4 labels in PCA, and cluster
- improve sim fn for svd trace (better than cosine sim)
- Ask GPT4 on how to do a statistical test to verify it’s working well (by manually checking samples) when there’s 1000 directions to check. How many samples to check to get a good analysis?
- check name mover in small is same name mover when found by svd trace

---

POSTPONED

- What heads rec first letter cases or the?
    - may just end up putting these test prompts in appendix
- Replace lion actv with cat, see how it changes prediction
- How did Seattle corruption work? they used noise instead of replacing

---

- [https://coda.io/@firstuserhere/open-problems-in-mechanistic-interpretability/rl-interpretability-15](https://coda.io/@firstuserhere/open-problems-in-mechanistic-interpretability/rl-interpretability-15)
- [https://arena-ch2-rl.streamlit.app/](https://arena-ch2-rl.streamlit.app/)
- [https://colab.research.google.com/github/neelnanda-io/TransformerLens/blob/main/demos/Othello_GPT.ipynb#scrollTo=MnLUGTrwFUGP](https://colab.research.google.com/github/neelnanda-io/TransformerLens/blob/main/demos/Othello_GPT.ipynb#scrollTo=MnLUGTrwFUGP)
- [List of Circuits](https://www.notion.so/List-of-Circuits-5d420f64bdbf45bb9312c576225c701b?pvs=21)