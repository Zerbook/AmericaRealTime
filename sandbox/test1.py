#!/usr/bin/python3

import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QWidget
from PyQt5.QtGui import QBrush
from PyQt5 import QtGui
from PyQt5.QtCore import Qt


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 700, 550)
        self.setWindowTitle('Пример представления табличных данных')
        tb = Tb(self)


class Tb(QTableWidget):
    def __init__(self, wg):
        super().__init__(wg)
        self.setGeometry(10, 10, 570, 500)
        cf = open('tabl.csv',mode="r", encoding="utf-8")
        data = cf.read()
        lines = data.split('\n')
        self.setColumnCount(len(lines[0].split(','))) # количество столбцов
        self.setHorizontalHeaderLabels(lines[0].split(','))
        for i in range(1, len(lines)): # заполнение таблицы
            if lines[i].strip() ==  '':
                 continue
            self.setRowCount(self.rowCount() + 1) # задать количество строк
            j, p = 0, lines[i].split(',')
            for t in p:
                self.setItem(i - 1, j, Tbi(t)) # задать поля в строке
                j += 1
        self.resizeColumnsToContents() # ширина столцов подогнать по ширине текста

    def keyPressEvent(self, e):
        QTableWidget.keyPressEvent(self, e) #  в начале правильная обработка
        if e.key() == Qt.Key_Return: # отлавливаем нажатие Enter
            print("Нажата Enter")

    def mousePressEvent(self, e):
        QTableWidget.mousePressEvent(self, e) #  в начале правильная обработка
        if e.button() == Qt.LeftButton:
            t = self.currentItem()
            print(t.text()) # содержимое ячейки на консоль
            t.setrc() # изменяем цветовую гамму текущей ячейки


class Tbi(QTableWidgetItem):
     def __init__(self, t):
          super().__init__(t)
          self.setrc()

     def setrc(self): # задание случайных цветов элемента
          r, g, b = getr()
          self.setBackground(QtGui.QColor(r, g, b))
          r, g, b = getr()
          self.setForeground(QtGui.QColor(r, g, b))


def getr(): # три случайных числа
    return random.randint(0, 255), random.randint(0, 255), \
           random.randint(0, 255)

app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())

