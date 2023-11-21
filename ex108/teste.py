import moeda
p = float(input('Digite o preço: R$'))
a = float(input('Porcentagem de aumento: '))
d = float(input('Porcentagem de redução: '))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}.')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}.')
print(f'Aumentando {a}% temos {moeda.moeda(moeda.aumentar(p, a))}.')
print(f'Reduzindo {d}% temos {moeda.moeda(moeda.diminuir(p, d))}.')
