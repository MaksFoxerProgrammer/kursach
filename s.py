# import unittest
import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets,  QtCore, QtGui
from PyQt5.QtCore import Qt # Теперь работает переключалка дебагера
import diz # Дизайн
from test import * # Из основного модуля


class ExampleApp(QtWidgets.QMainWindow, diz.Ui_MainWindow):
    debug = False

    
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле diz.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.pushButton.clicked.connect(self.run)
        self.checkBox.stateChanged.connect(self.changeCB)


    def run(self):
        self.label_4.setText("")
        self.lineEdit_2.setText("")  
        self.textEdit.setText("")
                
        x1 = int(self.comboBox_1.currentText())
        x2 = int(self.comboBox_2.currentText())
        numb = self.lineEdit.text()

        if numb != "":
            err, rez, out = fromgui(x1, x2, numb, self.debug)

            if err == 0:
                self.label_4.setText("Успех!")
                self.lineEdit_2.setText(rez)
                if self.debug == True:
                    self.textEdit.setText(out)
            else: 
                self.label_4.setText("Возвращена ошибка: " + rez)
                print("Возвращена ошибка...")
        else:
            self.label_4.setText("Кажется, вы забыли ввести число...")
            print("Ooops")


    def changeCB(self, state):
        if state == Qt.Checked:
            self.debug = True
        else:
            self.debug = False



# print("hi")
app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
window = ExampleApp()  # Создаём объект класса ExampleApp
# ui = Ui_MainWindow()
# ui.setupUi(MainWindow)
window.show()  # Показываем окно
app.exec_()  # и запускаем приложение