pessoa = {}
cadastro = []
mulheres = []
somaidade = 0
while True:
    pessoa. clear()
    pessoa['nome'] = str(input('Nome: ')).strip()
    pessoa['sexo'] = ' '
    while pessoa['sexo'] not in 'MF':
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
    pessoa['idade'] = int(input('Idade: '))
    cadastro.append(pessoa.copy())
    somaidade += pessoa['idade']
    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa.copy())
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar in 'N':
        break
print('-=' * 30)
print(cadastro)
print('-=' * 30)
print(f'A) {len(cadastro)} pessoas foram cadastradas.')
print('B) As mulheres cadastradas foram: ', end='')
for p in cadastro:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end=' ')
print()
print(f'C) A média de idade é de {somaidade / len(cadastro)} anos.')
print(f'D) Lista das pessoas que estão acima da média: ')
for p in cadastro:
    if p['idade'] > somaidade / len(cadastro):
        print('    ', end=' ')
        for k, v in p.items():
            print(f'{k} = {v};', end=' ')
        print()
print('<<<<<< EENCERRADO >>>>>>')
