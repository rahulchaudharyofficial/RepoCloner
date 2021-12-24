from requests import get
import json

def fetch_git_repos(uname):
    
    if uname:
        url = f"https://api.github.com/users/{uname}/repos?per_page=100"
        response = get(url)
        jres = json.loads(response.text)
        with open(f"{uname}_repo.json","w") as f:
            f.writelines(json.dumps(jres))
    else:
        raise Exception("ERROR: Invalid username given")