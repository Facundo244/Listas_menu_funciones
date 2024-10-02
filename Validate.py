#Validate.py

def validate_number(numero, min , max):

    if min <= numero <= max:

        return True
   
    return False


def validate_length(cadena, long_min, long_max):

    if long_min <= len(cadena) <= long_max:
        
        return True
    
    return False