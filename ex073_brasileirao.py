times = ('Botafogo', 'Bragantino', 'Grêmio', 'Palmeiras', 'Flamengo',
         'Fortaleza', 'Fluminense', 'Athletico-PR', 'Atlético-MG',
         'São Paulo', 'Cuiabá', 'Internacional', 'Corinthians', 'Santos',
         'Cruzeiro', 'Bahia', 'Vasco da Gama', 'Goiás', 'Coritiba',
         'América-MG')
print(f'{"BRASILEIRÃO 2023":^80}')
print('-' * 80)
print(f'Lista de times do Brasileirão: {times}')
print('-' * 80)
print(f'Os cinco primeiros colocados são {times[0:5]}')
print('-' * 80)
print(f'Os times que estão no Z4 são {times[-4:]}')
print('-' * 80)
print(f'Lista dos times em ordem alfabética: {sorted(times)}')
print('-' * 80)
print(f'O são Paulo está na {times.index("São Paulo")+1}ª posição')
print('-' * 80)
