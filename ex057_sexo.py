nome = str(input('Qual o seu nome? ')).strip().capitalize()
sexo = str(input('Qual o seu sexo? [M/F] ')).strip().upper()[0]
while sexo not in 'MF':
    print(f'{sexo} não é uma resposta válida.')
    sexo = str(input('Vamos tentar novamente. Qual o seu sexo? [M/F]')).strip().upper()[0]
if sexo == 'F':
    print(f'Olá {nome}! Prazer em conhecer a senhora.')
else:
    print(f'Olá {nome}! Prazer em conhecer o senhor.')
