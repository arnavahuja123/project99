import os
import shutil
import time
path=input("path to remove old files: ")
days = input("delete files before:")
timeComparer=(time-time())-1*86400

for fileName in os.listdir(path):
    if os.path.getmtime(os.path.join(path,fileName))<timeComparer:
        if os.path.isfile(os.path.join(path,fileName)):
            print(fileName)

        elif os.path.listdir(os.path.join(path,fileName)):
            print(fileName)
            shutil.rmtree(os.path.join(path,fileName))