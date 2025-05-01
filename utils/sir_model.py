import numpy as np
from scipy.integrate import odeint
from dataclasses import dataclass

@dataclass
class SIRModel:
    contagion_rate: float
    recovery_rate: float
    total_population: int
    initial_infections: int
    simulation_time: int

    def _SIR_model(self, SIR_vector: list, time_vector: list, beta: float, gamma: float)->list:
        """"Define el modelo SIR con sus respectivas ecuaciones diferenciales."""
        # Vector con los valores iniciales
        S, I, R = SIR_vector

        # Ecuaciones diferenciales
        dSdt = -beta*S*I/self.total_population
        dIdt = beta*S*I/self.total_population - gamma*I
        dRdt = gamma*I

        return dSdt, dIdt, dRdt

    def _get_initial_conditions(self)->list:
        """Devuelve las condiciones iniciales para el modelo."""
        # Todos menos los pacientes iniciales susceptibles
        S0 = self.total_population - self.initial_infections
        # Infectados iniciales
        I0 = self.initial_infections
        # Recuperados iniciales (nadie por defecto)
        R0 = 0 
        return S0, I0, R0
    
    def get_time_vector(self)->list:
        """Devuelve una lista de 0 al tiempo de simulación indicado (días)."""
        return np.linspace(0, self.simulation_time, self.simulation_time)

    def resolve(self)->list:
        """Resuelve las ecuaciones diferenciales del modelo."""
        SIR_vector = self._get_initial_conditions()
        time_vector = self.get_time_vector()
        solution = odeint(self._SIR_model, SIR_vector, time_vector, args=(self.contagion_rate, self.recovery_rate))
        return solution.T

""" test = SIRModel(0.3, 0.1, 1000, 1, 100)
print(test.resolve()) """