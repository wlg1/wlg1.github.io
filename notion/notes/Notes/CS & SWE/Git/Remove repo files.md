# Remove repo files

Cached doesn’t remove from computer, but is a command to staging

git rm -r --cached *.aux
git rm -r --cached *.wav
git add .
git commit -m "Removed tracked files which shouldn't be tracked"
git push

Yes, the **`git rm`** command, without the **`--cached`** option, will remove files from both the local Git repository and your local computer. It effectively deletes the files from your working directory, so they are no longer present on your local machine.

If you want to keep a copy of the files on your local machine but remove them from version control, you should use the **`git rm --cached`** command as initially mentioned in your first question. This command removes the files from the Git index (staging area) but leaves them in your working directory.

I did that, but when I pushed the local repo to remote repo, it still pushed the aux files. Shouldn't all the aux files from local repo have been deleted?

- will "git filter-branch --tree-filter 'rm -f *.aux' HEAD" affect local working directory files?
    
    Yes, running the command `git filter-branch --tree-filter 'rm -f *.aux' HEAD` will affect both the Git history and your local working directory files. Here's what will happen:
    
    1. **Git History**: This command will rewrite the Git history of your repository by going through each commit in the history (up to `HEAD`) and applying the `rm -f *.aux` command to the tree of each commit. This means that the `.aux` files will be removed from the history of your repository.
    2. **Working Directory**: While the command is running, it will temporarily check out each commit in the history, apply the filter (removing `.aux` files), and then check out the next commit. During this process, your working directory will be updated to match each checked-out commit, which will also remove the `.aux` files from your local working directory.
    
    Please make sure you have a backup of your repository or any important files before running this command, as it can have a significant impact on both your Git history and working directory. Additionally, consider coordinating with any collaborators to inform them of these changes, especially if you're working in a shared repository.
    

- is the working directory. the local repo or the computer?
    
    The working directory is the directory on your local computer where you have a copy of your Git repository. In other words, the working directory is the place where you create, edit, and organize your files as you work on your project. This directory contains both the files that are tracked by Git and any untracked files that are not currently managed by Git.
    
    To clarify:
    
    - The "local repo" refers to your entire Git repository, which includes the working directory, the Git database (containing the history and commits), and other Git-related files. It's the entire project stored on your computer.
    - The "working directory" is a specific directory within your local repo where you do your day-to-day work. It contains both tracked files (files Git is aware of and that are part of the version history) and untracked files (files not yet added to Git).
    
    When you interact with Git, you typically make changes in your working directory, stage those changes, and then commit them to your local repository. The working directory is the place where you manipulate and create files on your computer, and it's an essential part of your local repository.
    

how do I check if *.mkv files are in the local repo?

git ls-files "*.mkv”

- how do I do a history rewrite that only affects the local repo, not the working directory?
    
    To perform a history rewrite that only affects the local repository (not the working directory) while keeping the working directory clean, you can use the `filter-branch` command with the `--index-filter` option. This command will modify the Git history without checking out the files in the process. Here's how you can do it:
    
    1. Make sure that you have a backup of your local repository before proceeding, as history rewriting can be irreversible, and it's always wise to have a safety net.
    2. Open your terminal or command prompt.
    3. Navigate to the root directory of your Git repository using the `cd` command if you're not already there.
    4. Run the following `filter-branch` command to remove the `.mkv` files from the Git history while keeping your working directory clean:
    
    ```bash
    git filter-branch --index-filter 'git rm --cached --ignore-unmatch *.mkv' -- --all
    
    ```
    
    - `-index-filter`: This option specifies the filter to apply to the index (staging area) without checking out the files.
    - `git rm --cached --ignore-unmatch *.mkv`: This command will remove the `.mkv` files from the index without deleting them from your working directory. The `-ignore-unmatch` option ensures that Git doesn't fail if it can't find any `.mkv` files to remove.
    - `- --all`: This specifies that you want to rewrite the history for all branches in your repository.
    1. Git will go through each commit in the history and apply this filter. The `.mkv` files will be removed from the index of each commit, but your working directory won't be affected.
    2. After the process is complete, you may need to force-push the changes to the remote repository if you've already pushed the previous history with the `.mkv` files. Be cautious with force-pushes, as they can disrupt collaboration. Communicate with your collaborators if necessary.
    
    Please remember that history rewriting can be a complex and potentially disruptive operation, especially in shared repositories. It's important to coordinate with other collaborators and ensure everyone is aware of and comfortable with the changes you're making to the repository's history.
    

---

[https://stackoverflow.com/questions/19730565/how-to-remove-files-from-git-staging-area](https://stackoverflow.com/questions/19730565/how-to-remove-files-from-git-staging-area)

`git reset HEAD -- .`

`git reset --soft HEAD^` : just rmvs last staging