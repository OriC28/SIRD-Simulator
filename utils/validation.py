
class Validator:
    """Clase destinada a contener métodos para validar las entradas del programa."""

    def validate_number_fields(self, input_fields):
        """Valida que el campo de entrada sea un número entero positivo."""
        
        for input_field in input_fields:
            if type(input_field) == int:
                if input_field < 0:
                    return "Error. Uno de los campos posee un valor negativo. Por favor, asegúrese de que todos los valores sean positivos."
            elif type(input_field) == str:
                if not input_field.isdigit():
                    return "Error. Uno de los campos posee un valor no numérico. Por favor, asegúrese de que todos los valores sean números."
        return None
    
    def validate_empty_fields(self, input_fields: list):
        for field in input_fields:
            if field == '' or field is None:
                return "Error. Todos los campos son requeridos."
        return None