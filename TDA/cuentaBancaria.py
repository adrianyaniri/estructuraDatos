# TDA que moldea una cuenta bancaria
# estructura nro de cuenta , dni titular, saldo de cta, interes anual

class Cuenta:
    def __init__(self, nroCta, dni, saldo, interesAnual):

        self.nroCta = nroCta
        self.dni = dni
        self.saldo =saldo
        self.interesAnual = interesAnual

    def __str__(self):
        string = 'numero de cuenta: ' + str(self.nroCta) +' \n'+ 'titular: ' + str(self.dni) +'\n' + 'saldo: $' + str(self.saldo)
        return string
    # function que actualiza el saldo actual

    def actualizarSaldo(self):
        interesDiario = self.interesAnual / 365
        saldoAct = round(self.saldo * interesDiario + self.saldo,2)
        self.saldo = saldoAct

    # ingresa un monto al saldo
    def ingresarDinero(self,monto):
        self.saldo = self.saldo + monto

    # function que retira dinero de la Cuenta
    # si el saldo es insuficiente lanza Exception

    def extraerDinero(self, monto):
        if self.saldo >= monto:
            self.saldo = self.saldo - monto
        else:
            raise Exception('fondo insuficiente')

cuenta = Cuenta(120,28528339,1500,5)
