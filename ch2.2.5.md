4. SVD

Based on:
https://www.youtube.com/watch?v=vSczTbgc8Rc&ab_channel=VisualKernel

Since Q are eigenvecs of A, it makes sense that U are eigenvecs of cov matrix. if we switch into X^T * X = V*lambda*U^T, it follows that V, from XV = V*lambda, are eigenvecs of X^T * X b/c the final operations are to send concepts from old basis onto eigenvecs, and cols of V are where these eigenvecs are.

https://www.techadhyapana.com/post/linear-algebra-9-geometric-interpretation-of-eigenvalue-decomposition
(V^(-1)) times x1 or x2 will map the Eigenvector to the standard unit basis of R^2 vector space (e1 and e2 shown in fig 1)

<<<
***Multp by eigenvectors: send concepts in basis to eigenvectors
The eigenvectors of cov are a lin combo of data pts where concepts in old space are simply stretched. This concept may be 'spine length', a combo of body len and quill len. This concept is STILL PRESERVED! In prev examples, we saw 'body face' is gone in the new space; but in this new space, spine length remains. This means we can still measure the data along spine length, except we simply measure then multiply it by an eigenvalue. Spine length becomes a good calibrator to make sure the info in spine length is preserved- if that info is preserved, then much info about the original variance between data pts is also preserved!

When multp by cov matrix and want to reduce dim:
Choose the eigenvectors that are stretched the most because when we're reducing dim, we lose info, and "stretch the most" means much of the MATRIX itself is still preserved. We want to preserve the matrix as much as possible, but simplify its dims. IE) We have a box but want to reduce its size to fit in a cabinet. However, we want to keep as much of the space within it as possible. (??) Eigenvalues make up the dimension of this space, so choosing largest eigenvalues chooses to keep as much space as possible. "As possible" means we can only choose k dims to keep. "Reducing this size" means removing some dims- Eg) turning a 3D box into a 2D rectangle, but this rectangles keeps as much of the original space as possible. This 2D is NOT A SLICE OF THE 3D, but 'squishes' as much as of the 3D into 2D space; the new rectangle's area it should be larger than a slice of the 3D, as it tries to contain as much of the vol as poss.

https://programmathically.com/singular-value-decomposition/
If X has rows 'cust' and cols 'food': 
[wrong assumption that ex. in the link is good; it should have data pts as rows, featuers as cols, to be consistent with our site. The paragraph in link also contradicts its figure as it says 'customers as rows']
X * X^T = cov of X w/ (dim_cust * dim_cust)
Its eigenvectors in U (dim_cust * dim_cust = 3 * 3) are a lin combo of the original cols 'food', and are where each food concept from orig basis vectors (wine, etc) are sent. So wine goes to the first col of U, an eigenvector of X. But we had 4 concepts, and now there's only 3 places to send them. Where are they sent? 2 of the concepts are split into 2, then joined together and sent to one places. The splitted concepts lose information in the transformation.

We see that originally each row cust had 4 dims- 4 foods as cols- but now, they only have 3 dims. The 3 new cols in U are NOT THE ORIGINAL FOOD COLS, but lin combos of them. Now we have one col 2.5*bourbon + 0.5*blueberry_juice, instead of one col bourbon and one col blueberry_juice. This new feature (an eigenvector) states we can measure a customer in terms of their tastes in bourbon and blueberry_juice, as together they create "Cocktail" (that is, assuming no additive effects and that it can be disentangled cleanly into its parts, which is rare for food). Someone who enjoys a lot of bourbon but not blueberry juice that much would somewhat like the cocktail, but someone who enjoys BOTH bourbon and blueberry juice would like the cocktail even more. 
    https://www.thespruceeats.com/how-to-measure-a-cocktail-using-parts-760305
The cocktail measurement measures both bourbon and blueberry_juice using just one measurement instead of two. It finds that it's more impt to find one's tastes in bourbon to have a stronger enjoyment of the cocktail.

Now what about V? That's the transpose- switching cols and rows- meaning X^T * X w/ (dim_food * dim_food), and V is (dim_food * dim_food), and it moves customer concepts onto the cols- but this time, instead of losing info, there is a new dim? How? Perhaps customers are split and a splitted part is sent to a new basis vector?

V^T is also (dim_food * dim_food). if we multiply V^T * X, where X is (dim_cust * dim_food), is this even possible? Only for X^T. Let's handwave that for now and do V^T * X^T. 
But actually- Whenever we do X^T * X, we also transpose the input, as we can't do X * input given X's dims. (?)

Since we do X^T, now the food is rows and cust is on cols. That's why we send the old cust basis to...

What's also strange is U * V. If they have diff dims, how are they supposed to multiply? The answer is that the scaling matrix would remove a dim. That is- some eigenvectors have eigenvalue of 0 (they are in the null space, as eigenvalue of 0 means =0*v = 0). But that means U must always have lower dim than V.

For U * V to work, we must have dim_cols_U = dim_rows_V. 

Actually, this is how:
https://www.d.umn.edu/~mhampton/m4326svd_example.pdf
The eigenvalue matrix is NOT SQUARE, unlike U and V. It was a wrong assumption to mean it must be. Thus, if we have 2x3 lambda and 3x3 V, we get lambda*V being 2x3. 

NOTE: just because one col of lambda is all 0, does not mean lambda*V will have a col that's all 0.

Also, the wine-cheese was a bad example because the M in that case was not square. Though SVD works for rectangular, cov of A * A^T is always square, so [following is WRONG- U and V will have same dim anyways- wrong b/c A^T*A has diff dims]

http://www.math.pitt.edu/~sussmanm/2071/lab09/index.html
Note this statement: right singular VECTORS correspond to vanishing singular values of A*A^T (BUT NOT OF A^T*A; for that, it's the non-vanishing eigenvecs!). That is, they have eigenvalue of 0. 

What's strange is that the rank of A seems to = rank of U, unless it doesn't. That is, by thm, rank(A) = rank(U) + rank(V), meaning if rank(V) > 0, rank(U) must be less, meaning some cols in U are lin dep. 
rank(U) = number of eigenvalues = number of rows of lambda matrix

it seems lambda is originaly square diagonal, and is only padded with 0s to be multiplied by V. but is it possible that V is smaller than U- that is, more eigenvectors in null space?

https://en.wikipedia.org/wiki/Singular_value_decomposition
For example, in the above example the null space is spanned by the last two rows of V⁎ and the range is spanned by the first three columns of U.
But V was 5x5- what does each col of V mean then if only last two cols of V (last two rows of V^T) are in null space?

How was SVD derived? 
https://gregorygundersen.com/blog/2018/12/20/svd-proof/

If some cols of V are in null space, the rows are V are how the new basis space uses the old basis space. Remember that V sends basis vectors to the cols of V, and V^-1 sends them back.

A * A^T seems to be cov matrix for data pts. So U, its eigenvectors, are lin combos of features, and are data dist of....
A^T * A seems to be cov matrix for features. So V, its eigenvectors, are lin combos of data pts. [still not sure how this conns to being in null space of A]

<<<
IMPT NOTE: the eigenvectors of a matrix X are NOT in its cols. In X, the concepts in its eigenvectors are simply scaled, and the concepts on its basis are NOT sent to the eigenvectors of X! However, if we put the eigenvectors in a col, we get a matrix where we send the concepts on the basis to the eigenvectors.

<<<
https://math.stackexchange.com/questions/1771013/how-is-the-null-space-related-to-singular-value-decomposition

https://math.stackexchange.com/questions/3359693/what-is-the-true-meaning-of-using-svd-in-finding-null-space
A = u * sigma * v^-1 * x
A = u * sigma * v^-1  -- focus on this
Av = u * sigma

v sent the eigenvectors of X^T * X, from the space in X, to the basis vectors, simultaneously rotating the basis vectors of X. V is a space of vectors; some of these vectors will be 0 when multiplied by A. 

Geometrically, we know the eigenvectors of X*X^T. Geometrically, what is the null space?
https://math.stackexchange.com/questions/21131/physical-meaning-of-the-null-space-of-a-matrix
The null space are the set of thruster intructions that completely waste fuel. They're the set of instructions where our thrusters will thrust, but the direction will not be changed at all.

Basis for null space:

What does A^T * A look like? What does A * A^T look like? What about their eigenvectors?

Relate null space of A to eigenvectors of A * A^T
How does col space fit in?
https://math.stackexchange.com/questions/500782/what-is-the-relation-between-the-eigenspace-of-a-matrix-and-its-column-space

http://www.math.pitt.edu/~sussmanm/2071/lab09/index.html
the right singular vectors (the columns of $ V$) provide groupings of words that are related according to their use in the documents, and can be regarded as ``concepts'' appearing in the documents. The left singular vectors (the columns of $ U$) provide groupings of the documents according to the words.