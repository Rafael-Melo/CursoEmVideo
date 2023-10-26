aluno = {}
aluno['nome'] = str(input('Digite o nome do aluno: ')).strip()
aluno['media'] = float(input('Digite a média do aluno: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'
print('-' * 30)
for k, v in aluno.items():
    print(f'{k} = {v}')
