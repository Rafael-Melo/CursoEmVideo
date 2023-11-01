from random import randint
from time import sleep
numeros = []
def sorteia():
    print('Sorteando os valores: ', end='')
    sleep(1)                            
    for i in range(0, 5):
        i = (randint(0, 10))
        numeros.append(i)
        print(i, end=' ')
        sleep(0.5)
    print('PRONTO!')


def somaPar():
    soma = 0
    for n in numeros:
        if n % 2 == 0:
            soma += n
    print(f'A soma dos números pares de {numeros} é {soma}.')


# Programa Principal
sorteia()
somaPar()
