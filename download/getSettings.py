import os
from datetime import datetime, timedelta
import json

from download.parameters import Param

def GetSetting(index):
    settings = {}
    folderData = Param.folderData.value
    folderStacks = Param.folderStacks.value
    fileSettings = Param.fileSettings.value
    beginPeriod = Param.beginPeriod.value

    if not os.path.isdir(folderData):
        os.mkdir(folderData)
    if not os.path.isdir(folderData + '/' + folderStacks):
        os.mkdir(folderData + '/' + folderStacks)
    if not os.path.isdir(folderData + '/' + folderStacks + '/' + index):
        os.mkdir(folderData + '/' + folderStacks + '/' + index)

    pathFile = folderData + '/' + folderStacks + '/' + index + '/' + fileSettings

    if not os.path.exists(pathFile):
        settings['period'] = beginPeriod
        now = datetime.now() - timedelta(days=1)
        dayLast = now.strftime("%d-%m-%Y")
        settings['dateLast'] = dayLast
        with open(pathFile, 'w') as outfile:
            json.dump(settings, outfile)
    else:
        with open(pathFile) as json_file:
            settings = json.load(json_file)

    return settings