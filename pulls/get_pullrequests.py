import time

import pandas
import requests
from pandas.io.json import json_normalize

github_api = "https://api.github.com"
gh_session = requests.Session()
gh_session.auth = ("pamsn", "a9aac7a15552b60618b40320d2d7261a4e232c2b")
headers = {'user-agent': 'pamsn'}


repositories = [
                # 'https://github.com/ArduPilot/ardupilot',
                # 'https://github.com/PX4/PX4-Autopilot',
                'https://github.com/iNavFlight/inav',
                'https://github.com/paparazzi/paparazzi']

def get_rate_limit(api):
    url = api + '/rate_limit'
    rate_limit_pg = gh_session.get(url=url, headers = headers)
    return int(rate_limit_pg.json()['rate']['remaining'])

def pulls_of_repo_github(owner, repo, api):
    pulls = []
    next = True
    i = 1
    # total_requests = 0
    # remaining = get_rate_limit(github_api)
    while next == True:
        # total_requests = total_requests + 1
        # if total_requests > remaining:
        #     time.sleep(60 * 60)
        #     print("Sleeping...")
        #     total_requests = 0
        url = api + '/repos/{}/{}/pulls?state=closed&page={}&per_page=100&access_token={}'.format(owner, repo, i, "a9aac7a15552b60618b40320d2d7261a4e232c2b")
        time.sleep(1)
        print(url)
        pull_pg = gh_session.get(url = url, headers = headers)
        pull_pg_list = [dict(item, **{'repo_name':'{}'.format(repo)}) for item in pull_pg.json()]
        pull_pg_list = [dict(item, **{'owner':'{}'.format(owner)}) for item in pull_pg_list]
        pulls = pulls + pull_pg_list
        # print(pull_pg.headers)
        if 'Link' in pull_pg.headers:
            # print(pull_pg.headers['Link'])
            if 'rel="next"' not in pull_pg.headers['Link']:
                next = False
        i = i + 1
    return pulls

def create_pulls_df(owner,repo, api):
    pulls_list = pulls_of_repo_github(owner, repo, api)
    return pandas.json_normalize(pulls_list )


i = 0
for url in repositories:
    i = i+1
    owner = url.split("/")[3]
    repo = url.split("/")[4].replace(".git", "")
    df = create_pulls_df(owner,repo, github_api)
    import json
    with open('/Users/pamsn/Projects/drone_project/githubapi/pulls/' + repo + '.json', 'w', encoding='utf-8') as f:
        df = df.to_json()
        json.dump(df, f, ensure_ascii=False, indent=4)
    time.sleep(300)
