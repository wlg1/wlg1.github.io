# Quiz- GPUs

- What is a core?
    
    A chip that performs calculations
    
    REF: [https://hsf-training.github.io/hsf-training-ml-gpu-webpage/01-introduction/index.html](https://hsf-training.github.io/hsf-training-ml-gpu-webpage/01-introduction/index.html)
    
- What is a processor?
    
    A component containing cores, using them to carry out instructions. CPUs, GPUs, etc are types of processors.
    
    REF: [https://www.techtarget.com/whatis/definition/processor](https://www.techtarget.com/whatis/definition/processor)
    
- What is a thread?
    
    A thread is a sequence of instructions that can be scheduled and executed independently by a processor core
    
- What is a scheduler? What factors does it account for (name 3)? What resources (name 2)?
    
    The operating system's scheduler distributes threads to different cores, taking into account factors like load balancing, priority, and resource allocation. The hardware ensures that each core has access to the necessary resources (registers, cache, etc.) to execute the assigned threads efficiently.
    
- Name 2 ways processors parallelize (based on above terms)
    
    Multicore and multithread 
    
- How do GPUs differ from CPUs in terms of cores? What types of cores are in GPUs?
    
    GPUs have 1000s of small cores, while multi-core CPUs only have several
    GPUS have CUDA cores
    
- What advantages do CPUs have over GPUs? When to use GPUs?
    
    GPU cores are smaller and more specialised than the cores on a CPU, this means that they are better for specific applications, but cannot be optimised or used efficiently in as many ways as CPUs.
    
    Use GPUs for NNs with many large MM. If have small NN, using GPU may be slower 
    
    REF: [https://hsf-training.github.io/hsf-training-ml-gpu-webpage/01-introduction/index.html](https://hsf-training.github.io/hsf-training-ml-gpu-webpage/01-introduction/index.html)
    
    <<<
    
-