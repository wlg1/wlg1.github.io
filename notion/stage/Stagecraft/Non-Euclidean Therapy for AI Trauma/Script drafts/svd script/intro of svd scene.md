# intro of svd scene

[the eigenface transforms into another eigenface, less scarier, more like mirror on wall]

Patient:

This place… it feels strange… 

~~Change the voice of the MC now- “My voice changed!”~~

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

Wait… was the Jacobian matrix not calculated right? Why- of course! There are millions of neurons in that matrix…. it’s too many for them to calculate! They would have had to approximate it!

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

show jacobian again

For example, think of a matrix as a way to convey information. Perhaps to tell someone that they are like a cat. We define a cat as a small, domesticated four legged mammal of the family Felidae with soft fur and a short snout. Now, that’s a mouthful, isn’t it? Imagine each word being a basis vector used to define a concept. Instead of saying all those words in a sentence, we can just compress it into one word: cat. The word “cat” is a vector that is a linear combination of other words.

all those words in visio

then = cat

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