from random import randint
from time import sleep
# Computador escolhe um número
computador = randint(0, 10)
print('-=-' * 25)
print('Vamos jogar um jogo? Estou pensando em um número inteiro de 1 a 10.')
print('-=-' * 25)
# Jogador tenta advinhar
jogador = int(input('Qual número você acha que é? '))
print('Processando')
sleep(2)
cont = 1
while computador != jogador:
    if computador > jogador:
        jogador = int(input('Um pouco mais... Tente de novo. '))
        cont += 1
        print('Processando')
        sleep(2)
    else:
        jogador = int(input('Um pouco menos... Tente de novo. '))
        cont += 1
        print('Processando')
        sleep(2)
print(f'Parabéns, você acertou! O número era {computador} e você levou {cont} tentativas para descobrir.')
