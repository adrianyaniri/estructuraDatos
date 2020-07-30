# TDA que moldea un sorteo de quiniela
# estructurado con primer y segundo premio , multplicador(cantidad a pagar por apostado)

class Quiniela():

    def __init__(self, firstNum = 0,secondNum = 0, pay = 0):
        if firstNum > 0 and firstNum < 99:
            self.firstNum = firstNum
        else:
            raise Exception('numero no permitido')
        if secondNum > 0 and secondNum< 99:
            self.secondNum = secondNum
        else:
            raise Exception('numero no permitido')

        if pay <= 1000:
            self.pay = pay
        else:
            raise Exception('apuesta accedida ')

    # funtion repersentacion
    def __repr__(self):
        string = 'primer numero ganador: ' + str(self.firstNum) + '\n' + 'segundo numero ganador: ' +str(self.secondNum) +'\n'+ 'paga X: $' + str(self.pay)
        return string

    # funtion recibe por parametro un numero y retorna si es el ganador o no

    def esGanador(self,nro):
        return self.firstNum == nro or self.secondNum == nro

    # funtion que retorna el importe a pagar
    # recibe por parametro un numero y un importe apostado
    # se no es el sorteado devuelve 0
    # primer numero paga x pay, segundo premio paga pay/2

    def importeAPagar(self,nro,apuesta):
        pagar = None
        if self.esGanador(nro)  or  apuesta < 1000:
            if self.firstNum == nro:
                pagar = apuesta * self.pay
            elif self.secondNum == nro:
                pagar = apuesta * (self.pay /2)
            else:
                pagar = 0
        else:
            raise Exception('apuesta maxima')
        return pagar

    # retorna True si los numero premiado esta a menos de 10 de distancia

    def premiosCercanos(self):
        return abs(self.firstNum - self.secondNum) >= 10


sorteo = Quiniela(22,15,70)
