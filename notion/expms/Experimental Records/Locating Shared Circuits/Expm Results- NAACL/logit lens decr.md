# logit lens decr

- [logit lens on decr circ](https://colab.research.google.com/drive/1GeM2vLnIan_q6kdiGKQoDcMrAtYe0FLG#scrollTo=mA0oSvhtL7q7&line=1&uniqifier=1)

note to read it means “after L9” for row 9. It’s not before L9.

- this depends a lot on seq length, when it changes
- [https://colab.research.google.com/drive/1GeM2vLnIan_q6kdiGKQoDcMrAtYe0FLG#scrollTo=h7PMwYkwOI6w&line=2&uniqifier=1](https://colab.research.google.com/drive/1GeM2vLnIan_q6kdiGKQoDcMrAtYe0FLG#scrollTo=h7PMwYkwOI6w&line=2&uniqifier=1)
- Don’t just unembed at end of each layer. Unembed at each head but not directly from MLP0
- compare to: [https://colab.research.google.com/drive/1ahWI9e0NMeAjdFNnj2vEj4d4aYIGsoNP#scrollTo=_1C-K9JDQ1G2&line=2&uniqifier=1](https://colab.research.google.com/drive/1ahWI9e0NMeAjdFNnj2vEj4d4aYIGsoNP#scrollTo=_1C-K9JDQ1G2&line=2&uniqifier=1)
    - 1515 actually is 2 tokens, just the last 15 has no space in front