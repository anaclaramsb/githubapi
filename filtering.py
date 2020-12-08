import json

import pandas as pd

# df = pd.read_json('/Users/belize/projetos_github/AnaDrones/githubapi/ardupilot.json')


with open('/Users/belize/projetos_github/AnaDrones/githubapi/ardupilot.json') as json_file:
    data = json.load(json_file)
data_dict = json.loads(data)
df = pd.DataFrame.from_dict(data_dict, orient='columns')

keywords = ['fix', 'defect', 'error', 'bug', 'issue', 'mistake', 'incorrect', 'fault' , 'flaw']
issues_title =[]
issues_labels =[]

for index, row in df.iterrows():
    for item in keywords:
        if str(item).lower() in row['title']:
            issues_title.append(row['url'])


for index, row in df.iterrows():
    for item in keywords:
        if len(row['labels']) > 0:
            for item2 in row['labels']:
                for key in keywords:
                    if key in str(item2['name']).lower():
                        issues_labels.append(item2['url'])


# print (issues)
issues_title = list(dict.fromkeys(issues_title))
issues_labels = list(dict.fromkeys(issues_labels))
print (len(issues_title))
print (len(issues_labels))