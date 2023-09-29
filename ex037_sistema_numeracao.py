n = int(input('Digite um número '))
conv = str(input('Digite B para converter para BINÁRIO. O para OCTAL. Ou H para HEXADECIMAL. ')).strip()
if conv.upper() == 'B':
    binario = bin(n)
    print(f'O decimal {n} em binário é {binario[2:]}.')
elif conv.upper() == 'O':
    octal = oct(n)
    print(f'O decimal {n} em octal é {octal[2:]}.') 
elif conv.upper() == 'H':
    hexadecimal = hex(n)
    print(f'O decimal {n} em hexadecimal é {hexadecimal[2:]}.')
else:
    print('Error: Invalid')
