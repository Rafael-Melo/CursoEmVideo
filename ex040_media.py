
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

media = (n1 + n2) / 2

if media < 5:
    print(f'A nota é {media}, o aluno está reprovado.')
elif media > 5.9:
    print(f'A nota é {media}, o aluno está em aprovado.')
else:
    print(f'A nota é {media}, o aluno está em recuperação.')
