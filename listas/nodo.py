
class Nodo:

    def __init__(self, dato):

        self.dato = dato
        self.siguiente = None

    def tieneSiguiente(self):

        return self.siguiente != None

    def append(self,nuevoNodo):
        if self.tieneSiguiente():
            self.siguiente.append(nuevoNodo)
        else:
            self.siguiente = nuevoNodo

# recorrido en pre Orden

    def recPre(self):
        print(self.dato)
        if self.tieneSiguiente():
            self.siguiente.recPre()

# recorrdio en pos orden

    def recPos(self):
        if self.tieneSiguiente():
            self.siguiente.recPos()
        print(self.dato)

# tamanio de la lista

    def len(self):
        cantidad = 1
        if self.tieneSiguiente():
            cantidad += self.siguiente.len()
        return cantidad

    
    def getDato(self, pos,posAct = 0):
        dato = None
        if posAct == pos:
            dato = self.dato
        else:
            dato = self.siguiente.getDato(pos, posAct +1)

        return dato



    def delete(self, delPos, actPos = 0):
        if actPos == delPos-1:
            self.siguiente = self.siguiente.siguiente
        else:
            self.siguiente.delete(delPos, actPos+1)



    def reemplazar(self,nuevo, viejo):
        if self.dato == viejo:
            self.dato = nuevo

        if self.tieneSiguiente():
            self.siguiente.reemplazar(nuevo, viejo)

    def clonar(self, lista):
        lista.append(self.dato)
        if self.tieneSiguiente():
            self.siguiente.clonar(lista)