# Colab / Jupyter

You should save as both .ipynb and .py during development to record the changes on github (.ipynb won’t show fine changes in commits!). After development is done, either move that folder to “old files” or delete it (the commits showing incr changes will still be there).

---

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

when you upload a notebook, it will appear in the Colab Notebooks folder by default, instead of the new notebook you created; it will not replace that new untitlted notebook. so you need to move it and delete the old untitlted one

---

note- if run all very quick and download multp files at once in colab in between, files wont downlaod until finish executing or interruppt execution

[https://chat.openai.com/c/6c5cac0c-b647-4099-8c5f-8003b5a82848](https://chat.openai.com/c/6c5cac0c-b647-4099-8c5f-8003b5a82848)

note- tpu doesn’t work with transformerlens or jax: 'numpy.linalg._umath_linalg' has no attribute '_ilp64’

---

- how come I can run a script on colab's A100 fine, but when I run it using !python on colab with A100 there's cuda out of memory error?
    1. **Different Execution Environments**: Running scripts directly in a notebook cell (e.g., using `!python script.py`) versus running Python code in the notebook's native cells might allocate resources differently. The native Colab environment might handle memory more efficiently or differently compared to invoking a script via the command line within Colab.
    2. **Memory Overhead of the Python Interpreter**: When you run a script using `!python`, you're essentially starting a new Python interpreter on top of the one that's already running your notebook. This additional interpreter can consume extra memory, potentially leading to OOM errors, especially if your script is memory-intensive.
    3. **CUDA Contexts**: Running the script with `!python` might create a new CUDA context, which consumes additional GPU memory. Multiple CUDA contexts can lead to increased memory usage, which might not be as efficiently managed as when running directly in the notebook's Python environment.
    4. **Memory Not Released**: If you've run other operations on the GPU before executing your script with `!python`, it's possible that not all GPU memory was released properly. This can happen if previous executions have allocated memory that hasn't been cleared. Running scripts in the native environment might benefit from Colab's memory management, potentially avoiding this issue.
    5. **Differences in Environment Setup**: There might be differences in how the Python environment is configured when executing a script using `!python` versus running code directly in a notebook cell. These differences can affect library versions, memory allocation, and other factors that impact GPU memory usage.