sal = float(input('Salário do funcionário R$'))
aumento = float(input('Porcentagem de aumento:'))
novo_sal = sal + (sal * aumento / 100)
print(f'O salário antes do aumento era de R${sal:.2f} e agora será de R${novo_sal:.2f}')
