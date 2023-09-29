import calendar
import datetime
ano = int(input('Qual ano você quer analisar? Coloque 0 para analizar o ano atual. '))
if ano == 0:
    ano = datetime.date.today().year 
if calendar.isleap(ano):
    print(f'{ano} é um ano bissexto.')
else:
    print(f'{ano} não é um ano bissexto.')
