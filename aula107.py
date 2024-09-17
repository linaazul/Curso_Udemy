# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

from itertools import zip_longest


lista1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista2 = ['BA', 'SP', 'MG', 'RJ']

dicionario = {
    # o range pega o tamanho da menor lista
    lista1[i]: lista2[i] for i in range(len(lista1))
}

print("Meu resultado:")
print(dicionario)
print()

# solução do professor


def zipper(lista1, lista2):
    interavalo_maximo = min(len(lista1), len(lista2))
    return [
        (lista1[i], lista2[i]) for i in range(interavalo_maximo)
    ]


l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']

print("Solução do professor sem função do python:")
print(zipper(l1, l2))
print()

# Função pronta, feita pelo python

print("Solução do professor com função do python:")
print(list(zip(l1, l2)))
print()

# Para utilizar o valor da lista maior, o python tem uma outra função que precisa ser importada
# from itertools import zip_longest

print("Solução do professor com função do python pegando a maior lista:")
print(list(zip_longest(l1, l2)))
print()
