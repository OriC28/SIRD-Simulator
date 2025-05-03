from views.main_view import SIRModelView
from views.graph_view import GraphView
from utils.sir_model import SIRModel
from utils.draw_graph import DrawGraph
from utils.validation import Validator

class Controller:
    def __init__(self):
        self.main_view = SIRModelView()
        self.graph_view = GraphView()
        self.validator = Validator()
        self.init_gui()

    def init_gui(self):
        """Inicializa la vista principal y las configuraciones de cada widget."""
        self.main_view.simulate.clicked.connect(self.show_graph)
        self.main_view.set_window_icon()
        self.main_view.set_image()
        self.main_view.show()

    def get_inputs(self):
        """Obtiene los datos ingresados por el usuario y los parsea."""

        # Aquí se deberían validar los datos antes de retornarlos
        return [
            float(self.main_view.contagion_rate.text()),
            float(self.main_view.recovery_rate.text()),
            int(self.main_view.population.text()),
            int(self.main_view.initial_infections.text()),
            int(self.main_view.simulation_time.text())
        ]

    def update_graph(self):
        """Actualiza la ventana eliminando el gráfico anterior e integrando uno nuevo."""
        if hasattr(self.graph_view, "graph_canvas"):
            self.graph_view.layout.removeWidget(self.graph_view.graph_canvas)
            self.graph_view.graph_canvas.deleteLater()

    def set_graph(self, graph: DrawGraph):
        """Integra el gráfico y muestra la ventana con el mismo."""
        self.graph_view.graph_canvas = graph.get_canvas()
        graph.animate()
        self.graph_view.layout.addWidget(self.graph_view.graph_canvas)

        self.move_windows()
        self.graph_view.show()

    def move_windows(self):
        """Reordena las ventanas para mostrar ambas a la vez."""
        self.main_view.move(10, 50)
        self.graph_view.move(460, 50)

    def show_graph(self):
        """Abre una nueva ventana con el gráfico del modelo SIR."""
        self.update_graph()
        
        contagion, recovery, population, infections, time = self.get_inputs()
        graph = DrawGraph(SIRModel(contagion, recovery, population, infections, time))

        self.set_graph(graph)

