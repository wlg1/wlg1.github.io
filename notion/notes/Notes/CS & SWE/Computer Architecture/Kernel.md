# Kernel

![Untitled](Kernel%20737168abc085435089e11aac6261f5e1/Untitled.png)

[https://www.baeldung.com/cs/os-kernel](https://www.baeldung.com/cs/os-kernel)

**User processes:** User processes actually create the userspace. However, these processes are the applications that the kernel controls. The kernel also enables these processes to communicate with each other. It uses [inter-process communication](https://www.baeldung.com/cs/inter-process-communication) (IPC) mechanisms to enable communication between processes.

**Kernel:** As we can see, it’s right in the middle of the layers. **It’s the core of the OS.**

**Hardware:** It’s the physical machine, the base of the system. It consists of memory, the processor or the central processing unit (CPU), and input/output (I/O) components such as graphics, storage, and networking. The CPU executes computations and reads and writes to memory.

**Objectives of Kernel :**

- To establish communication between user level application and hardware.
- To decide state of incoming processes.
- To control disk management.
- To control memory management.
- To control task management.