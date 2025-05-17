from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6 import uic, QtGui

class SIRDModelView(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('gui/gui.ui', self)

    def set_image(self)->None:
        """Configura el logo de la aplicación en la interfaz gráfica."""
        resource = QtGui.QPixmap("resources/logo.png")
        self.image.setScaledContents(True)
        self.image.resize(300, 250)
        self.image.setPixmap(resource)

    def show_message(self, type, title, text):
        message = QMessageBox()
        if type == 'warning':
            message.warning(self, title, text)
        
    def set_window_icon(self)->None:
        """Establece el ícono de la ventana del programa."""
        self.setWindowIcon(QtGui.QIcon('resources/icon.png'))