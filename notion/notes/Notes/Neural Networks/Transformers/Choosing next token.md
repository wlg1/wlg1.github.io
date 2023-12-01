# Choosing next token

[https://huggingface.co/blog/how-to-generate](https://huggingface.co/blog/how-to-generate)

There is evidence that the apparent flaws of *greedy* and *beam* search - mainly generating repetitive word sequences - are caused by the model (especially the way the model is trained), rather than the decoding method, *cf.* **[Welleck et al. (2019)](https://arxiv.org/pdf/1908.04319.pdf)**. Also, as demonstrated in **[Welleck et al. (2020)](https://arxiv.org/abs/2002.02492)**, it looks as *top-K* and *top-p* sampling also suffer from generating repetitive word sequences.

[https://towardsdatascience.com/foundations-of-nlp-explained-visually-beam-search-how-it-works-1586b9849a24](https://towardsdatascience.com/foundations-of-nlp-explained-visually-beam-search-how-it-works-1586b9849a24)

- With Greedy Search, we took just the single best word at each position. In contrast, Beam Search expands this and takes the best ’N’ words.
- With Greedy Search, we considered each position in isolation. Once we had identified the best word for that position, we did not examine what came before it (ie. in the previous position), or after it. In contrast, Beam Search picks the ’N’ best *sequences* so far and considers the probabilities of the combination of all of the preceding words along with the word in the current position.

In other words, it is casting the “light beam of its search” a little more broadly than Greedy Search, and this is what gives it its name. The hyperparameter ’N’ is known as the Beam width.

![Untitled](Choosing%20next%20token%201e0a56d892ae41ed8698df50d7c08d49/Untitled.png)

It finally ends up with the two best sequences and predicts the one with the higher overall probability.

---

Why does a transformer need to predict probabilities for all tokens in the input at each position if it only needs the probabilities for the last token to get the next token?

Diff responses:

[https://chat.openai.com/c/5f284337-36aa-42b1-9b76-b1a120aed2c6](https://chat.openai.com/c/5f284337-36aa-42b1-9b76-b1a120aed2c6)

[https://chat.openai.com/c/95ce2e25-b66e-4f8b-b629-0b845e3c8526](https://chat.openai.com/c/95ce2e25-b66e-4f8b-b629-0b845e3c8526)