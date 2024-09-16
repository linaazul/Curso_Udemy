# Higher Order Functions - Funções de primeira classe

def saudacao(msg, nome):
    return f'{msg}, {nome}!'

def executar_funcao(funcao, *args):
    return funcao(*args)


# saudacao_2 = saudacao #referenciando a funcao, nao executando
print(executar_funcao(saudacao, 'BOM DIA', 'Adriel'))

# variavel = saudacao('bom dia')
# print(variavel)
