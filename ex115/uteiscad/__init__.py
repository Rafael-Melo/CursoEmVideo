def exibir():
    try:
        with open('cadastro.txt', 'r') as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
    except FileNotFoundError:
        print('\033[1;31mArquivo não encontrado!\033[m')
    except Exception as e:
        print(f'\033[1;31mErro: {e}\033[m')


def cadastrar(nome, idade):
    nome = str(input('Nome :')).strip().capitalize()
    while True:
        try:
            idade = int(input('Idade :'))
            with open('cadastro.txt', 'a') as arquivo:
                arquivo.write(f'{nome}, {idade}\n')
                print(f'{nome} cadastrado com sucesso!')
                break
        except (ValueError, TypeError):
            print(f'Digite um valor válido!')


def menu(opc):
    while True:
        print('-' * 40)
        print(f'\033[0;30;44m{"MENU PRINCIPAL":^40}\033[m')
        print('-' * 40)
        print("""\033[34m[1]\033[m \033[1;32mLista\033[m
\033[34m[2]\033[m \033[1;32mCadastrar\033[m
\033[34m[3]\033[m \033[1;32mSair\033[m""")
        print('-' * 40)
        try:
            opc = int(input('\033[34mSua Opção:\033[m '))
            if opc == 1:
                print('-' * 40)
                exibir()
            elif opc == 2:
                print('-' * 40)
                cadastrar(nome = '', idade = 0)
            elif opc == 3:
                print('-' * 40)
                print('Saindo do Sistema... Volte Sempre!')
                break
            elif opc > 3:
                print('-' * 40)
                print('\033[1;31mOpção inválida\033[m')
            opc = ''
        except (ValueError, TypeError):
            print('-' * 40)
            print('\033[1;31mOpção inválida\033[m')

