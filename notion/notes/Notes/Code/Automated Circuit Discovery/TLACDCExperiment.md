# TLACDCExperiment

- Give a quick summary of what each function does
    1. **`__init__`:**
        - Initializes the ACDC experiment, setting up the model, data, thresholds, and various configurations for the experiment.
    2. **`verify_model_setup`:**
        - Ensures the model is correctly set up for the experiment, verifying specific configurations and properties.
    3. **`update_cur_metric`:**
        - Updates the current metric used in the experiment based on the model's outputs, optionally recalculating edges.
    4. **`reverse_topologically_sort_corr`:**
        - Reorders the computational graph in reverse topological order to ensure correct processing sequence.
    5. **`sender_hook`:**
        - Hook function that saves activations from a specified point (hook) in the model to a cache for later use.
    6. **`receiver_hook`:**
        - Manages nodes receiving input from other nodes, modifying inputs based on the current state of the computational graph.
    7. **`add_all_sender_hooks`:**
        - Adds sender hooks to all nodes in the computational graph, with options for different configurations.
    8. **`setup_corrupted_cache`:**
        - Sets up a cache of corrupted (or altered) activations for use in the experiment, particularly for ablation studies.
    9. **`setup_model_hooks`:**
        - Configures and adds hooks to the model for both sending and receiving data within the computational graph.
    10. **`save_edges`:**
        - Saves the current state of edges in the computational graph, typically for persistence or analysis.
    11. **`add_sender_hook`:**
        - Adds a sender hook to a specific node in the computational graph, with options to override existing hooks.
    12. **`add_receiver_hook`:**
        - Adds a receiver hook to a specific node, with options for overriding and order of execution.
    13. **`step`:**
        - Processes one node in the computational graph, evaluating and possibly modifying connections based on specified criteria.
    14. **`remove_redundant_node`:**
        - Removes nodes from the computational graph that are deemed redundant, based on the experiment's logic.
    15. **`current_node_connected`:**
        - Checks if the current node in the computational graph is connected to other nodes, used for managing graph structure.
    16. **`find_next_node`:**
        - Finds the next node to process in the computational graph following the current node.
    17. **`increment_current_node`:**
        - Moves to the next node in the computational graph, ensuring proper sequence of processing.
    18. **`count_no_edges`:**
        - Counts the number of edges in the current state of the computational graph, often for monitoring or analysis purposes.
    19. **`reload_hooks`:**
        - Reloads the hooks on the model, typically used after modifications to the computational graph or model.
    20. **`save_subgraph`:**
        - Saves the current subgraph (a portion of the computational graph) for persistence or later analysis.
    21. **`load_subgraph`:**
        - Loads a subgraph into the current experiment, often used for restoring previous states or configurations.
    22. **`load_from_wandb_run`:**
        - Loads experiment settings or configurations from a Weights & Biases (wandb) run, integrating external experiment tracking.
    23. **`remove_all_non_attention_connections`:**
        - Removes all connections in the computational graph that are not related to attention mechanisms.
    24. **`add_back_head`:**
        - Adds back a previously removed head (part of the model) to the computational graph. (Marked as not implemented)
    25. **`call_metric_with_corr`:**
        - Calls a metric function with a specific correspondence (state of the computational graph), used for evaluating different configurations.
- How exp is used
    
    ```jsx
    for i in range(args.max_num_epochs):
        exp.step(testing=False)
    
        show(
            exp.corr,
            f"ims/img_new_{i+1}.png",
            show_full_index=False,
        )
    
        if IN_COLAB or ipython is not None:
            # so long as we're not running this as a script, show the image!
            display(Image(f"ims/img_new_{i+1}.png"))
    
        print(i, "-" * 50)
        print(exp.count_no_edges())
    
        if i == 0:
            exp.save_edges("edges.pkl")
    
        if exp.current_node is None or SINGLE_STEP:
            show(
                exp.corr,
                f"ims/ACDC_img_{exp_time}.png",
    
            )
            break
    ```
    
    1. **Call to `exp.step(testing=False)`:**
        - The `step` method of the `exp` (an instance of `TLACDCExperiment`) is called. This method processes one node in the computational graph.
        - Inside `step`, various other methods are called, such as `update_cur_metric`, `add_receiver_hook`, `add_sender_hook`, `receiver_hook`, and potentially others based on the experiment's logic and the state of the computational graph.
    2. **Visualization with `show`:**
        - After each step, the computational graph's current state is visualized and saved to an image file using the `show` function.
    3. **Display Image (Conditional):**
        - If the script is running in a Jupyter Notebook or a similar interactive environment (checked by `IN_COLAB` or `ipython`), the image is displayed inline using `display(Image(...))`.
    4. **Print Current Iteration and Edge Count:**
        - The current iteration number and a separator are printed.
        - The current number of edges in the computational graph is printed, obtained by calling `exp.count_no_edges()`.
    5. **Save Edges (Conditional on First Iteration):**
        - On the first iteration (`i == 0`), the state of the edges in the computational graph is saved using `exp.save_edges("edges.pkl")`.
    6. **Check for Termination Conditions:**
        - If `exp.current_node` is `None` or if `SINGLE_STEP` is `True`, it indicates the end of processing or a single-step mode.
        - In this case, the final state of the computational graph is visualized and saved using `show`, and the loop is terminated with `break`.
- give a flow chart of function calling paths used by exp.step()
    1. Calls `update_cur_metric()`:
        - Updates metrics based on model outputs and optionally recalculates edges.
    2. **Check and Add Receiver Hook (Conditional):**
        - If the current node's `incoming_edge_type` is not a `PLACEHOLDER`, `add_receiver_hook()`
    3. **Direct Computation Nodes Handling (Conditional):**
        - If `incoming_edge_type` is `DIRECT_COMPUTATION`, `add_sender_hook()` is called:
            - Adds a sender hook to the current node.
    4. **Loop Over Sender Nodes:**
        - For each sender node connected to the current node:
            - For each index in the sender node:
                - Get the edge between the current node and the sender node.
                - Manipulate the edge's presence in the computational graph (set `edge.present` to `False`).
    5. **Update Metric After Edge Manipulation:**
        - Calls `update_cur_metric()` again to reevaluate the metric after the edge manipulation.
    6. **Compare Metrics and Decide Edge Inclusion:**
        - Compares the new metric with the old one.
        - If the result meets a certain threshold, it decides whether to include or exclude the edge in the graph.
    7. **Log Metrics (Conditional on using wandb):**
        - If using Weights & Biases (wandb), log the metrics.
    8. **Remove Redundant Node (Conditional):**
        - If the current node is not used (`is_this_node_used` flag) and `remove_redundant` is `True`, call `remove_redundant_node()`:
            - Removes nodes from the graph deemed redundant.
    9. **Visualization Call (Conditional):**
        - If the node is used, calls `show()` to visualize the current state of the computational graph.
    10. **Increment Current Node:**
        - Calls `increment_current_node()` to move to the next node in the graph.
    11. **Final Metric Update:**
        - Calls `update_cur_metric()` one last time to ensure the metrics are up to date after all modifications.
- Explain each line of def step(self, early_stop=False, testing=False):
    1. **Direct Computation Nodes Handling:** Checks if the `incoming_edge_type` of the `current_node` is `DIRECT_COMPUTATION`. If true, it proceeds to add a sender hook.
    2. Initializes a boolean flag `is_this_node_used` to `False`. This flag is likely used to track whether the current node is actively used in the computational graph.
    3. **Loop Over Sender Nodes:**
        - The following lines set up a loop over sender nodes connected to the current node. The loop involves nested iterations over sender names and indices, and manipulates edges based on certain conditions.
- What does "No Edge" mean in this code?
    
    This is NUMBER of edges that still need to be checked, not “there is no edge x”!
    
    In the context of the `TLACDCExperiment` class and its method `count_no_edges`, the term "No Edge" likely refers to the count or number of edges currently present in the computational graph of the transformer model being analyzed.
    
    It is counting the number of active edges in the current state of the model's computational graph. This count is significant in the context of ACDC (Automated Circuit Discovery and Correction), as it reflects the current complexity or connectivity of the model after certain transformations, ablations, or optimizations have been applied.
    
- What does "but it's bad" mean
    
    [https://github.com/ArthurConmy/Automatic-Circuit-Discovery/blob/main/acdc/TLACDCExperiment.py#L785](https://github.com/ArthurConmy/Automatic-Circuit-Discovery/blob/main/acdc/TLACDCExperiment.py#L785)
    
    the newly selected **`current_node`** does not meet certain criteria; it’s not included in the circuit
    
    ```jsx
    if self.current_node is None or self.current_node_connected() or self.current_node.name in ["blocks.0.hook_resid_pre", "hook_pos_embed", "hook_embed"]:
        break
    print("But it's bad")
    ```
    
    So if it’s not a required node, or if it’s not connected, don’t use it.
    
- `def current_node_connected(self):`
    1. **Check if the Current Node is Connected:**
        - The method iterates over all edges in the `self.corr.edges` dictionary (which represents the computational graph).
        - It checks if the `current_node` has any active ('present') edges connected to it.
            - an inactive edge is one that was removed previously during ACDC
                - but only about edges from curr node TO
        - If the `current_node` is found to have an active edge, the method returns `True`, indicating the node is connected in the graph.
    2. **Update Current Metric:**
        - If the `current_node` is not connected (i.e., it has no active edges), the method then proceeds to update the current metric of the model using `self.update_cur_metric(recalc_metric=True, recalc_edges=True)`. This update reflects the state of the model without considering the current node.
    3. **Store the Old Metric:**
        - The method stores the current metric value in `old_metric` for later comparison. This is to assess the impact of removing incoming edges to the `current_node`.
    4. **Remove All Incoming Edges:**
        - The method iterates over all parent nodes (and their indices) connected to the `current_node`.
        - For each parent node and index, it attempts to access the corresponding edge. If the edge exists (`KeyError` is not raised), it sets the edge's `present` attribute to `False`, effectively disconnecting it.
        - It then calls `self.corr.remove_edge` to remove the edge from the graph.
    5. **Update Metric After Edge Removal:**
        - After removing the edges, the method updates the metric again to reflect the new state of the model (`self.update_cur_metric(recalc_edges=True)`).
    6. **Assertion to Check Metric Consistency:**
        - The method then checks that the absolute difference between the new metric (`self.cur_metric`) and `old_metric` is less than `3e-3`.
        - This assertion ensures that removing all incoming edges to the `current_node` does not significantly change the metric, implying that these edges were not contributing meaningfully to the model's output.
        - If this assertion fails regularly, it might indicate an issue with how edges are being evaluated or removed.
    7. **Return False:**
        - Finally, the method returns `False`, indicating that the `current_node` was not connected (since it had no active edges and all its incoming edges were removed).
    
- the num edges doesn’t always decr by 1 when removed after eval as bad
    
    ```jsx
    We moved to  blocks.5.hook_v_input[:, :, 4]
    No edge 7153
    No edge 7087
    But it's bad
    We moved to  blocks.5.hook_v_input[:, :, 3]
    No edge 7087
    No edge 7021
    ```