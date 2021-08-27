#video 27 pooiv
class Coche():
    def __init__(self):
    
    # 4propiedades
        self.__largoChasis=250
        self.__anchoChasis=120
        self.__ruedas=4
        self.__enmarcha=False

#metodo para los 2 comportamiento, metodo es una funcion de la clase
    def arrancar(self,arrancamos):
        self.enmarcha=arrancamos

        if(self.__enmarcha):
            return 'el coche esta en marcha'
        else:
            return 'el coche esta parado'     
    def estado(self):
        print('el coche tiene',  self.__ruedas, 'ruedas. un ancho de', self.__anchoChasis, 'y un largo de',self.__largoChasis)   


miCoche=Coche() #isntanciar una clase
print(miCoche.arrancar(True))
miCoche.estado()


print('------------a continuacion creamos el segundo objeto---------------')


miCoche2=Coche()
print(miCoche2.arrancar(False))
miCoche2.ruedas=2
#para evitar este mod de propeidad se debe encapsular la propiedad de ruedas, se coloca doble guion bajo, por mas que la quiero modf con el encapsulamiento no me deja
miCoche2.estado()