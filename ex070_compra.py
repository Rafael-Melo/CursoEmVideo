total = maisdemil = menor = cont = 0
barato = ''
while True:
    nome = str(input('Digite o nome do produto: ')).strip()
    preco = float(input('Digite o preço do produto R$ '))
    total += preco
    cont += 1
    if preco > 1000:
        maisdemil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = nome
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar comprando?[S/N}] ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f"""Você comprou {cont} itens num total de R${total:.2f}.
{maisdemil} desses itens custaram mais de R$1000.00.
E o item mais bararto foi {barato} custando R${menor:.2f}.
""")
