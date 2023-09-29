from datetime import date
atual = date.today().year
menor = 0
maior = 0
for c in range(1, 8):
    ano = int(input(f'Digite o ano de nascimento da {c}ª pessoa: '))
    if atual - ano >= 21:
        maior += 1
    else:
        menor += 1
print(f'{maior} pessoas já atingiram a maioridade')
print(f'{menor} pessoas ainda não atingiram a maioridade')
