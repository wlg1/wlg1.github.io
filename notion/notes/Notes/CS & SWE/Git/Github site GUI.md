# Github site GUI

- if i use file upload, how do I delete files on a github repo?
    
    If you've used the file upload feature on GitHub's web interface to add files to a repository and now wish to delete them, you can do so directly through the web interface as well. Here's how:
    
    ### Deleting Files Through GitHub Web Interface
    
    1. **Navigate to the Repository**: Open the GitHub repository where the file is located.
    2. **Find the File**: Browse to the file you wish to delete within the repository.
    3. **Click on the File**: Click on the file's name to open it.
    4. **Edit or Delete**: At the top-right corner of the file view, you'll see a set of icons that allow you to perform various actions. Click on the "Trash Can" icon to delete the file.
    5. **Commit the Change**: After clicking the "Trash Can" icon, scroll down to the bottom of the page. You'll be given the option to commit the change. You can add a commit message describing why the file is being deleted. Then, click on "Commit changes" to finalize the deletion.
    6. **Create a Pull Request (Optional)**: If you are working on a fork or a branch, you may need to create a pull request to merge the changes into the main branch. This step is situational and depends on your workflow.
    
    ### Important Considerations
    
    - **History**: Deleting a file through the web interface will create a new commit that removes the file. The file's history will still be preserved in past commits.
    - **Multiple Files**: If you need to delete multiple files, it's often easier to clone the repository and delete them locally, then push the changes back to GitHub.
    - **Be Cautious**: Deleting a file removes it from the repository, so make sure you want to permanently remove it before doing so. If other people are collaborating on the project, this change will affect their copies of the repository as well.
    
    That's it! That's how you can delete a file from a GitHub repository using the web interface.