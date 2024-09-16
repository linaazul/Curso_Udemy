# Listas dentro de listas (iteráveis dentro de iteráveis)
# listas de listas e seus indices

salas_de_aula = [
    ['Maria', 'Helena'],
    ['Elaine'],
    ['Luiz', 'João', 'Eduarda']
]

# print(salas_de_aula[1][0])
# print(salas_de_aula[0][1])
# print(salas_de_aula[2][2])
# print(salas_de_aula[2][3][2])

for sala in salas_de_aula:
    print('sala:')
    for alunos in sala:
        print(alunos)