# ISSUE: GPT-2-XL is bad at writing in styles, and GPT-J too big to load

ISSUE:

Your session crashed after using all available RAM. As a Colab Pro user, you have higher memory than non-subscribed users, but if you are interested in even higher RAM runtimes, you may want to check out

POSS NEXT STEPS:

- Find ways to load GPT-J using GPUs that can run it
    - Try running on TPU in colab
        
        still has issue
        
        - How do I find out the total RAM I had in colab and how much was used?
            
            You can find the total amount of RAM available in your Colab runtime and how much RAM is being used by running the following code in a code cell:
            
            ```
            !cat /proc/meminfo
            ```
            
            This will output the memory information of your Colab runtime, including the total amount of memory available, the amount of memory used, and the amount of free memory.
            
            Alternatively, you can use the `psutil` library in Python to get the memory usage of your Colab runtime as shown below:
            
            ```
            !pip install psutil
            
            import psutil
            
            # Get the memory usage of the current process
            memory_info = psutil.Process().memory_info()
            
            # Print the memory usage in bytes
            print(memory_info.rss)
            
            ```
            
            This will print the amount of memory used by the current Python process in bytes. You can convert this to a more human-readable format, such as megabytes or gigabytes, by dividing the value by the appropriate number. For example:
            
            ```
            memory_usage_mb = memory_info.rss / 1024 / 1024
            print(f"Memory usage: {memory_usage_mb:.2f} MB")
            
            ```
            
        
        NOTE: when system RAM (check resources panel for its usage in real time) is full, it crashes and resets the entire run
        
    - Try reducing the batch size
    - https://github.com/huggingface/transformers/issues/14839
        
        [https://betterprogramming.pub/fine-tuning-gpt-j-6b-on-google-colab-or-equivalent-desktop-or-server-gpu-b6dc849cb205](https://betterprogramming.pub/fine-tuning-gpt-j-6b-on-google-colab-or-equivalent-desktop-or-server-gpu-b6dc849cb205)
        
    - Look at recent papers that analyzed it to see how they loaded it into colab (their reqs, etc)
- Run other expms on GPT-2 for now (eg. [https://www.neelnanda.io/mechanistic-interpretability/attribution-patching](https://www.neelnanda.io/mechanistic-interpretability/attribution-patching) )
- Didn’t use “low_cpu_mem_usage” before:

```
/usr/local/lib/python3.9/dist-packages/transformers/modeling_utils.py in from_pretrained(cls, pretrained_model_name_or_path, *model_args, **kwargs)
   2624             init_contexts = [deepspeed.zero.Init(config_dict_or_path=deepspeed_config())] + init_contexts
   2625         elif load_in_8bit or low_cpu_mem_usage:
-> 2626             init_contexts.append(init_empty_weights())
   2627   2628         with ContextManagers(init_contexts):

```

```
NameError: name 'init_empty_weights' is not defined
```

ISSUE: The old library can’t support GPT-J inside colab now. But the old library was the one that contained low_cpu_mem_usage

[https://github.com/huggingface/transformers/issues/21039](https://github.com/huggingface/transformers/issues/21039)

---

[https://colab.research.google.com/github/EleutherAI/GPTNeo/blob/master/GPTNeo_example_notebook.ipynb](https://colab.research.google.com/github/EleutherAI/GPTNeo/blob/master/GPTNeo_example_notebook.ipynb)

[https://github.com/EleutherAI/gpt-neo](https://github.com/EleutherAI/gpt-neo)