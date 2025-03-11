from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QMessageBox
class Calculator:
    def __init__(self):
        self.expression = ""

    def add_to_expression(self, char: str):
        self.expression += char

    def remove_last_character(self):
        self.expression = self.expression[:-1]

    def clear_expression(self):
        self.expression = ""

    def calculate(self):
        try:
            result = eval(self.expression)
            return str(result)
        except ZeroDivisionError:
            return "Error: Division by Zero"
        except Exception:
            return "Error"

    def get_expression(self):
        return self.expression

