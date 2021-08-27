#video28 poov encapsulamiento
class Coche():
    def __init__(self):
    
    # 4propiedades
    #se encapcula de acuerdo a las necesidades que tengo, es decir si quiero que solo funcione como lo determino lo tengo que encapsular, si no
        self.__largoChasis=250
        self.__anchoChasis=120
        self.__ruedas=4
        self.__enmarcha=False

#metodo para los 2 comportamiento, metodo es una funcion de la clase/uno para cambiar el arranque otro para mostrar el estado del objeto
    def arrancar(self,arrancamos):
        self.__enmarcha=arrancamos

        if(self.__enmarcha):
            chequeo=self.__chequeo_interno()

        if(self.__enmarcha and chequeo):
            return 'el coche esta en marcha'

        elif(self.__enmarcha and chequeo==False):
            return'algo a salido mal en el chequeo no podemos arrancar'  

        else:
            return 'el coche esta parado'     

    def estado(self):
        print('el coche tiene',  self.__ruedas, 'ruedas. un ancho de', self.__anchoChasis, 'y un largo de',self.__largoChasis)   

    def __chequeo_interno(self):
        print('realizando chequeo interno')

        self.gasolina='ok'
        self.aceite='ok'
        self.puertas='cerradas'

        if(self.gasolina=='ok' and self.aceite=='ok'and self.puertas=='cerradas'):
            return True
        else:
            return False




miCoche=Coche() #isntanciar una clase
print(miCoche.arrancar(True))
miCoche.estado()


print('------------a continuacion creamos el segundo objeto---------------')


miCoche2=Coche()
print(miCoche2.arrancar(False))
#miCoche2.ruedas=2
#para evitar este mod de propeidad se debe encapsular la propiedad de ruedas, se coloca doble guion bajo, por mas que la quiero modf con el encapsulamiento no me deja
miCoche2.estado()