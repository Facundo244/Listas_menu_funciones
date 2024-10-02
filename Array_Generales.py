def listar_numeros(numeros):
    print("Numeros ingresados: ", numeros)




def listar_pares(numeros):

    print("Numeros pares: " , end=" ")
    encontrado = False

    for n in numeros:
        if n % 2 == 0:
            print(n, end=" ")
            encontrado = True
    
    if not encontrado:

        print("No hay numeros pares")
    print()


def listar_posiciones_impares(numeros):
    print("Posiciones de números impares:", end=" ")

    for i in range(len(numeros)):
        if numeros[i] is not None:  
            if numeros[i] % 2 != 0:  
                print(i, end=" ")

    print()


def crear_matriz(cantidad_filas: int,  cantidad_columnas: int, valor_inicial: any) -> list:
    
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]
        
    return matriz

def mostrar_matriz(matriz:list)-> None:

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz[i][j], end=" ")
        print()