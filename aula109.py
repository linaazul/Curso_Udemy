# 174. Combinations, Permutations e Product - Itertools

# Combinations, Permutations e Product - Itertools
# Combinação - ordem não importa - iterável - tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos
from itertools import combinations, permutations, product


def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia',
]
camisetas = [
    ['roxo', 'azul',],
    ['p', 'm', 'g'],
    ['masculinas', 'femininas', 'unisex'],
    ['algodão', 'poliéster']
]

# combinations
print_iter(combinations(pessoas, 2))
print_iter(combinations(pessoas, 3))

# permutations
print_iter(permutations(pessoas, 2))

# products
print_iter(product(*camisetas))
