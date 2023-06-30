# Docker

[https://www.docker.com/blog/build-machine-learning-apps-with-hugging-faces-docker-spaces/](https://www.docker.com/blog/build-machine-learning-apps-with-hugging-faces-docker-spaces/)

- Docker for AI
    - ✅ New HuggingFace Space
    - ✅ In space, make new ‘requirements.txt’ and ‘app.py’ using FastAPI
    - ✅ Dockerfile to set up container env, reqs, and run app on port
        - ✅ get it to auto-build on HF; MUST capitalize “Dockerfile”
        - ✅ solve error:
            
            ---
            
            16 |     USER user
            17 |     # Set home to the user's home directory
            18 | >>> ENV HOME=/home/user \\
            19 |         PATH=/home/user/.local/bin:$PATH
            
            20
            
            ---
            
            error: failed to solve: Syntax error - can't find = in "\\\\". Must be of the form: name=value
            
            ---
            
            SOLN:
            
            The error message suggests that there is a syntax error in the line where you set the `HOME` and `PATH` environment variables in your code. It seems that you are using a double backslash (`\\\\`) instead of a single equal sign (`=`) to assign values to the variables.
            
            To resolve this error, you should modify the line to use a single equal sign for assignment. Here's the corrected code:
            
            ```
            USER user
            # Set home to the user's home directory
            ENV HOME=/home/user \\
                PATH=/home/user/.local/bin:$PATH
            
            ```
            
            By using a single equal sign, you can assign the desired values to the `HOME` and `PATH` environment variables.
            
        - In app tab:
        {"detail":"Not Found"}
            
            The error message "detail: Not Found" typically indicates that the requested resource or endpoint is not found. This error commonly occurs when the URL or API endpoint you are trying to access is incorrect or does not exist.
            
            To resolve this issue, you can check the following:
            
            1. Verify the URL or API endpoint you are trying to access. Make sure it is correct and corresponds to a valid resource.
            2. Ensure that you have the necessary permissions and authentication to access the resource.
            3. Double-check the API documentation or any relevant documentation to ensure you are using the correct endpoints and parameters.
            
            If you are still facing difficulties, providing more context or sharing the specific code or request you are making can help in identifying the problem more accurately.
            

---

[https://learn.microsoft.com/en-us/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package](https://learn.microsoft.com/en-us/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package)

---

Follow Learning Center tutorials on Docker Desktop

Put Dockerfile in workspace, cd to workspace, then build an image by running:

`docker build -t welcome-to-docker .`

On left hand panel, click on images (cloud icon) tab. Click on the new image and run it (top right) on a port. Click on the port name to go to the [localhost](http://localhost) site it’s run on.

---

- Can you deploy with just docker, or do you need AWS?
    
    Use any hosting service that supports Docker, such as DigitalOcean, Linode, or even your own on-premises servers. AWS offers a range of services that can be used to deploy and manage Docker containers
    
- What's an example of a compatibility issue and how does docker solve it?
    
    When an application requires specific versions of system libraries or dependencies that are not available or compatible with the underlying operating system. 
    
    A Docker container is a self-contained runtime environment for your application, including exact versions of its dependencies and libraries. Docker will ensure that they are installed and configured correctly within the container.
    
    Containers are easily moved between different environments, such as from a local machine to a production server. This helps to ensure that your application runs consistently and predictably across different environments.
    
- If docker uses the host os, how can there be compatibility if the libraries aren't compatible with host os?
    
    While Docker containers share the same host operating system kernel, they are isolated from the host system and other containers using a variety of techniques, including namespaces and cgroups.
    
    Namespaces provide a way to isolate resources at the kernel level, such as the network, file system, and process trees. This allows containers to have their own view of the system, including their own file system, network stack, and process tree, while still sharing the same underlying kernel with the host system.
    
    Cgroups, on the other hand, provide a way to limit and isolate resource usage for each container, such as CPU, memory, and disk I/O. This helps to ensure that containers do not monopolize system resources and can coexist peacefully on the same host system.
    
    So, even if a library is not compatible with the host operating system, it can still be installed and used within a Docker container, as long as the container's underlying operating system is compatible with the library. 
    
- Docker container vs virtual machine?
    
    While virtual machines emulate an entire operating system, including the kernel, Docker containers share the host operating system kernel and run only the application and its dependencies, making them much more lightweight and efficient than virtual machines.
    
    A virtual machine (VM) is a complete operating system installed on top of a hypervisor layer, which emulates the underlying hardware of the host machine. Each VM runs its own [Kernel](https://www.notion.so/Kernel-a33bfea1365f46078d9ca7975ab09874?pvs=21) and has its own resources, including CPU, memory, and storage. This makes VMs heavyweight and resource-intensive, but also allows for complete isolation between different VMs and the host system.
    
    On the other hand, Docker containers are lightweight, portable, and share the same host operating system kernel. Each container is isolated from the host system and other containers on the same host, but shares the same system resources, such as CPU and memory. Containers use a layered file system that allows them to share common files and libraries while still maintaining isolation.
    
    In summary, the key differences between Docker containers and virtual machines are:
    
    1. Resource usage: Containers are more lightweight and consume fewer resources compared to virtual machines, which require separate OS installations and dedicated resource allocations.
    2. Hypervisor: Virtual machines run on a hypervisor, whereas Docker containers leverage the host OS's kernel directly.
    
    Containers are commonly used for application packaging, deployment, and scaling, while virtual machines are often employed for running multiple operating systems simultaneously.
    
    Both virtual machines and Docker containers provide a way to isolate applications and their dependencies.
    
- Why use vm over docker?
    
    While Docker has many advantages over virtual machines (VMs), there are still some scenarios where using a VM might be preferable.
    
    One reason to use a VM over Docker is when you need to run an application that requires a different operating system than the host machine. For example, if you need to run an application that only works on Windows, but your development environment is Linux-based, you may need to use a VM to run the Windows application.
    
    Another reason to use a VM is when you need complete isolation between the host machine and the application. VMs provide a high degree of isolation, including their own kernel and file system, which makes them more secure and less vulnerable to attacks.
    
    Additionally, VMs can provide better performance in some scenarios, especially when running applications that require a lot of resources, such as video rendering or scientific simulations. Since VMs have their own resources, including CPU, memory, and disk, they can be optimized specifically for the needs of the application, which can lead to better performance.
    
    In summary, while Docker has many advantages over VMs, such as portability, efficiency, and ease of use, there are still some scenarios where using a VM might be preferable, such as when running an application that requires a different operating system or when requiring complete isolation between the host machine and the application.
    
- How can a VM be built? What if the VM resources are larger than host's?
    
    A virtual machine (VM) can be built using virtualization software, such as VMware, VirtualBox, or Hyper-V. These tools allow you to create and manage virtual machines on your host machine, which can be used to run guest operating systems and applications.
    
    To create a VM, you typically start by specifying the desired hardware resources for the virtual machine, such as the amount of CPU, memory, disk space, and network interfaces. You can then install an operating system on the virtual machine, just as you would on a physical machine.
    
    Once the VM is set up, you can run it on the host machine, either directly on the host hardware or within a hypervisor layer, depending on the virtualization software used. The guest operating system runs within the virtual machine, which provides a virtual CPU, memory, and other hardware resources.
    
    Regarding your second question, if the resources required by the virtual machine are larger than the resources available on the host machine, the virtual machine may not be able to run at full capacity. In this case, the virtualization software may limit the resources available to the virtual machine or may use techniques such as swapping or ballooning to manage memory usage.
    
    Swapping involves temporarily moving data from memory to disk, to free up memory for other processes. Ballooning involves reclaiming memory from the guest operating system by using a balloon driver to request memory from the guest and then releasing it back to the host when needed.
    
    However, it's generally best to ensure that the resources allocated to a virtual machine are not significantly larger than the resources available on the host machine, to avoid performance issues and ensure the best possible performance for the virtual machine.
    

- If I am building an app that downloads pdfs from arxiv, stores them in a database, then calls a language models to retrieve chunks of those pdfs, why do I need to deploy it as a docker instance?
    
    Firstly, Docker allows you to package your entire application along with its dependencies, configuration, and libraries into a single container, ensuring that it can run consistently and reliably on any machine that supports Docker. This means that you can develop your application on your local machine and then deploy it to a remote server with ease, without worrying about compatibility issues.
    
    Secondly, Docker provides a lightweight, isolated runtime environment that helps to minimize conflicts between your application and the underlying system. This can help to improve security and reduce the risk of dependency conflicts.
    
    Thirdly, deploying your app as a Docker instance can make it easier to scale your application horizontally by spinning up multiple instances of the container. This can help to improve performance and ensure high availability, particularly when dealing with large-scale applications or high levels of traffic.
    
    In summary, deploying your app as a Docker instance offers several benefits, including improved portability, better security and isolation, and easier scaling. By using Docker, you can ensure that your application runs consistently and reliably across different environments, while also making it easier to manage and maintain over time.
    

---

[https://www.youtube.com/watch?v=Gjnup-PuquQ&ab_channel=Fireship](https://www.youtube.com/watch?v=Gjnup-PuquQ&ab_channel=Fireship)
Docker in 100 Seconds

[https://www.youtube.com/watch?v=gAkwW2tuIqE&t=374s&ab_channel=Fireship](https://www.youtube.com/watch?v=gAkwW2tuIqE&t=374s&ab_channel=Fireship)
Learn Docker in 7 Easy Steps - Full Beginner's Tutorial

docker desktop + docker ext for IDE (vscode)

<<<
[https://www.youtube.com/watch?v=eGz9DS-aIeY&ab_channel=NetworkChuck](https://www.youtube.com/watch?v=eGz9DS-aIeY&ab_channel=NetworkChuck)
you need to learn Docker RIGHT NOW!! // Docker Containers 101

4m30s: while VMs virtualize the hardware, docker virts the OS.

15m: pull the image and run. it has all the dependencies, etc needed to run the site on ANY computer

17m: fast b/c only needs 1 kernel. VMs' OS each have their own kernel

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
[https://www.youtube.com/watch?v=PziYflu8cB8&ab_channel=Fireship](https://www.youtube.com/watch?v=PziYflu8cB8&ab_channel=Fireship)
Kubernetes Explained in 100 Seconds

manages docker containers

<<<
[https://www.youtube.com/watch?v=7bA0gTroJjw&ab_channel=NetworkChuck](https://www.youtube.com/watch?v=7bA0gTroJjw&ab_channel=NetworkChuck)
you need to learn Kubernetes RIGHT NOW!!

when lots of traffic, host may crash. so set up more host servers (mroe containers). load balancer manages who goes to what server to prevent crashes. may even have moer load balancers. and updates mean a change to each container (in each server). so automate this w/ kb

cost of master nodes and worker nodes