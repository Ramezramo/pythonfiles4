import subprocess
import os

# Specify the directory path you want to check
new_directory = input('your file directory :')

# Check if the directory exists
if os.path.exists(new_directory):
    print(f"The directory '{new_directory}' exists.")
else:
    print(f"The directory '{new_directory}' does not exist.")


# Specify the path to the directory you want to change to for the subprocess

# new_directory = 'F:\programming\dart_flutter\password_saver2'

# Specify the command you want to run

git_init = "git init"
# Initialize a new Git repository in your current directory.

git_clone = "git clone <>"#repository_url
# Clone a remote repository to your local machine.

git_add = "git add <>"#file
# Stage changes in a file to be committed.
def git_commit():
    commit_text = input ("enter the commit text :")
    git_commit = f'git commit -m "{commit_text}"'#message
    return git_commit

# Commit staged changes with a descriptive message.

git_pull = "git pull"
# Fetch changes from a remote repository and merge them into your local branch.
def git_push():
    mainBrunchOrAnother = input("you want to push main(enter) another(type its name) :")
    if mainBrunchOrAnother == "":
        git_push = "git push"
    else:

        git_push = f"git push origin {mainBrunchOrAnother}"
    return git_push
# Push your local changes to a remote repository.

git_branch = "git branch"
# List all branches in your local repository.

git_checkout = "git checkout <>"#branch_name
# Switch to a different branch.

git_merge = "git merge <>"#branch_name
# Merge changes from one branch into the current branch

git_status = "git status"
# Show the status of your working directory, including staged and unstaged changes.

git_log = "git log"
# Display a history of commits.

git_remote_v = "git remote -v"
# List remote repositories associated with your local repository.

git_remote_add = "git remote add <1> <2>"#name , repository_url
# Add a remote repository with a custom name.

git_fetch = "git fetch <>"#remote_name
# Fetch changes from a specific remote repository.

git_pull_origin = "git pull origin <>"#branch_name
# Pull changes from a specific branch of the remote repository named "origin."

git_push_remote = "git push <1> <2>"#remote_name , branch_name
# Push changes to a specific branch of a remote repository.

git_branch_d = "git branch -d <>" #branch_name
# Delete a local branch

git_remote_remove = "git remote remove <>" #remote_name
# Remove a remote repository reference.

git_stash = "git stash"
# Temporarily save changes that are not ready to be committed.

git_tag = "git tag <>" #tag_name
# Create a tag to mark a specific commit (e.g., for releases).

# Change the working directory for the subprocess and run the command
def makeCommand(command):
    try:
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, cwd=new_directory)
    except Exception as e:
        print(e)
        result = None
    return result

def testCommandResult(result):
    try:
        if result.returncode == 0:
            print("Command executed successfully")
            print("Output:")
            print(result.stdout)
            return True

        else:
            print("Command failed")
            print("Error:")
            print(result.stderr)
            return False
    except Exception as e:
        print(e)
        return False

def move_To_next_or_stop(result,successOrfail):
   
        if successOrfail:
            print(result.stdout)

            continueOrbreak = input("\nseccessful response \nfor continue(enter) stop(y) retry(r) restart(n):").lower()
            print(continueOrbreak)

            if continueOrbreak == "y":
                return 0
            elif continueOrbreak == "r":
                return 3
            elif continueOrbreak == "n":
                return 4
            else:
                return 1

        else:
            try:
                print(result.stdout)
            except:
                print("there is no result to print")

            continueOrbreak = input("\nfaild response \nnext(y) \nstop(enter) retry(r) restart(n):").lower()
            if continueOrbreak == "y":
                return 2 #continue any way
            elif continueOrbreak == "r":
                return 3
            elif continueOrbreak == "n":
                return 4
            else:
                return 0
def make_acommand(command):
    while True:
        command = command

        result = makeCommand(command)
        successOrfail = testCommandResult(result)
        moveOrStop = move_To_next_or_stop(result,successOrfail)
        print(f'result is equal {moveOrStop}')
        if moveOrStop == 1 or moveOrStop == 2:
            return True
        
        
        elif moveOrStop == 3:
            print(f'result is equal {moveOrStop}')
            continue
        elif moveOrStop == 4:
            restart = 4
            break
        else:
            return False

def makeUpdateToTheCode():
    while True :

        statue_result = make_acommand(git_status)
        if statue_result :
            statue_result = make_acommand("git add .")
            if statue_result:
                statue_result = make_acommand(git_commit())
                if statue_result:
                    statue_result = make_acommand(git_push())
                else:
                    break
            
            else:
                break

        else:
            break




restart = 0
def main():
    while True :

        makeUpdateToTheCode()
        if restart == 4:
            print("restarting")
            continue



if __name__ == "__main__":
    input("press any button")
    main()


# Check the result

