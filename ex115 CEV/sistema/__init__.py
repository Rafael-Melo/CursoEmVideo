def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(f'\033[0;30;44m{txt:^42}\033[m')
    print(linha())


def subtitulo(txt):
    print(linha())
    print(f'{txt:^42}')
    print(linha())


def rodape(txt):
    print(linha())
    print(f'\033[0;33;40m{txt:^42}\033[m')
    print(linha())


def leiaInt(valor):
    while True:
        try:
            numero = int(input(valor))
        except (ValueError, TypeError):
            print('\033[1;31mERRO!! Digite um número inteiro válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[1;31mO usuário não digitou um valor!\033[m')
            return 0
        else:
            return numero


def menu(list):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for i in list:
        print(f'\033[34m{c}\033[m - \033[1;32m{i}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[34mSua Opção: \033[m')
    return opc

