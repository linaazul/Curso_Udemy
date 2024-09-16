# Modularização - Entendendo os seus próprios módulos e sys.path no Python
# O primeiro módulo executado chama-se __main__
# O python conhece a pasta onde o __main__ está e as pastas abaixo dele
# Ele não reconhece as pastas e módulos acima do __main__ por padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path.

import aula97_m

print('Este módulo se chama', __name__)
print(aula97_m.variavel_modulo)
print(aula97_m.soma(2, 3))
