from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from utils.sir_model import SIRModel

class DrawGraph:
    def __init__(self, sir_model: SIRModel):
        self.time_vector = sir_model.get_time_vector()
        self.solution = sir_model.resolve()
        self.figure = Figure() 
        self.canvas = FigureCanvas(self.figure)  

    def get_canvas(self):
        """Dibujar el gráfico y lo muestra en un canvas de Qt."""
        S, I, R = self.solution

        # Limpiar la figura si ya existe una
        self.figure.clear()
        
        ax = self.figure.subplots()
        ax.plot(self.time_vector, S, label="Susceptibles")
        ax.plot(self.time_vector, I, label="Infectados")
        ax.plot(self.time_vector, R, label="Recuperados")
        ax.set_xlabel('Días')
        ax.set_ylabel('Número de personas')
        ax.legend()
        
        # Dibujar el gráfico
        self.canvas.draw()
        
        return self.canvas 
