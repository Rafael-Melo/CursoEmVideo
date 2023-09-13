preco = float(input('Digite o preço do produto: R$'))

condicao = int(input('''Escolha a condição de pagamento:
(1) À Vista Dinheiro/Cheque;
(2) À Vista Cartão;
(3) Em 2x no Cartão;
(4) Em 3x ou mais no cartão;
'''))

if condicao == 1: # 10% de desconto
    res = preco * 0.9
    print(res)
elif condicao == 2: # 5% de desconto
    res = preco * 0.95
    print(res)
elif condicao == 3: # Preço normal
    print(preco)
elif condicao == 4: # 20% de juros
    res = preco * 1.2
    print(res)
else:
    print('Opção inválida')
