print('\033[1;30;45mOlá, mundo!\033[m')
print('\033[7;30mHello Word!\033[m')

a = 3
b = 5
print(f'Os valores são \033[1;32m{a}\033[m e \033[1;31m{b}\033[m.')

cores = {
        'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'interte': '\033[7;30m'
}

nome = "Rafa"

print(f"Muito prazer em te conhecer, {cores['azul']}{nome}{cores['limpa']}!!!")

