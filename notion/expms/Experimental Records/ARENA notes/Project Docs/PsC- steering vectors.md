# PsC- steering vectors

First, use `set_add_activations` to modify output when `.forward` is called. Then, call `.forward` using `plot_decoded_activations_for_layer` :

- `model.set_add_activations(layer, multiplier * vec.cuda())` in activation_steering_interp.ipynb
    
    ```python
    def set_add_activations(self, layer, activations, do_projection=False):
            self.model.model.layers[layer].add(activations, do_projection)
    ```
    
    add() just sets class variables values
    
    ```python
    def add(self, activations, do_projection=False):
            self.add_activations = activations
            self.do_projection = do_projection
    ```
    
- `model.plot_decoded_activations_for_layer(25, tokens, 10)` ← `get_logits(tokens)` ← `logits = self.model(tokens).logits` ← `.forward()` ← class LlamaWrapper’s layers are BlockOutputWrapper `.forward()` in llamawrapper.py ← `augmented_output = add_vector_after_position(…)` ←`output = (augmented_output,) + output[1:]` ← `add_vector_after_position`() in helpers.py
    
    (optional):
    
    ```python
    if do_projection:
            matrix = project_onto_orthogonal_complement(matrix, vector)
    ```
    
    `project_onto_orthogonal_complement()` is just MM then sum over norm, then subtract
    

When you make notebooks you should add comments showing `plot_decoded_activations_for_layer` uses forward(), otherwise hard to decipher for reveiwers at first glance without looking at internals

---

- We're using concepts from calculate_and_apply_steering_vector() because we're generating, not from intervene_with_h() [which only finds the next token completion]
    
    If we used forward, completion is just new line token:
    
    ```jsx
    # with nnsight_model.forward(remote=REMOTE) as runner:
    
    #     # First, run a forward pass where we don't intervene, just save token id completions
    #     with runner.invoke(test_prompts) as invoker:
    #         token_completions_zero_shot = nnsight_model.lm_head.output[:, -1].argmax(dim=-1).save()
    
    #     # Next, run a forward pass on the zero-shot prompts where we do intervene
    #     with runner.invoke(test_prompts) as invoker:
    #         # Add the h-vector to the residual stream, at the last sequence position
    #         hidden_states = nnsight_model.model.layers[layer].output[0][:, -2, :] 
    #         hidden_states += diff_vec_mean
    #         # Also save completions
    #         token_completions_intervention = nnsight_model.lm_head.output[:, -1].argmax(dim=-1).save()
    
    # # Decode to get the string tokens
    # completions_zero_shot = nnsight_model.tokenizer.batch_decode(token_completions_zero_shot.value)
    # completions_intervention = nnsight_model.tokenizer.batch_decode(token_completions_intervention.value)
    ```
    

`"12345"[-2:]` Output is “45”