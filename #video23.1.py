#video23.1
import math
def calcularaiz(num1):
    if num1<0:
        raise ValueError ('el numero no puede ser negativo')
    else :
        return math.sqrt(num1)
op1=(int(input('introduce un numero:')))

try:
    print(calcularaiz(op1))
    
except ValueError as errordenumeronegativo:
    print(errordenumeronegativo)    

print('programa terminado')
