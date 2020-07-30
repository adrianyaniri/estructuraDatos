from graphviz import Digraph

class NodoArbol:

    def __init__(self, dato):

        self.dato = dato
        self.izquierdo = None
        self.derecho = None

    def tieneIzquierdo(self):

        return self.izquierdo != None

    def tieneDerecho(self):

        return self.derecho != None

    def esHoja(self):

        return not self.tieneDerecho() and not self.tieneIzquierdo()

    def insertar(self, nuevoNodo):
        
        if self.dato == nuevoNodo:
            print('ya existe el dato')
        elif nuevoNodo.dato < self.dato:
            if self.tieneIzquierdo():
                self.izquierdo.insertar(nuevoNodo)
            else:
                self.izquierdo = nuevoNodo

        else:
            if self.tieneDerecho():
                self.derecho.insertar(nuevoNodo)
            else:
                self.derecho = nuevoNodo


# impreme el dato al entrar al nodo
    def preOrden(self):
        print(self.dato)
        if self.tieneIzquierdo():
            self.izquierdo.preOrden()
        if self.tieneDerecho():
            self.derecho.preOrden()


# imprime el dato a la vuelta del recorrido

    def posOrden(self):
        if self.tieneIzquierdo():
            self.izquierdo.posOrden()
        if self.tieneDerecho():
            self.derecho.posOrden()
        print(self.dato)

# imprime en orden 

    def inOrden(self):
        if self.tieneIzquierdo():
            self.izquierdo.inOrden()
        print(self.dato)
        if self.tieneDerecho():
            self.derecho.inOrden()
