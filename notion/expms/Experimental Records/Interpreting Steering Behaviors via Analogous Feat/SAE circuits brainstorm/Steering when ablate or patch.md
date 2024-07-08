# Steering when ablate or patch

Start from existing features and find supporting features and backup features when ablated

This will help us find the exact side effects too

Subtract and decompose the patch

why certain layers? perhaps it’s because those layers contain that feature. but it is also because those features have important interactions with downstream layers, like in a feature circuit? then if we modify the feature circuit, perhaps we can 1) improve the steering vector (see above measurements) or 2) obtain steering on more specific types of behaviors.

multiple layers; multiple vectors may make it more specific

Use differences to find features

Why not just find features? Bc sv may not be found from saes. Can steering vector be found from saes?

Not just feature interactions, but component. Then find features in components 

Use diff of means to find vevs when decompose to find features and connect th9se features

what if subtraction makes actvs go to negative? where do existing prompts fall in measurement of love-hate? can we measure this via projection? 

---

put actvs thru sae to get features: run love, hate separately vs running love-hate

ablate components, **then** steer and see if still have effect. then narrow down to feature in impt components (that cannot be ablated)

search for sdie effects: see if features affected by steering vector have neg output on behavior.

we found that feature by decomposing sv, and not by activations before vs after steering

what if we just pass ‘love’ through and get top features for that activation?

what if we just steer this ‘love’ feature?

love-hate

friend-enemy

do they share features? is there an equation for features for each of them? these would ‘side effects’.

red dog - blue dog

red - blue

red dog VS red VS dog

are these features composite such that can actv both indp?

if so, we can just add them? if not, can we use a technq to add them?

- dog vs cat vs mammal vs animal
- pass each token in to decompose into features. do dog and cat share ‘animal’ feature? is this feature orthogonal to simplex? get cosine sim
- then use this to steer other prompts

steer by cluster

does steering love-hate also change outputs about friend/enemy using same vector? what if talk about love-hate and friend-enemy in same prompt?

further decompose features using another sae. ablate everything but that feature and reconstruct it. then train another sae on inputs for that feature to decompse it. 

---

Also, later layers have closer features. Why doesn’t it change later layers if it changes output signif?

ablate all the impt L6 features after steering

ablate and patch

compare features before + after steering 

VS before + after random additions

post vs pre

can we find the component(s) that outputs “I refuse” and/or “i am unable to”, and connect this to the steering vector? can we steer it to output a different phrase?

Eg) if refusal vector outputs “I am unable to”, does it affect components which outputs “I am unable to”?

Is the reason the steering vector may work at layer L and not earlier layers is because layer L and after would not have side effects, while earlier layers may?

Study concept vectors in intermediate space and see if orthogonality relations exist that would suggest simplex relations

how does steering vector at different stages of  training? when does it get effective?

First compare multiple steering vectors at diff layers

Decompose them

Perhaps downstream features not precise enough. Find them and steer only certain ones

Algo to sel

This is primary. Second is more specific fns

if steer, do we get different feature coeffs from pass in unsteered actvs vs steered actvs?

it’s okay if steering vector is done at post bc you cache the pre at later layers too, so just put them thru the pretrained saes

it could be possible that they’re more interpretable? we get a higher percentage of nonzero feature coefficients after steering.

What is a change in feature considered impt? Traceback? All features should change. Some drastic changes. Perhaps steer feature and ablate another feature. But why not just ablate that feature?

Can we distrust person type X but trust person type Y?

first compare interpreting features without relation to steering vector. what do we find?

then decompose steering vectors at each layer. compare their features. 

plot these features before and after steering. what happens to their simplex relations?

decompose sae into features

but also steer features in later layers too, and the upstream ones that affect the steering vector

claim: in IOI, they had stronger effect by steering features at multiple sites. another paper also argues that multiple vector steering is effective

why not just get steering vectors for multiple layers? yes, but then we decompose them. and we also see what they affect. 

an algorithm to select which multiple featuers across layers for steering is effective. develop it with chatgpt

In slides list assumptions of hypothesis and state how will test them. And if doesn't hold true how project still successful

If rind too compelx for safety vehavioes, then something in between ioi and deception or sycopjancu

Do you need this? Useful?

---

interacting features between love-hate and wedding- ablate that one and see what happens after steering both. measure change in actv vs output change in plot.

steer all related features. is there an effect? define related by semantic sim in embd space of token.

we can change the output by changing related features. 

an algorithm to select related features 

find the features that activate on ‘erotic’ or ‘friend’ and remove them- perhaps they’re the ones that out that word