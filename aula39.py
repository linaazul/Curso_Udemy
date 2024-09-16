#  Exercício guiado com while

nome = 'Luiz Otávio'
len_nome = len(nome)
indice = 0
nova_string = ''

while indice < len_nome:
    nova_string += f'*{nome[indice]}'
    indice += 1

print(nova_string)
