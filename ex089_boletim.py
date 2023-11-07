alunos = []
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 =float(input('Nota 2: '))
    media = (n1 + n2)/2
    alunos.append([nome, [n1, n2], media])
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar in 'N':
        break
print('-=' * 25)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-=' * 25)
for i, a in enumerate(alunos):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-=' * 25)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe) '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(alunos) - 1:
        print(f'Notas de {alunos[opc][0]} são {alunos[opc][1]}')
print('<<<<<<<<<<<<<<<< VOLTE SEMPRE >>>>>>>>>>>>>>>>')
