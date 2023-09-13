sal = float(input('Digite o valor do salário: R$'))

if sal > 1250:
    aum = sal * 0.1
    saln = sal + aum
    print(f' Com aumento de 10% seu salário de R${sal:.2f} vai subir para R${saln:.2f} isso é um aumento de R${aum:.2f}.')
else:
    aum = sal * 0.15
    saln = sal + aum
    print(f' Com aumento de 15% seu salário de R${sal:.2f} vai subir para R${saln:.2f} isso é um aumento de R${aum:.2f}.')
