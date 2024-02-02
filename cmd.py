"""
Windows Terminal Commands
aka Command line, CMD, Command Prompt, PowerShell, etc.

-----directories-----
cd <folder>         # change directory // goes to the <folder> directory // can drag&drop folder name too
cd ..               # go to previous directory
mkdir <folder>      # make directory // creates <folder>
pwd                 # print working directory - outputs path of current working directory
ls                  # shows a list of folders in current directory (without hidden files)
clear               # srcolls down & cleares command line
<tab>               # show suggested folders 

-----versions-----
python --version    # checks Python version
git -- version

code .              # opens Visual Studio to edit files


-----Git-----
See all commands on https://git-scm.com/docs
Workflow: create repo - clone - make changes - stage - commit - push/pull
Braching: checkout (switch to) the new brach before starting working on it

git config     Used to set various configurations such as user name and email

git init       Initialize Git to create a new local repository
git init -b main

git clone <repository URL>    Create a local working copy of a repository

git add          Adds one or more modified files to the staging area
git add -A       stages all changes
git add .        stages new files and modifications, without deletions
git add -u       stages modifications and deletions, without new files
git add <file>   stages a specific file
 
git commit -m "Commit message"    Commits chnages made with "git add" to the repo

git status     Lists the status of the modified files and commits

git push                                    Uploads the local commits to the remote repository
git push origin <branch>
git push --set-upstream origin <branch>     Push for newly created branches (only 1st time)

git pull                     Downloads and merges content from a remote repository to the local repository
git pull origin <branch>

git branch --all             Shows all repo branches
git branch <branch_name>     Creates a new brach named <branch name>

git checkout <branch_name>   Switching to that branch's working directory

git remote                                    Manages the set of repositories ("remotes")
git remote -v                                 Verifies the new remote URL
git remote set-url origin <new_url>           Sets new url for the remote (for example ater renaming it)


-----Example: create a new repository on the command line------
--in terminal go to your new local folder--
echo "# java" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/import-andy/java.git (your repo web address)
git push -u origin main

-----Example: push an existing repository from the command line------
git remote add origin https://github.com/import-andy/java.git (your repo web address)
git branch -M main
git push -u origin main
"""

