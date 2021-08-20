#video23-excepciones3
def evaluaedad(edad):
    if edad<0:
        raise TypeError('no se permiten edades negativas')
    if edad<20:
        return'eres muy joven'
    elif edad<40:
        return'eres maduro'
    elif edad<100:
        return'cuidate...'
print(evaluaedad(15))    
