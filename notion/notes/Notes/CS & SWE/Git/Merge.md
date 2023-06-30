# Merge

Always create a backup of both ‘from’ and ‘to’ first. Eg) make sure can restore both by a commit.

To merge with local branch

1. Check out the branch where you want to merge changes.
    - git checkout main
2. Use the "git merge" command followed by the name of the branch you want to merge into the current branch.
    - git merge feature-branch
    
    2b. Git will attempt to merge the changes automatically, but there may be conflicts that need to be resolved manually.
    
    1. # If there are conflicts:
    git status
    # Resolve conflicts manually
    
    2c. Use a code editor or Git's built-in merge tool to resolve any conflicts.
    
    1. # Open files in a code editor to manually resolve conflicts
    # OR
    # Use Git's built-in merge tool
    git mergetool
    
    2d. Test your merged code to make sure that all features and functionality are working as expected.
    
    1. # Run any necessary tests or check for any issues manually

To push to remote branch

1. Commit the merged changes using the "git commit" command, and include a clear commit message that describes the changes you've made.
    - git commit -m "Merge changes from feature-branch into main"
2. Push the merged changes to the remote repository using the "git push" command.
    - git push origin main

https://youtu.be/Q1kHG842HoI