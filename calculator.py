import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon
class MainForm(QMainWindow):
    def __init__(self):
        super(MainForm, self).__init__()

        self.setWindowTitle('CALCULATOR')
        self.setGeometry(200, 200, 420, 250)
        self.setWindowIcon(QIcon('pyqt6-calculator/calc.png'))
        self.initUI()

    def initUI(self):
        self.lbl_number1 = QtWidgets.QLabel(self)
        self.lbl_number1.setText('Number 1: ')
        self.lbl_number1.move(50,30)

        self.txt_number1 = QtWidgets.QLineEdit(self)
        self.txt_number1.move(150,30)
        self.txt_number1.resize(200,32)

        self.lbl_number2 = QtWidgets.QLabel(self)
        self.lbl_number2.setText('Number 2: ')
        self.lbl_number2.move(50,80)

        self.txt_number2 = QtWidgets.QLineEdit(self)
        self.txt_number2.move(150,80)
        self.txt_number2.resize(200,32)

        self.btn_topla = QtWidgets.QPushButton(self)
        self.btn_topla.setGeometry(40,40,40,40)
        self.btn_topla.setText('+')
        self.btn_topla.move(150,120)
        self.btn_topla.clicked.connect(self.hesapla)

        self.btn_cikar = QtWidgets.QPushButton(self)
        self.btn_cikar.setGeometry(40,40,40,40)
        self.btn_cikar.setText('-')
        self.btn_cikar.move(195,120)
        self.btn_cikar.clicked.connect(self.hesapla)
        
        self.btn_carp = QtWidgets.QPushButton(self)
        self.btn_carp.setGeometry(40,40,40,40)
        self.btn_carp.setText('*')
        self.btn_carp.move(150,165)
        self.btn_carp.clicked.connect(self.hesapla)

        self.btn_bol = QtWidgets.QPushButton(self)
        self.btn_bol.setGeometry(40,40,40,40)
        self.btn_bol.setText('/')
        self.btn_bol.move(195,165)
        self.btn_bol.clicked.connect(self.hesapla)

        self.lbl_result = QtWidgets.QLabel(self)
        self.lbl_result.move(250,145)
        self.lbl_result.setText('RESULT: ')


    def hesapla(self):
        sender = self.sender().text()
        
        if sender == '+':
            topla = int(self.txt_number1.text()) + int(self.txt_number2.text())
            self.lbl_result.setText(f'RESULT: ' + str(topla))
        elif sender == '-':
            cikar = int(self.txt_number1.text()) - int(self.txt_number2.text())
            self.lbl_result.setText(f'RESULT: ' + str(cikar))
        elif sender == '*':
            carp = int(self.txt_number1.text()) * int(self.txt_number2.text())
            self.lbl_result.setText(f'RESULT: ' + str(carp))
        elif sender == '/':
            bol = int(self.txt_number1.text()) / int(self.txt_number2.text())
            self.lbl_result.setText(f'RESULT: ' + str(bol))

def app():
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec())

app()