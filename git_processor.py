from requests import get
from os import path
from os import remove
import json

def fetch_git_repos(uname):
    if uname:
        url = f"https://api.github.com/users/{uname}/repos?per_page=100"
        response = get(url)
        jres = json.loads(response.text)
        output_file = f"{uname}_repo.json"
        if(path.exists(output_file)):
            remove(output_file)
        with open(output_file,"w") as f:
            f.writelines(json.dumps(jres))
    else:
        raise Exception("ERROR: Invalid username given")