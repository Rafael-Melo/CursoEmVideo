cidade = str(input('Digite o nome da sua cidade: ')).strip().title()

cidadelista = cidade.split()

if 'Santo' in cidadelista[0]:
    print(f'A cidade {cidade} começa com Santo.')
else:
    print(f'A cidade {cidade} não começa com Santo.')
