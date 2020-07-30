from nodoABB import*

class ABB:

    def __init__(self, entrada = None):
        
        self.raiz = None
        if entrada:
            for e in entrada:
                self.insertar(e)

    def estaVacio(self):

       return  self.raiz == None

    def insertar(self, dato):
        nuevoNodo = NodoArbol(dato)
        if self.estaVacio():
            self.raiz = nuevoNodo
        else:
            self.raiz.insertar(nuevoNodo)

# imprime el dato al entrar al nodo
    def preOrden(self):
        if not self.estaVacio():
            self.raiz.preOrden()
        else:
            print('arbol vacio')


# impreme el dato a la vuelta

    def posOrden(self):
        if not self.estaVacio():
            self.raiz.posOrden()
        else:
            print('arbol vacio')

#imprime en orden

    def inOrden(self):
        if not self.estaVacio():
            self.raiz.inOrden()
        else:
            print('arbol vacio')


arbol = ABB([30,20,70,25,55,6,75,14,3,19,22,66,80])
print(arbol.estaVacio())
arbol.inOrden()
