from sys import argv
from git_processor import fetch_git_repos

def main():
    if len(argv) != 2:
        print("ERROR: command line argments not valid. (i.e. python main.py <GITUSERNAME>")
        exit(1)
    response = fetch_git_repos(argv[1])
    

if __name__ == "__main__":
    main()