import json

import numpy as np
import pandas as pd
import re
# df = pd.read_json('/Users/belize/projetos_github/AnaDrones/githubapi/ardupilot.json')
import warnings
from pandas.core.common import SettingWithCopyWarning

warnings.simplefilter(action="ignore", category=SettingWithCopyWarning)

pattern0 = re.compile("(?::|\/|\s|^)fix(?:\s|\,|\/|:$)")
pattern1 = re.compile("(?::|\/|\s|^)fixes(?:\s|\,|\/|:$)")
pattern2 = re.compile("(?::|\/|\s|^)fixed(?:\s|\,|\/|:$)")
pattern3 = re.compile("(?::|\/|\s|^)fixing(?:\s|\,|\/|:$)")
pattern4 = re.compile("(?::|\/|\s|^)defect(?:\s|\,|\/|:$)")
pattern5 = re.compile("(?::|\/|\s|^)defects(?:\s|\,|\/|:$)")
pattern6 = re.compile("(?::|\/|\s|^)error(?:\s|\,|\/|:$)")
pattern7 = re.compile("(?::|\/|\s|^)errors(?:\s|\,|\/|:$)")
pattern8 = re.compile("(?::|\/|\s|^)bug(?:\s|\,|\/|:$)")
pattern9 = re.compile("(?::|\/|\s|^)bug-fix(?:\s|\,|\/|:$)")
pattern10 = re.compile("(?::|\/|\s|^)bugfix(?:\s|\,|\/|:$)")
pattern11 = re.compile("(?::|\/|\s|^)bugs(?:\s|\,|\/|:$)")
pattern12 = re.compile("(?::|\/|\s|^)issue(?:\s|\,|\/|:$)")
pattern13 = re.compile("(?::|\/|\s|^)issues(?:\s|\,|\/|:$)")
pattern14 = re.compile("(?::|\/|\s|^)mistake(?:\s|\,|\/|:$)")
pattern15 = re.compile("(?::|\/|\s|^)mistakes(?:\s|\,|\/|:$)")
pattern16 = re.compile("(?::|\/|\s|^)mistaken(?:\s|\,|\/|:$)")
pattern17 = re.compile("(?::|\/|\s|^)incorrect(?:\s|\,|\/|:$)")
pattern18 = re.compile("(?::|\/|\s|^)fault(?:\s|\,|\/|:$)")
pattern19 = re.compile("(?::|\/|\s|^)faults(?:\s|\,|\/|:$)")
pattern20 = re.compile("(?::|\/|\s|^)flaw(?:\s|\,|\/|:$)")
pattern21 = re.compile("(?::|\/|\s|^)flaws(?:\s|\,|\/|:$)")
pattern22 = re.compile("(?::|\/|\s|^)failure(?:\s|\,|\/|:$)")
pattern23 = re.compile("(?::|\/|\s|^)failures(?:\s|\,|\/|:$)")
pattern24 = re.compile("(?::|\/|\s|^)correction(?:\s|\,|\/|:$)")
pattern25 = re.compile("(?::|\/|\s|^)corrections(?:\s|\,|\/|:$)")


#verifica se tem keywords no title
def titleFilter(df):

    result = []
    for index, row in df.iterrows():
        if pattern0.search(row['title']) or pattern1.search(row['title']) or pattern2.search(row['title']) or \
                pattern3.search(row['title']) or pattern4.search(row['title']) or pattern5.search(row['title']) or \
                pattern6.search(row['title']) or pattern7.search(row['title']) or pattern8.search(row['title']) or \
                pattern9.search(row['title']) or pattern10.search(row['title']) or pattern11.search(row['title']) or \
                pattern12.search(row['title']) or pattern13.search(row['title']) or pattern14.search(row['title']) or \
                pattern15.search(row['title']) or pattern16.search(row['title']) or pattern17.search(row['title']) or \
                pattern18.search(row['title']) or pattern19.search(row['title']) or pattern20.search(row['title']) or \
                pattern21.search(row['title']) or pattern22.search(row['title']) or pattern23.search(row['title']) or \
                pattern24.search(row['title']) or pattern25.search(row['title']):
            result.append(True)
        else:
            result.append(False)
    df["Title"] = result

    # print(not df["html_url"].is_unique)
    # print(df['html_url'].duplicated().any())
    return df.loc[df['Title'] == True]

#verifica se tem keywords na lista de tags
def check_tag(row):
    result = False
    if len(row['labels']) > 0:
        for tag in row['labels']:
            if tag['name'].lower() in ['fix', 'fixes', 'fixed', 'fixing', 'defect', 'defects', 'error', 'errors',
                                       'bug', 'bug-fix', 'bugfix', 'bugs', 'issue', 'issues', 'mistake', 'mistakes',
                                       'mistaken', 'incorrect', 'fault', 'faults', 'flaw', 'flaws', 'failure',
                                        'failures', 'correction', 'corrections']:
                    result = True
                    break
    return result
#verifica se tem keywords na lista de tags
def tagFilter(df):
    result = []
    for index, row in df.iterrows():
        if check_tag(row) == True:
            result.append(True)
        else:
            result.append(False)
    df["Tag"] = result
    # print(not df["html_url"].is_unique)
    # print(df['html_url'].duplicated().any())
    return df.loc[df['Tag'] == True]



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

    #pega todos os pull requests que estao com o status merged e aplica o filtro no title
    filtered_titles = titleFilter(df.loc[df['Merged'] == True])
    # pega todos os pull requests que estao com o status merged e aplica o filtro nas tags
    filtered_tags = tagFilter(df.loc[df['Merged'] == True])

    #remove a coluna Title, criada durante o filtro de title
    filtered_titles = filtered_titles.drop('Title', inplace=False, axis=1)
    # remove a coluna Tag, criada durante o filtro de tag
    filtered_tags = filtered_tags.drop('Tag', inplace=False, axis=1)

    #concatena os dois dataframes e remove linhas duplicadas
    result = pd.concat([filtered_titles, filtered_tags], ignore_index=False)
    final_result = result.loc[result.astype(str).drop_duplicates().index]



    # result = pd.concat([filtered_titles, filtered_tags], ignore_index=False)
    # final_result = result.loc[result.astype(str).drop_duplicates().index]
    #
    # final_result = final_result[final_result['Tag'].notna()]
    # final_result = final_result[final_result['Merged'].notna()]



    # if 'ardupilot' in file:
    #     result_sample = final_result.sample(24)
    #     pd.set_option('display.max_colwidth', 1000)
    #     print(result_sample['html_url'].sort_values().to_string(index=False, header=False))
    # if 'PX4' in file:
    #     result_sample = final_result.sample(170)
    #     pd.set_option('display.max_colwidth', 1000)
    #     print(result_sample['html_url'].sort_values().to_string(index=False, header=False))
    # if 'inav' in file:
    #     result_sample = final_result.sample(87)
    #     pd.set_option('display.max_colwidth', 1000)
    #     print(result_sample['html_url'].sort_values().to_string(index=False, header=False))
    # if 'paparazzi' in file:
    #     result_sample = final_result.sample(65)
    #     pd.set_option('display.max_colwidth', 1000)
    #     print(result_sample['html_url'].sort_values().to_string(index=False, header=False))

    # print("Project Name:" + file + "  to analyze:  " + str(len(final_result.loc[final_result['Merged'] == True])) +"   Merged:   "  + str(len(df.loc[df['Merged'] == True])) + "   Tags:   "  + str(len(final_result.loc[final_result['Tag'] == True])) +"   Total pulls: " + str(len(df.index)))

    print("Project Name:" + file + "  to analyze:  " + str(len(final_result)) +"   Total pulls: " + str(len(df.index)))