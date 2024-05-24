# Exploratory Analysis Demo

[https://colab.research.google.com/drive/1nD6tfM33StbAqXG5HnYPlC40hKSj8mzD](https://colab.research.google.com/drive/1nD6tfM33StbAqXG5HnYPlC40hKSj8mzD)

- Why would a tokenizer use .cuda()? Why does it need a GPU?
    
    Tokenization can be a computationally expensive task, especially when working with large datasets. By using a GPU, the tokenizer can process data in batches in parallel, which can significantly speed up the tokenization process. 
    
    In PyTorch, `.cuda()` is a method that moves a tensor (or a model) from the CPU to the GPU. When a tokenizer uses `.cuda()`, it is essentially moving the tokenizer to the GPU to take advantage of the parallel processing power of the GPU.
    

## **Introduction**

### **Indirect Object Identification**

[https://www.grammarly.com/grammar](https://www.grammarly.com/grammar)

Indirect object: the receiver (of the direct object)

Direct object: what’s being received 

`names` : the first object in (A,B) is the indirect object 

**logit difference**, the difference in logit between the indirect object's name and the subject's name (eg, `logit(Mary)-logit(John)`).

### D**irect logit attribution**

> `logits=Unembed(LayerNorm(final_residual_stream))`. The Unembed is a linear map, and LayerNorm is approximately a linear map, so we can decompose the logits into the sum of the contributions of each component, and look at which components contribute the most to the logit of the correct token.
….
Getting an output logit is equivalent to projecting onto a direction in the residual stream.
…
Further, the metric helps us isolate the precise capability we care about - figuring out which name is the Indirect Object. There are many other components of the task - deciding whether to return an article (the) or pronoun (her) or name, realising that the sentence wants a person next at all, etc. By taking the logit difference we control for all of that.
> 
- How is Direct logit attribution different than getting the logit differences between two token outputs?
    
    [ first, give it the description of DLA]
    
    When we calculate the logit differences between two token outputs, we take the difference between the logit values of two different tokens in the output sequence.
    
    In contrast, direct logit attribution aims to understand the contribution of each component in the model to the final logit value for a specific token in the output sequence. 
    

To look at “which contributes the most”, look at which has the “largest projection in the direction of that component (of the residual stream)”. This is because projection on component direction measures “how much component there is in the logits”, or “how much component contributes to logits”.

(Similarly, projection on logit direction measures “how much logit contributes to component”.)

This is the matrix of ALL the component (vectors): [number of prompt inputs, vocab size]

One component vector is: [vocab size] - that is, how much each token contributes to logits

One can also measure linear comibnations of these component vectors

---

`log_probs == logits.log_softmax(dim=-1) == logits - logsumexp(logits)`

![Untitled](Exploratory%20Analysis%20Demo%20c61288d8f11b45d993c796ec28a62132/Untitled.png)

log(e^x) = x

log(a/b) = log(a) - log(b)

---

```python
answer_residual_directions = model.tokens_to_residual_directions(answer_tokens)
print("Answer residual directions shape:", answer_residual_directions.shape)
logit_diff_directions = answer_residual_directions[:, 0] - answer_residual_directions[:, 1]
print("Logit difference directions shape:", logit_diff_directions.shape)
```

- Explanation
    
    This code applies a language model's `tokens_to_residual_directions` method to the answer tokens generated earlier, to obtain the residual directions for each answer.
    
    The residual directions represent the change in the model's output probabilities when each token is added to the input sequence. The `tokens_to_residual_directions` method calculates the residual directions for a set of tokens, relative to a given context.
    
    The code then calculates the logit difference directions by subtracting the residual direction corresponding to the incorrect answer from the residual direction corresponding to the correct answer. This gives a vector that represents the direction of the change in output probabilities between the correct and incorrect answers.
    
    ![Untitled](Exploratory%20Analysis%20Demo%20c61288d8f11b45d993c796ec28a62132/Untitled%201.png)
    
    [ - is on VECTOR head, “incorrect” ]
    
    The shape of `answer_residual_directions` will be (num_answers, seq_len, hidden_size), where `num_answers` is the number of answer tokens (equal to the length of `answer_tokens`), `seq_len` is the length of the input sequence, and `hidden_size` is the size of the hidden layer in the language model. The shape of `logit_diff_directions` will be (num_answers, hidden_size), as this represents the difference in residual directions between the correct and incorrect answers for each prompt.
    
    The “input sequence length” disappears because each `logit_diff_directions` is not for each token in the sequence, but for an entire sequence
    

[number of prompt inputs, positions, vocab size]

`logit_diff_directions = answer_residual_directions[:, 0] - answer_residual_directions[:, 1]`

[**Sum over an index**](../Neural%20Networks%20e6abb23474464e098117dced189fb7bb/Tensor%205555c4af00994d9fb9a8b7e90d5b18de/Sum%20over%20an%20index%208e5f325c799447948ab6fc98514a56ea.md) 

Subtract column 0 and col 1 to get:

`Logit difference directions shape: torch.Size([8, 768])`

8 rows, 1 column, 768 “depth” —> 8 rows, 768 columns

**Logit Lens**

[https://www.alignmentforum.org/posts/AcKRB8wDpdaN6v6ru/interpreting-gpt-the-logit-lens](https://www.alignmentforum.org/posts/AcKRB8wDpdaN6v6ru/interpreting-gpt-the-logit-lens)

What about the 1600-dim vectors produced in the middle of the network, say the output of the 12th layer or the 33rd? If we convert them to vocab space, do the results make sense? The answer is ***yes***.

**logits**

Diagram bottom of col: input

Diagram top of col: CORRECT output

Rows: layers. Top guess for each (in token, layer) is in each cell.

Look at each column from bottom to top to see how the guess evolves all the way to the final guess. If the top row, the last layer, is different from the correct answer above the top row, there is no *.

Because the next input comes from the previous output, the bottom at i comes from the top at i-1

<<<

Transformer block: contains layers, including an attention head and an MLP

Residual component: the difference between the input and the output of a block.

Residual stack: sequence of residual components

- **`residual_stack_to_logit_diff`** [QUESTIONABLE]
    
    The **`residual_stack_to_logit_diff`** function takes as input a stack of residual components (**`residual_stack`**) and an **`ActivationCache`** object (**`cache`**) and returns a scalar value that represents the average logit difference between the original logits and the logits generated by the transformer model.
    
    The **`einsum`** function calculates the dot product between the **`scaled_residual_stack`** tensor and **`logit_diff_directions`**, which is a tensor of the same shape as the output of the transformer model and represents the difference between the original logits and the logits generated by the model.
    
    The purpose of taking the dot product is to measure the similarity between the scaled residual stack and the logit difference directions. If the dot product is large and positive, it suggests that the changes in the residual stack are aligned with the changes in the logits, indicating that the transformer model is doing a good job of capturing the important features of the input. (???)
    
    The resulting tensor is divided by the number of prompts (**`len(prompts)`**) to obtain the average logit difference. This value represents the extent to which the transformer model has changed the original logits, on average, across all prompts. A higher value indicates that the model has made more significant changes to the original logits, while a lower value indicates that the model has preserved more of the original logits.
    
- **`accumulated_residual`**
    
    The accumulated residual stream represents the cumulative difference between the input and the output of the final layer of the transformer model. It is obtained by summing the residual tensors across all layers from the input to the final layer. The `incl_mid=True` parameter includes the intermediate residual tensors in the sum, while `pos_slice=-1` parameter selects the final token of each input sequence for each residual tensor. The resulting tensor has shape `(batch_size, hidden_size)`.
    
    The resulting **`x`** array contains **`model.cfg.n_layers+1`** evenly spaced values that correspond to each layer of the transformer model (from 0 to **`model.cfg.n_layers`**) as well as an additional value for the accumulated residual stream. Each value on the x-axis represents the index of a layer or the accumulated residual stream
    

<<<

**Layer Attribution** is different from “Logit Lens” because Logit Lens looks at the ACCUMULATED RESIDUAL STREAM (1, 3, 5), whereas LA is not the accumulation, but just each layer (1, 1, 1)

### Activation Patching

- One natural thing to patch in is the residual stream at a specific layer and specific position. For example, the model is likely intitially doing some processing on the second subject token to realise that it's a duplicate, but then uses attention to move that information to the " to" token. So patching in the residual stream at the " to" token will likely matter a lot in later layers but not at all in early layers.
    
    GUESS of this meaning:
    
    ![Untitled](Exploratory%20Analysis%20Demo%20c61288d8f11b45d993c796ec28a62132/Untitled%202.png)
    
- **`patch_residual_component`**
    
    replaces the corrupted residual component at the given position with the corresponding value from the clean cache and returns the updated residual component.
    
- `hook_fn = partial(patch_residual_component, pos=position, clean_cache=cache)`
    
    This line of code defines a hook function `hook_fn` using the `partial()` function from the `functools` module.
    
    The `patch_residual_component` function is passed as the first argument to `partial()`, which means that `hook_fn` will be a partially applied version of `patch_residual_component` with two of its arguments already fixed: `pos=position` and `clean_cache=cache`. This means that when `hook_fn` is called later in the program, it will only need to be passed a single argument: `corrupted_residual_component`. The `pos` and `clean_cache` arguments will be automatically filled in with the values `position` and `cache`, respectively.
    
    The purpose of `hook_fn` is to patch the residual component of a transformer layer at a given position, by replacing the corrupted value with the corresponding clean value from the cache. This is achieved by calling `patch_residual_component` with the `corrupted_residual_component` argument (which is passed automatically by the model during the forward pass), and with the `pos` and `clean_cache` arguments fixed to the values `position` and `cache`, respectively. The resulting partially applied function is then returned by `hook_fn`, and will be used as a hook function during the forward pass of the model.
    
- `corrupted_prompts`
    
    ```
    corrupted_prompts = []
    for i in range(0, len(prompts), 2):
        corrupted_prompts.append(prompts[i+1])
        corrupted_prompts.append(prompts[i])
    ```
    
    The reason for this is b/c the answers are written as (Mary, John) and (John, Mary), and the prompts are written as so that odd index has “mary” as IOI, while evens have “john” as IOI. By swapping the odd and even prompts but not the answers, you corrupt their inputs as they do not provide the “right answers” (?)
    
- We can immediately see that, exactly as predicted, originally all relevant computation happens on the second subject token, and at layers 7 and 8, the information is moved to the final token. Moving the residual stream at the correct position near *exactly* recovers performance!
    
    ![Untitled](Exploratory%20Analysis%20Demo%20c61288d8f11b45d993c796ec28a62132/Untitled%203.png)
    
    This plot lines up with our guess in the drawing above. The layers at the end stopped attending to John_10 because the information there is moved to to_14, so the later layers attend to it there instead.
    

---

NOTE: Head attribution is different than activation head patching!!!

Logit diff head attribution

![Untitled](Exploratory%20Analysis%20Demo%20c61288d8f11b45d993c796ec28a62132/Untitled%204.png)

Activation head patching

![Untitled](Exploratory%20Analysis%20Demo%20c61288d8f11b45d993c796ec28a62132/Untitled%205.png)

Activation head patching seems to reveal more

---

### **Visualizing Attention Patterns**

while *one* early head (blue) attends from the second subject to its first copy, the other two mysteriously attend to the word *after* the first copy.

![Untitled](Exploratory%20Analysis%20Demo%20c61288d8f11b45d993c796ec28a62132/Untitled%206.png)

Second John query: Blue attends to “john”, but red and green attend to “mary”

middle heads attend from the final token (query, row) to the second subject (key, column)

![Untitled](Exploratory%20Analysis%20Demo%20c61288d8f11b45d993c796ec28a62132/Untitled%207.png)

---

**Decomposing Heads**

We can disentangle which of these is important by patching in just the attention pattern *or* the value vectors.

Heatmap:

- Explanation
    
    The code you provided seems to be patching the head vectors of a model and calculating the differences between the original and patched logits. Here's a breakdown of what the code does:
    
    1. Initializes a tensor called `patched_head_v_diff` with zeros. This tensor will store the normalized differences between the original and patched logits for each head vector.
    2. Iterates over each layer and head index in the model's configuration.
    3. Defines a partial function `hook_fn` using the `patch_head_vector` function, which takes the head index and a `clean_cache` parameter as arguments.
    4. Calls the `model.run_with_hooks` method to run the model with the `corrupted_tokens` input. The `fwd_hooks` argument specifies a hook function to be applied during the forward pass of the model. In this case, it hooks into the specified attention head using the `hook_fn`.
    5. The resulting `patched_logits` are computed by applying the hook function to the model's forward pass with the corrupted tokens.
    6. The `logits_to_ave_logit_diff` function is applied to calculate the differences between the `patched_logits` and the `answer_tokens`.
    7. The `normalize_patched_logit_diff` function is used to normalize the differences between the original and patched logits.
    8. The normalized difference is assigned to the corresponding index in the `patched_head_v_diff` tensor.
    
    Overall, this code calculates and stores the normalized differences between the original and patched logits for each head vector in the model.
    

```
patched_logits = model.run_with_hooks(
            corrupted_tokens, 
            fwd_hooks = [(utils.get_act_name("v", layer, "attn"), 
                hook_fn)], 
            return_type="logits"
        )
patched_logit_diff = logits_to_ave_logit_diff(patched_logits, answer_tokens)
patched_head_v_diff[layer, head_index] = normalize_patched_logit_diff(patched_logit_diff)
```

Scatterplot:

```
x=utils.to_numpy(patched_head_v_diff.flatten()), 
y=utils.to_numpy(patched_head_z_diff.flatten()),
```

`patched_head_z_diff` is from “Activation Patching—Heads”