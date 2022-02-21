import os
from datetime import datetime, timedelta
import json


class GettingDayData:
    def __init__(self, stack, dateNew):
        self.stack = stack
        self.dateNew = dateNew
        self.settings = {}

        self.fileSettings = 'settings.txt'

        if not os.path.isdir('data'):
            os.mkdir('data')
        if not os.path.isdir('data' + '/' + self.stack):
            os.mkdir('data' + '/' + self.stack)

        pathFile = 'data' + '/' + self.stack + '/' + 'settings.txt'

        if not os.path.exists(pathFile):
            self.settings['period'] = '80'
            now = datetime.now() - timedelta(days=1)
            dayLast = now.strftime("%d-%m-%Y")
            self.settings['dateLast'] = dayLast
            with open(pathFile, 'w') as outfile:
                json.dump(self.settings, outfile)
        else:
            with open(pathFile) as json_file:
                self.settings = json.load(json_file)





        ee = 1
        #self.period = period
        #self.dateLast = dateLast

