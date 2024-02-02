# Concept Hierarchy Components

(Send this plan over discord, with prelim code for each section)

This is about features in MLPs or residual stream, over attention connections

2/4: study superpos and SAEs

Plan:

1. In at least 2 large models like Llama-2, create datasets (not too long to avoid mem issues) regarding cat vs lion, dog vs wolf, dog vs cat, etc. (animal classes)
2. Find the common activations and features (using SAEs) 

---

If decide to expand on sequence continuation for ACL:

1. Train individual toy models meant for different sequence continuation tasks that aren’t simple memorization, but more natural language (this ensures, unlike GPT-2, they can complete them)
    1. Eg. 2, 4, 6, 8 **VS** 3, 5, 7, 9 (still not “language”)
    2. 
2. To get these toy models in transformerlens, see PQ’s notebooks and ask them for help

OR:

1. Just run existing algorithms on larger models
2. Still, need more “natural language” data. Combine work on greater-than and successsor heads
    1. Llama 2 prompts: “The month after January is…”

Focus on finding heads like 4.4 and 9.1 in multiple models

You don’t have to submit to ACL, send them this place and prelim code and say aim to submit to ArXiV (within 1 month) then submit to NeurIPS (in 3 months)