# Retorno de valores das funções (return)
# variavel = print('Ana')
# print(variavel) # retorna None.

def soma(x, y):
    print(f'{x=} {y=}')
    if x > 10:
        return 10, 20
    return x + y

# variavel = soma(1, 2)
# variavel = int('1')
soma1 = soma(2, 2)
soma2 = soma(3, 3)
print(soma1)
print(soma2)
print(soma(11,55))


