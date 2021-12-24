'''
    Author: Rahul Chaudhary
    Email: rahulchaudharyofficial@outlook.com

'''

import json
import time
from os import system
from os import path,rename
from requests import get


def fetch_json(uname):
    output = None
    try:
        url = f"https://api.github.com/users/{uname}/repos?per_page=100"
        response = get(url)
        output = json.loads(response.text)
    except Exception as e:
        print(e)
        output = []
    return output


def fetch_git_repos(uname):
    '''
    This function takes username as input param and return public repository's information of given username. 
    '''
    if uname:
        try:
            output_file = f"{uname}_repo.json"
            fetch = True
            choice = None
            cacheAvailble = False
            if path.exists(output_file):
                cacheAvailble = True
                choice = input("Found cache for given username: use cache? (yes/no)")
                if choice.lower() == "yes" or choice.lower() == "y":
                    fetch = False
                else:
                    fetch = True
            else:
                fetch = True
                cacheAvailble = False

            if fetch:
                if cacheAvailble:
                    rename(output_file,"bak__"+str(time.time_ns().as_integer_ratio()[0])+"_"+output_file)
                jres = fetch_json(uname)
                with open(output_file,"w",encoding="utf-8") as file_descriptor:
                    file_descriptor.writelines(json.dumps(jres))
                process_repos(jres)
            else:
                with open(output_file,"r",encoding="utf-8") as file_descriptor:
                    #print(file_descriptor.read())
                    repos = json.loads(file_descriptor.read())
                    process_repos(repos)               
        except Exception as e:
            print(e)
    else:
        raise Exception("ERROR: Invalid username given")


def clone(url):
    system(f"git clone {url}")


def process_repos(repo_json):
    for repo in repo_json:
        print(repo["git_url"])