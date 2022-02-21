
import sys
import youtube_dl
import time
from PyQt5 import QtCore, QtGui, QtWidgets
#from des import *
from PyQt5.QtCore import QPropertyAnimation, QRect, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QTableWidgetItem

from forms.formTerminal import Ui_MainWindow
from paralProcess import ParalProcess


class TerminalWin(QtWidgets.QMainWindow):
    indexes = []
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Терминал real time')
        self.setWindowIcon(QIcon('assets/icon2.ico'))

        with open("data/indexes.txt", "r") as file:
            for line in file:
                self.indexes.append(line.strip())
                #print(line.strip())
        self.ui.tableWidget.setColumnCount(2)
        self.ui.tableWidget.setRowCount(len(self.indexes))
        self.ui.tableWidget.setHorizontalHeaderLabels(
            ('Индекс', 'Примечание')
        )
        row = 0
        for item in self.indexes:
            cellinfo = QTableWidgetItem(item)
            self.ui.tableWidget.setItem(row, 0, cellinfo)
            row += 1

        self.download_folder = None
        self.ui.pushButton.clicked.connect(self.stop)
        self.ui.pushButton_2.clicked.connect(self.start)
        self.paralProcess = ParalProcess()
        self.paralProcess.mysignal.connect(self.handler)

    def start(self):
        self.paralProcess.setKeyStop(False)
        self.paralProcess.init_indexes(self.indexes)
        self.paralProcess.start()

    def stop(self):
        self.paralProcess.setKeyStop(True)

    def handler(self, value):
            self.ui.plainTextEdit.appendPlainText(value)

    def locker(self, lock_value):
        base = [self.ui.pushButton]
        for item in base:
            item.setDisabled(lock_value)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = TerminalWin()
    win.show()
    sys.exit(app.exec_())

