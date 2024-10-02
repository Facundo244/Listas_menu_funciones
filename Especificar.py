def contar_positivos_y_negativos(numeros):
    positivo = 0
    negativos = 0

    for n in numeros:
        if n > 0:
            positivo += 1
        elif n < 0:
            negativos += 1

    return positivo , negativos
    




def sumar_pares(numeros):

    suma = 0
    for n in numeros:
        if n % 2 == 0:
            suma += n
    return suma


def mayor_impares(numeros):

    mayor =  None
    for n in numeros:
        if n %2 != 0:
            if mayor is None or n > mayor:
                mayor = n
    return mayor