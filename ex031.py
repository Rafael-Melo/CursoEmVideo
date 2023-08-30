km = float(input('Digite quantos quilometros você vai viajar: '))

if km > 200:
    rs = km * 0.45
    print(f'Para uma viagem de {km}Km o valor é R$0,45 por quilometro e sua viagem custará R${rs:.2f}.')
else:
    rs = km * 0.50
    print(f'Para uma viagem de {km}Km o valor é R$0,50 por quilometro e sua viagem custará R${rs:.2f}.')
