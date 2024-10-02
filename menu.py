#Realizar un menú de opciones en donde el usuario pueda realizar las siguientes operaciones:
#Pedir el ingreso de 10 números enteros entre -1000 y 1000. 
#Mostrar la cantidad de números positivos y negativos.
#Mostrar la sumatoria de los números pares.
#Informar el mayor de los números impares.
#Listar todos los números ingresados.
#Listar todos los números pares.
#Listar los números de las posiciones impares.  
#Salir



#Notas:
#Solo se podrá ingresar a las opciones b a g, siempre y cuando el usuario haya ingresado los datos solicitados.
#Todas las opciones deberán ser programadas en funciones: habrá funciones específicas (por ejemplo para determinar si un número es positivo o negativo) y funciones de nivel general (por ejemplo una función que liste los números pares). Tener en cuenta las características de la programación funcional.
#Las funciones específicas deberán estar en el módulo “Especificas.py”, mientras que las generales en el módulo “Array_Generales.py”. Todos estos módulos deben estar integrados en el paquete Package_Arrays.
#Utilizar las funciones input del paquete Package_Input.



from Input import get_float,get_int,get_string
from Especificar import contar_positivos_y_negativos,sumar_pares,mayor_impares
from Array_Generales import listar_numeros, listar_pares ,listar_posiciones_impares

def menu():
    print("\nMenú de Opciones:")
    print("1. Ingresar 10 números")
    print("2. Mostrar cantidad de números positivos y negativos")
    print("3. Mostrar sumatoria de los números pares")
    print("4. Informar el mayor de los números impares")
    print("5. Listar todos los números ingresados")
    print("6. Listar todos los números pares")
    print("7. Listar los números de las posiciones impares")
    print("8. Salir")
    return input("Seleccione una opción: ")

def ingresar_numeros(cantidad: int, minimo: int, maximo: int) -> list:

    numeros = [0] * cantidad  
    for i in range(cantidad):
        numero = get_int(f"Ingrese un número entre {minimo} y {maximo}: ", "Número inválido.", minimo, maximo, 3)
        numeros[i] = numero
    return numeros

def main():

    cantidad_numeros = 10
    numeros = []
    
    while True:
        opcion = menu()

        match opcion:

            case "1":
                numeros = ingresar_numeros(cantidad_numeros, -1000,1000)
                print("Numeros ingresados: ", numeros) 
            case "2":
                contar = contar_positivos_y_negativos(numeros)
                print(f"Los numeros positivos son : {contar}")

            case "3":
                pares = sumar_pares(numeros)
                print(f"La suma de pares es: {pares}")
            case "4":
                mayor_impar = mayor_impares(numeros)
                print(f"El mayor de los numero impares es: {mayor_impar}")    
            case "5":
                listar_numeros(numeros) 
            case "6":
                listar_pares(numeros)
            case "7":
                listar_posiciones_impares(numeros)
            case "8":
                print("Saliendo del programa...")
                break  

            case _:
                print("Opción no válida, por favor intente nuevamente")


# Sirve para que el menu se ejecute cuando se corre directamente
if __name__ == "__main__":
    main()

        
