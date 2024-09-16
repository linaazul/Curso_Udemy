# Módulos - import, from, as e *
# https://docs.python.org/3/py-modindex.html
# inteiro - Importe nome_modulo
# Vantagens: você tem o namespace do módulo
# Desvantagens: nomes grandes

# import sys
# platform = 'A minha'
# print(sys.platform)
# print(platform)

# partes - from nome_modulo import objeto1, objeto2
# vantagens: nomes pequenos
# desvantagens: sem o nomespace do módulo.

# from sys import exit, platform
# print(platform)

# alias 1 - import nome_modulo as apelido
# import sys as s
# sys = 'alguma coisa'  # sobrescrevendo o sys
# print(sys)
# print(s.platform)

# alias 2 - frome nome_modulo import objeto as apelido
# from sys import platform as pf, exit as ex

# print(pf)

# vantagens: você pode reservar nomes para o seu código
# Desvantagens: pode ficar fora do padrão da linguagem

# má prática - from nome_módulo import *
# vantagens: importa tudo de um módulo
# desvantagens: importa TUDO de um módulo
from sys import *

print(platform)
exit()
