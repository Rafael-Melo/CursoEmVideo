def voto(ano):
    from datetime import date
    idade = date.today().year - ano      
    if idade < 16:
        return f'Com {idade} anos não vota!'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos o voto é opcional'
    else:
        return f'Com {idade} anos o voto é obrigatório'


# Programa Principal
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
