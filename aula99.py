# import sys

# # varias formas de importar
# import aula99_package.modulo
# from aula99_package.modulo import soma_do_modulo
# print(soma_do_modulo(1, 2))
# print(aula99_package.modulo.soma_do_modulo(1, 2))

# # print(*sys.path, sep='\n')

# from aula99_package.modulo import soma_do_modulo, fala_oi

# print(__name__)
# fala_oi()

from aula99_package import soma_do_modulo, fala_oi

fala_oi()
print(soma_do_modulo(2, 3))
