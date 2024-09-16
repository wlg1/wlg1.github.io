# Aug 13th Vidit meeting notes

temp

svd on ecncoder: if very different singular vals, then no universality or doesnt exist or far subtler

sort desc order to make decr vector (of diagonal). do it for both. L2 dist. may unit normalize in case one is just emphasizing more than other. U and V are just rotating

make sae smarter and would get universality? then as get smarter, svd of Es would conv to some univ list of nums.

num of nonzero singular vectors, get min(m, n). e' may have different one, then take smaller one and padding to 0. just in case,

let A be mxn matrix. cols and rows are not sacred. this linear map A: Rn to Rm. Rn and Rm have "isomorphisms". GLn or GLm are nxn invertible matrices vice versa. P in GLn means every vector x1 to xn, apply P to Y1 to yn, and Pinv brings y back to x. could prevserve inner product norm. still a lie group. Rn -> P to Rn. Rm Q to Rm. QAP^-1. if respect symm, no diff between two maps. Q in GLm . QAP^inv is also linear map equiv to A. But its cols are very different, so different basis. Natural symmetries get in the way of A vs QAP

can do SVD, as long as P has det 1

perturbation of Rn and Rm, can change Aij widlly, but can't change its rank and SVD. unitary transformation and is unique.

dont want to rotate and get diff answ

dont compare num by num bc nums depend on basis. roll E both out

sneeze on basis and norm completely changes

<<<
sample output space as densely as poss

where point cloud fail to be a manifold? svd or local pca, try to get best est of tangent space. hades by uzu lim. feed it pt cloud and will tell singular things. if get pt is singular, get neighb of pt find output whose is singular bc most likely to be singular

HADES: Fast Singularity Detection
with Local Measure Comparison