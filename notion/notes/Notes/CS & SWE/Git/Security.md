# Security

- What's a personal access token?
    
    A personal access token (PAT) is a type of authentication token that allows you to securely access resources on a remote system or service, typically through APIs or command-line tools. It serves as an alternative to using your account password for authentication.
    
    In the context of GitHub, a personal access token is a token that you can generate and use to authenticate yourself when interacting with GitHub's API or when accessing GitHub repositories using command-line tools or Git clients.
    
    1. **Scope**: When generating a personal access token, you can specify the desired scope, which determines the permissions and access rights granted to the token. You can limit the token's capabilities to only what is necessary for the intended use.
    2. **Usage**: Personal access tokens can be used instead of passwords for various operations, such as interacting with the GitHub API, pushing or pulling changes to repositories, or using command-line tools like Git on the command line.
    3. **Security**: Personal access tokens are more secure than using your account password because they can be easily revoked or limited in scope if compromised. It allows you to control and manage access to your GitHub account more effectively.
- Make personal access token
    
    [https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
    
    settings → dev settings (at bottom left) 
    
    <<<
    
    1. Go to your account settings by clicking on your profile picture in the top-right corner and selecting "Settings."
    2. In the left sidebar, click on "Developer settings."
    3. Select "Personal access tokens."
    4. Click on the "Generate new token" button.
    5. Provide a descriptive note for the token and select the desired scopes for the token.
    6. Click on the "Generate token" button.
    7. The token will be displayed on the screen. Make sure to copy and save it in a secure location, as it will not be displayed again.

<<<

How do you give permission for another user to access your private repo?

[https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-access-to-your-personal-repositories/inviting-collaborators-to-a-personal-repository](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-access-to-your-personal-repositories/inviting-collaborators-to-a-personal-repository)

Repo settings (right on top bar) → Access, Collaborators (top left) —> Add people —> They must accept your invite from their inbox by going to the repo site

Now the collaborators can acess the repo site w/o a 404, but still cannot access its settings, etc