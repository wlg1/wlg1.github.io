# llama2_ablate_prompts_explora_v1.ipynb

[https://colab.research.google.com/drive/1xrsPBgbC_AN_I6EssNpi1M1SxVuODluf](https://colab.research.google.com/drive/1xrsPBgbC_AN_I6EssNpi1M1SxVuODluf)

- tasks that work for clean
    - 1 2 3
    - 1 2 3 4 5 6
    - 1 2 … 50
    - one two three
    - January February March
    - Bob is first. David is
        - Bob is first in line. David is
    - "What comes after Monday is Tuesday, and **two** days after is”
    - "uno dos tres”
    - "2 4 6 “
- tasks that do not work for clean (increments only if recogs is seq or word problem context)
    - 1
    - two
    - March
    - "Two days after Monday is”

Get the llama-2 impt heads and MLPs from node ablation nbs

Able to corrupt by ablating:

1 2 3

Didn’t Work:

- ablate 20.7, 1.11, 16.0

Worked: (to destroy corr answer)

- 

2 4 6

Didn’t Work:

- ablate 0.1
- ablate 1.14

Worked: (to destroy corr answer)

- ablate 0.13

"What comes after Monday is Tuesday, and **two** days after is”