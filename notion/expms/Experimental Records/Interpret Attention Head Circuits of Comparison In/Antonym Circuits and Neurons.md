# Antonym Circuits and Neurons

simple_analogies_circuits, pt3.ipynb

[https://colab.research.google.com/drive/1GQo_RSEY40ncByvwy81kxwSKGPHlbxSx?usp=sharing#scrollTo=RMUGxbOrI40i](https://colab.research.google.com/drive/1GQo_RSEY40ncByvwy81kxwSKGPHlbxSx?usp=sharing#scrollTo=RMUGxbOrI40i)

antonym_heads.ipynb

[https://colab.research.google.com/drive/1TXi0A-TNXYr748Z23kpDw2YEHGjafOUO#scrollTo=u0pjmJZfIAiI](https://colab.research.google.com/drive/1TXi0A-TNXYr748Z23kpDw2YEHGjafOUO#scrollTo=u0pjmJZfIAiI)

We hypothesize this algorithm for finding antonyms roughly breaks down into:

1. Identify what are the adjectives and "is"
2. Predict the opposite 

The heads will probably compete with other heads, such as those trying to output:

- The most same adjective
- A similar adjective

What influences which one gets the highest logit score? How does in-context learning infuence this (# of examples, similarity of structure, etc)?

Auto output the impt heads based on their score on heatmap

H14, L30 could potentially be important. See what affects it

---

Copy Scores

[https://colab.research.google.com/drive/1cFJc2Zc1fh_BXV42q3h4zfvRikINE_Mo#scrollTo=X2SjICJ64uuN&line=25&uniqifier=1](https://colab.research.google.com/drive/1cFJc2Zc1fh_BXV42q3h4zfvRikINE_Mo#scrollTo=X2SjICJ64uuN&line=25&uniqifier=1)

This figures out what the head is doing

To use it, need layer, head, model, and dataset

The provided Python code block is meant to evaluate how accurately the model can copy certain elements from the input to the output.

The predicted tokens are then compared to the corresponding target tokens in the **`ioi_dataset`**. If the target token is found in the predicted tokens, **`n_right`** (the number of correct predictions) is incremented.

In our case, the target token is the correct adjective. If the head copies the adjective, it is an “Adjective Mover”. Hypothesize these exists and check if any heads have this behavior

- Two types of prompts: one that copies the same adjective (tall), and another which gives the antonym (short). See which heads do which for these prompts.
- John is tall. Dylan is tall. Mary is
    - Induction heads due to previous examples? Somehow these give more weight to the copying heads?
- John is tall. Mary is
    - Also induction heads, but somehow these give less weights to the copying heads vs the “antonym” heads?
- Candidate heads: check and auto put sigf heads into ‘copy score’ and ‘path patch’
    - 1) logit lens for heads: [https://colab.research.google.com/drive/1GQo_RSEY40ncByvwy81kxwSKGPHlbxSx#scrollTo=h5Z-XCXbTuqV&line=3&uniqifier=1](https://colab.research.google.com/drive/1GQo_RSEY40ncByvwy81kxwSKGPHlbxSx#scrollTo=h5Z-XCXbTuqV&line=3&uniqifier=1)
    - 2) attention patterns (top heads):
        
        [https://colab.research.google.com/drive/1GQo_RSEY40ncByvwy81kxwSKGPHlbxSx#scrollTo=M59tohQZUF0x](https://colab.research.google.com/drive/1GQo_RSEY40ncByvwy81kxwSKGPHlbxSx#scrollTo=M59tohQZUF0x)
        

---

gradually add more to new dataset to run path patching and copy scores
look at code in transformerlens
tall_short_circuit.ipynb
- alter dataset clean, corrupted dataset, circuit, layer_heads
what do the outputs mean?

figure out how to get same prompt names but flip adjective to antonym

[https://github.com/redwoodresearch/Easy-Transformer/blob/main/easy_transformer/ioi_dataset.py](https://github.com/redwoodresearch/Easy-Transformer/blob/main/easy_transformer/ioi_dataset.py)

def gen_flipped_prompts(prompts, names, flip=("S2", "IO")):

- modify "get flipped prompts" to flip an adjective to a given antonym input instead, for a sentence such as "John is tall. Mary is" into "John is short. Mary is". don't switch IO and S
    
    ```python
    def gen_flipped_prompts(prompts, names, templates, flip=("S2", "IO"), antonyms=None):
        flipped_prompts = []
    
        for prompt in prompts:
            t = prompt["text"].split(" ")
            prompt = prompt.copy()
            
            if flip[0] == "ADJ":
                if flip[1] == "ANTONYM":
                    adjective = prompt["A"]
                    antonym = antonyms[adjective]
                    t[t.index(adjective)] = antonym
                    prompt["A"] = antonym
                else:
                    raise ValueError("Invalid flip[1] value")
    
            elif flip[0] == "S2":
                # Existing code for flipping S2
                # ...
    
            elif flip[0] == "IO":
                # Existing code for flipping IO
                # ...
            
            # Existing code for other flip cases
            # ...
    
            if "IO" in prompt:
                prompt["text"] = " ".join(t)
                flipped_prompts.append(prompt)
            else:
                flipped_prompts.append(
                    {
                        "A": prompt["A"],
                        "B": prompt["B"],
                        "C": prompt["C"],
                        "text": " ".join(t),
                    }
                )
    
        return flipped_prompts
    ```