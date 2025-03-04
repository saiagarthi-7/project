# Git Configuration Commands

 git config --global user.name "Your Name"
 -->Sets the username for Git commits.

 git config --global user.email "your_email@example.com"
 -->Sets the email for Git commits.

 git config --global core.editor "code --wait"
 -->Sets the default text editor for Git.

 git config --list
 -->Displays all configured Git settings.

# Git Repository Initialization & Setup

 git init
-->Initializes a new Git repository in a project directory.

 git clone <repo_url>
-->Copies a remote repository to your local machine.

# Git Staging & Committing
These commands help in tracking changes in the project.
Used when adding changes to the repository before committing them.

 git status
-->Shows the status of files (modified, staged, or untracked).

 git add <file> / git add .
-->Moves specific files (or all changes) to the staging area.

 git commit -m "commit message"
-->Saves changes to the repository with a message.

 git commit --amend
-->Modifies the last commit message or adds missed changes.

# Git Branching & Merging
These commands help in working on different features separately.
Used when developing new features, fixing bugs, or managing multiple contributors.

 git branch
-->Lists all branches in the repository.

 git branch <branch_name>
-->Creates a new branch.

 git checkout <branch_name>
-->Switches to a different branch.

 git switch <branch_name>
-->Alternative way to switch branches (newer version).

 git merge <branch_name>
-->Merges a branch into the current branch.

 git rebase <branch_name>
-->Moves commits from one branch to another base, keeping history clean.

 git branch -d <branch_name>
-->Deletes a branch after merging.

# Git Remote Repository Management
These commands help in working with remote repositories like GitHub, GitLab, etc.
Used when pushing or pulling code from a remote repository.

 git remote add origin <repo_url>
-->Links a local repository to a remote repository.

 git push origin <branch_name>
-->Pushes the current branch to the remote repository.

 git pull origin <branch_name>
-->Fetches and merges changes from the remote repository.

 git fetch
-->Retrieves new changes from the remote repository but does not merge.

 git remote -v
-->Lists remote repositories linked to the project.

# Git Log & History Commands
These commands help in checking previous commits and changes.
Used when reviewing commit history or debugging issues.

 git log
-->Shows a history of commits.

 git log --oneline
-->Displays commit history in a compact format.

 git show <commit_hash>
-->Displays detailed information about a specific commit.

 git diff
-->Shows changes between commits, branches, or the working directory.

 git blame <file>
-->Shows who last modified each line of a file.

# Git Undo & Reset Commands
These commands help in reverting changes.
Used when fixing mistakes or undoing unwanted changes.

 git reset <file>
-->Unstages a file but keeps changes.

 git reset --hard <commit_hash>
-->Resets the repository to a previous commit, discarding all changes.

 git checkout -- <file>
-->Discards changes in a specific file.

 git revert <commit_hash>
-->Creates a new commit that undoes a previous commit.

# Git Stash Commands
These commands help in saving temporary work.
Used when switching tasks but don’t want to commit yet.

 git stash
-->Temporarily saves uncommitted changes.

 git stash pop
-->Restores stashed changes.

 git stash list
-->Shows all stashed changes.

 git stash drop
-->Deletes a specific stash.

# Git Tagging Commands
These commands help in marking specific points in history.
Used when releasing versions of software.

 git tag <tag_name>
-->Creates a new tag.

 git tag -a <tag_name> -m "message"
-->Creates an annotated tag with a message.

 git push origin <tag_name>
-->Pushes a tag to the remote repository.

 git tag -d <tag_name>
-->Deletes a local tag.