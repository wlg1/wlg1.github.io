# Branch

When to use:

Create a branch for every new feature

Branches allow you to move back and forth between 'states' of a project. Official git docs describe branches this way: ‘A branch in Git is simply a lightweight movable pointer to one of these commits.’

- Make branch
    
    [https://www.git-tower.com/learn/git/faq/create-branch](https://www.git-tower.com/learn/git/faq/create-branch)
    
    `git branch iss53`  : Make new branch for “issue #53” 
    
    `git checkout iss53` : Switch to branch for “issue #53” 
    
    To create a new branch for “issue #53” and switch to it at the same time:
    
    `git checkout -b iss53`
    
- Check the differences between two branches?
    
    `git diff <branch1> <branch2>`
    

[https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging)

- What's a production branch?
    
    A production branch, also known as a release branch or a stable branch, is a branch in a version control system that represents the codebase that is considered stable and suitable for deployment to a production environment. It is a branch where the software or application is in a state that is ready for public use or release.
    
    In software development workflows that follow a branching model like Gitflow, the production branch is often the main branch or a long-lived branch, such as "master" or "main." It contains the code that has passed through development, testing, and quality assurance stages and has been deemed stable and reliable for production use.
    
    The purpose of having a production branch is to separate the codebase that is ready for deployment from ongoing development work. Developers typically work on feature branches or development branches, where they implement new features or fix issues. Once those changes are thoroughly tested and approved, they are merged into the production branch to make them part of the stable codebase.
    
    Using a production branch helps maintain a clear separation between development and production environments, ensuring that only well-tested and approved code is deployed to production. It provides a controlled path for releasing updates and minimizing the risk of introducing bugs or instability into the live system.
    
- What's an upstream branch?
    
    An upstream branch is a reference to a branch in a remote repository. It serves as a point of reference for your local branch and allows Git to track the relationship between the local and remote branches.
    
    When you clone a repository or create a branch based on a remote branch, Git automatically sets up the upstream branch for you. The upstream branch typically has the same name as your local branch and resides in the remote repository you cloned from. It represents the branch to which you can push your local branch changes or from which you can pull updates.
    
    Having an upstream branch provides several benefits:
    
    1. **Pushing changes:** When you have an upstream branch configured, you can use the "git push" command without specifying the remote and branch names every time. Git automatically knows where to push the changes.
    2. **Pulling updates:** You can use the "git pull" command without explicitly specifying the remote and branch names. Git will fetch the latest changes from the upstream branch and merge them into your local branch.
    3. **Tracking changes:** Git can compare the differences between your local branch and the upstream branch using commands like "git diff" or "git status." It helps you identify the changes made on both sides.
    
    To set up an upstream branch manually, you can use the "--set-upstream" or "-u" flag when pushing your local branch for the first time. For example:
    
    ```
    git push --set-upstream origin feature-A
    
    ```
    
    This command pushes the local branch "feature-A" to the remote repository named "origin" and sets "origin/feature-A" as the upstream branch.
    
    In summary, an upstream branch establishes a connection between your local branch and a corresponding branch in a remote repository, enabling you to push and pull changes conveniently.
    

Display all branches LOCAL REPO: `git branch`

Display all branches, LOCAL AND REMOTE: `git branch -a`

Display all branches, REMOTE: `git branch -r`

The commits on github are specific to each branch. So when you push a new branch, you must switch to it to see its commit. It won’t be displayed on main.

![Untitled](Branch%20265cb6cbc5ee44b1a5aee59ea96804ac/Untitled.png)

---

Remote Repo Branches

```python
$ git branch -r
	origin/HEAD -> origin/main
	origin/main
```

In Git, "HEAD" is a reference to the current commit or branch you are working on. It is essentially a pointer to the latest commit in your repository.

- **`git checkout`**: Use this command to switch branches or check out a specific commit. When you switch branches, "HEAD" will be updated to point to the new branch.
- **`git commit`**: This command creates a new commit, and "HEAD" will be moved to point to the newly created commit.

- How to create a remote branch?
    1. Create a local branch: First, create a new branch locally.
        
        ```
        git checkout -b new-feature
        ```
        
    2. Push the branch to the remote repository: Use the `git push` command followed by the name of the remote repository (e.g., "origin") and the name of the local branch. 
        
        ```
        git push origin new-feature
        ```
        
    
    Note: By default, Git will set up the upstream tracking relationship when you push a new branch. It means that future `git push` and `git pull` commands on that branch will be aware of the remote branch and its location.
    
- Can you switch to a remote branch when you're on the command line in a local repo?
    
    No. Remote branches in Git are references to branches in the remote repository and are not directly editable or checkout-able on the local machine.
    
    To work with a remote branch, you need to create a local tracking branch that corresponds to the remote branch. This local tracking branch will keep your local repository in sync with the remote branch and allow you to make changes and perform operations on the branch.
    
    To switch to a remote branch, you'll need to perform the following steps:
    
    1. Fetch the latest changes: Run the command `git fetch` to fetch the latest updates from the remote repository. This ensures that your local repository is up to date with the remote branches.
    2. Create a local tracking branch: Once you have fetched the changes, create a local branch that tracks the remote branch using the `git checkout` command with the `b` flag. For example, to create a local tracking branch named "my-branch" that tracks the remote branch "origin/my-branch", use the following command:
        
        ```
        git checkout -b my-branch origin/my-branch
        ```
        
        This command creates a new local branch based on the remote branch and sets it as the active branch.
        
    3. Switch to the local branch: After creating the local tracking branch, you can switch to it using the `git checkout` command without any arguments:
        
        ```
        git checkout my-branch
        ```
        
    
    Now, you are on the local branch that tracks the corresponding remote branch. You can make changes, commit, and perform other Git operations on this branch as you would with any other local branch. When you're ready to push your changes, use `git push` to update the remote branch with your local commits.
    
    Remember to fetch and pull from the remote repository periodically to stay in sync with any changes made to the remote branch by other collaborators.
    
- Can you see branches in other local repos?
    
    No, you cannot directly see branches in other local repositories unless you have access to those repositories or you are working on a shared network or collaborative environment where you can access the file system of other local repositories.
    
    Each local repository is self-contained and isolated by default. It means that branches and other Git-related information within a local repository are not directly visible or accessible from other repositories unless you explicitly share or collaborate on the repository.
    
    However, you can gather information about branches in other local repositories indirectly through collaboration and remote repositories. If you have access to a remote repository (such as a repository hosted on a Git hosting service like GitHub or GitLab), you can clone or fetch that remote repository to create a local copy on your machine. Then, you can inspect the branches within that local copy and interact with them.
    
    Additionally, if you are working in a shared network environment or have access to the file system of other local repositories, you can navigate to the file system directories where those repositories are located and manually inspect the branch files (usually stored under the `.git/refs/heads/` directory) to see the available branches. However, modifying or interacting with branches in other local repositories directly on the file system can lead to complications and is generally not recommended.
    

---

Workspace vs Local Repo Branches

- In git, there is only one version of files on my laptop. But there are multiple branches in my local repo. How can this be?
    
    In Git, each branch represents a separate line of development. When you create a new branch, Git creates a new pointer to the current commit you are on, allowing you to switch between branches and work on different versions of your project simultaneously.
    
    While each branch may have its own set of commits and changes, the actual files on your laptop are typically shared across all branches. When you switch between branches, Git updates the working directory to reflect the state of the files as they exist in the branch you switched to. This means that the files you see in your local repository will correspond to the branch you have currently checked out.
    
    To better understand how this works, let's consider a scenario:
    
    1. You have a Git repository on your laptop with a `master` branch.
    2. You create a new branch called `feature` using the command `git branch feature`.
    3. Now, you have two branches: `master` and `feature`, both pointing to the same commit.
    4. If you make changes to files while on the `feature` branch, those changes will be reflected in your working directory. However, the `master` branch will remain unchanged until you merge the `feature` branch back into `master`.
    5. When you switch back to the `master` branch using `git checkout master`, the files in your working directory will be updated to match the state of the `master` branch.
    
    In summary, although you have multiple branches in your local repository, the files on your laptop are shared between them. The branch you have checked out determines which version of the files you see in your working directory at any given time.
    

The local working machine (eg. your laptop) IS NOT the ‘main branch’ or any branch of the local repo

The “working machine” is a way to say what computer your current “working directory” (where shell is pointing to) is in. **Working Directory/Working Tree** refers to the directory on your local machine where you have cloned or initialized a Git repository. Another name is ********************Workspace.********************

To make changes from the Workspace to the local repo, all you need to do is commit. Do not push; push is for commiting local repo changes to the remote repo.

- In the git command prompt, how do I list the files actually on the laptop, not just on any branch?
    
    To list the files that exist on your local machine, regardless of the Git branch, you can use regular command line or terminal commands. Here are a few commonly used commands to accomplish this:
    
    1. `ls` command (Unix-based systems): This command lists the files and directories in the current directory.
        
        ```
        $ ls
        file1.txt
        file2.txt
        directory/
        
        ```
        
    2. `dir` command (Windows): This command lists the files and directories in the current directory.
        
        ```
        C:\\> dir
        06/22/2023  10:00 AM    <DIR>          directory
        06/22/2023  09:55 AM                 0 file1.txt
        06/22/2023  09:55 AM                 0 file2.txt
                       2 File(s)              0 bytes
                       1 Dir(s)   1,048,576,000 bytes free
        
        ```
        
    
    These commands will list the files and directories in the current directory where you are executing the Git commands. They do not require using Git specifically and will show you the files on your laptop, irrespective of the Git repository or branch you are currently in.
    
- see files in repo using git command line
    
    To see the files in a Git repository using the command line, you can use the following Git commands:
    
    1. `git ls-files`: This command lists all the files tracked by Git in the current repository. It will display the file paths relative to the repository's root directory.
        
        ```
        $ git ls-files
        file1.txt
        file2.txt
        directory/file3.txt
        
        ```
        
    2. `git ls-tree`: This command shows the content of a specific tree or directory within the repository. You need to provide the treeish reference (commit hash or branch name) and the path to the tree or directory.
        
        ```
        $ git ls-tree HEAD
        100644 blob a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8 file1.txt
        100644 blob b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9 file2.txt
        040000 tree c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0 directory
        
        ```
        
    3. `git ls-tree --name-only`: This command lists only the names of the files or directories without additional information.
        
        ```
        $ git ls-tree --name-only HEAD
        file1.txt
        file2.txt
        directory
        
        ```
        
    4. `git status`: This command displays the current status of your repository, including information about modified, untracked, and deleted files.
        
        ```
        $ git status
        On branch master
        Your branch is up to date with 'origin/master'.
        
        Changes not staged for commit:
          (use "git add <file>..." to update what will be committed)
          (use "git restore <file>..." to discard changes in working directory)
                modified:   file1.txt
        
        Untracked files:
          (use "git add <file>..." to include in what will be committed)
                newfile.txt
        
        no changes added to commit (use "git add" and/or "git commit -a")
        
        ```
        
    
    These commands provide different ways to view the files in your Git repository using the command line interface. Choose the one that suits your specific needs.
    
- How to compare local branch to Workspace ?
    
    git diff <branch>
    
- How do you see the local repo, not just the working dir?
    
    To see the contents of the local Git repository, including the committed history, branches, tags, and other Git-related information, you can use various Git commands. Here are a few commands to inspect the local Git repository:
    
    1. **git log**: Running the command `git log` in the terminal while in the repository's root directory will display the commit history of the repository. It shows the commit hashes, authors, dates, and commit messages of each commit.
    2. **git branch**: The command `git branch` lists all the branches in the repository. It shows the current branch you're on, marked with an asterisk (*), and other branches present in the repository.
    3. **git tag**: Running `git tag` displays a list of tags in the repository. Tags are used to mark specific points in history, such as releases or significant milestones.
    4. **git status**: The command `git status` provides an overview of the current state of the repository, showing information about modified files, untracked files, and branch information.
    
    These commands provide different perspectives on the contents and status of the local Git repository. They can be used together to get a comprehensive view of the repository and its history.
    

ls : all files on working machine

git ls-files : all files in branch. you must add and commit from the working machine to a local repo branch for these to show up.

---

[https://softwareengineering.stackexchange.com/questions/278686/having-a-production-branch-or-using-master](https://softwareengineering.stackexchange.com/questions/278686/having-a-production-branch-or-using-master)

[https://learngitbranching.js.org/](https://learngitbranching.js.org/)

[https://www.atlassian.com/git/tutorials/using-branches](https://www.atlassian.com/git/tutorials/using-branches)