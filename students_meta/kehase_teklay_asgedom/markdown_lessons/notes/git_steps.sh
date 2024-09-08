1.  check status `git status`
2.  sync  `git pull`
3.  swich branch to main `git checkout main`
4.  sync `git pull`
5.  switch branch to previous  brach or desiered branch
        1.  `git checkout <name of branch>`
        2.  `git checkout -`
6.  finally merge main to desiered branch  `git merge main`
   
7. if editor is main close or delet git bash terminal and abort the merge process
   `git merge --abort`
8. set vscode as git default editor globally 
        `git config --global core.editor "code --wait"`
9. restart the merge process `git merge main`

Every days Task before begin

1. do not directly do changes in  main branch
2. always check status of your repo or project with git status
3. always make sure to sync and merge your local branch with remote branches
   1. git pull in your current branch
   2. git checkout main switch to main branch
   3. git pull to sync main branch
   4. git checkout <your desired branch > or git checkout  -
   5. git merge main