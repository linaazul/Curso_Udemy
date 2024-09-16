# (Parte 1) Métodos úteis nos dicionários Python (dict)
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe

pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
}

print(len(pessoa))

print(list(pessoa.keys()))
print(list(pessoa.values()))
print(list(pessoa.items()))
pessoa.setdefault('idade', 10)
print(pessoa['idade'])

for chave, valor in pessoa.items():
    print(chave, valor)