#En donde:
#mensaje: es el mensaje que se va a imprimir antes de pedirle al usuario el dato por consola.
#mensaje_error: mensaje de error en el caso de que el dato ingresado sea invalido.
#mínimo: valor mínimo admitido (inclusive)
#máximo: valor máximo admitido (inclusive)
#reintentos: cantidad de veces que se volverá a pedir el dato en caso de error


#Obtener un tipo de dato entero.

from Validate import validate_number, validate_length


def get_int(mensaje: str, mensaje_error: str , minimo: int , maximo: int , reintentos: int) -> int|None:

    intentos = 0

    while intentos < reintentos:
        
        entrada = input(mensaje)

        if entrada.isdigit():

            valor = int(entrada)

            if validate_number(valor,minimo,maximo):
                return valor
            
            else:
                print(mensaje_error)
        else:
            print(mensaje_error)

        intentos += 1

    return None





#Obtener  un dato tipo float

def get_float(mensaje: str , mensaje_error: str , minimo: int , maximo: int , reintentos: int) -> float|None:

    intentos = 0
    
    while intentos < reintentos:
        entrada = input(mensaje)

        if entrada.count('.') == 1 and entrada.replace('.','',1).isdigit():
            valor = float(entrada)

            if validate_number(valor,minimo,maximo):

                return valor
            
            else: 

                print(mensaje_error)
        else:

            print(mensaje_error)

        intentos += 1

    return None


#Obetner dato tipo string

def get_string(mensaje: str, mesaje_error: str , longitud: int , reintentos: int) -> str|None:

    intentos = 0

    while intentos < reintentos:
        usuario = input(mensaje)

        if validate_length(usuario, longitud, longitud):
            return usuario
        
        else:

            print(mesaje_error)

    return None




