# Path Patching

Folder: [https://drive.google.com/drive/folders/1x0pWudpR1eYJi4IRo3VsUidwwrSG2_eq](https://drive.google.com/drive/folders/1x0pWudpR1eYJi4IRo3VsUidwwrSG2_eq)

---

[https://arena-ch1-transformers.streamlit.app/[1.3]_Indirect_Object_Identification](https://arena-ch1-transformers.streamlit.app/%5B1.3%5D_Indirect_Object_Identification)

Firstly, what dataset should we use for patching? In the previous section we just flipped the subject and indirect object tokens around, which meant the direction of the signal was flipped around. However, what we'll be doing here is a bit more principled - rather than flipping the IOI signal, we'll be erasing it. We do this by constructing a new dataset from `ioi_dataset` which replaces every name with a different random name. This way, the sentence structure stays the same, but all information related to the actual indirect object identification task (i.e. the identities and positions of repeated names) has been erased.

Sentence structure ~ Sequence structure

identities and positions of repeated names ~ identities of seq digits (???)

For instance, given the sentence `"When John and Mary went to the shops, John gave the bag to Mary"`, the corresponding sentence in the ABC dataset might be `"When Edward and Laura went to the shops, Adam gave the bag to Mary"`. We would expect the residual stream for the latter prompt to carry no token or positional information which could help it solve the IOI task (i.e. favouring `Mary` over `John`, or favouring the 2nd token over the 4th token).

We define this dataset below. Note the syntax of the `gen_flipped_prompts` method - the letters tell us how to replace the names in the sequence. For instance, `ABB->XYZ` tells us to take sentences of the form `"When Mary and John went to the store, John gave a drink to Mary"` with `"When [X] and [Y] went to the store, [Z] gave a drink to Mary"` for 3 independent randomly chosen names `[X]`, `[Y]` and `[Z]`. We'll use this function more in the bonus section, when we're trying to disentangle positional and token signals (since we can also do fun things like `ABB->BAB` to swap the first two names, etc).

Note that we're always measuring performance ***with respect to the correct answers for the IOI dataset, not the ABC dataset***, because we want our ABC dataset to carry no information that helps with the IOI task (hence patching it in gives us signals which are totally uncorrelated with the correct answer). For instance, the model will obviously not complete sentences like `"When Max and Victoria got a snack at the store, Clark decided to give it to"` with the name `"Tyler"`.

[https://chat.openai.com/c/3aa91ef6-aab3-42ae-aa43-83b8c37e2fde](https://chat.openai.com/c/3aa91ef6-aab3-42ae-aa43-83b8c37e2fde)

Read and understand this:…

Now, instead of corrupting subjects, we want to corrupt sequences like “1 2 3 4” or “four five six”. How would we go about corrupting them in a similar way, as to preserve certain information while erasing others?

- Ideas
    
    When it comes to corrupting numerical sequences in a manner analogous to what was done with subjects (like names), the main goal remains consistent: we want to modify the sequences in such a way that they maintain their general structure but lose specific identifying information. Here's how you can do this for numerical sequences:
    
    1. **Decide on Information to Preserve**: Before corrupting the sequences, determine what you want to preserve. For example, do you want to maintain sequence length? Relative ordering? Absolute values?
    2. **Random Replacement**: Replace individual numbers with other random numbers. This would be analogous to the random name replacement.
        - Original Sequence: “1 2 3 4”
        - Corrupted Sequence: “5 6 7 8”
    3. **Shuffling**: Change the order of numbers within the sequence.
        - Original Sequence: “1 2 3 4”
        - Corrupted Sequence: “3 1 4 2”
    4. **Number-to-Word & Word-to-Number Conversion**: Similar to the random name replacement, replace numbers with their word forms and vice versa.
        - Original Sequence: “1 2 three 4”
        - Corrupted Sequence: “one two 3 four”
    5. **Mapping Sequences**: Create a consistent mapping of sequences. For instance, all sequences starting with “1” might be replaced by sequences starting with “5”, but the rest of the sequence maintains its structure.
        - Original Sequence: “1 2 3 4”
        - Corrupted Sequence: “5 6 7 8”
    6. **Use Placeholder Tokens**: Insert random tokens (placeholders) to disrupt the sequence while maintaining length.
        - Original Sequence: “1 2 3 4”
        - Corrupted Sequence: “1 X 3 Y”
    7. **Consistent Transformations**: Apply mathematical transformations consistently across sequences. For instance, add 2 to every number in the sequence. This maintains relative differences but changes absolute values.
        - Original Sequence: “1 2 3 4”
        - Corrupted Sequence: “3 4 5 6”
    8. **Length Preservation**: Regardless of the corruption method, if preserving the length of sequences is important, ensure the corrupted sequence maintains the same number of elements.
    
    Remember that the specific method you choose should align with the goals of your experiment or task. For instance, if you're testing a model's ability to understand relative differences between numbers, the consistent transformations method might be most appropriate. On the other hand, if you want to see if the model can handle missing data or disruptions, the placeholder method might be best.
    

Test several of these corruptions and see if you get the same results; if not, how different are they?

[https://colab.research.google.com/drive/1UQZrumDk5gEWuIlb4nZWRms8gbFf4z-w#scrollTo=4DZ2SGhfl6mW](https://colab.research.google.com/drive/1UQZrumDk5gEWuIlb4nZWRms8gbFf4z-w#scrollTo=4DZ2SGhfl6mW)

numseq_path_patch_repeatLast.ipynb

[https://colab.research.google.com/drive/1MfpvNd_Hgz4jvHVoOlSeqkpDMRNInXwH#scrollTo=gW5aQcIX4e42](https://colab.research.google.com/drive/1MfpvNd_Hgz4jvHVoOlSeqkpDMRNInXwH#scrollTo=gW5aQcIX4e42)

numseq_path_patch_repeatAll.ipynb

numseq_path_patch_repeatLast.ipynb

![Untitled](Path%20Patching%20967be4e1a2b241418a9603911dda4561/Untitled.png)

![Untitled](Path%20Patching%20967be4e1a2b241418a9603911dda4561/Untitled%201.png)

![Untitled](Path%20Patching%20967be4e1a2b241418a9603911dda4561/Untitled%202.png)

numseq_path_patch_repeatAll.ipynb

![Untitled](Path%20Patching%20967be4e1a2b241418a9603911dda4561/Untitled%203.png)

![Untitled](Path%20Patching%20967be4e1a2b241418a9603911dda4561/Untitled%204.png)

![Untitled](Path%20Patching%20967be4e1a2b241418a9603911dda4561/Untitled%205.png)

The strongest patterns are still the same, but “repeat all” has stronger differences. Some heads in “repeat all” don’t appear in “repeat last”. This is because “1 1 1 1” predicts “2” instead of “5”, which is far off from “1 2 3 3” predicting “4” instead of “5”. “Repeat all” may be too extreme, so don’t use it.

<<<

Compare with swapping, random #s, and +1 to all, instead of repeat

[https://colab.research.google.com/drive/1YAAIW3mY6Y9xarDF1iIW_Uw-QMWpANiR#scrollTo=gW5aQcIX4e42](https://colab.research.google.com/drive/1YAAIW3mY6Y9xarDF1iIW_Uw-QMWpANiR#scrollTo=gW5aQcIX4e42)

numseq_path_patch_switchLast.ipynb

![Untitled](Path%20Patching%20967be4e1a2b241418a9603911dda4561/Untitled%206.png)

Largely the same as “repeat last”, but for 9.1, 5.5 doesn’t appear, and 4.10 does. Perhaps because the “sequence pattern” was broken, so the induction isn’t recognized?

![Untitled](Path%20Patching%20967be4e1a2b241418a9603911dda4561/Untitled%207.png)

---

Types of corruption:

- all repeats (1 1 1 1)
- just repeat second last digit (1 2 3 3)

---

Corrupt “Adam is 1…”