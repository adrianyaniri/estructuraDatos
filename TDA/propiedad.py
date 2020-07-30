# moldear un TDA propiedad
# debe estar estructurado con una calle,numero, localidad, anio de constriccion y cantidad de ambientes

class Propiedad:
    # constructor
    def __init__(self, calle,nro, localidad, anioConst, ambientes):
        self.calle = calle      # string nombre de la calcule
        self.nro = nro      # int
        self.localidad = localidad      #string
        self.anioConst = anioConst      # int
        self.ambientes = ambientes       # int

# representacion
    def __repr__(self):
        string = 'direccion: '+ self.calle + ' '+ str(self.nro)+'\nlocalidad: ' + self.localidad
        return string

    # function recibe por prametro una propiedad
    # y retorna si tiene la misma localidad

    def mismaLocalidad(self,pro):
        return self.localidad == pro.localidad

    # function que retorna si estan en la mima calle
    # rebice por parametro una prpiedad y compara cual tiene mayor numeracion

    def mayorNumeracion(self,pro):
        mayor = None
        if self.calle == pro.calle:
            if self.nro > pro.nro:
                mayor = self
            else:
                mayor = pro
        else:
            raise Exception('no estan en la misma calle')
        return mayor

    def getAnioConst(self):
        return self.anioConst

    #calcula el impuesto aprobado
    # propiedad anio entre 1870-1949
    #1-3 ambientes 5%
    #4-6 ambientes 10%
    # + 6 ambientes 25%
    # priedad desde anio 1950
    # 1-5 ambientes 5%
    #+ 6 ambientes 35%

    def calcularARBA(self):
        impuesto = None
        if self.getAnioConst() >= 1870 and self.getAnioConst() <= 1949:
            if  self.ambientes <=3:
                impuesto = 5
            elif self.ambientes >=4 and self.ambientes <=6:
                impuesto = 10
            else:
                impuesto = 25
        else:
            if self.ambientes <=5:
                impuesto = 5
            else:
                impuesto = 35
        return impuesto

propiedad1 = Propiedad('gibraltar', 1051, 'hurlingham',1949,8)
propiedad2 = Propiedad('gibraltar',1061,'hurlingham', 2010,6)
propiedad3 = Propiedad('granada',1051,'stoTeseis',1990,3)

print(propiedad1.calcularARBA())
