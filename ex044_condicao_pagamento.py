loja = (' Lojas Melo ')
print(f'{loja:=^40}')
preco = float(input('Digite o preço do produto: R$'))
condicao = int(input('''Escolha a condição de pagamento:
(1) À Vista Dinheiro/Cheque;
(2) À Vista Cartão;
(3) Em 2x no Cartão;
(4) Em 3x ou mais no cartão;
'''))
if condicao == 1: # 10% de desconto
    res = preco * 0.9
    print('Você optou por pagamento à vista em dinheiro ou cheque:')
    print(f'Sua compra de R$ {preco:.2f} vai sair por R${res:.2f}.')
elif condicao == 2: # 5% de desconto
    res = preco * 0.95
    print('Você optou por pagamento à vista no cartão:')
    print(f'Sua compra de R$ {preco:.2f} vai sair por R${res:.2f}.')
elif condicao == 3: # Preço normal
    print('Você optou por pagamento parcelado em 2 vezes:')
    print(f'Sua compra de R$ {preco:.2f} em 2 parcelas de R${preco/2:.2f} vai sair por R${preco:.2f}.')
elif condicao == 4: # 20% de juros
    parcelas = int(input('Digite a quantidade de parcelas:'))
    res = preco * 1.2
    print(f'Você optou por pagamento parcelado em {parcelas} vezes:')
    print(f'Sua compra de R$ {preco:.2f} em {parcelas} parcelas de R${res/parcelas:.2f} vai sair por R${res:.2f}.')
else:
    print('Opção inválida')
