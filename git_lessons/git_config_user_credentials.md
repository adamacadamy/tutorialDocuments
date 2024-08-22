
# Configuring Git User and Credentials

## Overview
When using Git, it's crucial to set up your identity (username and email) and manage credentials for authentication. This configuration ensures that your commits are properly attributed and that you can securely interact with remote repositories.

### Purpose
- **Username & Email:** These identify the author of commits in Git. Every commit is associated with a name and email, which appear in the commit history.
- **Credentials:** Credentials (username and password, personal access tokens, or SSH keys) are used to authenticate with remote repositories, ensuring that only authorized users can access them.

## Setting User Name and Email

### Global Configuration
To set your global username and email (applies to all repositories), run the following commands:

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

- **Purpose:** This information will be attached to every commit you make, making it possible to track contributions in collaborative projects.

### Local Configuration
If you want to set a different username or email for a specific repository (e.g., using a personal account for one project and a work account for another), you can configure this locally:

```bash
git config --local user.name "Your Project-Specific Name"
git config --local user.email "your.project.email@example.com"
```

- **Purpose:** This is useful when you need different identities for different repositories.

## Managing Git Credentials

### HTTPS Authentication
When using HTTPS URLs to access Git repositories (e.g., on GitHub, GitLab), you need to authenticate using your username and password (or a personal access token).

#### Credential Managers
Credential managers allow Git to store and retrieve your credentials securely, so you don’t have to re-enter them for every interaction with a remote repository. There are different credential managers depending on your operating system:

- **Git Credential Manager Core:** Cross-platform credential helper for Windows, macOS, and Linux.
- **Windows Credential Manager:** Integrated with the Windows operating system to store and manage credentials securely.
- **macOS Keychain:** Uses the built-in macOS Keychain to store Git credentials.
- **libsecret:** Credential manager for Linux distributions.

To configure Git to use a credential manager:

```bash
git config --global credential.helper manager-core
```

- **Purpose:** This command enables the Git Credential Manager Core, which securely stores credentials for future use. You’ll only need to enter your credentials once.

#### Storing Credentials in Cache
To cache credentials temporarily (e.g., for a few minutes), use the following command:

```bash
git config --global credential.helper cache
```

- **Purpose:** This will cache your credentials for a limited time (default is 15 minutes). You can adjust the cache timeout, for example:

```bash
git config --global credential.helper 'cache --timeout=3600'
```

#### Storing Credentials Permanently
You can also choose to store your credentials permanently in plaintext. While convenient, this is less secure and generally not recommended for sensitive environments:

```bash
git config --global credential.helper store
```
#### Remove or Update Credentials

If you need to remove or update your credentials, you can edit the `.git-credentials` file manually or use the following command to clear all stored credentials:

```bash
git credential-cache exit
```

If you're using `manager` or `osxkeychain`, you can remove the credentials via the respective keychain manager.

### SSH Authentication
Using SSH keys is a more secure and convenient method for authenticating with Git remotes, especially for private repositories. Once you've generated an SSH key pair and added the public key to your Git hosting service, you can configure Git to use SSH.

To ensure Git uses SSH for all operations, you can configure it like this:

```bash
git config --global core.sshCommand "ssh -T"
```

- **Purpose:** This ensures all Git operations use SSH, providing better security and avoiding repeated password prompts.

## Viewing Configurations
To see your current user name, email, and credential settings, use:

```bash
git config --global --list
```

- **Purpose:** This displays all your global settings, so you can verify what’s currently configured.

## Summary
- **User Name & Email:** Identifies you as the author of commits. Set globally for general use or locally for specific projects.
- **Credential Manager:** Stores credentials securely for HTTPS authentication, reducing the need to enter credentials repeatedly.
- **Credential Cache:** Temporarily caches credentials for a short period to avoid frequent prompts.
- **Credential Store:** Permanently stores credentials in plaintext, providing convenience but with reduced security.
- **SSH Authentication:** Uses SSH keys for secure and efficient authentication with remote repositories.

## Useful Resources
- [Git Credential Manager Documentation](https://aka.ms/gcm)
- [Git Documentation: git-config](https://git-scm.com/docs/git-config) 
- [Git Documentation: Credential Storage](https://git-scm.com/book/en/v2/Git-Tools-Credential-Storage)
- **Purpose:** This stores your credentials in a plaintext file (`~/.git-credentials`), which Git will use automatically without prompting for authentication.