nome = str(input('Digite seu nome completo: ')).strip()

print(f'O seu nome maiúsculo é {nome.upper()}.')

print(f'O seu nome minúsculo é {nome.lower()}.')

nomej = ''.join(nome.split())
print(f'O seu nome tem {len(nomej)} letras.')

nomep = nome.split()
print(f'O seu primeiro nome é {nomep[0]} tem {len(nomep[0])} letras.')
