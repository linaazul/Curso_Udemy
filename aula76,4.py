# (Parte 2) Métodos úteis nos dicionários Python (dict)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
pessoa = {
    'nome': 'Adriel',
    'sobrenome': 'Marques',
}
# print(pessoa.get('nome'))
# print(pessoa.get('nome', 'Nao existe')) #Pega o nome se ele existir, se nao usa o nao existe

# nome = pessoa.pop('nome')
# print(nome)
# print(pessoa)

# ultima_chave = pessoa.popitem()
# print(ultima_chave)
# print(pessoa)
# pessoa.update({
#     'nome': 'Adriooo',
#     'idade': 23
# })
# pessoa.update(nome = 'Adrio', idade = 23)
atualizando_com_tupla = ('nome', 'Adrielzinho'), ('idade', 23)
atualizando_com_lista = [['nome', 'Adrielzinho'], ['idade', 23]]
pessoa.update(atualizando_com_lista)
print(pessoa)
