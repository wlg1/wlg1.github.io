# llama2_ablate_prompts_SPcircs.ipynb

### SP numword cont

- uno dos tres
    
    Works:
    
    - 16.0
    - 20.17
    
    Doesn’t work:
    
    - random 1
    - 5.25
- "seis siete ocho”
    
    Works:
    
    - intersect all
    - nums
    - nw
    - months
    
    Doesn’t work:
    
    - random 1
    - 16.0
    - 20.17
    - 5.25
- "enero, febrero, marzo, abril”
    
    Works:
    
    - intersect all
    - nums
    - nw
    - months
    
    Doesn’t:
    
    - random

### SP Arithmetic

- Be concise. What is uno plus cuatro? Answer:
    
    Works:
    
    - intersect all
    - nums
    - nw
    - months
    - random
    
    Doesn’t:
    
- Be concise. What is cinco minus dos? Answer:
    
    Works:
    
    - nums
    - months
    - random
    
    Doesn’t:
    
    - intersect all
    - nw

### SP Months Reasoning

- **What are the months in a year in Spanish?**
    
    Works:
    
    - nums
    - nw
    - months
    
    Doesn’t:
    
    - intersect all
    - random
- Be concise. List the months in Spanish. Answer:
    
    Works:
    
    - months
    
    Doesn’t:
    
    - intersect all
    - nums
    - nw
    - random