casa = float(input('Digite o valor da casa: '))

sal = float(input('Digite o valor do salário: '))

ano = float(input('Digite a quantidade de anos em que vai pagar: '))

prest = casa/(ano*12)

print(prest)

if prest < sal *0.3:
    print(f'Autorizado! A prestação de uma casa de R${casa:.2f} é de R${prest:.2f} e não vai exceder 30% do seu salário.')
else:
    print(f'Negado! A prestação de uma casa de R${casa:.2f} é de R${prest:.2f} e vai exceder 30% do seu salário.')
