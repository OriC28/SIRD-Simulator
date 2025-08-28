from abc import ABC

class Validator(ABC):
    """Clase destinada a contener métodos para validar las entradas del programa."""

    def validate_number_fields(input_fields: list) -> str:
        """Valida que el campo de entrada sea un número entero positivo."""
        
        for input_field in input_fields:
            try:
                if float(input_field) and float(input_field) < 0:
                    return "Error. Uno de los campos posee un valor negativo. Por favor, asegúrese de que todos los valores sean positivos."
            except ValueError:
                return "Error. Uno de los campos posee un valor no numérico. Por favor, asegúrese de que todos los valores sean números."
    
    def validate_empty_fields(input_fields: list)-> str | None:
        for field in input_fields:
            if field == '' or field is None:
                return "Error. Todos los campos son requeridos."
        return None