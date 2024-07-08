# Feature splitting

features correspond to syntactic aspects. syntax becomes one single semantic aspect

multiple polysemantic features together act as monosemantic 

scaling monosem:

Features as Computational Intermediates

[https://transformer-circuits.pub/2023/monosemantic-features/index.html#phenomenology-feature-splitting](https://transformer-circuits.pub/2023/monosemantic-features/index.html#phenomenology-feature-splitting)

- san fran feature splits
    
    We also find evidence of [feature splitting](https://transformer-circuits.pub/2023/monosemantic-features/index.html#phenomenology-feature-splitting) [8] , a phenomenon in which features in smaller SAEs **“split” into multiple features in a larger SAE, which are geometrically close and semantically related to the original feature, but represent more specific concepts**. For instance, a “San Francisco” feature in the 1M SAE splits into two features in the 4M SAE and eleven fine-grained features in the 34M SAE.
    
    similar features have small angles between their dictionary vectors.
    
- idealized features
    
    We conjecture that there is some idealized set of features that dictionary learning would return if we provided it with an unlimited dictionary size. Often, these "true features" are clustered into sets of similar features, which the model puts in very tight superposition. Because the number of features is restricted, dictionary learning instead returns features which cover approximately the same territory as the idealized features, at the cost of being somewhat less specific.
    
    In this picture, the reason the dictionary vectors of conceptually similar features are similar is that they are likely to produce similar behaviors in the model, and so should be responsible for similar effects in the neuron activations. For instance, it would be natural for a feature that fires on periods to predict tokens with a leading space followed by a capital letter
    

if the sae is better, then we can steer by features. so will a very big sae decompose into many composable specific features? red dog → red, dog

if so then we can steer by “analogous” hierarchical, wacky specific compositions

does feature splitting occur earlier for sae from 12mil to 18mil, then take approach

are there features that sae can’t isolate? feature splitting may do this, so try this

if you have really good sae, you can just steer with those features, so don’t need steering vector?

you still are interested in how steering those features affects other features? and can bthey be deocmposed