# llama2_ablate_prompts_numwords_circ

[https://colab.research.google.com/drive/1b6qzlOVuQKwNehyiWEYObKk3v5SRU8Ep#scrollTo=5TuWmMzGHSYA](https://colab.research.google.com/drive/1b6qzlOVuQKwNehyiWEYObKk3v5SRU8Ep#scrollTo=5TuWmMzGHSYA)

1 2 3

Works:

- all nw circ heads
- top 20 nw circ heads + top 20 impt month heads

Works if CONTINUE GEN:

- top 20 nw circ heads

Doesn’t work:

- top 10 nw circ heads
- top 10 nw circ heads +  top 20 impt month heads

2 4 6

Works:

- all nw circ heads
- top 15 nw circ heads
- top 20 nw circ heads + top 20 impt month heads
- top 10 nw circ heads +  top 20 impt month heads

Doesn’t work:

- random 50
- top 10 nw circ heads

uno dos tres

Works:

- all nw circ heads
- top 10 nw circ heads
- random 10
- random 10, not allowing overlap with nw circ

Doesn’t work:

What comes after the second item in a list? Be concise.

Works:

- all nw circ heads (?)

Doesn’t work:

- top 10 nw circ heads
- random 10
- random 10, not allowing overlap with nw circ

"What comes after the second item in a list? The next item in a list is the”

Works:

- all nw circ heads

Doesn’t work:

- top 10 nw circ heads
- random 10
- random 10, not allowing overlap with nw circ

"If today is the 14th of a month, what date will it be in 10 days?”

Works:

- all nw circ heads

Doesn’t work:

- top 10 nw circ heads
- random 10
- random 10, not allowing overlap with nw circ