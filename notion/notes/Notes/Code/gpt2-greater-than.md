# gpt2-greater-than

[https://github.com/redwoodresearch/rust_circuit_public](https://github.com/redwoodresearch/rust_circuit_public)

[https://docs.conda.io/projects/miniconda/en/latest/](https://docs.conda.io/projects/miniconda/en/latest/)

(6 linux command lines)

Then restart shell and use: `conda create -n circ python=3.11 -y`

[https://chat.openai.com/c/02b1a654-105e-414f-8dbd-12559085fcf7](https://chat.openai.com/c/02b1a654-105e-414f-8dbd-12559085fcf7)

can i use "pip install maturin==0.14.7" then separately install [patchelf] dependency for it, or is the dependency required during maturin installation?

pip install patchelf

pip install maturin==0.14.7

`pip install attrs cattrs blake3 numpy msgpack websockets`

(nav to folder of repos, click filepath to open in terminal)

git clone [https://github.com/redwoodresearch/rust_circuit_public.git](https://github.com/redwoodresearch/rust_circuit_public.git)

`conda activate circ`

sudo apt-get install cmake

cd to the repo with the cargo.toml file, then `maturin develop --features static-z3`

Some crates, especially those with complex or extensive code bases or those that rely on external libraries, can take a long time to compile.

[https://stackoverflow.com/questions/40700039/how-can-you-clone-a-conda-environment-into-the-root-environment](https://stackoverflow.com/questions/40700039/how-can-you-clone-a-conda-environment-into-the-root-environment)

[https://chat.openai.com/c/99b58615-8af6-4c6e-af8c-6d34d6bb20e3](https://chat.openai.com/c/99b58615-8af6-4c6e-af8c-6d34d6bb20e3)

how do I change the folder dir that loads gpt2 to the current folder in this code?

no need to do that b/c the fn that calls it uses rust_circuits. instead, go to home folder (first dir opened in gui) in linux and paste rrfs/tensor_db/[gpt2 files] there.

I am using a dual boot windows and linux. I have nvidia cuda access on windows but not on linux. do i have to install nvidia separately on linux or can I use it thru windows?

If you're using a dual-boot system with both Windows and Linux, the installations and configurations of software on each operating system are independent of each other. This means that software, drivers, and configurations done on Windows do not directly affect Linux and vice versa.

If you're using Ubuntu, the simplest way is to let the system recommend the best driver for you. Run the following commands:

`sudo ubuntu-drivers devices`

`sudo ubuntu-drivers autoinstall`

The `recommended` tag indicates the version that is suggested for your system based on compatibility and stability.

`sudo apt install nvidia-driver-470`

Reboot computer

- ERROR: cuda out of memory
    
    /gpt2-greater-than$ python circuit_discovery.py
    Traceback (most recent call last):
    File "/media/linux/2TB HDD/Documents/_prog/repos_DL/gpt2-greater-than/circuit_discovery.py", line 80, in <module>
    baseline_mean = se(c).mean()
    ^^^^^
    File "/media/linux/2TB HDD/Documents/_prog/repos_DL/gpt2-greater-than/circuit_discovery.py", line 66, in se
    return transform.sample(c).evaluate()
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    File "/media/linux/2TB HDD/Documents/_prog/repos_DL/rust_circuit_public/rr_util/rust_circuit_type_utils.py", line 192, in <lambda>
    einsum = lambda tensors_and_axes, out_axes: torch.einsum(*itertools.chain(*tensors_and_axes), out_axes)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    File "/home/linux/miniconda3/envs/circ/lib/python3.11/site-packages/torch/functional.py", line 378, in einsum
    return _VF.einsum(equation, operands)  # type: ignore[attr-defined]
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    torch.cuda.OutOfMemoryError: CUDA out of memory. Tried to allocate 20.00 MiB (GPU 0; 5.94 GiB total capacity; 5.06 GiB already allocated; 5.06 MiB free; 5.33 GiB reserved in total by PyTorch) If reserved memory is >> allocated memory try setting max_split_size_mb to avoid fragmentation.  See documentation for Memory Management and PYTORCH_CUDA_ALLOC_CONF
    

The NVIDIA GeForce GTX 1060 Mobile GPU typically comes with either 3GB or 6GB of VRAM (memory).

T4: 16GB GDDR6
GTX 1060: Comes in variants with either 3GB or 6GB GDDR5.

- if I install rust_circuits locally, can I use colab to run code using rust_circuits using colab's t4 gpus?
    
    Using local libraries in Google Colab with Colab's GPUs requires a bit of setup and, in some cases, workarounds. Here's a general approach to using a local library like `rust_circuits` with Colab:
    
    1. **Packaging the Local Library**:
        - If `rust_circuits` can be packaged (e.g., as a `.whl` or `.tar.gz` file), you can upload it to Colab and then install it directly within the notebook.
    2. **Uploading to Colab**:
        - Use the Colab interface to upload the library package:
            
            ```python
            from google.colab import files
            uploaded = files.upload()
            
            ```
            
        - Then, install the uploaded package:
            
            ```python
            !pip install <package_name>.whl
            
            ```
            
    3. **Shared Drives**:
        - If the library is large or consists of multiple files, consider using Google Drive to store the library and then mount the drive in Colab to access it.
            
            ```python
            from google.colab import drive
            drive.mount('/content/drive')
            
            ```
            
    4. **Using Colab's GPUs**:
        - Once the library is available in the Colab environment, you can use it just like any other library. Colab's GPUs (like the T4) can be utilized as long as the library and your code are set up to leverage GPU acceleration.
    5. **Potential Issues**:
        - **Dependencies**: Ensure that all dependencies of `rust_circuits` are available in the Colab environment. You might need to install additional packages or libraries.
        - **Binary Compatibility**: If `rust_circuits` includes compiled binaries, they must be compatible with the Colab environment. In some cases, you might encounter issues if the binaries were compiled for a different architecture or system.
        - **Persistent Installation**: Remember that changes in Colab, including library installations, are temporary. If you restart your Colab kernel or start a new session, you'll need to reinstall and reconfigure everything.
    
    Given the potential complexities, especially if `rust_circuits` involves Rust components or compiled binaries, it might require some trial and error to get everything running smoothly in Colab. Always ensure you have backups of your work, and test thoroughly to ensure the library functions as expected in the Colab environment.