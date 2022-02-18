import os
import sys
import youtube_dl
import time
from PyQt5 import QtCore, QtGui, QtWidgets
#from des import *
from PyQt5.QtCore import QPropertyAnimation, QRect, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QTableWidgetItem

from formTerminal import Ui_MainWindow


class downloader(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.url = None
        self.indexes = None
        self.keyStop = True
    def run(self):
        #      привет мир
        #self.mysignal.emit('Процесс скачивания запущен!')
        #with youtube_dl.YoutubeDL({}) as ydl:
        # ydl.download([self.url])
        #self.mysignal.emit('Процесс скачивания завкршен!')
        row = 0
        for item in self.indexes:
            if self.getKeyStop():
                break
            time.sleep(1)
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

class TerminalWin(QtWidgets.QMainWindow):
    indexes = []
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Терминал real time')
        self.setWindowIcon(QIcon('icon2.ico'))


        with open("indexes.txt", "r") as file:
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
        self.mythread = downloader()
        self.mythread.mysignal.connect(self.handler)

    def start(self):
        #if len(self.ui.lineEdit.text()) > 5:
            #if self.download_folder != None:
                #link = self.ui.lineEdit.text()
                #self.mythread.init_args(link)


                self.mythread.setKeyStop(False)
                self.mythread.init_indexes(self.indexes)

                self.mythread.start()
                #self.locker(True)
           # else:
           #     QtWidgets.QMessageBox.warning(self, "Ошибка", "Вы не выбрали папку!")
        #else:
          #  QtWidgets.QMessageBox.warning(self, "Ошибка", "Ссылка на видео не указана!")

    def stop(self):
        #self.download_folder = QtWidgets.QFileDialog.getExistingDirectory(self, 'Выбрать папку для сохранения')
        #os.chdir(self.download_folder)
        self.mythread.setKeyStop(True)
        #flags = self.windowFlags() | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint
        #self.setWindowFlags(flags)
        #self.anim = QPropertyAnimation(self, b"geometry")
        #self.anim.setStartValue(QRect(150,30,200,1))


    def handler(self, value):

            self.ui.plainTextEdit.appendPlainText(value)

    def locker(self, lock_value):
        base = [self.ui.pushButton]  #, self.ui.pushButton_2
        for item in base:
            item.setDisabled(lock_value)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = TerminalWin()
    win.show()
    sys.exit(app.exec_())

