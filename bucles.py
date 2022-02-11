# Imprimir todas las potencias de 2 hasta que el resultado sea menor que 1000
import time

LIMITE = 1000
counter = 0
potencia_2 = 2 ** counter

while potencia_2 < LIMITE:
    print(f'2 elevado a la {counter} = {potencia_2}')
    counter +=1
    potencia_2 = 2 ** counter
    time.sleep(.5)