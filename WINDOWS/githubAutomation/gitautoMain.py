import subprocess
import os

# Specify the directory path you want to check


# Check if the directory exists
class Main:
    def __init__(self):
            
        while True:
            self.workingDirectory = input('your file directory :')
            if os.path.exists(self.workingDirectory):
                print(f"now in directory '{self.workingDirectory}'")
                
                break
            else:
                print(f"The directory '{self.workingDirectory}' does not exist.")
                continue


        # Specify the path to the directory you want to change to for the subprocess

        # new_directory = 'F:\programming\dart_flutter\password_saver2'

        # Specify the command you want to run

        self.git_init = "git init"
        # Initialize a new Git repository in your current directory.

        self.git_clone = "git clone <>"#repository_url
        # Clone a remote repository to your local machine.

        self.git_add = "git add <>"#file
        # Stage changes in a file to be committed.
        

        # Commit staged changes with a descriptive message.

        self.git_pull = "git pull"
    # Fetch changes from a remote repository and merge them into your local branch.

        self.git_branch = "git branch"
    # List all branches in your local repository.

        self.git_checkout = "git checkout <>"#branch_name
        # Switch to a different branch.

        self.git_merge = "git merge <>"#branch_name
        # Merge changes from one branch into the current branch

        self.git_status = "git status"
        # Show the status of your working directory, including staged and unstaged changes.

        self.git_log = "git log"
        # Display a history of commits.

        self.git_remote_v = "git remote -v"
        # List remote repositories associated with your local repository.

    
        self.git_fetch = "git fetch <>"#remote_name
        # Fetch changes from a specific remote repository.

        self.git_pull_origin = "git pull origin <>"#branch_name
        # Pull changes from a specific branch of the remote repository named "origin."

        self.git_push_remote = "git push <1> <2>"#remote_name , branch_name
        # Push changes to a specific branch of a remote repository.

        self.git_branch_d = "git branch -d <>" #branch_name
        # Delete a local branch

        self.git_remote_remove = "git remote remove <>" #remote_name
        # Remove a remote repository reference.

        self.git_stash = "git stash"
        # Temporarily save changes that are not ready to be committed.

        self.git_tag = "git tag <>" #tag_name
        # Create a tag to mark a specific commit (e.g., for releases).

    def git_commit(self):
        self.commit_text = input ("enter the commit text :")
        self.git_commit = f'git commit -m "{self.commit_text}"'#message
        return self.git_commit
    def git_push(self):
        self.mainBrunchOrAnother = input("you want to push main(enter) another(type its name) make new branch(mk_b):")
        if self.mainBrunchOrAnother == "":
            self.git_push = "git push"
        elif self.mainBrunchOrAnother == "mk_b":

                self.statue_result = self.make_acommand(self.createNewBranch())
                self.git_push = f"git push origin {self.mainBrunchOrAnother}"

        else:

            git_push = f"git push origin {self.mainBrunchOrAnother}"
        return git_push
    # Push your local changes to a remote repository.
    def createNewBranch(self):
        self.NewBranchName = input("type the new branch name ")
        return f"git checkout -b {self.NewBranchName}"





    def git_remote_add(self):
        mainBrunchOrAnother = input("you want to push main(enter) another(type its name) :")
        link = input("enter repo link :")
        if mainBrunchOrAnother == "":
            git_remote_add = "git remote add main {link}"   #name , repository_url
            # Add a remote repository with a custom name.
        else:

            git_remote_add = "git remote add {mainBrunchOrAnother} {link}"
        




    # Change the working directory for the subprocess and run the command
    def makeCommand(self,command):
        try:
            print(f"({command})")
            result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, cwd=self.workingDirectory)
        except Exception as e:
            print(e)
            result = None
        return result

    def testCommandResult(self,result):
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

    def move_To_next_or_stop(self,result,successOrfail):
    
            if successOrfail:
                print(result.stdout)

                self.continueOrbreak = input("\nseccessful response \nfor continue(enter) stop(y) retry(r) restart(n):").lower()
                print(self.continueOrbreak)

                if self.continueOrbreak == "y":
                    return 0
                elif self.continueOrbreak == "r":
                    return 3
                elif self.continueOrbreak == "n":
                    return 4
                else:
                    return 1

            else:
                try:
                    print(result.stdout)
                except:
                    print("there is no result to print")

                self.continueOrbreak = input("\nfaild response \nnext(y) \nstop(enter) retry(r) restart(n):").lower()
                if self.continueOrbreak == "y":
                    return 2 #continue any way
                elif self.continueOrbreak == "r":
                    return 3
                elif self.continueOrbreak == "n":
                    return 4
                else:
                    return 0
    def make_acommand(self,command):
        while True:
            command = command

            result = self.makeCommand(command)
            successOrfail = self.testCommandResult(result)
            moveOrStop = self.move_To_next_or_stop(result,successOrfail)
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

    def makeUpdateToTheCode(self):
        while True :

            statue_result = self.make_acommand(self.git_status)
            if statue_result :
                statue_result = self.make_acommand("git add .")
                if statue_result:
                    statue_result = self.make_acommand(self.git_commit())
                    if statue_result:
                        statue_result = self.make_acommand(self.git_push())
                    else:
                        break
                
                else:
                    break

            else:
                break

    def create_new_repo(self):

        while True :

            statue_result = self.make_acommand(self.git_init)
            if statue_result :
                statue_result = self.make_acommand("git commit -m \"first commit\"")
                if statue_result:
                    statue_result = self.make_acommand("git branch -M main")
                    if statue_result:
                        statue_result = self.make_acommand(self.git_remote_add())
                        if statue_result:
                            statue_result = self.make_acommand("git push -u origin main")
                        else:
                            break
                    else:
                        break
                
                else:
                    break

            else:
                break

    restart = 0
    def main(self):
        while True :
            whichProcessDoYouWant = input("update<enter> create<c>").lower()
            if whichProcessDoYouWant == "":
                
                self.makeUpdateToTheCode()
            elif whichProcessDoYouWant == "c":
            
                self.create_new_repo()



            
            if self.restart == 4:
                print("restarting")
                continue



if __name__ == "__main__":
    variable = Main()

    variable.main()


# Check the result

