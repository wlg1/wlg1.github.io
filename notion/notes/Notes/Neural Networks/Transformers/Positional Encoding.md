# Positional Encoding

[https://e2eml.school/transformers.html#positional_encoding](https://e2eml.school/transformers.html#positional_encoding)

![Untitled](Positional%20Encoding%2027e592dc216e43cdb52abea533181cb6/Untitled.png)

The position of the word in the embedding space acts as the center of a circle (ORIGINALLY). A perturbation is added to it, depending on where it falls in the order of the sequence of words. For each position, the word is moved the same distance but at a different angle, resulting in a circular pattern as you move through the sequence. Words that are close to each other in the sequence have similar perturbations, but words that are far apart are perturbed in different directions.

https://youtu.be/zxQyTK8quyY?si=0FLkb0UF0KAz64zp

Each token pos has an embedding vector of size dmodel neurons

Each embedding neuron has its own sin or cos wave. Dmodel has dmodel embedding neurons.

Each token pos is an x-axis tick on the wave.  Thus stack each embedding as a row, now the col of an xtick has all pos encodings of that xtick pos. Add these vector wise to each dmodel value of the embedded vector of that one hot token. 

The y-axis value of each x-axis tick is added go each dmodel value of that token pos on the x-axis . This value is independent of the token, it only depends on position 

For decoders, a lot of ppl start with token they call eos, even though when decoder that token is at the start of the string input