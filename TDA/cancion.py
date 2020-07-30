from enum import Enum
from tiempo import*
# moldear un TDA cancio
# estructura nombre cancion , nombre artista, duracion , genero, anio edicion, likes
# genero pueden ser rock , jazz, blues, funk, reagge y rap

class Genero(int, Enum):
    rock = 1
    jazz = 2
    blues = 3
    funck = 4
    reagge = 5
    rap = 6

class Cancion:

    def __init__(self, nombre = None, artista = None, duracion = None, genero = Genero.rock,anio = None, likes = None):
        self.nombre = nombre
        self.artista = artista
        self.duracion = duracion
        self.genero = genero
        self.anio = anio
        self.linkes = likes

    def __repr__(self):
        string = 'nombre: ' + str(self.nombre)+ '-' + 'artista: ' + str(self.artista) + ' (' + str(self.duracion) + ')'+'\n' + 'genero: ' + str(self.genero.name)
        return string

# funcion que recibe 2 canciones y retorna la mas vota
    def mayorDuracion(self, cancion):
        mayor = None
        if self.duracion > cancion.duracion:
            mayor = self
        else:
            mayor = cancion
        return mayor
    # function que obtiene la cantidad de likes de una cancion
    def getLikes(self):
        return self.linkes

    # opercaion que agrega liks a la cancion

    def setLikes(self,cantidad):
        self.linkes = self.linkes + cantidad

    # opercion que recibe 2 canciones compara si son del mismo artista y Genero
    # retorna la que tiene mayor de linkes

    def masVotada(self, cancion):
        mayor = None
        if self.genero == cancion.genero and self.artista == cancion.artista:
            if self.linkes > cancion.linkes:
                mayor = self
            else:
                mayor = cancion
        else:
            raise Exception('no se pueden comparar las canciones')
        return mayor





cancion1 = Cancion('hola','fito',Tiempo(0,5,10),Genero.rock,2010,2000)
cancion2 = Cancion('chau','fito', Tiempo(0,3,52),Genero.rap, 2015,5000)
