# 162. Exercício - Adiando execução de funções
def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y


def criar_funcao(funcao, *args):
    def funcao_com_y(y):
        return funcao(*args, y)
    return funcao_com_y


soma_com_5 = criar_funcao(soma, 5)
multiplicacao_com_10 = criar_funcao(multiplica, 10)

print(soma_com_5(10))
print(multiplicacao_com_10(10))
