# O que aprendemos com while também funciona no for (continue, break, else, etc)
for i in range(10):
    if i == 2:
        print("I é 2, pulando")
        continue
    if i == 8:
        print('i é 8 seu else nao executara.')
        break
    
    for j in range(1,3):
        print(i, j)
else:
    print("for completo com sucesso.")