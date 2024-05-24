# GPU Training at Scale

[https://github.com/tatsu-lab/stanford_alpaca](https://github.com/tatsu-lab/stanford_alpaca)

- what does this mean: machine with 4 A100 80G GPUs in FSDP full_shard mode.
    
    The phrase "machine with 4 A100 80G GPUs in FSDP full_shard mode" refers to a computing setup that includes:
    
    - **4 A100 80G GPUs**: This specifies that the machine is equipped with four NVIDIA A100 GPUs, each with 80 GB of VRAM (Video RAM). The NVIDIA A100 is designed for data centers and offers significant computational power for machine learning, deep learning, and high-performance computing tasks. The 80 GB of VRAM per GPU allows for processing large datasets and models that require a lot of memory.
    - **FSDP (Fully Sharded Data Parallel)**: FSDP is a distributed deep learning training approach that shards (splits) the model across multiple GPUs to reduce the memory footprint on each GPU. This means that each GPU only stores a portion of the model's parameters at any given time during training, which allows for training larger models or increasing batch sizes without running out of memory.
    - **Full Shard Mode**: In the context of FSDP, "full shard mode" likely refers to fully sharding the model's parameters across all available GPUs. This is opposed to partially sharding the model where only some of the model's parameters are sharded. Full sharding maximizes memory efficiency by distributing the entire model's parameters across the GPUs, ensuring that each GPU is utilized to its fullest potential in terms of memory usage.
    
    In summary, a "machine with 4 A100 80G GPUs in FSDP full_shard mode" is a high-performance computing setup optimized for training very large deep learning models. It leverages both the substantial memory capacity of the A100 GPUs and the memory efficiency of fully sharded data parallelism to handle tasks that are extremely demanding in terms of computational and memory resources. This setup is particularly beneficial for training state-of-the-art models in AI research and development, where maximizing the utilization of available hardware resources is crucial.
    

[https://engineering.fb.com/2021/07/15/open-source/fsdp/](https://engineering.fb.com/2021/07/15/open-source/fsdp/)

In standard DDP training, every worker processes a separate batch and the gradients are summed across workers using an [all-reduce operation](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/usage/collectives.html#allreduce). While DDP has become very popular, it takes more GPU memory than it needs because the model weights and optimizer states are replicated across all DDP workers.

One method to reduce replications is to apply a process called full parameter sharding, where only a subset of the model parameters, gradients, and optimizers needed for a local computation is made available.

[https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/usage/collectives.html#allreduce](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/usage/collectives.html#allreduce)

---

[https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html](https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html)

CUDA C++ extends C++ by allowing the programmer to define C++ functions, called *kernels*, that, when called, are executed N times in parallel by N different *CUDA threads*, as opposed to only once like regular C++ functions.

---

[https://courses.nvidia.com/courses/course-v1:DLI+T-AC-01+V1/](https://courses.nvidia.com/courses/course-v1:DLI+T-AC-01+V1/)

[https://developer.nvidia.com/blog/even-easier-introduction-cuda/](https://developer.nvidia.com/blog/even-easier-introduction-cuda/)

function that the GPU can run, called a *kernel* in CUDA

[https://colab.research.google.com/github/NVDLI/notebooks/blob/master/even-easier-cuda/An_Even_Easier_Introduction_to_CUDA.ipynb](https://colab.research.google.com/github/NVDLI/notebooks/blob/master/even-easier-cuda/An_Even_Easier_Introduction_to_CUDA.ipynb)

---

[https://www.nvidia.com/en-us/training/](https://www.nvidia.com/en-us/training/)

[https://courses.nvidia.com/courses/course-v1:DLI+C-AC-02+V1/](https://courses.nvidia.com/courses/course-v1:DLI+C-AC-02+V1/)

---

[https://www.quora.com/How-does-the-GPUs-use-of-advanced-techniques-from-the-field-of-category-theory-such-as-monads-and-functors-impact-its-performance-and-efficiency-in-tasks-such-as-functional-programming-and-software-engineering](https://www.quora.com/How-does-the-GPUs-use-of-advanced-techniques-from-the-field-of-category-theory-such-as-monads-and-functors-impact-its-performance-and-efficiency-in-tasks-such-as-functional-programming-and-software-engineering)

Monads, a concept from category theory, provide a way to structure computations in a functional programming language. Monads provide a way to sequence operations and manage side effects, such as input/output and error handling, in a predictable and consistent manner. This can lead to more efficient and maintainable code, as well as improved performance due to the ability to reason about and optimize the code more easily.

Functors, another concept from category theory, provide a way to map functions over the elements of a data structure, such as a list or a tree. This can lead to more efficient and concise code, as well as improved performance due to the ability to apply operations to large data sets in parallel.

https://www.marktechpost.com/2024/03/15/zhejiang-university-researchers-propose-fuyou-a-low-cost-deep-learning-training-framework-that-enables-efficient-100b-huge-model-fine-tuning-on-a-low-end-server-with-a-low-end-gpu-and-limited-cpu-mem/

https://www.reddit.com/r/MachineLearning/s/wE26u9VQQh