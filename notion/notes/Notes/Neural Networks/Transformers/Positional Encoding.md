# Positional Encoding

[https://e2eml.school/transformers.html#positional_encoding](https://e2eml.school/transformers.html#positional_encoding)

![Untitled](Positional%20Encoding%2027e592dc216e43cdb52abea533181cb6/Untitled.png)

The position of the word in the embedding space acts as the center of a circle (ORIGINALLY). A perturbation is added to it, depending on where it falls in the order of the sequence of words. For each position, the word is moved the same distance but at a different angle, resulting in a circular pattern as you move through the sequence. Words that are close to each other in the sequence have similar perturbations, but words that are far apart are perturbed in different directions.