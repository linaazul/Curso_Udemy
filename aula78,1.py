# Peculiaridades do tipo mutável set em Python
# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)
# lista1 = [1, 2, 3, 3, 3, 3, 3, 1]
# s1 = set(lista1)
# lista2 = list(s1)
s1 = set('Luiz')
s1 = {1, 2, 3}
print(s1)

for numero in s1:
    print(numero)
