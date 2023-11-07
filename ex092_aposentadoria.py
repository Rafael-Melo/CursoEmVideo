from datetime import date
cadastro = {}
cadastro['nome'] = str(input('Digite o nome: ')).strip()
nascimento = int(input('Digite o ano de nascimento: '))
cadastro['idade'] = date.today().year - nascimento
cadastro['ctps'] = int(input('Digite o número da carteira de trabalho: ')) 
if cadastro['ctps'] != 0:
    cadastro['contratacao'] = int(input('Digite o ano de contratação: '))
    cadastro['salario'] = float(input('Digite o salário: '))
    cadastro['aposentar'] = (cadastro['contratacao'] + 35) - nascimento
print('-' * 50)
for k, v in cadastro.items():
    print(f'- {k}: {v}')
