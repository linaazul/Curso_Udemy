# Valores padrão para parâmetros em funções Python + NoneType e None
"""
valores padrao para parametros
ao definir uma funcao, os parametros 
podem ter valor padrao.caso o valor 
nao seja enviado para o parametro, 
o valor padrao sera usado.
refatorar = editar o seu codigo.
"""

def soma(x, y, z = None):
    if z is not None:
        print(f'{x=}, {y=}, {z=}, x + y + z = {x + y + z}')
    else:
        print(f'{x=}, {y=}, x + y = {x + y}')

soma(1, 2)
soma(3, 5)
soma(100, 200)
soma(8, 9, 3)
