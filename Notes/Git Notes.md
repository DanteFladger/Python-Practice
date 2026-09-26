# Git Commands Sets
## Setting up Github connection 
    1. cd "pathtodestination"
    2. git init
    3. gh repo create "Repo Name" --[public/private] --source= "local resource path" --remote="Connection Name"
        - [public/private]: determins view state of repo
        - source: points to the local resource you want to connect
        - remote: connects your local Git repo to the new GitHub repository and gives the connection a name
    4. git commit -m "Note"
        - Adds the desciption of what changed 
        - "m" | Sets the commit message
    5. git push -u origin main
        - Sends the commit to the remote repository 
        - "-u" = "--set_upstream" | Remembers that your local "main" branch correspons to origin/main. 
        - "origin" | Target path for push
        - "main" | the target branch
## Push from local machine to repo
    1. git status
        - Checks the current Git repository
    2. git add "path to local resource"
        - Stages all changes for the next commit
        - "." | Includes everything in the current folder
    3. git commit -m "Note"
        - Adds the desciption of what changed 
    4. git push
        - Sends the commit to the remote repository 