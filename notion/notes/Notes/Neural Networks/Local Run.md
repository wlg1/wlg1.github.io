# Local Run

https://youtu.be/WxYC9-hBM_g?si=2wpSU30z3ZCo-ga4

Run your own llama

Setup: [https://ollama.com/](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbUNMcVVPa0dSZWpKWDdwZ3pTR2h0MHBPaFZvUXxBQ3Jtc0tuQ3Z4YXRiUDNOWGVJWFNMUTduYU5DTGlYSEFja0hIbEN1WmF6YV9uOWpNWnJMdWJQZzR2alltTzg2bDV2SHN5ZVFlOGt1QjBXR05EYWFPd2JlZkhsNE1pSFVxZzdGS2E1WkR4S3ZQRDlqZnBiX1FONA&q=https%3A%2F%2Follama.com%2F&v=WxYC9-hBM_g)

Windows is only a preview. Thus, use linux vers using WSL

[Windows Subsys Linux](../CS%20&%20SWE%20f7436b5aff924c04aa569007bb061038/Linux%201813a7ba23cd4e458006a25c8c7d61b0/Windows%20Subsys%20Linux%20dad83ec4cbf140aebe0eec5ce5e162d1.md)

 `curl -fsSL https://ollama.com/install.sh | sh`

ollama is a library with API for managing local llama models

`ollama run llama2`

this downloads llama2

- if your laptop has a gpu like rtx, will installing llama2 via ollama using wsl auto run llama2 using the gpu? use both your knowledge and look it up on the web
    
    To utilize an RTX GPU with Llama-2 installed via oLLaMa on WSL, it's not automatically guaranteed that Llama-2 will use the GPU. You'll need to ensure a few key configurations are in place for GPU acceleration to be enabled within your WSL environment, particularly for applications that can leverage NVIDIA CUDA.
    
    Firstly, it's critical to have the correct setup for WSL to utilize NVIDIA GPUs. Windows 11 and Windows 10 (version 21H2 onwards) support running machine learning tools, libraries, and frameworks like PyTorch and TensorFlow with GPU hardware acceleration inside a WSL instance. This setup requires:
    
    - Installing the NVIDIA CUDA-enabled driver for WSL.
    - Ensuring your WSL version and Linux distribution are correctly installed and updated.
    - Verifying that your kernel version supports GPU acceleration【13†source】.
    
    NVIDIA has integrated its CUDA platform with WSL, enabling developers and users to run AI and machine learning applications with GPU acceleration under a Linux environment on Windows. This integration provides access to the NVIDIA software stack, including CUDA and DirectML support for WSL, which you can download from NVIDIA's official site【14†source】.
    
    However, directly for oLLaMa and Llama-2, while the documentation and GitHub repository provide extensive guidance on setting up and running various models locally, including Llama-2, they do not explicitly detail the process for enabling GPU acceleration through CUDA within WSL【12†source】. It's generally understood that if your WSL setup correctly supports CUDA, applications capable of utilizing GPU acceleration, such as those running through oLLaMa, should be able to leverage it as long as they're compatible with CUDA and the application is configured to use the GPU.
    
    Therefore, after ensuring your WSL environment is set up for NVIDIA CUDA, the next steps would involve:
    
    - Checking oLLaMa's documentation for any specific flags or configuration options required to enable GPU use.
    - Verifying that Llama-2 itself supports CUDA acceleration and is configured to utilize it when available.
    
    In practice, if your system and WSL environment are properly configured to support CUDA, and Llama-2 is capable of GPU acceleration, it should be able to leverage your RTX GPU automatically or with minor configuration adjustments. Always ensure that your GPU drivers and CUDA installation are up to date to avoid compatibility issues.
    

<<<

Fine Tuning

Pre-train took 6000 GPUs and 1.7 million GPU hours

11m40s: VMware private AI includes all resources in 1 package for fine tuning

[https://www.vmware.com/products/vsphere/ai-ml.html](https://www.vmware.com/products/vsphere/ai-ml.html)

13m30s: fine tuning nb

instead of 7B, change 65 mil parameters (only ~1%)

prompt tuning: just prompts with answers

3-4 mins

<<<

RAG: connect LLM to vector database

[https://docs.privategpt.dev/installation/getting-started/main-concepts](https://docs.privategpt.dev/installation/getting-started/main-concepts)

[https://medium.com/@docteur_rs/installing-privategpt-on-wsl-with-gpu-support-5798d763aa31](https://medium.com/@docteur_rs/installing-privategpt-on-wsl-with-gpu-support-5798d763aa31)