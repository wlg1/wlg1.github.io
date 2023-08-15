# 3 functions

Did you catch all of that? Feel free to rewind whenever you need to review it.

[make this more into a back-forth w/ ques later on. intersperse scary imagery- “an example” that’s modified but not what pateitn sees]

---

Therapist:

Let’s move on. Pay close attention this time. Otherwise, you might not be able to escape that frightening creature. And we wouldn’t want that now, would we?

…

To summarize, our aim is to navigate the hidden space, also called the Latent Space. However, we don’t know its geometry. So just like when we are lost in a forest, we can rely on a map to try to navigate our way through the forest, staying away from the puppet as best as we can. This map has its own metric, which we’ll use to approximate the distances in the forest. What is this map?

Patient:

I’m trying to think…. but, I’m- I’m not sure.

Therapist:

It’s our Semantic Space.

Patient:

Yes! We had just went over that. I’m sorry…. I was just nervous.

Therapist:

We are going to go over this procedure more thoroughly this time, distinguishing between three types of portals, which we call Functions, that go between the forest and the map.

Let’s give each of these geometric objects a symbol. We call our Latent Space X, and we call our Semantic Space S. The function “f” from X to S transfers points. This means if you are on point A on X, you will be sent to point f of A on S. Likewise, the function from S back to X will be “f inverse”. This is our first function type- a smooth map.

But this “f” only transfers locations between manifolds; it cannot calculate how a direction on the map appears from the perspective of the forest. 

[forest + map appears on screen again for 1 sec before talking again]

If the map says the distance between the lake and the puppet is one inch, that doesn’t mean the distance between them is one inch in the forest. Nor would the puppet be exactly 45 degrees north of the lake. And if you wrongly calculate where the puppet is at… there will be fatal consequences. We need another function that correctly calculates what this direction is in the actual forest. 

Thus, there are maps not just between the manifolds, but between the tangent spaces, where we can approximately see the forest as flat, just like our flat map. This flatness allows a better approximation that transfers our directions from the map to the forest; however, this only works within a tangent space that is only a very small part of the forest, which is curved over large distances.

On X, the tangent spaces are called T x, and on S, the tangent spaces are called T s. The tangent vectors in T x are called v, and tangent vectors in T s are called u. The map between the tangent spaces T x to T s is called J, and the map from T s back to T x is called J inverse. 

They are the pushforwards of the maps f and f inverse, respectively. And they are our second function type. For our case, do you know how we represent the pushforward of the smooth map from X to S?

Patient:

… I’m sorry again, but I really don’t remember.

Therapist:

… I see. I had thought you would have known. This is troubling.

Patient:

… <patient is speaking>

Therapist:

We represent it with the Jacobian Matrix. The Jacobian will not always be the pushforward; it only is under certain conditions which we won’t delve into for now.

We will also need to measure distances between tangent vectors in Latent Space using a metric. Now, this is where we’ll actually be using the Pullback function. This transfers a metric from Semantic Space to what is called a pullback metric in Latent Space. Essentially, the pullback of the smooth map calculates that a distance of one inch in the map is actually one mile in the forest. It is our third and final function.

- notes
    
    for now, don’t use symbols, just write ‘metric’ next to S, then ‘pullback metric’ next to X bracket, and use a pullback arrow (dotted) - use visio for precision
    
    a bracket between 2 vectors. animate to move thru pullback
    
    [https://wlg1.github.io/ch2.2.html](https://wlg1.github.io/ch2.2.html)
    
    dot product, which projects one vector onto another, outputting a scalar that says “how much of n2 is used to get vector n1”.
    
    show the cat person feature of ‘why NN use LA’
    
    It measures the distance between two tangent vectors ~~by taking their dot product~~
    

Now, can you summarize the three functions for me?

Patient:

Yes… I’ll- I’ll try to get it right this time.

- First, there are smooth maps f between the manifolds. These transform points, or locations.
- Second, there are pushforward functions J between the tangent spaces. These transform tangent vectors, or directions.
- Finally, there are pullback functions that transform metrics, or distances.

Therapist:

Hmm… Very good. You are doing so well. I’m proud of you.

---