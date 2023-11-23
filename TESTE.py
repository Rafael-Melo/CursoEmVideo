def cadastrar(nome, idade):
    with open('cadastro.txt', 'a') as arquivo:
        arquivo.write(f'{nome}, {idade}\n')


n = str(input('Nome: '))
i = int(input('Idade: '))
cadastrar(n, i)
