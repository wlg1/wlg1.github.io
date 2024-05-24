# New laptop

windows backup

[https://chat.openai.com/c/a426ef39-dc32-4957-8f1e-df5e393291a3](https://chat.openai.com/c/a426ef39-dc32-4957-8f1e-df5e393291a3)

how does windows backup to a new computer work? does it just transfer the files in onedrive, or all programs?

is onedrive located on primary disk, or does it also transfer internal hard drive installed separately?

is onedrive free? why use backblaze if have onedrive?

jm-crv +1.5: jakemy precision screwdriver

[https://www.youtube.com/watch?v=vma_e67Ic0c](https://www.youtube.com/watch?v=vma_e67Ic0c)

**How to install laptop HDD in 2 Minutes 🔥 MSI GF63,**

9.5 mm hdd thickness

[https://chat.openai.com/c/2d850418-21a4-4a2a-a67b-9c4455d41086](https://chat.openai.com/c/2d850418-21a4-4a2a-a67b-9c4455d41086)

The Seagate BarraCuda 8TB Internal Hard Drive (ST8000DMZ04) that you've described is a 3.5-inch SATA drive, typically designed for use in desktop computers. This type of hard drive is larger and requires more power compared to the 2.5-inch drives or solid-state drives (SSDs) that are commonly used in laptops.

Most laptops, including MSI models, are designed to accommodate 2.5-inch hard drives or SSDs, primarily due to size and power consumption considerations. The 3.5-inch drive is too large to physically fit into the standard hard drive bay of a laptop. Additionally, laptops are not generally equipped to provide the necessary power for a 3.5-inch drive.

<<<

- **Seagate (ST2000LX001) FireCuda 2TB Solid State Hybrid Drive Performance SSHD – 2.5 Inch SATA 6Gb/s Flash Accelerated for Gaming PC Laptop**
    1. **Performance:** The most significant difference is in performance. The FireCuda SSHD combines a standard HDD with a small amount of SSD storage. This SSD portion is used to cache frequently accessed data, resulting in faster boot times, quicker application loading, and overall snappier performance compared to a traditional HDD. The BarraCuda HDD, on the other hand, is a standard hard drive without this SSD caching, meaning it will generally be slower in accessing data.
    2. **Cache Size:** The FireCuda has a flash-accelerated cache (the size of the SSD portion is not always specified but is typically around 8GB), while the BarraCuda HDD has a 128MB cache. The flash cache in the FireCuda is much faster than the standard cache in the BarraCuda HDD, contributing to its better performance.
    3. **Spindle Speed:** The BarraCuda HDD has a spindle speed of 5400 RPM. The FireCuda SSHD likely also operates at 5400 RPM for its HDD portion, but the presence of the SSD cache compensates for the slower rotational speed when accessing frequently used data.
    4. **Use Case:** The FireCuda is more suited for users who want a balance between high storage capacity and performance, especially beneficial for gaming or for running applications that benefit from faster load times. The BarraCuda HDD is more for those who prioritize storage capacity and are okay with standard HDD speeds, such as for general data storage or less demanding applications.

---

- **Apps keep pinning after start up on Windows 11**
    
    [https://answers.microsoft.com/en-us/windows/forum/all/apps-keep-pinning-after-start-up-on-windows-11/b7fdf2fa-f932-455b-865b-d3175d8ef1df](https://answers.microsoft.com/en-us/windows/forum/all/apps-keep-pinning-after-start-up-on-windows-11/b7fdf2fa-f932-455b-865b-d3175d8ef1df)
    
    1. Search notepad in the start menu, right-click, and run as administrator
    
    2. From notepad, click File > Open then paste this in the file path, "C:\Users\*YourUserHere*\AppData\Local\Microsoft\Windows\Shell\" (replace the *YourUserHere* and if there are no results make sure the filter at the bottom right is set to all files and not just .txt ones)
    
    3. Open LayoutModification.xml (you might want to make a copy of it just to be safe)
    
    4. Use ctrl+f to search "TaskbarPinList"
    
    5. Delete [what’s needed] between <TaskbarPinList> and </TaskbarPinList>
    
    6. Make sure to save before you close and restart the computer
    
    This is a tutorial with basically the same (just slightly different) steps if you want to look at that too: [https://www.thewindowsclub.com/apps-keep-pinning-themselves-on-startup-to-the-taskbar](https://www.thewindowsclub.com/apps-keep-pinning-themselves-on-startup-to-the-taskbar)