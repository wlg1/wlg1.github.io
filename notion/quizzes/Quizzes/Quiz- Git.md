# Quiz- Git

Local Repo

- In git, there is only one version of files on my laptop. But there are multiple branches in my local repo. How can this be?
    
    The local working machine (eg. your laptop) IS NOT the ‘main branch’ or any branch of the local repo
    
    - In the git command prompt, how do I list the files actually on the laptop, not just on any branch? How do I list the files on a branch?
        
        `ls` : on working machine
        
        `ls-files` : checkout to branch then use this
        
    - How to compare between local working machine and a local branch?
        
        git diff <branch>
        
    - How to compare between two local branches?
        
        `git diff <branch_1> <branch_2>`
        
    - How to compare between a local branch and a remote branch?
        
        `git diff <local-branch> <remote>/<remote-branch>`
        
        Eg) `git diff main origin/main`
        

Remote Repo

[Remote Repo](https://www.notion.so/Remote-Repo-065557e5db3d4170bcee5b1714ad6efc?pvs=21) 

- What is origin?
    
    "Origin" is a commonly used default name for the main remote repository when you clone a repository or add a remote repository to your local Git configuration. However, it is not a requirement, and the remote repository can have a different name.
    
- How to create a remote branch?
    1. Create a local branch: First, create a new branch locally.
        
        ```
        git checkout -b new-feature
        ```
        
    2. Push the branch to the remote repository: Use the `git push` command followed by the name of the remote repository (e.g., "origin") and the name of the local branch. 
        
        ```
        git push origin new-feature
        ```
        
    
- What is HEAD?
    
    A reference to the current commit or branch you are working on
    

Merging

- How to merge?
    
    git checkout <branch to merge into>
    
    git merge <branch to merge in>
    
- How to do a pull request?
    1. Fork, clone
    2. branch, commit, push
    3. Discuss with owner and team acc to repo etiquette
    4. Make Pull Request 

Users

- How do you switch users via local git bash shell?
    
    `git config user.email "github account email"`
    
    Note that [user.name](http://user.name) doesn’t matter