produtos = ('Gabinete', 5000, 'Monitor', 1500, 'Teclado', 350,
            'Mouse', 250.50, 'Headset', 179.75, 'Mousepad', 20.35,
            'webcam', 100, 'impressora', 1259.90)
print('-' * 38)
print(f'{"LISTAGEM DE PREÇO":^35}')
print('-' * 38)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<26}', end=' ')
    else:
        print(f'R${produtos[pos]:>8.2f}')
print('-' * 38)
