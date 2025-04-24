from gui.view import SIRModelView
from gui.view_graph import GraphView
from sir_model import SIRModel
from graphs import DisplayGraph
from validation import Validator

class Controller:
    def __init__(self):
        self.view = SIRModelView()
        self.view_graph = GraphView()
        self.validator = Validator()
        self.init_gui()

    def init_gui(self):
        """Inicializa la vista principal y las configuraciones de cada widget."""
        self.view.simulate.clicked.connect(self.show_graph)
        self.view.set_window_icon()
        self.view.set_image()
        self.view.show()

    def get_inputs(self):
        """Obtiene los datos ingresados por el usuario y los parsea."""
        return [
            float(self.view.contagion_rate.text()),
            float(self.view.recovery_rate.text()),
            int(self.view.population.text()),
            int(self.view.initial_infections.text()),
            int(self.view.simulation_time.text())
        ]
    
    def show_graph(self):
        """Abre una nueva ventana con el gráfico del modelo SIR."""

        # Si la ventana ya tieen un gráfico, eliminarlo
        if hasattr(self.view_graph, "graph_canvas"):
            self.view_graph.layout.removeWidget(self.view_graph.graph_canvas)
            self.view_graph.graph_canvas.deleteLater()
        
        contagion, recovery, population, infections, time = self.get_inputs()
        graph = DisplayGraph(SIRModel(contagion, recovery, population, infections, time))

        self.set_graph(graph)

    def set_graph(self, graph: DisplayGraph):
        """Integra el gráfico y muestra la ventana con el mismo."""
        self.view_graph.graph_canvas = graph.get_canvas()
        self.view_graph.layout.addWidget(self.view_graph.graph_canvas)
        self.view_graph.show()
