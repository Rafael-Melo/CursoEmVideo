from random import randint
from time import sleep
v = 0
print('Vamos jogar par ou ímpar!')
while True:
    pc = randint(0, 10)
    jogador = int(input('Digite um valor: '))
    soma = pc + jogador
    res = ' '
    while res not in 'PI':
        res = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'O computador jogou {pc} e você jogou {jogador}. Total deu {soma}.')
    sleep(1)
    print('DEU PAR!' if soma % 2 == 0 else 'DEU ÍMPAR!')
    if res == 'P':
        if soma % 2 == 0:
            print(f'Você venceu!')
            v +=1
            sleep(1)
        else:
            print(f'Você perdeu!')
            sleep(1)
            break
    elif res == 'I':   
        if soma % 2 == 1:
            print(f'Você venceu!')
            v +=1
            sleep(1)
        else:
            print(f'Você perdeu!')
            sleep(1)
            break
    print('Vamos jogar novamente!')
print(f'GAME OVER!!! Você venceu {v} vezes!')
