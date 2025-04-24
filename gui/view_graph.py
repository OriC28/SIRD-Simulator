from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout

class GraphView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SIR Model Graph")
        self.setGeometry(100, 100, 800, 600)
        
        self.layout = QVBoxLayout()
        
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)
   