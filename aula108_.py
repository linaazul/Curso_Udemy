# Exercícios - somando duas listas
"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""

lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]
print("Solução do professor:")
lista_soma = [x + y for x, y in zip(lista_a, lista_b)]
print(lista_soma)

print("Minha solução:")
lista = list(zip(lista_a, lista_b))
lista_soma2 = []
for i, n in lista:
    lista_soma2.append(i + n)
print(lista_soma2)
