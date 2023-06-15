# Branches

When to use:

Create a branch for every new feature

Branches allow you to move back and forth between 'states' of a project. Official git docs describe branches this way: ‘A branch in Git is simply a lightweight movable pointer to one of these commits.’

- Make branch
    
    [https://www.git-tower.com/learn/git/faq/create-branch](https://www.git-tower.com/learn/git/faq/create-branch)
    
    `git branch iss53`  : Make new branch for “issue #53” 
    
    `git checkout iss53` : Switch to branch for “issue #53” 
    
    To create a new branch for “issue #53” and switch to it at the same time:
    
    `git checkout -b iss53`
    

[https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging)

- What's a production branch?
    
    A production branch, also known as a release branch or a stable branch, is a branch in a version control system that represents the codebase that is considered stable and suitable for deployment to a production environment. It is a branch where the software or application is in a state that is ready for public use or release.
    
    In software development workflows that follow a branching model like Gitflow, the production branch is often the main branch or a long-lived branch, such as "master" or "main." It contains the code that has passed through development, testing, and quality assurance stages and has been deemed stable and reliable for production use.
    
    The purpose of having a production branch is to separate the codebase that is ready for deployment from ongoing development work. Developers typically work on feature branches or development branches, where they implement new features or fix issues. Once those changes are thoroughly tested and approved, they are merged into the production branch to make them part of the stable codebase.
    
    Using a production branch helps maintain a clear separation between development and production environments, ensuring that only well-tested and approved code is deployed to production. It provides a controlled path for releasing updates and minimizing the risk of introducing bugs or instability into the live system.
    

Display all branches LOCAL REPO: `git branch`

Display all branches, LOCAL AND REMOTE: `git branch -a`

Display all branches, REMOTE: `git branch -r`

[https://www.atlassian.com/git/tutorials/using-branches](https://www.atlassian.com/git/tutorials/using-branches)

---

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

[https://softwareengineering.stackexchange.com/questions/278686/having-a-production-branch-or-using-master](https://softwareengineering.stackexchange.com/questions/278686/having-a-production-branch-or-using-master)

[https://learngitbranching.js.org/](https://learngitbranching.js.org/)