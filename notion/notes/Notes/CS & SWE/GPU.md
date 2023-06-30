# GPU

- In colab, is all code faster with a GPU than without one?
    
    Not all code will necessarily be faster with a GPU in Colab. The benefit of using a GPU depends on the type of computations being performed in the code.
    
    GPUs excel at performing matrix operations and other parallelizable computations, making them particularly well-suited for deep learning tasks such as training neural networks. If your code involves heavy matrix operations or other computations that can be parallelized, it is likely that using a GPU will result in faster execution times compared to running the same code on a CPU.
    
    However, if your code involves primarily sequential operations, such as reading and writing files or executing loops with few computations, then using a GPU may not provide any significant speedup over a CPU.
    
    It's also worth noting that there are different types of GPUs with varying performance levels. In Colab, you can choose between a CPU runtime or a GPU runtime, and the GPU runtime offers two different GPU options: a Tesla K80 or a Tesla T4. The T4 is generally faster than the K80, so if you have the option to choose between the two, using the T4 is likely to result in faster execution times.
    
- What advantages do CPUs have over GPUs? When to use GPUs?
    
    GPU cores are smaller and more specialised than the cores on a CPU, this means that they are better for specific applications, but cannot be optimised or used efficiently in as many ways as CPUs.
    
    Use GPUs for NNs with many large MM. If have small NN, using GPU may be slower 
    
    REF: [https://hsf-training.github.io/hsf-training-ml-gpu-webpage/01-introduction/index.html](https://hsf-training.github.io/hsf-training-ml-gpu-webpage/01-introduction/index.html)
    
    <<<
    
    CPU better for sequential
    
    [https://learnopencv.com/demystifying-gpu-architectures-for-deep-learning/](https://learnopencv.com/demystifying-gpu-architectures-for-deep-learning/)
    
- What are mixed-precision computations?
    
    uses different precision levels within a single operation to achieve computational efficiency without sacrificing accuracy.
    
    REF: [https://blogs.nvidia.com/blog/2019/11/15/whats-the-difference-between-single-double-multi-and-mixed-precision-computing/](https://blogs.nvidia.com/blog/2019/11/15/whats-the-difference-between-single-double-multi-and-mixed-precision-computing/#:~:text=Mixed%2Dprecision%2C%20also%20known%20as,values%20for%20rapid%20matrix%20math)
    
- Do cores primarily execute threads?
    
    Yes, cores in a multi-core processor are primarily responsible for executing threads. A thread is a sequence of instructions that can be scheduled and executed independently by a processor core. Each core in a multi-core processor is capable of executing multiple threads simultaneously, known as concurrent execution or parallelism.
    
    The operating system and the hardware work together to manage and schedule threads across the available cores. The operating system's scheduler distributes threads to different cores, taking into account factors like load balancing, priority, and resource allocation. The hardware ensures that each core has access to the necessary resources (registers, cache, etc.) to execute the assigned threads efficiently.
    
    By leveraging multiple cores and executing threads in parallel, processors can achieve higher throughput and improved performance, especially for applications that can be parallelized effectively, such as multi-threaded applications or tasks that can be divided into smaller independent units of work.
    

[https://towardsdatascience.com/what-is-a-gpu-and-do-you-need-one-in-deep-learning-718b9597aa0d](https://towardsdatascience.com/what-is-a-gpu-and-do-you-need-one-in-deep-learning-718b9597aa0d)

Bandwidth is one of the main reasons why GPUs are faster for computing than CPUs. With large datasets, the CPU takes up a lot of memory while training the model.

Computing huge and complex jobs take up a lot of clock cycles in the CPU — CPUs take up jobs *sequentially* and has a fewer number of cores than its counterpart, GPU.

A standalone GPU, on the other hand, comes with dedicated VRAM (Video RAM) memory. Thus, the CPU’s memory can be used for other tasks.

[https://www.digitaltrends.com/computing/what-is-a-teraflop/](https://www.digitaltrends.com/computing/what-is-a-teraflop/)
a teraflop refers to a processor’s capability to calculate one trillion floating-point operations per secon

<<<

[https://lambdalabs.com/blog/multi-node-pytorch-distributed-training-guide](https://lambdalabs.com/blog/multi-node-pytorch-distributed-training-guide)

The code launches `4` workers, where `worker_0` create a tensor on `GPU 0`  of node `104.171.200.62`, and send the tensor to all other three workers.

<<<

[https://huggingface.co/blog/hf-bitsandbytes-integration](https://huggingface.co/blog/hf-bitsandbytes-integration)

<<<<

[https://hsf-training.github.io/hsf-training-ml-gpu-webpage/](https://hsf-training.github.io/hsf-training-ml-gpu-webpage/)

<<<

[https://developer.nvidia.com/blog/cutlass-linear-algebra-cuda/](https://developer.nvidia.com/blog/cutlass-linear-algebra-cuda/)

<<<

[https://learnopencv.com/demystifying-gpu-architectures-for-deep-learning/](https://learnopencv.com/demystifying-gpu-architectures-for-deep-learning/)

CUDA: In this new programming model, different computations could be performed on different devices most suited to that task. For example, since CPUs excel at sequential computations while GPUs, by design, excel at parallel computations, the programming model introduced ways for CPUs and GPUs to exchange data and synchronize their operations. This unified model simplified heterogenous programming and NVIDIA called it Compute Unified Device Architecture or CUDA.

The CUDA programming model has a C/C++ interface for coding both CPU and GPU computations. Bindings also exist for many languages like Python.

<<<

[https://arena-ch3-training-at-scale.streamlit.app/[3.1]_GPUs](https://arena-ch3-training-at-scale.streamlit.app/%5B3.1%5D_GPUs)

[https://pytorch.org/tutorials/recipes/recipes/profiler_recipe.html](https://pytorch.org/tutorials/recipes/recipes/profiler_recipe.html)