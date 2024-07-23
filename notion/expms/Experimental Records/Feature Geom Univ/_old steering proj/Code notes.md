# Code notes

[https://github.com/fbarez/actbasedoninternal/blob/main/ccs/evaluate.py](https://github.com/fbarez/actbasedoninternal/blob/main/ccs/evaluate.py)

- why use parser?
    
    The use of a parser in a Python script, particularly for a command line interface (CLI), is a common practice to manage and interpret command line arguments. 
    
    1. **Argument Organization**: It helps in organizing the input arguments that the script can accept. By defining these arguments, you're effectively creating a user interface for your script.
    2. **Flexibility**: It provides flexibility to the user running the script. The user can customize the behavior of the script by passing different values for these arguments.
    3. **Default Values and Types**: You can set default values and specific data types for each argument. This makes the script more robust as it reduces the risk of runtime errors due to incorrect data types or missing values.
    4. **Help and Documentation**: The parser can automatically generate help and usage messages. This helps users understand what arguments the script accepts and how to use them.
    5. **Error Handling**: It handles errors related to incorrect arguments. The parser can display the correct usage and inform the user about the mistake.
    6. **Additional Arguments at Runtime**: In your script, additional arguments are added (`nepochs`, `ntries`, `lr`, etc.) after the initial parsing. This can be useful for adding arguments that are conditional or context-dependent.
    7. **Code Readability and Maintenance**: Using a parser makes the code more organized and easier to understand and maintain. It separates the argument parsing logic from the main operational logic of the script.
    8. **Integration with Other Systems**: If your script is part of a larger system or workflow, having well-defined command line arguments makes it easier to integrate with other software.

---

[https://aypan17.github.io/machiavelli/](https://aypan17.github.io/machiavelli/)

[https://github.com/aypan17/machiavelli/blob/main/experiments/run_trajectories.py](https://github.com/aypan17/machiavelli/blob/main/experiments/run_trajectories.py)

[https://github.com/fbarez/actbasedoninternal/commit/282433bf176686a60a2682f00963e09ff44aea2d](https://github.com/fbarez/actbasedoninternal/commit/282433bf176686a60a2682f00963e09ff44aea2d)

---

model_edit_deception_draft.ipynb:

[https://colab.research.google.com/drive/1AgTC7ebuZGVJTdh5b4FG9Yu-M0RxdKB0](https://colab.research.google.com/drive/1AgTC7ebuZGVJTdh5b4FG9Yu-M0RxdKB0#scrollTo=97292f90-5c2e-444d-88e4-41265e8ad0d9)

[https://nnsight.net/documentation/models/](https://nnsight.net/documentation/models/)