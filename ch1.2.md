---
theme: jekyll-theme-minimal
title: CHAPTER 1.2
---

<!-- <head>
    <link rel="stylesheet" href="index.css">
</head> -->

<!-- <div class="topnav">
  <a class="active" href="eduBlogHome.html">Home</a>
  <a href="#contact">Contact</a>
  <a href="#about">About</a>
</div>
<br> -->

<center><h2>CHAPTER 1.2: Beware of False Friends when Changing Basis?</h2></center>

**(Reading time: 2 minutes)**

---

Before delving into the intricacies of matrix multiplication, let's look at another example to gain even better intuition about the difference between the real world and our coordinate space model. Instead of cat and rat data samples, we'll look at the two data samples <img src="/cob/poison.jpg" width="30" height="30">, a dangerous substance, and <img src="/cob/gift.jpg" width="30" height="30">, which is charitably given to someone. And instead of using numbers, let's use letters to label our entities. This means our models will resemble languages, some of which also use letters to label entities. So our first model, or language, is labeled as follows:

<img src="/cob/german_gift.PNG" width="400" height="300">

To an English speaker, this may look wrong, because <img src="/cob/poison.jpg" width="30" height="30"> should be called something like 'poison', not 'gift'. But in German, <img src="/cob/poison.jpg" width="30" height="30"> is in fact called 'gift'. If a German speaker tells the English speaker that they're giving the English speaker a gift, the English speaker may be delighted because they think they're getting <img src="/cob/gift.jpg" width="30" height="30">. But they shouldn't be, because what they're ACTUALLY receiving is <img src="/cob/poison.jpg" width="30" height="30">, which would kill them.[^false_friend]

Since there is a misunderstanding, the English speaker needs to know what 'gift' is actually referring to; or in other words, to know the right English word to use for <img src="/cob/poison.jpg" width="30" height="30">. So they need to translate from the language above, which resembles German, to English as follows:

[^false_friend]: This is an example of a False Friend, "which is a pair of words in two different languages that look similar, but have different meanings." Source: https://en.wikipedia.org/wiki/False_friend

![gift_cob](/cob/gift_cob.PNG)
<!---[animation transforming poison and gift pics to English coordinate space. The vector does not move. Label first Sys as German, second as English.]
[Don't give names to basis vectors, ONLY show I -> gift, which is wrong.]--->

In summary:

<!---<p align="center"> --->
'gift' in German <img src="/cob/poison.jpg" width="30" height="30"> != 'gift' in English <img src="/cob/gift.jpg" width="30" height="30">

'gift' in German <img src="/cob/poison.jpg" width="30" height="30"> ~ 'poison' in English  <img src="/cob/poison.jpg" width="30" height="30">

Relating this back to using numbers as labels:

$$\begin{bmatrix} -1 \\ 2 \end{bmatrix}$$ in German <img src="/cob/poison.jpg" width="30" height="30"> != $$\begin{bmatrix} -1 \\ 2 \end{bmatrix}$$ in English <img src="/cob/gift.jpg" width="30" height="30">

$$\begin{bmatrix} -1 \\ 2 \end{bmatrix}$$ in German <img src="/cob/poison.jpg" width="30" height="30"> ~ $$\begin{bmatrix} -4 \\ 1 \end{bmatrix}$$ in English <img src="/cob/poison.jpg" width="30" height="30">

Now if the English speaker tells the German speaker that they're giving them a 'gift', the German speaker must translate this to a German word or expression that makes them understand that it's <img src="/cob/gift.jpg" width="30" height="30">. The German word for <img src="/cob/gift.jpg" width="30" height="30"> is 'geschenk'. Going the other way around, the English word for  <img src="/cob/poison.jpg" width="30" height="30"> is 'poison'.

![all_words_cob](/cob/all_words_cob.PNG)
<!---[show coordinate space w/ geschenk and poison]--->

$$\begin{bmatrix} 1/3 \\ 5/3 \end{bmatrix}$$ 'geschenk' in German <img src="/cob/gift.jpg" width="30" height="30"> ~ $$\begin{bmatrix} -1 \\ 2 \end{bmatrix}$$ 'gift' in English <img src="/cob/gift.jpg" width="30" height="30">

$$\begin{bmatrix} -1 \\ 2 \end{bmatrix}$$ 'gift' in German <img src="/cob/poison.jpg" width="30" height="30"> ~ $$\begin{bmatrix} -4 \\ 1 \end{bmatrix}$$ 'poison' in English <img src="/cob/poison.jpg" width="30" height="30">

<!---
Note that there is a difference between "what gift translates to" and "what gift means". "What gift translates to in German" means what the label on <img src="/cob/gift.jpg" width="30" height="30"> is in English. "What gift means in German" is about what the LABEL 'gift' itself points to in German. The data ssample <img src="/cob/gift.jpg" width="30" height="30"> and the label 'gift' are not the same. They are only the same when using English, which is defined by the "English basis vectors". More about what this means will be discussed in section X, which views basis vectors in a similar way to the Rosetta Stone.

"what gift translates to" : <img src="/cob/gift.jpg" width="30" height="30">

"what gift means": the label 'gift' (each label should be highlighted w/ diff font)
--->

But what does the label 'poison' mean in German? As we see in the German coordinate space, it does not point to any data sample. In fact, the label 'poison' does not mean anything in German. The same goes for the label 'gescheck' in English. Not all labels have to point to an data sample; so in some coordinate spaces, they just mean nonsense. 

<center><a href="ch1.3.html"><b>NEXT: CHAPTER 1.3</b></a></center>

<!---
This is an instance of 'not confusing the map for the territory'- the map of Switzerland is not 1-1 with Switzerland itself. The model may not capture everything about reality.

[show a place in Switzerland not on the map]
--->

<!---
MOVE TO 1.1+:
Note that the relationships between the entities doesn't change. Since the basis vectors from Model 1 still exist in Model 2, you can still use the instructions from Model 1, but you have to translate them using the change of basis matrix.
... As we'll see in section X, this is why the dot product instructions work.

section Y will delve deeper into the relationships between concepts, and how they can be preserved or destroyed via matrix multiplication. It retrieves insights that are crucial for...

While [cat pic entity] is a representation of a entity that exists in the real world, 
Relationships are preserved. Analogy. Structure preserving map
[Maps between 2 domains: the real world, and the coordinate space]
--->

<br><br>

---
---

<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript" async></script>