# Funções recursivas, recursividade e Stack Overflow
# Funções recursivas - que podem se chamar de volta
# - úteis para dividir problemas grandes em partes maiores.
# TODA FUNÇÃO RECURSIVA DEVE TER:
# - Um problema que possa ser divido em partes menores
# - Um caso base que para a recursão
# - Fatorial - n! =5! = 5 * 4 * 3 * 2 * 1 = 120
# import sys
# # não recomendado
# sys.setrecursionlimit(1004)


# def recursiva(inicio=0, fim=10):
#     print(inicio, fim)
#     # caso base
#     if inicio == fim:
#         return fim
#     # caso recursivo
#     # contar até chegar ao final
#     inicio += 1
#     return recursiva(inicio, fim)


# # recursiva(0,1000) passa o limite do stack
# print(recursiva(0, 1000))

def factorial(n):
    if n <= 1:
        return 1

    return n * factorial(n-1)


print(factorial(5))
print(factorial(10))
