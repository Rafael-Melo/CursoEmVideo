dias = int(input('Quantos dias ficou com o carro?\n'))
km = float(input('Quantos quilômetros rodou com o carro?\n'))
preco = (dias * 60) + (km * 0.15)
print(f'O valor do aluguel do carro por {dias} dias e {km}Km ficará em R${preco:.2f}.')
