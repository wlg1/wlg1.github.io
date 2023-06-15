# Main Demo notebook (TransformerLens)

[https://colab.research.google.com/drive/1Jte9lTR05cfwToO-OyoP83R7o2qNQ1UJ#scrollTo=yBShE5-G4YvL](https://colab.research.google.com/drive/1Jte9lTR05cfwToO-OyoP83R7o2qNQ1UJ#scrollTo=yBShE5-G4YvL)

### Introduction

- **`gpt2_cache` (activations)**
    
    This variable will store the cache generated by the model for the input sequence of tokens. The cache is an internal state that the model uses to keep track of information from previous tokens in the sequence, allowing it to generate more accurate predictions as it progresses through the sequence. The cache can be passed back to the model on subsequent calls to improve the model's predictions.
    

**Hooks: Intervening on Activations**

`def head_ablation_hook()` : returns losses after ablating head in a layer

ACTIVATION PATCHING:

Finds the (token, layer) that is important for correct output

`def logits_to_logit_diff():` logit(correct answer) - logit(incorrect answer)

Compare the clean `logits_to_logit_diff` with the corrupted `logits_to_logit_diff`

Clean should be positive b/c correct > incorrect

Corrupted should be neg b/c incorrect > correct

We'll patch in the [residual stream](https://dynalist.io/d/n2ZWtnoYHrU1s4vnFSAQ519J#z=DHp9vZ0h9lA9OCrzG2Y3rrzH) at the start of a specific layer and at a specific position. This will let us see how much the model is using the residual stream at that layer and position to represent the key information for the task.

**Hooks: Accessing Activations**

See how induction heads generalize to repeated sequences