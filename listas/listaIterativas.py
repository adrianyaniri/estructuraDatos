#constructor de lista y nodo

class Nodo:
    def __init__(self, data):
        self.sig = None
        self.data = data

    def tieneSiguiente(self):
        return self.sig != None


class Lista:
    def __init__(self):
        self.primero = None

    def vaciar(self):
        self.primero = None

    def isEmpty(self):
        return self.primero == None

    def len(self):
        cant = 0
        nodoAux = self.primero
        while nodoAux !=None:
            cant +=1
            nodoAux = nodoAux.sig
        return cant

    def append(self,item):
        nodoNuevo = Nodo(item)
        if self.isEmpty():
            self.primero = nodoNuevo
        else:
            nodoAux = self.primero
            while nodoAux.tieneSiguiente():
                nodoAux = nodoAux.sig
            nodoAux.sig = nodoNuevo

    def insertar(self,pos , item):
        if pos >= 0:
            nodoNuevo = Nodo(item)
            if self.isEmpty():
                self.primero = nodoNuevo
            elif pos == 0:
                nodoNuevo.sig = self.primero
                self.primero = nodoNuevo
            elif pos < self.len():
                posAux = 0
                nodoAux = self.primero
                while posAux < pos - 1:
                    nodoAux = nodoAux.sig
                    posAux +=1
                nodoNuevo.sig = nodoAux.sig
                nodoAux.sig = nodoNuevo
            else:
                self.append(item)
        else:
            raise Exception('posicion no valida')

    def getElemento(self,pos):
        item = None
        if 0 <= pos < self.len():
            nodoAux = self.primero
            posAux = 0
            while posAux < pos:
                posAux +=1
                nodoAux = nodoAux.sig
            item = nodoAux.data
        else:
            raise Exception('posicion no valida')


        return item

    def eliminar(self, posDel):
        if not self.isEmpty() and 0 <= posDel < self.len():
            if posDel == 0:
                self.primero = self.primero.sig
            else:
                aux = self.primero
                posAux = 0
                while posAux < posDel -1:
                    posAux +=1
                    aux = aux.sig
                aux.sig = aux.sig.sig
        else:
            if self.isEmpty():
                raise Exception('lista vacia')
            else:
                raise Exception('posicion no valida')


    def clonar(self):
        nuevaList = Lista()
        nodoAux = self.primero
        while nodoAux != None:
            nuevaList.append(nodoAux.data)
            nodoAux = nodoAux.sig
        return nuevaList


    def __repr__(self):
        strOut = 'primero'
        aux = self.primero
        while aux != None:
            strOut += '-> ' + str(aux.data)
            aux = aux.sig
        strOut += ' |'
        return strOut

# ejercio 2 intercambia los 2 primeros nodos
class Lista(Lista):
    def interCambiar(self):
        if self.len() >= 2:
            nodoAux = self.primero
            self.primero = nodoAux.sig
            nodoAux.sig = self.primero.sig
            self.primero.sig = nodoAux
        else:
            raise Exception('')


# ejercico 3
# buscar elemento pasado por parametro
# retornar lista con los posiciones donde se encuentra el elemento

class Lista(Lista):

    def buscarElemento(self, item = None):
        if not self.isEmpty():
            listElem = Lista()
            pos = 0
            nodoAux = self.primero
            while nodoAux.tieneSiguiente():
                if nodoAux.data == item:
                    listElem.append(pos)
                pos += 1
                nodoAux = nodoAux.sig
            if nodoAux.data == item:
                listElem.append(pos)
        else:
            raise Exception('lista vacia')

        return listElem         # falta verificar cuando el elemento buscado no esta en la lista

# ejercicio 4
# eliminar Ocurrencia pasadas por parametro
# retorna la cantidad de veces q se borro

class Lista(Lista):
    def eliminarOcu(self,item = None):
        cant = 0
        if not self.isEmpty():
            while not self.isEmpty() and self.primero.data == item:
                cant +=1
                self.primero = self.primero.sig 
            if not self.isEmpty():
                nodoAux = self.primero
                while nodoAux.tieneSiguiente():
                    if nodoAux.sig.data == item:
                        cant +=1
                    nodoAux = nodoAux.sig 
        else:
            raise Exception('lista vacia')
        return cant


# ejercicio 5
# sacar el nodo de la pos 0 y llevarlo a la ultima posicion

class Lista(Lista):

    def primeroAlFinal(self):
        nodoAux = self.primero
        while nodoAux.tieneSiguiente():
            nodoAux = nodoAux.sig
        nodoAux.sig.sig = self.primero
        self.primero = self.primero.sig
            
            
        
            
#ejewrcico 6
# reemplaza las ocurrencia por otro numero
# los numero son pasdado por parametro

class Lista(Lista):
    def reemplazar(self, nOcu = 0, nRem = 0):
        if not self.isEmpty():
            nodoAux  = self.primero
            while nodoAux != None:
                if nodoAux.data == nOcu:
                    nodoAux.data = nRem
                nodoAux = nodoAux.sig 
        else:
            raise Exception('lista vacia')


# ejercicio 7
# duplicar lista

class Lista(Lista):
    def duplicarLista(self):
        nodoAux = self.primero
        while nodoAux.sig != None:
            nodoAux = nodoAux.sig 
        nodoAux.sig = self.primero


# ejercicio 8
#         
class Lista(Lista):
    def recorridoSalteado(self):
        if not self.isEmpty():
            nodoAux = self.primero
            while nodoAux.tieneSiguiente():
                print(nodoAux.data)
                nodoAux = nodoAux.sig.sig
            print(nodoAux.data)
        else:
            raise Exception('lista vacia')
        

# ejercicio 9

class Lista(Lista):
    def recorridoParImpar(self):
        if not self.isEmpty():
            nodoAux = self.primero
            while nodoAux.tieneSiguiente():
                if nodoAux.data % 2 == 0:
                    print(nodoAux.data)
                    nodoAux = nodoAux.sig
                else:
                    print(nodoAux.data)
                    nodoAux = nodoAux.sig.sig
            print(nodoAux.data)
        else: 
            raise Exception('lista vacia')


# ejercicio 10

class Lista(Lista):
    def multiplicarMayores(self, numero, multi):
        if not self.isEmpty():
            nodoAux = self.primero
            while nodoAux.tieneSiguiente():
                if nodoAux.data <= numero:
                    nodoAux = nodoAux.sig
                else:
                    nodoAux.data *= multi
                    nodoAux = nodoAux.sig
            if nodoAux.data >= numero:
                nodoAux.data *= multi
            
        else:
            raise Exception('lista vacia')

# ejercicio 11

class Lista(Lista):
    def reemplazarPos(self, pos, numero):
        posActual = 0
        if pos == 0:
            self.primero.data = numero
            self.primero = self.primero.sig

        nodoAux = self.primero

        while pos == posActual:
            if pos== posActual:
                nodoAux.data = numero
                nodoAux = nodoAux.sig
            posActual +=1

    def posicion(self,pos):
        nodo = None
        aux = self.primero
        if pos == 0:
            pos = 0
        else:
            while aux.sig != None:
                pos +=1
                
        return pos

l = Lista()
l.append(0)
l.append(1)
l.append(2)
l.append(3)
l.append(4)
l.append(5)
l.append(6)
l2 = Lista()

print(l)
print(l.posicion(1).data)
