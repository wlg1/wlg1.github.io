# Dot Product

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