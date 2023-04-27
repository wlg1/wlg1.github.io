# Colab / Jupyter

- %load_ext autoreload
%autoreload 2
    
    These two lines of code are typically used in Jupyter Notebook or IPython environments to enable automatic reloading of modules that have been edited.
    
    When **`%load_ext autoreload`** is executed, it loads the autoreload extension, which provides the **`%autoreload`** magic command.
    
    When **`%autoreload 2`** is executed, it sets the autoreload mode to automatically reload all modules (except those excluded via the **`%aimport`** command) before executing any code.
    
    This can be useful when you are working on a large codebase and frequently edit the source code. By using **`%autoreload 2`**, you can avoid having to manually reload the modules every time you make a change.
    
    Here's an example of how to use these two lines of code:
    
    ```
    pythonCopy code
    %load_ext autoreload
    %autoreload 2
    
    import my_module
    
    # Edit my_module.py in another window
    # When you run the following line, my_module will be automatically reloaded
    my_module.my_function()
    
    ```
    

---

Prevent colab from stopping execution:

```
%%capture
# Set the maximum amount of time to run the notebook to 24 hours
import time
import subprocess

def sleep_minutes(minutes):
    for i in range(minutes):
        print(f"Time left: {minutes-i} minutes")
        time.sleep(60)

# Run a command to keep the notebook running
subprocess.Popen(["tail", "-f", "/dev/null"])

# Sleep for 5 hours to make sure the runtime limit is not reached
sleep_minutes(300)
```