from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.animation as animation
from matplotlib.figure import Figure
from utils.sir_model import SIRModel

class DrawGraph:
    def __init__(self, sir_model: SIRModel):
        self.time_vector = sir_model.get_time_vector()
        self.solution = sir_model.resolve()
        self.figure = Figure() 
        self.canvas = FigureCanvas(self.figure)
    
    def get_canvas(self, frame=None):
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
        
        return self.canvas 

    def animate(self):
        """Realiza la animación en tiempo real que actualiza el gráfico."""
        self.anim = animation.FuncAnimation(self.figure, self.get_canvas, save_count=100, interval=1000)