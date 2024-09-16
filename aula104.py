# Decoradores em Python (@syntax_sugar)
# Decorar = Adicionar / remover / restringir / alterar
# Funções decoradas são funções que decoram outras funções
# Decoradores são usados para fazer o python usar as funções decoradas em outras funções
# Decoradores são "Syntax Sugar" (Açucar sintático)

def criar_funcao(funcao):
    def interna(*args, **kwargs):
        for arg in args:
            is_string(arg)
        resultado = funcao(*args, **kwargs)
        resultado += ' uarevá'  # alterando o resultado
        return resultado
    return interna


@criar_funcao
def inverte_string(string):
    print(f'{inverte_string.__name__}')
    return string[::-1]


def is_string(parametro):
    if not isinstance(parametro, str):
        raise TypeError('Parametro deve ser uma string.')


invertida = inverte_string('123')
print(invertida)
