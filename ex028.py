import random

n = random.randint(0, 10)

print('Vamos jogar um jogo? Estou pensando em um número inteiro de 1 a 100.')

chute = int(input('Qual número você acha que é? '))

if chute == n:
    print(f'Parabéns, você acertou! O número era {n}.')
else:
    print(f'Que pena, você errou. O número era {n}.')
