import requests
import json

link = 'https://meuprimeiroprojeto-db032-default-rtdb.firebaseio.com/'

#Vendas
cliente = str(input('Nome do cliente: '))
preco = int(input('Preco do produto: '))
produto = str(input('Nome do produto: '))

dados = {f'Cliente': f'{cliente}', 'Preco': f'{preco}', 'Produto': f'{produto}'}
r = requests.post(f'{link}/Vendas/.json', data=json.dumps(dados))
print(r)
print(r.text)

#Produtos
nome_produto = str(input('Nome do produto: '))
preco_produto = int(input('Preco do produto: '))
quantidade = str(input('Quantidade do produto: '))

dados = {f'Nome': f'{nome_produto}', 'Preco': f'{preco_produto}', 'Quantidade': f'{quantidade}'}
r = requests.post(f'{link}/Produtos/.json', data=json.dumps(dados))
print(r)
print(r.text)

cliente = str(input('Nome do cliente: '))
preco = int(input('Preco do produto: '))
produto = str(input('Nome do produto: '))

#Editar a venda
dados = {f'Cliente': f'{cliente}', 'Preco': f'{preco}', 'Produto': f'{produto}'}
r = requests.post(f'{link}/Vendas/-Myh0VuoUCiuMsaf3enN/.json', data=json.dumps(dados))
print(r)
print(r.text)

#Pegar as vendas ou algo especifico
requisicao = requests.get(f'{link}/Vendas/.json')
print(requisicao)
dic_requisicao = requisicao.json()
print(dic_requisicao)