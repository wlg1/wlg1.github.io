# todd hamish meeting

[https://en.wikipedia.org/wiki/Plane-based_geometric_algebra#Projective_geometric_algebra](https://en.wikipedia.org/wiki/Plane-based_geometric_algebra#Projective_geometric_algebra)

[https://direct.mit.edu/netn/article/5/2/549/97548/Simplicial-and-topological-descriptions-of-human](https://direct.mit.edu/netn/article/5/2/549/97548/Simplicial-and-topological-descriptions-of-human)

generalization of a venn diagram

there’s a plane where triangle is in. geometric algebra does planes, not triangles

quaternion: rotation is a 3d simplex added to a 1d simplex (3 vol add to 1 vol). N vol added to (n-2) vol. 2d sphere added to a point, so is around a point. a 3d sphere rotates around a line.

rotation using n x n matrix- but getting an axis from the matrix (an eigenvector problem) is very painful , but geom alg says if you have a transformation then it can break into pieces and ask about those pieces (such as axis of rotation) 

you have something that preserves N things and rotates everything else 

linear features beget a linear plane since the plane / convex hull 

projecting 

for any k vol, can always ask what’s the transformation that this k-vol encodes

shapes and transformations are the “same” in geometric algebra. what happens if you transform a “tree” using the concept “dog”

reflect, rotate, generalizations of those

screw motion is a strange transformation

[https://bivector.net/tools.html?p=3&q=0&r=0](https://bivector.net/tools.html?p=3&q=0&r=0)

code to multiply these things, use cayley table

assume A*B = C. Also define inverting C^(-1)

sandwich product: X*Y*X^-1 = Z → this is alll you need to transform Y with X. if X is rotation, then Z is what you get if you rotate Y. 

N = 2000 (embedding space), X is rotation in N dims, therefore X is a N-volume added to a N-2-volume

N choose 2 plus 1 is dim of X, 2000 choose 2 is approx 2 million, still theoretically feasible to store

XYX^-1 : how long? X^-1 just negates 2 vol part. but multiplying the rest would be a lot of compute, need ot use, would want to use sparse repr

computational adn expm wise: find vector representations of features, and find relations between these vectors. but can we also represent features in other ways and then perform transformations

any k-vector is a vector. here they use 1-vector. actv adding is just 1-vector in 4098 dim space.

generalize distance

distance at angle is different

plane and point is just distance (not angle)

pair of lines and in most dims this is the case, they have both a distance and agle form each other. geom alg can extract the angle and distance, so not forced to use distance. 

simplest transformtion of this one to that one