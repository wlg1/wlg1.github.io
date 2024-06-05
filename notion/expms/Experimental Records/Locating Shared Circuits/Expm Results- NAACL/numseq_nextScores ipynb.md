# numseq_nextScores.ipynb

Link to notebook:

[https://colab.research.google.com/drive/1QvmISAyqw413-zhswSTc5ylmXHrKZ3Xl](https://colab.research.google.com/drive/1QvmISAyqw413-zhswSTc5ylmXHrKZ3Xl)

The aim of this experiment is to get evidence suggesting what each head is doing. For instance, an attention head may be copying a token by outputting the same token, thus passing it along in the circuit. Here, we want to check if an attention head takes in a token (eg. 1) and outputting the next token (eg. 2). We do this because when we checked the top-5 tokens outputted by head 9.1 using the copy score method described below, we found the top-5 often had the “next token”, rather than the same token (though it also had the same token in many cases).

The copy score is calculated by:

1) First get matrix `z_0` of 1st MLP embedded vectors of the tokens for each input prompts

2) Multiply them by the OV matrix of the head (not taking QK into account)

3) Unembed this output and apply final layer norm to get logits

`pred_tokens` are the top-k tokens

4) Get the logits for a specific keyword position, and find the tokens with the top 5 logit scores

“Specific keywords” are what we want to see are copied. For instance, every subject in a sentence can be considered a keyword to see if subjects are copied (outputted by the head). For digits, each digit is a keyword to see if digits are copied.

`pred_tokens_dict[prompt[word]] = pred_tokens`

`pred_tokens_dict`is printed out to show the top-5 for a specific token `prompt[word]`

5) If the specific token is within these top-5 tokens, +1 to total score

6) Divide total score by total number of keywords

Check what percentage of “keywords” from an input prompt are in the top-k tokens (based on logit score).  In this case, k=5. For multiple input prompts, it takes the percentage of all keywords added up from all prompts.

How does copy score check if a token is copied? By this:

**`if " " + prompt[word] in pred_tokens:`**

The `prompt` is a dict of the prompt text and keys (`word`), such as “1” or “2”. Thus, get `prompt[word]` as a string such as “1”, change to an int and add 1, then change back to a string. Check if this “next digit” is in `pred_tokens`.

The main difference with Next Score is that before, we checked if the same digits/numberwords/etc are copied by the head. Now, we modifying step (5) so that for a specific token, we are not checking if that specific token is within its top-5 predicted tokens, but if the “next” of the specific token is within the top-k.

If `print_tokens=True`, then the output would show the top-k for each keyword. For each keyword, the last value is `nextToken_in_topK`, which states if the “next” token is among the top-k.

Also modify the condition to be: 

`if " " + next_word in pred_tokens or next_word in pred_tokens:`

---

Compare the next score to the copy score

For head 9.1, “next” score is 87%, while “copy” score is 59%

So far, this evidence suggests that 9.1 is responsible for associating a token with its “next” member, rather than for the same member.

This may be **important** because this means the attention heads are responsible within the circuit for getting the next member.

---

Test this on more heads:

[https://colab.research.google.com/drive/1QvmISAyqw413-zhswSTc5ylmXHrKZ3Xl#scrollTo=7Ir5Ct8U-VUE&line=1&uniqifier=1](https://colab.research.google.com/drive/1QvmISAyqw413-zhswSTc5ylmXHrKZ3Xl#scrollTo=7Ir5Ct8U-VUE&line=1&uniqifier=1)

Put this in a table where cols are copy and next, and rows are heads: (disregard scores <1%)

| Head | Copy Score | Next Score |
| --- | --- | --- |
| 6.1 | 1.8% | 14.9% |
| 7.10 | 87.4% | 48.7% |
| 8.8 | 36.6% | 55.4% |
| 7.11 | 16.5% | 9.3% |
| 8.11 | 76.3% | 25.8% |
| 9.1 | 59.3% | 87.3% |

7.10 and 8.11 seem to be more copy heads than next heads

8.8 is “somewhere in the middle”, not having that high scores for each

Only 9.1 seems to be overwhelming a “next” head

---

This might be enough to state these are next heads.

Now, how do next heads interact in the hypothesized circuit so far? Layers 8 and 9 are considered middle-late heads.

---

To do next:

- (Optional)- make a table for each **token** with columns of “next” and “copy” which state if the next or same token is in the top-k
- Try to piece these heads together into a hypothesized circuit
- If the heads already get the next member, are MLPs impt in the circuit, or not really? Knockout MLPs to test this
- Notice that the top-5 often contains number words, not just digits. Are number words used in the “thinking process” of the model to output the correct next digit, despite not being used in the final output? Figure out a way to test this.