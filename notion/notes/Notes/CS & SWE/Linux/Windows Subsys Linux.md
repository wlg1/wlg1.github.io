# Windows Subsys Linux

[https://learn.microsoft.com/en-us/windows/wsl/install](https://learn.microsoft.com/en-us/windows/wsl/install)

Developers can access the power of both Windows and Linux at the same time on a Windows machine. The Windows Subsystem for Linux (WSL) lets developers install a Linux distribution (such as Ubuntu, OpenSUSE, Kali, Debian, Arch Linux, etc) and use Linux applications, utilities, and Bash command-line tools directly on Windows, unmodified, without the overhead of a traditional virtual machine or dualboot setup.

`wsl --install`

- on windows 11 i didn't see enter username for wsl install
    
    When you restart and open the cmd prompt then go to new tab → Ubuntu, it will ask you
    
- how to use wsl after installing? how to access each time restart computer?
    
    After you've installed Windows Subsystem for Linux (WSL) and set up your preferred Linux distribution on Windows 11, using it is quite straightforward. Here's a guide to help you access and use WSL each time you restart your computer:
    
    ### Launching WSL
    
    There are several ways to access WSL on Windows 11:
    
    1. **Start Menu**:
        - Open the Start menu, then scroll down to the Linux distribution you've installed (e.g., Ubuntu). Click on it to open a terminal window for your distribution.
    2. **Windows Terminal**:
        - Open Windows Terminal, which can be found in the Start menu or by right-clicking the Start button and selecting it. In Windows Terminal, you can open a new tab with your Linux distribution by clicking the dropdown arrow next to the new tab button and selecting your distribution.
    3. **Command Prompt or PowerShell**:
        - You can also launch your Linux distribution from the Command Prompt or PowerShell by simply typing the name of the distribution (e.g., `ubuntu`) and pressing Enter. If you have multiple distributions installed and want to use the default distribution, just type `wsl` and press Enter.
    
    ### Setting WSL to Start Automatically (Optional)
    
    If you frequently use WSL and prefer to have it start automatically when you log into Windows, you can set up a scheduled task for this purpose:
    
    1. **Open Task Scheduler**:
        - Press `Win + R` to open the Run dialog, type `taskschd.msc`, and press Enter.
    2. **Create a New Task**:
        - In the Task Scheduler, go to `Action > Create Task...`.
        - Give your task a name (e.g., `Start WSL`).
        - Set the task to run with the highest privileges and configure it for Windows 10 regardless of your actual version.
    3. **Trigger**:
        - Go to the `Triggers` tab and click `New...`.
        - Choose `At log on` from the "Begin the task" dropdown.
        - Specify any user or leave it to default to run for any user logging in.
        - Click `OK`.
    4. **Actions**:
        - Go to the `Actions` tab and click `New...`.
        - Set the action to `Start a program`.
        - In the "Program/script" box, type `wsl` (to start the default distribution) or the specific name of your Linux distribution (e.g., `ubuntu`).
        - Click `OK`.
    5. **Finish Setup**:
        - Go through any other settings you might want to customize (e.g., Conditions, Settings) and click `OK` to finish setting up the task.
    
    Now, your WSL distribution should start automatically in the background each time you log into Windows. You can open a terminal window as described above to interact with it.
    
    ### Accessing Files
    
    You can access your Linux files from Windows through the File Explorer:
    
    - Navigate to `\\\\wsl$` in the File Explorer address bar. You'll see a list of your installed Linux distributions. You can browse and manage files directly from here.
    
    Remember, you can always shut down all running WSL instances by running `wsl --shutdown` in your Command Prompt or PowerShell if needed. This is useful if you want to free up resources or reset your WSL session.
    
- if i install llama-2 on wsl where are the files located? how do I get all files installed on wsl? how do I individually del them to free up mem?
- would llama be installed under C:\Users\…\AppData\Local\Packages
    
    When you install software within a Windows Subsystem for Linux (WSL) distribution, it doesn't get installed in the typical Windows directories like `C:\\Users\\…\\AppData\\Local\\Packages`. Instead, software installed in WSL resides entirely within the virtual file system of the Linux distribution you're using with WSL.
    
    However, it is possible to access the Linux file system from Windows. For WSL 1, the Linux files are stored as part of the Windows file system and can be accessed through a path that looks similar to what you mentioned but specifically for WSL paths. For WSL 2, the files are stored within a virtual disk image, making direct access slightly different.
    
    ### Accessing WSL Files from Windows
    
    For **WSL 1** distributions, you might find Linux files under a path similar to `C:\\Users\\YourUsername\\AppData\\Local\\Packages\\<DistributionName>\\LocalState\\rootfs\\`, where `<DistributionName>` corresponds to the specific Linux distribution you've installed (e.g., Ubuntu).
    
    For **WSL 2**, accessing files is a bit different due to its use of a virtual disk image. Here's how you can access these files:
    
    1. Open **File Explorer** in Windows.
    2. Type `\\\\wsl$` in the address bar and press Enter. You'll see a list of your installed Linux distributions.
    3. Navigate through your distribution to find the installed files. For instance, `\\\\wsl$\\Ubuntu\\home\\yourusername\\` could be a starting point.
    
    ### Best Practices for Accessing WSL Files
    
    - **Modification**: It's safe to read and copy files from the WSL file system to the Windows file system. However, be cautious when modifying or deleting Linux files from Windows, especially in WSL 2, as this could potentially lead to data corruption within the Linux distribution. It's recommended to perform modifications from within WSL using Linux commands or editors.
    - **Software Installation**: If you're installing something like Llama (assuming it's a Linux-compatible tool) in WSL, it's best managed through the Linux distribution's package manager (e.g., `apt` for Debian/Ubuntu, `yum` for Fedora) or through a language-specific package manager if it's a programming tool (e.g., `pip` for Python packages).
    
    In summary, while Windows and WSL share the same physical hardware, they operate with distinct file systems. Software installations in WSL should be managed within the WSL environment itself, and while Windows can access these files, any interaction should be done with an understanding of the potential risks to file integrity.
    

[https://www.youtube.com/watch?v=qYlgUDKKK5A&ab_channel=NeuralNine](https://www.youtube.com/watch?v=qYlgUDKKK5A&ab_channel=NeuralNine)

[https://learn.microsoft.com/en-us/training/modules/wsl-introduction/](https://learn.microsoft.com/en-us/training/modules/wsl-introduction/)

---

- [https://www.quora.com/Is-WSL-better-than-dual-boot](https://www.quora.com/Is-WSL-better-than-dual-boot)
    
    WSL isn’t the same as using an actual Linux distribution. You have all the privacy and security issues of Windows and not really much of an advantage other than being able to run UNIX shell scripts. Most applications on Linux are also on Windows.
    
    If you have dual boot you also have disadvantages. You may do most of the work on Linux and you can even play games, but if you want to run some software that only works on Windows, you need to reboot. That may or may not be annoying to you.
    
- [https://www.reddit.com/r/bashonubuntuonwindows/comments/tgwdib/dualboot_or_wsl2_for_software_development/](https://www.reddit.com/r/bashonubuntuonwindows/comments/tgwdib/dualboot_or_wsl2_for_software_development/)
    
    I'm using WSL2 for coding both in windows and linux.
    
    In my use case, WSL2 terminal is enough, I don't need linux GUI apps.
    
    All GUI apps I need could be started in windows.
    
    Working with WSL2 for a long time and recently been trying Arch Linux. So i compared the compile times of my Go program on both.
    
    From a performance point of view, there is very little. The compile times had at best a 3 to 5% difference, and ironically sometimes WSL2 was faster then Linux. Yea, that was a headscratcher... But in reality, you will not notice this difference in speed on both systems.
    
    Debugging is frankly the same. Using Visual Studio Code, the debugger integrates the same like it does on native Linux. Code simply transports the information between the WSL2 development environment and your IDE.
    

[https://askubuntu.com/questions/1380253/where-is-wsl-located-on-my-computer](https://askubuntu.com/questions/1380253/where-is-wsl-located-on-my-computer)

Short answer: In your case, given the basic installation, the actual files are in a virtual disk named `ext4.vhdx`. You really don't need to worry about the "where" at this point (since it's a virtual drive), but you'll typically find it under `%userprofile%\AppData\Local\Packages\Canonical...\LocalState\ext4.vhdx`. Your `%userprofile%` is typically something like `C:\Users\<username>`.

`C:\Users\…\AppData\Local\Packages`

[https://www.quora.com/Can-Windows-Subsystem-for-Linux-WSL-be-installed-on-an-external-hard-drive#](https://www.quora.com/Can-Windows-Subsystem-for-Linux-WSL-be-installed-on-an-external-hard-drive#)

**Yes, Windows Subsystem for Linux (WSL) can be installed on an external hard drive**. However, you will need to ensure that your external hard drive is formatted to NTFS or ReFS file system and has sufficient storage space for your Linux distribution.