import numpy as np
import numpy as np
import matplotlib.pyplot as plt

# ejercicio 1
# invertir el array
#sumar todos los elemento
# sacar el promedio de la sumar

vector = np.array([20,11,2,3,5,10])

#imprime el vector en reversed
"""for e in reversed(vector):
    print(e)"""

# imprime la pos del vector
"""for p in range(len(vector)):
    print(p)"""

def sumaArray(array):
    suma = 0
    promerdio = 0
    for e in vector:
     suma += e
    promedio = suma / len(vector)
    return suma,promedio

suma , promedio = sumaArray(vector)


# ejecicio 2
# mover una posicion hacia la derecha los elemento del sumaArray
#el ultimo debe quedar en la 1 posicion
def desplazarDer(array):
    last = array[len(array)-1]
    for p in reversed(range(len(array))):
        array[p] = array[p -1 ]
    array[0] = last

# ejercio 2 plus

def desplzarIz(array):
    first= array[0]
    for p in range(len(array)-1):
        array[p] = array[p+1]
    array[p+1] = first


# ejercicio 3
# insertar un elemento en el array
# en la posicion pasada por parametro
#si esta lleno el array esta lleno el ultimo se pierde

vector2 =  np.zeros((5),int)
def insertar(array, elemento,pos):
    if pos <= len(vector):
        for p in reversed(range(pos, len(array)-1)):
            array[p+1] = array[p]
        array[pos] = elemento
    else:
        raise Exception('posicion invalida')

# ejercicio 4
# eliminar elemento del vector de la posicion pasada por parmetro
# desplaza todo a la izquierda y agrega un 0 al final

def delete(array,pos):
    if pos < len(array):
        for p in range(pos,len(array)-1):
            array[p] = array[p+1]

        array[len(array)-1] = 0
    else:
        raise Exception('posicion fuera de rango')



# erjicion 5
# eliminar todas la ocurrencias del vector
# recibe por parametro un array y un items a eliminar
# completa el array con 0

vector3 = np.array([2,5,42,2,10,6])
def deleteOcu(array, items):
    for p in range(len(array)):
        if array[p] == items:
            delete(array, p)

# ejercicio 6
# retornar las suma de los valores de todo el array
# calcular en formar recursiva
vector = np.array([1,2,3,4])
def sumaArrayDesde(array,posIncial = None):
    suma = 0
    if posIncial == len(array)-1:
        suma = array[len(array)-1]
    else:
        suma = array[posIncial] + sumaArrayDesde(array, posIncial+1)
    return suma




# matices

matriz1 = np.array(([1,2,3],[6,7,8],[9,10,11]))
matriz2 = np.array(([1,5,6],[9,8,10],[6,7,8]))



# ejercicio 7
# sumar 2 matriz

def sumaDeMatrices(matriz1, matriz2):
    matrizRes = np.zeros((matriz1.shape),int)
    for fila in range(len(matriz1)):
        for colum in range(len(matriz1)):
            matrizRes[fila][colum] = matriz1[fila][colum] + matriz2[fila][colum]
    return matrizRes


# ejercicio 9
# obtener la suma de los elemento de la diagonal superior de la matriz

matriz = np.array(([0,0,20],[4,5,0],[7,8,1]))
def diagonalSup(matriz):
    res = 0
    for fila in range(0,len(matriz)-1):
        for colum in range(fila+1,len(matriz[0])):
            res += matriz[fila][colum]
    return res
    


# ejercicio 10
# retorna true si la matriz es matriz diagonal

# matriz diagonal tiene  todo cero menos la diagonal principal

def matrizCuadrada(matriz):
    diagonal = True
    posFila = 0
    while diagonal and posFila < len(matriz):
        posColum = 0
        while diagonal and posColum < len(matriz):
            if posFila != posColum and matriz[posFila][posColum] != 0:
                diagonal = False
            posColum += 1
        posFila +=1
    return diagonal
matriz = np.array([[1,1,0],[0,1,0],[0,0,1]])


arreglo = np.array([['d','s','e'],['s','d','a'],['e','a','d']])
# ejercio 11 matriz cuadrada

def matrizCuadrada2(arreglo):
    res = False
    posFila = 0
    posCol = 0
    while posFila < len(arreglo):
        if arreglo[posFila][posCol] == arreglo[posFila+1][posCol+1]:
            res = True
            posCol +=1
        posFila += 1
            
# ejercicio 12

arreglo1 = np.array([[3,10,20],[20,1,1000],[0,40,1]])

def sumaTrazaMatriz(arreglo, posCol = 0, posFila = 0):
    suma = 0
    if posFila == len(arreglo)-1:
        suma = arreglo[posCol][posFila]
    else:
        suma =  arreglo[posCol][posFila] + sumaTrazaMatriz(arreglo, posCol +1, posFila +1)
    
    return suma




# ejercicio 15

felix = np.genfromtxt('felix.csv',delimiter =',')
plt.imshow(felix)
plt.show()

print(felix[0:50][0:4])