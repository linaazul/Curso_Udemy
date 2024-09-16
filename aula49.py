# Cuidados com tipos de dados mutáveis - list e copy
"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
# nome = 'Adriel'
# outra_variavel = nome
# nome = 'João'
# print(nome)
# print(outra_variavel)

lista_a = ['Luiz', 'Maria']
lista_b = lista_a
lista_a[0] = 'Adriel'
print(lista_b)

lista_a = ['Luiz', 'Maria']
lista_b = lista_a.copy()
lista_a[0] = 'Adriel'
print(lista_b)
print(lista_a)
