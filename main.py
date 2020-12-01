# This is a sample Python script.
import time
import requests
import pandas as pd

ACCESS_TOKEN = 'YOUR TOKEN HERE'

github_api = "https://api.github.com"
gh_session = requests.Session()
gh_session.auth = ("pamsnufrpe", ACCESS_TOKEN)
headers = {'user-agent': 'pamsnufrpe'}


def issues_of_repo_github(owner, repo, api):
        issues = []
        next = True
        i = 1
        total_requests = 0
        while next == True:
            total_requests = total_requests + 1
            if total_requests > 4500:
                time.sleep(60 * 60)
                print("Sleeping...")
                total_requests = 0
            url = api + '/repos/{}/{}/issues?state=all&page={}&per_page=100&access_token={}'.format(owner, repo, i,
                                                                                                ACCESS_TOKEN)
            time.sleep(1)
            issue_pg = gh_session.get(url=url, headers=headers)
            issue_pg_list = [dict(item, **{'repo_name': '{}'.format(repo)}) for item in issue_pg.json()]
            issue_pg_list = [dict(item, **{'owner': '{}'.format(owner)}) for item in issue_pg_list]
            issues = issues + issue_pg_list
            print(url)
            if 'Link' in issue_pg.headers:
                if 'rel="next"' not in issue_pg.headers['Link']:
                    next = False
            i = i + 1
        return issues


if __name__ == '__main__':
    url = 'https://github.com/ArduPilot/ardupilot'
    owner = "ArduPilot"
    repo = "ardupilot"
    issues = issues_of_repo_github(owner, repo, github_api)
    dfItem = pd.DataFrame.from_records(issues)
    dfItem.to_csv('ardupilot.csv')

 #passa um dataframe do panda
 #salvar json o resultado do arquivo
 #filtrar json por label e titulo