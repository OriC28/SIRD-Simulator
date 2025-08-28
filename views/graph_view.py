from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel

class GraphView(QMainWindow):
    def __init__(self):
        super().__init__()
    
        self.setWindowTitle("Gráfico de Modelo SIRD")
        self.setGeometry(100, 100, 560, 530)
        
        self.layout = QVBoxLayout()
        
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

    def set_text(self, text: str):
        """Agregar texto a la vista."""
        self.label = QLabel(text)
        self.layout.addWidget(self.label)
    
    def clear_text(self):
        """Limpiar el texto cada que se actualice el gráfico."""
        if hasattr(self, 'label'):
            self.layout.removeWidget(self.label)
            self.label.deleteLater()
   