import datetime
ano = int(input('Digite o ano: '))
hj = datetime.date.today().year
idade = hj - ano
if idade > 20:
    print(f'A idade é {idade} e ele está na categoria \033[1;32mMASTER\033[m.')
elif idade > 19:
    print(f'A idade é {idade} e ele está na categoria \033[1;33mSENIOR\033[m.')
elif idade > 14:
    print(f'A idade é {idade} e ele está na categoria \033[1;34mJUNIOR\033[m.')
elif idade > 9:
    print(f'A idade é {idade} e ele está na categoria \033[1;35mINFANTIL\033[m.')
else:
    print(f'A idade é {idade} e ele está na categoria \033[1;36mMIRIM\033[m.') 
