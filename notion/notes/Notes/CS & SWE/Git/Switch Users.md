# Switch Users

- How do we switch users in git bash?
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