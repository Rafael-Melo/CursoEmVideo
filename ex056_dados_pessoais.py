idade_soma = 0
ultima_idade = 0
velho =''
mulheres = 0

for c in range(1, 5):
    print(f'----- {c}ª PESSOA -----')
    nome = str(input('Digite o nome: ')).strip()
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo (M) masculino ou (F) feminino : ')).upper()
    idade_soma += idade
    if sexo == 'M':
        if idade > ultima_idade:
            ultima_idade = idade
            velho = nome
    elif sexo == 'F': 
        if idade < 20:
            mulheres +=1

media = idade_soma/4

print(f'A média de idade do grupo é {media} anos.')
print(f'O homem mais velho é o {velho} com {ultima_idade} anos.')
print(f'Tem {mulheres} mulheres com menos de 20 anos.')
