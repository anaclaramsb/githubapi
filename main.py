# This is a sample Python script.
import time
import requests
from github import Github

ACCESS_TOKEN = '764b947594a95af75b012058d71a417e5690fda0'

g = Github(ACCESS_TOKEN)

github_api = "https://api.github.com"
gh_session = requests.Session()
gh_session.auth = ("pamsnufrpe", "6444b3886a6e76b2fe406f161da11f748d62d329")
headers = {'user-agent': 'pamsnufrpe'}

def search_github(c):
    query = '+'.join(keywords) + '+in:readme+in:description'
    result = g.search_repositories(query, 'stars', 'desc')

    print(f'Found {result.totalCount} repo(s)')

    for repo in result:
        print(f'{repo.clone_url}, {repo.stargazers_count} stars')


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
                                                                                                    "797130c04f13bccb6ed63322143cb94aa7129ebe")
            time.sleep(1)
            issue_pg = gh_session.get(url=url, headers=headers)
            issue_pg_list = [dict(item, **{'repo_name': '{}'.format(repo)}) for item in issue_pg.json()]
            issue_pg_list = [dict(item, **{'owner': '{}'.format(owner)}) for item in issue_pg_list]
            issues = issues + issue_pg_list
            if 'Link' in issue_pg.headers:
                if 'rel="next"' not in issue_pg.headers['Link']:
                    next = False
            i = i + 1
        return issues


if __name__ == '__main__':
    # keywords = input('Enter keyword(s)[e.g python, flask, postgres]: ')
    # keywords = [keyword.strip() for keyword in keywords.split(',')]
    # search_github(keywords)

    url = 'https://github.com/PX4/PX4-Autopilot/'
    owner = "PX4"
    repo = "PX4-Autopilot"
    print(repo)
    print(owner)
    print(issues_of_repo_github(owner, repo, github_api))
