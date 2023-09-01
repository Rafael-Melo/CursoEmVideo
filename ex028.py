from random import randint
from time import sleep

# Computador escolhe um número
n = randint(0, 10)

print('-=-' * 25)

print('Vamos jogar um jogo? Estou pensando em um número inteiro de 1 a 10.')

print('-=-' * 25)

# Jogador tenta advinhar
chute = int(input('Qual número você acha que é? '))

print('Processando')

sleep(2)

if chute == n:
    print(f'Parabéns, você acertou! O número era {n}.')
else:
    print(f'Que pena, você errou. O número era {n}.')
