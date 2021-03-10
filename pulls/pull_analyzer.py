import json

import numpy as np
import pandas as pd

# df = pd.read_json('/Users/belize/projetos_github/AnaDrones/githubapi/ardupilot.json')



def titleFilter(df):
    pull_title_fix = df[(df['title'].str.contains('(?::|\/|\s|^)fix(?:\s|\,|\/|:$)'))]
    pull_title_fixes = df[(df['title'].str.contains('(?::|\/|\s|^)fixes(?:\s|\,|\/|:$)'))]
    result = pd.concat([pull_title_fix, pull_title_fixes], ignore_index=False)
    result = result.loc[result.astype(str).drop_duplicates().index]
    pull_title_fixed = df[(df['title'].str.contains('(?::|\/|\s|^)fixed(?:\s|\,|\/|:$)'))]
    result_1 = pd.concat([result, pull_title_fixed], ignore_index=False)
    result_1 = result_1.loc[result_1.astype(str).drop_duplicates().index]
    pull_title_fixing = df[(df['title'].str.contains('(?::|\/|\s|^)fixing(?:\s|\,|\/|:$)'))]
    result_2 = pd.concat([result_1, pull_title_fixing], ignore_index=False)
    result_2 = result_2.loc[result_2.astype(str).drop_duplicates().index]
    pull_title_defect = df[(df['title'].str.contains('(?::|\/|\s|^)defect(?:\s|\,|\/|:$)'))]
    result_3 = pd.concat([result_2, pull_title_defect], ignore_index=False)
    result_3 = result_3.loc[result_3.astype(str).drop_duplicates().index]
    pull_title_defects = df[(df['title'].str.contains('(?::|\/|\s|^)defects(?:\s|\,|\/|:$)'))]
    result_4 = pd.concat([result_3, pull_title_defects], ignore_index=False)
    result_4 = result_4.loc[result_4.astype(str).drop_duplicates().index]
    pull_title_error = df[(df['title'].str.contains('(?::|\/|\s|^)error(?:\s|\,|\/|:$)'))]
    result_5 = pd.concat([result_4, pull_title_error], ignore_index=False)
    result_5 = result_5.loc[result_5.astype(str).drop_duplicates().index]
    pull_title_errors = df[(df['title'].str.contains('(?::|\/|\s|^)errors(?:\s|\,|\/|:$)'))]
    result_6 = pd.concat([result_5, pull_title_errors], ignore_index=False)
    result_6 = result_6.loc[result_6.astype(str).drop_duplicates().index]
    pull_title_bug = df[(df['title'].str.contains('(?::|\/|\s|^)bug(?:\s|\,|\/|:$)'))]
    result_7 = pd.concat([result_6, pull_title_bug], ignore_index=False)
    result_7 = result_7.loc[result_7.astype(str).drop_duplicates().index]
    pull_title_bug_fix = df[(df['title'].str.contains('(?::|\/|\s|^)bug-fix(?:\s|\,|\/|:$)'))]
    result_8 = pd.concat([result_7, pull_title_bug_fix], ignore_index=False)
    result_8 = result_8.loc[result_8.astype(str).drop_duplicates().index]
    pull_title_bugfix = df[(df['title'].str.contains('(?::|\/|\s|^)bugfix(?:\s|\,|\/|:$)'))]
    result_9 = pd.concat([result_8, pull_title_bugfix], ignore_index=False)
    result_9 = result_9.loc[result_9.astype(str).drop_duplicates().index]
    pull_title_bugs = df[(df['title'].str.contains('(?::|\/|\s|^)bugs(?:\s|\,|\/|:$)'))]
    result_10 = pd.concat([result_9, pull_title_bugs], ignore_index=False)
    result_10 = result_10.loc[result_10.astype(str).drop_duplicates().index]
    pull_title_issue = df[(df['title'].str.contains('(?::|\/|\s|^)issue(?:\s|\,|\/|:$)'))]
    result_11 = pd.concat([result_10, pull_title_issue], ignore_index=False)
    result_11 = result_11.loc[result_11.astype(str).drop_duplicates().index]
    pull_title_issues = df[(df['title'].str.contains('(?::|\/|\s|^)issues(?:\s|\,|\/|:$)'))]
    result_12 = pd.concat([result_11, pull_title_issues], ignore_index=False)
    result_12 = result_12.loc[result_12.astype(str).drop_duplicates().index]
    pull_title_mistake = df[(df['title'].str.contains('(?::|\/|\s|^)mistake(?:\s|\,|\/|:$)'))]
    result_13 = pd.concat([result_12, pull_title_mistake], ignore_index=False)
    result_13 = result_13.loc[result_13.astype(str).drop_duplicates().index]
    pull_title_mistakes = df[(df['title'].str.contains('(?::|\/|\s|^)mistakes(?:\s|\,|\/|:$)'))]
    result_14 = pd.concat([result_13, pull_title_mistakes], ignore_index=False)
    result_14 = result_14.loc[result_14.astype(str).drop_duplicates().index]
    pull_title_mistaken = df[(df['title'].str.contains('(?::|\/|\s|^)mistaken(?:\s|\,|\/|:$)'))]
    result_15 = pd.concat([result_14, pull_title_mistaken], ignore_index=False)
    result_15 = result_15.loc[result_15.astype(str).drop_duplicates().index]
    pull_title_incorrect = df[(df['title'].str.contains('(?::|\/|\s|^)incorrect(?:\s|\,|\/|:$)'))]
    result_16 = pd.concat([result_15, pull_title_incorrect], ignore_index=False)
    result_16 = result_16.loc[result_16.astype(str).drop_duplicates().index]
    pull_title_fault = df[(df['title'].str.contains('(?::|\/|\s|^)fault(?:\s|\,|\/|:$)'))]
    result_17 = pd.concat([result_16, pull_title_fault], ignore_index=False)
    result_17 = result_17.loc[result_17.astype(str).drop_duplicates().index]
    pull_title_faults = df[(df['title'].str.contains('(?::|\/|\s|^)faults(?:\s|\,|\/|:$)'))]
    result_18 = pd.concat([result_17, pull_title_faults], ignore_index=False)
    result_18 = result_18.loc[result_18.astype(str).drop_duplicates().index]
    pull_title_flaws = df[(df['title'].str.contains('(?::|\/|\s|^)flaws(?:\s|\,|\/|:$)'))]
    result_19 = pd.concat([result_18, pull_title_flaws], ignore_index=False)
    result_19 = result_19.loc[result_19.astype(str).drop_duplicates().index]
    pull_title_flaw = df[(df['title'].str.contains('(?::|\/|\s|^)flaw(?:\s|\,|\/|:$)'))]
    result_20 = pd.concat([result_19, pull_title_flaw], ignore_index=False)
    result_20 = result_20.loc[result_20.astype(str).drop_duplicates().index]
    pull_title_failure = df[(df['title'].str.contains('(?::|\/|\s|^)failure(?:\s|\,|\/|:$)'))]
    result_21 = pd.concat([result_20, pull_title_failure], ignore_index=False)
    result_21 = result_21.loc[result_21.astype(str).drop_duplicates().index]
    return result_21


def tagFilter(df):
    result = []
    tags = []
    cont = 0
    for index, row in df.iterrows():
        # print(row['labels'])
        if len(row['labels']) > 0:
            for tag in row['labels']:
                # print(tag['name'])
                if str(tag['name']).lower() in ['fix','fixes','fixed','fixing','defect','defects','error','errors',
                                   'bug','bug-fix','bugfix','bugs','issue','issues','mistake','mistakes',
                                   'mistaken', 'incorrect','incorrect','fault','faults','flaws','flaw','failure']:
                    # print(index)
                    # rowIndex = df.index[int(index)]
                    # df.loc[rowIndex, 'Tag'] = True
                    tags.append(True)
                    break
                else:
                    tags.append(False)
            if True in tags:
                # result.append(True)
                # print(cont)
                # print(1)
                rowIndex = df.index[cont]
                df.loc[rowIndex, 'Tag'] = True
        else:
            # result.append(False)
            rowIndex = df.index[cont]
            df.loc[rowIndex, 'Tag'] = False
        cont = cont +1

    # se = pd.Series(result)
    # df['Tag'] = se.values
    return df



files = [
         '../pulls/ardupilot.json',
        '../pulls/PX4-Autopilot.json',
         '../pulls/inav.json',
         '../pulls/paparazzi.json',
         ]

for file in files:
    with open(file) as json_file:
        data = json.load(json_file)

    data_dict = json.loads(data)
    df = pd.DataFrame.from_dict(data_dict, orient='columns')


    filtered_titles = titleFilter(df.loc[df['Merged'] == True])
    filtered_tags = tagFilter(df.loc[df['Merged'] == True])
    filtered_tags = filtered_tags.loc[filtered_tags['Tag'] == True]

    # print(filtered_tags.head().to_string())

    result = pd.concat([filtered_titles, filtered_tags], ignore_index=False)
    final_result = result.loc[result.astype(str).drop_duplicates().index]


    # print(df.head().to_string())

    # if 'ardupilot' in file:
    #     result_sample = result_21.sample(190)
    #     pd.set_option('display.max_colwidth', 1000)
    #     print(result_sample['html_url'].to_string(index=False, header=False))
    # if 'PX4' in file:
    #     result_sample = result_21.sample(105)
    #     pd.set_option('display.max_colwidth', 1000)
    #     print(result_sample['html_url'].to_string(index=False, header=False))
    # if 'inav' in file:
    #     result_sample = result_21.sample(22)
    #     pd.set_option('display.max_colwidth', 1000)
    #     print(result_sample['html_url'].to_string(index=False, header=False))
    # if 'paparazzi' in file:
    #     result_sample = result_21.sample(59)
    #     pd.set_option('display.max_colwidth', 1000)
    #     print(result_sample['html_url'].to_string(index=False, header=False))

    print("Project Name:" + file + "  to analyze:  " + str(len(final_result.loc[final_result['Merged'] == True])) +"   Merged:   "  + str(len(df.loc[df['Merged'] == True])) + "   Tags:   "  + str(len(final_result.loc[final_result['Tag'] == True])) +"   Total pulls: " + str(len(df.index)))
