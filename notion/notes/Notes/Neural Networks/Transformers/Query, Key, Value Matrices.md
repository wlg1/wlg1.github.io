# Query, Key, Value Matrices

[https://towardsdatascience.com/illustrated-self-attention-2d627e33b20a](https://towardsdatascience.com/illustrated-self-attention-2d627e33b20a)

![Untitled](Query,%20Key,%20Value%20Matrices%20fe92464f6ee24068b6aaa56bb85e903e/Untitled.png)

There are 4 basis vectors to represent a token 

There are 3 tokens (inputs)

Each row of the Q weight matrix is on a basis vector

Each column of the Q weight matrix is for a token 

How each weight is learned depends on how each token is encoded as a vector

---

[https://jalammar.github.io/illustrated-transformer/](https://jalammar.github.io/illustrated-transformer/)

~~Unlike what chatgpt claims,~~ there is a separate key VECTOR for each word in the input sentence (paragraph, book, etc). These vectors are separate columns of the key matrix.

When we do Input * Key Matrix, we are doing 

input (row) * key column

to calculate each element of the output vector. This output vector is a row in the output matrix.

[https://www.youtube.com/watch?v=4Bdc55j80l8&ab_channel=TheA.I.Hacker-MichaelPhi](https://www.youtube.com/watch?v=4Bdc55j80l8&ab_channel=TheA.I.Hacker-MichaelPhi)

![Untitled](Query,%20Key,%20Value%20Matrices%20fe92464f6ee24068b6aaa56bb85e903e/Untitled%201.png)

---

![Untitled](Query,%20Key,%20Value%20Matrices%20fe92464f6ee24068b6aaa56bb85e903e/Untitled%202.png)

On a graph, red arrow between hidden states on different token rows corresponds to the final output of that token’s row ??? still doesn’t make sense

![Untitled](Query,%20Key,%20Value%20Matrices%20fe92464f6ee24068b6aaa56bb85e903e/Untitled%203.png)