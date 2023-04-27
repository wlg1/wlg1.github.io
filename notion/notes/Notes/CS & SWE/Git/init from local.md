# init from local

How to create a repo on github from your local repo?

1. Log in to your GitHub account and click on the "New" button on the top right-hand side of the page. Click on "Create repository"
2. Locally, cd to dir with files for local repo. Initialize the local repository:
    
    `git init`
    
3. Add the remote repository URL by typing the following command in the terminal:
    
    `git remote add origin <remote repository URL>`
    
    Now you can add files to local, commit, then push to remote