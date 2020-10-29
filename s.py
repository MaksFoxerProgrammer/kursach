import unittest
import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets,  QtCore, QtGui
# from gui import Ui_MainWindow # Здесь подключается UI формы
import diz
from test import *


class ExampleApp(QtWidgets.QMainWindow, diz.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле diz.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.pushButton.clicked.connect(self.run)


    def run(self):
        x1 = int(self.comboBox_1.currentText())
        x2 = int(self.comboBox_2.currentText())
        numb = self.lineEdit.text()
        if numb != "":
            rez = fromgui(x1, x2, numb)
            if rez != '':   
                pass  
        else:
            print("Ooops")




# print("hi")
app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
window = ExampleApp()  # Создаём объект класса ExampleApp
# ui = Ui_MainWindow()
# ui.setupUi(MainWindow)
window.show()  # Показываем окно
app.exec_()  # и запускаем приложение