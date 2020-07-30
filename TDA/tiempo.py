# moldea un TDA tiempo
# validar horas, minutos y segundo

class Tiempo:

    def __init__(self, horas, minutos,segundos):

        if horas >= 0 and horas <=24:
            self.horas = horas
        else:
            raise Exception('hora no valida')

        if minutos >= 0 and minutos <=60:
            self.minutos = minutos
        else:
            raise Exception('minutos invalidos')

        if segundos >= 0 and segundos <= 60:
            self.segundos = segundos
        else :
            raise Exception('segundo invalidos')

    def __repr__(self):
        string = 'horas: ' + str(self.horas) +' \n'+ 'minutos: '+ str(self.minutos)+ ' \n'+ 'segundos: ' + str(self.segundos)
        return string


    def __gt__(self,tiempo):
        return self.pasarASegundos() > tiempo.pasarASegundos()

    # function que recibe por parametro un tiempo y lo pasa a segundos

    def pasarASegundos(self):
        horasAMinutos = self.horas *60
        return (horasAMinutos + self.minutos) * 60

# recibe por parametro segundos y lo retorna en TDA tiempo
    def tiemposDesdeSegundos(self,segundos):
        if segundos >=60:
            minutos = segundos // 60
            segundos %= 60
        if minutos >= 60:
            horas = minutos // 60
            minutos %= 60
        tiempo = Tiempo(horas, minutos, segundos)

        return tiempo

    #recibe por parametro un Tiempo y retorna el de mayor duracion

    def mayorTiempo(self,tiempo):
        mayor = None
        if self.pasarASegundos() > tiempo.pasarASegundos():
            mayor = self
        else:
            mayor = tiempo
        return mayor

hora = Tiempo(1,0,0)
hora2 = Tiempo(2,0,0)
