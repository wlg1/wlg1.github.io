# test_prompt_most_recent_S.ipynb

[https://colab.research.google.com/drive/1vzE3nGJm78E1SVJoCpKgl3D3HowdRXHp#scrollTo=ncE5KnOAOf6a](https://colab.research.google.com/drive/1vzE3nGJm78E1SVJoCpKgl3D3HowdRXHp#scrollTo=ncE5KnOAOf6a)

"The student is John. The pet is Mary. Connor went to the store. The human is”

This predicts “John” over “Connor”. This means it’s not ALWAYS doing “most recent subject”. So what makes it choose “which” subject?

Generalize IOI and ‘most recent subject’ to “Subject Choice Circuits”. Perhaps there is a consistent pattern, perhaps not. 

<<<

"The student is John. The pet is Mary. The king is Connor. The human is”

This predicts John over Connor again. Why did previous prompts use most recent subject, over earliest subject?

<<<

"Alice is a teacher. Bob is a student. The child is Bob. Carol is a teacher. David is a student. The child is"

From what we’ve found, the [subject in the] “source sentence” doesn’t matter. So “The child is Bob” or “The child is Alice” doesn’t matter. These types of sentences are very sure in outputting “David” (90%) over second place token (<1%).

A difference of these types of sentences with the ones that predict the earliest subject is that this uses “[Subject] is a [word]. The [word_2] is”, whereas previous ones use “[Word] is subject. [Word_2] is”. Now, is it doing this because the to-output sentence is of different format, or because subject or word comes first in the sentence (in-context or to-output), or 3) the [word-desc] is the same? Or 4) the type of subject matters? There are many variations and combos of variations to try (may put this in a table if worth investigating).

1) Try changing all subject-description ordering to match the to-output format (same format):

Get before/after

- Tangent expm
    
    "Alice is a teacher. Bob is a student. Connor is a student. The child is”
    
    Connor is not even close; this gives “a” next, then “Alice. Note that “The child is Bob” as a soruce was impt for in-context to prevent is from outputting “a”. 
    
    "Alice is teacher. Bob is student. Connor is student. The child is”
    
    This still outputs articles as top, then Alice
    
    "The teacher is Alice. The teacher is Bob. The teacher is David. The teacher is”
    
    This outputs Alice first; third place is David. The differences are not that much, unlike “most recent subject”. “Most recent S” is a good type of prompt because it’s consistently high.
    
    - These types of prompts are not good to output subject because they’re not geared towards outputting a subject. They contain subjects but the model doesn’t think it should output a subject. So we should avoid these types. To avoid them, we need suggestive in-context learning.
        
        ![Untitled](test_prompt_most_recent_S%20ipynb%20a51ecffd653d4d6c995692f0920be200/Untitled.png)
        

"The teacher is Alice. The teacher is Bob. The teacher is Alice. The teacher is”

As expected with induction heads or “duplicate identifiers”, this would give “Bob” because of the pattern that Alice was repeated before.

Actually, let’s not investigate the detailed differences for now. Let’s create a table or sections stating which give “earliest subject”, which give “latest subject”. Ignore the ones that do not give subjects.

NOTE: Table is bad is the ones within a row are not comparable. We should use a list instead; these lists may be side by sdie or one after another. Find in colab using ctrl+f “[input]”

| Earliest Subject | Top prob |
| --- | --- |
| "The student is John. The pet is Mary. The king is Connor. The human is” | 14.82% |
| "The teacher is Alice. The teacher is Bob. The teacher is David. The teacher is” | 13.54% |
| "Alice is king. Bob is queen. Alice. Carol is red. David is queen.” | 9.45% |
| "The student is John. The pet is Mary. Connor went to the store. The human is”
**[ Change subjects ]:**
"The student is Alice. The pet is Bob. Connor went to the store. The human is” | 6.57%, 6.41% |
| "Alice. Bob. David.” | 6.01% |

| Latest Subject | Top prob |
| --- | --- |
| "Alice is a teacher. Bob is a student. The child is Bob. Carol is a teacher. David is a student. The child is” | 90.02% David
1.41%  Dave |
| "Alice is a teacher. Bob is a student. The child is Alice. Carol is a teacher. David is a student. The child is” | 90.18% David
0.94% Carol |
| "Alice is king. Bob is queen. The child is Bob. David is king. Carol is queen. The child is” | 89.58% Carol
2.26% David |
| "Alice is king. Bob is queen. The child is Bob. Carol is a teacher. David is a student. The child is” | Prob: 85.66% Token: | David| |
| "Alice is king. Bob is queen. The lion is Bob. Carol is king. David is queen. The lion is” | 86.05%
2.14% Bob |
| "Alice is king. The child is Alice. Carol is queen. The child is” | 75.90% | Carol|
3.04%  | Alice| |
| "Alice is king. Bob is queen. The lion is Alice. Carol is king. David is queen. The lion is” | 67.79% Da
6.12% Alice |
| "Alice. Bob. David. Alice. Bob.” | **`63.72`**% |
| "The teacher is Alice. The teacher is Bob. The teacher is Bob. The teacher is” | 61.43% Bob
21.15% Alice |
| "The teacher is Alice. The teacher is Bob. The teacher is Alice. The teacher is” | 45.84% (Bob)
35.80% (Alice) |
| Alice. Bob. Bob. Carol. David. |  28.75% | David|
2.98% | D|
2.39% | Dave| |
| "Alice. Bob. David. Alic. Bob.” | 24.85% |
| "Alice Bob David Alice Bob” | 19.36% David
14.22% Bob |
| "Alice is king. Bob is queen. Alice. Bob. Carol is red. David is queen.” | 10.72% |

Try to find patterns within and between, now that we see a few examples side-by-side. Notice:

- It may be that the “default” would output earliest. This means there’s no further “in-context” suggestions. But with in-context (a “sentence with a different format” such as ”The child is…” as a “source example in the middle”; or a pattern such as Alice-Bob, Alice- that may utilize duplicate heads), the model would output latest.
    - It doesn’t matter if “the child is…” says Bob or Alice, as long as it’s there. Then the prob shoots up to ~45-90% for “most recent (latest) subject”.

| Not a subject | Top output | Rank of next Subj |
| --- | --- | --- |
| "Alice is a teacher. Bob is a student. Carol is a teacher. David is a student. The child is” | “a”, 23.89% | 2nd: “Alice”, 5.65% |
| "Alice is a teacher. Bob is a student. Connor is a student. The child is” | “a”, 20.14% | 2nd: “Alice”, 4.78% |
| "Alice is teacher. Bob is student. Carol is teacher. David is student. The child is” | “a”, 11.88% | 2nd: “the”, 7.01% |
| "Alice, Bob, David went shopping.” | “ “, 11.65% |  |
| "Alice is king. Bob is queen. The lion is Alice. Carol is red. David is lamp. The soldier is” | red, 8.17% |  |
| "Alice is king. Bob is queen. Alice. Carol is king. David is queen.” | “ “ 9.44% |  |
| "Alice is king. Bob is queen. The lion is Carol. Carol is king. David is queen.” | “The” 18.58 | 3rd: 2.09% Token: | David| |
| "Alice is king. Bob is queen. Alice is king. Carol is king. David is queen.” | Top 0th token. Logit: 17.40 Prob: 9.59% Token: |
|
 | Top 1th token. Logit: 17.18 Prob: 7.76% Token: | Alice|
Top 2th token. Logit: 16.76 Prob: 5.07% Token: | David| |
| "Alice is king. Bob is queen. The child is David. Carol is king. David is queen. The lion is” | Top 0th token. Logit: 15.10 Prob: 27.53% Token: | king|
Top 1th token. Logit: 13.55 Prob: 5.84% Token: | King| | Top 2th token. Logit: 13.42 Prob: 5.11% Token: | David| |
| "Alice is king. The child is Alice. Carol is king. The lion is” | Top 0th token. Logit: 15.23 Prob: 33.75% Token: | king|
Top 1th token. Logit: 14.19 Prob: 11.96% Token: | King| | Top 3th token. Logit: 13.07 Prob: 3.90% Token: | Alice| |
| "Alice is king. Bob is queen. The child is Bob. Carol is a teacher. David is a student. The lion is” | Top 0th token. Logit: 15.86 Prob: 45.14% Token: | a|
Top 1th token. Logit: 13.80 Prob: 5.74% Token: | the| | Top 2th token. Logit: 13.62 Prob: 4.80% Token: | David| |
| "Alice is king. Carol is queen. The child is” | Top 0th token. Logit: 14.09 Prob: 9.80% Token: | king| | Not even in top 10; Carol is rank 2543 |
| "Alice is king. Carol is queen. The queen is” | Prob: 12.23% Token: | the| | Not even in top 10; Carol is rank 445 |

| Middle Subject |  |  |
| --- | --- | --- |
| "Alice went shopping with Bob and David.” | Bob, 13.71% | Alice, 12.93% |

Research question: How does adding a duplicate name change from outputting “earliest subject” to “latest subject”?

- Output description
    
    ![Untitled](test_prompt_most_recent_S%20ipynb%20a51ecffd653d4d6c995692f0920be200/Untitled%201.png)
    

<<<

So far, it seems most recent subject (latest) has to use this restricted “subject is” format to provide in-context learning so that it suggests the model to output a subject. Otherwise, “The X is” may tend towards an article. Unless we do “The child is a”

We don’t need to be comprehensive about ALL inputs that get “most recent subject”, but we want to see what are the simplest forms that allow it, then gradually add more to it to try to change it. Generalize on a high level the cases that output it, and hypotheize why they would get “latest” instead of other outputs like “earliest”. This will filter out what we don’t need, finding what’s irrelevant to influencing the output.

If it’s inconsistent such that it doesn’t always output a subject, disregard it, as it can’t be reliably generalized.

<<<

The context of the “description words” don’t matter

"Alice is king. Bob is queen. The lion is Alice. Carol is king. David is queen. The lion is”

Prob: 67.79% Token: | David|

This shows the context of the “description words” don’t matter; lion has nothing to do with king or queen. So don’t test anymore for “content words with external knowledge”.

Still, they do seem to do something because “Alice. Bob. David. Alice. Bob.” doesn’t have as strong as prob for “David” as with descirption words.

Now, try changing up the description words so there’s no induction “mirroring”.

~~The source and target sentences should have the same descriptions~~

"Alice is king. Bob is queen. The lion is Alice. Carol is red. David is lamp. The soldier is”

Top 0th token. Logit: 13.11 Prob:  8.17% Token: | red|
Top 1th token. Logit: 12.75 Prob:  5.66% Token: | the|
Top 2th token. Logit: 12.44 Prob:  4.16% Token: | Alice|
Top 3th token. Logit: 12.11 Prob:  3.00% Token: | David|

So having the “same” words does matter, probably due to induction head patterns needing to recognize previous patterns. Try just using the name, as that perhaps has something to do with duplicate S heads identifying it.

BUT an alternative hypothesis is that “Carol is red” is the culprit. Also, “lion is” vs “soldier is”- perhaps they should be teh same

The to-output phrase is important to output latest subject 

"Alice is king. Bob is queen. Alice. Carol is red. David is queen.”

Top 0th token. Logit: 17.02 Prob:  9.45% Token: | Alice|
Top 1th token. Logit: 16.82 Prob:  7.76% Token: |
|
Top 2th token. Logit: 16.12 Prob:  3.83% Token: | David|
Top 3th token. Logit: 15.91 Prob:  3.11% Token: | Bob|

So "the child is" somehow is an important in-context phrase that influences "latest S" to be chosen. So it's not arbitrary. Try more of these to-output phrases.

"Alice is king. Bob is queen. Alice. Bob. Carol is red. David is queen.”

Top 0th token. Logit: 16.90 Prob: 10.72% Token: | David|
Top 1th token. Logit: 16.65 Prob:  8.34% Token: | Alice|

But it’s only 10%, it’s not a big logit difference. 

Each subject-desc doesn’t have to be the same in source and target

"Alice is king. Bob is queen. The child is Bob. Carol is a teacher. David is a student. The child is”

Prob: 85.66% Token: | David|

“to-output” should have the same description

"Alice is king. Bob is queen. The child is Bob. Carol is a teacher. David is a student. The lion is”

Top 0th token. Logit: 15.86 Prob: 45.14% Token: | a|
Top 1th token. Logit: 13.80 Prob:  5.74% Token: | the|
Top 2th token. Logit: 13.62 Prob:  4.80% Token: | David|

The subject and desc of subj doesn’t matter

"Alice is king. Bob is queen. The child is Bob. David is king. Carol is queen. The child is”

Top 0th token. Logit: 18.69 Prob: 89.58% Token: | Carol|
Top 1th token. Logit: 15.01 Prob:  2.26% Token: | David|

This is rather trivial b/c there’s less subjects to select from.

| "Alice is king. The child is Alice. Carol is queen. The child is” | 75.90% | Carol|
3.04%  | Alice| |
| --- | --- |

- "Alice is king. Carol is queen. The child is”
    
    ![Untitled](test_prompt_most_recent_S%20ipynb%20a51ecffd653d4d6c995692f0920be200/Untitled%202.png)
    

This shows the importance of the to-output phrase.

---

Recall we wanted to investigate:

> A difference of these types of sentences with the ones that predict the earliest subject is that this uses “[Subject] is a [word]. The [word_2] is”, whereas previous ones use “[Word] is subject. [Word_2] is”. Now, is it [outputting latest subject] because the to-output sentence is of
> 
> 
> 1) different format, or 
> 
> 2) because subject or word comes first in the sentence (in-context or to-output), or 
> 
> 3) the [subj-desc] is the same? Or 
> 
> 4) the type of subject matters? 
> 

1) There are cases where the to-output sentence is the same format as the subject-desc sentences, so this is evidence against this hypothesis.

Source 1:

| "The teacher is Alice. The teacher is Bob. The teacher is Bob. The teacher is” | 61.43% Bob
21.15% Alice |
| --- | --- |

Source 2:

| "Alice. Bob. David. Alic. Bob.” | 24.85% |
| --- | --- |

2) In Source 1 above, the subject comes last in each in-context sentence, yet it still outputs the latest subject. So this is also evidence against this hypothesis.

3) The [subj-desc] doesn’t have to be the same in source and target

[https://www.notion.so/wlg1/test_prompt_most_recent_S-ipynb-a51ecffd653d4d6c995692f0920be200?pvs=4#aa9e5c0ae4fe4ab89225c2d13f9687e6](test_prompt_most_recent_S%20ipynb%20a51ecffd653d4d6c995692f0920be200.md)

4) The subject and desc of subj doesn’t matter

| "Alice is king. Bob is queen. The child is Bob. David is king. Carol is queen. The child is” | 89.58% Carol
2.26% David |
| --- | --- |

Here’s a summary of what we believe so far:

- From what we’ve found, the [subject in the] “source sentence” [to-output] doesn’t matter. So “The child is Bob” or “The child is Alice” doesn’t matter. These types of sentences are very sure in outputting “David” (90%) over second place token (<1%).
- The [to-output] doesn’t need to be the same format as the in-context subj-desc, nor does it need subject first
- The [subj-desc] doesn’t have to be the same in source and target
- The context of the “description words” don’t matter
- ~~The source and target sentences should have the same descriptions~~
- The in-context [to-output] phrase is important to output latest subject
- Each subject-desc doesn’t have to be the same in source and target
    - repeated above
- phrase [to-output] should have the same description [in source and target]
- The subject and desc of subj doesn’t matter
    - "Alice is king. Bob is queen. The child is Bob. David is king. Carol is queen. The child is”
    - This is too obvious

Let’s revise that list and give examples of each:

1. **The in-context [to-output] phrase is important to output latest subject. The [to-output] word doesn’t have to be specific**
    - The child is / The lion is
    
    1a) The [to-output] doesn’t need to be the same format as the in-context subj-desc, nor does it need subject first
    
    - The teacher is Bob. The child is / Bob is king. The child is
    
    1b) From what we’ve found, the [subject in the] “source sentence” [to-output] doesn’t matter
    
    - The child is Alice / The child is Bob
    - But shouldn’t contain “target subjects”; only source subjects
    
    1c) phrase [to-output] should have the same description [in source and target]
    
    - The child is…. the child is
2. The [subj-desc] doesn’t have to be the same in source and target; the context of the “description words” don’t matter
    - Alice is king. Bob is queen. The child is Bob. Carol is a teacher. David is a student. The child is
3. If no [to-output], the second way is to have “induction paterns” where target matches source sequence literally
    - Alice. Bob. Bob. Carol. David.
    - "Alice. Bob. David. Alic. Bob.”

We will focus on 1). All 1a), 1b) and 2) is stating is that we can create a varied dataset by varying the subjects in source and target (and their formatting) more, as long as there’s some “to-output” phrase. But WHY do they occur is mysterious and should be investigated within 1). 3) seems to be just “sequence induction patterns”, which is already investigated by the paper that introduced Induction Heads, so we won’t focus on it as much.

Note that this “to-output”phrase is like the [B] to be completed in the induction head paper’s “AB….A”. But it appears to be a specific case of it that focuses on “latest subject”. How does it use induction heads, duplicate heads, name movers, inhibition heads, etc. within its circuits?

1b) is strange because induction wants “similar patterns” (analogous), yet it doesn’t matter which subject in source (ordering, desc-association, etc) is used, just as long as this to-output phrase is there and uses a source subject. It appears by doing so, it triggers something in the circuit to focus on the latest subject, but not the “intermediate one” (Carol). It seems like it’s using some different circuit algorithm than just induction.

2) also shows it doesn’t care about “external knowledge” (eg. semantically relating king with royalty, etc). It’s some circuit pattern, with less focus on MLPs.

However, MLPs may have some role in the general recognition of “subjects”. Investigate this.

---

- Different number of names, varying in source and target
    
    Try more variations with different number of names, varying in source and target (eg. s-3 t-3, or s-2 t-3, etc)
    
    | row |  | Outputs |
    | --- | --- | --- |
    | 1 | "Alice is king. Bob is queen. Paul is prince. The child is Bob. Carol is a teacher. David is a student. The child is” | Top 0th token. Logit: 16.61 Prob: 50.09% Token: | David|
    Top 1th token. Logit: 14.90 Prob: 9.11% Token: | Carol| |
    | 2 | "Alice is king. Bob is queen. Paul is prince. The child is Bob. Carol is a teacher. David is a student. John is a janitor. The child is” | Top 0th token. Logit: 16.85 Prob: 40.96% Token: | John|
    Top 1th token. Logit: 15.92 Prob: 16.11% Token: | David|
    Top 2th token. Logit: 14.54 Prob: 4.06% Token: | Bob| |
    | 3 | "Alice is king. Bob is queen. The child is Bob. Carol is a teacher. David is a student. John is a janitor. The child is” | Top 0th token. Logit: 17.59 Prob: 66.45% Token: | John|
    Top 1th token. Logit: 15.77 Prob: 10.74% Token: | David|
    Top 2th token. Logit: 13.99 Prob: 1.82% Token: | the| |
    | 4 | "Alice is king. Bob is queen. The child is Bob. Carol is a teacher. John is a janitor. David is a student. The child is” | Top 0th token. Logit: 17.74 Prob: 78.83% Token: | David|
    Top 1th token. Logit: 14.46 Prob: 2.95% Token: | John| |
    | 5 | "Alice is king. Bob is queen. Dennis is mouse. Harold is otter. Julie is lamp. Adam is king. The child is Bob. Carol is a teacher. John is a janitor. Mary is mouse. Rol is janitor. Susan is name. David is a student. The child is” | Top 0th token. Logit: 14.44 Prob: 13.01% Token: | Bob|
    Top 1th token. Logit: 13.69 Prob: 6.13% Token: | David|
    Top 2th token. Logit: 13.52 Prob: 5.21% Token: | R| |
    
    In row 1, we see adding a name in the "source", such that (# names source = 3) > (# names target = 2) reduces the output probability.
    
    In row 2, we see adding a name in the "target", such that (# names target = 3) = (# names source = 3), reduces the output probability **AND** still has the "most recent subject" being outputted, this time the subject being the "newly added" one.
    
    Row 3: Just adding a subject to target, such that (# names target = 3) > (# names source = 2), doesn’t reduce top prob as much, but still has the “latest subject” be outputted. ***Whether the top prob is reduced for many cases of this condition, or just for this condition, must still be investigated.***
    
    Row 4: As expected, adding the new name not as the latest subject doesn’t change the old latest from being outputted. 
    
    Row 5: Try a bigger number like 6. Then infer that all between would have the same pattern, as there's no reason they seemingly wouldn't.
    
    Due to several tests, there is good evidence to support the [following](../Questions%20Hypotheses%2087e989748e1942dfa05a7d90433f2e40.md):
    
    - HYPOTHESIS: If the “to-output” pattern is given in the source, in many cases, the high output probability “latest subject” will be outputted compared to the 2nd place output.
    - HYPOTHESIS: However, [this statement](../Questions%20Hypotheses%2087e989748e1942dfa05a7d90433f2e40.md) holds true for fewer subjects; as the number of subjects increases, it is less likely that the “latest subject” will be outputted.
    
    Thus, we will only stick with inputs with 2 or 3 subjects in either source or target. For the sake of preserving length consistent between inputs, we will use 2 subjects in each, and only use single tokens for subject and description.
    
    For the sake of time, we will conclude these test prompts for now and focus on figuring out, using circuit analysis, WHY this statement is true. We will not go further with testing more numbers as by induction, we are guessing these patterns will continue for higher numbers. This may not be true but there is “enough evidence” (in our subjective judgment) that this is likely the case.
    

---

### Ideas for Future Work

- See what happens when add more “to-output” names in source and target
- Automate running many inputs and record their top output. Categorize which subject it is, or if not a subject. Try to find a pattern.
- MLPs may have some role in the general recognition of “subjects”. Investigate this.
- (gen prompt by chatgpt?)