from random import randint
from time import sleep
jogo = []
lista = []
cont = 0
print('-' * 52)
print(f'{"JOGO DA MEGA":^52}')
print('-' * 52)
sorteio = int(input('Quantos jogos você quer? '))
for i in range(0, sorteio):
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogo.append(lista[:])
    lista.clear()
    cont = 0
print('-=' * 8, f' SORTEANDO {sorteio} JOGOS ', '=-' *8)
for i, l in enumerate(jogo):
    print(f'JOGO {i+1}: {l}')
    sleep(1)
print('-=' * 9, f' < BOA SORTE > ', '=-' *9)
