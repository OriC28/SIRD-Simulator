import numpy as np
from scipy.integrate import odeint
from dataclasses import dataclass

@dataclass
class SIRDModel:
    contagion_rate: float
    recovery_rate: float
    mortality_rate: float
    total_population: int
    initial_infections: int
    simulation_time: int

    def _SIR_model(self, SIR_vector: list, time_vector: list, beta: float, gamma: float, miu: float)->list:
        """"Define el modelo SIR con sus respectivas ecuaciones diferenciales."""
        # Vector con los valores iniciales
        S, I, R, D = SIR_vector

        # Ecuaciones diferenciales

        # Representa el número de nuevas infecciones por unidad de tiempo.
        dSdt = -beta*S*I/self.total_population
        # Representa el número de personas que se recuperan por unidad de tiempo.
        dIdt = beta*S*I/self.total_population - (gamma*I) - (miu*I)
        # Representa el número de individuos infectados que se recuperan por unidad de tiempo.
        dRdt = gamma*I
        # Representa el número de individuos infectados que mueren por unidad de tiempo.
        dDdt = miu*I

        return dSdt, dIdt, dRdt, dDdt

    def _get_initial_conditions(self)->list:
        """Devuelve las condiciones iniciales para el modelo."""
        # Todos menos los pacientes iniciales susceptibles
        S0 = self.total_population - self.initial_infections 
        # Infectados iniciales
        I0 = self.initial_infections
        # Recuperados iniciales (nadie por defecto)
        R0 = 0 
        # Muertos iniciales (nadie por defecto)
        D0 = 0
        return S0, I0, R0, D0
    
    def get_time_vector(self)->list:
        """Devuelve una lista de 0 al tiempo de simulación indicado (días)."""
        return np.linspace(0, self.simulation_time, self.simulation_time)
    
    def get_basic_reproductive_number(self)->list:
        """
        Devuelve el número reproductivo básico (R0) del modelo y su estado para determinar el alcanse de la epidemia.
        """
        R0 = self.contagion_rate/(self.recovery_rate + self.mortality_rate)
        status = ""

        if R0 == 0:
            status = "No hay epidemia"
        elif 0 < R0 < 1:
            status = "Epidemia controlada"
        elif R0 == 1:
            status = "Epidemia en equilibrio"
        elif R0 > 1:
            status = "Epidemia en expansión"
        
        return R0, status

    def get_peaks(self)->list:
        """Devuelve el pico de la epidemia de cada grupo (infectados, recuperados y fallecidos)."""
        infected = max(self.resolve()[1])
        recovered = max(self.resolve()[2])
        deceased = max(self.resolve()[3])

        return infected, recovered, deceased
   

    def resolve(self)->list:
        """Resuelve las ecuaciones diferenciales del modelo."""
        SIR_vector = self._get_initial_conditions()
        time_vector = self.get_time_vector()
        solution = odeint(self._SIR_model, SIR_vector, time_vector, args=(self.contagion_rate, self.recovery_rate, self.mortality_rate))
        return solution.T

""" test = SIRDModel(0.3, 0.1, 1000, 1, 100)
print(test.resolve()) """