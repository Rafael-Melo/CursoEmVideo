jogador = {}
time = []
gols = []
total = 0
while True:
    jogador.clear()
    gols.clear()
    jogador['nome'] = str(input('Nome do jogador: ')).strip()
    jogos = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for i in range(0, jogos):
        gols.append(int(input(f'    Quantos gols na partida {i+1}? ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    time.append(jogador.copy())
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar in 'N':
        break
print('-=' * 30)
print('cod', end=' ')
for i in jogador.keys():
    print(f'{i:<15}', end=' ')
print()
print('-' * 30)
for k, v in enumerate(time):
    print(f'{k:>3} ', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end=' ')
    print()
print('-=' * 30)
for j in time:
    print(f'    => O jogador {j["nome"]} jogou {len(j["gols"])} partidas.')
print('-=' * 30)

while True:
    opc = int(input('Mostrar dados de qual jogador? '))
    if opc == 999:
        break
    if opc >= len(time):
        print(f'Erro não existe jogador com o código {opc}!')
    else:
        print(f'-- Levantamento do jogador {time[opc]["nome"]}:')
        for i, g in enumerate(time[opc]["gols"]):
            print(f'    => Na partida {i+1}, fez {g} gols.')
    print('-=' * 30)
print('<<< VOLTE SEMPRE >>>')
