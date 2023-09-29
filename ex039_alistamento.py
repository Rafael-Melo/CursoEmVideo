from datetime import date
sexo = str(input('Qual seu sexo? (M) Masculino / (F) Feminino: ')).strip()
if sexo.upper() == 'F':
    print('Você não precisa se alistar.')
elif sexo.upper() == 'M':
    ano = int(input('Digite o ano de nascimento: '))
    hj = date.today().year
    idade = hj - ano
    if idade < 18:
        saldo = 18 - idade
        print(f'Você tem {idade} anos e falta {saldo} anos pra se alistar.')
        print(f'Você deverá se alistar em {hj + saldo}.')
    elif idade > 18:
        saldo = idade - 18
        print(f'Você tem {idade} anos e está atrasado em {saldo} anos pra se alistar.')
        print(f'Seu alistamento foi em {hj - saldo}.')
    else:
        print(f'Você tem {idade} anos e está na hora de se alistar.')
else:
    print()