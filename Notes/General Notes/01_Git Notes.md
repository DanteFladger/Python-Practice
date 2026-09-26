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
        - "m" : Sets the commit message
    5. git push -u origin main
        - Sends the commit to the remote repository 
        - "-u" = "--set_upstream" : Remembers that your local "main" branch correspons to origin/main. 
        - "origin" : Target path for push
        - "main" : The target branch

## Push from local machine to repo
    1. git status
        - Checks the current Git repository
    2. git add "path to local resource"
        - Stages all changes for the next commit
        - "." : Includes everything in the current folder
    3. git commit -m "Note"
        - Adds the desciption of what changed 
    4. git push
        - Sends the commit to the remote repository 

## Creating the virtual environemt 
    1. *Confirm you are in the root directory of your project*
    2. python3 -m venv .venv
        - Creates the virtual environment
        - "-m venv" : runs the module names venv.
        - ".venv" : the name of the folder being created 
    3. ls .venv || cat .venv/pyvenv.cfg 
        - Looks inside
        - "cat" : prints the file's contents to the terminal 
    4. source .venv/bin/activate
        - Activates it
        - Running the script normally would start a seperate child process, make changes there, and then exit, so your terminal would be unchanged
            What's being done?
                a. Put's .venv/bin at the front of your PATH, this way typing python or pip finds the .venv version first
                b. Sets the environment variable "VIRTUAL_ENV"
                c. Adds (.venv) to your prompt so you can see it's active
    5. which python || which pip || python --version
        - Vailidate vertualized environment 
    6. touch .gitignore | Add names of files to not include in git push
        - input names of documents that may hold sensitive information
    7. git rm --cached .DS_Store
        - stop tracking .DS_Store that has been commited 
    8. deactivate 
        - disconnects from vertial environment 


