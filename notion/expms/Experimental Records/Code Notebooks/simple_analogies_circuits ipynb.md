# simple_analogies_circuits.ipynb

[https://colab.research.google.com/drive/1mhcgx2SU3GrDq3pMZp_-JPtE_fO-7kGg#scrollTo=7GpmMGjpioid](https://colab.research.google.com/drive/1mhcgx2SU3GrDq3pMZp_-JPtE_fO-7kGg#scrollTo=7GpmMGjpioid)

simple_analogies_circuits.ipynb : 

GPT-2-small prompts:

- "1 2 3 4”
- "2 4”
- "Mary is a human. Fido is a dog. The pet of this family is Fido. Rachel is a human. Pebbles is a cat. The pet of this family is”
- "The human is Mary. The dog is Fido. The pet is Fido. The human is Rachel. The dog is Pebbles. The pet is”

GPT-2-large prompts:

- "Mary is a teacher. Fido is a student. The child is Fido. Pebbles is a student. Rachel is a teacher. The child is”
    - Gets the most recent subject instead of the student
    - TRY: more in-context examples
- "Mary. Fido. Fido. Pebbles. Rachel. “
    - Fails
- "Mary is X. Fido is Y. Z is Fido. Pebbles is Y. Rachel is X. Z is “
    - Fails

---

[https://colab.research.google.com/drive/1aOEeY4roW8oWqkZ0MuuZRJXmJGDRNcbr](https://colab.research.google.com/drive/1aOEeY4roW8oWqkZ0MuuZRJXmJGDRNcbr)

simple_analogies_circuits, pt2.ipynb

Checks if GPT-2-Large and GPT-2-xl and GPT-Neo-2.7b can correctly complete analogies. Does preliminary logit lens, activation patching and attention head analysis on a few input formats. Also checks why these billion parameter models have trouble finding who “is” or who “has” given a previous statement from in-context learning. Prompts include:

- Transitivity: Mary has X. John has Y. Z is John. [Repeat template to find Z in new target system]
- "John is big. Mary is small. John is tall. Mary is”

Try:

- Use more in-context examples

---

simple_analogies_pt3.ipynb

[https://colab.research.google.com/drive/1GQo_RSEY40ncByvwy81kxwSKGPHlbxSx?usp=sharing](https://colab.research.google.com/drive/1GQo_RSEY40ncByvwy81kxwSKGPHlbxSx?usp=sharing)