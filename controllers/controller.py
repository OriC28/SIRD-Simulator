from views.main_view import SIRDModelView
from views.graph_view import GraphView
from utils.sird_model import SIRDModel
from utils.draw_graph import DrawGraph
from utils.validation import Validator

class Controller:
    def __init__(self):
        self.main_view = SIRDModelView()
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
        """Obtiene los datos ingresados, los valida y parsea."""
        input_fields = [
            self.main_view.contagion_rate.text(),
            self.main_view.recovery_rate.text(),
            self.main_view.mortality_rate.text(),
            self.main_view.population.text(),
            self.main_view.initial_infections.text(),
            self.main_view.simulation_time.text()
        ]
        #Validar campos vacíos 
        error = Validator.validate_empty_fields(input_fields)
        if error is not None:
            SIRDModelView.show_message(self.main_view,"warning", "Error", error)
            return [None for field in input_fields]

        # Validar campos numéricos
        error = Validator.validate_number_fields(input_fields)
        if error is not None:
            SIRDModelView.show_message(self.main_view,"warning", "Error", error)
            return [None for field in input_fields]
        
        #Si todo es correcto, se retornan los datos
        return [
            float(self.main_view.contagion_rate.text()),
            float(self.main_view.recovery_rate.text()),
            float(self.main_view.mortality_rate.text()),
            int(self.main_view.population.text()),
            int(self.main_view.initial_infections.text()),
            int(self.main_view.simulation_time.text())
        ]

    def update_graph(self):
        """Actualiza la ventana eliminando el gráfico anterior e integrando uno nuevo."""
        if hasattr(self.graph_view, "graph_canvas"):
            self.graph_view.layout.removeWidget(self.graph_view.graph_canvas)
            self.graph_view.graph_canvas.deleteLater()
        self.graph_view.clear_text()

    def set_graph(self)->None:
        """Integra el gráfico y los datos principales en la ventana."""
        # Establecer gráfico
        self.graph_view.graph_canvas = self.graph.get_canvas()
        self.graph.animate()
        self.graph_view.layout.addWidget(self.graph_view.graph_canvas)
        
        # Integrar datos estadísticos
        self.set_data_text()

        # Reorganizar ventanas
        self.move_windows()
        

    def set_data_text(self)->None:
        """Agrega los datos estadísticos principales a la vista."""
        R0, status = self.sird_model.get_basic_reproductive_number()
        infected, recovered, deceased = self.sird_model.get_peaks()
        self.graph_view.set_text(
            f"""
            Número de reproducción básico: {R0:.2f} ({status})\n
            Picos de la epidemia: (Infectados: {infected:.2f}, Recuperados: {recovered:.2f}, Fallecidos: {deceased:.2f})\n
            """
        )

    def move_windows(self)->None:
        """Reordena las ventanas para mostrar ambas a la vez."""
        self.main_view.move(10, 50)
        self.graph_view.move(460, 15)

    def show_graph(self)->None:
        """Abre una nueva ventana con el gráfico del modelo SIRD."""
        
        contagion, recovery, mortality, population, infections, time = self.get_inputs()
        if (contagion is not None):
            self.update_graph()

            self.sird_model = SIRDModel(contagion, recovery, mortality, population, infections, time)
            self.graph = DrawGraph(self.sird_model)

            self.set_graph()

            self.graph_view.show()

