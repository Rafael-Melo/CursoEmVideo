from utilidadescev import moeda, dados
p = dados.leiaDinheiro('Digite o preço: R$')
a = dados.leiaDinheiro('Porcentagem de aumento: ')
d = dados.leiaDinheiro('Porcentagem de redução: ')
moeda.resumo(p, a, d)
