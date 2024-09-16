# Bei Meeting Aug 16th

strong expm evidence : mapper captures branching behavior, 

obtain collection of actv vectors

have student using language model word embeddings mapper is extension of topobert

topoact: even if see branches out of img actvs, interpretability of why two images of horse and deer- why are they together? 

transformer vs sae mapper graphs: if they’re further transformed, then hypothesis is mapper graph from feature vectors would be an even better representation of sepration class. 

is months circle in llms?

pca could be misleading, so is orig high dim space?

months looks more branching than circular? 7 branches perhaps?

tda has diff way to detect circular struc

[https://www.sci.utah.edu/~beiwang/publications/Branching_BeiWang_2011.pdf](https://www.sci.utah.edu/~beiwang/publications/Branching_BeiWang_2011.pdf)

if have sufficient sample it will start conn, but fig 1 

bifurcation: want to argue 

what is effect of sae on mapper graph of actv space? 

how much improvement in bifurcation structure? 

[https://www.sci.utah.edu/~beiwang/publications/Compare_Activations_BeiWang_2023.pdf](https://www.sci.utah.edu/~beiwang/publications/Compare_Activations_BeiWang_2023.pdf)

run multp times bc optm to get mini (optimal transport). bijection between their points. natural alignment, so now use this to measure dist

if 2 mapper grphs not the same- does sae feature graph create more isalnds? if branch struc in resnet18, branches all come off into islands. depdns on mapper params- range of params wher structure is stable. seee branching struc in all range of params. so loops (esp very small) maybe not enough data. does manifold have hole, or not enough data?

mapper graph is built on reeb graphs which is a skeleton, so if space with proj fn

branching struc is conn between saddle and extrema. that’s what captures

[how detect branches](https://github.com/tdavislab/mapper-compare)

global corr but also structure cocorrespondces

aaai 2023 try both pershom and mapper

[https://www.sci.utah.edu/~beiwang/publications/AAAI_Activation_BeiWang_2023.pdf](https://www.sci.utah.edu/~beiwang/publications/AAAI_Activation_BeiWang_2023.pdf)

if have perturbations to data, model is less robust. put images in gaussian noise then topological signals disappear

inhouse tool called mapper interactive built on top of kepler mapper

comparisons: optimal transport method is best. others are hard

MSID

this is pt cloud lvl, not graph lvl

gromov wasserstein distance

persistent homology: not as strong a tool, 

position paper from ICML: 

[https://www.sci.utah.edu/~beiwang/publications/Position_TDL_BeiWang_2024.pdf](https://www.sci.utah.edu/~beiwang/publications/Position_TDL_BeiWang_2024.pdf)

actv space done in aaai paper, but ph not as powerful. 0

Ablate the branches