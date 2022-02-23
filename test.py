

#from ..gettingDayData import GettingDayData
from download.getSettings import GetSetting
from download.gettingDataDay import GettingDataDay
from download.parameters import Param

#g = Param.folderStacks.value


settings = GetSetting("APPL")

GettingDataDay("APPL", settings['dateLast'], settings['period'])



t = 1