# Git

[init from local](Git%204c9bd0a8425541b68fa7a146f2df3f37/init%20from%20local%20acd1dbb6ae904fccbace655a66957fac.md)

[local repo to remote](Git%204c9bd0a8425541b68fa7a146f2df3f37/local%20repo%20to%20remote%20e71f0d7f13a54f2eb5474f95111e9e96.md)

[Merge](Git%204c9bd0a8425541b68fa7a146f2df3f37/Merge%209ebb454e688443e6884980079a13df63.md)

[How do we switch users in git bash?](Git%204c9bd0a8425541b68fa7a146f2df3f37/How%20do%20we%20switch%20users%20in%20git%20bash%200f47e20825d648b398cc49c1afe05a9f.md)

[requirements.txt](Git%204c9bd0a8425541b68fa7a146f2df3f37/requirements%20txt%204528740894b7494f933c0915795d144a.md) 

[After cloning repo to local, how to get latest updates?](Git%204c9bd0a8425541b68fa7a146f2df3f37/After%20cloning%20repo%20to%20local,%20how%20to%20get%20latest%20upd%20200fe381701442be903a5542e9d8202d.md) 

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
        

### Misc

---

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
    

[https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)

settings → dev settings (bottom) 

How do we restore a local repo based on the last commit in the local repo, not from the remote repo?

How do we create a branch in the local repo?