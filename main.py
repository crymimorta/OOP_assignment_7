from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QMessageBox
from window import CalculatorWindow

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = CalculatorWindow()
    window.show()
    sys.exit(app.exec())
