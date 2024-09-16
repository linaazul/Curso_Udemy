# Manipulando chaves e valores em dicionários em Python
pessoa = {}

## 


chave = 'nome' #chave dinamica

pessoa[chave] = 'Adrio'
pessoa['sobrenome'] = 'Evangelista'

print(pessoa[chave])

pessoa[chave] = 'maria'

del pessoa['sobrenome']
print(pessoa)
print(pessoa['nome'])

if pessoa.get('sobrenome') is None:
    print('Não existe')
else:
    print(pessoa['sobrenome'])