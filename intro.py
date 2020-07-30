import numpy as np

# hola mundo

print('hola mundo')

# ejercio N 2
saludo = 'hola mundo, bienvendidos'
print(saludo)

# ejercicio 3

num1 = 10
num2 = 20

suma = num1 + num2
resta = num1 - num2
multi = num1 * num2
div = num1 // num2
resto = num1 % num2

print('suma',suma)
print('resta', resta)
print('multiplicacion',multi)
print('divicion entera', div)
print('resto', resto)

# ejercicio 4
# pasar de grados celcius a fahrenheit

gradosC = 20
gradosF = 1.8 * gradosC + 32
#print(gradosF)

# ejercicio 5
# calcular primetro y area de un rectangulo
base = 2
altura = 4
perimetro = 2 * base + 2 * altura
area = base * altura

# calcular area de un circulo
pi = np.pi
radio = 2
areaC = pi *radio **2

# ejecicio 6
# ingresar 2 numero enteros
# indicar cual es el mayor
# si son iguales indicar por separado

num1 = 20
num2 = 20

if num1 > num2:
    print(num1)
elif num1 < num2:
    print(num2)
else:
    print('los numeros son iguales')

# ejercio 7
# ingresa nombre por input

nombre = 'adrian '
saludo = 'hola'
print(saludo , nombre)

# ejercicio 8
# indicar si el numero es par o impar
num = 20

if num % 2 == 0:
    print('numero par')
else:
    print('numero impar')

# ejercicio 9
# indicar el dia de la semana correspondiente a cada numeros
# si el numero esta fuera del rango lanzar error

dia = 7
if dia > 7 or dia < 0 :
    raise Exception('dia de la semana incorreto')
elif dia == 1:
    print('lunes')
elif dia == 2:
    print('martes')
elif dia == 3:
    print('miercoles')
elif dia == 4:
    print('jueves')
elif dia == 5:
    print('viernes')
elif dia == 6:
    print('sabado')
else:
    print('domingo')

# ejercicio 10
# grupos divididos por genero y nombre
# grupo A mujeres con inicial anterio M y hombres con inicial # N
# grupo B resto

inicial = 'b'
genero = 'F'

if genero == 'F' and inicial < 'm' or genero == 'M' and inicial > 'n':
    print('pertenece al Grupo A ')
else:
    print('pertences al grupo B')

# ejercicio 11
# calcular precio de entrada para clientes
# menores a 4 = $0
# entre 4 y 18 = $ 5
# mayores 18 = $ 10

edad = 24
valorEntrada = None

if edad == 4:
    valorEntrada = 0
elif edad > 4 and edad < 18:
    valorEntrada = 5
else:
    valorEntrada = 10
print(valorEntrada)
print('\n')

# ejercicio 12
# mostrar todos numero en el rango dado
# usar ciclo while y for


rango = 10
numero = 0
while numero  < rango:
    print(numero)
    numero += 1
print('\n')
for n in range(rango):
    print(n)
# ejercicio 13
# imprimir todos lo numero entero entre los num1 y num2

num1 =0
num2 = 20
print('\n')
# opcion for 1
for n in range(num1,num2):
    if n % 2 == 0:
        print(n)
print('\n')
# opcion for 2
for n in range(num1,num2,2):
    print(n)

# ejercicio 14
# imprimir la cantidad n veces la variable nombre, en linea distintas

nombre = 'racing'
veces = 5
for n in range(5):
    print(nombre)


# ejerccio 15
# imprimir triangulo del signo *

simbolo = "*"
repetir = 5

for t in range(repetir):
    print(simbolo)
    simbolo += "*"

# ejercio 16
#imprimir la fichas de domino sin repetir

for i in range(7):
    for j in range(i,7):
        print(i, '/', j)


# ejercio 17
# impimir la suma de los numero n
# ejemplo n = 5 salida 1+2+3+4+5=15

numero = 5
suma = 0

for n in range(numero+1):
    suma += n
    print(suma)

# ejercicio 18
# calcula la suma de los numero pares de un numero N

n = 10
suma = 0
for n in range(0,n,2):
    suma += n*2
    print(suma)



def sumaOResta( opcion = 0, n1 = 0 , n2 = 0):
    salida = None
    if opcion == 0:
        salida= n1 + n2
    elif opcion == 1:
        salida = n1 - n2
    return salida


def sumaYResta(x = 0, y = 0):
    suma = x + y
    resta = x - y
    return suma , resta

resultado = sumaOResta(1,10,15)
resultado2 = sumaYResta(8,9)

print(resultado)
print(resultado2)