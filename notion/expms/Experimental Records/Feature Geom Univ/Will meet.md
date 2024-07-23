# Will meet

l1 on features, not output recon

embedding is conditioned on sample, not just tokens (batch, seq)

probabilistic manifold on actvs

each time plot token, it’s sampling from distribution

based on formalizing what a feature manifold, ways to show bounds or convergence of feature manifolds

no closed form manifold; implicit form poss only; in order to have closed form, need to find the projected area of those tokens and parameterize that proj area directly. eg) equation- if pts on manifold then equation satisfies =0. else, not =0. 

if y=f(x) where y is encoder of SAE, y are sparse feat coeff, is not easy to obtain an eqn without using x. y=f(x) is implicit def of manifold instead of explicit. implicit means can only find mapping between manifold, not manifold.

f(y) = 0 satisfies on manifold, else is not. 

can still try to find intrinsic dim of implicit, or use this as a regularization (instead of L1 reg, use other reg that can optimize for extrinsic dim, which is dim est of manifold)

make estimate of this manifold for some property such as dimensionality

actv manifold is probabilistic (estimation)

build up radius graph and use locality of raidus graph (local cluster / subgroup) then optm for est of the genus of the graph

use stnd norm so all nodes are conn in cutoff, so with batch sample a raidus graph

dim is genus

point cloud to mapper is hypergraph (not 1-1) of radius graph (which is too expensive)

sae not optimizing for consistent 0

not for all tokens, 

each token has diff zeroes

if no group sparsity, not restricting to manifold dim

this projs to a higher manifold dim

count the actually dim of the feature manifold 

how many features consistently are 0. total feature dim - dead feature dim = real space dim

SAE loss: optm for geometric targets (smooth), so use laplacian of graph so constrain eigenvalues to impose manifold smoothness, so want smooth manifold that can be plot so can easily analyze its properties for analyzing

train to get features which are already on smooth manifold that’s low dim; existing SAEs may not find low dim manifold structure

is sae dim reduc? this sparsity is formalized. l1 sparsity- huge euclid dim but actual data is only small subset of it. but data manifold is not subspace it takes. std basis like a1 to aN, sparsity for diff tokens only a subset of those index (as1 to asn), n << N. then 

manifold poss has weird topology, so theoretical soundness cares about topology of feature manifold

continuous homeomorphism between two planes, can compute how likely homemomorphism between two manifolds, then homeomorphic

how exact are those data pts in higher dim that can be explained ; by look at locality of these manifolds. look at neighborhood of graph, if look at any neighbor of graph. if neighbor of dog is cats; how likely they itnersect with their graph can approx homeomorphic

compu of two nodes; manifoold sim . dog cat. instead of stnd norm, compute only with dist defined on manifold. shortest path on radius graph. this approximates it.

---

lens function- dog features?

![Untitled](Will%20meet%20c258bd9c464d453a90a6c7110cece677/Untitled.png)