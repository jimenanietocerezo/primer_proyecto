#video26-poo3
class Coche():
    #propiedades
    largoChasis=250
    anchoChasis=120
    ruedas=4
    enmarcha=False

#metodo para comportamiento, metodo es una funcion de la clase
    def arrancar(self):
        self.enmarcha=True
    def estado(self):
        if (self.enmarcha):
            return'el coche esta en marcha'
        else:
            return'el coche esta parado'        

miCoche=Coche() #isntanciar una clase
print(miCoche.largoChasis)
print('el coche tiene', miCoche.ruedas, 'ruedas')
miCoche.arrancar()
print(miCoche.estado())
