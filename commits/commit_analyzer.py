import json

import pandas as pd

# df = pd.read_json('/Users/belize/projetos_github/AnaDrones/githubapi/ardupilot.json')

files = ['../commits/ardupilot.json',
         '../commits/PX4-Autopilot.json',
         '../commits/inav.json',
         '../commits/paparazzi.json',
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


    commits_message = df[df['commit.message'].str.contains('(?::|\/|\s|^)fix(?:\s|\,|\/|:$)|'
                                                           '(?::|\/|\s|^)fixes(?:\s|\,|\/|:$)|'
                                                           '(?::|\/|\s|^)fixed(?:\s|\,|\/|:$)|'
                                                           '(?::|\/|\s|^)fixing(?:\s|\,|\/|:$)|'
                                                           '(?::|\/|\s|^)defect(?:\s|\,|\/|:$)|'
                                                           '(?::|\/|\s|^)defects(?:\s|\,|\/|:$)|'
                                                           '(?::|\/|\s|^)error(?:\s|\,|\/|:$)|'
                                                           '(?::|\/|\s|^)errors(?:\s|\,|\/|:$)|'
                                                           '(?::|\/|\s|^)bug(?:\s|\,|\/|:$)|'
                                                           '(?::|\/|\s|^)bug-fix(?:\s|\,|\/|:$)|'
                                                           '(?::|\/|\s|^)bugfix(?:\s|\,|\/|:$)|'
                                                           '(?::|\/|\s|^)bugs(?:\s|\,|\/|:$)|'
                                                           '(?::|\/|\s|^)issue(?:\s|\,|\/|:$)|'
                                                           '(?::|\/|\s|^)issues(?:\s|\,|\/|:$)|'
                                                           '(?::|\/|\s|^)mistake(?:\s|\,|\/|:$)|'
                                                           '(?::|\/|\s|^)mistakes(?:\s|\,|\/|:$)|'
                                                           '(?::|\/|\s|^)mistaken(?:\s|\,|\/|:$)|'
                                                           '(?::|\/|\s|^)incorrect(?:\s|\,|\/|:$)|'
                                                           '(?::|\/|\s|^)fault(?:\s|\,|\/|:$)|'
                                                           '(?::|\/|\s|^)faults(?:\s|\,|\/|:$)|'
                                                           '(?::|\/|\s|^)flaws(?:\s|\,|\/|:$)|'
                                                           '(?::|\/|\s|^)flaw(?:\s|\,|\/|:$)|'
                                                           '', regex = True)]


    # # commits = df[df['commit.message'].str.contains('fix')]
    # if 'https://github.com/PX4/PX4-Autopilot/commit/540e4f9464f4aeaa14accc88715be5c870c4081e' in commits_message.values:
    #     print ('ok')

    print("Project Name:" + file +"   "+str(len(commits_message)) + "   Total Commits: " + str(len(df.index)))
    # print(file)
    # print(commits_message.head().to_string())