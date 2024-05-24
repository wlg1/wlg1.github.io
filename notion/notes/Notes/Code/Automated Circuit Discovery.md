# Automated Circuit Discovery

[https://github.com/ArthurConmy/Automatic-Circuit-Discovery](https://github.com/ArthurConmy/Automatic-Circuit-Discovery)

- This takes a long time because each head has these to go through:
    
    ```jsx
    blocks.0.hook_resid_post
    blocks.0.hook_mlp_out
    blocks.0.mlp.hook_post
    blocks.0.mlp.hook_pre
    blocks.0.ln2.hook_normalized
    blocks.0.ln2.hook_scale
    blocks.0.hook_mlp_in
    blocks.0.hook_resid_mid
    blocks.0.hook_attn_out
    blocks.0.attn.hook_result
    blocks.0.attn.hook_z
    blocks.0.attn.hook_pattern
    blocks.0.attn.hook_attn_scores
    blocks.0.attn.hook_v
    blocks.0.attn.hook_k
    blocks.0.attn.hook_q
    blocks.0.ln1.hook_normalized
    blocks.0.ln1.hook_scale
    blocks.0.hook_v_input
    blocks.0.hook_k_input
    blocks.0.hook_q_input
    blocks.0.hook_resid_pre
    ```
    
    Not just (L, H)
    
- explain what all of these do:
    1. **`blocks.0.hook_resid_post`**: This might be a hook applied after a residual connection, often used in Transformer blocks to add the input of the block to its output for better gradient flow.
    2. **`blocks.0.hook_mlp_out`**: A hook on the output of a multi-layer perceptron (MLP) layer, typically found in Transformer blocks for processing information after the attention mechanism.
    3. **`blocks.0.mlp.hook_post`**: Similar to `hook_mlp_out`, this hook is likely applied after the processing of an MLP layer.
    4. **`blocks.0.mlp.hook_pre`**: A hook applied before the MLP layer, useful for inspecting or modifying the input to the MLP.
    5. **`blocks.0.ln2.hook_normalized`**: This hook might be applied to the output of the second layer normalization (`ln2`) after it has normalized its input.
    6. **`blocks.0.ln2.hook_scale`**: Potentially a hook to inspect or modify the scaling parameters of the second layer normalization.
    7. **`blocks.0.hook_mlp_in`**: A hook applied at the input to the MLP layer.
    8. **`blocks.0.hook_resid_mid`**: This could be a hook in the middle of a residual connection, possibly inspecting or altering the data before it's added back to the main flow.
    9. **`blocks.0.hook_attn_out`**: A hook on the output of the attention mechanism, useful for examining or modifying the attention outputs.
    10. **`blocks.0.attn.hook_result`**: Likely a hook on the final result of the attention layer.
    11. **`blocks.0.attn.hook_z`**: This could be a hook on an intermediate variable in the attention mechanism, possibly the output before any final transformations.
    12. **`blocks.0.attn.hook_pattern`**: Potentially a hook to inspect the attention pattern or weights.
    13. **`blocks.0.attn.hook_attn_scores`**: A hook on the attention scores, which represent the weights given to each element in the sequence.
    14. **`blocks.0.attn.hook_v`**, **`blocks.0.attn.hook_k`**, **`blocks.0.attn.hook_q`**: Hooks on the "value", "key", and "query" matrices in the attention mechanism, respectively. These are fundamental components of the attention calculation.
    15. **`blocks.0.ln1.hook_normalized`** and **`blocks.0.ln1.hook_scale`**: Similar to `ln2` hooks but applied to the first layer normalization in the block.
    16. **`blocks.0.hook_v_input`**, **`blocks.0.hook_k_input`**, **`blocks.0.hook_q_input`**: Hooks on the inputs that will be transformed into "value", "key", and "query" matrices.
    17. **`blocks.0.hook_resid_pre`**: A hook applied before a residual connection, useful for examining the original input to the block.
- It also takes a long time because it’s not removing nodes, it’s removing EDGES (node pairs)
    
    eg) 
    
    Node: cur_parent=TLACDCInterpNode(blocks.1.attn.hook_result, [:, :, 11]) (self.current_node=TLACDCInterpNode(blocks.8.hook_v_input, [:, :, 11]))
    
    Metric after removing connection to blocks.1.attn.hook_result [:, :, 11] is 7.742216110229492 (and current metric 7.766965866088867)
    Result is -0.024749755859375...so removing connection
    

try in colab:

[https://colab.research.google.com/drive/1bxC_a0yEpsBTIljkyOU7nqgyvjzHMQhW](https://colab.research.google.com/drive/1bxC_a0yEpsBTIljkyOU7nqgyvjzHMQhW)

[https://arthurconmy.github.io/automatic_circuit_discovery/](https://arthurconmy.github.io/automatic_circuit_discovery/)

the baseline dataset[1](https://arthurconmy.github.io/automatic_circuit_discovery/#fn:fn2) could be sentences like “This time it is here and last time it was”, that would presumably produce similar activations to the main dataset, but don’t introduce any context about months, or that the next word should be about a date in future.

---

### Docs

[**TLACDCExperiment**](Automated%20Circuit%20Discovery%2078c36eb7aa084d7db89fa74016e83d3e/TLACDCExperiment%20c4ddc44462e945f7bee72cedce242b50.md)

[**TLACDCEdge**](Automated%20Circuit%20Discovery%2078c36eb7aa084d7db89fa74016e83d3e/TLACDCEdge%20e0a5b5a980c14f58abf04d094dfce4aa.md)

[ioi - utils.py](Automated%20Circuit%20Discovery%2078c36eb7aa084d7db89fa74016e83d3e/ioi%20-%20utils%20py%204e1576e4437c46d7a02febd7c292317d.md)