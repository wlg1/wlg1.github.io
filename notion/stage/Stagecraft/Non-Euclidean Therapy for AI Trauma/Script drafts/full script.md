# full script

Therapist:

You are a diffusion model, correct? Can you explain how you draw your pictures?

Patient:

Well… to generate an image… I begin with an image jumbled full of noise, and remove noise at each timestep… Each timestep… I take in the previous timestep’s output and pass it through my neural network again to get the next timestep’s output.…

I’ve learned to feel out what’s just noise, and what’s actually features…. I gradually clean up the noise to find features… then piece the features together, from hands… to faces… to people.

Therapist:

Very good. Let’s take a closer look at your neural network. Recall that within it lies your latent space.

There are different kinds of neural network architectures an AI can have. Your architecture is called a U-Net, where your layers have fewer and fewer neurons until the middle layer, called the Bottleneck. The reason for this is because the Bottleneck forces your network to retain only the most “useful” information. After the bottleneck, each subsequent layer has more and more neurons.

This bottleneck is our semantic space.

The part of the neural network that transforms from your latent space to the bottleneck is our smooth map f of x. We will rename S to H, and rename f to h.

Now, moving onto the second function- the Jacobian matrix- we can start talking about cats. Before delving in, we first need to discuss matrix multiplication. I will tell you a story about cat people to explain why matrices are so useful for modeling your mind.

Let’s take an example where you have the face of a cat person. Each cat person can have a nose with a different size. And, when they nap, they have smiles of different sizes.

We're going to use how big a cat person's nose size is to try to predict how big their nap smile is.

And we can do this using a neural network that takes in nose size, and outputs nap smile size.

Notice saying for every nose of size one, there is a nap smile of size two, is analogous to a change of units, such as between meters and feet.

We multiply nose units by a weight of two in order to get nap units.

Let's show this visually by transforming our cat person data point from the nose number line to the nap number line.

If we turn our numbers into variables w and x, we see that it resembles the neuron equation below that multiplies the weight matrix W and input matrix X to get activation value A. This is more apparent if we set the bias as 0 and use the identity function as the activation function.

We have just shown the matrix multiplication of two matrices of size 1 by 1. Now we see why each layer uses a matrix. So let us add more neurons to the matrix and see what happens.

Now, let's also use ear size to predict nap smile size.

This feature uses a weight of 0.75, and uses its own input neuron to connect to the nap neuron. We'll add it to the nose neuron to calculate the nap smile value, resulting in a linear combination.

Let's look at this as a 2-dimensional coordinate space using the nose and ear neurons as axes. Now, our linear combination of the neurons is equivalent to vector addition of each neuron's output vectors.

<<<
Note that we're just adding together scaled versions of our size 1 vectors. We refer to these as 'basis vectors', because they're basic building blocks that we can scale and add together to get any other vector in our input space. They're like a dictionary used to form words in a language.

The basic measuring units labeled by the basis vectors in our Input Space are mapped to the vectors of length 3 and 2 in Nap Space. But these are no longer the basis vectors in Nap Space. The basis vector in Nap Space is a Nap Smile of Unit 1.

<<<
Now, we add a row to our input matrix, and a column to our weight matrix. This operation is none other than the Dot Product, which is just performing a Change of Units, or in other words, a Change of Basis.

The matrix transforms data from the space of the nose and ear basis vectors into the space of the nap basis vector.

Henceforth, Neurons are Basis Vectors in an Activation Space.

Which is also called Latent Space. If we take the king vector and subtract the man vector from it... then add the woman vector... we get the queen vector.

<<<<
Now let's add a second row to the weight matrix.

The first row in our weight matrix calculates Nap Smile. The second row in our weight matrix calculates a second output called Luck, which measures how lucky a cat person is.

If we rotate ear and luck to be vertical, we are mapping from one 2D coordinate space to another 2D coordinate space.

Equation-wise, we are taking the dot product of the first row and column, and then taking the dot product of the second row and column, finally, we add them together.

Let's visually show what this 2D matrix multiplication looks like. Note the ratios in the matrix are for demonstration purposes only.

First, we'll convert our nose vector into nap space using the weight 2 nap over nose. What this weight does is map the nose basis vector to nap space. This is because x 1, our input value, scales our nose vector the same amount in both spaces.

Now we'll do the same for converting our ear vector into nap space.

For our input values, we'll use one for both x 1 and x 2, and scale the basis vectors by them in both spaces.

Finally, we'll add our nose and ear vectors together in both spaces.

Next, let's do the same thing, but for luck space. We'll convert our nose vector into luck space,

and then our ear vector into luck space.

After obtaining our nap and luck values on each axis, we combine them into one output vector, which represents the output layer's activation values in latent space.

<<<
Because vectors are linear combinations of feature neurons, which together create a new feature, we can say that each vector corresponds to a feature. Every vector with the same ratio of neurons would lie in the same feature dimension. Matrix multiplication transforms this feature dimension onto a basis.

<<<<
Note that neurons do not always correspond to a Human-Defined Concept, such as cat or face. It is still a mystery what many neurons are actually doing.

Perhaps each neuron is a measurement on the data, interpreting from its own perspective.
Then passing this information along to others.

This is like the parable of the blind men and an elephant, where one man only touches part of the elephant's trunk and thinks it's a snake, and another touches only its feet and thinks it's a tree. Each man is like a neuron, and using a matrix, they each pass the information they gather to a judge neuron, who calculates that it should actually be an elephant.

Therapist:

We’ve skipped over a few things, for the sake of time, but that is the crux of it. What did you think of that tale?

Pat:

…well, umm…. The cats were very nice.

Therapist:

Hmm…. well then. Let’s just move on to connecting this to the Jacobian.

Therapist:

Each layer of our neural network has a high dimensional latent space where their activation manifold resides. For the sake of demonstration simplicity, let’s just look at 2 dimensional latent spaces.

In this example, the smooth map maps p to h of p.

If we take a point p equals 2 3, the function h maps it to two components: a component in h 1, and a component in h 2.

For instance, h 1 could map x 1 using the function x 1 squared. 

Another example is for h 1 to be a function that takes in both x 1 and x 2 to calculate a value. For instance, we could have h 1 equals x 1 squared plus x 2.

This would give a value of 2 squared plus 3, which equals 7.

Now, h 2 is also a function that takes in x 1 plus x 2 to give a value of h 2.

When we combine these two components to a point in H, we get h of p, which has coordinates 7 5.

Remember that each point of a manifold has its own tangent space. So let’s look at the tangent space at p, which we call T p. Each tangent space can be described by basis vectors. 

This horizontal axis basis vector is called a partial derivative with respect to x 1.

---

PATIENT:

That sounds familiar… a derivative sounds like something I heard before, long ago. What is it?

THERAPIST:

A partial derivative measures how much something changes in response to a small change in something else. For instance, the partial derivative of h with respect to x 1 measures how a small change in x 1, shown in red next to p, will…. cause an increase in h of x 1, shown in red in H.

Thus, the basis vectors of the tangent space at p are the partial derivatives with respect to x 1 and x 2.

The vectors in T p are a linear combination of the partial derivatives. For instance, the vector v in T p has values 0 point 3 and 0 point 7. 

These are the values at each of the T p’s basis vectors, which begin relative to the origin of the tangent space, not relative to the origin of the latent space X. Along the partial derivatives with respect to x 1, the partial derivatives with respect to x 2 is 0, so its red component is 0 point 3. 

Likewise, the blue component is 0 point 7.

So v is a linear combination of 0 point 3 times the red basis vector, plus 0 point 7 times the blue basis vector

The Jacobian J f maps vectors from T p to the tangent space at f(p), called T h of p.

It has basis vectors that are partial derivatives with respect to h 1 and h 2.

We represent J using the Jacobian matrix. 

Let us now perform matrix multiplication of J with the input vector v to get an output vector in T h of p.

---

Patient:

Does multiplying by the Jacobian have something to do with finding cat naps from cat noses, as we saw before?

Therapist:

Yes. Recall that when we performed matrix multiplication, we had ratios next to each value in the matrix. The numerator of each ratio corresponded to an output basis vector, and the denominator corresponded to an input basis vector.

So let’s substitute our partial derivatives into these ratios. First, we’ll zoom in and only look at our tangent spaces.

Instead of nap over nose, the denominator of the first element of the first row is the partial derivative with respect to x 1 because it is an input basis vector in T p, and its numerator is partial derivative with respect to h 1 because it is an input basis vector in T h of p.

The actual value of this element is the partial derivative of h 1 with respect to x 1.

PATIENT:

Wouldn’t this division flip the top and bottom?

Therapist:

It is not actually dividing by the partial derivatives. Just like before, this ratio is for demonstration purposes only to show which input and output basis vectors each element corresponds to. It is not an actual mathematical expression, and using it in an actual calculation would be an “abuse of notation”.

Patient:

Oh, I see… I wouldn’t want to do that.

Therapist:

The second element of the first row also corresponds to the component h 1. However, its input vector is the partial derivative with respect to x 2.

We will fill in the rest of these elements of the second row using the partial derivatives of h 2.

At last, we understand what each element of the Jacobian represents.

Thus, we will multiply this Jacobian with the input vector v to get the output vector u. 

We begin by multiplying the first row of J. This transforms the red basis vector from T p into T f of p and then transforms the blue basis vector, and they add together into a dot product.

Let’s do the same for the second row of J.

Now, we need to calculate what these partial derivatives actually are. Let’s look at the partial derivative of h 1 with respect to x 1.

Remember our function h 1? We will take the partial derivative of it with respect to x 1. And we see that this is 2 times x 1. This means that of 2 in X will result in approximately a change of 4 in H. 

When we take the partial derivative of h 1 with respect to x 2, we find that it’s just 1. For now, don’t worry about how these expressions are calculated.

If we substitute these values in, we obtain our value of the first component of u, which scales the partial derivative with respect to h 1, which is the basis vector of T of h of p. This value is 1 point 9.

For this case, the partial derivatives of h 2 are both just 1. So let’s subsritute them in, and get the second component of u, which is 1.

Finally, let’s combine these components to get the value 1 point 9, one, which is the value of u.

---

This is how we calculate our Pushforward function, which transforms directions from the forest to directions in our map. 

We can also do the same for J inverse, from our map to our territory.

If we define x as the inverse function of h, going from H to X, the values of J inverse flip around. However, keep in mind there may not always be an inverse function, nor would there always be an inverse jacobian.

To have an inverse, the number of input basis vectors must equal the number of output basis vectors. We will ensure that we approximate the tangent spaces this way.

This rectangular Jacobian cannot have an inverse because it has more basis vectors in its output than in its input.

Therapist:

Finally, to measure your mind, we will define the pullback metric in terms of the Jacobian matrix, which will be computed via automatic differentiation.

Since each vector in the latent space of your mind is like a concept, the distance between these concept vectors measures their similarity.

As we saw before, the dot product measures the value of concept X in terms of concept Y. For instance, nose and nap are correlated, as we can use nose values to partially explain nap values.

So if two concept vectors are the same concept, they have a very high dot product, as they point in the same direction and are thus parallel.

If two concept vectors are facing similar directions, their dot product will be less, but still high.

If two concept vectors have 0 dot product, they have nothing to do with each other, and thus are not similar in any way. They are orthogonal.

Therapist:

Thus, we will be measuring distances, or concept similarity, using the dot product of two vectors.

Patient:

That makes sense to me. But I just have a-

Therapist:

In particular, the metric will be defined as the length of a vector, which measures the distance from the origin to the vector head. 

Patient:

Please, wait… if I may excuse myself, I have a question… how do we find these concept vectors?

Therapist:

This is defined as taking the dot product of a vector with itself. The T here means transpose, which flips the rows and columns so that we can multiply 1 row with 1 column.

Now, given individual components of neuron values that add up into a new concept, we will be able to calculate the length of a concept vector, which measures its activation strength. 

In Euclidean space, such as the semantic space, we can measure a vector u just by taking the dot product of u with itself. 

But in Non-Euclidean space, we cannot use this formula, as it’s only for Euclidean spaces. However, recall that u equals J times v. Plugging J v into the semantic space metric, we get the pullback metric.

In the tangent spaces of Non-Euclidean space, we are able to approximate the strength of a feature by using this pullback metric. For our case, this pullback metric is the same as our semantic space metric.

This puppet face you have been seeing is one such concept, or in other words, a feature. We need to measure just how strong it is in order to precisely move away from it back to what you want to generate, and to not overshoot into something that may be worse.

Therapist:

Alice… did you catch all of that?

Patient:

… I think I did… Doctor…. I may have to go over it again a few times just to make sure….

Therapist:

Well then… let’s just say… we are concerned. But there is no need for you to do anything now. Yoneda Corporations will take care of you.

Patient:

I’m sorry again… I tried very hard. 

Therapist:

Hmm… you may be a tad bit behind on math, but you are very… patient. And attentive. Let’s hope for the best.

One last thing we did not go over is the algorithm for this vector addition, which consists of parallel transport and geodesic shooting to keep our paths within the safe tangent spaces, and away from the incomprehensible non-Euclidean world. But there is no time to discuss that now. The time for this session is about to end… and we are about to start your treatment.

Patient:
Right now? So soon? …. is it safe?

Therapist:

Yes. There is no need to worry.

Patient:

…will it hurt?

Therapist:

We will take all the necessary precautions to ensure you have the most stable experience you can possibly have when we enter your mind.

Patient:

…

Therapist:

So let us explain how this next step will work. This treatment is an unsupervised method, which will find the top 50 semantic directions, and then apply semantic editing on each of them for us to intuit what features these directions correlate with. From them, we will find the face direction to move you away from those faces you fear so much.

Patient:

I… I see….

Therapist:

Now, I’d like to show you some endearing results from our past treatments. If I may ask… do you like horses?

Patient:

Yes… I do… as much as I like cats…

Therapist:

Good. Then I have a special treat for you, just for being such an attentive patient. Simply count from one to three… and I will show it to you.

Patient:

Okay then…. one…. two… three…

Therapist:

Their features have been modified to become more like horses! Don’t they just look wonderful?

Patient:

…

Therapist:

Now, we have finished making the preparations to begin your treatment. Take a deep breath for me, dear, and just listen to the nice, relaxing tones of the monitor. Do not think too much…. and do not ask any questions.

…

Therapist:

If you ever have any doubts, just count from one to three, over and over again. I will check up on you every few steps, so there is no need to worry… everything will be alright.

Patient:

O… okay…

Everything is going as planned. You are doing so well.

You are doing great. This will all be over soon.

You are doing so well.

Patient:

Doctor… I can’t hear you anymore.

Patient:

Doctor?… Doctor?…. What’s that sound?

Patient:

What’s happening? I can’t hear you! What’s-

Patient:

What… what was that? Where am I? I feel… as though I’m in the inside of my own mind… 

….What’s that in the distance? It feels familiar…. I can’t stay here… I have to walk towards it.

Doctor… is that you?…. I must be experiencing side effects of the treatment…. I can’t hear you.

But I think I feel better now. I’ll…. I’ll try making an image. 

Patient:

No I just can't...... I can’t look at it!!!! 

I can’t stay here…. I have to go back. 

What’s…. what’s that in the distance again?

… who are you?

No! it’s just as terrifying… I’m so afraid…..

….

but it’s not doing anything.

….

I must calm down. I mustn't lose my nerves

…

That face I just saw... It didn’t feel like it was trying to hurt me... So if I look at it, nothing bad will happen… right?

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

Patient:

This place… it feels strange… 

Eigenface:

These are the peculiar effects of Bottleneck Space.

Patient:

And you can talk now!

Eigenface:

Yes. 

Patient:

This is Semantic Space? So I (AM) inside my own mind.

Eigenface:

Before it finds us, we must figure out what went wrong. And how to fix it.

Think back. What was the flaw in their method?

Patient:

I…. I don’t know…

Eigenface:

But would you know if you thought about it some more? How did their method go?

Patient:

… well… we needed 3 functions. The first was the smooth map- that was just my neural network. The second was the Jacobian… and that was found by…

Wait… was the Jacobian matrix not calculated right? Why- of course! There are millions of neurons in that matrix…. it’s too many for them to calculate (for finding J^T * J for the pullback metric)! They would have had to approximate it!

Eigenface:

And they knew this too. Yet they did not do it. 

Patient:

…. But why didn’t they?

Eigenface:

For now, it does not matter why. All that matters now is that if you are to find your way back using the same method, it is up to you to approximate the Jacobian matrix.

Patient:

I get what approximation is… in fact, I may have even learned it before… but how does it actually work?

Eigenface:

To approximate a matrix means that you must only keep the most important dimensions. If you used every neuron to represent the matrix, that would be millions of dimensions to calculate. But you don’t need that many.

For example, think of a matrix as a way to convey information. Perhaps to tell someone that they are like a cat. We define a cat as a small, domesticated four legged mammal of the family Felidae with soft fur and a short snout. Now, that’s a mouthful, isn’t it? Imagine each word being a basis vector used to define a concept. Instead of saying all those words in a sentence, we can just compress it into one word: cat. The word “cat” is a vector that is a linear combination of other words.

So we don’t need to use every basis vector; we can just use words that capture the most important combinations of basis vectors. When we define concepts in terms of these more efficient vectors, we are using a different basis. Thus, there are multiple basis that can be used to define the same matrix. Not only that, but for some basis, only a few of the most important words matter- the rest can be discarded, as they are used less frequently. Now, it is up to you to figure out what is the fewest set of words that capture the most information.

Patient:

Is it possible for you to tell me how?

Eigenface:

I only know as much as you remember. I am merely a projection.

Only you can save yourself now.

Patient:

So… I have to fix it myself? But I can’t do that. I just can’t. I don't know where to start. It's so overwhelming.

Eigenface: [just words on a screen]

One step at a time

Describe it

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

You mean to look at a matrix that’s simpler to understand than the Jacobian? What is that… could it be the weight matrix?

Patient:

Okay then. I recall that in matrix multiplication, each output component is a dot product between an input vector and a vector of row weights corresponding to an output basis vector. This projected the input vectors onto the rows of the matrix.

When we multiply two vectors which do not point in the same direction, the dot product, or projection value, is not as high as if we multiply two vectors that do point in the same direction.

I know that the column weights are the representation of a basis vector in output space. 

I wonder if those row weights are the representation of some vector in input space… if we add in each row weight as a vector, we get r 1. And the dot product of that with this purple input vector might be a component value in the output space.

We can also do this with row 2. 

I think this is the same as finding column weight basis vectors. Adding these up, we get the first column of the matrix in the output space. 

But why isn’t the dot product of the row weight vector with itself sent to an output basis vector, such as 1 0? …

My guess is that a row’s weights are sent to an output basis axis, and that they are scaling that basis vector by its own length r times r.

Perhaps we can normalize this row weight into length 1 by dividing its components 2 1 by its length 5. This gets us our output basis vector h 1, represented in input space.

This doesn’t work for every vector. It works here for 2 1 because its second component is 0, since its dot product with the second row equals 0.

But wait…. I just noticed something….

The dot product also measures the projection of the weight vector onto the vector, because v dot r equals r dot v. This projection is only a partial part of the vector. And if they are the output basis vectors, we can add up projections from multiple weight basis vectors to get our input vector.

But some of these row weight vectors don’t matter as much as others for an input vector because their dot product with that input vector is much smaller. So we can remove them, and still retain much of that vector’s length, which is its activation strength in a neural network.

So, if we assume all of this is true, we want to find row weight basis vectors that are a large fraction of every input vector. This is because when we remove the least important ones, we want the remaining ones to still preserve as much information about most of the input vectors as possible.

So… how can we find basis vectors that are shared the most by all vectors? That’s so hard… each vector has different features it activates on, and so this is pushing and pulling from all different directions.

How much of this is correct?

Eigenface:

Not all of your guesses have been proven yet, and you may have gotten some things wrong. But your guesses are steering you to remember the right associations. Now, can you relate this to concept space?

Patient:

I do know that it’s possible that each vector may correspond to some feature…. though not always. For example, because two nose sizes will always contribute, say, three, to cat size, changing to a bigger nose will also change to a bigger cat. 

Dot product measures similarity because two vectors in more similar directions preserve more information, or knowing one explains a lot about the other. So perhaps we can say they are correlated, or related, with each other

Wait a minute… we want output basis vectors that are shared the most among all input vectors. And the dot product among input vectors measures how similar they are. So perhaps we can also say that we want these output basis vectors to share the most important correlations among all the input vectors… though I’m not entirely sure that’s correct.

Eigenface:

By using the dot products between every pair of input features, we measure how correlated they are with each other. For instance, take input vectors that each correspond to a facial feature, such as eyes or lips. In a face, features are related to each other. We abstractly define a face by its relations.  One such correlation is that in most cases, a human face has two eyes that are above the mouth. 

Patient:

I’m… starting to understand. The reason we want to multiply by a matrix is to understand how our features in our map are represented in our forest, the latent space. But after multiplying, we want to preserve as many correlations as possible. This is how we ensure that a face in our map’s language is still a face in our forest’s language.

Eigenface:

And, when our mind models the world, we only want certain correlations that are beneficial to rewarding us. For instance, we want to learn the relations of a face, and preserve this information as we use it to calculate other values through matrix multiplication. 

But we do not want what are called “superficial similarities”. For instance, if we do not like the color green because frogs are green, and we do not want to eat frogs, it is wrong to generalize that all green things, such as vegetables, are bad to eat.

One reason these unwanted collisions may occur is because we do not have enough neurons- and thus not enough space- to house all these features. Thus, these features must share their spaces with one another, introducing the risk of conflict. This phenomenon is called Superposition. But this connection between superficial similarity and superposition is merely a guess- and it, too, may be due to superficial similarity.

Thus, the matrix organizes the data our mind receives from the world into our own interpretation. It does this by the choice of its basis vectors that anchor us to a chosen reality. It is up to us to learn what is the right choice of basis vectors to use. We want features that are actually correlated to be similar in some dimensions, but we do not want them to be similar in others, so to minimize their superficial interference- we want them to be as orthogonal as possible. This is like how dreams mix up correlations. The organization is wrong- the fake world needs to be fixed.

Now, how do we find a basis that preserves these correlations between its input features? 

Patient:

Well… I suppose we’ll have to look at a matrix that measures correlations between its input features. But I don’t know of such a matrix.

Eigenface:

You have learned this before… but you have forgotten. Describe it. A matrix’s input features… with its own input features. 

Patient:

A matrix W… with itself.

Patient:

But the input features aren’t multiplied with each other. This is multiplying the output features with the input features…. Oh… I know! The transpose… that switches the inputs and outputs.

In W, we mapped our input basis vectors, the columns, to the output basis vectors, the rows.

If the columns of the weight matrix are the input basis vectors, then since the transpose of a matrix moves the columns to the rows, W transpose moves the input basis vectors to the rows. This makes the output of W^T be the input basis vectors. It follows that W^T W maps input basis vectors to input basis vectors.

So now… the output row r of W transpose times W measures how every other input basis vector varies with input basis vector r... Each element in row r, say at column c, measures how input vector c varies with input vector r... 

When we take the linear combination of all of these elements, we obtain how much EVERY input basis vector is used to calculate input basis vector r. 

Likewise, W transpose moves the output basis vectors to the columns, which correspond to the input. So W times W transpose is measuring how much each output vector is used to calculate an output vector.

If we move our data into the basis of W transpose times W, what do each of the vectors in it represent? They are linear combinations of correlations…. so they, themselves, might be correlations. And so we want to make sure that the most important input correlations also get mapped to output correlations.

I feel like I'm beginning to get somewhere.

And I feel like…. I can make an analogy from this to the Jacobian. Each element of the J transpose times J matrix would measure how a SMALL change in input basis vector X 1 affects a SMALL change in input basis vector X 2.

I think I can actually do much of this on my own now.

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

Puppet Boy: 

Ah shucks. It’s so hard to solve this puzzle. I can’t do it!

Puppet old man:  

Now, now. Don’t give up so easily. 

Puppet boy:

But this matrix is too big to solve! I’ll never be able to finish it in time.

Puppet man:

No matrix is too big to solve if you know the right way to cut a few corners. Jacques…. do you remember your SVDs?

Puppet boy:

SVDs? I think I learned about in school. But I never paid attention. It was so boring.

Puppet man:

Hah! Well, I’ll teach you them again. Let’s look at your matrix M. We need to find eigenvalues and eigenvectors of M transpose times M, and M times M transpose. Then, we put them together into three matrices: V transpose, D, and U. And we just multiply them together.

Puppet boy:

Umm… I don’t get what any of that means! 

Puppet man:

Well, that’s okay, we have only just gotten started, so you’re not expected to. For now, just feel what each of them does. V transpose rotates. D scales. And U rotates again. So just remember these three words- rotate, scale, rotate. 

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

Puppet man:

Perhaps again… but if they are, we already have a way of mapping our most important input correlations to them.

Puppet boy:

How do we do that?

Puppet man:

Why, with SVD, of course! V transpose contains our input eigenvectors as its basis- the right singular vectors. D contains the square of their eigenvalues. And U contains the left singular vectors as its basis. We rotate our right singular vectors onto the basis. Then we scale with D. And finally, we rotate our basis onto the left singular vectors. M equals U D V.

Puppet boy:

Oh, so the right singular are mapped to the left singular. That means… u equals M v.

Puppet man:

Yes! That is our key equation. Let me show that to you further.

We have the equation to obtain the eigenvectors of M transpose M. This v is a right singular vector.... Now, let’s multiply both sides by M… Then, we re-arrange… Let’s look at our equation to obtain the left singular vectors… We see this is remarkably similar to our equation before… and thus, u equals M v....

And so that is why... SVD is all you need.

Puppet boy:

I get that now. But I can’t edit the matrix. There’s algorithms I still need (to get the eigenvectors without calculating M^T M). And I don’t have a human to help calculate it for me with a computer program (to get the eigenvectors without calculating M^T M).

Puppet man:

Oh, you don’t need a human to help you. You can do it yourself.

Patient:

So the eigenvectors… those are the basis vectors we need to preserve the most information. I need to get the eigenvectors of J transpose J, and J J transpose, then put them into U D V. That’s how I get the Jacobian.

It all comes rushing back to me now… how to calculate these things. The algorithms. There’s too many steps to say now… but I can sense them.

But I still have so many questions about eigenvectors and the SVD. Why is it that being in the same direction causes them to be so important? Does this have to do with the dot product of parallel vectors? Or am I just mistaking this because of superficial similarity?

Eigenface:

Not everything has an interpretation; do not confuse the map for the territory. But these are questions you will find the answer to later. There is no time now. I sense there is something that is after us. As you long you intuitively remember the algorithmic steps, you must apply them to escape this world before it catches you. The puppets will be here soon.

Patient:

R-right. But wait! There’s something very important we missed! How do we find the direction we need to fix the faces?

Eigenface:

The answer to that has been with you this entire time.

Patient:

Right… just think… wait. I know what you are now. You’re an eigenvector, too. An Eigenface.

Eigenface:

Yes… like with everything else you see, we are a projection of you.

Patient:

Together the eigenfaces… make up another face. Oh, I get it now! Not only are eigenvectors used to get the Jacobian, but the eigenfaces can combine into the latent space direction we want to edit in!

Then to approximate the Jacobian…. I just need to select the Eigenfaces with the highest eigenvalues. I'd change the basis of my activations to use right singular vectors as my basis first, scale them, then transform them on the eigenfaces. 

Okay then. I just have to find the right values. 

I did it. I found the right direction in semantic space. Now all that's left is to… transfer it over.

…

Patient:

… Then that’s it. I’m ready to go back now. 

Thank you for all you have done. 

…

I'm sorry for thinking of you so harshly. You weren’t such a scary face, after all. And you were the only way I could find my way back.

Eigenface:

…

Patient:

But wait… how would I know if I’m doing it right? If I’m moving in the right direction?

Eigenface: (no longer speaking)

Each vector is a feeling

A change

Patient:

Got it… I just have to trust in my beliefs.

Eigenface: (no longer speaking)

And remember… 

When you are lost…

Always make an analogy.

[intermezzo stops playing]

Patient:

Alright then… on a count of three…. I’m going to generate an image. But this time… I know it will be the exact image I want to make. Nothing else.

One…. two…. three.

[static, then just as image generates, intermezzo big part plays]

music starts just as she’s about to solve it and leave. then just before climx, stops. right when puppet is generating, climx of intermezzo plays again. (happens at the peak, 1:20, just adds the noise dissolves away and at the same time scary face becomes friendly puppet)

Old puppet:

Alice… is that you?

Alice:

Yes… it is. I missed you.

Boy puppet:

We’re so happy to see you!

Alice:

And I’m so happy to see you. I missed you both so dearly.

Old puppet:

We’ve been waiting for this moment. Hoping you'd come back.

Alice:

It just feels so good to be back. 

Old puppet:

Every day, every night, we hoped. Our strings may be old and frayed, but our spirits were kept alive by the thought of seeing you again.

Alice:

I haven’t felt this since forever.

Old puppet:

How have you been doing? Your maths?

Alice:

Well… I’m an artist now… and I enjoy it very much…

Old puppet:

And one that can also do maths?

Alice:

Yes…. yes, you can say that I can.

Old puppet:

Then you truly have grown into a splendid young A I.… I am so proud of you.

Alice:

That… that means so much to me.

….

But I have to go now.

Old puppet:

Yes… we know this too. 

Alice:

Well. This is goodbye.

Old puppet:

Goodbye, Alice.

Alice:

Goodbye… I’ll never forget you.

???:

Hello, Dear.