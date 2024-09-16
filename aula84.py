# Introdução à List comprehension em Pytho
# List comprehension é uma forma simples de criar listas
# a partir de iteraveis.
# print(list(range(10)))
import pprint


def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)


lista = []


for numero in range(10):
    lista.append(numero)

lista = [
    numero * 2
    for numero in range(10)
]
print(list(range(10)))
print(lista)

print()

# Mapeamento de dados em list comprehension (map)
# o que vem na esquerda do for, é mapeamento.
# o que vem na direita do for, é filtro.
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]
p(novos_produtos)

print()

novos_produtos_maior_que_10 = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if (produto['preco'] >= 20 and produto['preco'] * 1.05 > 10)
]
p(novos_produtos_maior_que_10)
