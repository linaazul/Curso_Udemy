# Argumentos nomeados e argumentos posicionais (não nomeados) em funções
"""
Argumentos nomeados e argumentos não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento nao nomeado recebe apenas o valor
"""

def soma(x, y):
    print(f"{x=}, {y=}, {x + y}")

soma(3, 5) # argumentos posicionais

soma(y=3, x=5) # argumentos nomeados