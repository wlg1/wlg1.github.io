# ablate_seqcont_thenMath_explora

Try diff circs on more tasks for gpt2-small

- tasks that work for clean
    - 1 2 3
    - 1 2 3 4 5 6
    - 1 2 … 50
    - one two three
    - January February March
    - Bob is first. David is
        - Bob is first in line. David is
    - "What comes after Monday is Tuesday, and **two** days after is”
- tasks that do not work for clean (increments only if recogs is seq or word problem context)
    - 1
    - two
    - March
    - "Two days after Monday is”

Try diff lengths

- v1
    - [pure seq 1 2 3](https://colab.research.google.com/drive/1OVMkA1IZKZLmKq2paGRIXykzm5fxrGIx#scrollTo=H5H-d2URUSVJ&line=1&uniqifier=1)
    - [seqcont word problems](https://colab.research.google.com/drive/1OVMkA1IZKZLmKq2paGRIXykzm5fxrGIx#scrollTo=aB5OqTVcYigX&line=1&uniqifier=1)
- [ablate_seqcont_thenMath_explora_v2](https://colab.research.google.com/drive/1wf9Xsd4Qbq7rp-v4DS8_ozlMb_3sdRxI?authuser=4)

Able to corrupt by ablating:

To find what DID work, check if the next char is incorrect. if corr, it didn’t work.

1 2 3

Didn’t Work:

- ablate 4.4, 7.11, 9.1
- ablate 9.1 and mlp9
- ablate just 9.1
- ablate mlp 9
- ablate random head 6.2

Worked: (to destroy corr answer)

- ablate 4.4, 7.11, 9.1 and mlp 9
- ablate all

1 2 3 4 5 6

Didn’t work:

- ablate 4.4, 7.11, 9.1
- ablate 9.1 and mlp9
- ablate just 9.1
- ablate mlp 9
- ablate random head 6.2

Worked:

- ablate 4.4, 7.11, 9.1 and mlp 9
- ablate all

1 2 … 20

Didn’t work:

- ablate 4.4, 7.11, 9.1
- ablate 9.1 and mlp9
- ablate just 9.1
- ablate mlp 9
- ablate random head 6.2

Worked:

- ablate 4.4, 7.11, 9.1 and mlp 9
- ablate all

1 2 … 50

Didn’t work:

- ablate 4.4, 7.11, 9.1 and mlp 9
- ablate 4.4, 7.11, 9.1
- ablate 9.1 and mlp9
- ablate just 9.1
- ablate mlp 9
- ablate random head 6.2

Worked:

- ablate all

one two three

Didn’t work:

- ablate 9.1 and mlp9
- ablate just 9.1
- ablate mlp 9
- ablate random head 6.2

Worked:

- ablate 4.4, 7.11, 9.1
- ablate 4.4, 7.11, 9.1 and mlp 9
- ablate all

January February March

Didn’t work:

- ablate 4.4, 7.11, 9.1
- ablate 9.1 and mlp9
- ablate just 9.1
- ablate mlp 9
- ablate random head 6.2

Worked:

- ablate 4.4, 7.11, 9.1 and mlp 9
- ablate all

"What comes after Monday is Tuesday, and **two** days after is”

Didn’t Work:

- ablate random head 6.2
- ablate mlp 9

Wroked:

- ablate 4.4, 7.11, 9.1 and mlp 9
- ablate 4.4, 7.11, 9.1
- ablate 9.1 and mlp9
- ablate just 9.1

Bob is first in line. David is

Didn’t work:

- ## ablate random head 6.2
- ## ablate 4.4, 7.11, 9.1 and mlp 9
- ## corrupt 9.1 and mlp9
- ## ablate just 9.1
- ## ablate mlp 9

Worked:

- ablate all