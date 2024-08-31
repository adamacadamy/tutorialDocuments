
# Git and GitHub Datasheet


## Index

- [Git and GitHub Datasheet](#git-and-github-datasheet)
  - [Index](#index)
  - [Introduction](#introduction)
    - [What is Git](#what-is-git)
    - [Why Git](#why-git)
    - [Features of Git](#features-of-git)
    - [What is GitHub](#what-is-github)
  - [Configuring Git for the First Time](#configuring-git-for-the-first-time)
  - [General Git Features](#general-git-features)
    - [Initializing Git](#initializing-git)
    - [Staging Files](#staging-files)
    - [Making a Commit](#making-a-commit)
    - [Status of Files and Log](#status-of-files-and-log)
  - [Git Help](#git-help)
  - [Git Branching](#git-branching)
  - [Working with GitHub](#working-with-github)
    - [Pull Branch from GitHub](#pull-branch-from-github)
    - [Push Branch to GitHub](#push-branch-to-github)
  - [Git Undo](#git-undo)
    - [Git Revert](#git-revert)
    - [Git Reset](#git-reset)
    - [Git Amend](#git-amend)

---

## Introduction

- **Git** is a version control system that helps you keep track of code changes and collaborate on code.
- **GitHub** is a platform that hosts Git repositories, allowing developers to work together from anywhere in the world. It's the largest host of source code in the world and has been owned by Microsoft since 2018.
- Over 70% of developers use Git.

### What is Git

- Git is a version control system.
- Git helps you keep track of code changes.
- Git is used to collaborate on code.

### Why Git

- Git allows developers to see the full history of the project.
- Developers can revert to earlier versions of a project.
- Git does not store a separate copy of every file in every commit but keeps track of changes made in each commit.

### Features of Git

- Modified files are those that have been changed, added, or deleted.
- You can stage modified files for committing.
- Committed files prompt Git to store a permanent snapshot.
- Git allows you to revert back to any previous commit.

### What is GitHub

- GitHub makes tools that use Git.
- GitHub allows developers to work together on projects.
- GitHub has been owned by Microsoft since 2018.

## Configuring Git for the First Time

```bash
$ git config --global user.name "<Enter your username here>"
$ git config --global user.email "<Enter your email here>"
```

## General Git Features

### Initializing Git

- Git will watch the folder you initialized and create a hidden folder to keep track of changes.

```bash
$ git init
```

### Staging Files

- **Adding files to Git repo:**

```bash
$ git add <filename with extension>
```

- **Staging all files in a folder:**

```bash
$ git add --all
$ git add -A
```

### Making a Commit

- Adding commits keep track of progress and changes.

```bash
$ git commit -m "<Enter your message here>"
```

- **Git Commit without Stage:**

```bash
$ git commit -a -m "<Enter your message here>"
```

### Status of Files and Log

- **Check the status of files:**

```bash
$ git status
```

- **File status in a more compact way:**

```bash
$ git status --short
```

- **View commit history:**

```bash
$ git log
$ git log --oneline
```

## Git Help

- **Get help with a specific command:**

```bash
$ git <command> -help
```

- **See all available options:**

```bash
$ git help --all
```

## Git Branching

- **Making a new Git branch:**

```bash
$ git branch <name of branch>
```

- **Checking all available branches:**

```bash
$ git branch
```

- **Switching to other branches:**

```bash
$ git checkout <branch name>
```

- **Making a new branch and directly switching to it:**

```bash
$ git checkout -b <branch name>
```

- **Deleting a branch:**

```bash
$ git branch -d <branch name>
```

- **Merging two branches:**

```bash
$ git merge <branch name>
```

## Working with GitHub

- **Push local repo to GitHub:**

```bash
$ git remote add origin <paste copied URL here>
$ git push --set-upstream origin master
```

- **Pushing local repo to GitHub after initial push:**

```bash
$ git push origin
```

- **Pull local repo from GitHub:**

```bash
$ git pull origin
```

### Pull Branch from GitHub

- **Viewing local and remote branches:**

```bash
$ git branch -a
```

- **View only remote branches:**

```bash
$ git branch -r
```

- **Pull the branch from GitHub:**

```bash
$ git checkout <branch name>
$ git pull
```

### Push Branch to GitHub

- **Create a new local branch and push to GitHub:**

```bash
$ git checkout -b <branch name>
$ git commit -a -m "<Message>"
$ git push origin <branch name>
```

## Git Undo

### Git Revert

- **Revert the latest commit:**

```bash
$ git revert HEAD --no-edit
```

- **Revert to any commit:**

```bash
$ git revert HEAD~x
```

### Git Reset

- **Reset the repository back to a previous commit:**

```bash
$ git reset <commithash>
```

### Git Amend

- **Modify the most recent commit:**

```bash
$ git commit --amend -m "<Commit Message>"
```
