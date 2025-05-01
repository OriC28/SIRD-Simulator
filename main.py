from PyQt6.QtWidgets import QApplication
from controllers.controller import Controller

if __name__ == '__main__':
    app = QApplication([])
    sir_model = Controller()
    app.exec()