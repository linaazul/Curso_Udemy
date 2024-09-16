# Variáveis livres + nonlocal (locals, globals)
# print(globals())
# def fora(x):
#     a = x

#     def dentro():
#         print(locals())  # Informa as variaveis locais.
#         return a

#     return dentro


# dentro1 = fora(10)
# dentro2 = fora(5)

# print(dentro1())
# print(dentro2())

def concatenar(string_inicial):
    valor_final = string_inicial

    def interna(valor_a_concatenar):
        # valor_final += valor_a_concatenar #Isso gera erro pois valor_final nao e uma variavel local
        nonlocal valor_final
        valor_final += valor_a_concatenar
        return valor_final
    return interna


c = concatenar('a')
print(c('b'))
print(c('c'))
print(c('d'))
