# Transformer NLP Style Editing

[Read papers + code about how transformers were edited ](Transformer%20NLP%20Style%20Editing%2089f0ac65415e4976bc3abe7ec8fec35c/Read%20papers%20+%20code%20about%20how%20transformers%20were%20edi%20204357b85f0b4e8a858502319e6f9f15.md)

[Brainstorm how to apply methods to edit transformer styles](Transformer%20NLP%20Style%20Editing%2089f0ac65415e4976bc3abe7ec8fec35c/Brainstorm%20how%20to%20apply%20methods%20to%20edit%20transforme%20e8ac10fbd3b549d79f44cfd06a609dec.md)

[Study existing implementations of  fine-tuning](Transformer%20NLP%20Style%20Editing%2089f0ac65415e4976bc3abe7ec8fec35c/Study%20existing%20implementations%20of%20fine-tuning%20a696395c83c24b7daa804db20dd9f50b.md)

[Edit a collection of style’s (s,r,…) using ROME, MEMIT](Transformer%20NLP%20Style%20Editing%2089f0ac65415e4976bc3abe7ec8fec35c/Edit%20a%20collection%20of%20style%E2%80%99s%20(s,r,%E2%80%A6)%20using%20ROME,%20M%20655f558c453c4f1599b0674505036064.md)

[ISSUE: GPT-2-XL is bad at writing in styles, and GPT-J too big to load](Transformer%20NLP%20Style%20Editing%2089f0ac65415e4976bc3abe7ec8fec35c/ISSUE%20GPT-2-XL%20is%20bad%20at%20writing%20in%20styles,%20and%20GP%20ce645a11c51f43b3b8c577e86c66c998.md)

### Future Work

Modify the loss function to penalize associating an input descirption with {a collection style words and the hierarchical relational syntax they’re put together in}

look at ‘erasure SD’ code for ideas

[Study ‘Erasing Concepts from Diffusion Models’ code for ideas](Transformer%20NLP%20Style%20Editing%2089f0ac65415e4976bc3abe7ec8fec35c/Study%20%E2%80%98Erasing%20Concepts%20from%20Diffusion%20Models%E2%80%99%20cod%20ffc34b804ba2484b9b61a35b5e441eba.md)

use search engine + chatgpt to search through pdfs for related work on modifying transformer loss (may require multiple hierarchical user prompts to double check each pdf)

### Challenges

This is not trivial because the style may not be a “direction”. What brings together this entire collection of “frequently used words, the order of words, etc” into a [style]? It’s not just using associated word(s), but semantically understanding that something is [exaggerated] or [sad]. These were not classes the model was explictly trained on.