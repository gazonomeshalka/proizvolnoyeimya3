import sqlite3
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget, QTableWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.loadTable()
        self.r = 0

    def loadTable(self):
        bd = sqlite3.connect('coffee.sqlite')
        cur = bd.cursor()
        self.table.setRowCount(0)
        data = cur.execute("""SELECT * from coffee""").fetchall()
        self.table.setColumnCount(len(data[0]))
        for i in range(len(data)):
            self.table.setRowCount(
                self.table.rowCount() + 1)
            for j in range(len(data[0])):
                self.table.setItem(
                    i, j, QTableWidgetItem(str(data[i][j])))
        self.table.setHorizontalHeaderLabels(['ID', 'название сорта', 'степень обжарки',
                                              'молотый/в зернах', 'описание вкуса', 'цена',
                                              'объём упаковки'])
        bd.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
