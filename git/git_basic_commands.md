
# Git Basic Commands

## Git Configuration
### Set your name and email for Git commits:
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### Check your Git configuration:
```bash
git config --list
```

## Starting a Git Repository
### Initialize a new Git repository:
```bash
git init
```

### Clone an existing repository:
```bash
git clone <repository_url>
```

## Staging and Committing Changes
### Check the status of your working directory:
```bash
git status
```

### Add a file to the staging area:
```bash
git add <file_name>
```

### Add all files to the staging area:
```bash
git add .
```

### Commit changes with a message:
```bash
git commit -m "Your commit message"
```

### Commit all staged changes:
```bash
git commit
```

## Branching and Merging
### Create a new branch:
```bash
git branch <branch_name>
```

### List all branches:
```bash
git branch
```

### Switch to a branch:
```bash
git checkout <branch_name>
```

### Create and switch to a new branch:
```bash
git checkout -b <branch_name>
```

### Merge a branch into the current branch:
```bash
git merge <branch_name>
```

### Delete a branch:
```bash
git branch -d <branch_name>
```

## Pushing and Pulling Changes
### Push changes to the remote repository:
```bash
git push origin <branch_name>
```

### Pull changes from the remote repository:
```bash
git pull
```

### Fetch updates from the remote repository without merging:
```bash
git fetch
```

## Viewing History
### View the commit history:
```bash
git log
```

### View a concise log (one line per commit):
```bash
git log --oneline
```

### View a specific file's history:
```bash
git log <file_name>
```

## Undoing Changes
### Unstage a file:
```bash
git reset <file_name>
```

### Undo changes in a file (revert to the last commit):
```bash
git checkout -- <file_name>
```

### Revert to a previous commit (does not delete commit history):
```bash
git revert <commit_hash>
```

### Reset to a previous commit (deletes commit history after this point):
```bash
git reset --hard <commit_hash>
```

## Working with Remotes
### Add a remote repository:
```bash
git remote add origin <repository_url>
```

### List remote repositories:
```bash
git remote -v
```

### Remove a remote repository:
```bash
git remote remove <remote_name>
```

## Tagging
### Create a tag:
```bash
git tag <tag_name>
```

### List all tags:
```bash
git tag
```

### Push a tag to the remote repository:
```bash
git push origin <tag_name>
```

### Delete a local tag:
```bash
git tag -d <tag_name>
```

## Miscellaneous
### Show the differences between commits:
```bash
git diff
```

### Stash your changes (temporarily save them):
```bash
git stash
```

### Apply stashed changes:
```bash
git stash apply
```

### Delete all stashed changes:
```bash
git stash clear
```

## References
- [Git Documentation](https://git-scm.com/doc)
