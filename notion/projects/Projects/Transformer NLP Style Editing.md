# Transformer NLP Style Editing

[Read papers + code about how transformers were edited ](Transformer%20NLP%20Style%20Editing%20d413b09bf00a4516886ff16dc26c65f4/Read%20papers%20+%20code%20about%20how%20transformers%20were%20edi%206f6d350b0ccd4c859d2bcd22abfd6c44.md)

[Brainstorm how to apply methods to edit transformer styles](Transformer%20NLP%20Style%20Editing%20d413b09bf00a4516886ff16dc26c65f4/Brainstorm%20how%20to%20apply%20methods%20to%20edit%20transforme%204280abcda7a246d6afeda0bda4ac5df4.md)

[Study existing implementations of  fine-tuning](Transformer%20NLP%20Style%20Editing%20d413b09bf00a4516886ff16dc26c65f4/Study%20existing%20implementations%20of%20fine-tuning%20da553b84e64840b1bbdd9105bcf57840.md)

[Edit a collection of style’s (s,r,…) using ROME, MEMIT](Transformer%20NLP%20Style%20Editing%20d413b09bf00a4516886ff16dc26c65f4/Edit%20a%20collection%20of%20style%E2%80%99s%20(s,r,%E2%80%A6)%20using%20ROME,%20M%20647ebe7cfbb04b748e5bc799caf45f1a.md)

[ISSUE: GPT-2-XL is bad at writing in styles, and GPT-J too big to load](Transformer%20NLP%20Style%20Editing%20d413b09bf00a4516886ff16dc26c65f4/ISSUE%20GPT-2-XL%20is%20bad%20at%20writing%20in%20styles,%20and%20GP%20c39db252454747ac9fc78d61b038de79.md)

### Future Work

Modify the loss function to penalize associating an input descirption with {a collection style words and the hierarchical relational syntax they’re put together in}

look at ‘erasure SD’ code for ideas

[Study ‘Erasing Concepts from Diffusion Models’ code for ideas](Transformer%20NLP%20Style%20Editing%20d413b09bf00a4516886ff16dc26c65f4/Study%20%E2%80%98Erasing%20Concepts%20from%20Diffusion%20Models%E2%80%99%20cod%20ed15e0fe8e884bde91ea08128200e1ac.md)

use search engine + chatgpt to search through pdfs for related work on modifying transformer loss (may require multiple hierarchical user prompts to double check each pdf)

### Challenges

This is not trivial because the style may not be a “direction”. What brings together this entire collection of “frequently used words, the order of words, etc” into a [style]? It’s not just using associated word(s), but semantically understanding that something is [exaggerated] or [sad]. These were not classes the model was explictly trained on.