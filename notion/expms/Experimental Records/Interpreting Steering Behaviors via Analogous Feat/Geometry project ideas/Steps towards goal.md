# Steps towards goal

Macro Steps:

1. Measure similarity kernel score across saes
    1. this allows us to show universality not just for ONE feature, but for MULTIPLE features in space
    2. issue: this does not locate and map specific features to one another, so that is addressed in future work
2. Identify simplices, circles, etc. in activation data using algorithms to measure relations and search for them in networks
3. Measure similarities of higher-order structures across sae spaces
    1. Eg) count topological invariant scores and compare
    2. issue: this does not locate and map specific features to one another, so that is addressed in future work
4. For feature actv (not weight) spaces, test how steering/ablating/patching changes the geometry in several layers. Compare these changes across models.
    1. This may compare circuits across models
    2. Compare this to changes in causal networks. Find small neigh circuit that steering acts on.
        1. this by itself is not novel enough as a paper, and risky if the steering vec circuit too complex to be found for behavior OR it doesn’t change anything about steering vec. but this is good as a finding within a larger paper. delegate this task to someone else.
            1. this is like an entirely separate project. but work on it on the side just in case it finds something? connecting geometry to circuits would be helpful.
                1. Your single plan of experiments finding how steering features connects to other features can yield two papers: this is useful for geometry too, but ANOTHER PAPER (such as workshop) can focus on steering vec circuits, but uses these same expms. So it’s not doing 2 things at once. The second steering vec circuits paper can be published after internship (ICML, or workshop) and you can mention it in interviews or make blog post (arxiv first)
    3. We can also compare circuits across models by measuring space sim using grokking-spline paper

Future work to mention

1. Map relations from one model to another using matching algorithm based on kernel similarity score and “feature labels” (how to get labels? by activations on inputs?)
    1. This may find “functionally equivalent features”
    2. This is riskier. May be for future paper.
2. Map structures (polytopes, etc) from one model to another
    1. First need to find structures AND mapping algorithm. May be for future paper.
    

first geom + topo metrics between models on sae weights

- toy models with diff inits
- which layer to compare for diff models? how does platonic repr do it?
- what if saes get very big? do we compare the same saes?

then do activations

plot 2d sae feature weights, acts

measure cosine sim as a matrix

feature splitting

plot steering vectors in geometric space

relate steering vectors to other features, then relate these relns across models

model similarity (platonic repr code)

---

composable geometry plan:

1. first find simplices for animal
2. then try to find for safety behaviors 
3. animal steering (cat to dog) and safety behavior simplex steering
4. see if concepts are also recombined in circuits

---

Why expect one layer to be same as another? Only if A and B are initialized same way as in Anthropci towards

This also reveals more about how feature splitting works

[https://transformer-circuits.pub/2023/monosemantic-features#phenomenology-universality](https://transformer-circuits.pub/2023/monosemantic-features#phenomenology-universality)
These A and B are different transformer toy models with diff random seeds

How do their steering ectore change if we can get steering vectors?

Multi layer toy models

Trivial is if they both get bigger they converge. But this is still an assumption. Also this studies specifically how they converge such as when. Would we see grokking as their features get more similar? When do they? How do they split?

Hard to compare models sith different layers but would be interesting to try, may be future work if too complex

but if models can get similar steering cectors , perhaps their features are also similar. We can do a univ test without geam matrices (or use it too but don't expect it) on diff models. Match anger feature on one to another based on feature activations

---

Msg kiho, bloom, conmy
Plan slides
Steer then plot
Gram matrices, cca on pretraiend saes

Toy models
Sae on toy models
Compare saes

One issue is that these saes don't train for the same features. But as you find the more true ones, they may. When do they converge?

1. compare plots to neuronpedia
2. label features 
    1. use labels from neuronpedia. can they be downloaded from saelens?
    2. auto-label based on similar output or actv plot

Feature actvs- measure sim

1. ‣
    1. ph paper did this for inputs, but we want feature relns
2. topact also did this for inputs