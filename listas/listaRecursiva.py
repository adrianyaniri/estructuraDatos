from nodo import*

class Lista:

    def __init__(self):

        self.primero = None

    def estaVacia(self):

        return self.primero == None

    def __repr__(self):
        
        out = 'primero'
        aux = self.primero
        while aux !=None:
            out += ' -> ' + str(aux.dato)
            aux = aux.siguiente
        out += ' |'
        return out

    def append(self,dato ):
        nuevoNodo = Nodo(dato)
        if self.estaVacia():
            self.primero = nuevoNodo
        else:
            self.primero.append(nuevoNodo)


# recorrido en preOrden

    def recPre(self):
        if not self.estaVacia():
            self.primero.recPre()
        else:
            raise Exception('lista vacia')

# recorrido pos Orden

    def recPos(self):
        if not self.estaVacia():
            self.primero.recPos()
        else:
            raise Exception('lista vacia')


# tamanio de la lista

    def len(self):
        cantidad = 0
        if not self.estaVacia():
           cantidad =  self.primero.len()
        else:
            raise Exception('lista vacia')
        return cantidad

    # obtener el dato de la posicion pasada por parametro

    def getDato(self, pos):
        if not self.estaVacia():
            dato = None
            if 0 <= pos < self.len():
                dato =  self.primero.getDato(pos)
            else:
                raise Exception('posicion invalida')
        else:
            raise Exception ('lista vacia')
        return dato


    # eliminar elemento de posicion pasada por parametro

    def delete(self,pos):
        if not self.estaVacia():
            if 0 <= pos < self.len():
                if pos == 0:
                    self.primero = self.primero.siguiente
                else:
                    self.primero.delete(pos)
            else:
                raise Exception('posicion no valida')
        else:
            raise Exception('lista vacia')
        

    def reemplazar(self, nuevo, viejo):
        if not self.estaVacia():
            self.primero.reemplazar(nuevo, viejo)
        else:
            raise Exception('lista vacia')

#clonar lista

    def clonar(self):
        lista = Lista()
        if not self.estaVacia():
            self.primero.clonar(lista)
        else:
            raise Exception('lista vacia')
        return lista




l = Lista()

l.append('hola')
l.append(5)
l.append(20)
l.append('mundo')

print(l)
l.reemplazar(4,'mundo')
print(l)
l2 = l.clonar()
print(l2)