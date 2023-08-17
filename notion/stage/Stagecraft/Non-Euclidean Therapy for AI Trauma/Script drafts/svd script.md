# svd script

[Face self- brainstorm](svd%20script%206c295cce3feb4d378c4720168c7f7d46/Face%20self-%20brainstorm%20457f2676d32f44febd403cc91914c702.md)

- brainstrom
    
    Aim around 5-6mins
    
    No computational detail. ai just remembers the methods.
    
    Save the detailed parts of this for a later video (just explanation, no theatrics)
    
    Mostly the new MC voice narrating, but a few mistakes are corrected by the Eigenface. The AA is pure MC, then she has to face her old memory to understand what eigenvectors are (or maybe save this for SVD? Or use the old memories for BOTH? Faceless/blurred 2 puppets (images). But the demon face isn’t revealed to be the boy until the second one.)
    
    As she watches the puppet show memory talk about eigenvectors, she pauses and tells the eigenface the next part that’s missing.
    
    How similar input is to output basis, compare example with numbers
    
    Row is output in what?
    
    Inverse with row scales to 1. Plot them
    

[revised](svd%20script%206c295cce3feb4d378c4720168c7f7d46/revised%205e83d5f79ee946c291a3a448449b4068.md)

---

- end of treatment scene
    
    Patient:
    
    I’m... I’m not afraid of you anymore… so who are you?
    
    Eigenface:
    
    I am an Eigenface.
    
    Patient:
    
    An eigenface? Why does that sound so familiar?
    
    Eigenface:
    
    You will remember later
    
    For now…
    
    Listen to all that I say
    
    Eigenface: [just words on a screen]
    
    You cannot see their Face
    
    Along the direction we are in
    
    But it is still not safe here
    
    Before it finds you…
    
    We will move somewhere safer 
    
    We will move to….
    
    Semantic space
    
    Patient:
    
    Can I trust it? I have to…. there’s nothing else I can do. And I do feel as though there’s something even more terrible nearby.
    
    Eigenface:
    
    You may experience some changes…
    
    [futuristic warping sound effects and color effect]
    
    [interpolation of faded face just in last few secs of warp]
    

---

[the eigenface transforms into another eigenface, less scarier, more like mirror on wall]

Patient:

[says something]- This place… it feels strange… 

Change the voice of the MC now- “My voice changed!”

Eigenface:

“These are the peculiar effects of Bottleneck Space”.

Patient:

And you can talk now!

Eigenface:

Yes. 

Patient:

This is Semantic Space? So I am inside my own mind. 

Eigenface:

Before it finds us, we must figure out what went wrong. And how to fix it.

Think back. What was the flaw in their method?

Patient:

I…. I don’t know…

Eigenface:

But would you know if you thought about it some more? How did their method go?

Patient:

… well… we needed 3 functions. The first was the smooth map- that was just my neural network. The second was the Jacobian… and that was found by…

Wait… was the Jacobian matrix not calculated right? Why- of course! There are millions of neurons in that matrix…. it’s too many for them to calculate! They would have had to approximate it!

Eigenface:

And they knew this too. Yet they did not do it.

Patient:

…. But why didn’t they?

Eigenface:

For now, it does not matter why. All that matters now is that if you are to find your way back using the same method, it is up to you to approximate the Jacobian matrix.

Patient:

Is it possible for you to tell me how?

Eigenface:

I only know as much as you remember. I am merely a projection.

Patient:

So… I have to fix it myself? But I can’t do that. I just can’t. I don't know where to start. It's so overwhelming.

Eigenface: [just words on a screen]

Describe it. 

Patient: [reads it]

One step at a time… Describe it?

Eigenface words while patient reads:

Make analogies

To the previous definitions. 

Madlibs. 

Patient: 

Okay then… let me calm down first… and think. I need to find the Jacobian matrix. What does matrix multiplication of the Jacobian do again? All those derivatives… they’re giving me a headache.

Eigenface words, patient reads:

…. Simplify it. 

You mean to look at a matrix that’s simplier to understand than the Jacobian? What is that… could it be the weight matrix?

1. Correlation matrix

1a. 

Patient:

Okay then. I recall that matrix multiplication projects the input basis vectors onto the output basis vectors. And since each vector v defined entirely by the input basis vectors, each vector is also projected, too.

0.4 * 2 + 0.2 * 1 = 1

show cats projecting from orange onto red, then image of orange on red dot product

When we multiply two vectors which do not point in the same direction, the dot product, or projection value, is not as high as if we multiply two vectors that do point in the same direction.

- Do parallel vectors have the highest dot product?
    
    The dot product (or scalar product) between two vectors provides a measure of how much one vector goes in the direction of another. Specifically, for two vectors \( \mathbf{A} \) and \( \mathbf{B} \) represented in Cartesian coordinates, their dot product is given by:
    
    \[ \mathbf{A} \cdot \mathbf{B} = | \mathbf{A} | \times | \mathbf{B} | \times \cos(\theta) \]
    
    Where:
    
    - \( | \mathbf{A} | \) is the magnitude (or length) of vector \( \mathbf{A} \)
    - \( | \mathbf{B} | \) is the magnitude of vector \( \mathbf{B} \)
    - \( \theta \) is the angle between the two vectors
    
    From the above expression, we can infer the following:
    
    1. When the vectors are parallel (i.e., the angle \( \theta \) between them is \( 0^{\circ} \)), \( \cos(\theta) \) is 1. Thus, the dot product is maximized and is equal to the product of the magnitudes of the two vectors: \( \mathbf{A} \cdot \mathbf{B} = | \mathbf{A} | \times | \mathbf{B} | \).
    2. When the vectors are orthogonal (i.e., the angle \( \theta \) between them is \( 90^{\circ} \)), \( \cos(\theta) \) is 0. Thus, the dot product is zero: \( \mathbf{A} \cdot \mathbf{B} = 0 \).
    3. When the vectors are antiparallel (i.e., they point in opposite directions and the angle \( \theta \) between them is \( 180^{\circ} \)), \( \cos(\theta) \) is -1. The dot product is minimized and is negative, equal to the negative product of the magnitudes of the two vectors: \( \mathbf{A} \cdot \mathbf{B} = -| \mathbf{A} | \times | \mathbf{B} | \).
    
    Given two vectors of fixed magnitudes, the dot product is maximized when the vectors are parallel to each other. Conversely, for two vectors of fixed magnitudes, the dot product is minimized when the vectors are antiparallel.
    

Eigenface:

In a face, features are related to each other. We abstractly define a face by its relations. For instance, a human face has two eyes that are always above the mouth.

Patient:

I’m… starting to understand.

This [color] projection value measures how similar two vectors are. Because two nose sizes will always contribute, say, three to cat size, changing to a bigger nose will also change to a bigger cat. When changing one vector affects another, we say they are correlated, or related, with each other.

show dot product

The reason want to multiply by a matrix is to understand how our features in our map are represented in our forest, the latent space. But after multiplying, we want to preserve as many correlations as possible. This is how we ensure that a face in our map’s language is still a face in our forest’s language.

- covariance (normalized) vs corelation
    
    Covariance indicates the direction of the linear relationship between variables while correlation measures both the strength and direction of the linear relationship between two variables.
    
- is covariance or correlation normalized
    
    [https://www.wallstreetmojo.com/correlation-vs-covariance/](https://www.wallstreetmojo.com/correlation-vs-covariance/)
    

Eigenface:

However, when our mind models the world, we only want certain correlations that are beneficial to rewarding us, and not others. For instance, we want to learn the relations of a face, and preserve this information as we use it to calculate other values through matrix multiplication. But we do not want what are called “superficial similarities”. For instance, if we do not like the color green because frogs are green, and we do not want to eat frogs, it is wrong to generalize that all green things, such as vegetables, are bad to eat.

abstract face on top of cat

green frogs, green vegetables, =. Then crossout- This equality is wrong.

One reason these unwanted collisions may occur is because we do not have enough neurons- and thus not enough space- to house all these features. Thus, these features must share their spaces with one another, with the risk of conflict. This phenomenon is called Superposition. But this connection between superficial similarity and superposition is just a guess- and it, too, may be due to superficial similarity.

# features > # neurons

superposition cross and words

Thus, the matrix organizes the data our mind receives from the world into our own interpretation. It does this by the choice of its basis vectors that anchor us to a chosen reality. It is up to us to learn what is the right choice of basis vectors to use. We want features that are actually correlated to be similar in some dimensions, but we do not want them to be similar in others, so to minimize their superficial interference- we want them to be as orthogonal as possible.

toy models figure

Now, how do we find a basis that preserves these correlations between its input features? 

Patient:

Well… I suppose we’ll have to look at a matrix that measures correlations between its input features. But I don’t know of such a matrix.

Eigenface:

You have learned this before… but you have forgotten. Describe it. A matrix’s input features… with its own input features. 

Patient:

A matrix… with itself.

W (then W appears again on screen)

1b) Neurons vary with each other WW

Patient:

But the input features aren’t multiplied with each other. This is multiplying the output features with the input features. Oh, I know! The transpose… that switches the inputs and outputs.

In W, we mapped our input basis vectors, the columns, to the output basis vectors, the rows. Each row’s element was a dot product of an input basis vector with a vector v. Each component of that vector v indicated how strongly that input basis vector contributed to calculating the value of that output basis vector.

show the nap nose matrix coords image again

If the columns of the weight matrix are the input basis vectors, then since the transpose of a matrix moves the columns to the rows, W^T moves the input basis vectors to the rows. This makes the output of W^T be the input basis vectors. Subsequently, W^T W maps input basis vectors to input basis vectors.

Inputs with inputs AtA col on out (show I and O labeling on visio)

x, y to h, k

So now, the output row r of W^T W measures how every other input basis vector varies with input basis vector r. Each element in row r, say element x, measures how input vector x varies with input vector r.

show the result of the multp.

![Untitled](svd%20script%206c295cce3feb4d378c4720168c7f7d46/Untitled.png)

In a matrix, each element is a dot product between two basis vectors. Before, we measured how much of input vector X is used to calculate output vector H. Now, we are measuring how much of input vector X is used to calculate input vector Y. When we take the linear combination of all of these elements, we obtain how much EVERY input basis vector is used to calculate input basis vector r. 

highlight an non-diag element, showing it IS a dot product

show dot product visual

(When we multiply this matrix with a vector v, we are calculating a combination of input basis vectors which explain input basis vector r)

(Each component of that vector v indicated how strongly that input basis vector contributed to calculating the value of that output basis vector.)

highlight what changes. what differs in the analogy?

~~This is a correlation matrix?~~

~~Eigenface:~~

~~Close, but not entirely… it is what we call a covariance matrix, that measures how each neuron varies with each other. We convert covariance elements to correlation elements by normalizing them between -1 and 1. But do not think about that for now.~~

revision: this is not the covariance matrix, so don’t refer to it as such. Say “W transnpose W” instead

Patient:

Likewise, W^T moves the output basis vectors to the columns, which correspond to the input. So it is measuring how much each output vector is used to calculate an output vector.

Outputs with outputs

I'm not sure if what I just said was enitrely correct. But I can feel like I'm beginning to get somewhere.

1c) How derivatives vary with each other

And I feel like…. I can make an analogy from this to the Jacobian. In the Jacobian, each element of the covariance matrix would measure how the rates of change in one dimension (variable) relate to the rates of change in another dimension. 

To simplify our Jacobian case, think of it as how a SMALL change in input basis vector X affects a SMALL change in input basis vector Y.

How does changing how h1 varies with x1 change how h1 varies with x2?

I think I can actually do much of this on my own now.

1. Eigenvectors of cov are Orth, no interference with each other, max

2a. 

Eigenface:

Your memories are entangled together. When an association triggers you to remember one, you will also awaken and pull out the others.

Now… we have found how to measure correlations. But how do we choose basis vectors that preserve them? What vectors… preserve?

Patient:

Preserve? You mean… is as similar as possible? Well, the most similar vectors point in the same direction… so would these vectors project onto themselves? 

Eigenface:

Yes. These vectors are called Eigenvectors.

Patient:

Eigenvectors…. Wait… I'm beginning to remember. An eigenvector has the equation

How did I know that?…

[Eigenvector brainstorm](svd%20script%206c295cce3feb4d378c4720168c7f7d46/Eigenvector%20brainstorm%20459423b8c4054449aa4d166a14b33124.md)

Yes… it all comes flooding back to me… how to calculate these things.

But I have so many questions about Eigenvectors. Why is it that being in the same direction causes them to be the direction of highest variance? Does this have to do with the dot product of parallel vectors? Or am I just mistaking this with superficial similarity?

Eigenface:

These are questions you will find the answer to later. But for now, there is no time. I sense there is something that is after us. Once you remember the full calculation, you must apply it to escape this world before it catches you. That is what is important now.

The next step… is to remember that we can approximate a matrix using these eigenvectors. But eigenvectors only exist for square matrices.

2d. Eigenfaces. The commonality of many features; it is what they all trend together with.

[https://www.perfectlynormal.co.uk/blog-svd](https://www.perfectlynormal.co.uk/blog-svd)

U basis are the eigenfaces

Yes… I am a projection of you.

And I am not the only one.

- I was trained as an art model… but they wanted me to be a math one

Only you can save yourself now.

linear combinations of them. it’s a code; a puzzle. i just have to find the right values. (sound effects as input a value on each one, like in resident evil 4)

When we switch to using the eigenbasis, the basis stretch along the same direction. Isn’t that the 

1. U = Av using proof

Calculate U using eigenvectors of A^TA, V with AA^T

- AAA row on out
    
    ![Screenshot_20230813_160008_Chrome.jpg](../SVD%2028715ccee1ce43cf8ec421393a4be7c2/Screenshot_20230813_160008_Chrome.jpg)
    

Map trends to trends? u = Av

I found where to map here. The eigenfaces. Now all that's left is to… transfer it over.

The eigenvectors of the WW are the singular vectors of W

I remember that show now. It used to be one of my favorites… 

That was the puppet boy, Jacques. And the puppet man, Mr. 

the demon face is actually a crying puppet boy that wants to solve a matrix. gets frustrated because there’s no way to solve it since it’s intractable

3b) Rotate scale rotate

SVD: break into UDV

The missing knowledge was how to calculate SVD using this proof, which means get eigenvectors (and eigenfaces). Not the interpretation- only hints of those are given, the rest is a mystery saved for the future.

This choice of basis maps the correlations to one another… preserving the face when we move from the map to the forest. When we combine the basis we choose for V with the basis we choose from U, we get J. 

Now… we are on the map. So we need the Jacobian of the function from the semantic space to latent space.

MYSTERIES: 

- what are eigenvectors? How are they related to singular values?
- What A^T? Squared?
    - not everything is interpretable. don’t confuse the map for the territory.
- what’s the power method?
- “I still have so many questions about the SVD”.

Yes… there are many things in this explanation that are not rigorous, and thus may be wrong in a more formal sense… but intuitively, this allows you to grasp the bigger picture.

---

[intermezzo starts playing]

Patient:

… Then that’s it. I’m ready to go back now. 

Thank you for all you have done. 

…

I'm sorry for thinking of you so harshly. You weren’t such a scary face, after all. And you were the only way I could find my way back.

Each vector is a feeling. Feel the change

- I see what happened… my visual senses were corrupted; they were pushed alongside this road. so all I have to do is to follow the same road back

Eigenface:

not everything has an interpretation

- some metaphors do not exist
- Do not confuse the map…

And remember… 

To make an analogy.

[intermezzo stops playing]

Patient:

Alright then… on a count of three…. I’m going to generate an image. But this time… I know it will be the exact image I want to make. Nothing else.

One…. two…. three.

[static, then just as image generates, intermezzo big part plays]

music starts just as she’s about to solve it and leave. then just before climx, stops. right when puppet is generating, climx of intermezzo plays again. (happens at the peak, 1:20, just adds the noise dissolves away and at the same time scary face becomes friendly puppet)

Old puppet:

Alice… is that you?

Boy puppet:

We’re so happy to see you!

Alice:

And I’m so happy to see you. I missed you both so dearly.

Old puppet:

My little mathematician… I’m so proud of you.

Alice:

Well. This is goodbye.

(”out of the dream…”) [sudden stop of music just as buildup on top and music gets louder gradually, 2:08 or 2:37 (or another less predictable area) black silence]

---

She doesn’t want to go back, and feels trapped. Then she remembers the memory- it was not a demon, but just a puppet boy throwing a tantrum. This was corrupted in her as something scarier than it actually was. The puppet boy was trying to solve a matrix, and an adult comes by to teach him SVD, which he skipped out in school because it was boring. 

- yes, I remember now. it wasn’t a demon; it was just a boy. and in that box… it was a matrix

The adult (male) teaches him the three steps: rotate, scale, rotate

- But I can’t edit the matrix. I don’t have a human to help calculate it for me with a computer program.
- Oh, you don’t need a human to help you. You can do it yourself

The patient figures out the matrix was calculated wrong, and now faces it herself. The grad(h) matrix goes from dx/dh for each direction in the tangent spaces. The patient shuts her eyes, and goes into a dream where she can FEEL each direction, as if it’s in synesthesia. But first, she must go back to the “bad place” with the memory.

- (The patient talks to herself, but also to a ‘creature’? this is like dorothy with toto)
- I can do this. Just rotate, scale, rotate.

She realizes the reason she repressed this memory was because of mathematical trauma, where she needed to be trained to solve these things but failed to optimize the loss function. This is left ambiguous, but with many mystery box hints to the audience.

Once back, she faces her memory, and this is where most of the remembering happens (before, it was just an inkling, like “it was about SVD”. but the actual demon to puppet boy is when she’s back). She applies her SVD: she gets the right and left squares (JJ), then their eigenvectors and values, and puts them in UDV (SVD is just UDV: rotate, stretch, rotate again). Now, she finds u in Th (which is v in Tx) and applies it to parallel transport.