# Brainstorm- anything

Path patch feature to feature causation

Relations between features: path patching by partially ablating neuron activations. This subtracts out the activations used by the neuron, and is like zero ablation. See if this works.

path patch between sae, svd, pca features

modify them for your purpose

path patching only between impt components: very strict threshold + makes ranking go down

animal features, lion features - find differences b/w feature vectors

male vector, angry vector, build up to
automated subtraction and measuring similarity to find what's orth

circuit for differentiating lion vs tiger vs bear vs animal

[https://transformer-circuits.pub/2023/monosemantic-features#phenomenology-fsa](https://transformer-circuits.pub/2023/monosemantic-features#phenomenology-fsa)

features changing prob of tokens which change prob of other features firing

eg) A.0.207 → CAPS tokens → A.0.358 → “_” tokens → A.0.207

Interpolation by common concepts- meaningful (to a goal) vs superficial

interpolation between abstract features from weight memory and various inputs. interpolation in input space + the inner weight spaces + their combined activations.

jumping tangents in dreams from non-main trait that becomes main trait (eg. lamps on vacation, get distracted and focus on lamps and now moths in dream and forget about vacation)

translate activations into different fields. abstract actv added from fable to work may force tortoise to become a person.

fables- tinystories

composite of memories? memories become weights.

interpolate smoothly between unrealted things to find their underlying abstract commonalities and also unrelated tangents they share. tangent is also in tangential ironically a vector

vectors are feelings; find the right angles to calculate that will yield the common activation abstraction between unrelated inputs.

eg. traveling vacation and the deadline, when merged, match with their tangential commonality, and can interpolate between them

transfer feeling of concept to behavior

Recursive: relations become objects for the next level

relative features are also features (recursive)

recursive formula for shape/position/discrete counting/quantity. now, can this be used for continuous vectors?

objects become relations in recursive levels; what field in math models this?

- 
    
    

prove there is invariance between abstractions (represented as feature vectors or circuits)

see geometry of truth paper for circuits in latent space

[https://www.lesswrong.com/posts/Go5ELsHAyw7QrArQ6/searching-for-a-model-s-concepts-by-their-shape-a](https://www.lesswrong.com/posts/Go5ELsHAyw7QrArQ6/searching-for-a-model-s-concepts-by-their-shape-a)

Automate feature relation finding

automated subtraction and measuring similarity to find what's orth

pos, dist, shape- multiple perspectives to find patterns

automate finding patterns using algo triggers that notice ANY anomalies. have many diff measurements to look for. (opt- include ai to look for these). transformations. have ai suggest at diff steps. the ai feels and connects patterns to analogous intuitive things.

use CT to find the triggers to look for- finding the match. what formula to calulcate from CT (eg. mapping score for equivariance) that implies a lock is done?

Learn to lock inputs onto weights
gradually use gradients to learn and have the analogy settle and lock into place of mathcing weights to specific inputs of work place people.

calculate the rate of change of the model output with respect to each of the singular directions

in the limit, what do they converge to? do they lock into a match under certain conditions?

loss function: match similarity

Feature definition using analogy

A feature is not defined by specific objects (vectors), but the relation between vectors (a circuit). The hypothesis is that a circuit is finding analogies. A man failing and glass breaking are semantic graphs containing specific 

Interpret Abstract Reasoning

LLaMA can complete abstract reasoning. Find the components used in an abstract group.

---

Matrix Decomp Notes

Matrix: rows (output) are feature vectors, cols (input) are activation vectors. This NMF (F) or right singular value matrix merely changes perspective to viewing from a different angle (feature vectors as anchor reference/basis), but the topological relations between data remains the same

SVD maintains variance (high singular values to explain most vectors that make up data’s shape) while reducing dims

NMF and PCA are more specific versions of SVD. PCA has the mean activation vector as a feature (row), while NMF has all feature vectors have positive/zero values AND coefficients when composing into activations (makes it more interpretable if you think “what does negative mean”). 

The C matrix has activations as rows and features as cols because A ~ CF. The C tranforms the features into vectors from the activations as basis vectors; CF decomposes …

CCA: choose basis subspace that maximizes correlation between basis vectors

Few features vs many features: The few are the “most general” (obtain from SVD). The many can be decompositions of the few

Matrix of features to features: features decomposed as other features. We may think of these as relations because it says “how much” a col feature is of another row feature

Sparsity and minimal graphs

Pushouts aim to get minimal. Can putting pushouts in the loss function get sparsity?

Work backwards

What causes the output to fire high for that class? Work backwards. Are there multiple routes for it to fire high? Does the component at layer L-1 always need to be high? 

eg. We notice from ablation that ALL components in L-1 need to be present

Discrete vs continuous linear combination: if neurons use activation function that may make it more discrete (like softmax), discrete. But reLU is continuous. So this means activations are continuous.

When continous, don’t just measure by combos neurons! Need to measure individual changes in output activations! So put in A1, A2, and B inputs in and see what activation LEVELS, not just component, are similar for A1 and A2 (in which A is “both are about animals” and B is “not animal”). These activations are input values. The next layer’s weights are the coefficients! (this is just like coefficient matrix in NMF, or U in SVD).

So the NEXT LAYER is the feature; the activations just activate those features! We need to see what linear combo of input weights to neuron K_1 in layer K and previous layer K-1 activations (which use the prev layer’s output weights) cause that to fire. Work backwards; start from desired class (eg. vocab token) and see why different prompts which all have that vocab as final output give it a high value. 

If A1 and A2 have NO similarities, perhaps it’s alternate paths. What do these alternate paths have in common? If we take SVD on their activations, are there similarities? Perhaps the activations are different, but their SVD singular vectors are the same either in cosine sim (dir) or unembedding. 

---

Survey paper

same features both times (as measured by cosine similarity of features sorted by the canonical ordering of each singular vector set

The Linear Representation Hypothesis paper

Not all concept vectors are causally separable (eg. english-french and english-russian). 

---

Mindset

maguyver existing tools for unorthodox purposes; don't be held back by thinking you're automatically using them wrong for these unorthodox purposes. try them first, then check their validity.

dont be afraid of superficial sims; you must test to see if they are, dont just assume they're superficial bc they dont fix the orthodox ways ppl already uesd the tools for. embrace the superficial sims as actual rsch leads to re-create as if sculpting a dream, but now you're re-creating using the legos of algorithm tools. use algorithms as instruments where their re-arrangement will output the same feelings of the dream. vectors are feelings; find the right angles to calculate that will yield the common activation abstraction between unrelated inputs.

edit features from circuits, edit by adding relational feature vectors, but the training and analogies etc are for your own paper
just show this paper anyways as wip, but say jsut brainstorming and can go in diff direction that this

Based on openreviews, a lot of people when they use new techniques don’t know if they’ll work and the results are often cherry picked, so don’t be hesistant to try any new techniques and put them in a paper.