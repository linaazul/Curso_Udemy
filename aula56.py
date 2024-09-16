# split, join e strip são métodos muito úteis da str
"""
split e join com list e str
split - divide uma string em determinado caracter (list)
join - une uma string
strip - corta os espaço do começo e do fim da minha string.
lstrip - mesma coisa so que na esquerda
rstrip - mesma coisa so que na direita
"""

frase = 'Olha só, que coisa interessante'

lista_frases_crua = frase.split(',')
lista_frases_corrigida = []

for i, frase in enumerate(lista_frases_crua):
    lista_frases_corrigida.append(lista_frases_crua[i].strip())

# print(lista_frases_crua)
# print(lista_frases_corrigida)

frases_unidas = '*'.join(lista_frases_corrigida)
print(frases_unidas)