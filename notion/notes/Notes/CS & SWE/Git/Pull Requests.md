# Pull Requests

- Do you need to fork a repo to make a pull request?
    
    Yes, typically.
    
    1. Click on the "Fork" button in the top-right corner of the original page
    2. Clone the Forked Repository to a local repo and workspace.
    3. New branch, commit and push changes to your fork
        1. new branch is opt but good practice to avoid merging 
    4. Create a Pull Request:
        - Go to **your forked** repository's GitHub page (not the original)
        - Click on the "Pull requests" tab.
        - Click on the "New pull request" button.
        - Select the appropriate branches for the base repository (the original repository) and the head repository (your fork).
        - Review the changes and provide a descriptive title and comment for your pull request.
        - Click on the "Create pull request" button to submit the pull request.
    
    Please note that specific projects or organizations may have different workflows or requirements for contributing changes, so it's always recommended to refer to their contributing guidelines or documentation for the most accurate instructions.
    
- How do you accept a pull request?
    
    In the original repo, click on pull requests to display open ones created by others. Select “Merge Pull Request”
    
- Once a pull request is accepted, is a branch in your fork pushed as a new branch to the original repo, but not merge it yet with the main branch of the original repo?
    
    No, when a pull request is accepted and merged, the branch from your fork is not pushed as a new branch to the original repository. Instead, the changes from your branch are integrated directly into the main branch of the original repository, typically through a merge commit.
    
    Here's what happens when a pull request is accepted and merged:
    
    1. You create a branch in your forked repository and make changes in that branch.
    2. You submit a pull request from your branch in the forked repository to the original repository.
    3. The maintainers and contributors of the original repository review your pull request, provide feedback, and potentially request modifications.
    4. Once the pull request is approved by the maintainers, they merge your changes into the main branch of the original repository.
    5. The merge process typically creates a new merge commit in the main branch, incorporating the changes from your branch. This merge commit integrates your changes while preserving the commit history of the main branch.
    6. After the merge, your branch from the fork remains in your forked repository and is not pushed as a new branch to the original repository.
    
    In summary, the accepted pull request results in the integration of your changes into the main branch of the original repository through a merge commit. Your branch in the forked repository is not directly pushed or merged as a separate branch into the original repository. Instead, the changes are consolidated into the main branch of the original repository, providing a clear and organized commit history.
    
- Are collaborators able to make new branches in the original repo?
    
    Yes, collaborators with write access to the original repository can create new branches directly in the repository. 
    
- Why would a collaborator not just make a new branch and later merge it with the main? Why do they need to fork, make a new branch and make a pul request?
    
    This approach is suitable when collaborators have direct write access to the repository and are actively working on the project. However, there are cases where a pull request is preferred. 
    
    1. **Maintainer Review**: By forking the repository and creating a pull request, collaborators provide an opportunity for project maintainers to review their changes before merging them into the main branch. This review process ensures that the proposed changes align with the project's guidelines, coding standards, and desired functionality.
    2. **Collaboration on External Projects**: When contributing to external projects where collaborators don't have direct write access, forking the repository is necessary. Forking allows collaborators to make changes in their own forked repository, independent of the original repository, and then propose those changes via a pull request. This workflow respects the ownership and control of the original repository while enabling contributions from external contributors.
    3. **Contributor Licensing**: When contributing to open-source projects, forking and creating a pull request often involves agreeing to the project's licensing terms. Contributors typically need to sign a Contributor License Agreement (CLA) or indicate their acceptance of the project's license terms. Forking and creating a pull request streamline this process.
- Is there a way to have a branch in the forked copy be pushed to the original repo as a branch separate from main?
    
    Yes
    
    1. **Create a Branch in Your Fork**: In your forked copy, create a new branch using the `git branch` command. **Checkout the New Branch**
    2. **Add the Original Repository as a Remote**: Add the original repository as a remote to your local Git repository using the `git remote add` command.
        
        ```
        git remote add upstream <original-repo-url>
        ```
        
    3. **Push the New Branch to the Original Repository**: Push the new branch from your forked copy to the original repository using the `git push` command.
        
        ```
        git push upstream <new-branch-name>
        ```
        
    
    Now, the branch from your forked copy will be available in the original repository as a separate branch, distinct from the main branch. Other collaborators or maintainers can see and access this branch in the original repository.
    
    It's worth noting that pushing a branch to the original repository is subject to the access permissions and branch protection settings configured for the repository. Make sure you have the necessary permissions to push the branch to the original repository, or collaborate with the repository maintainers to ensure the branch is properly reviewed and integrated.
    
- Branching off another branch:
    
    [https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-branches#working-with-branches](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-branches#working-with-branches)
    
    If you delete a head branch after its pull request has been merged, GitHub checks for any open pull requests in the same repository that specify the deleted branch as their base branch. GitHub automatically updates any such pull requests, changing their base branch to the merged pull request's base branch. The following diagrams illustrate this.
    
    Here someone has created a branch called `feature1` from the `main` branch, and you've then created a branch called `feature2` from `feature1`. There are open pull requests for both branches. The arrows indicate the current base branch for each pull request. At this point, `feature1` is the base branch for `feature2`. If the pull request for `feature2` is merged now, the `feature2` branch will be merged into `feature1`.
    
    ![https://docs.github.com/assets/cb-2058/images/help/branches/pr-retargeting-diagram1.png](https://docs.github.com/assets/cb-2058/images/help/branches/pr-retargeting-diagram1.png)
    
    In the next diagram, someone has merged the pull request for `feature1` into the `main` branch, and they have deleted the `feature1` branch. As a result, GitHub has automatically retargeted the pull request for `feature2` so that its base branch is now `main`.
    
    ![https://docs.github.com/assets/cb-2581/images/help/branches/pr-retargeting-diagram2.png](https://docs.github.com/assets/cb-2581/images/help/branches/pr-retargeting-diagram2.png)
    
    Now when you merge the `feature2` pull request, it'll be merged into the `main` branch.
    

---

[https://www.youtube.com/watch?v=8lGpZkjnkt4&ab_channel=Fireship](https://www.youtube.com/watch?v=8lGpZkjnkt4&ab_channel=Fireship)