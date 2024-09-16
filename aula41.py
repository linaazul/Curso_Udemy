# while / else (recurso peculiar do Python)

"""while/else"""
string = 'Valor qualquer'

indice = 0

while indice < len(string):
    letra = string[indice]

    print(letra)

    indice += 1
else:
    print('Esse while tem um else por incrivel que pareça.')
print('Fora do while')