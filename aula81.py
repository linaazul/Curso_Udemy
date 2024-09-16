# Introdução à função lambda + list.sort e sorted
# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.
# lista = [
#     {'nome': 'Luiz', 'sobrenome': 'miranda'},
#     {'nome': 'Maria', 'sobrenome': 'Oliveira'},
#     {'nome': 'Daniel', 'sobrenome': 'Silva'},
#     {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
#     {'nome': 'Aline', 'sobrenome': 'Souza'},
# ]

# lista = [4, 32, 1, 34, 5, 6, 6, 21]
# lista.sort(reverse=True)
# # sorted(lista) # faz uma copia rasa e cria uma nova lista ordenada
# print(lista)

lista = [
    {'nome': 'Luiz', 'sobrenome': 'Miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]


# def ordenar_lista(item):
#     return item['nome']

def exibir_lista(lista):
    for item in lista:
        print(item)
    print()

# lista.sort(key=lambda item: item['nome'])


lista1 = sorted(lista, key=lambda item: item['nome'])
lista.sort(key=lambda item: item['nome'])
lista2 = sorted(lista, key=lambda item: item['sobrenome'])

exibir_lista(lista1)
exibir_lista(lista)
exibir_lista(lista2)
