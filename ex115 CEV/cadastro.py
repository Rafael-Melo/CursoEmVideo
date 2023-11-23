from sistema import *
from arquivo import *
from time import sleep
arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)
while True:
    resposta = menu(['Lista', 'Cadastrar', 'Sair'])
    if resposta == 1:
        exibir(arq)
    elif resposta == 2:
        subtitulo('CADASTRO')
        n = str(input('Nome: ')).strip().capitalize()
        i = leiaInt('Idade: ')
        cadastrar(arq, n, i)
    elif resposta == 3:
        rodape('Saindo do Sistema... Volte Sempre!')
        break
    else:
        print('\033[1;31mERRO!! Digite uma opção válida!\033[m')
    sleep(1)
