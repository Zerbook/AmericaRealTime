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

        iterYear = dStartDate.year
        endYear = dEndDate.year

        my_list = []
        my_list.append(iterYear)
        while not iterYear >= endYear:
            iterYear += 1
            my_list.append(iterYear)








        ee = 1
        #self.period = period
        #self.dateLast = dateLast

