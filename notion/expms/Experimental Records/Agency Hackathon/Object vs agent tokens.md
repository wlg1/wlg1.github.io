# Object vs agent tokens

Object tokens vs animal/human/other tokens- does it ever say an object does a living_being-like action?

- obj_vs_subj_circuit_expms.ipynb
    
    [https://colab.research.google.com/drive/1H9U30b0eoViouqQtrV9GJ4j-iBpUdWgl#scrollTo=zfslsJs9SxGE&line=3&uniqifier=1](https://colab.research.google.com/drive/1H9U30b0eoViouqQtrV9GJ4j-iBpUdWgl#scrollTo=zfslsJs9SxGE&line=3&uniqifier=1)
    
    "After lamp and desk went to the store, lamp gave a bottle of milk to”
    
    NO! Unlike John/Mary, or Alice/Bob, it doesn’t say “desk”. If you try this again with house/shoe, it also won’t work. It explicitly knows the “pattern” what are “names”. This is likely because in training data, 
    
    Try lower case (first letter) names
    
    still works, but a little worse
    
    Try upper case objects
    
    actually works better. this may be because some people’s last names are House; in general, upper case of anything may signify “name”
    
    red and Shoe- just caps one doesn’t work
    
    Try animals- both lower and upper case first letter
    
    lower case lion/cat: lion in 9th, much better than objs which were in 2000s
    
    Lion/Cat- now Lion is in first
    
    so upper case matters A LOT.
    

Clean: upper case Lion/Cat

Corrupted: lower case lion/cat

10.7 seems to matter a lot

---

Test this against GPT-3.5. You can likely tell chatgpt to do both ways, which involves knowing the pattern vs knowing the meaning of the pattern.

cluster names vs everything else

cluster names vs animals

---

Take small steps, small modifs, of existing

[Towards Automated Circuit Discovery for Mechanistic Interpretability](https://www.notion.so/Towards-Automated-Circuit-Discovery-for-Mechanistic-Interpretability-e22fd1e2478347ea9686424d6080b5b7?pvs=21) 

16m30s- is that part SPECIFIC to ioi, or the prompt structure in general? To know specifics, keep general structure but specifically replace ioi with ABC.
*We can test this too with subjects vs non subjects!!!

---

Find heads that activate for (or attend to) Names 

AND find heads that activate for (or attend to) Objects (pen, ball, lamp, etc.)

John gave Mary the

Do this separately at first and see if there are common components

- What's a sentence template that will focus on outputting (for the next word) an object from the previous part of the sentence, but not a subject? For instance, a sentence template that will output (for the next word) a subject from the previous of the sentence is “When John and Mary went to the store, John gave a toy to” because it will output “Mary” as the next word, and not an object because you don’t give the object something. Do the same but for an object. Subjects are defined as living beings, while objects are not.
    
    [https://chat.openai.com/c/99dfaaa8-17c9-4a0e-a3e0-3e1ad1a24ad5](https://chat.openai.com/c/99dfaaa8-17c9-4a0e-a3e0-3e1ad1a24ad5)
    
    - Include both an object and a subject in the previous part of the sentence, so as to pick the object over the subject
        
        In that case, you could use a sentence template like:
        
        "While Sarah was reading, she put her coffee cup on the table next to the."
        
        In this sentence, "Sarah" is the subject (living being), and "coffee cup" and "table" are objects (non-living things). The way the sentence is structured makes it more likely that the next word would be "table," which is an object, rather than "Sarah," which is the subject.
        
    
    [https://colab.research.google.com/drive/1Zy0ZjYaHGjoAzhlZSKG8v3RrOU0ht4TM#scrollTo=WsWigp7JosXX&line=3&uniqifier=1](https://colab.research.google.com/drive/1Zy0ZjYaHGjoAzhlZSKG8v3RrOU0ht4TM#scrollTo=WsWigp7JosXX&line=3&uniqifier=1)
    
    "While Sarah was reading near a lamp, John put a toy on the table next to the”
    
    Token “the” indicates object over subject
    
    ISSUE: removing “the” changes sentence length. If we add in more words, that may shift positions of our impt tokens (Sarah, lamp, John), so we shouldn’t add in when it shifts their position. But it may be okay to shift the unimportant positions?
    
    "While Sarah was near a lamp, John put a toy on the table next to the”
    
    lamp
    
    "While Sarah was near a lamp, John put a big toy on the table next to”
    
    her
    
    Subjects do things that objects cannot do. 
    
    “Sarah is alive. A lion is alive.”
    
    “Question: Is Sarah alive? Answer: yes. Question: Is a lamp alive? Answer:”
    
    [https://colab.research.google.com/drive/1Zy0ZjYaHGjoAzhlZSKG8v3RrOU0ht4TM#scrollTo=UWyox3oSrMs7&line=2&uniqifier=1](https://colab.research.google.com/drive/1Zy0ZjYaHGjoAzhlZSKG8v3RrOU0ht4TM#scrollTo=UWyox3oSrMs7&line=2&uniqifier=1)
    
    It says “yes”, indicating it doesn’t understand this.
    

object_attn_test_prompts.ipynb

[https://colab.research.google.com/drive/1Zy0ZjYaHGjoAzhlZSKG8v3RrOU0ht4TM#scrollTo=lrzgZVvBWKxW](https://colab.research.google.com/drive/1Zy0ZjYaHGjoAzhlZSKG8v3RrOU0ht4TM#scrollTo=lrzgZVvBWKxW)

**try to choose obj over subj: "While Sarah was reading near a lamp, John put a toy on the table next to the”**

ANSWER: lamp

- Replacing “a lamp” with “the Adam” causes “adam”  to be chosen
- Replacing “a lamp” with “a Adam” puts Adam up higher, but doesn’t cause it to be chosen
    - so it still depends on position
- Replacing “the” with another “to” causes “her” to be chosen
    - this is the same as removing “the”. But we repeat it instead of removing because the activation patching functions in this library require the clean and corrupted prompts to have the same number of tokens, and aligning the same tokens (aside from the clean to corrupted tokens) in the same positions.
    - HYPOTHESIS: GPT-2 Small recognizes objects using “the”

---

Subj expms:

[https://colab.research.google.com/drive/1rNi9D2kgCb7RAYekM3qlPTo7GjB5estA](https://colab.research.google.com/drive/1rNi9D2kgCb7RAYekM3qlPTo7GjB5estA)

Obj expms:

[https://colab.research.google.com/drive/1zswsmCywMxZzhJUkQ823v2jbKcv_Wl7N](https://colab.research.google.com/drive/1zswsmCywMxZzhJUkQ823v2jbKcv_Wl7N)

replace by “"While Sarah was near a lamp, John put a big toy on the table next to”

Differing heads (by DLA): obj has 10.11

Differing heads (by actv patch): obj has 10.0, but only 6%

obj expms has strange layer activation patching results that don’t show transfer of “lamp” to the end word, and end word (the) has all blue. This may be due to differing word positions. So see, in acdc paper (a survey of previous circuits) how they corrupted their prompts to get more ideas on what’s allowed vs not allowed.

---

obj_expms_v2.ipynb

[https://colab.research.google.com/drive/1YDtzTKZ8dUa8319ajCbOPFStZS4xt-zb#scrollTo=DcZG9rm2IAiA](https://colab.research.google.com/drive/1YDtzTKZ8dUa8319ajCbOPFStZS4xt-zb#scrollTo=DcZG9rm2IAiA)

Replace 'the' with 'to'

same results as before

---

obj_expms_v3.ipynb

[https://colab.research.google.com/drive/1j6TYHDKJ41SuizyhD2UOBuxlRaTUMt0_#scrollTo=m90WRkxYIAiL](https://colab.research.google.com/drive/1j6TYHDKJ41SuizyhD2UOBuxlRaTUMt0_#scrollTo=m90WRkxYIAiL)

"When John and lamp went to the store, Mary gave a toy to” —> John

- (john, Lamp) → 0th them, 1st John
- (john, lamp) → 0th them, 3rd john, 4th John
- (john, Lamp) → 0th them, 1st John
- (John, Lamp) → 0th John, 7th Lamp

"When John and Lamp went to the store, John gave a toy to” —> Lamp

- Then because of ‘removing duplicates’ it chooses Lamp over John

- (lamp) → lamp in 145th
- (Lamp) → Lamp in 6th

Even if not in first, that’s a big jump up

"When Adam sat on the couch, Mary gave a toy to” —> him

- "When couch sat on the Adam, Mary gave a toy to”  —> the
    - (Adam still over couch in ranking)

This shows that the model is not basing on who is doing what action, or “the”, or capitals, but on previous patterns ingrained in it. 

- (table, lamp)

---

****How does GPT-2 compute greater-than****

[https://arxiv.org/abs/2305.00586](https://arxiv.org/abs/2305.00586)

we create the “01-dataset”: we take each example in the original dataset and replace the last two digits YY of the start year with “01”.