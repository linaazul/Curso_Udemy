# Funções decoradoras em geral
# Decorar = Adicionar / remover / restringir / alterar
# Funções decoradas são funções que decoram outras funções
# Decoradores são usados para fazer o python usar as funções decoradas em outras funções


# Função decoradora
def criar_funcao(funcao):
    def interna(*args, **kwargs):
        for arg in args:
            is_string(arg)
        resultado = funcao(*args, **kwargs)
        return resultado
    return interna


# Função decorada
def inverte_string(string):
    return string[::-1]


def is_string(parametro):
    if not isinstance(parametro, str):
        raise TypeError('Parametro deve ser uma string.')


inverte_string_checando_parametro = criar_funcao(inverte_string)
invertida = inverte_string_checando_parametro('123')
print(invertida)
