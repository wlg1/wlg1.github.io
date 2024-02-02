# 1.2 code

rep_cache is global namespace so seq_len var, used in rep_cache, can be used in a fn

logit DA:

how much L0 (attn layer 0) contrib to logits. find by unembed using the specific token index of unbmed matrix. unembed using matrix multp

embed, L0, L1

concat along last dim. so 25 components in total (see return type dim)

the higher loss the worse, so a higher loss ablation (vs loss no ablation) means that head is more impt because ablating increases the loss

---

![Untitled](1%202%20code%2005323c354fcf4d78bf8d26960166abb0/Untitled.png)

A is one-hot, so $W_E$ has d_vocab rows, so it acts as a look up table. That’s why AW is the Ath row.

W_U would have B as a col because it outputs into d_vocab space, so the entire MM expression has (A,B)

<<<

![Untitled](1%202%20code%2005323c354fcf4d78bf8d26960166abb0/Untitled%201.png)

x is d_model vector of residual stream. Eg) if in first layer x is embedding vector. x is one of batch and one of seqlen. transformer operates over each batch

residual stream dim is always batch x seqlen x dmodel.

Obtain Q matrix using residual stream output * W_Q (weights to get Q), so x is like a row of this residual stream matrix? think of residual stream as a sequence of vectors (each pos is done in parallel this way). this is the query vector.

x_j * W_K gets the key vectors

Attention score is dot product of key and query vectors

<<<

![Untitled](1%202%20code%2005323c354fcf4d78bf8d26960166abb0/Untitled%202.png)

$W^T$ is to make dims match when comparing A and B. This describes how info from B is moved to A. This “info” is **how much attention** A pays to B. All pairs are done in parallel by matrix multp.

Special kind of dot product: inner product is any function with two vectors that returns a scalar that satisfies dot product props (comm, etc.). Thm: any dot product in Eucl space can be written as $x^T A Y$. This looks a special dot product (A is semi positive definite). This transforms to a new space “key query space” and take dot product there. 

<<<

Linear Algebra thms review: SVD, matrix norms, vector norms, eigenv. Project onto orthogonal subspace spanned by eigenvectors with eigenvalues. Prove this as thm. Out of all poss projections, this is PCA if linear. If nonlinear (autoencoder), the best poss projection to subspace can be better but there’s no closed form soln.

<<<

![Untitled](1%202%20code%2005323c354fcf4d78bf8d26960166abb0/Untitled%203.png)

See how impt position is compared to token value

Pos vectors close in matrix are more similar in key query space (using this dot product expression)

This should be rougly close to the identity matrix. So positions mostly pay attention to itself.

<<<

![Untitled](1%202%20code%2005323c354fcf4d78bf8d26960166abb0/Untitled%204.png)

Trace path between two attention matrices (h1 is earlier than h2)

Not much mcuh a

How much does output of h1 pays attention to B; not A to B.

A to Z. How much Z pays to B.

This describes the prev token + induction circuit circuit since it’s h1 (prev) to h2 (ind)

<<<

![Untitled](1%202%20code%2005323c354fcf4d78bf8d26960166abb0/Untitled%205.png)

This just means take SVD of the middle part just like taking SVD of A

The aim is to get from SVD of A and SVD of B into SVD of M.

The U of M uses UA*U’. The multiplication of orthonormal matrices is still orthonormal. Same with diagonal. So U_A * U’ is also orthonormal, so it’s valid as singualr vectors for M

<<<

![Untitled](1%202%20code%2005323c354fcf4d78bf8d26960166abb0/Untitled%206.png)

Usually these W_v is all other heads, this is just showing some heads

---

channel for teams for paper replication

first week material for RL (PPO): how to structure modular training loop (Resnet)

build function to train diff parts of RL agents

can’t always calculaet matrices and look at diagonal etc.; OV QK is ‘gold standard’

1.2 is less impt for 1.5; more impt for 1.3 (since 1.5 uses nnsight)

1.5 for paper replication

function vectors (must use pairs to get FV; focuses on ICL tasks as model will learn ‘antonym pattern’) more intuitive than steering vectors (which aims to trigger behavior changes)

FV more quantitative because find how many times it gets correct completion. Steering is more behaviorial changes.

SWE team practices:

- shared repo
- divide diff tasks indp beforehand