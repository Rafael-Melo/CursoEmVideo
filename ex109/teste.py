import moeda
p = float(input('Digite o preço: R$'))
a = float(input('Porcentagem de aumento: '))
d = float(input('Porcentagem de redução: '))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}.')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}.')
print(f'Aumentando {a}% temos {moeda.aumentar(p, a, True)}.')
print(f'Reduzindo {d}% temos {moeda.diminuir(p, d, True)}.')
