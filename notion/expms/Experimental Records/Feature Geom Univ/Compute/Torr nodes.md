# Torr nodes

1) What you use to run multiple jobs in parallel and with multiple GPUs?

2) Do you use tmux to create virtual sessions that persist between logins

3) Do you use more than 1 node at a time?

(1) Currently the model I used is small enough to be put in a single GPU so I just use naive data parallel to do multi-gpu training. Specifically, I use the huggingface trainer,  a nice encapsulation of parallel training.(2) I use screen but I think it is very similar to tmux and tmux probably works too.(3) Yes, I currently use two or three nodes but not all the GPUs in these nodes. I think more than one node is OK if there are always some idle GPUs for others to use and I am ready to release the GPUs when asked.

By the way, there are 31 A40 GPUs in total. It’s hard to imagine these GPUs being enough for all the grad students

---

remote server questions:
[https://chatgpt.com/c/2ce7669b-10b6-448f-a6a9-533e607bd1c1](https://chatgpt.com/c/2ce7669b-10b6-448f-a6a9-533e607bd1c1)

To run code:
git clone <repository_url>
cd <repository_directory>

after doing:
ssh <username>@login.robots.ox.ac.uk
ssh [torrlogin1.robots.ox.ac.uk](http://torrlogin1.robots.ox.ac.uk/)
ssh torrnode<n>

We suggest creating a single folder once you login into the torrnode, and git cloning. You can either
write code on your own system with your IDE of choice and Git push/pull your changes to the server, or use nano or vi to edit code directly on the server. Since this is a home directory, make sure to periodically clean up files / models you save here - you shouldn’t use more than a few GB here long running.

- how do I run code using this
    
    To run code on the torrnodes at "[login.robots.ox.ac.uk](http://login.robots.ox.ac.uk/)", follow these detailed steps:
    
    ### 1. Connect to the Server
    
    1. **Open Terminal:**
        - On macOS or Linux, open the Terminal application.
        - On Windows, you can use PowerShell, Command Prompt, or a terminal emulator like PuTTY.
    2. **Connect to the Login Server:**
    Use the SSH command to connect to the initial login server. Replace `<username>` with your actual username.
        
        ```
        ssh <username>@login.robots.ox.ac.uk
        
        ```
        
    3. **Connect to a Specific Node:**
    From the login server, you can SSH into the specific torrnode. Replace `<n>` with the node number you want to access.
        
        ```
        ssh torrlogin1.robots.ox.ac.uk
        ssh torrnode<n>
        
        ```
        
    
    ### 2. Set Up Your Environment
    
    1. **Create a Working Directory:**
    Once logged into the desired node, create a single folder for your project.
        
        ```
        mkdir -p ~/my_project
        cd ~/my_project
        
        ```
        
    2. **Clone Your Repository:**
    If you have a Git repository, clone it into your working directory. Replace `<repository_url>` with the URL of your Git repository.
        
        ```
        git clone <repository_url>
        cd <repository_directory>
        
        ```
        
    
    ### 3. Edit and Manage Your Code
    
    You have two options for managing your code:
    
    ### Option 1: Local Editing with Git
    
    1. **Edit Code Locally:**
    Write and edit your code on your local machine using your preferred IDE.
    2. **Push Changes to Repository:**
    Push your changes to the remote repository.
        
        ```
        git add .
        git commit -m "Your commit message"
        git push origin main
        
        ```
        
    3. **Pull Changes on Server:**
    On the server, pull the latest changes from your repository.
        
        ```
        git pull origin main
        
        ```
        
    
    ### Option 2: Direct Editing on Server
    
    1. **Edit Code on Server:**
    Use a text editor like `nano` or `vi` to edit your code directly on the server.
        
        ```
        nano <filename>
        # or
        vi <filename>
        
        ```
        
    
    ### 4. Run Your Code
    
    1. **Navigate to Your Project Directory:**
    Make sure you are in the directory containing your code.
        
        ```
        cd ~/my_project/<repository_directory>
        
        ```
        
    2. **Run Your Code:**
    Depending on your programming language and environment, use the appropriate command to run your code. For example, for Python:
        
        ```
        python3 your_script.py
        
        ```
        
    
    ### 5. Manage Disk Space
    
    1. **Clean Up Files Periodically:**
    Since you have limited disk space, periodically delete unnecessary files or models to free up space.
        
        ```
        rm -rf ~/my_project/old_models
        
        ```
        
    
    ### Summary
    
    1. **SSH to the server:**
        
        ```
        ssh <username>@login.robots.ox.ac.uk
        ssh torrlogin1.robots.ox.ac.uk
        ssh torrnode<n>
        
        ```
        
    2. **Create and navigate to your project directory:**
        
        ```
        mkdir -p ~/my_project
        cd ~/my_project
        
        ```
        
    3. **Clone your repository:**
        
        ```
        git clone <repository_url>
        cd <repository_directory>
        
        ```
        
    4. **Edit your code (either locally with Git or directly on the server):**
        
        ```
        # Local editing with Git
        git pull origin main
        
        # or Direct editing on server
        nano <filename>
        # or
        vi <filename>
        
        ```
        
    5. **Run your code:**
        
        ```
        python3 your_script.py
        
        ```
        
    6. **Clean up files periodically:**
        
        ```
        rm -rf ~/my_project/old_models
        
        ```
        
    
    By following these steps, you can effectively develop, manage, and run your code on the torrnodes.
    
- if you close the command prompt window when logged into remove server torrnode do your jobs stop
    
    Yes, if you close the command prompt (terminal) window while logged into a remote server (such as `torrnode`), your running jobs will typically stop. This happens because closing the terminal session usually terminates any processes that were started within that session.
    
    However, there are ways to keep your jobs running even after you disconnect from the server:
    
    ### 1. Using `nohup`
    
    `nohup` (short for 'no hang up') is a command that allows a process to continue running in the background after you log out.
    
    ### Example:
    
    ```
    nohup python3 my_script.py &
    
    ```
    
    - `nohup` prevents the process from being terminated when the terminal is closed.
    - The `&` at the end of the command puts the process in the background.
    - Output is typically redirected to `nohup.out` unless otherwise specified.
    
    ### 2. Using `screen`
    
    `screen` is a terminal multiplexer that allows you to create a session and run processes within that session. You can detach from the session and log out, then later reattach to it.
    
    ### Install `screen`:
    
    On Debian-based systems (like Ubuntu):
    
    ```
    sudo apt-get install screen
    
    ```
    
    On Red Hat-based systems (like CentOS):
    
    ```
    sudo yum install screen
    
    ```
    
    ### Example:
    
    1. **Start a Screen Session:**
        
        ```
        screen -S my_session
        
        ```
        
    2. **Run Your Command:**
        
        ```
        python3 my_script.py
        
        ```
        
    3. **Detach from the Screen Session:**
    Press `Ctrl + A` then `D`.
    4. **Reattach to the Screen Session:**
        
        ```
        screen -r my_session
        
        ```
        
    
    ### 3. Using `tmux`
    
    `tmux` is another terminal multiplexer similar to `screen`.
    
    ### Install `tmux`:
    
    On Debian-based systems (like Ubuntu):
    
    ```
    sudo apt-get install tmux
    
    ```
    
    On Red Hat-based systems (like CentOS):
    
    ```
    sudo yum install tmux
    
    ```
    
    ### Example:
    
    1. **Start a Tmux Session:**
        
        ```
        tmux new -s my_session
        
        ```
        
    2. **Run Your Command:**
        
        ```
        python3 my_script.py
        
        ```
        
    3. **Detach from the Tmux Session:**
    Press `Ctrl + B` then `D`.
    4. **Reattach to the Tmux Session:**
        
        ```
        tmux attach -t my_session
        
        ```
        
    
    ### Summary
    
    To keep your jobs running after you disconnect from the server, you can use:
    
    1. **nohup**: `nohup python3 my_script.py &`
    2. **screen**:
        - Start: `screen -S my_session`
        - Detach: `Ctrl + A`, `D`
        - Reattach: `screen -r my_session`
    3. **tmux**:
        - Start: `tmux new -s my_session`
        - Detach: `Ctrl + B`, `D`
        - Reattach: `tmux attach -t my_session`
    
    These tools ensure that your processes continue running even after you disconnect from the server.
    

- if a server has no slurm, how do you send jobs to run in parallel on it (torrnode)?
    
    If the server does not have SLURM installed, you can still run jobs in parallel using various other methods. Here are a few common approaches:
    
    ### 1. Using GNU Parallel
    
    GNU Parallel is a tool for executing jobs in parallel on a single server. It is flexible and easy to use.
    
    ### Install GNU Parallel
    
    1. **Install GNU Parallel:**
    If GNU Parallel is not already installed, you can install it using your package manager. On Debian-based systems (like Ubuntu), use:
        
        ```
        sudo apt-get install parallel
        
        ```
        
        On Red Hat-based systems (like CentOS), use:
        
        ```
        sudo yum install parallel
        
        ```
        
    
    ### Run Jobs with GNU Parallel
    
    1. **Create a Job File:**
    Create a file (e.g., `jobs.txt`) containing the commands you want to run, one per line.
        
        ```
        echo "python3 script1.py" >> jobs.txt
        echo "python3 script2.py" >> jobs.txt
        echo "python3 script3.py" >> jobs.txt
        
        ```
        
    2. **Run the Jobs in Parallel:**
    Use GNU Parallel to run the jobs. The `j` option specifies the number of jobs to run in parallel.
        
        ```
        parallel -j 4 < jobs.txt
        
        ```
        
        This will run the commands in `jobs.txt` in parallel, with up to 4 jobs running at the same time.
        
    
    ### 2. Using Python Multiprocessing
    
    If your tasks can be parallelized within Python, you can use the `multiprocessing` module.
    
    ### Example Python Script
    
    1. **Create a Python Script:**
    Create a Python script (e.g., `run_parallel.py`) using the `multiprocessing` module.
        
        ```python
        import multiprocessing
        import os
        
        def worker(script_name):
            os.system(f'python3 {script_name}')
        
        if __name__ == '__main__':
            scripts = ['script1.py', 'script2.py', 'script3.py']
            with multiprocessing.Pool(processes=4) as pool:
                pool.map(worker, scripts)
        
        ```
        
    2. **Run the Python Script:**
    Run the script to execute the jobs in parallel.
        
        ```
        python3 run_parallel.py
        
        ```
        
    
    ### 3. Using Background Processes
    
    You can also run jobs in the background using `&` and `wait`.
    
    ### Example
    
    1. **Run Jobs in Background:**
        
        ```
        python3 script1.py &
        python3 script2.py &
        python3 script3.py &
        
        ```
        
    2. **Wait for Jobs to Complete:**
    Use `wait` to ensure the shell waits for all background jobs to finish.
        
        ```
        wait
        
        ```
        
    
    ### Summary
    
    Here are three approaches to run jobs in parallel on a server without SLURM:
    
    1. **GNU Parallel:**
        - Install GNU Parallel: `sudo apt-get install parallel` (Ubuntu) or `sudo yum install parallel` (CentOS).
        - Create a job file: `jobs.txt`.
        - Run jobs: `parallel -j 4 < jobs.txt`.
    2. **Python Multiprocessing:**
        - Create a script using `multiprocessing`.
        - Run the script: `python3 run_parallel.py`.
    3. **Background Processes:**
        - Run jobs in the background using `&`.
        - Use `wait` to wait for all jobs to complete.
    
    Choose the method that best fits your workflow and the specifics of your environment.
    
- is qsub only for slurm
    
    No, `qsub` is not exclusively for SLURM. In fact, `qsub` is primarily associated with the Portable Batch System (PBS) and its derivatives, such as Torque. SLURM uses its own set of commands for job submission and management, such as `sbatch` for submitting jobs.
    
    Here is a brief overview of how `qsub` is used and alternatives in SLURM:
    
    ### 1. Using `qsub` with PBS or Torque
    
    If your server is using PBS or Torque, you can submit jobs using the `qsub` command. Here’s a basic example of how to use it:
    
    1. **Create a Job Script:**
    Create a script (e.g., `job_script.sh`) with the necessary PBS directives at the top.
        
        ```
        #!/bin/bash
        #PBS -N my_job
        #PBS -l nodes=1:ppn=4
        #PBS -l walltime=01:00:00
        #PBS -q batch
        #PBS -o output.log
        #PBS -e error.log
        
        # Change to the directory from which qsub was executed
        cd $PBS_O_WORKDIR
        
        # Run the job
        python3 my_script.py
        
        ```
        
    2. **Submit the Job:**
    Submit the job script using `qsub`.
        
        ```
        qsub job_script.sh
        
        ```
        
    
    ### 2. Using SLURM (`sbatch`)
    
    If your server uses SLURM, the equivalent command for submitting a job is `sbatch`.
    
    1. **Create a Job Script:**
    Create a script (e.g., `job_script.sh`) with the necessary SLURM directives at the top.
        
        ```
        #!/bin/bash
        #SBATCH --job-name=my_job
        #SBATCH --nodes=1
        #SBATCH --ntasks=4
        #SBATCH --time=01:00:00
        #SBATCH --output=output.log
        #SBATCH --error=error.log
        
        # Run the job
        python3 my_script.py
        
        ```
        
    2. **Submit the Job:**
    Submit the job script using `sbatch`.
        
        ```
        sbatch job_script.sh
        
        ```
        
    
    ### 3. Running Jobs Without a Scheduler
    
    If your server does not use any job scheduler like SLURM, PBS, or Torque, you can still run jobs in parallel using methods such as GNU Parallel, Python Multiprocessing, or background processes as discussed earlier.
    
    ### Summary
    
    - **PBS/Torque:** Use `qsub` to submit jobs.
    - **SLURM:** Use `sbatch` to submit jobs.
    - **No Scheduler:** Use GNU Parallel, Python Multiprocessing, or background processes.
    
    Ensure you are using the appropriate commands and job scripts based on the job scheduler installed on your server. If you are unsure which scheduler is installed, you can check with your system administrator or look for documentation specific to your computing environment.