from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic, QtGui

class SIRModelView(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('gui/gui.ui', self)

    def set_image(self)->None:
        """Configura el logo de la aplicación en la interfaz gráfica."""
        resource = QtGui.QPixmap("resources/dibujito.png")
        self.image.setScaledContents(True)
        self.image.resize(141, 123)
        self.image.setPixmap(resource)
    
    def set_window_icon(self)->None:
        """Establece el ícono de la ventana del programa."""
        self.setWindowIcon(QtGui.QIcon('resources/dibujito.png'))