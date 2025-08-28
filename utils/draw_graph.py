from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.animation as animation
from matplotlib.figure import Figure
from utils.sird_model import SIRDModel

class DrawGraph:
    """Clase para dibujar el gráfico del modelo SIRD."""
    def __init__(self, sird_model: SIRDModel):
        self.sird_model = sird_model
        self.time_vector = sird_model.get_time_vector()
        self.solution = sird_model.resolve()
        self.figure = Figure() 
        self.canvas = FigureCanvas(self.figure)
    
    def get_canvas(self, frame=None):
        """Dibuja el gráfico y lo muestra en un canvas de Qt."""
        S, I, R, D = self.solution

        # Limpiar la figura si ya existe una
        self.figure.clear()
        
        ax = self.figure.subplots()

        ax.set_title("Modelo SIRD enfocado en individuos de tercera edad")
        
        ax.plot(self.time_vector, S, label="Susceptibles")
        ax.plot(self.time_vector, I, label="Infectados")
        ax.plot(self.time_vector, R, label="Recuperados")
        ax.plot(self.time_vector, D, label="Fallecidos")
        ax.set_xlabel('Días')
        ax.set_ylabel(f'Número de personas')
        ax.legend()
        
        return self.canvas 

    def animate(self):
        """Realiza la animación en tiempo real que actualiza el gráfico."""
        self.anim = animation.FuncAnimation(self.figure, self.get_canvas, save_count=100, interval=1000)
        