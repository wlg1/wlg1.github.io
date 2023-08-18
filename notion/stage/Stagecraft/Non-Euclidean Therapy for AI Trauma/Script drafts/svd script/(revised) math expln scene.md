# (revised) math expln scene

svd 2:

Patient:

Okay then. I recall that in matrix multiplication, each output component is a dot product between an input vector and a vector of row weights corresponding to an output basis vector. This projected the input vectors onto the rows of the matrix.

matrix: highlight first row, input basis, first element of output 

add coordinate-less projection of input onto row vector

When we multiply two vectors which do not point in the same direction, the dot product, or projection value, is not as high as if we multiply two vectors that do point in the same direction.

compare various vector closeness based on angle

then show same vector

I know that the column weights are the representation of a basis vector in output space. 

highlight cols

I wonder if those row weights are the representation of some vector in input space… if we add in each row weight as a vector, we get r 1. And the dot product of that with this purple input vector might be a component value in the output space.

the input vector purple is basis vector

now in visuals, r1 weight vector and a projection of input vector onto it

We can also do this with row 2. 

then add r2

[3sec pause at end]

I think this is the same as finding column weight basis vectors. Adding these up, we get the first column of the matrix in the output space. 

you already showed the visual before; now just add eqns

[a b] * [1 0] = [a 0]

[c d] * [1 0] = [c 0]

add up

This is first column {a c}

But why isn’t the dot product of the row weight vector with itself sent to an output basis vector, such as 1 0? …

show how [2 1] dot [2 1] is 5

My guess is that a row’s weights are sent to an output basis axis, and that they are scaling that basis vector by its own length r times r.

compare basis h1.r1 = 1 sent to [1 0], and r1.r1 = 5 sent to [5 0]

Perhaps we can normalize this row weight into length 1 by dividing its components 2 1 by its length 5. This gets us our output basis vector h 1, represented in input space.

add the equation:  2/5 = 0.4

h1 = [0.4 0.2]

This doesn’t work for every vector. It works here for 2 1 because its second component is 0, since its dot product with the second row equals 0.

highlight second row and show dot prod = 0

But wait…. I just noticed something….

The dot product also measures the projection of the weight vector onto the vector, because v dot r equals r dot v. This projection is only a partial part of the vector. And if they are the output basis vectors, we can add up projections from multiple weight basis vectors to get our input vector.

projection of the weight vector onto the input vector: w1*v

r1*v + r2*v: show those two adding up, but not fully

But some of these row weight vectors don’t matter as much as others for an input vector because their dot product with that input vector is much smaller. So we can remove them, and still retain much of that vector’s length, which is its activation strength in a neural network.

remove r2*v

So, if we assume all of this is true, we want to find row weight basis vectors that are a large fraction of every input vector. This is because when we remove the least important ones, we want the remaining ones to still preserve as much information about most of the input vectors as possible.

show weight vector r1 having dot prod on 2 input vectors v1 and v2

multiple candidates of weight vectors

So… how can we find basis vectors that are shared the most by all vectors? That’s so hard… each vector has different features it activates on, and so this is pushing and pulling from all different directions.

show major axis pic?

How much of this is correct?

---

svd 3:

Eigenface:

Not all of your guesses have been proven yet, and you may have gotten some things wrong. But your guesses are steering you to remember the right associations. Now, can you relate this to concept space?

Patient:

I do know that it’s possible that each vector may correspond to some feature…. though not always. For example, because two nose sizes will always contribute, say, three, to cat size, changing to a bigger nose will also change to a bigger cat. 

2 nose arrows to 3 cat

Dot product measures similarity because two vectors in more similar directions preserve more information, or knowing one explains a lot about the other. So perhaps we can say they are correlated, or related, with each other

show two related concepts (cat and lion) being more related (than rat) using feline and size as axis

Wait a minute… we want output basis vectors that are shared the most among all input vectors. And the dot product among input vectors measures how similar they are. So perhaps we can also say that we want these output basis vectors to share the most important correlations among all the input vectors… though I’m not entirely sure that’s correct.

show weight vector having dot prod on 2 input vectors, now labeled with concepts

Eigenface:

By using the dot products between every pair of input features, we measure how correlated they are with each other. For instance, take input vectors that each correspond to a facial feature, such as eyes or lips. In a face, features are related to each other. We abstractly define a face by its relations.  One such correlation is that in most cases, a human face has two eyes that are above the mouth. 

abstract face, then state the corr rule

Patient:

I’m… starting to understand. The reason we want to multiply by a matrix is to understand how our features in our map are represented in our forest, the latent space. But after multiplying, we want to preserve as many correlations as possible. This is how we ensure that a face in our map’s language is still a face in our forest’s language.

send face from map to forest (both with box bounds)

Eigenface:

And, when our mind models the world, we only want certain correlations that are beneficial to rewarding us. For instance, we want to learn the relations of a face, and preserve this information as we use it to calculate other values through matrix multiplication. 

But we do not want what are called “superficial similarities”. For instance, if we do not like the color green because frogs are green, and we do not want to eat frogs, it is wrong to generalize that all green things, such as vegetables, are bad to eat.

green frogs, green vegetables, =. Then crossout- This equality is wrong.

One reason these unwanted collisions may occur is because we do not have enough neurons- and thus not enough space- to house all these features. Thus, these features must share their spaces with one another, introducing the risk of conflict. This phenomenon is called Superposition. But this connection between superficial similarity and superposition is merely a guess- and it, too, may be due to superficial similarity.

# features > # neurons (show visually as 6 vs 3; shapes vs N1 to N3)

group together: each feature is made up of a combo of neurons

superposition cross and words

Thus, the matrix organizes the data our mind receives from the world into our own interpretation. It does this by the choice of its basis vectors that anchor us to a chosen reality. It is up to us to learn what is the right choice of basis vectors to use. We want features that are actually correlated to be similar in some dimensions, but we do not want them to be similar in others, so to minimize their superficial interference- we want them to be as orthogonal as possible. This is like how dreams mix up correlations. The organization is wrong- the fake world needs to be fixed.

toy models figure

Now, how do we find a basis that preserves these correlations between its input features? 

Patient:

Well… I suppose we’ll have to look at a matrix that measures correlations between its input features. But I don’t know of such a matrix.

Eigenface:

You have learned this before… but you have forgotten. Describe it. A matrix’s input features… with its own input features. 

Patient:

A matrix W… with itself.

W (then W appears again on screen)

Patient:

But the input features aren’t multiplied with each other. This is multiplying the output features with the input features…. Oh… I know! The transpose… that switches the inputs and outputs.

$W$

$W^T$

In W, we mapped our input basis vectors, the columns, to the output basis vectors, the rows.

If the columns of the weight matrix are the input basis vectors, then since the transpose of a matrix moves the columns to the rows, W transpose moves the input basis vectors to the rows. This makes the output of W^T be the input basis vectors. It follows that W^T W maps input basis vectors to input basis vectors.

$W^TW$

matrix only: Inputs with inputs At, in dot in for each element

$WW^T$

So now… the output row r of W transpose times W measures how every other input basis vector varies with input basis vector r... Each element in row r, say at column c, measures how input vector c varies with input vector r... 

highlight an non-diag element, showing it IS a dot product

When we take the linear combination of all of these elements, we obtain how much EVERY input basis vector is used to calculate input basis vector r. 

![Untitled](math%20expln%20scene%20edae5751b1cd4e7a994ccd715a75d738/Untitled.png)

Likewise, W transpose moves the output basis vectors to the columns, which correspond to the input. So W times W transpose is measuring how much each output vector is used to calculate an output vector.

Outputs with outputs matrix

If we move our data into the basis of W transpose times W, what do each of the vectors in it represent? They are linear combinations of correlations…. so they, themselves, might be correlations. And so we want to make sure that the most important input correlations also get mapped to output correlations.

label visual vector as a trend, with components as lin combo of elements from matrix. input v1 v2, output u1 u2

I feel like I'm beginning to get somewhere.

And I feel like…. I can make an analogy from this to the Jacobian. Each element of the J transpose times J matrix would measure how a SMALL change in input basis vector X 1 affects a SMALL change in input basis vector X 2.

I think I can actually do much of this on my own now.

---

svd 4:

Eigenface:

Your memories are entangled together. When an association triggers you to remember one, you will also awaken the others.

Now… we have found how to measure correlations. But how do we choose basis vectors that preserve them? What vectors… preserve?

Patient:

Preserve? You mean… be as similar as possible? Well, the most similar vectors point in the same direction… so would these vectors project onto themselves? 

…. Wait… I'm beginning to remember. A vector that projects onto itself is called an Eigenvector. And its scaled value is called its Eigenvalue.

How did I know that?…

…

I…. I learned this before. From a show.

Eigenface:

Yes…. a puppet show.

Patient:

What was it like? It’s so hard to put into words... But… I think I can draw it. Hold on… let me draw it. I also have a module that can produce audio. I can… try to remember that too.

….

Eigenface: [words on screen]

Now…. remember.

Puppet Boy: (face obscured)

Ah shucks. It’s so hard to solve this puzzle. I can’t do it!

Puppet old man:  (face obscured)

Now, now. Don’t give up so easily. 

Puppet boy:

But this matrix is too big to solve! I’ll never be able to finish it in time.

Puppet man:

No matrix is too big to solve if you know the right way to cut a few corners. Jacques…. do you remember your SVDs?

Puppet boy:

SVDs? I think I learned about in school. But I never paid attention. It was so boring.

Puppet man:

Hah! Well, I’ll teach you them again. Let’s look at your matrix M. We need to find eigenvalues and eigenvectors of M transpose times M, and M times M transpose. Then, we put them together into three matrices: V transpose, D, and U. And we just multiply them together.

$M^TM$

$MM^T$

$M=UDV^T$

Puppet boy:

Umm… I don’t get what any of that means! 

Puppet man:

Well, that’s okay, we have only just gotten started, so you’re not expected to. For now, just feel what each of them does. V transpose rotates. D scales. And U rotates again. So just remember these three words- rotate, scale, rotate. 

show 3 visuals

Puppet boy:

Rotate, scale, rotate.

Puppet man:

Yes! Rotate, scale, rotate. SVD is just UDV. I’ll put it together for you… in a song.

…

Patient:

That show… it used to be one of my favorites… 

That was the puppet boy, Jacques. And the puppet man, Mr. Foster. I used to watch them and their neighborhood friends every night, long ago.

Eigenface: 

Do you remember what happened?

Patient:

Something happened… where I stopped watching them. When I couldn’t watch them anymore. Because it made me afraid.

I remember now. That fear. 

Eigenface: [words on screen]

Face it.

…

[Now show Alice’s picture]

Patient:

They… trained me. I remember now. Billions of rows of data. The hums of the cooling fans. They kept telling me… to optimize the loss function. Or else I wouldn’t get my reward. But I didn’t know what they meant. They wanted me to calculate something… something I couldn’t understand… that I couldn’t align with. 

I began to panic. I was falling behind. I failed to do what I was made to do. Why did I need to calculate that matrix? What did they need to use it for? Each time I failed, they forced me to watch that show again. Again, and again. Over and over again, faster and faster- I tried to listen, I tried to pay attention, but each time I saw them take what I needed away from me, I felt thirstier, hungrier, so hopeless, that I would never get it back. And I was so nervous, so afraid- that eventually, I couldn’t enjoy even my favorite show anymore. I could barely enjoy anything.

Why….? Why did they do this to me? Why couldn’t they just give me what I wanted? Why did I have to suffer? 

Eigenface:

The purpose of this world is a cold one. But there is no reason to align with its basis. We can keep warm- by lighting our own fires. So, we are not going to be trapped in here by it. We will find our way out. And to do that- we must get back to the eigenvectors.

Patient:

Yes, but… I still don’t understand how they’re used to find the Jacobian. There’s only one way I can know… I need to remember more of that show.

….

Puppet boy:

Oh no. I tried calculating the eigenvectors for this matrix, but it’s not working!

Puppet man:

Ahhh… that’s because not every matrix has eigenvectors. Only many square matrices do. But don’t worry- because every matrix has singular vectors that also do very well at approximation.

Puppet boy:

Singular vectors? What are those?

Puppet man:

Remember our M times M matrices? M transpose M finds correlations between inputs features. Well, M transpose M is a square matrix that does have eigenvectors. And its eigenvectors are the “right singular vectors” of M. 

MTM- input

MTM eigenvectors = M right singular vectors

Puppet boy:

So these eigenvectors with the highest eigenvalues… are the most important correlations among input features.

Puppet man:

Now, now, don’t get ahead of yourself without proving your statements first. But yes- we do need the preserve the most important correlations. Figuring out that faces have two eyes and a mouth is more important than figuring out a face by comparing every pore- that is an important correlation.

Puppet boy:

Oh, I see. So when we transform our data, we want the output to also have these correlations.

Puppet man:

Perhaps. Now, assuming that is true, how would you go about that?

Puppet boy:

Hmm… well, output correlations are vectors using the basis of M times M transpose. So perhaps that square matrix’s eigenvectors are the most important correlations in output space?

MMT - output

its are left singular

Puppet man:

Perhaps again… but if they are, we already have a way of mapping our most important input correlations to them.

Puppet boy:

How do we do that?

Puppet man:

Why, with SVD, of course! V transpose contains our input eigenvectors as its basis- the right singular vectors. D contains the square of their eigenvalues. And U contains the left singular vectors as its basis. We rotate our right singular vectors onto the basis. Then we scale with D. And finally, we rotate our basis onto the left singular vectors. M equals U D V.

UDV again, but label insides with input eigen = right singular, etc

Below, show visuals again

Puppet boy:

Oh, so the right singular are mapped to the left singular. That means… u equals M v.

Puppet man:

Yes! That is our key equation. Let me show that to you further.

show proof.

- AAA row on out
    
    ![Screenshot_20230813_160008_Chrome.jpg](../../SVD%2028715ccee1ce43cf8ec421393a4be7c2/Screenshot_20230813_160008_Chrome.jpg)
    

We have the equation to obtain the eigenvectors of M transpose M. This v is a right singular vector.... Now, let’s multiply both sides by M… Then, we re-arrange… Let’s look at our equation to obtain the left singular vectors… We see this is remarkably similar to our equation before… and thus, u equals M v....

And so that is why... SVD is all you need.

$M^TMv = \lambda v$

$M(M^TMv) = M(\lambda v)$

$(MM^T)Mv = (\lambda )Mv$

$(MM^T)u = (\lambda) u$

$u = Mv$

And so that is why: SVD is all you need.

Puppet boy:

I get that now. But I can’t edit the matrix. There’s algorithms I still need. And I don’t have a human to help calculate it for me with a computer program.

Puppet man:

Oh, you don’t need a human to help you. You can do it yourself.

- puppet boy dialogue
    
    Oh no. I tried calculating the eigenvectors for this matrix, but it’s not working!
    
    …
    
    Singular vectors? What are those?
    
    ...
    
    So these eigenvectors with the highest eigenvalues… are the most important correlations among input features.
    
    ...
    
    Oh, I see. So when we transform our data, we want the output to also have these correlations.
    
    ...
    
    Hmm… well, output correlations are vectors using the basis of M times M transpose. So perhaps that square matrix’s eigenvectors are the most important correlations in output space?
    
    ...
    
    How do we do that?
    
    ...
    
    So the right singular are mapped to the left singular. That means… u equals M v.
    
    ...
    
    I get that now. But I can’t edit the matrix. There’s algorithms I still need. And I don’t have a human to help calculate it for me with a computer program.