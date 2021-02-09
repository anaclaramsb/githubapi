import time

import pandas
import requests
from pandas.io.json import json_normalize

github_api = "https://api.github.com"
gh_session = requests.Session()
gh_session.auth = ("pamsn", "a9aac7a15552b60618b40320d2d7261a4e232c2b")
headers = {'user-agent': 'pamsn'}


repositories = [
                'https://github.com/ArduPilot/ardupilot',
                'https://github.com/betaflight/betaflight',
                 'https://github.com/PX4/PX4-Autopilot',
                 'https://github.com/cleanflight/cleanflight',
                'https://github.com/iNavFlight/inav',
                'https://github.com/paparazzi/paparazzi']



def commits_of_repo_github(owner, repo, api):
    commits = []
    next = True
    i = 1
    global total_requests
    while next == True:
        # total_requests = total_requests + 1
        # if total_requests > 4500:
        #     time.sleep(60 * 60)
        #     print("Sleeping...")
        #     total_requests = 0
        url = api + '/repos/{}/{}/commits?page={}&per_page=100&access_token={}'.format(owner, repo, i, "a9aac7a15552b60618b40320d2d7261a4e232c2b")
        time.sleep(1)
        print(url)
        commit_pg = gh_session.get(url = url, headers = headers)
        commit_pg_list = [dict(item, **{'repo_name':'{}'.format(repo)}) for item in commit_pg.json()]
        commit_pg_list = [dict(item, **{'owner':'{}'.format(owner)}) for item in commit_pg_list]
        commits = commits + commit_pg_list
        if 'Link' in commit_pg.headers:
            if 'rel="next"' not in commit_pg.headers['Link']:
                next = False
        i = i + 1
    return commits

def create_commits_df(owner,repo, api):
    commits_list = commits_of_repo_github(owner, repo, api)
    return pandas.json_normalize(commits_list)


i = 0
for url in repositories:
    i = i+1
    owner = url.split("/")[3]
    repo = url.split("/")[4].replace(".git", "")
    df = create_commits_df(owner,repo, github_api)
    import json
    with open('commits/'+repo+'.json', 'w', encoding='utf-8') as f:
        df = df.to_json()
        json.dump(df, f, ensure_ascii=False, indent=4)
    time.sleep(300)
