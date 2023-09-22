from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')

#Computador escolhe um número
c = randint(1,3)

print('-=-' * 25)

j = int(input('''Vamos jogar Jokenpô!
Escolha:
[0] Pedra
[1] Papel         
[2] Tesoura\n
'''))

print('-=-' * 25)

print('Joooo')
sleep(1)
print('Keeeeen')
sleep(1)
print('Pô!')
sleep(1)

print('-=-' * 25)

if c == 0:
    if j == 0:
        print(f"O computador escolheu \033[35m{itens[0]}\033[m!")
        print(f"\033[35m{itens[0]}\033[m X \033[35m{itens[0]}\033[m! Empate!")
    elif j == 1:
        print(f"O computador escolheu \033[35m{itens[0]}\033[m!")
        print(f"A \033[35m{itens[0]}\033[m é embrulhada pelo \033[36m{itens[1]}\033[m! Você vencêu!")
    elif j == 2:
        print(f"O computador escolheu \033[35m{itens[0]}\033[m!")
        print(f"A \033[35m{itens[0]}\033[m quebra a \033[34m{itens[2]}\033[m! Você perdeu!")
    else:
        print('\033[1;31mJogada inválida\033[m')

elif c == 1:
    if j == 0:
        print(f"O computador escolheu \033[36m{itens[1]}\033[m!")
        print(f"O \033[36m{itens[1]}\033[m embrulha a \033[35m{itens[0]}\033[m! Você perdeu!")
    elif j == 1:
        print(f"O computador escolheu \033[36m{itens[1]}\033[m!")
        print(f"\033[36m{itens[1]}\033[m X \033[36m{itens[1]}\033[m! Empate!")
    elif j == 2:
        print(f"O computador escolheu \033[36m{itens[1]}\033[m!")
        print(f"O \033[36m{itens[1]}\033[m é cortado pela \033[34m{itens[2]}\033[m! Você venceu!")
    else:
        print('\033[1;31mJogada inválida\033[m')

elif c == 2:
    if j == 0:
        print(f"O computador escolheu \033[34m{itens[2]}\033[m!")
        print(f"A \033[34m{itens[2]}\033[m é quebrada pela \033[35m{itens[0]}\033[m! Você venceu!")
    elif j == 1:
        print(f"O computador escolheu \033[34m{itens[2]}\033[m!")
        print(f"A \033[34m{itens[2]}\033[m corta o \033[36m{itens[1]}\033[m! Você perdeu!")
    elif j == 2:
        print(f"O computador escolheu \033[34m{itens[2]}\033[m!")
        print(f"\033[34m{itens[2]}\033[m X \033[34m{itens[2]}\033[m! Empate!")
    else:
        print('\033[1;31mJogada inválida\033[m')
