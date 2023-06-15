# Git

- Resource List
    
    [https://product.hubspot.com/blog/git-and-github-tutorial-for-beginners](https://product.hubspot.com/blog/git-and-github-tutorial-for-beginners)
    
    [https://www.atlassian.com/git/tutorials](https://www.atlassian.com/git/tutorials)
    
    [https://git-scm.com/docs/gittutorial](https://git-scm.com/docs/gittutorial)
    
    https://livablesoftware.com/tools-to-visualize-the-history-of-a-git-repository/#:~:text=to%20learn%20Git.-,GitUp,and%20merges%20with%20perfect%20clarity.
    
    https://git-scm.com/book/en/v2/Appendix-A%3A-Git-in-Other-Environments-Graphical-Interfaces
    

---

**Basic Workflow**

- How to create a repo on github from your local repo
    1. Log in to your GitHub account and click on the "New" button on the top right-hand side of the page. Click on "Create repository"
    2. Locally, cd to dir with files for local repo. Initialize the local repository:
        
        `git init`
        
    3. Add the remote repository URL by typing the following command in the terminal:
        
        `git remote add origin <remote repository URL>`
        
        Now you can add files to local, commit, then push to remote
        
- Update from local repo onto remote repo
    1. Add all the files to the local repository by typing the following command in the terminal:
        
        `git add .`
        
    2. Commit the changes by typing the following command in the terminal:
        
        `git commit -m "[what was changed]"`
        
    3. Push the changes to the remote repository by typing the following command in the terminal:
        
        `git push -u origin main`
        
        OR: `git push`
        
- Make branch (when adding new feature or move b/w commits)
    
    [https://www.git-tower.com/learn/git/faq/create-branch](https://www.git-tower.com/learn/git/faq/create-branch)
    
    `git branch iss53`  : Make new branch for “issue #53” 
    
    `git checkout iss53` : Switch to branch for “issue #53” 
    
    To create a new branch for “issue #53” and switch to it at the same time:
    
    `git checkout -b iss53`
    

[Merge](Git%204c9bd0a8425541b68fa7a146f2df3f37/Merge%209ebb454e688443e6884980079a13df63.md)

- Make Pull Request on Github
    
    This is to change remote main branch with changes from another branch
    
    A pull request (or PR) is a way to alert a repo's owners that you want to make some changes to their code. It allows them to review the code and make sure it looks good before putting your changes on the primary branch.
    
- git pull
    
    This is to change your local repo with updates from remote 
    
    - What does it mean "pull the changes from upstream”
        
        When you "pull the changes from upstream," it means you are retrieving the latest changes made to a repository or branch in a version control system, such as Git. The term "upstream" typically refers to the original repository or branch that you cloned or forked from. By pulling the changes from upstream, you bring those updates into your local copy, allowing you to incorporate the latest modifications made by others into your own codebase.
        
        The process of pulling involves comparing your local repository's commit history with the upstream repository's commit history. The version control system identifies the differences between the two and brings the new commits from upstream into your local repository. This operation can be done through various commands, such as `git pull` in Git.
        
        Pulling changes from upstream is particularly useful when collaborating on a project with other developers. It allows you to stay up to date with the latest code changes, bug fixes, or new features added by your team members or the project maintainers. By pulling regularly, you can avoid conflicts and ensure that your local codebase remains synchronized with the upstream repository.
        

- Workflow Diagram
    
    ![Untitled](Git%204c9bd0a8425541b68fa7a146f2df3f37/Untitled.png)
    

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
        

### Other Notes

[Remote Repo](Git%204c9bd0a8425541b68fa7a146f2df3f37/Remote%20Repo%20065557e5db3d4170bcee5b1714ad6efc.md)

[Branches](Git%204c9bd0a8425541b68fa7a146f2df3f37/Branches%20265cb6cbc5ee44b1a5aee59ea96804ac.md)

[requirements.txt](Git%204c9bd0a8425541b68fa7a146f2df3f37/requirements%20txt%204528740894b7494f933c0915795d144a.md) 

[Fork](Git%204c9bd0a8425541b68fa7a146f2df3f37/Fork%203c0dff0745b84401a39f322a2a232bb6.md)

[Staging](Git%204c9bd0a8425541b68fa7a146f2df3f37/Staging%206b42eb45b45b4ee7b8ffb818f4a7eafa.md)

- Git fetch vs pull?
    
    ![Untitled](Git%204c9bd0a8425541b68fa7a146f2df3f37/Untitled%201.png)
    
    1. `git fetch`: This command retrieves the latest changes from the remote repository, including all branches and tags, without automatically merging them into your current branch. It updates your local copy of the remote branches, allowing you to inspect and review the changes before incorporating them into your work. Fetching essentially synchronizes your local repository with the remote repository, ensuring you have the latest commits, branch updates, and tags.
    2. `git pull` merges the remote branch into your current local branch.
    - If you want to review the changes before merging them, use `git fetch`. This allows you to inspect the changes, compare branches, run tests, or make other preparations before merging.
    - If you trust the changes and want to quickly integrate them, use `git pull`. It automatically merges the changes from the remote branch into your current branch, saving you the extra step of manually performing a merge.
    - If you're working on a shared branch or collaborating with others, it's generally a good practice to use `git fetch` and review the changes before merging. This allows you to maintain control over what gets merged and resolve any conflicts that may arise.
    
    It's worth noting that both `git fetch` and `git pull` can be configured with additional options and arguments to customize their behavior. For example, you can specify the remote repository and branch to fetch or pull from.
    

How do you see the local repo, not just the working dir?

### Questions

---

[How do we switch users in git bash?](Git%204c9bd0a8425541b68fa7a146f2df3f37/How%20do%20we%20switch%20users%20in%20git%20bash%200f47e20825d648b398cc49c1afe05a9f.md)

[After cloning repo to local, how to get latest updates?](Git%204c9bd0a8425541b68fa7a146f2df3f37/After%20cloning%20repo%20to%20local,%20how%20to%20get%20latest%20upd%20200fe381701442be903a5542e9d8202d.md) 

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
    
- Make personal access token
    
    [https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
    
    settings → dev settings (bottom) 
    
- see all new commits
    
    git log
    
- see which files are unmerged at any point after a merge conflic
    
    git status
    

**To Answer Later**

How do we restore a local repo based on the last commit in the local repo, not from the remote repo?

Remove from staging (after add, before commit)? 

Remove from commit (before push)?