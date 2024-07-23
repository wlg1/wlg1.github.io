# kiho meeting 2

summary:

It seems the paper we discussed has additional difficulties when applying to intermediate (not the last layer) space, as it relies on the orthogonality relations to find the simplices, but these relations seemed to only hold in causal inner product space, which the main author said could not (right now) apply for intermediate spaces after I spoke to him more. He guessed it may still be possible to find simplices using some other method, such as topological data analysis, but we'll have to see. Let me know if you have any ideas about this, for now I may try to apply TDA to see what happens.

---

- kiho meeting to continue emailed questions
    
    Brief overview of main project, and state haven’t started looking into hier bc wanted to make sure expm set up was right first
    
    - Should we use causalp space?
    - how to get samples with next token?
        - Can’t we just compare LDA vectors?

Brief overview of main project, and state haven’t started looking into hier bc wanted to make sure expm set up was right first

- Should we use causalp space?
- how to get samples with next token?
    - Can’t we just compare LDA vectors?
    

last token, last layer:

months, 0 to 9 (mod 10)

training data and poss diff structure - same

if structures are diff (hinton 

downstream output

geometry of hidden states of two different structures- difficult to interpret 

num layers may be okay to vary

llama VS gemma have very diff structures; weights not tied, gemma inits first tokens differently

logit lens for llama is very useful, but for gemma doesnt work. spaces they use are very different. not sure how to compare them. and if dim are different

tinystories 1L 21M from scratch?

---

causal inner product space

when multiply matrix on embedding and unembeddings, softmax prob is preserved. euclidean inner product in emb space is not identifiable, if we get causal inner product, the estimate is whitening the unembedding space, and est causal inner product multp inv transpose to embeddings, so cov gamma multp by lamdba, means embeddings (transposed) also has information of unembeddings. this is combined inner product with semantic meanings.

sae used euclidean inner product for loss?

maybe sae feature space

gemma model: unembd in cone, after whitening with causal inner product, there’s orthogonality. original space doesn’t have this orthogonality

interm spaces

not just next word prediction

downstream logits

---

2) each word in unembedding space, not embedding space actvs

nonlinear paper- 

continuous

LDA in unembedding space (logits in vocab space)

LM hat: each token has a corresponding vector

didn’t use transformer structure

if you pass dog through the model, that’s predicting the next word. 

you have a sample, you’re trying to see what features activate on dog, and possibly use info to predict next word. 

sentences where next word should be ‘dog’. Eg) in lin repr hypothesis paper, used example where next word should be “king”

LDA vectors of mammal might be different than SAE features that highly activate on dataset examples

just want one featuer direction that explains the high lvl concept

SAE features 

project token unembeddings on pca

causal inner product can see it, but not in original space

 A starting point would be to just look at the embedded activation vectors of individual tokens, and to use LDA to calculate vectors for the attribution sets they belong to. Then we can calculate the orthogonality relations of these attribute vectors.

brutce force way to try to find this structure:

a token dog. pass through to sae feature space to get a vector of feature activations for lalyer L. And you get feature vectors for multiple tokens say wolf or cat. then calculate animal vector using LDA for that in feature space?

ISSUE: when dog is put into the model, and you logit lens, it’s not dog anymore. 

SAE features are defined by dataset examples. you would call n SAE feature a “dog’ if it actives on “dog” tokens. what if these SAE “dog” features- does it make any sense to have a simplex relation with these features? The features are rows of the weight matrix

---

1) ICML- see if anyone mentions this for intermediate space, and you can also connect me with them

2) not sure if there will be orthogonality between simplices. if dont have causal inner product, may find simplicces in activation space. but will look to set up experiments and colab to send to you for critique (say using TDA to find simplices, and approaches of “Not All Language Model Features Are Linear”). If you have any ideas on how to approach this for intermediate layers, let me know

3) 

just check orth as expm

---

is dsitances of feature splitting comparable across models