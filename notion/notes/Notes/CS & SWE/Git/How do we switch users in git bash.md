# How do we switch users in git bash?

1. Open Git Bash and navigate to the repository that you want to work with.
2. Use the following command to list the current user information:

```
git config user.name

```

This will display the name of the current user.

1. Use the following command to set the new user name:

```

git config user.name "New User Name"

```

Make sure to replace "New User Name" with the actual name of the new user that you want to switch to.

1. Use the following command to set the new user email:

```

git config user.email "newuseremail@example.com"

```

Make sure to replace "**[newuseremail@example.com](mailto:newuseremail@example.com)**" with the actual email address of the new user that you want to switch to.

1. Once you have set the new user name and email, you can start making changes and commits as the new user.

Note that these user settings are specific to the local repository, and will not affect other repositories on your system or on remote servers. If you want to switch users globally across all Git repositories on your system, you can use the "--global" flag with the "git config" command, like this:

```

git config --global user.name "New Global User Name"
git config --global user.email "newglobaluseremail@example.com"

```

By following these steps, you should be able to switch users in Git Bash and start making changes and commits under the new user name and email.