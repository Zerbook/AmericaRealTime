import os
from datetime import datetime, timedelta
import json


class GettingDataDay:
    def __init__(self, index, dateNew, period):
        self.stack = index
        self.dateNew = dateNew
        self.period = period
        sEndDate = dateNew


        timeDeltaKwarg = {'days': int(self.period)}
        dEndDate = datetime.strptime(sEndDate, "%d-%m-%Y")
        dStartDate = dEndDate - timedelta(**timeDeltaKwarg)

        startYear = dStartDate.year
        endYear = dEndDate.year
        iterYear = startYear

        my_list = []
        listPeriod = []
        my_list.append(iterYear)
        while not iterYear >= endYear:
            if iterYear == startYear:
                line = {dStartDate.strftime("%d-%m-%Y"): "31-12-" + str(startYear)}
                listPeriod.append(line)

            iterYear += 1
            my_list.append(iterYear)








        ee = 1
        #self.period = period
        #self.dateLast = dateLast

