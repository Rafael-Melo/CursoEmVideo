jogador = {}
gols = []
total = 0
jogador['nome'] = str(input('Nome do jogador: ')).strip()
jogos = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for i in range(0, jogos):
    gols.append(int(input(f'Quantos gols na partida {i+1}? ')))
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, g in enumerate(jogador["gols"]):
    print(f'    => Na partida {i+1}, fez {g} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
