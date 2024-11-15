# PractiesSelenium
I am going to upload my selenium practies code in this repository.

Author - Vishal Pommedi

To Run this project in your local system, please install required dependenties with "pip install -r requirements.txt" command in your system

To store all dependencies on requiremets.txt file we need to use "pip freeze > requirements.txt" command in our system.



Git commands

1. Initialize and Configure Git:

    git init
        Initializes a new Git repository in the current directory.
        Example: git init
    git config
        Configures Git settings like username and email.
        Example:
            Set username: git config --global user.name "Your Name"
            Set email: git config --global user.email "you@example.com"

2. Cloning Repositories:

    git clone
        Creates a copy of a remote repository.
        Example:
        git clone <repository-url>
            git clone https://github.com/username/repo.git

3. Check Repository Status:

    git status
        Shows the status of the working directory and staged files.
        Example: git status

4. Adding Files to Staging:

    git add
        Stages changes (new, modified, or deleted files) to be committed.
        Example:
            Add a specific file: git add <filename>
            Add all files: git add .

5. Committing Changes:

    git commit
        Records the staged changes in the local repository.
        Example:
        git commit -m "Your commit message"

6. Branching and Merging:

    git branch
        Lists branches, creates new branches, or deletes branches.
        Example:
            List branches: git branch
            Create a branch: git branch <branch-name>

    git checkout
        Switches to a branch or commit.
        Example:
            Switch branch: git checkout <branch-name>
            Create and switch to a new branch: git checkout -b <branch-name>

    git merge
        Merges changes from one branch into another.
        Example:
        git merge <branch>

7. Pushing and Pulling from Remote:

    git push
        Pushes local changes to the remote repository.
        Example:
        git push origin <branch-name>

    git pull
        Fetches and merges changes from the remote repository to your local branch.
        Example:
        git pull

8. Viewing Commit History:

    git log
        Shows commit history.
        Example:
            Full log: git log
            Oneline log: git log --oneline

9. Working with Remote Repositories:

    git remote
        Manages the remote repository configurations.
        Example:
            Show remote URLs: git remote -v
            Add a remote: git remote add origin <url>

10. Handling Conflicts:

    git mergetool
        Launches an external merge tool to resolve conflicts.
        Example: git mergetool

11. Undoing Changes:

    git reset
        Resets the current HEAD to a specified state.
        Example:
            Soft reset (keep changes): git reset --soft <commit>
            Hard reset (discard changes): git reset --hard <commit>

    git revert
        Creates a new commit that undoes changes from a previous commit.
        Example: git revert <commit>

12. Tagging:

    git tag
        Adds a lightweight or annotated tag to a commit.
        Example:
            Create a tag: git tag <tag-name>
            Push a tag: git push origin <tag-name>

13. Stashing:

    git stash
        Temporarily saves changes that are not ready to be committed.
        Example:
        git stash

    git stash pop
        Restores stashed changes.
        Example:
        git stash pop

14. Deleting Branches:

    git branch -d
        Deletes a local branch.
        Example:
        git branch -d <branch-name>

    git push origin --delete <branch>
        Deletes a remote branch.
        Example:
        git push origin --delete <branch-name>

Usage Breakdown:

Each Git command typically follows this format:

    git is the command-line interface.
    <command> is the specific Git command (e.g., commit, add, status).
    [options] are additional parameters you can add (e.g., -m for a commit message).
    <arguments> are the specific files, branches, or URLs that you act upon.

This structure helps you efficiently interact with Git for

version control.
