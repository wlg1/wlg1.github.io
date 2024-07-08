# Ashkan meeting notes

[https://www.lesswrong.com/posts/MFBTjb2qf3ziWmzz6/sae-feature-geometry-is-outside-the-superposition-hypothesis?commentId=W2Ed9KpznoEqtphg7](https://www.lesswrong.com/posts/MFBTjb2qf3ziWmzz6/sae-feature-geometry-is-outside-the-superposition-hypothesis?commentId=W2Ed9KpznoEqtphg7)

how to measure “ground truth” features? see makelov

under what conditions what they have similar features?

very subjective to dataset

is it trivial if two models on same dataset would have same sae features? but what if they’er different- is it just a fault of the saes? compare them under different sae conditions

SAE optimization conditions also affects. try different seeds, datasets

maybe there’s “more optimal” saes that would similar for different LLMs? optimal in terms of having saes share more features? perhaps can change sae loss condition to make them more similar?

random LLMs- would you find random featueres? cnns inductive bias enoug hto separate two objs, very sensitive similarity metrics. cca is sensitive.

when comparing ONE sae for each model, still a lot of randomness. may have to compare multiple sae instances somehow. splitting has randomness

would 2 different models handle arranging months/days circular in sae features, or differently and how different?

one guessed barrier is the randomness of saes and sensitivty. try small sae

“towards” claims both fire high on impt logits (like pred period) but not others

(multp by weights, assume lienarity) linear importance score- attribution score

weighting by logit weights (conn from actv)

[https://www.lesswrong.com/posts/MFBTjb2qf3ziWmzz6/sae-feature-geometry-is-outside-the-superposition-hypothesis#F6z8gu7nMMyDCLuxJ](https://www.lesswrong.com/posts/MFBTjb2qf3ziWmzz6/sae-feature-geometry-is-outside-the-superposition-hypothesis#F6z8gu7nMMyDCLuxJ)

We found these by (1) performing some graph-based clustering on SAE features with the cosine similarity between decoder vectors as the similarity measure. 

calude scaling paper is on exact halfwy middle layer?

torr nodes can’t handle 8 billion samples

prob wont work but who knows: before toy models or train saes (bc 8 billion samples in towards monosem), take existing saes on existing models and compare using metrics. probably wont find anything but decent starring pt to test techniques before spending time training. 

compare all middle layers

arabic script feature and arabic food feature if both actv across models, are their distances also similar? now extend this to even more features (polytopes)

two different distributions in feature space

subset of dataset only on oen topic (say food) as control, and see what are components. then need less data.

[https://huggingface.co/EleutherAI/sae-llama-3-8b-32x](https://huggingface.co/EleutherAI/sae-llama-3-8b-32x)

compare to sae on llama-2?

pre-existing saes cannot test about ‘feature splitting’ etc (unless those are also uploaded pretrained), would need to train own saes on existing pretrained LLMs (not good idea to train LLM from scratch unless toy model)

nonlinear months paper: why each month category has so many datapoints if it’s just “february”? are they prompts containing feb?

actually: the points are features and theres multiple features for February

- contrastive trainedly (platonic repr hyp) then close by design
    
    ![Untitled](Ashkan%20meeting%20notes%20cf47680d80a04812ac616fd4597e9e09/Untitled.png)
    

cca is good for different sae feature distributions, 

hinto paper: [https://arxiv.org/pdf/1905.00414](https://arxiv.org/pdf/1905.00414)