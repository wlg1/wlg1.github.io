# Dot Product

- Can you only take dot product of two vectors if they use the same basis?
    
    No, the dot product of two vectors can be computed regardless of the basis they are expressed in. The dot product is a scalar value obtained by multiplying the corresponding components of the two vectors and summing them up. The basis vectors are used to express the vectors in terms of their components, but the dot product itself does not depend on the basis.
    
    The dot product of two vectors can be calculated as follows:
    
    For two vectors v and w expressed in terms of their components:
    
    v = (v₁, v₂, v₃, ..., vₙ)
    w = (w₁, w₂, w₃, ..., wₙ)
    
    The dot product v · w is given by:
    
    v · w = v₁w₁ + v₂w₂ + v₃w₃ + ... + vₙwₙ
    
    The dot product is a scalar value that represents the projection of one vector onto another, providing information about the alignment or similarity between the vectors. The basis vectors are used to express the components of the vectors, but the dot product itself is basis-independent.
    
- Can you only take dot product of two vectors if they are in the same vector space?
    
    Yes, in order to take the dot product of two vectors, they must be defined in the same vector space. The concept of dot product is defined for vectors in a particular vector space, and the vectors must share the same underlying space for the dot product operation to be valid.
    
    A vector space is a mathematical structure that consists of a set of vectors along with operations of vector addition and scalar multiplication. Each vector space has its own set of rules and properties, including whether or not a dot product operation is defined.
    
    In some cases, different vector spaces may have their own notion of a dot product, such as the inner product in complex vector spaces or the dot product in Euclidean vector spaces. These dot product variations may have different properties or definitions, but within a specific vector space, the vectors involved must still be elements of that space.
    
    If two vectors belong to different vector spaces, it is not meaningful to compute their dot product because the mathematical framework for the dot product may not be defined or consistent between the spaces.
    
- Does being in the same vector space mean having the same basis?
    
    No, being in the same vector space does not necessarily mean that the vectors have the same basis. The basis of a vector space is a set of linearly independent vectors that span the entire space, and it is not required for vectors in the same space to have the same basis.
    
    In a given vector space, different sets of vectors can form valid bases. Any set of linearly independent vectors that span the entire space can serve as a basis. This means that vectors in the same vector space can be expressed using different bases, as long as the bases are valid and span the space.
    
    For example, in a two-dimensional Euclidean vector space, the standard basis consists of two linearly independent vectors, usually denoted as (1, 0) and (0, 1), which represent the unit vectors along the x and y axes, respectively. However, another valid basis could be (1, 1) and (-1, 1), which still spans the same vector space.
    
    The dot product of two vectors is independent of the basis chosen to represent them. The dot product is defined by the algebraic properties of the vector space, not by the specific choice of basis. As long as the vectors are defined in the same vector space, the dot product can be computed regardless of the basis used to express them.
    

dot prod sim: the closer a vector is, the bigger its projection will be onto the new axis. the farther it is, the smaller its proj will be
closer means "it has more of that measurement"
if a cat point vec was already close to the nose vector, that cat had a big nose. it faced in a simialr direction to it.

this may be wrong; imagine 2 axis. what if nose=3, but ear=2? and nose=3 and ear =6? in both cases, have same nose, but latter is farther.

ask chatgpt for dot prod sim
using an example where the vectors correspond to human interpretable terms, explain why dot product similarity measures vector closeness

does a higher dot product mean the vectors are geometrically closer?

No, a higher dot product does not necessarily mean that the vectors are geometrically closer. The dot product similarity measure is not a measure of geometric distance between vectors. Instead, it is a measure of the similarity of the values of the corresponding elements of the two vectors.

thus, this was wrong.

geometrically, what does it mean for two vectors to be similar?
Geometrically, two vectors can be considered similar if they have the same direction or if they are pointing towards the same general area in space.
parallel (more sim) vs orthogonal (no sim)

direction is measured by ratio. each feature is a direction (ratio of lin combo terms).
(x1, x2) is a vector composed of orthogonal basis vecs
it's a vec within that as a space
(w1, w2) is a vector also in that space. that's the new dir being proj on!
(x1,x2) is proj onto (w1,w2). the closer (x1,x2) is to the w vec, the "more similar" it is to (w1,w2). that is, if w vec measures nap, (x1,x2) may be very close to measuring nap too!