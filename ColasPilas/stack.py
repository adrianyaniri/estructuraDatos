

class Stack:

    def __init__(self):
        self.pila = []

    def vaciar(self):
        self.pila.clear()

    def push(self, item):
        self.pila.append(item)

    def pop(self):
        pop = None
        if not self.estaVacia():
            pop = self.pila.pop()
        else:
            raise Exception('pila vacia')
        return pop

    def top(self):
        dato = None
        if not self.estaVacia():
           dato =  self.pila[len(self.pila)-1]
        else:
            raise Exception('pila vacia')
        return dato

    def clonar(self):
        clon = Stack()
        for e in self.pila:
            clon.push(e)
        return clon

    def len(self):
        return len(self.pila)
    
    def estaVacia(self):
        return len(self.pila) == 0

    def __repr__(self):
        return str(self.pila)




pila = Stack()
pila.push(5),pila.push(1), pila.push(2), pila.push(3),pila.push(4),pila.push(5),pila.push(5)


#inverite la pila que resive por parametro

def invertirPila(pila):
    aux = pila.clonar()
    pila.vaciar()
    while not aux.estaVacia():
        pila.push(aux.pop())


def ultimoAPrimero(pila):
    aux = pila.clonar()
    pila.vaciar()
    while not aux.estaVacia():
        pila.push(aux.pop())
    top = pila.pop()
    invertirPila(pila)
    pila.push(top)



#coloca un elemento al fondo de la pila

def pushFondo(pila,elemento):
    aux = pila.clonar()
    pila.vaciar()
    while not aux.estaVacia():
        pila.push(aux.pop())
    pila.push(elemento)
    invertirPila(pila)


# eliminar la ocurrencia de la pila
# elemento pasado por parametro

def eliminarOcurencia(pila, elemento):
    aux = pila.clonar()
    pila.vaciar()
    while not aux.estaVacia():
        if aux.top() != elemento:
            pila.push(aux.pop())
        else:
            aux.pop()
    invertirPila(pila)


# duplica la pila pasada por parametro

def duplicarPila(pila):
    aux = pila.clonar()
    invertirPila(aux)
    while not aux.estaVacia():
        pila.push(aux.pop())


# pila 1 =  8 5 6 9 9 6 2 5 
# pila 2 =  7 5 4 2 6 6 5 2 
# pila res = 1 6 1 1 2 6 7 7

pila1 = Stack()
pila2 = Stack()

pila1.push(8), pila1.push(5), pila1.push(6), pila1.push(9), pila1.push(9), pila1.push(6), pila1.push(2), pila1.push(5)
pila2.push(7), pila2.push(5), pila2.push(4), pila2.push(2), pila2.push(6), pila2.push(6), pila2.push(7), pila2.push(7)


def sumarDigitos(pila1, pila2):
    aux1 = pila1.clonar()
    aux2 = pila2.clonar()
    res = Stack()
    resto = 0
    while not aux1.estaVacia() and not aux2.estaVacia():
        suma = aux1.pop() + aux2.pop() + resto
        resto = suma // 10
        res.push(suma % 10)
    if resto:
        res.push(resto)
        invertirPila(res)
    return res



print(sumarDigitos(pila1,pila2))
