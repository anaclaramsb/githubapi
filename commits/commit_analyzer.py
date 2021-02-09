import json

import pandas as pd

# df = pd.read_json('/Users/belize/projetos_github/AnaDrones/githubapi/ardupilot.json')

files = ['/Users/pamsn/Projects/drone_project/codigo_drone/commits/ardupilot.json',
         '/Users/pamsn/Projects/drone_project/codigo_drone/commits/betaflight.json',
         '/Users/pamsn/Projects/drone_project/codigo_drone/commits/PX4-Autopilot.json',
         '/Users/pamsn/Projects/drone_project/codigo_drone/commits/cleanflight.json',
         '/Users/pamsn/Projects/drone_project/codigo_drone/commits/inav.json',
         '/Users/pamsn/Projects/drone_project/codigo_drone/commits/paparazzi.json',
         ]

for file in files:
    with open(file) as json_file:
        data = json.load(json_file)

    data_dict = json.loads(data)
    df = pd.DataFrame.from_dict(data_dict, orient='columns')

    # print(df.head().to_string())

    keywords = ['fix', 'defect', 'error', 'bug', 'issue', 'mistake', 'incorrect', 'fault', 'flaw']
    commits_message =[]

    # is_closed = df.loc[df['state'] == 'closed']

    # commits = df[df['commit.message'].str.contains('fix|defect|error|bug|issue|mistake|incorrect|fault|flaw')]
    commits = df[df['commit.message'].str.contains('fix')]
    print("Project Name:" + file +"   "+str(len(commits)) + "   Total Commits: " + str(len(df.index)))
