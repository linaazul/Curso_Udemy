# Shallow Copy vs Deep Copy em dados mutáveis Python
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
import copy #usado quando eu quero uma copia profunda.

dicionario1 = {
    'chave1': 1,
    'chave2': 2,
    'lista1': [0, 1, 2] # Nao copiam valores mutaveis como listas, por isso copia rasa
}
dicionario2 = copy.deepcopy(dicionario1)

dicionario2['chave1'] = 1000
dicionario2['lista1'][1] = 99999

print(dicionario1)
print(dicionario2)