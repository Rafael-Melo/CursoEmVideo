import requests
try:
    response = requests.get("http://pudim.com.br/")
except Exception as e:
    print('Site não está acessivel no momento!')
else:
    print('Site acessado com sucesso!')
