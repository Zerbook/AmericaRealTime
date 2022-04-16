from PyQt5 import QtCore
import time


class paralProcess(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.url = None
        self.indexes = None
        self.keyStop = True
    def run(self):
        row = 0
        for item in self.indexes:
            if self.getKeyStop():
                break
            time.sleep(0.2)
            self.mysignal.emit(str(row))
            row += 1

        self.mysignal.emit('finish')
        rrr = 1
    def init_args(self, url):
        self.url = url
    def init_indexes(self, indexes):
        self.indexes = indexes
    def getKeyStop(self):
        return self.keyStop
    def setKeyStop(self, key):
        self.keyStop = key