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


    # commits_message = df[df['commit.message'].str.contains(keywords)]
    commits_message_fix = df[(df['commit.message'].str.contains('(?::|\/|\s|^)fix(?:\s|\,|\/|:$)'))]
    commits_message_fixes = df[(df['commit.message'].str.contains('(?::|\/|\s|^)fixes(?:\s|\,|\/|:$)'))]


    result = pd.concat([commits_message_fix, commits_message_fixes], ignore_index=False)
    result = result.loc[result.astype(str).drop_duplicates().index]
    commits_message_fixed = df[(df['commit.message'].str.contains('(?::|\/|\s|^)fixed(?:\s|\,|\/|:$)'))]
    result_1 = pd.concat([result, commits_message_fixed], ignore_index=False)
    result_1 = result_1.loc[result_1.astype(str).drop_duplicates().index]
    commits_message_fixing = df[(df['commit.message'].str.contains('(?::|\/|\s|^)fixing(?:\s|\,|\/|:$)'))]
    result_2 = pd.concat([result_1, commits_message_fixing], ignore_index=False)
    result_2 = result_2.loc[result_2.astype(str).drop_duplicates().index]
    commits_message_defect = df[(df['commit.message'].str.contains('(?::|\/|\s|^)defect(?:\s|\,|\/|:$)'))]
    result_3 = pd.concat([result_2, commits_message_defect], ignore_index=False)
    result_3 = result_3.loc[result_3.astype(str).drop_duplicates().index]
    commits_message_defects = df[(df['commit.message'].str.contains('(?::|\/|\s|^)defects(?:\s|\,|\/|:$)'))]
    result_4 = pd.concat([result_3, commits_message_defects], ignore_index=False)
    result_4 = result_4.loc[result_4.astype(str).drop_duplicates().index]
    commits_message_error = df[(df['commit.message'].str.contains('(?::|\/|\s|^)error(?:\s|\,|\/|:$)'))]
    result_5 = pd.concat([result_4, commits_message_error], ignore_index=False)
    result_5 = result_5.loc[result_5.astype(str).drop_duplicates().index]
    commits_message_errors = df[(df['commit.message'].str.contains('(?::|\/|\s|^)errors(?:\s|\,|\/|:$)'))]
    result_6 = pd.concat([result_5, commits_message_errors], ignore_index=False)
    result_6 = result_6.loc[result_6.astype(str).drop_duplicates().index]
    commits_message_bug = df[(df['commit.message'].str.contains('(?::|\/|\s|^)bug(?:\s|\,|\/|:$)'))]
    result_7 = pd.concat([result_6, commits_message_bug], ignore_index=False)
    result_7 = result_7.loc[result_7.astype(str).drop_duplicates().index]
    commits_message_bug_fix = df[(df['commit.message'].str.contains('(?::|\/|\s|^)bug-fix(?:\s|\,|\/|:$)'))]
    result_8 = pd.concat([result_7, commits_message_bug_fix], ignore_index=False)
    result_8 = result_8.loc[result_8.astype(str).drop_duplicates().index]
    commits_message_bugfix = df[(df['commit.message'].str.contains('(?::|\/|\s|^)bugfix(?:\s|\,|\/|:$)'))]
    result_9 = pd.concat([result_8, commits_message_bugfix], ignore_index=False)
    result_9 = result_9.loc[result_9.astype(str).drop_duplicates().index]
    commits_message_bugs= df[(df['commit.message'].str.contains('(?::|\/|\s|^)bugs(?:\s|\,|\/|:$)'))]
    result_10 = pd.concat([result_9, commits_message_bugs], ignore_index=False)
    result_10 = result_10.loc[result_10.astype(str).drop_duplicates().index]
    commits_message_issue = df[(df['commit.message'].str.contains('(?::|\/|\s|^)issue(?:\s|\,|\/|:$)'))]
    result_11 = pd.concat([result_10, commits_message_issue], ignore_index=False)
    result_11 = result_11.loc[result_11.astype(str).drop_duplicates().index]
    commits_message_issues = df[(df['commit.message'].str.contains('(?::|\/|\s|^)issues(?:\s|\,|\/|:$)'))]
    result_12 = pd.concat([result_11, commits_message_issues], ignore_index=False)
    result_12 = result_12.loc[result_12.astype(str).drop_duplicates().index]
    commits_message_mistake = df[(df['commit.message'].str.contains('(?::|\/|\s|^)mistake(?:\s|\,|\/|:$)'))]
    result_13 = pd.concat([result_12, commits_message_mistake], ignore_index=False)
    result_13 = result_13.loc[result_13.astype(str).drop_duplicates().index]
    commits_message_mistakes = df[(df['commit.message'].str.contains('(?::|\/|\s|^)mistakes(?:\s|\,|\/|:$)'))]
    result_14 = pd.concat([result_13, commits_message_mistakes], ignore_index=False)
    result_14 = result_14.loc[result_14.astype(str).drop_duplicates().index]
    commits_message_mistaken = df[(df['commit.message'].str.contains('(?::|\/|\s|^)mistaken(?:\s|\,|\/|:$)'))]
    result_15 = pd.concat([result_14, commits_message_mistaken], ignore_index=False)
    result_15 = result_15.loc[result_15.astype(str).drop_duplicates().index]
    commits_message_incorrect = df[(df['commit.message'].str.contains('(?::|\/|\s|^)incorrect(?:\s|\,|\/|:$)'))]
    result_16 = pd.concat([result_15, commits_message_incorrect], ignore_index=False)
    result_16 = result_16.loc[result_16.astype(str).drop_duplicates().index]
    commits_message_fault = df[(df['commit.message'].str.contains('(?::|\/|\s|^)fault(?:\s|\,|\/|:$)'))]
    result_17 = pd.concat([result_16, commits_message_fault], ignore_index=False)
    result_17 = result_17.loc[result_17.astype(str).drop_duplicates().index]
    commits_message_faults = df[(df['commit.message'].str.contains('(?::|\/|\s|^)faults(?:\s|\,|\/|:$)'))]
    result_18 = pd.concat([result_17, commits_message_faults], ignore_index=False)
    result_18 = result_18.loc[result_18.astype(str).drop_duplicates().index]
    commits_message_flaws = df[(df['commit.message'].str.contains('(?::|\/|\s|^)flaws(?:\s|\,|\/|:$)'))]
    result_19 = pd.concat([result_18, commits_message_flaws], ignore_index=False)
    result_19 = result_19.loc[result_19.astype(str).drop_duplicates().index]
    commits_message_flaw = df[(df['commit.message'].str.contains('(?::|\/|\s|^)flaw(?:\s|\,|\/|:$)'))]
    result_20 = pd.concat([result_19, commits_message_flaw], ignore_index=False)
    result_20 = result_20.loc[result_20.astype(str).drop_duplicates().index]
    commits_message_failure = df[(df['commit.message'].str.contains('(?::|\/|\s|^)failure(?:\s|\,|\/|:$)'))]
    result_21 = pd.concat([result_20, commits_message_failure], ignore_index=False)
    result_21 = result_21.loc[result_21.astype(str).drop_duplicates().index]






    # studied_commits = commits_message.sample()


    print("Project Name:" + file +"   "+str(len(result_21)) + "   Total Commits: " + str(len(df.index)))
    # # print(file)
