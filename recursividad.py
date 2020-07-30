# ejercio 1
# calcular el factorial de numero forma recursiva

def factorial(num):
    fac = None
    if num == 0:
        fac = 1
    else:
        fac = factorial(num-1)* num
    return fac

# ejercio 2
# calcular la cantidad de agua que pierde una canilla
# primer dia pierde solo 2 gotas

def perdidad(dias):
    cant = 2
    if dias == 1:
        cant = 2
    else:
        cant += perdidad(dias-1)
    return cant

# ejercio 3
# calcualar la secuencia fibonacci en forma recursiva

def fibonacci(numero):
    secuencia = None
    if numero == 0 or numero ==1:
        secuencia = numero
    else:
        secuencia = fibonacci(numero-1) + fibonacci(numero -2)
    return secuencia


# ejercio 4
#calcular el numero triangular de inice n

def nroTriangular(numero):
    suma = None
    if numero == 0:
        suma = numero
    else:
        suma = nroTriangular(numero -1) + numero
    return suma

#ejercio 5
# calcular la cantidad de seguidores por posteo
# los primero 20 posteos , seguidores = 1000 x cada posteo
# a partir de 21 se duplica + 500 extras

def seguidores(posteos = None):
    total = None
    if posteos == 1:
        total = 1000
    elif posteos <= 20:
        total = seguidores(posteos-1)+ 1000
    else:
        total = seguidores(posteos - 1)*2 + 500
    return total

#ejercicio 6
# cantidad de baldosas coloacadas en n dias

def cantBaldosas(dias):
    cant = None
    if dias == 1:
        cant = 100
    elif dias % 2 == 0:
        cant = cantBaldosas(dias -1 ) *2
    else:
        cant = cantBaldosas(dias -2) + cantBaldosas(dias -1)
    return cant

def cantBaldosasColocadas(nroDias):
    cant = None
    if nroDias == 1:
        cant = cantBaldosas(dias)
    else:
        cant = cantBaldosas(nroDias) + cantBaldosas(nroDias -1)
    return cant
cantBaldosasColocadas(10)

#ejercico 7
#calcular cuantas cantidad de algas hay en un estanque
# primer dias 12 algas , 2 -11 dias se incrementan 15 por dias
# desde el 12 triplica mas 100

def crecimientoDeAlgas(dias):
    cant = None
    if dias > 0:
        if dias == 1 :
            cant = 12
        elif 1 < dias <= 12:
            cant = crecimientoDeAlgas(dias -1 ) + 15
        else:
            cant = crecimientoDeAlgas(dias -1) * 3 + 100
    else:
        raise Exception('dias ivalido')
    return cant



# ejercio 8
# recursiva que calcula la potencia de N de un numero M
# n = exponente
#m = numero

def potencia(n,m):
    res = None
    if n >= 0:
        if n == 0:
            res = 1
        else:
            res = m * potencia(n-1,m)
    else:
        raise Exception('numero no entero')
    return res


# ejercio 9
# resolve cuanto granos hay en un tablero de ajedrez
# un grano en el primero, 2 en el segundo y asi sucesivamente

def granosEnCasillero(nroCasillero):
    cant = None
    if nroCasillero > 0 :
        if nroCasillero == 1:
            cant = 1
        else :
            cant = granosEnCasillero(nroCasillero - 1) * 2
    else:
        raise Exception('numero no valido')

    return cant
def  granosTotalEnTablero(casilleros):
    cant: None
    if casilleros > 0:
        if casilleros == 1:
            cant = granosEnCasillero(casilleros)
        else:
            cant = granosEnCasillero(casilleros) + granosTotalEnTablero(casilleros -1)
    else:
        raise Exception(' no valido')
    return cant

# ejercio 10
# calcular la cantidad de cucarachas en el edificio
# primer piso = 1 cucaracha
# en piso pares doble del numero de piso ( piso 2 = 4 cucas)
# pisos impares la suma de los 2 pisos anteriores

def cucasEnPiso(piso):
    cant = None
    if piso > 0:
        if piso == 1:
            cant = 1
        elif piso % 2 == 0:
            cant = piso * 2
        else:
            cant = cucasEnPiso(piso-2) + cucasEnPiso(piso -1)
    else:
        raise Exception('')
    return cant

def cantiCucaEnEdificio(nroPisos):
    cant = None
    if nroPisos > 0:
        if nroPisos == 1:
            cant = cucasEnPiso(nroPisos)
        else:
            cant = cucasEnPiso(nroPisos) + cantiCucaEnEdificio(nroPisos -1)
    else:
        raise Exception('piso no valido')
    return cant
