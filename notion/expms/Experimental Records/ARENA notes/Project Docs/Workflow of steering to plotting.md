# Workflow of steering to plotting

[repl_paper_plots.ipynb](https://colab.research.google.com/drive/1EDBWJKfkT1e3KGAVeDGYo0ZgQ2V7LCs2)

- Workflow how-to from README:
    
    ```
    Scripts that can be run to replicate the experiments are in the `scripts/` folder.
    Run `./scripts/generate_all_vectors.sh` first to generate steering vectors.
    ```
    
- Dataset files guide
    
    In the preprocessed_data folder:
    
    - generate_dataset.json: used to create steering vectors
    - These are used ONLY to apply the generated vectors on:
        - test_dataset.json
        - truthful_qa_dataset.json
- Workflow of steering to plotting
    
    In `plot_results.py`, the function `plot_in_distribution_data_for_layer()` is what gives the Figures. y-axis is `get_avg_key_prob()`, which uses the `results` dict output by `prompting_with_steering.py` to get the prob output value of token A or B (the answer) over their total prob sum. 
    
    `prompting_with_steering` gets the results using `process_item_in_distribution()`, finding the probs using `get_a_b_probs` from `utils.helpers`. Notice there is no ‘score’ key; that is for `plot_out_of_distribution_data`.