# Switch users on same machine

- [https://gist.github.com/rahularity/86da20fe3858e6b311de068201d279e3](https://gist.github.com/rahularity/86da20fe3858e6b311de068201d279e3)
what are the steps to do this for windows?
    1. if folder doesn’t exist yet: `mkdir -p ~/.ssh` . parent folder is `C:\Users\[YourUsername]`
    2. **Generate New SSH Keys for each account**
        
        `ssh-keygen -t rsa -C "your-email-address" -f "github-username"`
        
    3. **Start the SSH-Agent and Add Your Keys**:
        
        NOTE: each time you restart git bash, you need to start agent and add ssh keys again!
        
        - Start the SSH-Agent in the background:
            
            ```bash
            eval $(ssh-agent -s)
            ```
            
        - Add your SSH keys to the SSH agent:
            
            ```bash
            ssh-add ~/.ssh/id_rsa_user2
            ```
            
            DO NOT USE -K. This is for PIN. If you have a PIN set up for your hardware token or security module, enter it at the prompt. Not using -K won’t trigger PIN.
            
        - list all added ssh keys: `ssh-add -l`
    4. **Create or Modify the SSH Config File**:
        - Create or edit the config file by running `nano config` or using any text editor
            
            `cd ~/.ssh`
            
            `touch config`
            
            `open config` or manually open in interface
            
        - Add the following content, adjusted for your setup:
            
            ```
            # Default GitHub account
            Host github.com
              HostName github.com
              User git
              IdentityFile ~/.ssh/id_rsa
            
            # Secondary GitHub account
            Host github-user2
              HostName github.com
              User git
              IdentityFile ~/.ssh/id_rsa_user2
            ```
            
    5. **Add SSH Keys to GitHub Accounts**:
        - For two github accounts, do I add both ssh keys for both accounts to both accounts, or just each ssh key to its own account?
            
            For managing two GitHub accounts with SSH keys, you should add each SSH key to its respective account only, not both keys to both accounts.
            
        - For each SSH key, you need to add the public key (`.pub` file) to the corresponding GitHub account.
        - Go to GitHub, log in to your account, and navigate to Settings → SSH and GPG keys → New SSH key.
        - Paste the content of your public key file (`id_rsa_user2.pub` for example).
    6. Temporarily make private repo public
    7. **Clone Repositories Using the Config Aliases**:
        - To clone a repository from your secondary account, use the host alias from your SSH config. For example:
            
            ```
            git clone git@github.com-{your-username}:{owner-user-name}/{the-repo-name}.git
            
            [e.g.] git clone git@github.com-rahul-personal:rahul-personal/TestRepo.git
            ```
            
    8. Switch to the user you want to display on commit history:
        
        ```
          git config --global user.email "my_office_email@gmail.com"
          git config --global user.name "Rahul Pandey"
        ```
        
    
    use --global; --local is specifically only when in a repo. using neither implies using --local. 
    
    - I did "git config --global [user.name](http://user.name/) "user_1"" and new email but when I commit, the history still shows user_0. why?
        
        **Local Repository Configuration Overrides Global Configuration**: Each Git repository has its own local configuration. If you've set a username and email in the local repository's configuration, it will override the global settings. To check the local configuration, use **`git config user.name`** and **`git config user.email`** within the repository. If these show "user_0", you'll need to update them.
        
        <<<
        
        if get "could not lock config file .git/config: File exists” when config --local: 
        
        Go into the .git folder of your local repo, check if config.lock is there. Delete it, then git config -- local
        
    1. In repo:
        
        `git remote set-url origin [git@github.com](mailto:git@github.com):user_2/REPONAME.git`
        
        git add, commit, push for first time from local machine
        
    2. make repo private on github
        
        now, you can STILL push on local machine! you need to make it public first to clone and do first push. but then, once you make private again, you can just do this again. It does not reset even if the ssh key is reset from agent after restarting git bash
        
    
    Remember, this setup allows you to use multiple GitHub accounts on the same machine by distinguishing them with different SSH keys and config aliases. Each time you clone or interact with a repository, Git will use the corresponding SSH key as per the SSH config file.
    
    [https://chat.openai.com/c/a705c95c-bba8-4d31-a349-c1a322a3aeb1](https://chat.openai.com/c/a705c95c-bba8-4d31-a349-c1a322a3aeb1)
    
    [https://www.youtube.com/watch?v=lAPcvItvdy0&ab_channel=AyyazTech](https://www.youtube.com/watch?v=lAPcvItvdy0&ab_channel=AyyazTech)
    

- N**ow do this every time you restart git bash!**
    
    eval `ssh-agent -s`
    
    ssh-add ~/.ssh/user_2
    
    git remote set-url origin [git@github.com](mailto:git@github.com):user_2/REPONAME.git
    
    git add, commit, push etc
    

- the ssh key is removed from agent each time close and restart git bash
    
    If your SSH key is being removed from the SSH agent each time you close and restart Git Bash, this is because the SSH agent does not persist keys between sessions by default. Each time you open Git Bash, it starts a new session, and you'll need to re-add your SSH key to the agent. Here's how you can manage this more efficiently:
    
    ### 1. Automatically Add SSH Key When Starting Git Bash
    
    You can automate the process of adding your SSH key to the SSH agent each time you start Git Bash. To do this:
    
    1. **Create or Edit the `~/.bashrc` or `~/.bash_profile` File:**
        - Open Git Bash.
        - Use a text editor like `nano` or `vi` to create or edit the `~/.bashrc` or `~/.bash_profile` file. For example, type `nano ~/.bashrc`.
    2. **Add SSH Key to SSH Agent:**
        - Add the following lines to the file:
            
            ```bash
            # Start SSH agent and add key
            eval $(ssh-agent -s)
            ssh-add ~/.ssh/id_rsa
            
            ```
            
        - Replace `~/.ssh/id_rsa` with the path to your SSH key if it's different.
        - Save the file and exit the editor.
    3. **Reload or Restart Git Bash:**
        - To apply the changes, you can either close and reopen Git Bash or source the file by typing `source ~/.bashrc` or `source ~/.bash_profile`.
    
    ### 2. Using SSH Config File for Persistent SSH Connections
    
    Another approach is to use an SSH config file to manage your SSH connections more efficiently. This doesn't keep your SSH key in the agent across sessions but can simplify the process of connecting to servers.
    
    1. **Create or Edit the SSH Config File:**
        - The config file is located at `~/.ssh/config`.
        - Edit this file to include host-specific configurations.
    2. **Example SSH Config Entry:**
        - Add entries like this for each host you connect to:
            
            ```
            Host myserver
                HostName example.com
                User myusername
                IdentityFile ~/.ssh/my_custom_key
            
            ```
            
        - Replace `example.com`, `myusername`, and `~/.ssh/my_custom_key` with your server's details and key.
    
    ### Notes
    
    - Ensure your SSH key has the correct permissions (`chmod 600 ~/.ssh/id_rsa`).
    - If you're using a passphrase-protected SSH key, you'll be prompted for the passphrase each time unless you use an SSH key manager with passphrase caching.
    - Be cautious with scripts and commands that automatically start the SSH agent, as they might pose a security risk if not configured correctly.
    
    These methods should help you manage your SSH keys more effectively in Git Bash on Windows.
    

- are ssh keys personal account tokens?
    
    No, SSH keys and Personal Access Tokens (PATs) are two different methods of authentication used for different purposes, especially in the context of services like GitHub:
    
    1. **SSH Keys**:
        - SSH keys are a pair of cryptographic keys that can be used to authenticate to an SSH server as an alternative to password-based logins.
        - An SSH key pair consists of a private key (which is kept secret) and a public key (which is shared).
        - You use SSH keys to establish a secure and encrypted connection between your computer and a remote server, such as GitHub.
        - When you add your public SSH key to your GitHub account, GitHub can authenticate your git operations over SSH by matching the public key with the private key stored on your machine.
        - SSH keys are often used for secure access to repositories and are not tied to specific operations within GitHub.
    2. **Personal Access Tokens (PATs)**:
        - A Personal Access Token (PAT) is an alternative to using passwords for authentication to GitHub when using the GitHub API or the command line.
        - PATs are used to grant limited access to your GitHub account, with scopes defining the level of access the token provides.
        - They are particularly useful for scripts where you need to authenticate Git operations or for accessing the GitHub API.
        - PATs are also used as a replacement for passwords when Git operations are performed over HTTPS.
        - Each token can have custom levels of access and specific expiration times, offering a more controlled and secure way of automation or integration with GitHub.
    
    In summary, SSH keys are used for secure access to Git repositories over SSH, while Personal Access Tokens are used for API access and sometimes for Git operations over HTTPS, particularly when two-factor authentication is enabled. Both methods enhance security but are used in different contexts and have different setup and management processes.
    

---

- How do we switch users in git bash? (for a repo)
    1. Open Git Bash and navigate to the repository that you want to work with.
    2. Use the following command to list the current user information:
    
    ```
    git config user.name
    ```
    
    1. Use the following command to set the new user name:
    
    ```
    git config user.name "New User Name"
    ```
    
    Make sure to replace "New User Name" with the actual name of the new user that you want to switch to.
    
    1. Use the following command to set the new user email:
    
    ```
    git config user.email "newuseremail@example.com"
    ```
    
    1. Once you have set the new user name and email, you can start making changes and commits as the new user.
    
    Note that these user settings are specific to the local repository, and will not affect other repositories on your system or on remote servers. If you want to switch users globally across all Git repositories on your system, you can use the "--global" flag with the "git config" command, like this:
    
    ```
    git config --global user.name "New Global User Name"
    git config --global user.email "newglobaluseremail@example.com"
    ```
    
- switch users github bash entirely not just in repo
    
    To switch users in GitHub Bash, you need to update the Git configuration with the new user details. Here's how you can switch users globally, not just for a specific repository:
    
    1. Open your terminal or command prompt.
    2. Check your current Git configuration by running the following command:
    
    ```
    git config --list
    
    ```
    
    1. Look for the lines that start with `user.name` and `user.email` in the output. These lines contain your current Git user details.
    2. To switch to a different user globally, use the following commands, replacing `NEW_USERNAME` and `NEW_EMAIL` with the desired username and email address for the new user:
    
    ```
    git config --global user.name "NEW_USERNAME"
    git config --global user.email "NEW_EMAIL"
    
    ```
    
    For example:
    
    ```
    git config --global user.name "JohnDoe"
    git config --global user.email "johndoe@example.com"
    
    ```
    
    1. After running these commands, your Git configuration will be updated with the new user details.
    
    You can verify the changes by running `git config --list` again and checking if the `user.name` and `user.email` values have been updated.
    
    From this point forward, any Git actions you perform, including commits and pushes, will use the new user details you have set globally.
    
- in git bash, how do I switch to a new user such that I can clone a private repo from their github account?
    
    Switching to a new user in Git Bash to clone a private repository involves multiple steps. You'll need to configure the Git username and email for that specific user, and most importantly, you'll need to set up authentication for that GitHub account.
    
    ### Steps to switch to a new user in Git Bash:
    
    1. **Configure Username and Email**: You can set a new username and email for Git to use in your local repository.
        
        ```bash
        git config user.name "New User"
        git config user.email "newuser@example.com"
        
        ```
        
        If you want to set these globally (for all repositories), you can use the `--global` flag.
        
        ```bash
        git config --global user.name "New User"
        git config --global user.email "newuser@example.com"
        
        ```
        
    2. **Set up Authentication**: There are various methods for authenticating to GitHub including SSH keys, HTTPS with a token, or a combination of username and password (which GitHub is discouraging). Here are some options:
        - **SSH Keys**: If you haven't already, generate a new SSH key for the new GitHub account and add it to the SSH agent.
            
            ```bash
            ssh-keygen -t rsa -b 4096 -C "newuser@example.com"
            ssh-add ~/.ssh/new_rsa
            
            ```
            
            Then, you'll need to add this new SSH key to the GitHub account. Copy the SSH key to your clipboard.
            
            ```bash
            clip < ~/.ssh/new_rsa.pub  # For Windows
            # or
            pbcopy < ~/.ssh/new_rsa.pub  # For macOS
            # or
            xclip -sel clip < ~/.ssh/new_rsa.pub  # For Linux
            
            ```
            
            Go to GitHub -> Settings -> SSH and GPG keys -> New SSH key, and then paste your key.
            
        - **HTTPS with Token**: You can use a personal access token instead of your GitHub password. Create a new token in GitHub under Settings -> Developer settings -> Personal access tokens -> Generate new token. Make sure you give it the right permissions. Then, you can clone using:
            
            ```bash
            git clone <https://token@github.com/username/repository.git>
            
            ```
            
            Replace `token` with your actual personal access token.
            
    3. **Clone the Repository**: Finally, clone the private repository. If you've set up an SSH key, you can use:
        
        ```bash
        git clone git@github.com:username/repository.git
        
        ```
        
        If you're using HTTPS with a token, you can use:
        
        ```bash
        git clone <https://token@github.com/username/repository.git>
        
        ```
        
    
    Remember, these configurations are local to your machine, and you need to make sure you are authenticated properly to access private repositories.
    
- enter file in which to save the key
    
    When you run the `ssh-keygen` command to generate an SSH key, you'll be prompted with a message asking where to save the key. The message will look something like this:
    
    ```bash
    Enter file in which to save the key (/home/yourusername/.ssh/id_rsa):
    
    ```
    
    Here are your options:
    
    1. **Default Path**: If you simply press `Enter`, the SSH key will be saved to the default path, which is usually `/home/yourusername/.ssh/id_rsa` on Linux and macOS or `C:\\Users\\yourusername\\.ssh\\id_rsa` on Windows. This will overwrite any existing key at that location unless you specify a different path.
    2. **Custom Path**: You can specify a custom path where you'd like to save your new SSH key. This is useful if you already have an SSH key and would like to generate a new one for a different account. For example, you could specify `/home/yourusername/.ssh/id_rsa_newuser` as the path.
    
    Here's how to specify a custom path:
    
    ```bash
    ssh-keygen -t rsa -b 4096 -C "newuser@example.com"
    
    ```
    
    When prompted:
    
    ```bash
    Enter file in which to save the key (/home/yourusername/.ssh/id_rsa): /home/yourusername/.ssh/id_rsa_newuser
    
    ```
    
    After specifying the path, you'll be prompted to enter a passphrase for additional security, which is optional.
    
    **Note**: If you choose a custom path, you'll need to tell SSH to use this key when interacting with the remote server. You can do this by adding the key to the SSH agent:
    
    ```bash
    ssh-add /path/to/your/custom/id_rsa_newuser
    
    ```
    
    And also by potentially modifying your SSH config file (typically found at `~/.ssh/config`) to specify which key to use for which server.
    
- Could not open a connection to your authentication agent.
    
    The error message "Could not open a connection to your authentication agent" typically occurs when you try to add an SSH key to the SSH agent but the agent isn't running.
    
    Here's how you can troubleshoot this issue:
    
    ### On Linux or macOS:
    
    1. **Start the SSH Agent**: Run the following command to start the SSH agent in the background.
        
        ```bash
        eval "$(ssh-agent -s)"
        
        ```
        
        This will start the SSH agent and set the necessary environment variables so the agent can be accessed from the current shell session.
        
    2. **Add SSH Key to Agent**: After the SSH agent is running, you can add your SSH key to it.
        
        ```bash
        ssh-add ~/.ssh/id_rsa_newuser
        
        ```
        
        Replace `id_rsa_newuser` with the name of your SSH key if you've used a different name.
        
    
    ### On Windows:
    
    1. **Start the SSH Agent**: You can start the SSH agent by running the following command in Git Bash:
        
        ```bash
        eval $(ssh-agent -s)
        
        ```
        
    2. **Add SSH Key to Agent**: Once the agent is running, add your SSH key.
        
        ```bash
        ssh-add ~/.ssh/id_rsa_newuser
        
        ```
        
        Replace `id_rsa_newuser` with the name of your SSH key if you've used a different name.
        
    
    After successfully adding your SSH key to the SSH agent, you should be able to clone, fetch, and push to and from your repositories without encountering authentication issues.
    
    Remember that running these commands will only affect the current shell session. If you open a new terminal window, you may need to repeat these steps. Some users set up their shell profiles to automatically start the SSH agent and add their keys to avoid having to do this manually each time.
    
- WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!
Add correct host key in X to get rid of this message.
    
    The message suggests that the SSH key for the remote host has changed, and the new key doesn't match the one stored in your `known_hosts` file. This could happen for a variety of reasons, including legitimate server key rotation or configuration changes. However, in some cases, it could be indicative of a security risk, such as a man-in-the-middle attack.
    
    ### Steps to Resolve the Issue:
    
    1. **Backup Existing `known_hosts` File**: Before making any changes, it's a good idea to back up your existing `known_hosts` file.
        
        ```bash
        cp /c/Users/mikel/Documents/_prog/github/.ssh/known_hosts /c/Users/mikel/Documents/_prog/github/.ssh/known_hosts_backup
        
        ```
        
    2. **Remove the Offending Key**: The message tells you the line number of the offending key in the `known_hosts` file. You can remove it using the `ssh-keygen` command:
        
        ```bash
        ssh-keygen -R github.com -f /c/Users/mikel/Documents/_prog/github/.ssh/known_hosts
        
        ```
        
        This will remove the offending entry for `github.com` from the specified `known_hosts` file.
        
    3. **Verify and Reconnect**: After you've removed the offending entry, you can attempt to SSH into GitHub again:
        
        ```bash
        ssh -T git@github.com
        
        ```
        
        This time, you should see a prompt asking you if you want to continue connecting and add the new key to your `known_hosts` file. Before saying 'yes', you should verify that the key fingerprint matches what it's supposed to be. You can often find this information in official documentation or by contacting support.
        
    4. **Add the New Key**: If the fingerprint is correct, you can proceed to add the new key to your `known_hosts` file by typing 'yes' at the prompt.
    
    By following these steps, you should be able to safely update the SSH key for GitHub in your `known_hosts` file. Always exercise caution and verify the new keys when doing this to ensure security.
    
- I have two ssh keys stored on my computer, how do I deal with this?
    
    Having multiple SSH keys on your computer is not uncommon, especially if you interact with different remote systems or services that require SSH access. The way to manage multiple SSH keys depends on what you want to achieve. Here are some scenarios and how you might handle them:
    
    ### Different Keys for Different GitHub Accounts
    
    If you have two different GitHub accounts and you want to use a different SSH key for each account, you can specify which SSH key to use for each GitHub account in your SSH config file.
    
    1. **Create/Edit SSH Config**: Create or edit the SSH config file, usually located at `~/.ssh/config`:
        
        ```bash
        nano ~/.ssh/config  # or use your favorite text editor
        
        ```
        
    2. **Add Host Configurations**: Add host configurations to specify which SSH key to use for each GitHub account. For example:
        
        ```
        # Default GitHub account
        Host github.com
          HostName github.com
          User git
          IdentityFile ~/.ssh/id_rsa_account1
        
        # Second GitHub account
        Host github.com-second
          HostName github.com
          User git
          IdentityFile ~/.ssh/id_rsa_account2
        
        ```
        
    3. **Clone and Interact with Repos**: Now, when cloning a repo from the second account, you can use the host alias `github.com-second`:
        
        ```bash
        git clone git@github.com-second:second_username/repository.git
        
        ```
        
    
    ### Different Keys for Different Services
    
    If you use SSH keys for different services (like GitHub, GitLab, Bitbucket, etc.), you can add different host sections in the SSH config file as explained above:
    
    ```
    # GitHub
    Host github.com
      HostName github.com
      User git
      IdentityFile ~/.ssh/id_rsa_github
    
    # GitLab
    Host gitlab.com
      HostName gitlab.com
      User git
      IdentityFile ~/.ssh/id_rsa_gitlab
    
    ```
    
    ### Add Keys to SSH Agent
    
    You can also add multiple keys to your SSH agent, which will automatically use the correct key for each service based on your SSH config:
    
    ```bash
    ssh-add ~/.ssh/id_rsa_account1
    ssh-add ~/.ssh/id_rsa_account2
    
    ```
    
    ### Check Loaded Keys
    
    You can check which keys are currently loaded into the SSH agent by running:
    
    ```bash
    ssh-add -l
    
    ```
    
    By managing your SSH keys this way, you can easily switch between different GitHub accounts or different services without having to replace your SSH key each time.
    
- On git bash I am tied to a github user account. I want to switch users so I can push to another user's repo. How can I do this?
    
    To switch GitHub accounts in Git Bash, you'll need to update the credentials associated with the Git repository on your local machine. Here are the steps:
    
    1. **Unset existing credentials**: Use the following command to remove the credentials stored in the credential helper.
        
        ```
        git credential reject '<https://github.com>'
        
        ```
        
        Or, if you're using Windows Credential Manager:
        
        ```
        git credential reject '<https://username@github.com>'
        
        ```
        
    2. **Change Remote URL** (Optional): If the repository you want to push to belongs to a different account, update the remote URL.
        
        ```
        git remote set-url origin <https://new-username@github.com/repo.git>
        
        ```
        
    3. **Add New Credentials**: The next time you try to push or pull, Git will prompt you to enter the username and password for the new account.
        
        ```
        git push origin master
        
        ```
        
        Or whatever branch you're working on.
        
    4. **Enter New Credentials**: Input the new username and password when prompted.
    
    Now you should be able to push to the other user's repo using the new account's credentials.
    
- I don't see the config file
    
    If you don't see a `config` file in your `~/.ssh` directory, you may need to create one. Here's how you can do it:
    
    1. **Open Git Bash**.
    2. **Navigate to the SSH directory**:
        
        ```
        cd ~/.ssh
        
        ```
        
        If the directory doesn't exist, create it:
        
        ```
        mkdir ~/.ssh
        cd ~/.ssh
        
        ```
        
    3. **Create a new `config` file**:
        - **Using `touch` command**: To create a new file, you can simply use the `touch` command.
            
            ```
            touch config
            
            ```
            
        - **Using a text editor**: Alternatively, you can use a text editor like `nano` to create and edit the file in one go.
            
            ```
            nano config
            
            ```
            
    4. **Add SSH configurations**:
    Open the `config` file with a text editor, like `nano`:
        
        ```
        nano config
        
        ```
        
        Then add your SSH configurations. For example:
        
        ```
        # Personal account
        Host github.com-personal
            HostName github.com
            User git
            IdentityFile ~/.ssh/id_rsa
        
        # Work account
        Host github.com-work
            HostName github.com
            User git
            IdentityFile ~/.ssh/id_rsa_work
        
        ```
        
    5. **Save the file**:
        - If you're using `nano`, press `Ctrl + O` to write changes, and then `Ctrl + X` to exit the editor.
    6. **Set the permissions**:
    The SSH `config` file should be readable and writable only by the user and not accessible by others.
        
        ```
        chmod 600 ~/.ssh/config
        
        ```
        
    7. **Test the Configuration**:
    You can test your SSH configuration with the following command:
        
        ```
        ssh -T git@github.com-personal
        
        ```
        
        or
        
        ```
        ssh -T git@github.com-work
        
        ```
        
        Follow the prompts. If everything is set up correctly, you should receive a message saying that you've successfully authenticated.
        
    
    After these steps, you should have a `config` file in your `~/.ssh` directory with the correct configurations for multiple accounts.
    
- I added the ssh key and config file but I still can't switch users on git bash and clone a private repo
    
    If you're still experiencing issues cloning a private repository after setting up SSH keys and the `config` file, here are some steps to diagnose and potentially resolve the issue:
    
    ### Diagnosing the Issue
    
    1. **Test SSH Connection**: Make sure that your SSH connection is working for the respective GitHub account:
        
        ```bash
        ssh -T git@github.com-personal
        
        ```
        
        or
        
        ```bash
        ssh -T git@github.com-work
        
        ```
        
        If you get a "Permission Denied" message, then the SSH key is not properly configured.
        
    2. **Check SSH Agent**: Ensure that the SSH agent is running and that it has your key:
        
        ```bash
        ssh-add -l
        
        ```
        
        If your key is not listed, add it using:
        
        ```bash
        ssh-add ~/.ssh/id_rsa_work  # adjust the file name accordingly
        
        ```
        
    3. **Verify Config File**: Make sure that the `~/.ssh/config` file is correctly set up. Permissions should also be correct (`chmod 600 ~/.ssh/config`).
    4. **Check GitHub Permissions**: Ensure that the GitHub account you're trying to use has permission to access the private repository. Go to the repository's settings on GitHub and check under the "Access" tab.
    5. **Check Repository URL**: Make sure you're using the correct URL format as defined in your `config` file:
        
        ```bash
        git clone git@github.com-personal:username/repo.git
        
        ```
        
        or
        
        ```bash
        git clone git@github.com-work:username/repo.git
        
        ```
        
    
    ### Common Solutions
    
    1. **Restart SSH Agent**: Sometimes, the SSH agent might not pick up the keys properly. You can restart it using:
        
        ```bash
        eval $(ssh-agent -s)
        ssh-add ~/.ssh/id_rsa_work  # adjust the file name accordingly
        
        ```
        
    2. **Update Remote URL**: If you initially cloned using HTTPS or another SSH key, update the remote URL to use the new SSH host alias.
        
        ```bash
        git remote set-url origin git@github.com-personal:username/repo.git  # adjust the URL accordingly
        
        ```
        
    3. **Recheck All Steps**: Sometimes, a simple typo or mistake in the `~/.ssh/config` file or while adding SSH keys can cause issues. Double-check to make sure everything is correct.
    4. **Check for Error Messages**: Pay close attention to any error messages you get when trying to clone the repository. They often give clues as to what's going wrong.
    5. **Check Git Version**: Ensure you're using a reasonably updated version of Git that supports the features you're trying to use.
    6. **Review Documentation**: The GitHub documentation for [connecting with SSH](https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh) can offer additional insights and troubleshooting tips.
    7. **Revoke and Re-add SSH Keys**: As a last resort, you can remove the SSH keys from your GitHub account and your local machine and go through the process of creating and adding them again.
    
    If you have followed these steps carefully and are still encountering issues, the problem might require more specific troubleshooting.
    
- How do I add a key to known hosts?

- FINALIZED SOLUTION TO SWITCHING USERS ON GIT BASH
    
    ssh-keygen -t rsa -b 4096 -C "[NEW@gmail.com](mailto:NEW@gmail.com)"
    
    add to: PATH_TO/.ssh/id_rsa_NEW
    
    clip < PATH_TO/.ssh/id_rsa_NEW.pub
    add ssh key to github account under settings
    
    eval "$(ssh-agent -s)"
    ssh-add PATH_TO/.ssh/id_rsa_NEW
    
    create config file
    chmod 600 PATH_TO/.ssh/config
    
    the following gives " WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!":
    ssh NEW@github
    git clone [private repo]
    
    *SOLN:
    
    1. change repo to public
    2. [https://stackoverflow.com/questions/75830783/why-are-connections-to-github-over-ssh-throwing-an-error-warning-remote-host-i](https://stackoverflow.com/questions/75830783/why-are-connections-to-github-over-ssh-throwing-an-error-warning-remote-host-i)
    ssh-keygen -R [github.com](http://github.com/)
    3. git push
    The authenticity of host '[github.com](http://github.com/) (IP)' can't be established.This key is not known by any other names. Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
    4. git remote set-url origin [git@github.com](mailto:git@github.com):new/REPO.git
    5. change repo back to private. now you can STILL push to it
    
    now even if you switch back to prev user and email, you can push to your old accnt. if you want to push to accnt 2 using new name, just switch to it.
    

---

- Is the user name on the local machine the same as the user name on github?
    
    The user name on your local machine is not necessarily the same as the user name on GitHub. These are separate entities and can have different values.
    
    In Git, the user name and email configured locally using the `git config` command are used for associating commits with an author. The user name and email specified in the local Git configuration can be set to match your GitHub user name and email to provide consistency, but they are not automatically synchronized.
    
    On your local machine, the user name typically refers to the user account or profile name associated with your operating system or development environment. It is specific to your local machine and may be used for various purposes, such as identifying the current user, displaying in the command prompt, or as part of file ownership.
    
    On the other hand, the user name on GitHub refers to the user account name associated with your GitHub account. It is the unique identifier used for your GitHub profile and is displayed on your GitHub profile page and in the URLs of your GitHub repositories.
    
    The user name on GitHub is used for identification purposes when interacting with GitHub's services, such as pushing commits, creating repositories, or participating in collaborations. It is separate from the user name on your local machine and can be different.
    
    It's worth noting that when you interact with GitHub through Git commands, you need to authenticate using your GitHub credentials, which include your GitHub user name and an access token or password. These credentials are separate from the user name on your local machine and are used to establish a connection and authorize actions with your GitHub account.
    
- In github, how do I change which account commits to the repo using the git bash shell? On my local shell, I changed the user name but it did not change the account on the commit
    
    SOLN: the user name doesn’t matter in the local shell. The [user.email](http://user.email) does, or the access token. Note that each time you change to a new account, it may take a while for the commit to show up in hist, compared to using the prev account.
    
- On git bash, how do you switch user accounts using personal access token?
    1. Run the following command to view the current remote repository URL:
        
        ```
        git remote -v
        ```
        
    2. To switch user accounts, you need to change the URL to include your new PAT in the authentication credentials. The updated URL should follow this format:
        
        ```
        <https://<PAT>@github.com/><username>/<repository>.git
        ```
        
        Replace `<PAT>` with your personal access token and `<username>` and `<repository>` with the appropriate GitHub account and repository information.
        
        For example, the updated URL for a repository named "example-repo" under the GitHub account "example-user" with a personal access token "abcdef123456" would be:
        
        ```
        <https://abcdef123456@github.com/example-user/example-repo.git>
        
        ```
        
    3. To update the remote repository URL with the new URL containing the PAT, use the following command:
        
        ```
        git remote set-url origin <new-url>
        ```
        
        Replace `<new-url>` with the updated URL from the previous step.
        
        For example:
        
        ```
        git remote set-url origin <https://abcdef123456@github.com/example-user/example-repo.git>
        ```
        
    4. After running the command, the remote repository URL will be updated, and future interactions with the repository will use the new user account associated with the PAT.
    
    By switching the user account in the remote repository URL using a personal access token, you can authenticate and access the remote repository with the desired GitHub account credentials.
    

- When you are on a local repo that has access to a remote repo, and you switch users on the local repo, then the new user can commit to the original repo’s branches and overwrite its previous states
    
    WHY:
    
    Git tracks commits based on the user's name and email configured in the local Git configuration. When you switch users on the local repository by updating the user name and email, the subsequent commits will be associated with the new user's identity.
    
    If the new user has appropriate write access to the remote repository, they will be able to push their commits to the remote branches, potentially overwriting the previous states of those branches. However, the ability to overwrite previous states also depends on the branch protection rules and access control settings in place for the remote repository.
    
    It's important to note that modifying the commit history and overwriting previous states of a branch can have significant consequences, especially in collaborative environments. It is generally recommended to follow proper Git workflows, including code reviews, branch management, and collaboration practices, to ensure the integrity and maintain the history of the repository.
    
    Additionally, it's crucial to have clear communication and coordination within the team to avoid unintentional or destructive overwrites of previous states. Collaborators should have a shared understanding of the branch management and processes to prevent conflicts and maintain a coherent history of the repository.
    
- Can anyone who clones a repo commit to it and overwrite previous states?
    
    No.
    
    To push changes from a local repository to a remote repository, a user needs appropriate permissions and access rights to the remote repository. In most cases, users are required to have write access or be contributors to the remote repository to be able to push their changes.
    
    If someone without proper access tries to push changes to a remote repository, they will encounter an authentication or authorization error. Only users with the necessary privileges, such as the repository owner or authorized collaborators, can push changes to the remote repository.
    

- all i had to do before was switch user to avoid permission denied, but now it needs ssh key. why?
    
    If you were previously able to clone a private repository using HTTPS authentication after switching users, but now you are encountering permission denied errors that require an SSH key, it is possible that the repository's access permissions have been updated.
    
    GitHub allows repository owners to configure the access control method for their repositories. They can choose to enforce SSH authentication for repository access, which means that HTTPS authentication will no longer be sufficient to clone or interact with the repository.
    
    If you're now prompted for an SSH key when trying to clone the repository, it indicates that the repository owner has updated the access permissions to require SSH authentication. This change is made at the repository level and affects all users, regardless of the switching of GitHub users.
    
    To resolve this issue, you'll need to set up SSH authentication and associate your SSH key with your GitHub account. Here's a general outline of the steps involved:
    
    1. Generate an SSH key pair on your local machine if you haven't already done so. You can use the `ssh-keygen` command to generate the key pair. Make sure to specify a passphrase for added security.
    2. Add the generated SSH public key (`id_rsa.pub`) to your GitHub account. Log in to GitHub, go to your account settings, and navigate to the SSH and GPG keys section. Add a new SSH key and paste the contents of the `id_rsa.pub` file into the provided field.
    3. Configure your local Git client to use SSH instead of HTTPS for repository interactions. This involves updating the remote URL for the repository you're trying to clone. Replace the HTTPS URL with the SSH URL using the `git remote set-url` command. For example:
        
        ```
        git remote set-url origin git@github.com:username/repo.git
        
        ```
        
        Replace `username` with the appropriate username and `repo` with the repository name.
        
    4. Retry the clone command using the updated SSH URL:
        
        ```
        git clone git@github.com:username/repo.git
        
        ```
        
        This should now use SSH authentication instead of HTTPS.
        
    
    By following these steps, you'll be able to set up SSH authentication and clone the repository that now requires SSH key-based access. Remember to protect your SSH private key and passphrase since they provide access to your GitHub account.
    
- is it because before, i pushed to a fork as a new user? and the fork came from the original user which did have ssh auth?
    
    Yes, that could be a possible reason for the change in authentication requirements. When you push changes to a forked repository, it typically retains the same authentication method as the original repository. In this case, if the original repository had SSH authentication configured, your fork would also require SSH authentication for pushing changes.
    
    When you initially switched users and were able to clone the private repository using HTTPS authentication, it might have been because you were interacting with your forked repository, which allowed HTTPS authentication. However, if the original repository's access permissions were updated to require SSH authentication, it would affect both the original repository and any forks.
    
    To summarize:
    
    - If the original repository requires SSH authentication, all forks, including yours, will also require SSH authentication.
    - When you switched users and pushed changes to your fork, you were likely able to use HTTPS authentication because your fork retained the original repository's authentication settings.
    - Subsequently, if the original repository's access permissions were updated to enforce SSH authentication, you would need to configure SSH authentication to interact with both the original repository and your fork.
    
    To resolve this issue and access the repository, follow the steps mentioned earlier to set up SSH authentication and associate your SSH key with your GitHub account. Then update your local Git configuration to use the SSH URL for cloning and pushing to the repository and your fork.
    
    Remember to consult with the repository owner or organization administrator for any specific access requirements or further assistance.