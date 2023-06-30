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

---

[https://www.reddit.com/r/GoogleColab/comments/xs62o9/what_exactly_is_a_compute_unit/](https://www.reddit.com/r/GoogleColab/comments/xs62o9/what_exactly_is_a_compute_unit/)

- test
    
    After a bit of testing, if you pay for colab pro or for payasyou go, this is what you get.
    
    100 compute units.
    
    You are given a T4 GPU as default same as free tier, but a T4 GPU consumes 1.96 compute units per hour
    
    If you pay for colab pro, you can choose "Premium GPU" from a drop down, I was given a A100-SXM4-40GB - which is 15 compute units per hour
    
    apparently if you choose premium you can be given either at random which is annoying
    
    p100 = 4units/hr
    
    v100 = 5units/hr
    
    a100 =15units/hr
    
    Even if you pay for colab pro it still timesout around after 8-10hrs, in my opinion there is less of reason these days for colab pro since those compute units are quite expensive
    

<<<

- If High Ram:
    
    This notebook was authored in a high RAM runtime environment, and may require more resources than are allocated in the version of Colab that is free of charge.
    

(these change based on what’s being computed. but approx magnitude comparison is:)

CPU: 0.08 compute units per hour

T4: 1.96 per hour

V100: 5.36 compute units per hour

A100: 15

[https://blog.paperspace.com/alternative-to-google-colab-pro/](https://blog.paperspace.com/alternative-to-google-colab-pro/)

---

[https://colab.research.google.com/notebooks/pro.ipynb](https://colab.research.google.com/notebooks/pro.ipynb)

Making the Most of your Colab Subscription

---

NOTE: if drive uploads an .ipynb, don’t copy drive link, copy the colab url either from ad bar or cell