from random import randint
from time import sleep
cont = 1
jogo = {'jogador1': randint(1,6),
        'jogador2': randint(1,6),
        'jogador3': randint(1,6),
        'jogador4': randint(1,6)}
itens_ordenados = sorted(jogo.items(), key=lambda item: item[1], reverse=True)
jogo_ordenado = dict(itens_ordenados)
print('VALORES SORTEADOS:')
for j, d in jogo.items():
    print(f'O {j} tirou {d}')
    sleep(1)
print('-=' * 30)
print('RANKING DOS JOGADORES:')
for j, d in jogo_ordenado.items():
    print(f'{cont}º Lugar: {j} com {d} pontos')
    cont += 1
    sleep(1)
