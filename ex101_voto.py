from datetime import date

def voto(ano):
    idade = date.today().year - ano
    return idade


# Programa Principal
nasc = int(input('Em que ano você nasceu? '))
if voto(nasc) < 16:
    print(f'Com {voto(nasc)} anos não vota!')
elif voto(nasc) >= 16 and voto(nasc) < 18:
    print(f'Com {voto(nasc)} anos o voto é opcional')
elif voto(nasc) >= 18 and voto(nasc) < 65:
    print(f'Com {voto(nasc)} anos o voto é obrigatório')
else:
    print(f'Com {voto(nasc)} anos o voto é opcional')
