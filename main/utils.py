
def validate_type(value, tp, dateobj=None):
    new_value = ''
    if tp == 'int':
        try:
            new_value = int(value)
            return new_value
        except:
            return False

    if tp == 'float':
        if ',' in value:
            new_value = value.replace(',', '.')
        else:
            new_value = value
        
        try:
            new_value = float(new_value)
            return new_value
        except:
            return (False, 'Digite um valor válido')
    
    if tp == 'str':
        if value == '' or len(value) <= 2:
            return (False, 'Digite um nome ou local válido')
        else:
            return value.strip()

    if tp == 'date':
        new_value = dateobj.strptime(value, '%d/%m/%Y').date()
        return new_value