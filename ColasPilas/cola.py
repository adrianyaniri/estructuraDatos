
class Cola():

    def __init__(self):
        self.cola = []

    def vaciar(self):
        self.cola.clear()
    
    def queue(self,item):
        self.cola.append(item)

    def deQueue(self):
        dato = None
        if not self.noEstaVacia():
            dato = self.cola.pop()
        else:
            raise Exception('cola vacia')

    def top(self):
        dato = None
        if not self.estaVacia():
            dato = self.cola[len(self)-1]
        else:
            raise Exception('cola vacia')
        return dato

    def estaVacia(self):
        return len(self.cola) == 0

    def vacia(self):
        return self.cola.clear()

    def __repr__(self):
        return str(self.cola)


cola = Cola()
cola.queue(5)
print(cola)