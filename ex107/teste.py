import moeda
p = float(input('Digite o preço: R$'))
a = float(input('Porcentagem de aumento: '))
d = float(input('Porcentagem de redução: '))
print(f'A metade de R${p} é R${moeda.metade(p)}.')
print(f'O dobro de R${p} é R${moeda.dobro(p)}.')
print(f'Aumentando {a}% temos R${moeda.aumentar(p, a)}.')
print(f'Reduzindo {d} % temos R${moeda.diminuir(p, d)}.')
