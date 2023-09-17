# Why do NN use LA

cut down to 6m: use lots of cuts instead of fluid, slow animation; speedup

how long each still is depends on script, so write it first

- optional
    
    Though knowing this will significantly help you understand your own mind, it is not required. I will take 5 minutes to explain this, so if at any time you wish to move on, please feel free to tell me to stop and skip ahead.
    

---

Start:

Now, moving onto the second function- the Jacobian matrix- we can start talking about cats. Before delving in, we first need to discuss matrix multiplication. I will tell you a story about cat people to explain why matrices are so useful for modeling your mind.

---

Ending:

Therapist:

We’ve skipped over a few things, for the sake of time, but that is the crux of it. What did you think of that tale?

Pat:

…well, umm…. The cats were very nice.

Therapist:

Hmm…. well then. Let’s just move on to connecting this to the Jacobian.

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