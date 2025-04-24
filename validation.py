

class Validator:
    
    def validate_type(self, type, value):
        try:
            if type == 'float':
               float(value)
            else:
                int(value)
        
        except Exception as e:
            return False