# MY_Pro
# Git Commands

# Creating Projects
1. "git init" : Initialize a local Git repository
2. "git clone ssh://git@github.com/[username]/[repository-name].git " : Create a local copy of a remote repository

# Basic Snapshotting

3. "git status" : Check Status
4. "git add [file-name.txt]" : Add a file to the staging area
5. "git add -A" : Add all new and changed files to the staging area
6. "git commit -m "[commit message]"" : Commit changes
7. "git rm -r [file-name.txt]" : Remove a file (or folder)
8. "git remote -v" : View the remote repository of the currently working file or directory
9. "git branch" : List branches (the asterisk denotes the current branch)
10. "git branch" : List branches (the asterisk denotes the current branch)
11. "git branch -a" : List all branches (local and remote)
12. "git branch [branch name]" : Create a new branch
13. "git branch -d [branch name]" : Delete a branch
14. "git push origin --delete [branch name]" : Delete a remote branch
15. "git checkout -b [branch name]" : Create a new branch and switch to it
16. "git checkout -b [branch name] origin/[branch name]" : Clone a remote branch and switch to it

# Branching & Merging

17. "git branch -m [old branch name] [new branch name]" : Rename a local branch
18. "git checkout [branch name]" : Switch to a branch
19. "git checkout - " :	Switch to the branch last checked out
20. "git checkout -- [file-name.txt]" :	Discard changes to a file
21. "git merge [branch name]" : Merge a branch into the active branch
22. "git merge [source branch] [target branch]" :	Merge a branch into a target branch
23. "git stash" : Stash changes in a dirty working directory
24. "git stash clear" : Remove all stashed entries
25. "git stash pop" : Apply latest stash to working directory

# Sharing & Updating Projects
26. "git push origin [branch name]" : Push a branch to your remote repository
27. "git push -u origin [branch name]" : Push changes to remote repository (and remember the branch)
28. "git push" : Push changes to remote repository (remembered branch)
29. "git push origin --delete [branch name]" : Delete a remote branch
30. "git pull" : Update local repository to the newest commit
31. "git pull origin [branch name]" : Pull changes from remote repository
32. "git remote add origin ssh://git@github.com/[username]/[repository-name].git" : Add a remote repository
33. "git remote set-url origin ssh://git@github.com/[username]/[repository-name].git" : Set a repository's origin branch to SSH

# Inspection & Comparison

34. "git log" : View changes
35. "git log --summary" : View changes (detailed)
36. "git log --oneline" : View changes (briefly)
37. "git diff [source branch] [target branch]" : Preview changes before merging

***source == https://github.com/joshnh/Git-Commands***