**CHAPTER 1.1**

<a href="index.md">back</a>

Let's start with an example that will show us how matrix multiplication transforms data to reveal new insights. Say there's a population of cats and rats, and we represent them in a dataset. However, the dataset is only able to measure two features: body size, and face length (or more specifically, snout length).

![Figure 1: Cat](/cob/fig1.PNG)

So every entity in the population is represented in the dataset as a data point, which is an abstraction defined only by body size and face length:
[arrow from text to pics of shapes only, labeling which is body size and which is face length]

We can represent the datapoints in this dataset as data points in a coordinate space, using the two features as axes:

<img src="/cob/fig2a.PNG" width="300" height="200">
<img src="/cob/fig2b.png" width="300" height="200">
<!---Make dataset image: first row is face, second row is body, third row is data pt (combo of both) using #s, then show in coord sys on right. Then in 2nd image, turn all numbers into imgs, and again show in coordsys on right.--->

<img src="/cob/fig3a.PNG" width="300" height="200">
<img src="/cob/fig3b.png" width="300" height="200">

When labeling our coordinate space, if we keep only the images of unit 1, we get:
<img src="/cob/fig2.png" width="600" height="400">

Every data point is a combination of [body size 1] and [face length 1]. For instance, the data point (2, 0.5), which represents [cat pic], is a combination of [2 size body pic] and a [face length of 0.5]. Note that [2 size body pic] = 2 * [body size 1] and [face length of 0.5] = 0.5 * [face length 1].
[body size 1] is smaller than [body size 2]

![Figure 3: Linear Combination](/cob/fig3.PNG)

If we see each data point as a vector, then every vector is an addition of [body size 1] and [face length 1], such that [body size 1] and [face length 1] are basis vectors. And so in this coordinate space, every entity like [cat pic] is labeled using an addition of [body size 1] and [face length 1]. Thus (2, 0.5) can also be represented as [2 0.5] = [basis vector addition]

![Figure 4: Cat in Coordinate Space](/cob/fig4.PNG)

[under each body size pic, number it so reader knows if it's 1, 2, etc. The 2 glues two 1s together, showing the border, the 0.5 shows the other half grayed out, etc. This is to indicate they're scaling the unit vector. But [cat pic] does not do this, since it's not always measured using bodysize or face length, it's just pure data that can be represented using different features. you can show the addition with an 'intermediate step' that shows gluing them on, then removing the borders/faded. can also be gif]

Now there is another way to measure the entities in this population. We can assign each entity the following two labels: 1) How likely it is to be a cat, and 2) How likely it is to be a rat.

How do we find the values of these new measurements? We can calculate them using the measurements from the previous system. For example:

Shorter face + Bigger body = Cat

Longer face + Smaller body = Rat

Or in terms of basis vector addition:

Fig 5
[figure showing the analogy: 
Bigger body + Shorter face = Cat
2 * [body pic X] + 0.5 * [face pic Y] = value 2X+0.5Y on cat axes ]

What are X and Y? We will reveal them once we get into the algebra of matrix multiplication in section [].

[coordinate space of body size vs face length, showing cat and rat, but onto it fades 'likely a cat' and 'likely a rat'. then it shifts.]

Since these two measurement methods are measuring the same entities, the entities in Model 1 are present in Model 2, but are labeled differently:
[coordinate space and labeled vectors don't change, and there's only 1. Only objs prev on basis vectors move.]
[as it's changing, the old basis labels shift too. the word 'body size' shifts into a non-axes vector, but the word 'likely a cat' shifts onto the basis vector. all 4 axes concepts are present.]
[ Another way to fade is to first show images, then fade away into colored dots, then move dots, and fade images back in.]
https://docs.manim.community/en/stable/reference/manim.animation.fading.FadeOut.html
Or fade out still image using video editor

(Likely a cat 1 (axis j) means "1 unit sure"?)

Since each coordinate space is a different way to represent the data, let's call each coordinate space a Model. The first model we saw will be Model 1, and the second will be Model 2.

Fig 6a, 6b

<img src="/cob/fig6a.png" width="300" height="200">
<img src="/cob/fig6b.png" width="300" height="200">

Label left as Model 1, etc
[Model 1, and Model 1 on top of Model 2. Sys 2 'jk'. No vectors.]

The [body size 1] that c (colored) pointed to is now in a new location in Model 2. So is the [face length 1] that d pointed to.*

* note that [body size 1] is present in Model 2, even though it's missing [face length]. In other words, it's [body size 1] + 0 * [face length 1]. This means that any data point which only contains a body of size 1 is seen as [meaning in terms of basis jk]

Fig 7a,7b
[Model 1, and Model 1 on top of Model 2. Sys 2 'jk'. WITH vectors.]
Disclaimer: now show with rotated vectors. Animation doesn't rotate vectors. This can get confusing because before, the vectors stayed in place. So we have to note that these are different vectors, just colored the same way because they point onto the same data point.
To prev clutter here, ONLY use 2 vectors: c and d. Or perhaps don't show them as vectors, just as dots. This should be clean and summarized.


We know in Model 1 that [2 0.5] is [cat pic].

Fig 8a, 8b

<img src="/cob/fig8a.png" width="300" height="200">
<img src="/cob/fig8b.png" width="300" height="200">

[[2 0.5] catpic in Model 1 and [2 0.5] in Model 1 on 2. I vector is fixed. unlike prev anim, fade j,k only after change basis so not too cluttered]

The two [2 0.5] no longer label the same Concept! [labels cat pic on left, and nothing on right] [color code or include pic of vector when referring to [2 0.5] in text paragraph]

This is because [2 0.5] no longer has the same meaning as it did in Model 1. Now it means "it's very likely to be a rat (2), but not as likely to be a cat (0.5)". In fact, [2 0.5] should now point to [rat pic], instead of [cat pic].

Fig 9
[now fill in what [2 0.5] is in Sys 2]

This shows the difference between the entities in the real world, and the model that represents those entities using labels. [2 0.5] is not [cat pic] itself; it is merely a label of it, and whichever label is used for [cat pic] depends on the basis vectors used to define every label. 

[2 0.5] != [cat pic]

Fig 10
[animated reality of concepts vs fixed coord space model]

Notice that Model 2 demonstrates an idealized, simplified example of what a neural network does- it is making a guess about the data point given to it as input. In fact, one can think of it as a single layer 'neural network' such that for its neuron function:

o = ReLU(WX + b)

used to calculate the values it guesses for the 2 classes {cat, rat}, it sets ReLU = identity and b = 0, thus using the equation:

o = WX

Fig 11
[picture of X as input vector, W as arrow, O=WX as Model 2 vector on [cat pic]]

While [cat pic] is merely how the dataset sees [actual cat pic], we are referring to [cat pic] as an "entity in the real world". This is because the only information the neural network knows about [actual cat pic] comes from [cat pic]. For the purposes of this example, we can replace [cat pic] with [actual cat pic] to explain the same concept.*

Fig 12
[fading gif of changing abstractions back to actual pics; place images on coord sys]

? * FOOTNOTE: In this example, [cat pic] contains information from the original dataset that does not change after the transformation- namely, body size and face length. However, in other cases, it is possible for a transformation to reduce the information previously contained, although this information may not be important.

---

Let's look at another example involving [poison pic and gift pic] to further illustrate the difference between the real world and our coordinate space model. Instead of using numbers, let's use letters to label our entities.

[first show coordinate space labeling gift as poison]

To an English speaker, this may look wrong. But in German, [poison pic] is in fact called 'gift'. If a German speaker tells the English speaker that they're giving the English speaker a gift, the English speaker may be delighted. But they shouldn't be, because what they're actually receiving is [poison pic], which would kill them.

Instead, the English speaker needs to know what [poison pic] is actually referring to. So they need to translate from German to English as follows:

[animation transforming poison and gift pics to English coordinate space. The vector does not move. Label first Sys as German, second as English.]
[Don't give names to basis vectors, ONLY show I -> gift, which is wrong.]

label ('gift') in German != label ('gift') in English
label ('gift') in German ~ label ('poison') in English 

Relating this back to using numbers as labels (write #s below):
label [2 0.5] ('gift') in German != label [2 0.5] ('gift') in English
label [2 0.5] ('gift') in German ~ label [? ?] ('poison') in English 

Now if the English speaker tells the German speaker that they're giving them a 'gift', the German speaker must translate this to a German translation* that makes them understand that it's [gift pic]. 
* not necessarily a word, but possibly a German sentence, or even a paragraph or textbook

[show coordinate space w/ Geschenk]

[2 0.5] (Gift, German) != [2 0.5] (Gift, English)
[2 0.5] (Gift, German) ~= [-4 1] (Disgust, English)
[1/3 5/3] (Geschenk, German) ~= [2 0.5] (Gift, English)

Note that there is a difference between "what gift translates to" and "what gift means". "What gift translates to in German" means what the label on [gift pic] is in English. "What gift means in German" is about what the LABEL 'gift' itself points to in German. The entity [gift pic] and the label 'gift' are not the same. They are only the same when using English, which is defined by the "English basis vectors". More about what this means will be discussed in section X, which views basis vectors in a similar way to the Rosetta Stone.

"what gift translates to" : [gift pic]
"what gift means": the label 'gift' (each label should be highlighted w/ diff font)

But what does the label 'disgust' mean in German? As we see in the German coordinate space, it does not point to any entity. In fact, the label 'disgust' does not mean anything in German. Not all labels have to point to an entity; so in some coordinate spaces, they just mean nonsense. This is an instance of 'not confusing the map for the territory'- the map of Switzerland is not 1-1 with Switzerland itself. The model may not capture everything about reality.

[show a place in Switzerland not on the map]

* this is an example of a False Friend. link

<<<
Now that we understand the difference between entities and labels, let's look back at our example with cats and rats. Remember that in Model 2, the vector I no longer labels the entity [cat pic]; in Model 2, it's the vector O that labels [cat pic]. 

[put vector O on coord sys]

How do we calculate what the new label for [cat] is? As we'll soon see in section X, the answer is found using Matrix-Vector Multiplication.

<<<
MOVE TO 1.1+:
Note that the relationships between the entities doesn't change. Since the basis vectors from Model 1 still exist in Model 2, you can still use the instructions from Model 1, but you have to translate them using the change of basis matrix.
... As we'll see in section X, this is why the dot product instructions work.

section Y will delve deeper into the relationships between concepts, and how they can be preserved or destroyed via matrix multiplication. It retrieves insights that are crucial for...

While [cat pic entity] is a representation of a entity that exists in the real world, 
Relationships are preserved. Analogy. Structure preserving map
[Maps between 2 domains: the real world, and the coordinate space]

