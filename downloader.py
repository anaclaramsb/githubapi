import os

import git #pip install gitpython


import time



repositories = ['https://github.com/ArduPilot/ardupilot', 'https://github.com/betaflight/betaflight', 'https://github.com/PX4/PX4-Autopilot',
                'https://github.com/cleanflight/cleanflight', 'https://github.com/iNavFlight/inav', 'https://github.com/paparazzi/paparazzi']

for url in repositories:
    # print((project.url).split("/")[3])
    path = "/Users/pamsn/Downloads/temp"
    # try:
    # os.mkdir(path)
    git.Git(path).clone(url)
    time.sleep(10)

    # except:
    #     print("download problem" + project.url)