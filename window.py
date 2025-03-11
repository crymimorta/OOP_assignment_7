from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QMessageBox
from calculator import Calculator
from PyQt6 import uic
from output import Ui_MainWindow

class CalculatorWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("calc.ui", self)  
        self.calculator = Calculator()
        self.init_ui()

    def init_ui(self):
        self.lineEdit.setReadOnly(True)
        self.pushButton_2.clicked.connect(lambda: self.on_button_click("0"))
        self.pushButton_10.clicked.connect(lambda: self.on_button_click("1"))
        self.pushButton_11.clicked.connect(lambda: self.on_button_click("2"))
        self.pushButton_14.clicked.connect(lambda: self.on_button_click("3"))
        self.pushButton_5.clicked.connect(lambda: self.on_button_click("4"))
        self.pushButton_13.clicked.connect(lambda: self.on_button_click("5"))
        self.pushButton_6.clicked.connect(lambda: self.on_button_click("6"))
        self.pushButton.clicked.connect(lambda: self.on_button_click("7"))
        self.pushButton_12.clicked.connect(lambda: self.on_button_click("8"))
        self.pushButton_8.clicked.connect(lambda: self.on_button_click("9"))
        self.pushButton_4.clicked.connect(lambda: self.on_button_click("+"))
        self.pushButton_15.clicked.connect(lambda: self.on_button_click("-"))
        self.pushButton_7.clicked.connect(lambda: self.on_button_click("*"))
        self.pushButton_3.clicked.connect(lambda: self.on_button_click("/"))
        self.pushButton_16.clicked.connect(self.clear)
        self.pushButton_9.clicked.connect(self.calculate)

    def on_button_click(self, char):
        self.calculator.add_to_expression(char)
        self.lineEdit.setText(self.calculator.get_expression())

    def clear(self):
        self.calculator.clear_expression()
        self.lineEdit.setText("")

    def calculate(self):
        result = self.calculator.calculate()
        self.lineEdit.setText(result)
        if result in ["Error", "Error: Division by Zero"]:
            QMessageBox.warning(self, "Calculation Error", result)
        else:
            self.calculator.expression = result
