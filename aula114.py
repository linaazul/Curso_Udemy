# Funções recursivas, recursividade e Stack Overflow
# Funções recursivas - que podem se chamar de volta
# - úteis para dividir problemas grandes em partes maiores.
# TODA FUNÇÃO RECURSIVA DEVE TER:
# - Um problema que possa ser divido em partes menores
# - Um caso base que para a recursão
# - Fatorial - n! =5! = 5 * 4 * 3 * 2 * 1 = 120

def recursiva(inicio=0, fim=10):
    print(inicio, fim)
    # caso base
    if inicio == fim:
        return fim
    # caso recursivo
    # contar até chegar ao final
    inicio += 1
    return recursiva(inicio, fim)


print(recursiva(0, 4))
