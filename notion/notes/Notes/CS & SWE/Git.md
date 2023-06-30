# Git

- Resource List
    
    [https://product.hubspot.com/blog/git-and-github-tutorial-for-beginners](https://product.hubspot.com/blog/git-and-github-tutorial-for-beginners)
    
    [https://www.atlassian.com/git/tutorials](https://www.atlassian.com/git/tutorials)
    
    [https://git-scm.com/docs/gittutorial](https://git-scm.com/docs/gittutorial)
    
    https://livablesoftware.com/tools-to-visualize-the-history-of-a-git-repository/#:~:text=to%20learn%20Git.-,GitUp,and%20merges%20with%20perfect%20clarity.
    
    https://git-scm.com/book/en/v2/Appendix-A%3A-Git-in-Other-Environments-Graphical-Interfaces
    

---

**Basic Workflow**

- Workflow Diagram
    
    ![Untitled](Git%204c9bd0a8425541b68fa7a146f2df3f37/Untitled.png)
    
- How to create a repo on github from your local repo
    1. Log in to your GitHub account and click on the "New" button on the top right-hand side of the page. Click on "Create repository"
    2. Locally, cd to dir with files for local repo. Initialize the local repository:
        
        `git init`
        
    3. Add the remote repository URL by typing the following command in the terminal:
        
        `git remote add <remote-name> <remote repository URL>`
        
        `<remote-name>` is usually `origin`
        
        - Why does url have .git?
            
            The inclusion of ".git" in the URL is a convention and not always required. Some Git hosting services or repositories may allow you to omit the ".git" suffix in the URL and still successfully interact with the repository. 
            
            The ".git" suffix in the remote repository URL refers to the Git repository itself. Including ".git" in the URL helps Git clients and tools identify that the provided URL is for a Git repository and ensures that the necessary Git-specific operations and protocols are used when interacting with that URL.
            
- Make new branch *(when adding new feature or move b/w commits)*
    
    [https://www.git-tower.com/learn/git/faq/create-branch](https://www.git-tower.com/learn/git/faq/create-branch)
    
    `git branch iss53`  : Make new branch for “issue #53” 
    
    `git checkout iss53` : Switch to branch for “issue #53” 
    
    To create a new branch for “issue #53” and switch to it at the same time:
    
    `git checkout -b iss53`
    
    To push this local branch to remote:
    
    `git push <repo-name> <new-branch-name>`
    
    <<<
    
    - What does 'move b/w commits' mean?
        
        When referring to "moving between commits," it means changing the current state of your repository to a specific commit in the commit history.
        
        1. **Viewing Previous Versions**: You can move to a previous commit to see the state of your project at that particular point in time. This can be useful for inspecting code, reviewing changes, or identifying when a specific feature or bug was introduced.
        2. **Branch Switching**: By moving to a specific commit, you can switch to a different branch or create a new branch from that commit. This is commonly done when you want to work on a specific feature or fix a bug independently from the current branch.
        3. **Rewriting History**: Moving between commits allows you to modify the commit history, such as rearranging, squashing, or amending commits. These operations can be performed with Git commands like `git rebase`, `git cherry-pick`, or interactive rebasing (`git rebase -i`).
        
        To move between commits, you typically use Git commands such as `git checkout` or `git switch`. For example:
        
        ```
        git checkout <commit-hash>
        ```
        
        Replace `<commit-hash>` with the actual commit hash or a branch name pointing to the desired commit. 
        
- Update remote branch with local branch changes
    1. Add all the files from working machine to the local repository by typing the following command in the terminal:
        
        `git add .`
        
    2. Commit the changes by typing the following command in the terminal:
        
        `git commit -m "[what was changed]"`
        
    3. Push the changes to the remote repository by typing the following command in the terminal:
        
        `git push -u <repo-name> <branch-name>`
        
        OR: `git push`
        
        - What does "push -u" do?
            
            Set up tracking between the local branch and the remote branch
            
            By setting up tracking, Git remembers the relationship between the local and remote branches. This allows you to use subsequent `git push` or `git pull` commands without specifying the remote branch explicitly.
            
            For example, if you are on the "feature-branch" and run `git push -u origin feature-branch`, Git pushes the "feature-branch" to the "origin" remote repository and sets up tracking between the local "feature-branch" and the "origin/feature-branch" on the remote repository. After this, you can use `git push` and `git pull` without specifying the remote and branch names.
            
            Additionally, when you run `git status`, Git will show you the relationship between the local and upstream branches, informing you of the ahead/behind status.
            
            Using `git push -u` is particularly useful when you are pushing a branch for the first time.
            
- Make [Pull Requests](Git%204c9bd0a8425541b68fa7a146f2df3f37/Pull%20Requests%20c48bf9dcf2944e2989b66f2e5e53124b.md) on Github
    
    This is to change remote main branch with changes from another branch
    
    A pull request alerts a repo's owners that you want to make changes to their code. It allows them to review the code.
    
    - Do you have to do a pull request?
        
        Not in **Individual Work**. It serves as a way in collabs to propose and review changes before merging.
        
- [Merge](Git%204c9bd0a8425541b68fa7a146f2df3f37/Merge%209ebb454e688443e6884980079a13df63.md) new branch from
- Update your local repo with remote changes
    
    `git pull`
    
    - What does it mean "pull the changes from upstream”
        
        When you "pull the changes from upstream," it means you are retrieving the latest changes made to a repository or branch in a version control system, such as Git. The term "upstream" typically refers to the original repository or branch that you cloned or forked from. By pulling regularly, you can avoid conflicts .
        

### All Notes

[Remote Repo](Git%204c9bd0a8425541b68fa7a146f2df3f37/Remote%20Repo%20065557e5db3d4170bcee5b1714ad6efc.md)

[Fork](Git%204c9bd0a8425541b68fa7a146f2df3f37/Fork%203c0dff0745b84401a39f322a2a232bb6.md)

[Staging](Git%204c9bd0a8425541b68fa7a146f2df3f37/Staging%206b42eb45b45b4ee7b8ffb818f4a7eafa.md)

[Commit](Git%204c9bd0a8425541b68fa7a146f2df3f37/Commit%205b1331da28bd4dc89826002c931cb6a2.md)

[Branch](Git%204c9bd0a8425541b68fa7a146f2df3f37/Branch%20265cb6cbc5ee44b1a5aee59ea96804ac.md)

[Merge](Git%204c9bd0a8425541b68fa7a146f2df3f37/Merge%209ebb454e688443e6884980079a13df63.md)

[Pull Requests](Git%204c9bd0a8425541b68fa7a146f2df3f37/Pull%20Requests%20c48bf9dcf2944e2989b66f2e5e53124b.md)

- Git fetch vs pull?
    
    ![Untitled](Git%204c9bd0a8425541b68fa7a146f2df3f37/Untitled%201.png)
    
    1. `git fetch`: This command retrieves the latest changes from the remote repository, including all branches and tags, without automatically merging them into your current branch. It updates your local copy of the remote branches, allowing you to inspect and review the changes before incorporating them into your work. Fetching essentially synchronizes your local repository with the remote repository, ensuring you have the latest commits, branch updates, and tags.
    2. `git pull` merges the remote branch into your current local branch.
    - If you want to review the changes before merging them, use `git fetch`. This allows you to inspect the changes, compare branches, run tests, or make other preparations before merging.
    - If you trust the changes and want to quickly integrate them, use `git pull`. It automatically merges the changes from the remote branch into your current branch, saving you the extra step of manually performing a merge.
    - If you're working on a shared branch or collaborating with others, it's generally a good practice to use `git fetch` and review the changes before merging. This allows you to maintain control over what gets merged and resolve any conflicts that may arise.
    
    It's worth noting that both `git fetch` and `git pull` can be configured with additional options and arguments to customize their behavior. For example, you can specify the remote repository and branch to fetch or pull from.
    

[Rebase](Git%204c9bd0a8425541b68fa7a146f2df3f37/Rebase%20ab7a3565d33344aa9958e3d17b285919.md)

[Switch Users](Git%204c9bd0a8425541b68fa7a146f2df3f37/Switch%20Users%200f47e20825d648b398cc49c1afe05a9f.md)

[Security](Git%204c9bd0a8425541b68fa7a146f2df3f37/Security%208b45c6b0f41b4a55ac1f5b402f39c00a.md)

File Types

[requirements.txt](Git%204c9bd0a8425541b68fa7a146f2df3f37/requirements%20txt%204528740894b7494f933c0915795d144a.md) 

### Errors

- git pull —> fatal: refusing to merge unrelated histories
    
    This error message is typically encountered when trying to merge two branches that don't have a common ancestor. Git uses the history of a branch to determine how to merge it with another branch. If there is no common ancestor, Git will consider the branches as unrelated and will refuse to merge them.
    
    To fix this issue, you can try the following steps:
    
    1. Ensure that you are in the correct branch. You can check this by running the command **`git branch`**.
    2. Fetch any changes from the remote repository by running the command **`git fetch`**.
    3. Create a new branch from the remote branch you want to merge. You can do this by running the command **`git checkout -b <new-branch-name> origin/<remote-branch-name>`**.
    4. Merge the new branch with your current branch by running the command **`git merge <new-branch-name>`**.
    
    If you still encounter the same error message after trying these steps, it is possible that the branches have unrelated histories and cannot be merged. In this case, you may need to consider a different approach to combine the changes from the two branches.
    
- error: Your local changes to the following files would be overwritten by merge
    
    ```python
    error: Your local changes to the following files would be overwritten by merge:
            ai_settings.yaml
    Please commit your changes or stash them before you merge.
    Aborting
    Updating 816dc14..4870356
    ```
    
    This error message indicates that you have some uncommitted changes in the **`ai_settings.yaml`** file, and Git is unable to merge the changes from the remote branch because it would overwrite your local changes.
    
    To resolve this issue, you can either commit your changes or stash them before merging.
    
    If you want to commit your changes, you can simply run the following commands:
    
    ```
    sqlCopy code
    git add ai_settings.yaml
    git commit -m "Committing changes to ai_settings.yaml"
    
    ```
    
    Alternatively, if you want to stash your changes, you can run the following command:
    
    ```
    arduinoCopy code
    git stash save "Stashing changes to ai_settings.yaml"
    
    ```
    
    This will save your changes to a stash, allowing you to merge the changes from the remote branch without overwriting your local changes. Once the merge is complete, you can apply the stash using the following command:
    
    ```
    Copy code
    git stash apply
    
    ```
    
    This will apply your changes to the **`ai_settings.yaml`** file. If there are any conflicts, Git will prompt you to resolve them manually.
    
    - will git stash only affect the local?
        
        Yes, **`git stash`** will only affect your local repository.
        
        When you run the **`git stash`** command, Git will save your local changes in a stash and revert your working directory to the last committed state. This means that the changes you stashed are no longer visible in your working directory, but they are still saved in the Git repository.
        
        The stash is saved locally on your machine, and it's not pushed to the remote repository. Other team members who are working on the same remote repository won't be affected by your stash.
        
        You can apply the stash later to restore your saved changes to your working directory. However, if you're not careful, applying the stash can cause conflicts with other changes that have been made to the same file since you stashed your changes. Therefore, it's important to review and test your changes carefully before applying the stash to ensure that your changes do not conflict with other changes made in the repository.
        
    - $git stash apply
    CONFLICT (modify/delete): ai_settings.yaml deleted in Updated upstream and modified in Stashed changes. Version Stashed changes of ai_settings.yaml left in tree.
    CONFLICT (modify/delete): .env.template deleted in Stashed changes and modified in Updated upstream. Version Updated upstream of .env.template left in tree.
        
        The **`git stash apply`** command attempts to apply the most recent stash to your working directory. However, in your case, it seems that there are conflicts between the changes made in the stash and the changes made in the updated upstream branch.
        
        The error message indicates that the **`ai_settings.yaml`** file was deleted in the upstream branch but modified in the stash, and the **`.env.template`** file was deleted in the stash but modified in the upstream branch. Git is not able to automatically resolve these conflicts, and you need to manually resolve them before you can apply the stash.
        
        To resolve these conflicts, you can follow these steps:
        
        1. Use the **`git status`** command to see which files have conflicts.
        2. Open the conflicting files and manually resolve the conflicts by editing the files to include the changes you want to keep.
        3. After you have resolved the conflicts, run the **`git add`** command to stage the changes.
        4. Once all conflicts are resolved, you can run the **`git stash apply`** command again to apply the stash.
        
        If there are still conflicts, you may need to repeat the above steps until all conflicts are resolved. After the stash is applied successfully, you should review and test your changes carefully to ensure that everything is working as expected.
        
- fatal: The current branch feature-A has no upstream branch.
To push the current branch and set the remote as upstream, use `git push --set-upstream origin feature-A`
    
    An upstream branch is a remote branch in a remote repo. When you push changes using just "git push" from a branch in a local repo to a branch in a remote repo, git tries to find a branch in the remote repo with the same name. So if this remote branch name doesn’t exist, you will get this error. So either be more specific with `git push <remote> <branch>` or push this local branch to the remote repo.
    

### Questions

---

- After cloning repo to local, how to get latest updates?
    
    SOLN: git pull
    
- What's the best format to save a github directory structure in?
    1. JSON: This is a common format for representing structured data, and it's easy to parse and manipulate using many programming languages. GitHub's API returns directory structure data in JSON format, so you could save it directly as a JSON file. However, JSON may not be the best format for human-readable data.
    2. YAML: This is a human-readable format that is often used for configuration files. It's easy to read and write by both humans and computers, and it supports hierarchical structures. YAML can be a good choice if you want to make the directory structure easily readable and editable by humans.
    3. XML: This is a widely-used format for representing structured data, and it's supported by many programming languages and tools. XML can be a good choice if you need to exchange data with other systems that use XML or if you need to validate the structure of the data using XML Schema.
    4. CSV: This format is simple and widely used for tabular data. If you only need to represent a flat directory structure with just the file and folder names, then CSV can be a good choice.
- How get directory structure of github to a json file?
    
    You can get the directory structure of a GitHub repository in JSON format using the GitHub REST API.
    
    Here are the steps you can follow:
    
    1. Generate a personal access token from your GitHub account settings.
    2. Make a GET request to the GitHub API endpoint **`https://api.github.com/repos/{owner}/{repo}/contents/{path}`** where **`{owner}`** is the username or organization that owns the repository, **`{repo}`** is the name of the repository, and **`{path}`** is the directory or file path that you want to retrieve. For the root directory, use an empty string for **`{path}`**.
    3. Parse the JSON response to extract the directory structure.
    
    Here's a Python script that demonstrates how to retrieve the directory structure of a GitHub repository in JSON format:
    
    ```
    import requests
    import json
    
    # GitHub repository details
    owner = "github"
    repo = "docs"
    path = ""
    
    # GitHub API endpoint
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"
    
    # Personal access token
    token = "your_personal_access_token_here"
    
    # Headers
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/vnd.github.v3+json"}
    
    # Make a GET request to the API endpoint
    response = requests.get(url, headers=headers)
    
    # Parse the JSON response
    if response.ok:
        directory_structure = response.json()
        print(json.dumps(directory_structure, indent=4))
    else:
        print(f"Failed to retrieve directory structure. Status code: {response.status_code}")
    
    ```
    
    Replace the values of **`owner`**, **`repo`**, and **`token`** with your own repository details and personal access token, respectively. The script will print the directory structure in JSON format to the console.
    
    Note that the GitHub API has rate limits, so you may need to authenticate or use pagination to retrieve the entire directory structure of a large repository.
    
- see all new commits
    
    git log
    
- see which files are unmerged at any point after a merge conflic
    
    git status
    
- in github, how do we add work to an existing commit?
    
    git add -A
    
    git commit --amend
    
    git push  (says still have to: [https://smartlogic.io/blog/git-commit-amend/](https://smartlogic.io/blog/git-commit-amend/) )
    
    OR: git push --force origin main
    
    ---
    
    To add work to an existing commit in Git, you typically need to follow these steps:
    
    1. **Create a new branch (optional):** It's a good practice to create a new branch before making any changes to the commit history. This helps keep your changes separate from the main branch until you're ready to merge them.
        
        ```
        git checkout -b new-branch-name
        
        ```
        
    2. **Make the desired changes:** Modify the files in your project as needed.
    3. **Stage the changes:** Add the modified files to the staging area.
        
        ```
        git add file1 file2 ...
        
        ```
        
    4. **Amend the commit:** Combine your new changes with the existing commit using the `git commit --amend` command. This command replaces the previous commit with a new commit that includes both the original changes and your new changes.
        
        ```
        git commit --amend
        
        ```
        
        This will open your default text editor where you can modify the commit message if needed. Save and close the editor to finalize the changes.
        
    5. **Push the changes (optional):** If you created a new branch, you can push the changes to the remote repository.
        
        ```
        git push origin new-branch-name
        
        ```
        
        If you're working on an existing branch and want to update the remote branch with your amended commit, you can use the `--force` flag to overwrite the branch history. Be cautious when using `--force` as it can affect other collaborators working on the branch.
        
        ```
        git push --force origin existing-branch-name
        
        ```
        
    
    That's it! Your changes will now be included in the existing commit.
    
    - I did not create a new branch, and after commit --amend, I got this error:
        - error
            
            $ git push
            To [https://github.com/wlg1/wlg1.github.io](https://github.com/wlg1/wlg1.github.io)
            ! [rejected]        main -> main (non-fast-forward)
            error: failed to push some refs to '[https://github.com/wlg1/wlg1.github.io](https://github.com/wlg1/wlg1.github.io)'
            hint: Updates were rejected because the tip of your current branch is behind
            hint: its remote counterpart. Integrate the remote changes (e.g.
            hint: 'git pull ...') before pushing again.
            hint: See the 'Note about fast-forwards' in 'git push --help' for details.
            
        
        The error message you received indicates that the remote branch has been updated since your last commit, and Git is rejecting your push because it would result in overwriting the remote changes. To resolve this, you can follow these steps:
        
        1. **Fetch the latest changes:** Start by fetching the latest changes from the remote repository. This will update your local copy of the remote branch without merging anything.
            
            ```
            git fetch origin
            
            ```
            
        2. **Rebase your changes:** Once you have fetched the latest changes, you can rebase your changes on top of the updated branch. This will apply your amended commit on the latest commit from the remote branch.
            
            ```
            git rebase origin/main
            
            ```
            
            If you encounter any conflicts during the rebase process, you'll need to resolve them by editing the conflicting files manually. You can use `git status` to see which files have conflicts.
            
        3. **Push your changes:** After resolving any conflicts, you can push your changes to the remote repository.
            
            ```
            git push origin main
            
            ```
            
            If the push still fails, it may be necessary to force the push. However, be cautious when using `--force` as it can overwrite other collaborators' changes.
            
            ```
            git push --force origin main
            
            ```
            
        
        Please note that using `--force` can cause data loss if you're not careful. It's essential to communicate with your team members and ensure that no one else has made important changes that could be overwritten by forcing the push.
        
- (main|REBASE 1/1)
    
    It seems like you're currently in the middle of a rebase operation. When you see the `(main|REBASE 1/1)` status in your Git command prompt, it indicates that you're rebasing your changes on top of the latest commit from the `main` branch.
    
    To proceed with the rebase or resolve any conflicts, follow these steps:
    
    1. **Resolve conflicts:** If Git encounters conflicts during the rebase process, you need to resolve them manually. Open the files with conflicts, locate the conflict markers (`<<<<<<<`, `=======`, and `>>>>>>>`), and modify the code to resolve the conflicts. Once you've resolved all conflicts in a file, save the changes.
    2. **Stage the resolved changes:** After resolving conflicts in a file, you need to stage the resolved changes to continue the rebase.
        
        ```
        git add resolved-file1 resolved-file2 ...
        
        ```
        
    3. **Continue the rebase:** Once you've resolved all conflicts and staged the changes, you can continue the rebase operation.
        
        ```
        git rebase --continue
        
        ```
        
        If there are additional conflicts, Git will prompt you to resolve them and continue until the rebase is complete.
        
    4. **Push the changes:** After successfully completing the rebase, you can push your changes to the remote repository.
        
        ```
        git push origin main
        
        ```
        
        If the push still fails, you might need to force the push, as mentioned earlier. However, exercise caution when using `--force` to avoid overwriting others' work.
        
        ```
        git push --force origin main
        
        ```
        
    
    Remember to communicate with your team members to ensure you don't inadvertently overwrite their changes when using `--force`.
    

**To Answer Later**

How do we restore a local repo based on the last commit in the local repo, not from the remote repo?

Remove from staging (after add, before commit)? 

Remove from commit (before push)?