from random import randint
from time import sleep

#Computador escolhe um número
c = randint(1,3)

print('-=-' * 25)

j = int(input('''Vamos jogar Jokenpô!
Escolha:
(1) Pedra
(2) Papel         
(3) Tesoura
'''))

print('-=-' * 25)

print('Joooo')
sleep(1)
print('Keeeeen')
sleep(1)
print('Pô!')
sleep(1)

if c == 1:
    if j == 1:
        print("Pedra X Pedra! Empate!")
    elif j == 2:
        print("A Pedra é embrulhada pelo Papel! Você vencêu!")
    elif j == 3:
        print("A Pedra quebra a Tesoura! Você perdeu!")

if c == 2:
    if j == 1:
        print("O Papel embrulha a Pedra! Você perdeu!")
    elif j == 2:
        print("Papel X Papel! Empate!")
    elif j == 3:
        print("O Papel é cortado pela Tesoura! Você venceu!")

if c == 3:
    if j == 1:
        print("A Tesoura é quebrada pela Pedra! Você venceu!")
    elif j == 2:
        print("A Tesoura corta o Papel! Você perdeu!")
    elif j == 3:
        print("Tesoura X Tesoura! Empate!")

print(c)
