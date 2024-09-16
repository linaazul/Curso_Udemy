# Recarregando módulos, importlib e singleton
# Uma biblioteca que tem como uma de suas funções poder recarregar o módulo.
import importlib
import aula98_m

print(aula98_m.variavel)

for i in range(10):
    # Nao vai importar mais de uma vez pois o import de módulos é um singleton
    # import aula98_m
    importlib.reload(aula98_m)

print('fim')
