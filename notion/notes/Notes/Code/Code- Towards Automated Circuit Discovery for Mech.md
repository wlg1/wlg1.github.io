# Code- Towards Automated Circuit Discovery for Mechanistic Interpretability

[https://colab.research.google.com/github/ArthurConmy/Automatic-Circuit-Discovery/blob/main/notebooks/colabs/ACDC_Main_Demo.ipynb](https://colab.research.google.com/github/ArthurConmy/Automatic-Circuit-Discovery/blob/main/notebooks/colabs/ACDC_Main_Demo.ipynb)

`things = get_all_ioi_things()`

`from acdc.ioi.utils import (get_all_ioi_things,`

[https://github.com/ArthurConmy/Automatic-Circuit-Discovery/blob/main/acdc/ioi/utils.py](https://github.com/ArthurConmy/Automatic-Circuit-Discovery/blob/main/acdc/ioi/utils.py)

`exp = TLACDCExperiment() … exp.step()`

- What is exp?
    
    In the code snippets you've provided, `exp` appears to be an instance of a class named `TLACDCExperiment`. This object seems to handle various aspects of an experiment you're running. Here's a breakdown of how `exp` is used based on the provided snippets:
    
    1. **Initialization**:
        
        ```python
        exp = TLACDCExperiment(
            model=tl_model,
            threshold=THRESHOLD,
            ...
            show_full_index=use_pos_embed,
        )
        
        ```
        
        This suggests that `TLACDCExperiment` is a class that is initialized with a variety of arguments, including model, threshold, wandb configurations, and more.
        
    2. **Training**:
        
        ```python
        exp.step(testing=False)
        
        ```
        
        The `step` method on the `exp` object seems to perform one training or evaluation step of the experiment. The boolean argument `testing` might be determining whether this step is for training or testing.
        
    3. **Metrics or Properties Logging**:
        
        ```python
        print(exp.count_no_edges())
        
        ```
        
        The method `count_no_edges` likely computes and returns some metric or property of the experiment, possibly the count of nodes without edges or a similar metric.
        
    4. **Check for Stopping Condition**:
        
        ```python
        if exp.current_node is None or SINGLE_STEP:
            break
        
        ```
        
        The `current_node` attribute of `exp` is being checked to determine if the training loop should be terminated early. This might indicate that the experiment has finished processing all nodes.
        
    5. **Save Data**:
        
        ```python
        exp.save_edges("edges.pkl")
        
        ```
        
        The `save_edges` method seems to save some internal data or results of the experiment to a file.
        
    6. **Interactions with WandB**:
    Various wandb-related configurations and methods indicate that the `TLACDCExperiment` class has integrated support for logging and tracking experiments using Weights & Biases (wandb).
    
    Without more detailed information about the `TLACDCExperiment` class itself, these are educated guesses based on the context and typical practices. To fully understand what `exp` is and how it works, you'd need to inspect the definition and implementation of the `TLACDCExperiment` class.
    

[https://github.com/ArthurConmy/Automatic-Circuit-Discovery/blob/main/acdc/TLACDCExperiment.py](https://github.com/ArthurConmy/Automatic-Circuit-Discovery/blob/main/acdc/TLACDCExperiment.py)

[https://github.com/ArthurConmy/Automatic-Circuit-Discovery/blob/main/acdc/TLACDCCorrespondence.py](https://github.com/ArthurConmy/Automatic-Circuit-Discovery/blob/main/acdc/TLACDCCorrespondence.py)

- **`TLACDCCorrespondence`**
    
    This code defines a class named `TLACDCCorrespondence` which seems to represent a computational graph, similar to another correspondence graph (as mentioned in the docstring) named `ACDCCorrespondence` from some `rust_circuit` code. The main objective of this class appears to be to build and manage a graph structure which comprises nodes (`TLACDCInterpNode`) and edges (`Edge`).
    
    Here's a breakdown of the main components:
    
    1. **Attributes**:
        - `graph`: This is a multi-level dictionary storing nodes (`TLACDCInterpNode`) based on their name and `TorchIndex`.
        - `edges`: Another multi-level dictionary storing edges (`Edge`). The structure indicates a child node's name and `TorchIndex`, followed by a parent node's name and `TorchIndex`.
    2. **Initialization**: The `__init__` method initializes the `graph` and `edges` with default values.
    3. **Node and Edge Management**:
        - `first_node()`: Returns the first node in the graph.
        - `nodes()`: Returns a list of all nodes in the graph.
        - `all_edges()`: Concatenates and returns all edges in the graph as a dictionary.
        - `add_node()`: Adds a node to the graph.
        - `add_edge()`: Adds an edge between two nodes in the graph.
        - `remove_edge()`: Removes an edge between two nodes based on their names and indices.
    4. **Graph Construction**:
        - `setup_from_model()`: A classmethod to create a correspondence graph based on the structure of a model. The logic here seems specific to some kind of neural network model with multiple layers and attention heads, but without the full context of the model's definition, it's a bit hard to grasp all the intricacies.
    5. **Utility**:
        - `count_no_edges()`: Counts the number of non-placeholder edges in the graph. If `verbose` is `True`, it prints out tuples of edges and the count.
    
    Overall, the `TLACDCCorrespondence` class provides a robust structure for managing a computational graph built from a given model. The integration of nodes and edges into a multi-dimensional dictionary provides an efficient way to access and manipulate the graph components.
    
    However, there are some potential improvements and considerations:
    
    1. **Error Handling**: The code currently uses assertions for error handling. While assertions can be useful for catching unexpected behavior during development, they are not recommended for production code. Instead, it would be more robust to raise specific exceptions with informative error messages.
    2. **Documentation**: More inline comments and docstrings would make the code easier to understand, especially when trying to grasp the intricacies of the graph construction from a model.
    3. **Performance**: The repeated traversal of nodes and edges in certain functions may not be optimal for large graphs. Optimizations may be needed for better scalability.
    4. **Code Duplication**: There's a bit of code repetition, especially in the `setup_from_model()` method. This could be refactored for clarity and maintainability.
    
    This is a high-level overview, and to fully understand the intricacies of the logic, one would ideally have access to the related classes and modules such as `TLACDCInterpNode`, `Edge`, and the structure of the model used in `setup_from_model()`.
    

---

[https://github.com/ArthurConmy/Automatic-Circuit-Discovery/blob/main/acdc/TLACDCEdge.py](https://github.com/ArthurConmy/Automatic-Circuit-Discovery/blob/main/acdc/TLACDCEdge.py)

---

[https://github.com/ArthurConmy/Automatic-Circuit-Discovery/blob/main/experiments/launch_induction.py](https://github.com/ArthurConmy/Automatic-Circuit-Discovery/blob/main/experiments/launch_induction.py)

---

[https://github.com/ArthurConmy/Automatic-Circuit-Discovery/blob/main/tests/acdc/test_acdc.py](https://github.com/ArthurConmy/Automatic-Circuit-Discovery/blob/main/tests/acdc/test_acdc.py)

- @pytest.mark.slow
@pytest.mark.skip(reason="TODO fix")
    
    Decorators used with the `pytest` framework, a popular testing tool in Python. Let's break them down:
    
    1. **`@pytest.mark.slow`**: This is a custom marker that indicates the test is slow to run. By marking tests with custom labels like this, you can selectively run or skip certain categories of tests. For instance, if you've marked several tests as `slow`, you could skip them all by running `pytest -k "not slow"` to avoid long wait times during development.
    2. **`@pytest.mark.skip(reason="TODO fix")`**: This decorator tells `pytest` to skip this particular test when running the test suite. The `reason` parameter is optional but can be helpful to remind developers why the test was skipped. In this case, the test seems to have an issue (possibly a bug or not fully implemented feature), and thus it has been temporarily skipped until someone can address the "TODO" and fix it.
    
    When `pytest` is run, any test decorated with `@pytest.mark.skip` won't be executed, and `pytest` will report it as skipped. The given reason ("TODO fix") will also be displayed in the test results, serving as a reminder to developers that this test needs attention.
    
- @pytest.mark.parametrize("task", ["tracr-proportion", "tracr-reverse", "docstring", "induction", "ioi", "greaterthan"])
@pytest.mark.parametrize("zero_ablation", [False, True])
    
    These lines use the `@pytest.mark.parametrize` decorator, which is a feature provided by the `pytest` testing framework in Python. The `parametrize` decorator allows you to run a test function multiple times with different arguments. It's a powerful way to execute the same test logic with different input values and to ensure that a function behaves correctly across a range of data.
    
    Let's break down the provided lines:
    
    1. **`@pytest.mark.parametrize("task", ["tracr-proportion", "tracr-reverse", "docstring", "induction", "ioi", "greaterthan"])`**: This line tells `pytest` to run the subsequent test function once for each of the provided task values. For example, the first time the test runs, the `task` parameter will be set to `"tracr-proportion"`. The second time, it will be set to `"tracr-reverse"`, and so on.
    2. **`@pytest.mark.parametrize("zero_ablation", [False, True])`**: This line tells `pytest` to run the test function with each of the `zero_ablation` values, i.e., once with `False` and once with `True`.
    
    When used together like this, the test function will be executed for each combination of the provided parameters. Given the two decorators you've shown, the test will run a total of `6 (tasks) * 2 (zero_ablation values) = 12` times.
    
    For example, if the test function is defined as:
    
    ```python
    def test_example(task, zero_ablation):
        # test logic here
    
    ```
    
    Then the `test_example` function will be called with the following combinations of arguments:
    
    1. (`"tracr-proportion"`, `False`)
    2. (`"tracr-proportion"`, `True`)
    3. (`"tracr-reverse"`, `False`)
    4. (`"tracr-reverse"`, `True`)
    5. ... and so on for all combinations.
    
    This makes it easier to verify that the test function behaves correctly across a wide range of input scenarios without having to write separate tests for each one.
    

---

---

[https://colab.research.google.com/drive/1dRf87ZOpnc1c6NUAdDxuu-nwCVoCTndf#scrollTo=945274fc](https://colab.research.google.com/drive/1dRf87ZOpnc1c6NUAdDxuu-nwCVoCTndf#scrollTo=945274fc)

[https://chat.openai.com/c/b6a9ec62-115b-41bd-9ebf-f1c003bfe5ea](https://chat.openai.com/c/b6a9ec62-115b-41bd-9ebf-f1c003bfe5ea)

Where does this file import "TASK" (which has value 'induction') from?

where is argparse.ArgumentParser

- how do I change the value of TASK to 'greaterthan'?
    
    To change the value of `TASK` to `'greaterthan'` within the Jupyter notebook, you should modify the line that sets the `--task` argument value. Specifically, you'll want to change:
    
    ```python
    --task=induction
    
    ```
    
    to:
    
    ```python
    --task=greaterthan
    
    ```
    
    Here's how you can modify the code cell in the notebook:
    
    1. Locate the code cell that contains the string block with the argument `-task=induction`.
    2. In that string block, replace `-task=induction` with `-task=greaterthan`.
    3. Execute the cell to parse the modified arguments and set the value of `TASK`.
    
    Once you make this change and execute the cell, the value of `TASK` will be set to `'greaterthan'`. If you're modifying the notebook interactively, you can make this change directly. If you're trying to modify the notebook programmatically or need further assistance, please let me know!
    

TASK is in **ACDC Experiment Setup**