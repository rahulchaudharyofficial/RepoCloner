# RepoCloner

This command line tool let you clone all public repositories from given username. This tool also save cache as json for all repositories and in next run it lets you choose if
intend to fetch new cache or use existing stored in local to speed up.
if you think there has been a change in repositoes then chose no to use cache when prompt show up.

## Setup instruction
  1. If you are using virtualenv or python
     install dependency using following command
     pip install -r requirements.txt
   2. Once dependencies are installed successfully then execute main with command line argument as username
      i.e.
      python main.py rahulchaudharyofficial
