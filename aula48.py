# Tipo list - Introdução às listas mutáveis em Python
"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

string = 'ABCDE'
lista = [123, True, 'NOME', 1.2, []] 
# print(bool(lista)) # Falsy
# print(lista, type(lista))
lista[2] = 'tome'
print(lista) 
print(lista[2], type(lista[2]))

# Alterando uma lista com índices, del, append e pop (Tipo list)
lista = [10, 20, 30, 40]
# lista[2] = 300
# del lista[2]  # deleta um item da lista
# print(lista)
# print(lista[2])
lista.append(50)  # Adiciona um item no fim da lista
lista.pop()  # remove o ultimo item da lista
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop(3)
print(lista)
print('Removido:', ultimo_valor)


# Inserindo itens em qualquer índice da lista com insert (Tipo list)
lista = [10, 20, 30, 40]
lista.append('Luiz')
nome = lista.pop()
lista.append(1233)
del lista[-1]
# lista.clear()
lista.insert(100, 5)
print(lista)

# Concatenando e estendendo listas em Python
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b)
print(lista_a)