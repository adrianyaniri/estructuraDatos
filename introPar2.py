import numpy as np

# Funciones

# ejercio 1

# procedimiento saludo que imprima 'hola mundo' cada vez q se lo invoque

def saludo():
    print('hola mundo')

# ejercicio 2
# procedimiento que imprima el texto pasado por parametro

def mensaje(texto):
    print(texto)

mensaje('hola adrian')

# ejercicio 3
#funcion que retorne el factorial del numero pasado por parametro

def factorial(numero):
    fac = 1
    if numero !=0:
        for i in range(1,numero + 1):
            fac *= i
    else:
        fac = 1
    return fac

# ejercicio 4
# calcular el valor despues de aplicar el iva = 21%

def facturaConImporte(importe, impuesto = 21):
    total = impuesto / 100 * importe + importe
    return total

# ejercicio 5
# funcio recibe 2 numero por parametro y retorna el mayor

def mayorEntre(num1,num2):
    mayor = None
    if num1 > num2:
        mayor = num1
    else:
        mayor = num2
    return mayor

# ejercicio 6
#funcio que calcual el area de un circulo
# funcion q calcule el volumen usando la funcion anterior

def areaCirculo(radio):
    return np.pi * radio**2

def volumenCirculo(radio,altura):
    return areaCirculo(radio) * altura

# ejercicio 7
# calcular el promedio pasado por parametro
# retornar aprobado si el promedio es >=7
# caso contrario retornar desaporbado

def calificacion(n1,n2,n3):
    promedio = (n1 + n2 + n3) / 3
    calif = None
    if promedio < 7:
        calif = 'desaprobado'
    else:
        calif = 'aprobado'
    return 'promedio: ', promedio, calif

#ejercicio 8
# calcular la potencia n al la m de numeros enteros

def potenciaEnteros(n,m):
    if n > 0 and m > 0:
        potencia = n ** m
    else:
        potencia = 1
    return potencia

# ejercicio 9
# funcion que recibe por parametro horas, minutos y segundo
# retorna la cantida en segundo

def totalSegundos(hora, minutos, segundos):
    totalMinutos = hora *60 + minutos
    totalSegundos = totalMinutos * 60 + segundos
    return totalSegundos

# ejercicio 10
# retornar si es bisiesto el anio pasado por parametro

def bisiesto(anio):
    return anio % 4 == 0 and anio % 100 != 0 or anio % 10 == 0 and anio % 400 ==0

# ejercicio 11
# calcular los annio bisiesto que hay entre los numeros pasados por parametros

def aniosBisiestos(anio1, anio2):
    cant = 0
    for n in range(anio1,anio2 + 1):
        if bisiesto(n):
            cant +=1
    return cant


# ejercicio 12
# funcion que resibe por parametro un numero y retorna la suma d los mismos

def sumaDigitos(num):
    suma = 0
    digito = 0
    entero = num
    while entero !=0:
        digito = entero % 10
        entero = entero // 10
        suma = suma + digito
    return suma

# opcion funcion recursiva
def sumaDigitos2(num):
    suma =0
    digito = 0
    if num // 10 == 0:
        suma = num
    else:
        digito = num % 10
        suma = sumaDigitos2(num // 10) + digito

    return suma


# ejercicio 13
# funcion que dado 2 numero por parametro retorne el que tiene mayor sumatoria de sumaDigitos

def mayorSumatoria(num1,num2):
    mayor = None
    if sumaDigitos(num1) > sumaDigitos(num2):
        mayor = num1
    else:
        mayor = num2
    return mayor


numeros = [22,155,10,555]

for n in range(len(numeros)):
    cantMayores = 0
    cantMenores = 0
    if sumaDigitos(n) >= 10:
        cantMayores +=1
    else:
        sumaDigitos(n) < 10
        cantMenores +=1
print(cantMenores, cantMayores)
