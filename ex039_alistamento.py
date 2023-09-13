import datetime

ano = int(input('Digite o ano de nascimento: '))

hj = datetime.date.today().year

idade = hj - ano

if idade < 18:
    print(f'Você tem {idade} anos e falta {18 - idade} anos pra se alistar.')

elif idade > 18:
    print(f'Você tem {idade} anos e está atrasado em {idade - 18} anos pra se alistar.')

else:
    print(f'Você tem {idade} anos e está na hora de se alistar.')

