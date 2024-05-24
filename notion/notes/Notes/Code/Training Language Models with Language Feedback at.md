# Training Language Models with Language Feedback at Scale

[https://github.com/JeremyAlain/imitation_learning_from_language_feedback/blob/main/reward_model/score_refinements.py](https://github.com/JeremyAlain/imitation_learning_from_language_feedback/blob/main/reward_model/score_refinements.py)

- `predictions = defaultdict(lambda: [0.0] * (args.num_samples + 1)) # type: ignore`
    
    The line of code you provided:
    
    ```python
    predictions = defaultdict(lambda: [0.0] * (args.num_samples + 1))  # type: ignore
    
    ```
    
    is initializing a `defaultdict` from the Python collections module. Here's a breakdown:
    
    - **`defaultdict`**: This is a subclass of the built-in `dict` class. It overrides one method to provide a default value for a nonexistent key, which is specified when you create the defaultdict. If you try to access or modify a key that doesn't exist in the dictionary, it will return/use the default value instead of raising a `KeyError`.
    - **`lambda: [0.0] * (args.num_samples + 1)`**: This is the default factory function for the defaultdict. Whenever a key is accessed that does not exist in the dictionary, this lambda function is called to provide a default value. In this case, it returns a list of zeros. The length of this list is `(args.num_samples + 1)`, where `args.num_samples` is a command-line argument that seems to specify the number of summary samples. By adding 1, it seems to account for an additional sample or category, perhaps a human summary as hinted elsewhere in the code.
    - **`# type: ignore`**: This is a type hint comment that's commonly used with tools like `mypy` to ignore type checking for this specific line. It's likely added here because the default lambda function might produce type errors or warnings when the code is checked by a static type checker.
    
    In simple terms, this code creates a dictionary where:
    
    - If you access a key that hasn't been set yet, it will give you a list filled with zeros as the default value.
    - The length of this list is determined by the `args.num_samples + 1` value.
    
    For example, if `args.num_samples` was 3:
    
    ```python
    print(predictions["any_key"])  # Outputs: [0.0, 0.0, 0.0, 0.0]
    
    ```
    
    You get a list of four zeros as a default value.
    

---

 /[utilities](https://github.com/JeremyAlain/imitation_learning_from_language_feedback/tree/main/utilities)/**general_utilities.py**

Only uses numpy for random

- summary
    
    ---
    
    **`split_off_dataset_with_proportional_subreddit_distribution`**:
    
    This function aims to create a subset of the original data (`data`) with a target size (`target_dataset_size`), ensuring that the distribution of subreddits remains proportional.
    
    1. Reset the index of the dataframe.
    2. Calculate the fraction of data needed from the original data.
    3. Assert that the dataframe has a column named 'subreddit'.
    4. Sample the data proportionally based on subreddit categories.
    5. Remove the samples from the original dataframe.
    6. If the sampled data doesn't match the target size, either add or remove rows to meet the target.
    7. Return the modified data and the sampled data.
    
    ---
    
    **`assert_saved_dataframe_is_equal_to_dataframe`**:
    
    This function checks if the data saved in a `.jsonl` file (at `dataframe_path`) is the same as a provided dataframe (`dataframe`).
    
    1. Check if the file extension is `.jsonl`.
    2. If the file exists, read it into a dataframe.
    3. Ensure that the saved dataframe and the provided dataframe are of the same shape.
    4. For each row in the saved dataframe, check if it is the same as the corresponding row in the provided dataframe.
    
    ---
    
    **`save_list_of_dicts_to_jsonl`**:
    
    This function saves a list of dictionaries (`list_of_dicts`) as a `.jsonl` file at the given `save_path`.
    
    1. Open the specified file for writing.
    2. For each dictionary in the list, convert it to a JSON string and write it to the file.
    
    ---
    
    **`print_columns_of_dataframe`**:
    
    This function prints specified columns (`columns`) of a given dataframe (`dataframe`) row by row.
    
    1. For each row in the dataframe:
        1. Print the sample number.
        2. Fetch the row's data.
        3. For each specified column, print its name and value.
        4. Print a divider for clarity.
    
    ---
    
    **Overall**:
    
    The script seems focused on handling a dataset (specifically in the form of a Pandas dataframe) with special attention to subreddits. It provides functionalities to create a subset with a proportional distribution, check the integrity of saved data, save data in the `.jsonl` format, and print specified columns of a dataframe.