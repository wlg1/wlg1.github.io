---
title: CHAPTER 2.2.3
---
<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>


3. Cov matrix eigenvectors meaning? There is no permanent meaning; the matrix is just a tool of where to send concepts to (to re-frame persepctive).

after multp cov matrix by orig, eigenvec (lin combo of orig) just stretches.

**Stretching the eigenvdctors is the same as applying the matrix**

Diagonal can only be done on basis. So Q transpose is to get eigenvdctors onto basis.

Only square symmetric have orthogonal eigenvdctors. So to get sq sym for A, do AAtr and AtrA.

<<<
https://www.youtube.com/watch?v=mhy-ZKSARxI&ab_channel=VisualKernel

roate to get eigenvec to stnd basis so can stretch by diag. when eigenvectors on diag, diag of eigenvals stretches the eigenvectors. that's the reason there's a diag.

eigenvec are 'diags' of the square (orig)

<<<
3a. spine length eigenvector
3b. eigenvectors of cov matrix are vectors of lin combo of how each feature affects that col's feature
3c. scaling affects what's currently on basis
    why doesn't QQ^-1 = I? try lambda*Q; it's the same as Q*lambda

cov pts are pairs, and each axis is one of the orig x data pts (not the features of each x). pt (x1,x2): the proj along one of the orig data pts x1 shows how far away x2 is from x1. thus, an eigenvector of cov matrix is a lin combo of orig data pts (in which every x2...?)

or is it lin combo of orig features of x (not data pts)? cov matrix is multiplied by orig space, but are eigenvectors of the matrix's basis or of the basis the matrix is mulpt by? 

<<<
Is the eigenvector in the column of Q?
https://www.d.umn.edu/~mhampton/m4326svd_example.pdf
Yes, but it's the eigenvectors of X*X = A = QLQ^-1, not of X

https://en.wikipedia.org/wiki/Eigendecomposition_of_a_matrix
where Q is the square n × n matrix whose ith column is the eigenvector qi of A

(this is the anchor pt of the analogical reasoning)
(see fig1 in ch1.2)
Since the columns of matrix Q are the NEW coordinates of the concepts that were on the basis vectors, then multiplying by Q means the concepts that were on the basis vectors are now sent to the eigenvectors. 

In terms of body + face --> In terms of cat + rat
In terms of body + face --> In terms of eigenvectors

Q matrix:
face_ev1, body_ev1
face_ev2, body_ev2

So if the eigenvector is 'cat', we interpret the data in terms of cat. All we need to do to interpret in terms of cat is to use the eigenvalues (?)

We use cov=Q*lambda*Q^-1. Q^-1 sends concepts on the eigenvectors to the basis vecs. 
Since the columns of matrix Q are the NEW coordinates of the concepts that were on the basis vectors, the columns of Q^-1 sends the concepts on the basis vectors somewhere, as long as it allows the concepts from the eigenvectors to get to the basis vectors.

After Q^-1 sends the concepts on the basis vectors 'somewhere', lambda stretches them, then Q sends these concepts back to basis vecs, meaning that the concepts originally from the eigenvectors are no longer on the basis vectors, but are back on the eigenvectors.

Eg) Originally, face and body were on the basis vectors, and 'cat' was on the eigenvectors. First, Q^-1 sends 'cat' and 'rat' to the basis vectors, and sends face and body 'somewhere'. Then, Lambda stretches 'cat' and 'rat', moving two concepts 'p' and 'q' onto the basis vectors (cat and rat are NO LONGER ON THE BASIS VECTORS). Finally, Q sends concepts 'p' and 'q' onto eigenvectors ev1 and ev2.

What's important is that to remember that vectors and concepts are different- thus, what was on the eigenvectors is DIFFERENT from the eigenvectors themselves. Before cov = Q*L*Q^-1, the eigenvectors ev1 and ev2 had 'cat' and 'rat' on them. Afterwards, they have new concepts 'p' and 'q', and cat and rat are no longer on the eigenvectors. It is not right to assume that Q sends cat and rat back to the eigenvectors. The eigenvectors, contrary to an easily mistaken assumption, do not always have the same concepts on it!

QUESTION- if the concepts on an eigenvector are merely stretched, how does Q rotate p from basis onto eigenvector?
ANSWER- it's not about AFTER THE Q TRANSFORM, IT'S ABOUT AFTER THE A (COV) TRANSFORM! This is another easily mistaken assumption, because 'after the transform' is ambiguous, so you think it's Q and/or A, when it's just A. As you see in this link:
https://math.stackexchange.com/questions/2816259/geometric-interpretation-of-eigendecomposition
After A, the concepts on the eigenvectors are stretched. They don't necessarily stay in the same place- they're stretched!!! This is why they're useful to orient back again- you know where they're supposed to go originally, albeit stretched.

Why not just stretch eigenvecs? The reason is because we need to stretch what's on the basis using lambda, so we need to get cat and rat onto the basis. 

Ultimately, cov interprets the data in terms of cov. Remember, cov is how much one feature changes when another feature is changed.

The next step is to not take this example too strictly- when it comes to the cov matrix, what's on the eigenvector won't be 'cat' or 'spine length'. 

Another tricky thing is that when you multp by cov, the PCs (eigenvectors) should be on basis- but we showed that they're not. 
ANSWER- we don't multiply the data by cov, but by the eigenvectors of cov. This means we don't end up with cov on the basis vectors, but with the eigenvectors of cov on the basis. So we multiply the data by Q, not by A. The reason we do eigendecomposition on A is to find Q:

https://builtin.com/data-science/step-step-explanation-principal-component-analysis
"An important thing to realize here is that the principal components are less interpretable and don’t have any real meaning since they are constructed as linear combinations of the initial variables."

oddly enough, GANspace uses principal components to find interpretable edit directions

ev: "the line in which the projection of the points (red dots) is the most spread out."

Now why do eigenvectors with the highest eigenvalues have 'the most information' (most variance) about cov? That's its 'meaning'. 

https://www.youtube.com/watch?v=FD4DeN81ODY&ab_channel=VisuallyExplained
3m: information preserved after projection onto the eigenvector is given by the eigenvalue

C = xx = cov
eigenvalue = uCu = EV*u*u = EV * I

https://math.stackexchange.com/questions/3211467/why-eigenvectors-with-the-highest-eigenvalues-maximize-the-variance-in-pca

Not all eigenvectors contain a lot of variance; only the ones with the highest eigenvalues

https://www.visiondummy.com/2014/04/geometric-interpretation-covariance-matrix/
As we saw in figure 3, the covariance matrix defines both the spread (variance), and the orientation (covariance) of our data. So, if we would like to represent the covariance matrix with a vector and its magnitude, we should simply try to find the vector that points into the direction of the largest spread of the data, and whose magnitude equals the spread (variance) in this direction.

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
What are eigenvectors of neurons? A measurement that's preserved. But remember, eigenvectors are just the vectors, NOT the concepts.

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
https://www.projectrhea.org/rhea/index.php/PCA_Theory_Examples
Does PCA multiply by PCs? Yes:
https://builtin.com/data-science/step-step-explanation-principal-component-analysis
the feature vector is a matrix that has as columns the eigenvectors of the components that we decide to keep. Reorient the data from the original axes to the ones represented by the principal components- This can be done by multiplying the transpose of the original data set by the transpose of the feature vector.

<<<<<<<<<<<<
https://math.stackexchange.com/questions/2830554/multiplying-a-matrix-with-its-eigenvectors-stretches-or-contracts-the-vector-wit

<<<<<<<<<<<
Multiplying by covariance matrix means...
https://stats.stackexchange.com/questions/326508/intuitive-meaning-of-vector-multiplication-with-covariance-matrix
sum over the weighted covariances
 which means a value of how well Xi "covaries" in the direction of r.

https://www.researchgate.net/post/What-is-the-intuition-of-eigenvector-and-eigenvalue-from-a-control-system-perspective

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
https://math.stackexchange.com/questions/2816259/geometric-interpretation-of-eigendecomposition
the orthogonal matrix U determines in which directions this scaling happens

this shows eigenvec of cov:
https://www.visiondummy.com/2014/04/geometric-interpretation-covariance-matrix/
The eigenvalues still represent the variance magnitude in the direction of the largest spread of the data (just for cov matrix, not any matrix?)

<<<
https://www.youtube.com/watch?v=yDpz0PqULXQ&ab_channel=SteveBrunton
Robust Principal Component Analysis (RPCA)