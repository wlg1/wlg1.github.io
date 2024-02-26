# PsC- Generating Steering Vectors

**Plan on how to learn the algorithm using explr tests**

- Think about how to implement this: “Generate steering vectors by averaging the differences [between positive and negative examples, such as paired sycophantic / non-sycophantic texts] in intermediate residual stream activations after a transformer block”
    - Use invoke() in residual stream output, similar to “Exercise - intervene with h” and “Exercise - replicate the steering vector results”. Start with the code you learned from “calculate_and_apply_steering_vector” and research what’s different.
        - Look at this quote from “2- Related Work”: “Our technique is similar to Activation Addition. However, our steering vectors are generated from a large dataset of hundreds or even thousands of contrast pairs rather than a single pair.”
        - So we just need to take the tensor.mean(dim=0) of all prompts along the batch dim
    - First test on 2 prompts, then 10 prompts
    - What should be the shapes? Each activation is a 1D tensor of size d_model. Figure out how to index these in the context managers.
- Code the pseudocode
    - Think of a data structure format for the first few test samples
        - For the first dataset, the test samples are multiple choice. The difference between pos and neg is just a single answer (A or B)
        - The prompt structure is question + answer
    - What do we index on for the activations? We need to get a single position: the value of A (positive) or B (negative). This determines the model’s choice. So this is likely the last value of the prompt
    - Base this on calculate_h() from 1.5 subsec 2
    - Should we take the mean within each pos and neg group, or the mean of the diffs? It makes more sense to take mean of the diffs obviously because each pos neg prompt is paired with the same question
- Compare the shapes of activation tensors you get from original code with the shapes you get from nnsight saving code. Make sure they’re the same.
    
    

**Pseudocode Outline:**

1. For all the positive prompts,
    1. For each layer we want to take activations from
        1. At the output of a residual stream layer, save the activations to a dictionary mapping layer to activations. Each activation is a 1D tensor of size d_model because they are for a specific batch and specific token position
2. Repeat step 1 for negative prompts
3. Subtract P - N (see equation (1) in paper) and take mean along batches (dim=0)