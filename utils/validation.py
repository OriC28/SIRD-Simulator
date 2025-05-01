
class Validator:
    """Clase destinada a contener métodos para validar las entradas del programa."""
    def validate_empty_fields(self, input_fields: list):
        for field in input_fields:
            if field == '' or field is None:
                return "Error. Todos los campos son requeridos."
    