#video22.1-excepciones

def divide():
    try:
        op1=(float(input('introdce el primer numero')))
        op2=(float(input('introduce el segundo nuero')))
        print('la division es: ' + srt(op1/op2))
    except ValueError:    
        print('el valor introducido es erroneo')
    except ZeroDivisionError:
        print('no se puede dividir en cero')
    finally:    
    print('calculo finalizado')    

divide()    